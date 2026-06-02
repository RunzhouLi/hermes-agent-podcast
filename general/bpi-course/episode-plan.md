# BPI 课程播客 — 分集规划

> 基于 **Business Process Intelligence (SS 2026)** — Prof.dr.ir. Wil van der Aalst, RWTH Aachen
> Study Guide BPI26.pdf 验证：全名 Business Process Intelligence（过程挖掘 / 流程智能），19讲 + 10次练习

## Episode Split

**原则：** 每讲 87–147 页幻灯片，密度高。算法课（Alpha Miner、Region-Based、Inductive Mining）各独立一集。Guest Lecture 与相邻讲合并。共计 **17 集**。

| EP | 源讲 | 课题 | 幻灯片 | 嵌入练习 |
|---|---|---|---|---|
| 01 | L1 | Introduction to Process Mining | 147 | E1 (工具导览) |
| 02 | L2 | Data Science: Supervised Learning | 135 | E2 (数据挖掘) |
| 03 | L3 | Data Science: Unsupervised Learning & Evaluation | 132 | — |
| 04 | L4 | Introduction to Process Discovery | 122 | E3 (Petri Nets) |
| 05 | L5 | Alpha Algorithm Part 1 | 87 | E4 (Alpha Miner) |
| 06 | L6 | Alpha Algorithm Part 2 | 139 | — |
| 07 | L7 | Model Quality & Representation | 140 | — |
| 08 | L8 | Heuristic Mining | 90 | E5 (Heuristic Mining) |
| 09 | L9 | Region-Based Mining | 142 | — |
| 10 | L10 | Inductive Mining | 116 | E6 (Region & Inductive Mining) |
| 11 | L11 | Event Data & Exploration | 107 | — |
| 12 | L12 | Conformance Checking Part 1 | 105 | — |
| 13 | L13 | Conformance Checking Part 2 | TBD | E7 (Conformance Checking) |
| 14 | L14 | Decision Mining | TBD | E8 (Decision Mining) |
| 15 | L15–L16 | Guest Lecture + Performance & Organizational Mining | TBD | E9 (Performance & Org Mining) |
| 16 | L17–L18 | Operational Support + Distributed & Streaming Mining | TBD | E10 (Operational Mining) |
| 17 | L19 | Course Wrap-up & Closing | TBD | — |

## 课程五大模块

| 模块 | EP | 内容 |
|---|---|---|
| **基础与数据科学** | 01–03 | 过程挖掘导论、监督学习、无监督学习与评估 |
| **过程发现算法** | 04–10 | 过程发现入门、Alpha 算法 (×2)、模型质量、启发式挖掘、区域挖掘、归纳挖掘 |
| **合规检查与决策挖掘** | 11–14 | 事件数据探索、合规检查 (×2)、决策挖掘 |
| **高级主题** | 15–16 | Guest Lecture、性能与组织挖掘、运营支持、分布式流式挖掘 |
| **总结** | 17 | 课程回顾与考试要点 |

## 制作状态

| EP | 状态 | 讲稿模型 | 审阅 | TTS |
|---|---|---|---|---|
| 01–17 | 📋 待制作 | — | — | — |

## 制作流程

参照 BPM 课程播客的生产流程：
1. **Claude CLI `claude-opus-4-8` TUI 交互模式** 生成讲稿
2. **Gemini CLI `gemini-3.1-pro-preview` 跨模型审阅**
3. 应用审阅修订 + 概念深度审计
4. TTS-clean 脚本 → **Doubao `zh-female-warm`** 渲染
5. 验证音频、更新 show notes、发布 RSS

## 文件路径

- 播客目录：`general/bpi-course/`
- 课件目录：`/root/documents/BPI_Course/Lectures/`
- 练习目录：`/root/documents/BPI_Course/Exercises/`
