# EP12 — Conformance Checking Part 1 (一致性检查 上)

> BPI Course Podcast · RWTH Aachen SS 2026 · Prof. Wil van der Aalst 第十二讲
> 中心类比：体检与诊断 — 建出来的模型，对不对？

## 本集概要

前十集我们建模型——Alpha、Heuristic、Region、Inductive，四种发现算法，线条画完。上一集我们挖数据——107张幻灯片讲事件日志从哪来、怎么抽出、案例是选出来的。这两条线在今天汇合了：**一致性检查 (Conformance Checking)**。

模型说应该怎么走。日志记录了实际怎么走。拿这两个一对，哪合、哪不合？合不合能量化成一个数吗？这就是本集要回答的问题。

先从四个维度讲起：拟合度 (Fitness)、精确度 (Precision)、泛化度 (Generalization)、简洁度 (Simplicity)。然后直面一个痛：拟合和精确天生拉扯——调高一个，另一个就掉。帕累托前沿告诉我们：没有全能冠军，只有取舍。

第一把尺子：**因果足迹 (Causal Footprints)**。x>y，x 直接后跟 y。简单、快速，但不看频率、不判因果，只是个影子。

第二把尺子：**令牌回放 (Token-Based Replay)**。四个计数器——p(产出)、c(消耗)、m(缺失)、r(剩余)。一次完美回放和一次失败回放的完整 walkthrough。不变量 p+m≥c≥m 为什么永真。然后揭示一个让人不舒服的事实：c=p 并非永远成立。

最后一节：为什么基本回放不够——静默变迁、局部决策陷阱——引出下一站对齐 (Alignments)。

## 关键术语

- **Conformance Checking / 一致性检查** — 模型 vs 日志 = 对得上吗
- **Fitness / 拟合度** — 模型能解释多少日志行为
- **Precision / 精确度** — 日志实际使用了多少模型空间
- **Pareto Front / 帕累托前沿** — 最优取舍面
- **Direct Succession / 直接后继 (x>y)** — x 后面直接跟了 y
- **Causal Footprint / 因果足迹** — 直接后继对的集合
- **Token-Based Replay / 令牌回放** — 在 Petri 网上重放每条 trace
- **p/c/m/r** — produced/consumed/missing/remaining tokens
- **Silent Transition τ / 静默变迁** — 看不见的模型节点
- **Alignment / 对齐** — 基于状态空间的全局一致性

## 中心类比

**体检与诊断：**
- 模型 = 健康模板（器官功能参考值）
- 日志 = 病历数据（实际指标）
- CC = 比对模板和病历
- Fitness = 模板能解释多少症状
- Missing tokens = 解释不了的病情（模板不完整）
- Remaining tokens = 模板预期有但病人没表现的（模板过度拟合）
- Pareto = 灵敏度 vs 特异性 的取舍
- Token replay = 逐项核对检查清单
- Alignments = 二次诊断 / 全身影像

## 来源覆盖

- **教材:** BPI-L12-Conformance-Checking-1.pdf (105 张幻灯片)
- 49 个核心教学项

## 下一集

EP13 — Conformance Checking Part 2：对齐——全局视角的二次诊断
