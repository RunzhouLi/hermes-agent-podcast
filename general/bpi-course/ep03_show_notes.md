# EP03 — Data Science: Unsupervised Learning & Evaluation · 课程笔记

**发布时间：** 2026-06-05
**时长：** ~50 分钟（待验证）
**讲稿：** Claude Opus 4.8 (TUI) · 审阅：Gemini 3.1 Pro (NEEDS_FIX/GO_AFTER_FIX) · TTS：Doubao/Volcengine zh-female-warm
**课件：** BPI L3, RWTH Aachen SS 2026, Prof. Wil van der Aalst (132 slides)

---

## 本集概要

没有标签也能学习——这是无监督学习的核心命题。本集以意大利餐厅5000桌的消费数据为主线，串联起关联规则和聚类两大无监督技术，最后回到模型评估的方法论。

## 核心概念

- **关联规则 (Association Rule)**：X → Y 的共现模式。三个度量：Support（够常见）、Confidence（够准）、Lift（不是巧合）
- **支持度 (Support)**：P(X∩Y)，规则覆盖面
- **置信度 (Confidence)**：P(Y|X)，条件概率
- **提升度 (Lift)**：Confidence / P(Y)，>1正相关、<1负相关、=1独立
- **K均值聚类 (k-means)**：初始化质心→Assign分配→Recompute重算→循环至收敛
- **交叉验证 (Cross-validation)**：k-fold轮换训练/测试，评估泛化能力
- **Precision/Recall/F1**：Accuracy的进阶替代

## 关键术语

| 中文 | English | 说明 |
|---|---|---|
| 无监督学习 | Unsupervised Learning | 无标签学习 |
| 关联规则 | Association Rule | X→Y 模式 |
| 支持度 | Support | P(X∩Y) |
| 置信度 | Confidence | P(Y\|X) |
| 提升度 | Lift | 去伪存真 |
| K均值 | k-means | 迭代聚类 |
| 交叉验证 | Cross-validation | 泛化评估 |
| 概念漂移 | Concept Drift | 数据随时间变化 |

## 下集预告

EP04 — Introduction to Process Discovery。数据科学地基打完，真正的流程挖掘开始了——从事件日志自动长出第一张流程模型。

---

*BPI 课程播客 © 2026 · 基于 RWTH Aachen BPI SS 2026 课件制作*
