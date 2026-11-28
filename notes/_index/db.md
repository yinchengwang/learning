---
stack: db
difficulty: easy
status: done
links: []
ref: []
created: 2026-07-10
updated: 2026-11-28
tags: [index, db]
---

# DB 学习轨道

> 数据库系统：PostgreSQL、MySQL、SQLite、向量数据库等

## 必学清单

- [ ] PostgreSQL 存储引擎（WAL、MVCC、BTree、Heap）
- [ ] MySQL InnoDB 架构
- [ ] SQLite 轻量级实现
- [ ] 向量数据库（FAISS、Milvus、Chroma）
- [ ] 分布式事务（2PC、3PC、Saga）
- [ ] 查询优化器（成本估算、计划生成）

## 每日一特性（深度系列）

每篇只讲一个库的一个具体特性，写到内部实现。
**2026-11-28 起迁到 `C:\code\projects\ai-timer\每日一特性\learn_deep\db\`**，完整清单见该目录的 README。

- [pg-hot-update](C:/code/projects/ai-timer/每日一特性/learn_deep/db/pg-hot-update.md) —— PostgreSQL HOT 更新：不写索引项的 UPDATE、`LP_REDIRECT` 链、机会性修剪、fillfactor
- [mysql-innodb-undo-purge](C:/code/projects/ai-timer/每日一特性/learn_deep/db/mysql-innodb-undo-purge.md) —— MySQL InnoDB undo log 与 purge：7 字节 roll pointer、history list、purge 三件事、undo 表空间截断

> 系列总控与跨领域对照矩阵：[Learn Deep Index](C:/code/projects/ai-timer/每日一特性/_index/Learn%20Deep%20Index.md)

## 已有笔记（按目录）

| 目录 | 内容 |
|---|---|
| `C:\code\projects\ai-timer\每日一特性\learn_deep\db\` | 每日一特性深度系列（主存储，2026-11-28 迁出本 vault） |
| `DB/sqlite/` | SQLite 语法与轻量实现 |
| `DB/Redis/`、`Redis/` | Redis 设计与实现 |
| `DB/neo4j/` | Neo4j 图数据库 |
| `DB/vectordb/`、`vectordb/` | HNSW / IVF / DiskANN / SPANN / 量化 |
| `interview/database/` | 面试题库与项目追问 |

## 数据统计

Dataview 的 `FROM "db"` 只匹配字面名叫 `db` 的目录，本 vault 里不存在（旧目录已迁到 `learn_deep/db/`、`DB/` 等）。按标题关键词筛：

```dataview
TABLE file.folder AS "目录", difficulty, status, updated
FROM ""
WHERE contains(lower(file.folder), "db") OR contains(lower(file.name), "sqlite") OR contains(lower(file.name), "redis")
SORT updated DESC
```

返回总索引 [[home]]
