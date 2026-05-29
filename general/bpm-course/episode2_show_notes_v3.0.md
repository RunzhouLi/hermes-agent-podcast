# EP02 节目说明 — BPMN 基础与网关：用地图和弹珠学会流程建模

## 基本信息
- **集数**: 第 2 集
- **版本**: v3.0（启发式四阶段教学 + 地图隐喻 + 独立审查）
- **时长**: 约 24:03
- **来源**: Week 02 - BPMN Basics & Gateways

## 制作溯源
| 阶段 | 工具/模型 | 细节 |
|------|-----------|------|
| v2.0 原版 | Gemini CLI gemini-3.1-pro-preview | 声明式教学 |
| v3.0 重制 | Claude CLI claude-opus-4-8 | 启发式四阶段教学 + 地图/小球贯穿隐喻 |
| 独立审阅 | Gemini CLI gemini-3.1-pro-preview | NEEDS_FIX (2项) → GO_AFTER_FIX |
| 修复 | Hermes | Exercise 4 循环入口 XOR 网关 + Implicit Join/Split 英文术语补充 |
| TTS 渲染 | Doubao/Volcengine seed-tts | 116 片段，100% Doubao；自然语速；zh-female-warm |

## 覆盖内容
- BPMN 定义与受众（OMG, ISO 19510，从老板到程序员）
- 四大基础元素：Task（圆角矩形）、Sequence Flow（实线箭头）、Start Event（细圈）、End Event（粗圈）
- 令牌 Token 概念与"蓝色小球"Token Game
- 流程实例生命周期：Option 1（有头有尾）vs Option 2（靠箭头起止），严禁混用
- XOR 网关：互斥性 + 完备性 + 默认流，汇合来一个放一个
- AND 网关：并行分裂 + 同步汇合（synchronization）
- 隐式网关坏习惯：Implicit Join / Implicit Split
- Exercise 3 信用风险评估（XOR + AND 组合）
- Exercise 4 保险理赔循环（XOR 回路 + 循环入口网关防呆）
- v3.0 新增：循环的正确画法——回路箭头必须经过 XOR 网关再进任务

## 教学亮点
采用完整的启发式教学四阶段（引出困惑→探索问题→给出框架→重述锁死）。"地图+蓝色小球"作为贯穿隐喻，每段过渡使用因果桥接。Host A（晓雨）不再是简单的"然后呢"，而是主动猜测、推理、甚至踩坑——比如自己猜出 Token 概念、Option 2 规则、AND 网关逻辑。Exercise 4 中 B 故意等 A 画出隐式汇合后才纠正，形成"防坑教学"。
