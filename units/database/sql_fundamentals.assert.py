#!/usr/bin/env python3
"""sql_fundamentals 卡断言脚本 —— 校验 demo 的关键结论都出现在输出里。

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
    ("建表", "[[OK]] 表结构创建完成：departments / employees / projects"),
    ("建索引", "[[OK]] 索引创建完成：idx_emp_dept / idx_proj_emp"),
    ("示例数据", "[[OK]] 示例数据插入完成（3 部门、6 员工、6 项目）"),
    ("SELECT 段", "═══ 1. SELECT 基础 ═══"),
    ("查询结果", "员工 101: 张三，薪资 25000"),
    ("INNER JOIN 段", "═══ 2. INNER JOIN ═══"),
    ("LEFT JOIN 段", "═══ LEFT JOIN（含无项目的员工）═══"),
    ("聚合段", "═══ 3. 聚合查询 ═══"),
    ("子查询段", "═══ 4. 子查询 ═══"),
    ("索引对比段", "═══ 5. 索引效果对比 ═══"),
    ("演示跑完", "所有演示完成。"),
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
    failed = []
    for name, needle in CHECKS:
        if needle not in out:
            failed.append(name + "（缺少：" + needle + "）")
    if proc.returncode != 0:
        failed.append("demo 退出码非 0：" + str(proc.returncode))
        failed.append("demo 的 stderr 末尾：" + decode(proc.stderr)[-500:])
    if failed:
        for item in failed:
            print("断言失败：" + item)
        return 1
    print("全部断言通过（%d 条）" % len(CHECKS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
