# EP09 节目说明 — 流程发现与流程挖掘：像侦探一样画出现状

## 基本信息
- **集数**: 第 9 集
- **版本**: v2.0
- **时长**: 约 20:37
- **来源**: Week 09 - Process Discovery & Process Mining（Lecture Slides 36 页 + Exercises 4 题）

## 制作溯源 (Provenance)
| 阶段 | 工具/模型 | 细节 |
|------|-----------|------|
| 启发式重写 | Gemini CLI gemini-3.1-pro-preview | yolo mode；四阶段启发式教学 + 架构锚点 + 侦探类比 |
| 独立审阅 | Gemini CLI gemini-3.1-pro-preview | NEEDS_FIX（缺学生录取案例 + 研讨会包容性陷阱）；GO_AFTER_FIX |
| 修订定稿 | Hermes Autoproducer | 2 项修订：学生录取案例整合到访谈/研讨会，补充包容性陷阱 |
| TTS 渲染 | Doubao/Volcengine seed-tts | doubao-speech wrapper；自然语速；zh-female-warm 单音色；119 片段 |
| 音频 | 100% Doubao/Volcengine | 无 Gemini TTS fallback；无 0.9x 后处理 |

## 覆盖内容
本集覆盖 Week 09 Process Discovery & Process Mining 的全部教学内容与课后练习：

### Part 1: Process Discovery（流程发现）
- **四个任务**: Define the setting → Gather information → Conduct the modelling → Assure model quality
- **三个挑战**: 碎片化知识、实例级思维、对流程领域不熟悉
- **三种方法**: 基于证据（文档分析 + 观察）、基于访谈（正向/逆向/结构化/非结构化）、基于研讨会（Facilitator 促进者角色）
- **研讨会陷阱**: 包容性与文化敏感——权级差异下人们不敢说真话
- **模型质量**: Verification（语法正确）→ Validation（符合现实）→ Certification（签字确认）
- **时间估算**: 10个活动 × 14个工作日 ≈ 3周（完美条件）

### Part 2: Process Mining（流程挖掘）
- **事件日志**: IT系统里的"监控录像"
- **点图**: 批处理 vs 到达率 vs 异常事件
- **三大用途**: Discovery（自动生成模型）、Conformance Checking（一致性检查）、Enhancement（增强）
- **模型质量三维度**: Fitness（适配度）、Precision（精确度）、Simplicity（简洁度）
- **花模型陷阱**: 100%适配但零约束
- **重要洞察**: 并非所有偏差都是问题——Not all deviations are problems

### 课后练习
- Exercise 1: 学生录取文档分析（形成假设）
- Exercise 2: Mary Adams / Louise Smith / Peter Capello 三人访谈整合
- Exercise 3: 招生官 + 学术委员会研讨会（包容性陷阱）
- Exercise 4: 维也纳公交公司 CFO 数据仪表板

## 关键术语
- 流程发现 (Process Discovery)
- 现状模型 (as-is process model)
- 碎片化知识 (Fragmented Process Knowledge)
- 实例级思维 (Instance-Level Thinking)
- 促进者 (Facilitator)
- 验证 (Verification) / 校验 (Validation) / 认证 (Certification)
- 流程挖掘 (Process Mining)
- 事件日志 (Event Log)
- 点图 (Dotted Chart)
- 一致性检查 (Conformance Checking) / 增强 (Enhancement)
- 适配度 (Fitness) / 精确度 (Precision) / 简洁度 (Simplicity)

## 贯穿类比
侦探破案：访谈目击者 + 调取监控录像。流程发现（靠人）和流程挖掘（靠数据）是印证真相的两道防线。

## 教学亮点
本集采用**启发式教学**（v2.0 新技能），每个概念走"困惑→探索→框架→复述"四阶段，晓雨先猜再学，全程侦探类比贯穿六个转折点。
