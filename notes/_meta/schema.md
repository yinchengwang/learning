# 笔记 Frontmatter Schema

本目录的所有笔记**必须**包含以下 frontmatter 字段：

```yaml
---
stack: linux              # 必填：linux | db | c | ds | cpp | python
difficulty: medium        # 必填：easy | medium | hard
status: in-progress       # 必填：todo | in-progress | done
links: []                 # 必填：相关链接数组
ref: []                   # 可选：与 knowledge_hub/data/kanban-data.js 的 ID 对齐
created: 2026-07-10       # 必填：创建日期
updated: 2026-07-10       # 必填：最后修改日期
tags: []                  # 必填：自由标签
---
```

## 字段说明

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `stack` | enum | ✅ | 所属学习轨道：`linux` / `db` / `c` / `ds` / `cpp` / `python` |
| `difficulty` | enum | ✅ | 难度等级：`easy`（2 天内掌握）/ `medium`（3-5 天）/ `hard`（6 天+） |
| `status` | enum | ✅ | 完成状态：`todo`（未开始）/ `in-progress`（进行中）/ `done`（完成） |
| `links` | array | ✅ | 相关链接（论文、官网、文档） |
| `ref` | array | ⬜ | 与 knowledge_hub 的 kanban ID 对齐（可选） |
| `created` | date | ✅ | 首次创建日期（YYYY-MM-DD） |
| `updated` | date | ✅ | 最后修改日期（YYYY-MM-DD） |
| `tags` | array | ✅ | 自由标签（Dataview 查询用） |
| `unresolved` | boolean | ⬜ | 扩展键（`question` / `correction` 专用）：`true` 表示还没解决，会出现在仪表盘的「待解决疑问」清单里 |
| `problem` | string | ⬜ | 扩展键（`correction` 专用）：关联的题目 ID（如 `lc-00001`），是笔记与题库之间的连接键 |

## 笔记类型

| 类型 | 模板 | frontmatter 差异 |
|---|---|---|
| `theory` | `_templates/theory.md` | `status` 默认 `in-progress` |
| `practice` | `_templates/practice.md` | `tags` 必填 `[practice, experiment]` |
| `question` | `_templates/question.md` | `status` 默认 `in-progress`，加 `unresolved: true` |
| `summary` | `_templates/summary.md` | `status` 默认 `done` |
| `correction` | `_templates/correction.md` | `status` 默认 `in-progress`，`tags` 必填 `[practice, correction]`，追加 `unresolved` 与 `problem` 两个扩展键 |

## Dataview 查询示例

```dataview
TABLE stack, difficulty, status
FROM ""
WHERE stack = "linux"
SORT updated DESC
```

## 错题订正（correction）惯例

M4 起，app 会把做错题的复盘写进 `notes/practice/<题目ID>-订正.md`。这是新建的惯例。

- **目录**：`notes/practice/`，一个题目一篇，文件名 `<题目ID>-订正.md`
- **frontmatter 键序**：基线 8 键（`stack` / `difficulty` / `status` / `links` / `ref` / `created` / `updated` / `tags`）顺序不变，
  扩展键 `unresolved` 与 `problem` 追加在后面
- **`stack` 取值**：按题目的 track 映射——`interview→c`、`fundamentals→ds`、`advanced→ds`、`engineering→db`
- **`difficulty`**：直接取题目的难度（`easy` / `medium` / `hard`）
- **`status`**：默认 `in-progress`；订正做完改成 `done`
- **`tags`**：固定 `[practice, correction]`
- **`unresolved`**：默认 `true`——还没弄透就保持 `true`，它会出现在「待解决疑问」清单里；弄透后改成 `false`
- **`problem`**：题目的稳定 ID（如 `lc-00001`）
- **正文结构**：`## 订正 <日期>` 小节（可追加多段），末尾 `## 关联` 列出题目路径与知识点

示例：

```markdown
---
stack: c
difficulty: medium
status: in-progress
links: []
ref: []
created: 2026-11-11
updated: 2026-11-11
tags: [practice, correction]
unresolved: true
problem: lc-00001
---

# 两数之和 · 错题订正

## 订正 2026-11-11

哈希表一次遍历就能出解：先查再插，别先插再查。

## 关联

- 题目：`bank/interview/lc-00001.md`（`lc-00001`）
- 知识点：哈希表、数组
```

> **说明**：`_templates/correction.md` 这个模板文件本计划不生成（M4 只在运行时按上面的格式落盘）。
> 要模板的话，复制 `_templates/question.md` 改键名即可。

## 渐进式迁移策略

- **Phase A（已完成）**：建骨架（`_index/`、`_templates/`、`_meta/`、`_dashboard/` + `.obsidian/`）
- **Phase B**：手工迁移 20 个代表性笔记（每 stack 至少 2 个）+ 补 frontmatter
- **Phase C**：脚本批量处理剩余 112 个笔记
- **Phase D**：双向链接 + 仪表盘

详见 `_dashboard/progress.md`。