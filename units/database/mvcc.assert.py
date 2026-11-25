#!/usr/bin/env python3
"""mvcc 卡断言脚本 —— 校验 demo 的关键结论都出现在输出里。

用法：
  1) 直接跑：把本脚本与 demo 的 main.py 放在同一目录（沙箱副本）。
  2) 指定 demo：环境变量 STUDY_HUB_DEMO 指向 demo 的绝对路径。
全部断言通过 → exit 0；任一条不通过 → 打印失败原因并 exit 1。

编码：demo 的 stdout 按**本机 locale** 编码（Windows 中文环境是 GBK，Linux 是 UTF-8），
所以这里抓字节再按 utf-8 → gbk → latin-1 的顺序试解码，不写死编码。
"""

import os
import shutil
import subprocess
import sys
import tempfile

DEMO = os.environ.get("STUDY_HUB_DEMO") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "main.py"
)

# (说明, 在 stdout 里必须出现的片段)
CHECKS = [
    ("建表", "[[OK]] 表已创建"),
    ("版本链", "═══ 1. 版本链（Version Chain） ═══"),
    ("快照隔离", "═══ 2. ReadView 与快照隔离（Snapshot Isolation） ═══"),
    ("写写冲突", "═══ 3. MVCC 写写冲突 ═══"),
    ("最终余额", "2000 - 100 + 200 = 2100 [OK]"),
    ("演示跑完", "所有 MVCC 演示完成。"),
    # 变异测试会改坏第 102 行的 `if bal1 == bal2:`（改成 if False）：
    # demo 于是永远走 else 分支，输出「读到了新数据（非快照隔离）」。
    #
    # ⚠️ **不能**把 else 分支那句话写成「必须出现」的断言：
    #    正常 demo 只打印 if 那一支，两条分支互斥 —— 同时要求两句必然失败。
    # ⚠️ **也不能断言两次读的具体余额数值**：
    #    demo 的 Writer/Reader 是两个线程，谁先跑没有保证；Writer 先提交时
    #    两次读都是 5000.0（仍然快照一致），写死 800.0 会变成偶发失败。
    #
    # 所以这里只盯**分支结论那句话**，再在 main() 里做一次反向检查
    # （出现「非快照隔离」就判失败）—— 两者合起来等价于盯住那个 if。
    ("快照隔离分支", "→ 快照隔离！Reader 看到的是事务开始时的快照"),
    # 版本链那一段的具体数值：被改坏 balance 时会变
    ("版本链初始值", "balance=1000, version=1"),
    ("版本链改后值", "balance=800.0, version=2"),
    # 写写冲突那一段的具体结论
    ("写写冲突结论", "MVCC + 行锁：写操作序列化，读操作无阻塞"),
]


def decode(raw):
    """把字节流解成文本：utf-8 → gbk → latin-1 依次试。"""
    for enc in ("utf-8", "gbk"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1")


def run_demo():
    """把 demo 复制进临时目录再跑。

    为什么要复制：有的 demo（mvcc / transaction）会在 __file__ 旁边写 .db 文件，而且不能重复跑。
    复制进临时目录，既保证每次都是干净环境，也保证 .db 不落进 learning 仓。
    """
    if not os.path.exists(DEMO):
        return None, "找不到 demo：" + DEMO
    sandbox = tempfile.mkdtemp(prefix="study-hub-assert-")
    try:
        target = os.path.join(sandbox, os.path.basename(DEMO))
        shutil.copy2(DEMO, target)
        proc = subprocess.run(
            [sys.executable, target],
            capture_output=True,
            timeout=180,
        )
        return proc, None
    finally:
        shutil.rmtree(sandbox, ignore_errors=True)


def main():
    proc, err = run_demo()
    if err is not None:
        print(err)
        return 1
    out = decode(proc.stdout)
    # demo 的输出回显出来：单元页右栏要给用户看「demo 到底打印了什么」。
    # 不回显的话，demo 的 stdout 被 capture_output 吞掉，界面只能看到断言结果，
    # 看不到 demo 自己的输出。回显的是**解码后的文本**，不是原始字节。
    print("─── demo 输出开始 ───")
    print(out.rstrip())
    print("─── demo 输出结束 ───")
    failed = []
    # 反向检查：正常 demo 走 if 分支，不该出现 else 分支那句话。
    # 变异把 `if bal1 == bal2:` 改成 `if False:` 之后才会出现 ——
    # 正向断言抓不住这个，所以单独查一遍。
    if "读到了新数据（非快照隔离）" in out:
        failed.append("走了非快照隔离分支：if bal1 == bal2 被改坏，快照隔离没生效")
    for name, needle in CHECKS:
        if needle not in out:
            failed.append(name + "（缺少：" + needle + "）")
    if proc.returncode != 0:
        failed.append("demo 退出码非 0：" + str(proc.returncode))
        failed.append("demo 的 stderr 末尾：" + decode(proc.stderr)[-500:])
    if failed:
        for item in failed:
            print("断言失败：" + item)
        # demo 的错误输出走 **stderr**：判题链路（契约 §7.4）靠 stderr 判定
        # 「环境缺失」「崩了」这两类 verdict。demo 的 stderr 被脚本 capture 住了，
        # 不转发到脚本自己的 stderr，numpy 缺失这类问题就判不出来。
        print("─── demo 错误输出开始 ───", file=sys.stderr)
        print(decode(proc.stderr).rstrip(), file=sys.stderr)
        print("─── demo 错误输出结束 ───", file=sys.stderr)
        return 1
    print("全部断言通过（%d 条）" % len(CHECKS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
