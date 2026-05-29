# EP03 v3.0 Show Notes

**《BPM 流程解码》第三集：流程中的"人"与"对话"——资源、消息、OR 网关与模型质量**

本集 v3.0 采用启发式教学法（Heuristic Teaching）重制，以"地图与旅行者"为贯穿比喻，每个核心概念经过 Phase 1-4 四阶段探索节奏。

---

**本集核心内容：**

**一、组织结构的可视化（Resources）**
- 池（Pool）：独立组织/参与者的管辖边界 — 地图上的"国家"
- 泳道（Lane）：池内部的部门/角色 — 国家内的"省"
- 协作图（Collaboration Diagram）：多个池放在一起的多方合作图
- 白盒参与者（White-box Participant）vs 黑盒参与者（Black-box Participant）：透明建筑 vs 不透明建筑

**二、跨组织通信（Messages）**
- 消息流（Message Flow）：虚线箭头 — 国家之间的"桥梁"
- 顺序流（Sequence Flow）：实线箭头 — 国家内部的"道路"
- 消息（Message）vs 数据（Data）：信封 vs 信纸
- 通信死锁（Communication Deadlock）：两个池互相等消息

**三、包容性网关（OR Gateway / Inclusive Gateway）**
- OR split 语义：允许激活一条或多条路径（从 XOR/AND 不够用的场景推导）
- 默认路径（Default Path）：防止所有条件都不满足时流程卡死
- OR join"友好公交车司机"：等待所有实际被激活的 Token
- OR join 互相等待死锁（Waiting for one another）：两个 OR join 互相依赖导致流程卡死

**四、流程模型质量（Model Quality）**
- 四层质量框架（从问题推导，不是 checklist）：
  - 结构正确性（Structural Correctness）：语法对不对
  - 行为正确性（Behavioural Correctness / Soundness）：能不能走通（Option to Complete / No Dead Activities / Proper Completion）
  - 语义正确性（Semantic Correctness）：画的是不是真实世界
  - 模型惯例（Model Conventions）：别人看不看得懂
- 质量保证（Quality Assurance）：前两层靠电脑自动检查，后两层必须人工同行评审（Peer Review）

**五、本周练习题**
- 练习一：Token Game 检查 Soundness — 互动式玩 token
- 练习二：车险理赔协作图 — 白盒/黑盒/消息流
- 练习三：大学课程注册 — 语义正确性和模型约定
- 练习四（课后）：更完整的理赔流程建模
- 练习五（课后）：高级行为正确性挑战

**下期预告（Week 04）：**
子流程（Sub-processes）、数据（Data）、基于事件的网关（Event-Based Gateway）、定时器事件（Timer Events）

**v3.0 改进亮点：**
- 🗺️ 地图比喻贯穿全篇（Pool=国家、Message Flow=桥梁、Token=旅行者、OR=检查站）
- 🔍 启发式四阶段深度：每个核心概念在"制造困惑→自主探索→框架给出→锁定验证"中完成
- 🔗 架构锚定：段落转换使用因果桥梁，不是 checklist 式过渡
- 🎙️ Host A（晓雨）作为探索催化剂：在 B 给答案前主动尝试推理
- 📐 人机分工：新增 Quality Assurance 的人 vs 计算机分工讲解
- ✅ 三处审稿修复：OR Join 死锁语义纠正 / 术语例句补全 / QA 机制补充

**出处说明：**
- v3.0 draft: Gemini CLI gemini-3.1-pro-preview
- v3.0 review: Gemini CLI gemini-3.1-pro-preview（Claude CLI 不可用时的自审）
- v3.0 fixes: Hermes Agent（3 项审稿发现）
- Audio: Doubao/Volcengine TTS, zh-female-warm, natural speed
