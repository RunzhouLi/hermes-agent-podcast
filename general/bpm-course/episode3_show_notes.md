# EP03 Show Notes v1.2

**《BPM 流程解码》第三集：流程中的“人”与“对话”——资源、消息、OR 网关与模型质量**

本集 v1.2 根据试听反馈重写了口播脚本：不压缩时长，优先提高听懂率；每个重要术语按“中文术语 → English term → 简单解释 → 小例子”的顺序进入；晓雨作为学习者主持人负责放慢节奏、复述和追问。

**本集核心内容：**

**一、组织结构的可视化（Resources）**
- 资源（Resource）：执行流程的人、角色、部门、组织或系统。
- 池（Pool）：代表一个独立业务参与者或组织边界。
- 泳道（Lane）：池内部的部门或角色，用来说明谁负责哪个任务。
- 协作图（Collaboration Diagram）：多个池放在一起，展示多方如何协作完成一个端到端流程。
- 白盒参与者（White-box Participant）：内部流程可见，任务、泳道、网关都画出来。
- 黑盒参与者（Black-box Participant）：内部流程不展示，只暴露和外部的消息接口。

**二、跨组织通信（Messages）**
- 消息（Message）：跨组织边界传递的信息或物品。
- 消息流（Message Flow）：虚线箭头，只能跨池连接。
- 顺序流（Sequence Flow）：实线箭头，只能在同一个池内部连接。
- 接收任务、发送任务、消息开始事件、中间消息事件、消息结束事件。
- 消息和数据的区别：消息强调“传递动作”；数据对象强调“具体内容”。
- 设计不当的发送/接收顺序可能导致通信死锁。

**三、包容性网关（OR Gateway / Inclusive Gateway）**
- 拆分语义：检查所有条件，满足的路径全部激活，可能是一条，也可能是多条。
- 默认路径（Default Flow）：防止没有任何条件满足时流程无路可走。
- 合并语义：只等待实际被激活的分支；节目中用“友好的公交车司机”类比解释。
- 风险提示：两个 OR 合并网关互相等待可能造成死锁。
- 建模建议：非必要少用 OR 网关；不要让 OR 合并网关互相依赖。

**四、流程模型质量（Model Quality）**
- 结构正确性（Structural Correctness）：像语法，图形符号和连接方式要合法。
- 行为正确性（Behavioural Correctness）：像逻辑，流程要能顺利走完，不能卡死。
- 健全性（Soundness）：包括可完成性（Option to Complete）、无死活动（No Dead Activities）和正确完成（Proper Completion）。
- 语义正确性（Semantic Correctness）：模型内容要符合真实业务。
- 模型约定（Model Conventions）：命名、布局、规模、风格要便于团队阅读和维护。

**五、本周练习题**

本周共有 5 道练习。节目中重点讲解前三道，第四、第五题作为课后挑战保留。

- 练习一：用 Token Game 检查 Soundness，识别死锁和死活动。
- 练习二：车险理赔协作图，练习 Pool、Lane、White-box、Black-box 和 Message Flow。
- 练习三：评估大学课程注册流程的语义正确性和模型约定。
- 练习四：更完整的理赔流程建模，加入系统和多个岗位资源。
- 练习五：高级行为正确性，构造语法正确但违反健全性性质的模型。

**下期预告（Week 04）：**
子流程（Sub-processes）、数据（Data）、基于事件的网关（Event-Based Gateway）、定时器事件（Timer Events）。

**出处说明：**
- v1.0 raw draft: Gemini CLI terminal client (`gemini-2.5-pro`)
- v1.1 cleanup/finalization: Claude CLI terminal client (`claude-sonnet-4-6`)
- v1.1 pre-publish review: Gemini CLI terminal client (`gemini-3.1-pro-preview`)
- v1.2 listening-comprehension rewrite: Gemini CLI terminal client (`gemini-3.1-pro-preview`)
- TTS rendering: Doubao / Volcengine TTS via `doubao-speech` CLI after Gemini TTS quota exhaustion; current resource authorizes `zh-female-warm`, so both dialogue speakers are rendered with that provider voice; provider-natural speed, no 0.9x slowdown.

课程原材料：Sander Leemans，Fundamentals of Business Process Management，Week 03 讲义（Resources, Messages, OR Gateway, Quality 1 & 2, Exercises Week 03）。
