# EP07 Show Notes — 走进随机流程模型：用概率和数学看清业务流程的“不确定性”

> Review/fix v1.1 show notes staged from `episode7_show_notes.md`. TTS/render not started.
> Provenance: Gemini 3.1 Pro attempted via official Gemini CLI for drafting but failed with 429 MODEL_CAPACITY_EXHAUSTED; draft artifact came from Claude CLI. Gemini CLI `gemini-3.1-pro-preview` later completed independent review with PASS_WITH_MINOR_FIXES; Hermes Autoproducer applied accepted fixes. Final TTS provenance pending. Codex usage: none.

EP07 · 走进随机流程模型：用概率和数学看清业务流程的“不确定性”

本期概要
本集把静态的 BPMN 流程图升级为“能算账”的随机流程模型（Stochastic Process Models, SPM）。我们解释为什么传统确定性模型答不出“平均多久、瓶颈在哪、成本多少”，并系统讲解三种网关概率、负指数时间分布、轨迹概率，以及如何从事件日志反推概率，最后逐题推演课堂练习一到六。

双语术语卡片（中文 → English → 缩写 → 含义）
- 随机流程模型 → Stochastic Process Models → SPM → 在控制流上叠加概率与时间分布，用以计算流程整体性能。
- 随机性 → Stochastics → 把静态地图变成会算账的性能模型的“桥梁”。
- 随机 BPMN → Stochastic BPMN → 标注了分支概率与活动时间分布的 BPMN。
- 异或网关 → Exclusive OR Gateway → XOR → 互斥单选，分支概率之和必须等于一。
- 或网关 → Inclusive OR Gateway → OR → 可同时触发，单条分支不必加到一；可用“独立概率+默认”或“联合分布”表示，联合分布之和为一。
- 事件网关 → Event-Based Gateway → 等待哪个事件先发生（消息 vs 定时器）的“先到先得”赛跑。
- 负指数时间分布 → Negative Exponential Time Distribution → E(λ) → 描述等待时间，率参数 λ = 1 / 平均时间。
- 累积分布函数 → Cumulative Distribution Function → CDF → P(T < x) = 1 − e^(−λx)，即活动在 x 时间内完成的概率。
- 轨迹 → Trace → 日志中线性记录的活动序列。
- 偏序路径 → Partially Ordered Path → 模型中允许并行、不强制排序的执行路径。
- 随机标注 / 权重估计 → Stochastic Annotation / Weight Estimation → 从日志频率反推并标注分支概率。

核心公式与两条红色警告
- CDF：P(T < x) = 1 − e^(−λx)。直觉：e^(−λx) 是“还没完成”的概率，1 减去它就是“已完成”的概率。
- 警告一：λ 是速率，等于平均时间的倒数。平均 4 小时 → λ = 0.25，绝不是 4。
- 警告二：只有 XOR 分支概率之和必须为一；OR 单条分支不必。

时间例子（讲义第 10 页）
平均 10 小时（λ = 0.1），问 11 小时内完成的概率：1 − e^(−0.1×11) = 1 − e^(−1.1) ≈ 1 − 0.333 = 0.667。简化假设：消息不花时间、泳道同步开始。

练习答案速查
- 练习一（贷款拒绝 XOR）：0.15 + (0.85 × 0.1) = 0.15 + 0.085 = 0.235，即 23.5%。口诀：沿路相乘，合并相加。
- 练习二（信贷循环·随机标注）：总实例 105；并行 AND 不标概率。循环回去 = 15/120 = 12.5%，继续 = 105/120 = 87.5%（分母 120 = 105 + 15 次循环）。评估后 XOR：发放报价 70/105 ≈ 66.67%，通知拒绝 35/105 ≈ 33.33%。
- 练习三（运输报价·及时）：选“准备”0.8 × P(准备<48h)。λ = 0.25，1 − e^(−0.25×48) = 1 − e^(−12) ≈ 1。结果 ≈ 0.8（80%）。“拒绝平均 3 小时”是干扰项。
- 练习四（带循环的轨迹概率）：沿实际路径相乘 1×1×0.7×1×1×0.3 = 0.21（21%）。未经过的 0.8/0.2 网关不计入。
- 练习五（在线咨询·60 分钟）：λ = 0.2，P(完成<60min) = 1 − e^(−0.2×60) = 1 − e^(−12) ≈ 1。解决判定 0.95。结果 ≈ 0.95（95%）。
- 练习六（俱乐部订阅·p1/p2/p3）：客户响应=两段指数接力（超指数 survival）。续费 survival(72) = 2e^(−18) − e^(−36) ≈ 3×10⁻⁸；取消 survival(72) = 1.5e^(−12) − 0.5e^(−36) ≈ 9×10⁻⁶。
  - p1 = 0.6×3×10⁻⁸ + 0.4×9×10⁻⁶ ≈ 3.7×10⁻⁶ ≈ 0.00037%（定时器几乎从不触发）。
  - p2 ≈ 0.6（续费），p3 ≈ 0.4（取消）。三者之和 = 1。

本期记忆口诀
沿路相乘，合并相加；λ 是倒数；定时器看时限（时限远大于平均时，定时器≈摆设）。

延伸阅读
Adam Burke, Sander J.J. Leemans, Moe T. Wynn, “Stochastic Process Discovery By Weight Estimation,” International Workshop on Process Querying, Manipulation, and Intelligence, 2020.

下集预告
EP08 · 流程识别（Process Identification）：在建模和仿真之前，如何梳理组织中的流程、绘制流程架构并排定改造优先级。

来源覆盖：讲义第 1–18 页；练习一至六。
制作链路：初稿 Claude CLI artifact（exact model not captured）→ Gemini CLI gemini-3.1-pro-preview 独立审阅 → Hermes Autoproducer 终编修订。Codex usage: none。
