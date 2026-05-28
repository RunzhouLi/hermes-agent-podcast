# 第 06 集：行为正确性与 BPMN 信号（BPMN Model Correctness & Signals）

版本：V1.1  
来源：Week 06 — BPMN Model Correctness & Signals  
时长：00:41:10  
音频：Volcengine/Doubao seed-tts via doubao-speech wrapper; natural speed; single voice  
Codex usage: none.

## 本集简介

这一集专注于 BPMN 模型质量中的核心考点——行为正确性（Behavioural Correctness）与信号事件（Signal Events）。我们不仅会讨论静态的符号语法，还会用生动的“令牌游戏 (Token Game)”把流程模型变活，透彻剖析死锁（Deadlock）与缺少同步（Lack of Synchronization）的本质区别。此外，本集还会深度对比“信号 (Signal)”与“消息 (Message)”在 BPMN 通信语义中的关键差异（广播式 vs 定向式），并结合 Week 06 的典型练习题进行场景演练。

## 你会学到

1. 模型质量的五个维度：什么是结构正确性、语法正确性、语义正确性、行为正确性与模型约定。
2. 令牌游戏与行为正确性：如何通过“令牌（Token）”流动模拟来推导流程在运行时是否会卡死。
3. 池内反模式与死锁：大白话拆解排他分流（XOR-split）接并行汇合（AND-join）所导致的死锁悲剧。
4. 死锁 vs 缺少同步：彻底分清“卡住了（永远等不到令牌）”和“漏掉等待（流程提前跑完）”的区别。
5. 块结构化设计（SESE）：使用单入单出（Single Entry Single Exit）的对称网关来构建更健壮的流程。
6. 信号 vs 消息：用“大楼广播喇叭”与“打电话”的生动比喻，秒懂广播语义与定向通信的差异。
7. 实战解析：Week 06 课后练习中关于消息流正确性以及电子土地开发申请协作图（Assessment Manager 枢纽架构）的通俗化剖析。

## 关键术语

- 模型质量 — Process Model Quality：判断流程模型是否可读、合法、符合业务现实、并且能正确运行的一组质量维度。
- 行为正确性 — Behavioural Correctness：模型在执行时是否不会出现死锁、无法完成、错误同步、遗漏路径等行为问题。
- 令牌游戏 — Token Game：把流程执行想象成令牌沿着连线流动，用来检查某条执行路径是否会违反行为正确性。
- 块结构化 — Block-structuredness（SESE）：成对、匹配、边界清楚的网关和子块，英文缩写 SESE（Single Entry Single Exit）。
- 信号 — Signal：BPMN 中的广播事件（Signal）；向所有人公开发出的通知，而不是发给特定接收者的定向通信。
- 消息 — Message：具有明确发送方和接收方的定向通信，与广播性质的 Signal 形成对比。

## Provenance

- **Initial draft**: Claude CLI draft artifact `ep06_script_v1.0.md` (subscription/session token path).
- **Independent review**: Official Gemini CLI TUI review (`ep06_gemini_review_v1.0.md`), completed footer `gemini-3-flash-preview`, verdict `PASS_WITH_FIXES`.
- **Final script/TTS cleanup**: Claude CLI print mode (`--model sonnet`, `--effort high`) applied fixes in `ep06_script_v1.1.md`.
- **Shipped TTS/render**: Doubao/Volcengine seed-tts via doubao-speech wrapper; natural speed, single voice.

## Files

- `episode6_script_v1.1.md` — editorial script.
- `episode6_script.txt` — TTS-clean render script.
- `episode6_review_fix_checklist_v1.1.md` — review/fix checklist.
- `episode6_gemini_review_v1.0.md` — Gemini review artifact.
- `ep06_render_metadata.json` — render metadata.
