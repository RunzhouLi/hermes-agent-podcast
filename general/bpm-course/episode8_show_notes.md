# EP08 节目说明 — 流程识别：梳理流程架构，挑对流程下手

## 基本信息
- **集数**: 第 8 集
- **版本**: v1.1
- **时长**: 约 51:41
- **来源**: Week 08 - Process Identification（Lecture Slides 30 页 + Exercises 4 题）

## 制作溯源 (Provenance)
| 阶段 | 工具/模型 | 细节 |
|------|-----------|------|
| 初稿生成 | Claude CLI claude-opus-4-7 | session fbebaf33-636d-4506-b534-226bcd2a51ed |
| 独立审阅 | Gemini CLI gemini-3.1-pro-preview | TUI 交互；NEEDS_FIX → GO_AFTER_FIX |
| 修订定稿 | Hermes Autoproducer | 3 项审阅修订（P0/P1/P2） |
| TTS 渲染 | Doubao/Volcengine seed-tts | doubao-speech wrapper；自然语速；zh-female-warm 单音色；281 片段 |
| 音频 | 100% Doubao/Volcengine | 无 Gemini TTS fallback；无 0.9x 后处理 |

## 覆盖内容
本集覆盖 Week 08 Process Identification 的全部教学内容与课后练习：

### Designation（流程枚举与范围界定）
- Process Identification 在 BPM 生命周期中的位置
- 流程架构三级：Landscape → Business Process → Sub-process
- 三类流程（Porter 1985）：Core / Support / Management
- 流程范围界定三个维度：专门化（Specialisation）、水平（Horizontal）、垂直（Vertical）
- 三种流程关系：Sequence（序列）、Decomposition（分解）、Specialization（专门化）
- 水平边界判断四准则
- 价值链（Value Chain）与全景模型（Landscape Model）
- APQC 流程分类框架（PCF）

### Prioritisation（流程优先级排序）
- 三步标准：重要性（Importance）、健康度（Health）、可行性（Feasibility）
- 绩效度量三维度：成本（Cost）、时间（Time）、质量（Quality）
- 流程组合矩阵（Process Portfolio Matrix）

### 常见陷阱
- 七个流程识别常见错误（范围不清、过窄/过宽、孤立识别、利益相关者参与不足、成员选择不当、引导技能差）

### 课后练习
- Exercise 1: RWTH 流程架构（学生生命周期）
- Exercise 2: 流程架构价值（融入正文讨论）
- Exercise 3: 旅行社案例分析与改进建议
- Exercise 4: 大学流程组合矩阵与优先级排序

## 关键术语
- 流程识别 (Process Identification / PI)
- 流程枚举 (Process Enumeration)
- 流程范围界定 (Process Scoping)
- 核心流程 (Core Processes)
- 支持流程 (Support Processes)
- 管理流程 (Management Processes)
- 价值链 (Value Chain)
- 全景模型 (Landscape Model)
- APQC 流程分类框架 (APQC PCF)

## 稳定类比
医院分诊：先搞清楚有哪些科室（Designation），再决定哪个病人先看（Prioritisation）。
