# EP03 Show Notes

**《BPM 流程解码》第三集：流程中的"人"与"对话"——资源、消息、OR 网关与模型质量**

本集晓雨和老师把"人"与"组织"正式引入 BPMN 流程图，覆盖了资源建模、跨组织通信、包容性决策网关，以及系统性的模型质量评估框架；练习部分重点推演前三道代表题，并把第 4、5 题作为课后挑战说明。

**本集核心内容：**

**一、组织结构的可视化（Resources）**
- 池（Pool）：代表一个独立的业务参与者，拥有自己完整的流程边界
- 泳道（Lane）：位于池内，标注任务由哪个部门、角色或系统执行；支持嵌套和交叠
- 协作图（Collaboration Diagram）：包含两个或以上池的 BPMN 图，展示多方协同的端对端流程
- 白盒参与者（White-box Participant）：内部流程详细建模，可见泳道、任务、网关
- 黑盒参与者（Black-box Participant）：内部流程不展示，只呈现与外部的消息接口
- 建模原则：对内部流程与建模目的相关的参与者用白盒；消费者、学生等无结构化流程的方用黑盒

**二、跨边界通信（Messages）**
- 消息（Message）：代表池与池之间传递的信息或物品，用虚线消息流表示
- 顺序流 vs. 消息流：实线连池内，虚线连池间——这是 BPMN 的基本规则
- 消息语法：接收任务（先收消息再工作）、发送任务（先工作再发消息）、消息开始/中间/结束事件
- 消息 vs. 数据：消息是跨池的通信行为；数据对象是流程内部流转的具体内容
- 风险提示：设计不当的消息顺序可能导致通信死锁

**三、包容性网关（OR Gateway / Inclusive Gateway）**
- 拆分语义：评估所有出路的条件，满足条件的路径全部激活（可一条，可多条）；必须有默认路径防止无路可走
- 合并语义（"友好的公交车司机"）：只等待所有"实际上被激活"的分支，不等未激活的分支
- 核心风险：两个 OR 合并网关相互依赖会导致死锁，属于未定义行为
- 最佳实践：非必要不使用；永远不要让两个 OR 合并网关相互依赖

**四、流程模型质量（Quality）**

四个独立的质量维度，类比写文章：

| 维度 | 英文 | 类比 | 如何保证 |
|---|---|---|---|
| 结构正确性 | Structural Correctness | 语法 | 建模工具自动检查 |
| 行为正确性 | Behavioural Correctness | 逻辑（健全性 Soundness） | 逻辑推演 + 模型检查工具 |
| 语义正确性 | Semantic Correctness | 内容真实性 | 领域专家评审、签字 |
| 模型约定 | Model Conventions | 写作风格规范 | 团队规范 + 同行评审 |

关键行为正确性要求：可完成性（option to complete，无死锁）+ 无死活动（no dead activities）

常见模型约定：从左到右布局、活动名"动词+名词"、事件名"名词+过去分词"、单模型不超 30 元素、避免 OR 网关

**五、本周练习题**

本周共有 5 道练习。节目中重点推演前三道代表题，帮助听众巩固本集主线；第 4、5 题建议课后挑战。

- 练习一：Token 游戏验证健全性（Soundness），识别死锁和死活动，并修复
- 练习二：车险理赔协作图建模——白盒/黑盒资源分配 + 消息流设计
- 练习三：评估大学课程组织流程模型的语义正确性和模型约定，并改写
- 练习四：更完整的理赔流程建模，纳入 SAP System、Claims Officer、Senior Claims Officer、Claims Management System 等资源
- 练习五：Advanced behavioural correctness，构造违反不同健全性性质的语法正确模型

**下期预告（Week 04）：**
子流程（Sub-processes）、数据（Data）、基于事件的网关（Event-Based Gateway）、定时器事件（Timer Events）

**出处说明：**
Raw draft attempted and generated via Gemini CLI terminal client (`gemini-2.5-pro`)；终稿清理、补全及定稿由 Claude CLI terminal client (`claude-sonnet-4-6`) 完成；发布前 review 由 Gemini CLI terminal client (`gemini-3.1-pro-preview`) 完成；整个内容生产流程均在本地终端完成，未直接调用 Gemini API 或 Claude API 进行内容生成。

课程原材料：Sander Leemans，Fundamentals of Business Process Management，Week 03 讲义（Resources, Messages, OR Gateway, Quality 1 & 2, Exercises Week 03）

---
