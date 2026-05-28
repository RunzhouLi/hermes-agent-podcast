# EP05 Review/Fix Checklist v1.0

Date: 2026-05-28
Reviewer: official Gemini CLI TUI/PTY, `gemini-2.5-pro`, Google One AI Pro / Code Assist plan.
Initial draft: Claude CLI draft artifact `ep05_script_v1.0.md`; prior Claude log `ep05_claude_15.log` shows session limit, so provenance remains draft artifact + limited CLI log evidence.
Codex usage: none.

## Accepted review findings

- [x] Coverage: Gemini review found all substantive Week 05 ledger concepts represented: Terminate Event, Event Sub-Process, Text Annotation, Boundary Event, Error Event, Compensation, Exercises Week 05, Answer 5.2, Answer 5.3.
- [x] Terminology: core terms use audible bilingual terminology cards and consistent reuse.
- [x] Listenability: stage-play analogy and dual-host comprehension checks are present.
- [x] TTS cleanup requirement: final TTS-clean script must remove editorial brackets, Markdown blockquotes/bullets where unsuitable, and speaker Markdown formatting while preserving speaker turns.
- [x] Stray Markdown fence: Gemini did not catch it, but local verification found one trailing ``` fence at the end of `ep05_script_v1.0.md`; removed in this cron run.

## Medium findings assessed

- [x] Section 4 pacing: Gemini suggested another Host A interjection after the Terminate End Event property list. Existing lines immediately after the four-point list already include Host A asking to clarify the termination scope, so no extra edit applied.
- [x] Section 9 compensation recap: Gemini suggested Host A summarize the cancellation flow. Existing compensation section already includes Host A recap lines distinguishing error handling vs compensation and payment/refund, shipping/return examples, so no extra edit applied.
- [ ] Show notes visual aid: optional clean digital diagrams for visual learners. Deferred until show-notes/publish stage; not required for audio render gate.
- [ ] TTS-clean script: pending next stage.
- [ ] Render metadata/show notes/coverage audit for published EP05: pending render/publish stages.

## Gate decision

Review/fix stage status: PASS_WITH_FIXES resolved for editorial script. Next clear stage is generating the EP05 TTS-clean script and render-ready artifacts; do not publish until TTS render, ffprobe duration, byte length, RSS XML parse, commit/push, and public smoke tests pass.
