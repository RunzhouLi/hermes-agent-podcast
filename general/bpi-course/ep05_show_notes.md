# EP05 — Alpha Algorithm Part 1 (Alpha算法 第一部分)

## Show Notes

**BPI (Business Process Intelligence) — RWTH Aachen SS 2026**
**来源：** Lecture 5 by Prof. Wil van der Aalst

### 本集概要

DFG 画出了"谁跟着谁"，但它哑巴——分不清箭头背后是因果还是巧合。这一集我们学习 Alpha 算法：**从事件日志自动推断因果、并行、选择，然后生成一张能区分这三种语义的 Petri 网。**

贯穿全集的比喻：**编译器**。DFG 是源码注释（模糊但好读），Petri 网是机器码（精确但难写），Alpha 是编译器——自动把前者翻译成后者。

### 五节地图

1. **转移系统** — 统一的底层表示。Petri 网的可达图就是一个转移系统。教授名言："Petri 网理论对过程挖掘，就像线性代数对机器学习。"
2. **工作流网与健全性** — 编译器的"目标平台规范"。四条标准：安全、正确完成、有完成的可能、没有死部分。短路定理把健全性接回经典 Petri 网理论。
3. **Alpha 的核心洞察** — 四种顺序关系：直接跟随 (>) → 因果 (→) → 并行 (‖) → 选择 (#)。靠"方向对称性"这一个维度，劈开 DFG 的哑巴箭头。
4. **足迹矩阵与八步算法** — 编译器内部：从日志建足迹矩阵，找极大库所对，布线成 Petri 网。
5. **Alpha 的边界** — 短环、非自由选择、隐藏活动、重复活动——这些 Alpha 搞不定。

### 关键术语

- 转移系统 — Transition System
- 工作流网 — Workflow net (WF-net)
- 健全性 — Soundness（安全 + 正确完成 + 有完成的可能 + 没有死部分）
- 直接跟随 — Direct Succession (>)
- 因果 — Causality (→)
- 并行 — Parallel (‖)
- 选择 — Choice (#)
- 足迹矩阵 — Footprint matrix

### 制作信息

- 脚本生成：Claude Opus 4.8 (TUI interactive)
- 独立审阅：Gemini 3.1 Pro — GO_AFTER_FIX (3项修复)
- TTS：Doubao/Volcengine zh-female-warm，自然语速
- 对话轮次：273轮 (A:136, B:137)
