# EP02 — Data Science: Supervised Learning · 课程笔记

**发布时间：** 2026-06-05
**时长：** ~45 分钟（待验证）
**讲稿：** Claude Opus 4.8 (TUI) · 审阅：Gemini 3.1 Pro (PASS/GO) · TTS：Doubao/Volcengine zh-female-warm
**课件：** BPI L2, RWTH Aachen SS 2026, Prof. Wil van der Aalst (135 slides)

---

## 本集概要

这门课叫 Business Process *Intelligence*——那个 Intelligence 从哪来？答案：数据。本集从流程挖掘的事件日志出发，搭建"情境表"这个桥梁，把流程数据送入机器学习的轨道。核心角色是监督学习中分类算法的经典代表——**决策树 (Decision Tree)**。

## 核心概念

- **情境表 (Situation Table)**：流程挖掘通往机器学习的接口——把事件日志"拍扁"成一行一个案例的宽表
- **监督学习 (Supervised Learning)**：从带标签的数据中学习，标签 = Response Variable（响应变量）
- **分类 vs 回归 (Classification vs Regression)**：预测"类别" vs 预测"数值"
- **决策树 (Decision Tree)**：通过递归分裂数据来降低不确定性，每一步选信息增益最大的属性
- **熵 (Entropy)**：衡量不确定性的度量——0 = 完全确定，最大值 = 各类均匀分布
- **信息增益 (Information Gain)**：熵的减少量 ≠ 分类准确率提高。信息增益衡量的是"更确定"，不是"判得更对"
- **过拟合 vs 欠拟合 (Overfitting vs Underfitting)**：树太简单漏规律，树太复杂学噪声
- **混淆矩阵 (Confusion Matrix)**：TP/TN/FP/FN 四象限评估分类效果

## 关键术语

| 中文 | English | 说明 |
|---|---|---|
| 监督学习 | Supervised Learning | 用带标签的数据学习 |
| 分类 | Classification | 预测离散类别 |
| 回归 | Regression | 预测连续数值 |
| 决策树 | Decision Tree | 递归分裂分类器 |
| 熵 | Entropy | 不确定性度量 |
| 信息增益 | Information Gain | 分裂前后熵的减少量 |
| 过拟合 | Overfitting | 模型记住了噪声 |
| 欠拟合 | Underfitting | 模型错过了规律 |
| 情境表 | Situation Table | PM→ML 的数据桥梁 |
| 混淆矩阵 | Confusion Matrix | TP/TN/FP/FN 评估表 |
| 流经时间 | Flow Time / TPT | 案例从开始到结束的时间 |

## 核心算法

- **ID3** (Iterative Dichotomiser 3, Quinlan 1986)：基本决策树算法
- **C4.5 / C5.0**：支持连续特征、缺失值、后剪枝的进阶版
- **J48**：C4.5 的开源实现（Weka）
- **CART** (Classification and Regression Trees)：使用 Gini 指数，同时支持分类和回归
- **CHAID**：用卡方检验决定分裂点

## 下集预告

EP03 — Data Science: Unsupervised Learning and Evaluation。没有标准答案也能学习——聚类、关联规则、模型评估方法。

---

*BPI 课程播客 © 2026 · 基于 RWTH Aachen BPI SS 2026 课件制作*
