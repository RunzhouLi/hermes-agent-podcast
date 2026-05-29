# EP04 Show Notes V2.0

**节目:** 《BPM 流程解码》
**集数:** EP04
**标题:** 等待、记录、折叠、计时——BPMN 子流程与定时事件
**课程来源:** Week 04 — BPMN Sub-processes & Timer Events (Sander Leemans, QUT)
**版本:** V2.0

---

## 简介 / Summary

本集讲解 BPMN 中四个关键高级构件，帮助建模者超越基础顺序流，表达更真实的业务场景：

1. **事件网关**（Event-Based Gateway, EBG）：当流程需要等待外部世界先发生某个事件，再决定走哪条路。核心区别：XOR 是数据驱动、即时决策的；事件网关是事件驱动、延迟等待的。

2. **BPMN 数据建模**（Data Object / Data Collection / Data Store / Data Association）：表达流程读写的信息。区分实例级数据对象（折角纸图标）与持久化数据存储（圆柱体图标）；严格区分数据关联（虚线，不携带 Token）与顺序流（实线，携带 Token）。

3. **子流程**（Sub-process）：通过折叠（+）与展开管理流程复杂度。覆盖层级嵌套、数据作用域（DO1/DO2/DO3 逐层收窄）、展开可跨泳道折叠不能跨泳道。区分嵌入式与可复用调用活动（加粗边框）。事件子流程（虚线外框）处理运行时异常。循环（↺）、多实例（∥）、临时（∼）三种执行标记，其中 ↺ 和 ∥ 不可同时使用。补偿标记 + 另集讲解。

4. **定时事件**（Timer Events）：定时开始事件（自动触发）、中间定时事件（计划内等待）、边界定时事件（贴在活动边框上的超时/截止处理）。区分中断型（实线圆圈，取消当前活动）与非中断型（虚线圆圈，并行提醒路径）。区分边界事件的虚线圆圈与事件子流程的虚线外框。

贯穿全集的稳定类比：**客服工单系统**——等客户回复（事件网关）、记录工单和档案（数据）、折叠投诉处理步骤（子流程）、SLA 超时升级（边界定时事件）。

---

## 关键术语 / Key Terms

| 中文 | English | 标记/缩写 | 简要定义 |
|---|---|---|---|
| 事件网关 | Event-Based Gateway | EBG | 等外部事件先发生再决定路径；另一方做决定；排他且延迟 |
| 隐藏数据 | Hidden Data | — | BPMN 不规定布尔表达式和数据类型，这些细节在建模层面隐藏 |
| 数据对象 | Data Object | DO | 活动使用或产生的信息，折角纸图标，属于当前流程实例 |
| 数据集合 | Data Collection | — | 一组同类型数据对象，底部三条竖线 |
| 数据存储 | Data Store | DS | 持久化数据，跨流程实例存在，圆柱体图标 |
| 数据关联 | Data Association | — | 虚线，读写数据，不推动流程执行 |
| 顺序流 | Sequence Flow | — | 实线，携带控制令牌，推动流程向前 |
| 折叠子流程 | Collapsed Sub-process | + | 隐藏内部细节，底部有 + 标记 |
| 展开子流程 | Expanded Sub-process | — | 显示完整内部流程，跨泳道可 |
| 调用活动 | Call Activity | CA | 引用外部定义的可复用流程，加粗边框 |
| 事件子流程 | Event Sub-process | 虚线外框 | 父流程运行时由事件触发的内部处理 |
| 循环子流程 | Loop Sub-process | ↺ | 条件满足期间反复执行 |
| 多实例子流程 | Multi-instance Sub-process | ∥ | 运行 n 个独立实例，不可与 ↺ 同时使用 |
| 临时子流程 | Ad-hoc Sub-process | ∼ | 不定顺序和次数，内部无开始/结束事件 |
| 定时开始事件 | Timer Start Event | 单圈+时钟 | 按时间或周期启动流程实例 |
| 中间定时事件 | Intermediate Timer Catch Event | 双圈+时钟 | 流程中途计划性等待时间 |
| 边界定时事件 | Boundary Timer Event | 贴在活动边 | 附着在活动上的超时/截止处理 |
| 中断型 | Interrupting | 实线圆圈 | 取消当前活动，强制走异常路径 |
| 非中断型 | Non-interrupting | 虚线圆圈 | 保留当前活动，并行开提醒路径 |

---

## 本集亮点

- **启发式四阶段教学：** 每个核心概念均遵循"困惑→探索→框架→锚定"的学习节奏，Host A 晓雨作为发现催化剂，在 B 给出答案前自主尝试解决方案。
- **因果桥接过渡：** 段间不使用"好了A讲完了现在讲B"式清单过渡，而是解释"因为A给了我们X，所以自然需要Y"的逻辑依赖。
- **客服工单类比贯穿全程：** 从开头申请到结尾 SLA 定时器，每个过渡都回到工单场景。
- **五类常见混淆自测：** 事件网关 vs XOR、数据关联 vs 顺序流、子流程 vs 池/泳道、边界定时 vs 中间定时、中断型 vs 非中断型。

---

## 出处 / Provenance

- **初始草稿:** Gemini CLI (`gemini-3.1-pro-preview`)
- **方法论扩展:** Hermes Agent (gpt-5.5) — 全面应用 v1.4.0 启发式教学法和架构锚定规则
- **独立审阅:** Gemini CLI (`gemini-3.1-pro-preview`) — 自审阅模式 (Claude CLI 跨模型审阅不可用)
- **审阅结论:** NEEDS_FIX → 2 项修复 (EBG 缩写补充 + 标记组合规则)
- **TTS 合成:** Volcengine/Doubao seed-tts via doubao-speech CLI, zh-female-warm, 自然速度
- **Codex 使用:** none
