# EP04 — Introduction to Process Discovery (过程发现入门)

## Show Notes

**BPI (Business Process Intelligence) — RWTH Aachen SS 2026**
**来源：** Lecture 4 by Prof. Wil van der Aalst

### 本集概要

在有了三集数据科学基础之后，我们终于跨入了过程挖掘的核心领地——过程发现 (Process Discovery)。这一集我们用一个贯穿全程的比喻：**侦探破案**。

你手里有一堆事件数据（案发现场的痕迹），但没有现成的流程图。怎么从零拼出真实发生的流程？本集教你两种"还原手法"：快速的 DFG 草图，和法庭级的 Petri 网正式重建。

### 四站地图

1. **定位过程发现** — Play-In / Play-Out / Replay，事件日志的构造本质
2. **后续关系图 (DFG)** — 朴素但有用。优点：快、简、直观。致命缺陷：分不清并发和循环
3. **Petri 网复习** — 库所、变迁、令牌、弧。用结构区分选择、并发、循环——DFG 做不到
4. **审问 Petri 网** — 有界性、安全性、无死锁、活性（金字塔）。压轴反常识：活性不单调——多给令牌可能反而把活网变成死网

### 关键术语

- 过程发现 — Process Discovery
- 事件日志 — Event Log (case + activity + timestamp)
- 轨迹 — Trace
- 后续关系图 — Directly-Follows Graph (DFG)
- Petri 网 — Petri Net (place, transition, token, arc)
- 标识 — Marking
- 有界性 — Boundedness
- 安全性 — Safeness (1-bounded)
- 无死锁 — Deadlock-free
- 活性 — Liveness
- 工作流网 — Workflow Net (WF-net)
- 健全性 — Soundness

### 制作信息

- 脚本生成：Claude Opus 4.8 (TUI interactive)
- 独立审阅：Gemini 3.1 Pro — GO_AFTER_FIX (3项修复)
- TTS：Doubao/Volcengine zh-female-warm，自然语速
- 对话轮次：251轮 (A:126, B:125)
