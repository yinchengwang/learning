# Learning Track

学习轨道 —— **学习仓**（`yinchengwang/learning`）。Obsidian 笔记、课程进度、脚手架工程、算法题解、鸿蒙 ArkTS、面试资料。

本仓是 StillEvolving 四仓聚合中的学习仓：学习笔记、课程进度、算法题解、Obsidian vault，以及**学习轨的 openspec spec**（2026-10-26 从 projects 迁入本仓 `openspec/specs/`）。

## 仓库定位

| 项 | 值 |
|---|---|
| 上游 | `https://github.com/yinchengwang/learning.git` |
| 获取方式 | StillEvolving 父仓的 submodule（`git submodule update --init learning`） |
| 在聚合树中的位置 | `StillEvolving/learning/` |
| 角色 | 学习仓（笔记 + 脚手架 + 题解 + 进度） |
| 顶层目录 | 18 个（见下方「Canonical 内容」） |

四仓关系的权威定义在父仓：

| 文件 | 作用 |
|---|---|
| [`../repos.yaml`](../repos.yaml) | 机器可读的四仓清单 —— 唯一权威的「关系」定义（URL / 角色 / 拉取策略 / `must_contain`） |
| [`../docs/architecture.md`](../docs/architecture.md) | 目录树与归属判定规则总览 |
| [`../README.md`](../README.md) | 父仓入口：四仓关系与 bootstrap |

同级仓：[`../projects/`](../projects/)（工程仓）、[`../ai-docs/`](../ai-docs/)（AI 工作文档仓）。
第三方源码镜像在**独立仓** [`../../reference/`](../../reference/)（平级但**不进** submodule 树）。

> 本仓 README 自带一份归属判定表（见文末）—— 人进到 `learning/` 里看不到父仓文档，所以每仓 README 必须自带一份。

## 构建与测试

本仓自带 CMake 入口 `CMakeLists.txt`（`project(LearningTrack 1.0.0)`，C11 / C++17），**独立于父仓构建**：`projects/CMakeLists.txt` 已移除 `LEARNING_BUILD` 分支，本仓不再由父仓统一调度。

```bash
# Configure & build —— 构建目录在本仓 build/ 下（本仓 .gitignore 已忽略 build/ 与 test-results/）
cmake -B build/learning -S . -DBUILD_TESTING=ON
cmake --build build/learning --parallel 4

# Run tests
ctest --test-dir build/learning --output-on-failure
```

作为父仓 submodule 时，把产物放到父仓的构建目录（父仓 `.gitignore` 同样已忽略 `build/`）：

```bash
cmake -B ../build/learning -S . -DBUILD_TESTING=ON
cmake --build ../build/learning --parallel 4
ctest --test-dir ../build/learning --output-on-failure
```

| 项 | 值 |
|---|---|
| 测试开关 | `option(BUILD_TESTING "Build learning tests" ON)` —— **默认 ON**；只有 ON 时才 `enable_testing()`，并挂载 `code-solutions/c/test` |
| 构建目标 | `learning_includes`（INTERFACE，暴露 `learning/include`）、`ds`、`algo-c`、`leetcode-solutions`、`interview-solutions`、`distributed-solutions`、`leetcode_tests`（测试可执行） |
| GTest | 由 `third_part/googletest` 子模块 `add_subdirectory` 进 `${CMAKE_BINARY_DIR}/_googletest_build`，无需系统安装 |
| 静态库落位 | `${CMAKE_BINARY_DIR}/lib/`（各子库的 `ARCHIVE_OUTPUT_DIRECTORY`） |
| 测试二进制落位 | ⚠️ 目前**落到源码目录**，见下方「踩坑红线」 |

## Canonical 内容

| 目录 | 说明 | 规模（实测） |
|---|---|---|
| `scaffold/` | 学习脚手架工程（R5 卡片 + 各语言练习目录） | **文件数最多的目录**：1554 文件 / 381 子目录，其中 740 篇 Markdown、231 `.c`、71 `.cpp`、97 `.py`；分 `c/ cpp/ db/ ds/ grokking/ linux/ py/ python/` 8 个子域 |
| `notes/` | Obsidian vault | 21 个子目录，**164 篇 Markdown**（149 篇笔记正文 + 15 篇索引/模板/元数据与 vault README），共 13.0 MB |
| `code-solutions/` | 算法题解（LeetCode + 面试 + 分布式实验） | `c/`（`src/c` + `src/cpp` 题解，`test/` 下 15 个测试文件）、`interview/`（22 家公司目录）、`distributed/`（`coordinator/raft/shard/dist_txn`，8 个 `.c/.h`） |
| `ds-c/orig/` | 手撕数据结构教学版（C） | 13 个数据结构子目录（array → tree）+ `bsearch.c` / `common.c` |
| `algo-c/` | 教学算法 | `bit_operations/ contest/ prefix_sum/ problems/ sliding_window/` |
| `interview/` | 面试资料 | `c_cpp/ database/ md_png/ VDB/` + 6 个备忘文件（`resume.md`、`interview.txt` 等） |
| `arkts/` | 鸿蒙 ArkTS | `arkui/`（77 个文件） |
| `exam/` | 考试认证 | `SDE/sde.md` + `png/`（3 张图） |
| `articles/` | CSDN 长文草稿 | `csdn-drafts.md`（1 篇） |
| `blog/` | 博客草稿 | 8 篇（`claude/` `DB/` `openspec/` + 3 篇散篇） |
| `playground/` | 演示 / 练习代码 | `code_C/ code_CPP/ project_Greedy_snake/ rag/` |
| `progress/` | 课程进度日志 | 9 篇 `r*-progress.md`（r25 / 26 / 30 / 32 / 33 / 35 / 36 / 37 / 38） |
| `openspec/` | **学习轨 openspec**（2026-10-26 从 projects 迁入本仓） | `specs/`（`learning/` + 12 个纯学习向 `r*` 目录）、`changes/`（空）、`archived/`（空） |
| `include/` | 学习层公共头文件 | `ds/`（34 个）、`leetcode/`（3 个）、`uthash/`（6 个 vendored 头文件，**非子模块**）、`common.h` |
| `scripts/` | 学习专用脚本 | `sync-learn-deep.sh`、`sync-pipeline.py` |
| `tools/` | 学习专用工具备忘 | 3 个 `.txt`（pycharm / vim / windo 快捷键） |
| `misc/` | 杂项学习文件 | `kanban-snapshot.md`、`learn-vdb-deepdive-check.yml`、`lines_of_code.txt` |
| `third_part/` | 第三方依赖 | **仅 `googletest/` 一个子模块**（pin `f8d7d77c`，`release-1.8.0-3335-gf8d7d77c`） |

顶层文件：`CMakeLists.txt`、`LICENSE`、`README.md`、`.gitignore`、`.gitmodules`。

## 资产归属

`learning/` 是以下内容的唯一 canonical 位置：

- Obsidian 学习笔记与索引（`notes/`）、课程进度（`progress/`）、脚手架工程（`scaffold/`）
- 算法题解与教学实现（`code-solutions/`、`ds-c/`、`algo-c/`）、面试资料（`interview/`）、鸿蒙 ArkTS（`arkts/`）
- **学习轨的 openspec spec**：`openspec/specs/learning/` 与 12 个纯学习向 `r*` 目录（2026-10-26 从 projects 迁入本仓）
- 学习专用脚本与工具（`scripts/`、`tools/`）、杂项学习文件（`misc/`）、博客与长文草稿（`blog/`、`articles/`）、认证考试资料（`exam/`）、演示代码（`playground/`）

**本仓不收**：

- 工程代码、测试、构建脚本 → [`../projects/`](../projects/)（`../projects/engine/`）
- 跨项目可复用的模板、方法论、提示词 → [`../ai-docs/`](../ai-docs/)
- 第三方源码镜像 → [`../../reference/`](../../reference/)（独立仓）

跨轨引用禁令：**本仓不得引用 `../projects/engine/` 下的工程代码**。`engineering/` 这个旧目录名已随全仓改名为 `engine/` 而失效。

---

## 什么该放这个仓

本仓是四个仓中的**学习仓**（learning）。判断一份东西该放这里、还是放 `projects` / `ai-docs` / `reference`：

| 内容 | 归属 |
|---|---|
| 学习笔记、课程进度、算法题解、Obsidian vault | learning |
| 学习轨的 openspec spec（从 projects 迁出） | learning `openspec/specs/` |
| 工程代码、测试 | projects |
| 学习中产出的**可复用**方法论、模板 | ai-docs |
| 第三方源码镜像 | reference |

**判定口诀**：换个项目还用得上 → ai-docs；只对这个项目有意义 → 留在本仓。

> 完整目录规范见父仓 [`../docs/architecture.md`](../docs/architecture.md)；机器可读版见父仓 [`../repos.yaml`](../repos.yaml) 的 `must_contain` 字段。

## 踩坑红线

- **googletest 刻意保留两份，不合并**：本仓 `third_part/googletest` 与 `../projects/vendor/third_part/googletest` 各有一份，pin 可能不同。合并需两个仓各改 `.gitmodules`，风险高于收益。
- **学习轨的 spec 已迁入本仓**：`openspec/specs/learning/` 与 12 个纯学习向 `r*` 目录在本仓，**不在** `../projects/openspec/specs/`。找学习向 spec 别再去 projects 里翻。
- **构建产物不落源码目录**：编译产物统一进 `build/<轨道>/`，测试 / 运行产物进 `test-results/<轨道>/`。
  ⚠️ 已知违规：`code-solutions/c/test/c/CMakeLists.txt` 把 `leetcode_tests` 的 `RUNTIME_OUTPUT_DIRECTORY` 指向 `${CMAKE_CURRENT_SOURCE_DIR}`（源码目录），与该规范冲突，**待修**。
- **本仓只有 `third_part/googletest` 一个子模块**。`uthash` 在本仓是 vendored 头文件（`include/uthash/`），**不是**子模块；子模块 uthash 在 `../projects/engine/third_part/uthash`，属 projects 管辖。
- **双轨守卫当前不生效**：`learning/CMakeLists.txt` 引用的 `../cmake/dual-track-guard.cmake` 在当前布局下不存在（父仓无 `cmake/` 目录），守卫被 `if(EXISTS)` 跳过。跨轨隔离靠约定，不靠构建期强制。
- **`distributed/` 有意排除三个文件**：`raft.c` / `dist_txn.c` / `shard.c` 因 phase9 实现不完整被 `code-solutions/distributed/CMakeLists.txt` 的 `list(FILTER ...)` 排除出构建，产物里不会有这三个模块。
- **`engineering/` 是失效路径**：代码目录已改名 `engine/`。唯一仍叫 `engineering` 的是 `../projects/openspec/specs/engineering/`（工程轨 spec 目录名），与旧代码目录无关。
- **禁止对 `../../reference/` 递归初始化 submodule**：reference 内部有 95 个第三方库 submodule，递归拉取约 25 GB / 53.6 万文件。需要哪个库就用父仓 [`../scripts/fetch-reference.sh`](../scripts/fetch-reference.sh) `--name <名字>` 单独拉取。
