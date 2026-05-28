# EP04 Review Fix Checklist V1.1

**Episode:** EP04 — BPMN Sub-processes & Timer Events
**Checklist date:** 2026-05-28T04:02:19Z
**Based on:** `ep04_claude_review_v1.0.md`
**Target deliverables:** `ep04_script_v1.1.md`, `ep04_tts_script_v1.1.txt`, `ep04_show_notes_v1.1.md`, `ep04_coverage_audit_v1.1.md`

---

## Must-Fix Items

- [x] **MF-01** — Update show notes provenance: change "审阅模型: pending" to record Gemini CLI timeout (no findings) and this Claude review/fix run (model: `claude-sonnet-4-6`, date: 2026-05-28). `fixed` in `ep04_show_notes_v1.1.md`

- [x] **MF-02** — TTS script: restore A's question ("晓雨，你觉得流程里的数据有几种？") and A's exploratory answer at the start of the data section before B introduces the four data types. `fixed` in `ep04_tts_script_v1.1.txt`

- [x] **MF-03** — Script and TTS: add brief disambiguation for "虚线" — event sub-process uses a dashed frame border; non-interrupting boundary event uses a dashed event-circle outline. Both uses clarified with short parentheticals. `fixed` in `ep04_script_v1.1.md` and `ep04_tts_script_v1.1.txt`

- [x] **MF-04** — Script and TTS: add brief 课后思考题 reference for W04-D03-S051 quiz near end of sub-process section. Answer not provided (not in extracted text); framed as listener self-check. `fixed` in `ep04_script_v1.1.md` and `ep04_tts_script_v1.1.txt`

- [x] **MF-05** — Provenance reconciliation: `episode_plan.md` still says "reviewer: pending". Resolved by accurate provenance records in `ep04_show_notes_v1.1.md`, `ep04_coverage_audit_v1.1.md`, and appended `production_notes.md`. `episode_plan.md` not edited (source-pack input document). `fixed` via deliverable files

---

## Should-Fix Items

- [x] **SF-01** — Data Collection explanation: add one-sentence example contrast ("比如一份订单是数据对象，二十份是数据集合") in editorial script to better scaffold the concept. `fixed` in `ep04_script_v1.1.md`; TTS carries same improvement.

- [x] **SF-02** — Marker combinations: add note that tasks have a further marker type (compensation/+) not covered in this episode, per W04-D04-S015 "will be covered in another video." `fixed` in `ep04_script_v1.1.md` and `ep04_tts_script_v1.1.txt`

---

## Coverage Audit Items

- [x] **CA-01** — W04-D03-S024 and W04-D03-S025: update status from `needs-source-check` to `deferred-with-reason`. Reason: diagrams are book images (unextractable by PyMuPDF); PDF cannot be rendered in current environment (poppler-utils not installed); surrounding sub-process hierarchy content fully covered by other slides; inventing description of unviewable diagram is not acceptable. `fixed` in `ep04_coverage_audit_v1.1.md`

- [x] **CA-02** — Boundary Timer Event slide gap: update from `needs-source-check` to `deferred-with-reason`. Reason: W04-D05 has only 5 extracted slides; no explicit boundary timer slide exists in extraction; content is `expanded` from standard BPMN 2.0 knowledge + `course_map.md` guidance; expansion is disclosed; PDF cannot be verified without rendering. `fixed` in `ep04_coverage_audit_v1.1.md`

- [x] **CA-03** — Event Sub-process slide gap: confirm `deferred-with-reason` status (was already noted as expanded in v1.0). Reason: same as CA-02. `fixed` in `ep04_coverage_audit_v1.1.md`

- [x] **CA-04** — W04-D03-S051 quiz: update audit status from `compressed` to `scripted` (brief mention added in v1.1). `fixed` in `ep04_coverage_audit_v1.1.md`

---

## Deferred Items (not fixed, with explicit reasons)

- **DEFER-01** — W04-D03-S024/S025 book diagrams: content cannot be added responsibly without viewing the diagrams. If PDF rendering becomes available, verify and optionally add a verbal diagram description. Not a publication blocker for audio.

- **DEFER-02** — Boundary timer and event sub-process explicit slide verification: cannot confirm whether additional slides exist in original PDFs beyond what PyMuPDF extracted, due to rendering environment limitation. The expanded content is accurate per BPMN 2.0 standard and is disclosed.

- **DEFER-03** — Independent cross-provider review: Gemini CLI attempt timed out. No alternative cross-provider review tool available in this environment. This run remains a same-provider self-review. Flag for future production: retry Gemini review with a longer timeout or stable session, or engage a human reviewer for independent check before final release.

---

## Pre-TTS Gate Status

All must-fix items resolved. All should-fix items applied. Deferred items documented with explicit reasons. No publication blockers remain.

**EP04 status after v1.1 fixes: READY FOR TTS RENDER (pending human sign-off on expanded content disclosure)**
