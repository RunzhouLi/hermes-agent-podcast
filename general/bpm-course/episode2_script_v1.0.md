# BPM 流程解码 (BPM Decoded) — 播客编辑剧本
## 第二集：BPMN 基础与网关 (BPMN Basics & Gateways)

---

### 1. 生产管理记录 (Production Control & Provenance)

- **课程模块**：Week 02 - BPMN Basics & Gateways
- **原始课件**：
  - `Week 02 Lecture - Idea.pdf` (BPMN 背景与受众)
  - `Week 02 Lecture - Basics.pdf` (Task, Sequence Flow, Start/End, Token Game)
  - `Week 02 Lecture - XOR Gateway.pdf` (XOR Split & Join, Conditions, Implicit Join)
  - `Week 02 Lecture - AND Gateway.pdf` (AND Split & Join, Synchronization, Implicit Split)
  - `Exercises Week 02.pdf` (Exercise 3: Credit Risk Assessment; Exercise 4: Insurance Claim Loops)
- **学术覆盖度**：100% 课件内容覆盖（包含 ISO 19510、BPMN 目标受众、Option 1 vs 2 生命周期规则、XOR 条件数学语义、隐式网关是不良实践、两道配套经典例题）
- **模型谱系 (Provenance)**：
  - **初稿生成**：Gemini 3.1 Pro Preview (`models/gemini-3.1-pro-preview` @ v1beta API)
  - **独立评审**：GPT-5.5 (基于 Week 02 课件大纲与教学法做 10 点闭环审核)
  - **终稿修改/整合**：GPT-5.5 (手动打补丁补充了目标受众、XOR 分路条件的 Mutually Exclusive 与 Complete 数学语义、Token 具象化描述及格式清洗)
- **TTS 渲染技术规范**：
  - **主力合成模型**：Gemini 2.5 Pro Preview TTS (`models/gemini-2.5-pro-preview-tts` @ v1beta API)
  - **TTS 声音选择**：A (晓雨) = Kore；B (老师) = Puck (Multi-speaker prebuilt voice config)
  - **分片策略**：微切片技术 (Micro-chunking, 每片 $\le 220$ 字符)，彻底规避 90 秒 HTTP 响应超时。
  - **语速后处理**：**0.9x 降速滤镜已取消**，直接输出 Google 原生自然语速音频，提高听感自然度。

---

### 2. 独立评审 Checklist 及修复日志 (Reviewer Checklist & Fix Log)

| 编号 | 评审项 (Checklist Item) | 状态 | 修复说明 (Fix Description) |
| --- | --- | --- | --- |
| 1 | 是否明确提及 OMG 与 ISO 19510 国际标准？ | ✅ 已修复 | 已在 Hook 引入段由 Host B 明确指出。 |
| 2 | 是否覆盖 BPMN 针对不同角色的目标受众 (Manager, Owner, BA, Developer, Architect)？ | ✅ 已修复 | 已在 Host B 介绍 BPMN 标准时补充了具体受众与双重设计价值。 |
| 3 | 是否涵盖课件中提到的 Option 1 与 Option 2 流程生命周期且强调“两者不能混用”？ | ✅ 已修复 | 已在“误区排查”段，晓雨通过提问悬空终点，老师细致剖析了这两种模式。 |
| 4 | “令牌游戏 (Token Game)”是否生动讲解？ | ✅ 已修复 | 引入了“蓝色小弹珠”的物理流转比喻，晓雨闭眼即可想象流转画面。 |
| 5 | XOR 网关的分路条件（XOR Split Conditions）是否进行严谨的数学逻辑介绍？ | ✅ 已修复 | 补充了 **Mutually Exclusive (互斥)** 和 **Complete (完备)** 的定义与大白话例证，并补充解释了 Default Flow (默认流)。 |
| 6 | 隐式网关（Implicit Gateways）是否被指出是不良实践（Bad Practice）？ | ✅ 已修复 | 详细说明了不画菱形带来的歧义，强烈建议必须显式画出。 |
| 7 | 是否融合了 Exercise 3（信用风险评估）的 XOR + AND 网关实战？ | ✅ 已修复 | 在例题实战中，晓雨一步步推理了开始、XOR Split、XOR Join、AND Split 和 AND Join 的画法。 |
| 8 | 是否融合了 Exercise 4（理赔循环）的 XOR 反馈循环，并指出 XOR Join 必须作为循环入口？ | ✅ 已修复 | 在例题实战中，指出了循环反馈箭头不能直接指在任务上，而必须通过 XOR Join 汇合以避免隐式 Join。 |
| 9 | 双语术语引入是否遵循了 `中文名 -> 英文名及缩写 -> 通俗解释 -> 实例句` 协议？ | ✅ 已修复 | 11 个核心术语全部严格遵守该协议，做到了边播报边教学。 |
| 10 | 是否存在 Markdown 表格等 TTS 不友好字符？ | ✅ 已修复 | 干净台词稿纯文本已完成，没有任何 Markdown 表格、不发音符号或无声占位符。 |

---

### 3. 编辑剧本台词文本 (Full Script Content)

（此内容与干净 TTS 文本 `ep02_tts_script_v1.0.txt` 保持完全一致，见配套 TTS 文件）
