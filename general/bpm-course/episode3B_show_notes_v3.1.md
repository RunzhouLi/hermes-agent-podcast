# EP03B v3.1 — 流程地图质检 (Show Notes)

**版本：** v3.1（Claude Opus 4.8 完整启发式重制，拆分为 A/B 两集）
**来源：** Week 03 — Quality (Parts 1 & 2), Exercises Week 03
**时长：** 25:26
**脚本：** Claude CLI claude-opus-4-8 启发式教学初稿；Gemini CLI gemini-3.1-pro-preview 对比审阅 PASS WITH MINOR FIXES；Hermes 应用 2 项修订
**TTS：** 100% Doubao/Volcengine seed-tts，自然语速，zh-female-warm 单音色

---

## 本集内容

本集是 EP03A 的下半部分，从中场地图检查开始，转入**流程模型质量检验**：如何判断一张 BPMN 图到底是不是好图。最后逐题演练 Week 03 的全部 5 道习题。

### 第一块回顾——中场地图检查
- Host A 回看上半集三站：边界（Pool/Lane/白盒黑盒）、桥梁（Message Flow/消息vs数据/死锁）、检查站（OR Split/Join/双OR死锁）
- Host B 引出下半集主题：从画地图变为检查地图

### 第二块——质量框架：Models 的语言构成
- 语法（Syntax）：有哪些元素、连接规则
- 语义（Semantics）：元素及连接的含义
- 记法（Notation）：如何可视化
- 文字质量（Textual Quality）：乱写标签直接摧毁流程图可信度

### 第三块——四层质量金字塔（从底到顶）
**第一层：结构正确性（Structural Correctness）**
- 弧必须连接节点；开始/结束事件成对
- 开始事件不能有入向顺序流；结束事件不能有出向顺序流
- 网关必须有多于一条进或多于一条出的顺序流（一进一出是废物）
- XOR 出路必须带条件或默认流

**第二层：行为正确性 / 健全性（Behavioural Correctness / Soundness）**
- 小球玩法亲手体验：AND 分裂→XOR 支路→AND 合并的死锁陷阱
- 可完成性（Option to Complete）：每次都能走到完成，无死锁/活锁
- 无死任务（No Dead Activities）：每个任务至少能被某个实例执行
- 正确完成（Proper Completion）：结束时没有遗留小球

**第三层：语义正确性（Semantic Correctness）**
- 图和真实业务对不对得上（如"先发货后收款" vs "先收款后发货"）
- 语法对、小球跑得通，但语义全错——这层机器查不了

**第四层：模型惯例（Model Conventions）**
- 命名规范：任务=动词+名词，事件=名词+已发生，条件=引用数据
- 排版规范：左上到右下、少交叉、超过30个元素拆图
- 语法限制：团队约定避免 OR 网关
- Proper Completion 作为横跨行为与惯例的灰色地带

### 第四块——谁来质检：电脑 vs 人
- 结构层：电脑（语法检查器、建模工具）
- 行为层：人机各半——模型检验受限（非正式 BPMN 语义 + Halting Problem）
- 语义层：全靠人（领域专家、同行评审、评审会、签字）
- 惯例层：人机配合——定制语法检查器可查形式规则，可读性靠人感受
- **核心区分：机器管形式，人管意义**

### 第五块——5 道习题逐题讲解
1. 行为正确性——小球游戏诊断循环漏洞
2. 汽车理赔——白盒/黑盒 Pool/Lane/消息流综合建模
3. 大学课程组织——语义正确性（教室预订提前于确认报名人数）+ 惯例改进
4. 理赔流程——SAP 系统作为资源，白盒/黑盒取舍
5. 进阶——故意造三张"语法对但各违反一条行为性质"的反例图

---

## 关键英语术语

| 中文 | English | 缩写 |
|------|---------|------|
| 结构正确性 | Structural Correctness | — |
| 行为正确性 / 健全性 | Behavioural Correctness / Soundness | — |
| 语义正确性 | Semantic Correctness | — |
| 模型惯例 | Model Conventions | — |
| 可完成性 | Option to Complete | — |
| 无死任务 | No Dead Activities | — |
| 正确完成 | Proper Completion | — |
| 停机问题 | Halting Problem | — |
| 模型检验 | Model Checking | — |
| 同行评审 | Peer Review | — |

---

## 生成溯源

| 阶段 | 工具 | 结果 |
|------|------|------|
| 脚本初稿 | Claude CLI claude-opus-4-8 | 295段对话 |
| 对比审阅 | Gemini CLI gemini-3.1-pro-preview | PASS WITH MINOR FIXES (2项) |
| 修订 | Hermes Agent | OR条件措辞+Ex3预订教室修正 |
| 拆分 | Hermes Agent | EP03A 164段 + EP03B 136段 |
| 音频 | Doubao/Volcengine zh-female-warm | 300段，100% Doubao |