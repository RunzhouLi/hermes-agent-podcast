# EP07 — Model Quality & Representation (模型质量与表达)

> BPI Course Podcast · RWTH Aachen SS 2026 · Prof. Wil van der Aalst 第七讲
> 全课主线：翻译与语言 — 评模型如评译文，选语言如选目标语

## 本集概要

Alpha Algorithm 给了我们发现模型的能力。但发现之后呢？你怎么知道拿到的模型好不好？
这集回答的就是这个问题——而且它揭示了另一个更深的真相：你用什么"语言"表达模型，
本身就决定了你能发现什么。

**四种质量标准（Four Quality Criteria）** 就像评价一篇译文的四个维度：
- **Fitness（拟合度）= 信** — 原文（日志）有的，译文（模型）都覆盖了吗？
- **Precision（精确度）= 达** — 译文有没有添加原文没有的东西？
- **Generalization（泛化度）= 达（续）** — 换一个语境，译文还成立吗？
- **Simplicity（简洁度）= 雅** — 同等表现下，越简单越好

但这四个标准有一个共同的问题：**真实流程是未知的，负例不存在。** Precision 天生比 Fitness 更难量度——
这是整个 conformance checking 领域的哲学根基。

然后话题转向**表达偏差（Representational Bias）**——本集出现频率最高的词。
"中译英必然丢失敬语区分"——建模语言的固有限制，决定了你能发现什么、不能发现什么。
而且一个关键纠错：屏幕上画成 BPMN 的模型，不等于你用 BPMN 在搜索。**可视化 ≠ 表达偏差。**

最后介绍三种建模"语言"，贯穿全集的翻译类比：
- **BPMN = 英语** — 最通用，但有歧义。OR-join 恶性循环悖论（等也对不了、不等也对不了）是最好的证明
- **Dependency Graph = 句法树** — 最简表达，只标因果结构，没有可执行语义
- **C-net = 依存语法** — 用"绑定"灵活标注组合关系，声明式语义，比 WF-net 更有表达力

## 关键术语

| 中文 | English | 简述 |
|------|---------|------|
| 拟合度 | Fitness | 模型复现日志行为的能力 |
| 精确度 | Precision | 模型不放行日志外行为的能力 |
| 泛化度 | Generalization | 捕获未见但合理行为的能力 |
| 简洁度 | Simplicity | 奥卡姆剃刀，同等表现选最简单的 |
| 表达偏差 | Representational Bias | 建模语言固有的表达限制 |
| 令牌语义 | Token Semantics | 弹珠在图中流动的模拟方式 |
| 恶性循环悖论 | Vicious Cycle Paradox | BPMN OR-join 的语义死锁 |
| 依赖图 | Dependency Graph | 节点=活动，弧=因果关系 |
| 因果网 | Causal Net (C-net) | 活动+输入/输出绑定集合 |
| 声明式语义 | Declarative Semantics | 允许怎么走，而非必须怎么走 |

## 章节

1. 开场：发现之后呢？
2. 四种质量标准：翻译的评分维度
3. TP/FP/TN/FN：朴素分类框架，和它的哲学塌方
4. 四个手感：过拟合、欠拟合、不拟合、平衡
5. 表达偏差：语言决定你能说什么
6. WF-net 的偏见与并发爆炸
7. BPMN：最通用的语言，和它的陷阱
8. 可视化的幻象：Alpha 被画成 BPMN 不等于用 BPMN 搜索
9. 依赖图：句法树
10. C-net：依存语法
11. C-net 声明式语义：事后认领的灵活性
12. C-net vs WF-net：谁是真正的全能选手？
13. 收网前的终极测试：abcdcbde
14. 收网：四个标准，三门语言，一条主线
15. 预告：EP08 Heuristic Mining — C-net 终于上岗

## 来源

- BPI Lecture 7: Quality of Discovered Models and Representations
- Prof. Wil van der Aalst, RWTH Aachen SS 2026
- 140 slides (S3-S137 covered)
