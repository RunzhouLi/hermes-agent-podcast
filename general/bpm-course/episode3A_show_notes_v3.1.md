# EP03A v3.1 — 边界、桥梁与 OR 检查站 (Show Notes)

**版本：** v3.1（Claude Opus 4.8 完整启发式重制，拆分为 A/B 两集）
**来源：** Week 03 — Resources, Messages, OR Gateway
**时长：** 29:22
**脚本：** Claude CLI claude-opus-4-8 启发式教学初稿；Gemini CLI gemini-3.1-pro-preview 对比审阅 PASS WITH MINOR FIXES；Hermes 应用 2 项修订
**TTS：** 100% Doubao/Volcengine seed-tts，自然语速，zh-female-warm 单音色

---

## 本集内容

本集覆盖 Week 03 前半：**组织建模（Pool/Lane）、跨组织通信（Message Flow）与 OR 包容网关**。用"地图"贯穿隐喻——Pool=国家边界、Lane=省内部门、消息流=国际桥梁、OR=复杂检查站。

### 第一部分：边界——Pool 与 Lane
- Pool 表示独立组织或管辖区域（地图上的"国家"）
- Lane 表示组织内的部门或角色（地图上的"省"）
- Lane 可嵌套、可交叠（矩阵式组织）
- 协作图（Collaboration Diagram）：多参与方共同执行的流程
- 白盒（White-box）vs 黑盒（Black-box）：内部完全透明 vs 只有边界轮廓
- 建模决策：画角色不画个人；系统（如 ERP）也是可建模的资源
- 完整示例：订单到收款（Order-to-Cash）——卖方两部门×ERP系统×客户黑盒

### 第二部分：桥梁——消息流
- 同 Pool 内：Token 沿实线顺序流移动（国内公路）
- 跨 Pool：必须用虚线消息流（国际桥梁），带空心箭头
- 消息接收在任务执行之前，发送在任务执行之后
- 消息（Message）是信封，数据（Data）是信纸
- 通信死锁：两 Pool 互相等信，流程卡死

### 第三部分：OR 包容网关——边境检查站
- 语法：戴圈的菱形，每条非默认出路须有条件
- 真值表四种情况：a∧¬b, ¬a∧b, a∧b, ¬a∧¬b
- 默认流兜底：防止小球无路可走
- OR Join "友善公交车司机"语义：回看上游激活几条路，等齐实际发出的球再开走
- 两个 OR Join 互相依赖死锁：未定义行为，绝对禁止
- 收尾警告：能不用就不用；敢说"完整支持 OR Join"的，掉头就跑

---

## 关键英语术语

| 中文 | English | 缩写 |
|------|---------|------|
| 池 | Pool | — |
| 泳道 | Lane | — |
| 协作图 | Collaboration Diagram | — |
| 白盒 | White-box pool | — |
| 黑盒 | Black-box pool | — |
| 顺序流 | Sequence Flow | SF |
| 消息流 | Message Flow | MF |
| OR网关/包容网关 | OR Gateway / Inclusive Gateway | — |
| 默认流 | Default Flow | — |
| 死锁 | Deadlock | — |

---

## 参考
- Week 03 Lecture — Resources.pdf (9 slides，含完整Order-to-Cash示例)
- Week 03 Lecture — Messages.pdf (5 slides，含死锁情景)
- Week 03 Lecture — OR Gateway.pdf (8 slides，含真值表/公交车司机/OR Join未定义)

---

## 生成溯源

| 阶段 | 工具 | 结果 |
|------|------|------|
| 脚本初稿 | Claude CLI claude-opus-4-8 | 295段对话，5万字 |
| 对比审阅 | Gemini CLI gemini-3.1-pro-preview | PASS WITH MINOR FIXES（2项修正）|
| 修订 | Hermes Agent | OR条件措辞+Ex3教室预订修正 |
| 拆分 | Hermes Agent | 拆为 EP03A（边界+桥梁+OR）与 EP03B（质量+习题）|
| 音频 | Doubao/Volcengine zh-female-warm | 164段，100% Doubao，29:22 |

**对比 v3.0：** v3.0（Gemini 生成）仅 59 段、12 分钟，用检查清单式过渡、大部分概念缺乏 Host A 探索阶段、完全遗漏 ERP/SAP 系统资源讨论和中断问题讨论。v3.1 用完整启发式四阶段（Hunger→Explore→Construct→Anchor），Host A 在每一项关键概念均做独立试探后才由 Host B 给出框架，共 300 段对话、一拆为二后每集 25–30 分钟。