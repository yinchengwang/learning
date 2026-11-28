---
stack: c
difficulty: easy
status: done
links: []
ref: []
created: 2026-07-10
updated: 2026-11-28
tags: [index, home]
---

# 学习轨道总索引

> 双轨制下的 β 目标（学习日志）入口。6 大学习轨道 + 13 个深度系列领域。

## 学习轨道索引

| 轨道 | 简介 | 索引 |
|---|---|---|
| **linux** | Linux 内核、文件系统、网络、调度 | [[linux]] |
| **db** | 数据库（PG/MySQL/SQLite/向量库） | [[db]] |
| **c** | C 语言核心（指针、内存、编译） | [[c]] |
| **ds** | 数据结构与算法理论 | [[ds]] |
| **cpp** | C++ 现代特性（11/14/17/20） | [[cpp]] |
| **python** | Python 工具链与 AI/ML | [[python]] |

## 深度系列（每日一特性）

每个领域一个主题，写到内部实现。
**2026-11-28 起整体迁到 `projects/ai-timer/每日一特性/`** —— 该目录在 `projects/.gitignore` 中，属 AI 定时任务产出，不入版本库。

- 🗂️ [Learn Deep Index](C:/code/projects/ai-timer/每日一特性/_index/Learn%20Deep%20Index.md) —— 系列总控：13 个领域、每周配比、跨领域对照矩阵
- 主存储：`C:\code\projects\ai-timer\每日一特性\learn_deep\<领域>\`

| 领域 | 定位 |
|---|---|
| 数据库 | 主线根基：存储引擎、事务、索引、分布式 |
| 计算机基础 | **非科班地基** + 网络编程（每天 1 篇，18:00） |
| 分布式系统 | 共识、一致性、复制、分片、分布式事务 |
| 操作系统 | 虚拟内存、调度、文件系统、内核机制 |
| GPU 与硬件 | Tensor Core、内存层次、互连、能耗 |
| AI 推理基础设施 | 批处理调度、KV cache、量化、并行 |
| LLM 基础 | Attention 变体、MoE、长上下文、后训练 |
| Agent 运行时 | 工具协议、上下文工程、多 agent、harness |
| RAG | 分块、检索、重排、压缩、引用、评测 |
| 向量数据库 | 图索引、量化、混合检索、过滤 ANN |
| AI 安全 | 注入、后门、可信执行、隐私、供应链 |
| 代码智能与编译 | 编译技术 + SWE-agent、形式化辅助 |
| 图数据库 | 属性图、RDF、路径查询、GNN、GraphRAG |

## 资讯归档

- 📰 [Briefing Index](C:/code/projects/ai-timer/AI简报/Briefing%20Index.md) —— 数据库 + AI 每日简报（每日 08:30 定时任务产出）

## 代码仓巡检

- 🔍 [代码仓巡检](C:/code/projects/ai-timer/代码仓巡检/) —— 每日 08:00 只读巡检报告

## 仪表盘

- 📊 [_dashboard/progress.md](../_dashboard/progress.md) —— 学习进度仪表盘

## 元数据

- 📐 [_meta/schema.md](../_meta/schema.md) —— Frontmatter Schema 规范
- 📝 [_templates/](_templates/) —— 4 类笔记模板（theory/practice/question/summary）

## 个人分类（独立轨道）

- 📓 [_diary/](../_diary/) —— 私人日记
- 📄 [_papers/](../_papers/) —— 论文笔记
- 📚 [_excerpts/](../_excerpts/) —— 摘录
- 🖥️ [_hardware/](../_hardware/) —— 硬件笔记

## 数据统计

```dataview
TABLE length(rows) as "笔记数", 
       length(filter(rows, (r) => r.status = "done")) as "已完成"
FROM ""
GROUP BY stack
SORT length(rows) DESC
```