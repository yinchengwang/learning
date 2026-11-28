# 学习 Obsidian Vault

> 164 篇 Markdown 笔记 + 6 大学习轨道 + Dataview 仪表盘

## 快速开始

1. **打开 Obsidian** → File → Open vault → 选择 `learning/notes/` 目录
2. **启用插件**：第一次打开会提示启用 community plugins（dataview、templater 等）
3. **查看总索引**：左侧 `_index/home.md`

## 目录结构

```
learning/notes/
├── .obsidian/                 # Obsidian 配置（vault 标志）
├── _index/                    # 索引页（home + 6 轨道 + 深度系列指针）
├── _templates/                # 4 类笔记模板
├── _meta/                     # 元数据（schema 文档）
├── _dashboard/                # 仪表盘（Dataview）
├── _scripts/                  # 维护脚本（Python/Bash）
├── _diary/                    # 私人日记
├── _papers/                   # 论文笔记
├── _excerpts/                 # 摘录
├── _hardware/                 # 硬件笔记
├── linux/, db/, c/, ds/, cpp/, python/   # 6 大学习轨道（ds/ = 5 个数据结构笔记，2026-10-26 由根目录迁入）
├── HardWare/, LLM/, Redis/, neo4j/, sqlite/, vectordb/  # 旧目录（待 Phase C 迁移）
└── diary/, excerpt/, language/, paper/, test/         # 旧目录（待 Phase C 迁移）
```

> **2026-11-28 变更**：`_briefing/`（每日简报）与 `learn_deep/`（13 领域深度系列）已迁出本 vault，
> 改由 AI 定时任务写入 `C:\code\projects\ai-timer\`（该目录被 gitignore，不入版本库）。
> 深度系列与简报的索引页也随之迁出；本 vault 的 `_index/home.md`、`_index/db.md`、`_meta/schema.md` 保留为指针页，
> 跨仓链接一律用绝对路径 `C:/code/projects/ai-timer/...`。

## 6 大学习轨道

| 轨道 | 简介 |
|---|---|
| linux | Linux 内核、文件系统、网络、调度 |
| db | 数据库（PG/MySQL/SQLite/向量库） |
| c | C 语言核心 |
| ds | 数据结构与算法 |
| cpp | C++ 现代特性 |
| python | Python + AI/ML |

## 笔记类型（4 种模板）

- **theory**：理论学习笔记
- **practice**：动手实验笔记（必填 `tags: [practice, experiment]`）
- **question**：疑问笔记（加 `unresolved: true`）
- **summary**：阶段性总结

## Frontmatter Schema（必填字段）

```yaml
---
stack: linux              # 必填：6 轨道之一
difficulty: medium        # 必填：easy | medium | hard
status: in-progress       # 必填：todo | in-progress | done
links: []                 # 必填
created: 2026-07-10       # 必填
updated: 2026-07-10       # 必填
tags: []                  # 必填
---
```

详见 [_meta/schema.md](_meta/schema.md)

## 维护脚本

| 脚本 | 用途 |
|---|---|
| `_scripts/migrate_notes.py` | 批量补 frontmatter（幂等） |
| `_scripts/linkify.sh` | 双向链接（笔记↔代码，幂等） |
| `_scripts/sync_kanban.py` | 与 knowledge_hub kanban 对齐（stub） |
| `../scripts/sync-learn-deep.sh` | Learn Deep 数据双向同步（Obsidian ↔ knowledge_hub） |

## Learn Deep 数据来源

学习深度文章的数据源（**2026-11-28 起已迁出本 vault**）：

- **主存储**：`C:\code\projects\ai-timer\每日一特性\learn_deep\{c,cpp,comp,db,dist,os,hw,infra,llm,agent,rag,vectordb,aisec,codegen,graph}\`（由 AI 定时任务写入，`ai-timer/` 被 gitignore）
- **副本**：`projects/apps/web/src/data/learn_deep/` —— **当前不存在**。原 `engineering/apps/web/knowledge_hub/src/data/learn_deep/` 随 2026-11-26 前端合并一并消失，需先建目录才能恢复。
- **同步**：运行 `learning/scripts/sync-learn-deep.sh`（路径已更新到新布局；目标目录需先手动创建）


## 仪表盘

打开 [_dashboard/progress.md](_dashboard/progress.md) 查看：
- 各轨道笔记数 / 完成度
- 难度分布
- 最近 30 天更新
- 待解决疑问

## 渐进式迁移状态

- [x] **Phase A**：建骨架（_index/_templates/_meta/_dashboard + .obsidian）
- [ ] **Phase B**：手工迁移 20 个代表性笔记（每 stack 至少 2 个）
- [ ] **Phase C**：脚本批量处理剩余 112 个笔记
- [ ] **Phase D**：双向链接 + 仪表盘激活

## 写作建议

1. 新笔记先用 `_templates/` 下的模板（4 选 1）
2. frontmatter 必填字段不能少
3. 引用代码解法时用 `[[../../code-solutions/c/leetcode/1234]]` wikilink
4. 季度性 review：跑一次 `_scripts/migrate_notes.py --dry-run` 看是否需要补字段

## 相关文档

- `docs/` 下暂无 `learning/obsidian-setup.md` 与 `architecture/dual-track.md`（原链接失效）。当前可参考：
  - 本目录的 [_meta/schema.md](_meta/schema.md) —— Frontmatter Schema 规范
  - [_index/home.md](_index/home.md) —— 总索引与深度系列入口
- 深度系列与每日简报的产物在 `C:\code\projects\ai-timer\`（AI 定时任务产出，不入版本库），见 `C:\code\projects\ai-timer\README.md`。