# EP04 Claude Limited Review V1.0

**Episode:** EP04 — BPMN Sub-processes & Timer Events
**Review date:** 2026-05-28T04:02:19Z
**Reviewer:** Claude CLI (Claude Code), model `claude-sonnet-4-6`, same provider as initial draft
**Independent cross-provider review status:** INCOMPLETE — Gemini CLI `gemini-3.1-pro-preview` attempt started 2026-05-28T03:25:31Z; timed out after 25 minutes (GEMINI_EXIT:124) during TUI initialization/authentication spin; no final structured findings produced. This review is therefore a same-provider self-review, not an independent cross-provider review. See `production_notes.md` for full Gemini attempt log record.
**Files reviewed:** `ep04_script_v1.0.md`, `ep04_tts_script_v1.0.txt`, `ep04_show_notes.md`, `ep04_coverage_audit_v1.0.md`, `coverage_ledger.csv`, `extracted.md`, `course_map.md`, `episode_plan.md`

---

## 1. PASS/FAIL Summary

**Overall verdict: CONDITIONAL PASS — proceed to v1.1 with minor fixes**

No publication blockers found. The script is structurally sound, Chinese-first throughout, uses consistent analogies, covers all extractable source content, and correctly applies the audible terminology protocol for all core terms. Five minor issues require fixing before TTS render; three items are deferred with explicit reasons.

| Category | Finding |
|---|---|
| Structure & flow | PASS — dual-host format correct; micro-recap present; EP03 bridge natural |
| Chinese-first protocol | PASS — all terms introduced 中文 → English → explanation |
| Audible terminology protocol | PASS with note — all 19 terms in scope introduced correctly; see §5 for detail |
| Source coverage | PASS — all extractable slides covered; unextractable slides deferred with reason |
| Analogy consistency | PASS — 客服工单系统 analogy maintained throughout |
| TTS-clean/editorial separation | PASS — separate files; TTS file free of markdown tables and source footnotes |
| Provenance metadata | FAIL (minor, must-fix) — reviewer field still "pending" in show notes and episode plan |
| Visual-only references in TTS | PASS — icon descriptions are pedagogically necessary, not extraneous visual references |
| No invented source content | PASS — expanded content (boundary timer, event sub-process) disclosed in appendix; compatible with standard BPMN 2.0 |

---

## 2. Must-Fix Issues Before TTS

### MF-01: Provenance metadata incomplete in show notes
**File:** `ep04_show_notes.md`
**Issue:** "审阅模型: pending" — must be updated to reflect this review/fix run.
**Fix:** Update show notes to record this Claude review/fix run.

### MF-02: TTS script drops A/B exchange at data-section opening
**File:** `ep04_tts_script_v1.0.txt`, line 69
**Issue:** The editorial script has B ask "晓雨，你觉得流程里的数据有几种？" and A give an exploratory answer before B introduces the four data types. The TTS script skips this exchange entirely and has B jump straight to the four-type classification. This removes a natural learner-proxy moment that helps the listener prime their mental model before the answer arrives.
**Fix:** Restore the A-question and A-answer exchange in TTS v1.1.

### MF-03: Dashed-line terminology collision not resolved
**File:** `ep04_script_v1.0.md`, §第三段 and §第五段
**Issue:** Two BPMN constructs both described using "虚线" (dashed/dotted line):
- Event sub-process: "用虚线边框画" — refers to the entire frame of the sub-process having a dashed border
- Non-interrupting boundary timer event: "边界事件圆圈是虚线边框" — refers to the boundary event circle having a dashed outline

These are visually different objects (large frame vs small circle) and the description objects differ ("边框" vs "圆圈"), so a careful listener can distinguish them. However, a first-time listener could conflate them. A brief parenthetical clarification at each point eliminates this risk.
**Fix:** Add "（这里的虚线是指子流程外框，不是事件圆的样式）" to event sub-process description; add "（这里的虚线是指这个小圆圈本身的线型，不是子流程边框）" to non-interrupting boundary description. Or a single clarifying aside when first used.

### MF-04: W04-D03-S051 quiz not mentioned in script
**File:** `ep04_script_v1.0.md`, `ep04_tts_script_v1.0.txt`
**Issue:** The quiz on slide W04-D03-S051 ("How many BPMN elements do you need at least to express: First A is executed, after which B and C are executed in parallel. Finally, D is executed?") is listed as `compressed` in coverage audit but is not referenced in the script at all. The coverage audit note says "mentioned in script context (Exercise discussion)" but reading the script, it is not actually mentioned. The quiz is a good self-check opportunity.
**Fix:** Add a brief "课后思考题" reference near the end of the sub-process section. Do not provide the answer (the answer is not in the extracted text; slide says "refer to BPMN standard on sub-processes").

### MF-05: Episode plan provenance still says "reviewer: pending"
**File:** `episode_plan.md`
**Issue:** The production provenance ledger in `episode_plan.md` still has "Reviewer model: pending". This file is a planning document, not a deliverable, but it creates a discrepancy. However, since `episode_plan.md` is a source-pack input document and modifying it is lower priority than the deliverables, this is tracked as must-fix in the checklist but resolved via the review/notes files rather than editing episode_plan.md.
**Disposition:** Resolved by accurate provenance in `ep04_show_notes_v1.1.md`, `ep04_coverage_audit_v1.1.md`, and `production_notes.md` append.

---

## 3. Should-Fix Improvements

### SF-01: Data-type explanation could clarify "data collection" more concretely
**File:** `ep04_script_v1.0.md`, §第二段
**Issue:** The explanation of Data Collection is brief: "本质上是一组相同类型的数据对象。图标上加一个小竖三线。比如'一批订单'。" This is technically correct but the listener gets less scaffolding than for the other three data types. Adding a one-sentence contrast ("比如一份订单是数据对象，二十份订单就是数据集合") would help.
**Priority:** Low — current text is accurate; improvement is optional.

### SF-02: Call Activity "another video" caveat from W04-D04-S015 not mentioned
**File:** `ep04_script_v1.0.md`, §第四段
**Issue:** Slide W04-D04-S015 notes that the "+" (compensation/other task marker type) "will be covered in another video." The script correctly says tasks can use ↺ and ∥ markers but does not mention that there's a further task marker type not covered in this episode. Adding a brief note like "任务还有一种 + 型标记，本集不涉及，后续集会讲到" would set accurate expectations.
**Priority:** Low.

### SF-03: Micro-recap could explicitly bridge back to sub-process data scope
**File:** `ep04_script_v1.0.md`, 中段微总结
**Issue:** The micro-recap ends with A asking "这两条线索——'等外部事件'和'信息的流动'——在子流程里会怎么体现？" which is a good bridge. B's response is also good. No change required; this is a confirmation that the existing text is correct.
**Disposition:** No change needed.

---

## 4. Coverage Ledger Audit

**Ledger rows:** 89 total
**Status distribution in v1.0 audit:**
- scripted: 41
- compressed: 25
- expanded: 3
- needs-source-check: 3
- title/admin: 10
- (7 animation duplicate rows in semantics sequence absorbed into 1 block)

**Items requiring resolution:**

### W04-D03-S024 and W04-D03-S025 — "Source of image: the book"
**Finding:** These two slides contain diagrams sourced from the Dumas et al. BPM textbook. PyMuPDF extracted only the caption "Source of image: the book" — no diagram content. The surrounding slides (S026 onward) cover sub-process hierarchies with full text. The PDF cannot be rendered in this environment (pdftoppm/poppler-utils not installed).
**Disposition:** `deferred-with-reason` — diagram content cannot be extracted or rendered; surrounding sub-process hierarchy content is comprehensively covered by other slides; inventing a description of an unviewable diagram would be irresponsible. If rendered at a later stage, verify whether the diagrams show a different example worth adding; if so, a minor addition can be made before TTS.

### Boundary Timer Event slide gap
**Finding:** W04-D05 contains only 5 slides (confirmed by source_inventory.md: "5 pages/slides"). The extracted slides cover: title, syntax (start + intermediate timer), semantics, timer example, closing title. No explicit boundary timer event slide exists in W04-D05 extraction. The boundary timer content in the script is `expanded` — drawn from `course_map.md` explicit listing and standard BPMN 2.0 specification knowledge.
**Disposition:** `deferred-with-reason` — boundary timer is explicitly required by `course_map.md`; standard BPMN 2.0 coverage is authoritative and source-compatible; expanded content is clearly disclosed in script Appendix A. If the original W04-D05 PDF contains a sixth slide not captured by PyMuPDF (possible with image-based slides), the expanded content should be checked against it. Cannot verify without PDF rendering.

### Event Sub-process slide gap
**Finding:** No explicit event sub-process slide was extracted from W04-D03 or W04-D04. The concept is listed in `course_map.md` and `episode_plan.md` as required. Script content is `expanded` from standard BPMN 2.0 knowledge.
**Disposition:** `deferred-with-reason` — same rationale as boundary timer. Content is source-compatible and disclosure is present.

---

## 5. Terminology Audit

All 19 terms from the episode_plan.md key terms list and course_map.md are introduced using the required audible protocol (中文术语 → English term → abbreviation if any → 白话解释 → example sentence pattern).

| Term | In editorial script | In TTS script | Protocol followed |
|---|---|---|---|
| 事件网关 — Event-Based Gateway | §第一段 | line 41 | PASS |
| 隐藏数据 — Hidden Data | §第二段 | line 71 | PASS |
| 数据对象 — Data Object (DO) | §第二段 | line 77 | PASS |
| 数据集合 — Data Collection | §第二段 | line 87 | PASS |
| 数据存储 — Data Store (DS) | §第二段 | line 89 | PASS |
| 数据关联 — Data Association | §第二段 | line 81 | PASS |
| 顺序流 — Sequence Flow | §第二段 | line 81 | PASS |
| 折叠子流程 — Collapsed Sub-process | §第三段 | line 115 | PASS |
| 展开子流程 — Expanded Sub-process | §第三段 | line 119 | PASS |
| 调用活动 — Call Activity (CA) | §第三段 | line 147 | PASS |
| 事件子流程 — Event Sub-process | §第三段 | line 151 | PASS |
| 循环子流程 — Loop Sub-process | §第四段 | line 155 | PASS |
| 多实例子流程 — Multi-instance Sub-process | §第四段 | line 159 | PASS |
| 临时子流程 — Ad-hoc Sub-process | §第四段 | line 163 | PASS |
| 定时开始事件 — Timer Start Event | §第五段 | line 173 | PASS |
| 中间定时事件 — Intermediate Timer Catch Event | §第五段 | line 177 | PASS |
| 边界定时事件 — Boundary Timer Event | §第五段 | line 185 | PASS |
| 中断型 — Interrupting | §第五段 | line 193 | PASS |
| 非中断型 — Non-interrupting | §第五段 | line 195 | PASS |

**Note on TTS abbreviation omission:** In the TTS script, some abbreviations (DO, DS, CA) present in the editorial terminology table are not always repeated inline in the TTS dialogue. This is intentional: the TTS script introduces terms with full Chinese + English names; abbreviations are in the editorial glossary table which is not rendered in TTS. No fix needed.

---

## 6. Provenance / Metadata Audit

| Field | V1.0 state | Required state for v1.1 |
|---|---|---|
| Script draft model | `claude-sonnet-4-6`, date 2026-05-28 | Correct — retain |
| Gemini review | "审阅模型: pending" in show notes | Must update: Gemini attempt timed out; no findings |
| This review/fix model | Not recorded in show notes | Must add: Claude CLI `claude-sonnet-4-6`, date 2026-05-28 |
| TTS model | "pending" | Correct — TTS not yet rendered; retain pending |
| Codex usage | None | Confirmed none |
| Source extraction | PyMuPDF, Hermes cron job | Correct — retain |

---

## 7. Concrete Fix Checklist (input for ep04_review_fix_checklist_v1.1.md)

1. `[MF-01]` Update show notes provenance (reviewer field)
2. `[MF-02]` Restore A's data-section opening exchange in TTS v1.1
3. `[MF-03]` Add dashed-line clarification for event sub-process vs non-interrupting boundary event
4. `[MF-04]` Add brief quiz/思考题 mention near end of sub-process section
5. `[MF-05]` Provenance resolved via deliverable files (no edit to episode_plan.md required)
6. `[SF-01]` (Optional) Add one-sentence contrast for Data Collection
7. `[SF-02]` (Optional) Add "covered in another video" caveat for task compensation marker
8. Coverage audit: update W04-D03-S024/S025 and boundary timer gap from `needs-source-check` to `deferred-with-reason`
