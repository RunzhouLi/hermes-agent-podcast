# 第 05 集：BPMN 高级事件与补偿（Advanced Events & Compensation）

版本：V1.0  
来源：Week 05 — BPMN Advanced Events & Compensation  
时长：00:47:24  
音频：doubao+gemini-fallback — Mixed resumable render: Volcengine/Doubao seed-tts cached segments where available; Gemini 2.5 Flash preview TTS fallback via doubao_tts_with_gemini_fallback.py after Doubao text_words_lifetime quota exhaustion；自然语速，无 0.9x 后处理  
Codex usage: none.

## 本集简介

这一集继续 BPMN 建模课，但重点从“正常主流程”转到“流程演到一半出意外怎么办”。我们用电商订单和舞台剧两个稳定类比，讲清 BPMN 高级事件如何表达中止、异常、边界反应、错误抛接和补偿善后。

## 你会学到

1. 终止结束事件 Terminate End Event：为什么普通结束事件有时不够，以及“全停”的范围到底是哪一层。
2. 事件子流程 Event Sub-Process：流程运行时，如何插入随事件触发的处理。
3. 文本注释 Text Annotation：如何给模型加说明，但不改变执行语义。
4. 边界事件 Boundary Event：活动正在执行时，如何表达超时、取消、错误等边界反应。
5. 错误事件 Error Event：什么是抛出错误、捕获错误，以及为什么它不是普通分支判断。
6. 补偿 Compensation：已经完成的工作需要撤销或善后时，如何建模。
7. Week 05 练习与 selected answers 5.2 / 5.3 的建模检查点。

## 关键术语

- 终止结束事件 — Terminate End Event：一个带实心黑圆点的结束事件；用于清除当前流程范围内的令牌。
- 事件子流程 — Event Sub-Process：父流程运行期间由事件触发的子流程，可中断或非中断。
- 文本注释 — Text Annotation：模型中的解释性文字，不参与流程执行。
- 边界事件 — Boundary Event：附着在活动或子流程边界上的事件，用来表达活动执行期间发生的反应。
- 错误事件 — Error Event：表达异常失败条件的 BPMN 事件，通常涉及抛出与捕获。
- 补偿 — Compensation：对已经完成的工作进行撤销、退款、退货或其他善后处理。

## Provenance

- Initial draft: Claude CLI draft artifact `ep05_script_v1.0.md`; prior Claude log indicated subscription/session limit but complete draft artifact exists.
- Independent review: official Gemini CLI TUI/PTY `gemini-2.5-pro`, verdict `PASS_WITH_FIXES`; no high-priority factual/coverage blockers.
- Final script/TTS cleanup: Hermes cron deterministic cleanup and checklist resolution; Codex usage none.
- Shipped TTS/render: doubao+gemini-fallback — Mixed resumable render: Volcengine/Doubao seed-tts cached segments where available; Gemini 2.5 Flash preview TTS fallback via doubao_tts_with_gemini_fallback.py after Doubao text_words_lifetime quota exhaustion; natural speed, no 0.9x slowdown.

## Files

- `episode5_script_v1.0.md` — editorial script.
- `episode5_script.txt` — TTS-clean render script.
- `episode5_coverage_audit_v1.0.md` — source coverage audit.
- `episode5_review_fix_checklist_v1.0.md` — review/fix checklist.
- `episode5_gemini_review_v1.0.md` — Gemini review artifact.
- `ep05_render_metadata.json` — render metadata.
