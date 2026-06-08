# EP11 — Event Data & Exploration (事件数据与探索)

> BPI Course Podcast · RWTH Aachen SS 2026 · Prof. Wil van der Aalst 第十一讲
> 中心类比：地质勘探与石油钻井 — 算法再强，垃圾进垃圾出

## 本集概要

前十集我们学了四种发现算法——Alpha 数关系、Heuristic 数频率、Region 画状态图、Inductive 切蛋糕。它们吃进去的是同一样东西：事件日志。但这份日志从来不是"给"的，它是被"造"出来的——从成千上万张数据库表里抽取、挑选、塑形。

本集从"什么是事件日志"出发，俯瞰整条数据管道：从五层元模型（流程→案例→活动→活动实例→事件）到事务生命周期；从点图（dotted chart）的震波勘探到三种从数据库中刨出事件的铲子；然后直面本集最核心的认知翻转——案例概念（case notion）不是一个数据库字段，它是一个**建模选择**。后半场揭示一个更残酷的事实：多数真实数据是对象中心的（object-centric），多张表、多个实体相互交叠。当你强行压扁（flatten）成案例中心时，你会遇到收敛、发散、缺陷三种病态。

**事件数据，是流程挖掘这整座大厦的地基。** 今天我们把地基翻开来看：它在结构上长什么样、从哪里来、为什么案例中心的简化是个危险的幻觉、以及怎么用 OCEL 和 OCPM 正确地处理多对象数据。最后由 GIGO 收尾——垃圾进，垃圾出。

## 关键术语

- **Event Log (事件日志)** — XES IEEE 1849-2023 标准: log → trace → event → attribute
- **Case / Trace (案例 / 轨迹)** — 一次完整的流程执行；trace 是 case 在日志里的"脚印序列"
- **Activity Instance (活动实例)** — 区别于 Activity Type：类型是模板，实例是一次具体执行
- **Transactional Lifecycle (事务生命周期)** — schedule→assign→start→suspend→resume→complete（含各种中断路径）
- **Dotted Chart (点图)** — 一个点=一个事件；纵轴=案例/活动/资源；横轴=绝对/相对时间；探索工具，不是发现算法
- **Case Notion (案例概念)** — **案例是一个建模选择，不是数据给定的**
- **OCEL (Object-Centric Event Log)** — 对象中心事件日志：一个事件可以关联多个对象类型
- **Flattening (展平)** — 把 OCEL 压扁成单案例日志以兼容传统工具，但代价是……
- **Convergence / Divergence / Deficiency** — 展平的三种病态：事件重复/事件丢失/事件完全缺失
- **OCPM (Object-Centric Process Mining)** — 直接在 OCEL 上挖掘，创建多视图，不需要展平
- **G4L (Guidelines for Logging)** — 11 条打井最佳实践：命名清晰、引用稳定、值精确、完整忠实、可比、护隐私
- **GIGO (Garbage In, Garbage Out)** — 分析质量的上限 = 数据质量的下限

## 中心类比

**地质勘探与石油钻井：**
- 事件日志的元模型 = 岩石分类系统（火成岩/沉积岩/变质岩）
- 点图 = 地震勘探（钻之前先看清地下纹理）
- 从数据库中抽取事件 = 三种取油铲子
- 案例概念 = 选择钻进哪一层（不同的层→不同的油→不同的价值）
- 对象中心数据 = 地层是相互重叠的（真实地质）
- 收敛 = 从不同角度钻到同一个油袋，重复计算
- 发散 = 有些油袋你的钻孔根本没穿过
- G4L 指南 = 打井最佳实践
- GIGO = 地图错了，钻到哪里都是白钻

## 本集结构

1. **认岩** — 事件日志的五层元模型、事务生命周期、活动类型 vs 实例、XES 标准
2. **震波勘探** — 点图：三种纵轴视图、绝对/相对时间、性能谱简介
3. **取油** — 三种从数据库中重建事件的模式、案例选择之痛
4. **选层** — 案例概念 = 建模选择（本集核心认知翻转）
5. **重叠地层** — 对象中心事件数据、展平及其三种病态
6. **正确钻井** — OCEL 标准、OCPM 方法论、G4L 指南、GIGO

## 来源覆盖

- **教材:** BPI-L11-Event-Data-and-Exploration.pdf (107 张幻灯片)
- **6 个主题集群，64 个核心教学项**
- **覆盖面:** 案例中心元模型、点图、数据抽取、对象中心数据、OCEL/OCPM、数据质量与 G4L

## 制作信息

- **脚本:** Claude CLI claude-opus-4-8 (TUI interactive)
- **审阅:** Gemini CLI gemini-3.1-pro-preview (NEEDS_FIX → 修复后 GO)
- **TTS 合成:** Volcengine/Doubao zh-female-warm (自然语速)
- **审阅亮点:** 6/6 核心概念通过 4 层启发式教学深度审计（饥饿→探索→构建→锚定），类比映射"堪称教科书级别"

## 下一集

EP12 — Conformance Checking Part 1：有了模型，也有了真实跑出来的事件日志——怎么判断模型和现实对不对得上？
