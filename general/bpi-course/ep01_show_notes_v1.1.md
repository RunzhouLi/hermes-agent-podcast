# EP01 — Introduction to Process Mining · 课程笔记

**发布时间：** 2026-06-02
**时长：** 32:05
**讲稿：** Claude Opus 4.8 (TUI) · 审阅：Gemini 3.1 Pro · TTS：Doubao/Volcengine zh-female-warm
**课件：** BPI L1, RWTH Aachen SS 2026, Prof. Wil van der Aalst (147 slides)

---

## 本集概要

什么是过程挖掘（Process Mining）？它为什么被称为"数据科学与流程科学之间缺失的那一环"？本集从一条草坪上的土路讲起，带你理解过程挖掘的核心理念、事件数据的结构、以及三种基本玩法。

## 核心概念

- **过程挖掘 (Process Mining)**：从信息系统的事件日志中自动发现、监控和改进真实业务流程
- **事件日志 (Event Log)**：由 Case（案例）+ Activity（活动）+ Timestamp（时间戳）组成的记录集合
- **案例中心 vs 对象中心 (Case-Centric vs Object-Centric)**：事件数据的两种组织方式
- **三种基本类型**：
  - **过程发现 (Process Discovery / Play-In)**：从数据中自动生成流程模型
  - **合规检查 (Conformance Checking / Play-Out)**：对比模型与实际执行
  - **过程增强 (Process Enhancement / Replay)**：用时间数据丰富流程模型

## 关键术语

| 中文 | English | 说明 |
|---|---|---|
| 过程挖掘 | Process Mining (PM) | 从事件数据中发现、监控、改进流程 |
| 事件日志 | Event Log | Case + Activity + Timestamp 的记录 |
| 案例 | Case | 流程实例（如一个订单） |
| 活动 | Activity | 流程中的一个步骤 |
| 过程发现 | Process Discovery | 数据→模型 (Play-In) |
| 合规检查 | Conformance Checking | 模型vs实际 (Play-Out) |
| 过程增强 | Process Enhancement | 带时间重放 (Replay) |
| 渴望路径 | Desire Line | 人们实际走的路 vs 规划的路 |

## 工具

- **Celonis**：德国十角兽，全球最广泛使用的商业PM工具
- **ProM 6.15**：开源学术工具，1500+ 分析方法
- **RapidMiner (Altair AI Studio)**：数据科学/ML 平台

## 下集预告

EP02 — Data Science: Supervised Learning。从数据科学基础开始，给过程挖掘打地基。

---

*BPI 课程播客 © 2026 · 基于 RWTH Aachen BPI SS 2026 课件制作*
