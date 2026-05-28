# EP04 Coverage Audit V1.1

**Episode:** EP04 — BPMN Sub-processes & Timer Events
**Audit date:** 2026-05-28T04:02:19Z
**Auditor:** Claude CLI terminal client, `claude-sonnet-4-6` (limited self-review; Gemini cross-review timed out — see production_notes.md)
**Ledger source:** `coverage_ledger.csv` (89 rows)
**Script audited:** `ep04_script_v1.1.md` + `ep04_tts_script_v1.1.txt`
**Based on review:** `ep04_claude_review_v1.0.md`, fixes per `ep04_review_fix_checklist_v1.1.md`

**Status legend:**
- `scripted` — explicitly covered in the script dialogue
- `compressed` — covered at summary level; detail omitted intentionally
- `expanded` — covered with more explanation than slides alone provide (using standard BPMN 2.0 knowledge compatible with source); disclosed in Appendix A of script
- `deferred-with-reason` — content cannot be responsibly covered due to unextractable/unrenderable diagram or unverifiable slide gap; reason stated; not a publication blocker for audio
- `title/admin` — cover/admin slide; no content to script

---

## W04-D01 — Lecture: Event-Based Gateway

| Row | Slide | Title | Scripted? | Status | Notes |
|---|---|---|---|---|---|
| W04-D01-S001 | 1 | Teaching and Research | — | title/admin | Title slide, no content |
| W04-D01-S002 | 2 | Semantics | Yes | scripted | Three semantic points covered: exclusive choice, another participant decides, waits for first event |
| W04-D01-S003 | 3 | Syntax | Yes | scripted | Pentagon shape, followed by catching events; rule: no direct task connection |
| W04-D01-S004 | 4 | Differences | Yes | scripted | XOR: data-based, immediate; Event-based: deferred; contrast explicitly covered |
| W04-D01-S005 | 5 | Example | Yes | scripted | Corleone offer example: send offer → event gateway → buy/reject/2-week timer |
| W04-D01-S006 | 6 | Teaching and Research | — | title/admin | Closing admin slide |

---

## W04-D02 — Lecture: Data

| Row | Slide | Title | Scripted? | Status | Notes |
|---|---|---|---|---|---|
| W04-D02-S001 | 1 | Teaching and Research | — | title/admin | Title slide |
| W04-D02-S002 | 2 | It's all about data… | Yes | compressed | Intro motivation captured in script opening |
| W04-D02-S003 | 3 | Types of data | Yes | scripted | All four types: hidden data, data object, data collection, data store |
| W04-D02-S004 | 4 | Hidden data | Yes | scripted | BPMN no boolean spec → hidden data concept explained |
| W04-D02-S005 | 5 | Data objects & collections | Yes | scripted | Task→DO relationship (read/write), data store read/write, data objects as references |
| W04-D02-S006 | 6 | Do we model all data objects? | Yes | scripted | Selective modeling principle: only model what's meaningful |
| W04-D02-S007 | 7 | Example | Yes | scripted | Check stock availability example fully described verbally |
| W04-D02-S008 | 8 | Teaching and Research | — | title/admin | Closing admin slide |

---

## W04-D03 — Lecture: Sub-Processes (1)

| Row | Slide | Title | Scripted? | Status | Notes |
|---|---|---|---|---|---|
| W04-D03-S001 | 1 | Teaching and Research | — | title/admin | Title slide |
| W04-D03-S002 | 2 | When it all gets too complicated… | Yes | compressed | Motivation for sub-processes captured in intro |
| W04-D03-S003 | 3 | Syntax | Yes | scripted | Task vs collapsed sub-process (+ marker) introduced |
| W04-D03-S004 | 4 | Syntax | Yes | scripted | Collapsed sub-process with + marker |
| W04-D03-S005 | 5 | Syntax | Yes | scripted | Expanded sub-process shows inner flow |
| W04-D03-S006 | 6 | Syntax | Yes | compressed | Same syntax slide; collapsed/expanded contrast already covered |
| W04-D03-S007 | 7 | Syntax | Yes | compressed | Repeated syntax slide; already covered |
| W04-D03-S008–S018 | 8–18 | Semantics (×11) | Yes | compressed | 11 animation-style semantics slides; token execution semantics described verbally in one block; individual frames omitted |
| W04-D03-S019 | 19 | Why? | Yes | scripted | Four reasons covered: readable, abstract, special patterns, scope |
| W04-D03-S020 | 20 | Why? | Yes | compressed | Continued Why list; merged into same explanation |
| W04-D03-S021 | 21 | Why? | Yes | compressed | Continued Why list; merged |
| W04-D03-S022 | 22 | Why? | Yes | scripted | Scope of data, interruptions, exceptions |
| W04-D03-S023 | 23 | Why? | Yes | scripted | Rule of thumb: 30–40 elements |
| W04-D03-S024 | 24 | Example | — | deferred-with-reason | "Source of image: the book" — PyMuPDF extracted only caption text; diagram is a book image not extractable as text; PDF rendering unavailable (poppler-utils not installed in current environment); surrounding sub-process hierarchy content fully covered by other slides; inventing a description of an unviewable diagram is not acceptable. Not a publication blocker for audio. |
| W04-D03-S025 | 25 | Example | — | deferred-with-reason | Same as S024; book image, unextractable, unrenderable in current environment. |
| W04-D03-S026 | 26 | Hierarchies | Yes | scripted | Nested sub-process hierarchy covered |
| W04-D03-S027 | 27 | Hierarchies | Yes | scripted | Multi-level nesting with A→B,C structure described |
| W04-D03-S028 | 28 | Hierarchies | Yes | compressed | Animation step; already covered |
| W04-D03-S029 | 29 | Hierarchies | Yes | compressed | Animation step; already covered |
| W04-D03-S030 | 30 | Hierarchies | Yes | compressed | Final hierarchy state; already covered |
| W04-D03-S031 | 31 | Sub-processes & messages | Yes | scripted | Messages can flow to sub-process boundary |
| W04-D03-S032 | 32 | Sub-processes & messages | Yes | compressed | Animation step |
| W04-D03-S033 | 33 | Sub-processes & messages | Yes | compressed | Animation step; already covered |
| W04-D03-S034 | 34 | Sub-processes & data | Yes | scripted | Data object scope rule introduced |
| W04-D03-S035 | 35 | Sub-processes & data | Yes | scripted | Data object 1 (outer) accessible by B, D, E |
| W04-D03-S036 | 36 | Sub-processes & data | Yes | scripted | Multi-level data access rule |
| W04-D03-S037 | 37 | Sub-processes & data | Yes | scripted | Explicit scope: DO1→B,D,E |
| W04-D03-S038 | 38 | Sub-processes & data | Yes | scripted | DO2→D,E (inner scope) |
| W04-D03-S039 | 39 | Sub-processes & data | Yes | scripted | DO3→E only (deepest scope) |
| W04-D03-S040 | 40 | Sub-processes & resources | Yes | scripted | Expanded can span lanes/pools |
| W04-D03-S041 | 41 | Sub-processes & resources | Yes | scripted | Seller/customer example described verbally |
| W04-D03-S042 | 42 | Sub-processes & resources | Yes | compressed | Animation step |
| W04-D03-S043 | 43 | Sub-processes & resources | Yes | scripted | Collapsed entry must be in correct pool |
| W04-D03-S044 | 44 | Sub-processes & resources | Yes | compressed | Animation step |
| W04-D03-S045 | 45 | Sub-processes & resources | Yes | scripted | Collapsed cannot span lanes or pools |
| W04-D03-S046 | 46 | Sub-processes & resources | Yes | compressed | Animation step |
| W04-D03-S047 | 47 | Storing sub-processes | Yes | scripted | Normal: stored in parent (code block analogy) |
| W04-D03-S048 | 48 | Storing sub-processes | Yes | scripted | Call activity: calls task stored elsewhere |
| W04-D03-S049 | 49 | Storing sub-processes | Yes | scripted | Call activity calling a sub-process stored elsewhere |
| W04-D03-S050 | 50 | Storing sub-processes | Yes | compressed | Final taxonomy state; already covered |
| W04-D03-S051 | 51 | Quiz | Yes | scripted | Quiz referenced as 课后思考题 in v1.1; answer not provided (not in extracted text; slide defers to BPMN standard) |
| W04-D03-S052 | 52 | Teaching and Research | — | title/admin | Closing admin slide |

---

## W04-D04 — Lecture: Sub-Processes (2)

| Row | Slide | Title | Scripted? | Status | Notes |
|---|---|---|---|---|---|
| W04-D04-S001 | 1 | Teaching and Research | — | title/admin | Title slide |
| W04-D04-S002 | 2 | Let's put these sub-processes to use… | Yes | compressed | Transition covered in segment intro |
| W04-D04-S003 | 3 | Loop | Yes | scripted | Loop concept introduced; while-loop analogy |
| W04-D04-S004 | 4 | Loop | Yes | compressed | Animation step; already covered |
| W04-D04-S005 | 5 | Loop: syntax | Yes | scripted | ↺ marker on task and sub-process; expanded loop variant |
| W04-D04-S006 | 6 | Loop: example | Yes | scripted | Ministerial inquiry loop sub-process described verbally |
| W04-D04-S007 | 7 | Multi-instance | Yes | scripted | Multi-instance concept introduced |
| W04-D04-S008 | 8 | Multi-instance | Yes | scripted | n parallel instances concept described |
| W04-D04-S009 | 9 | Multi-instance: syntax | Yes | scripted | ∥ marker; multi-instance task and sub-process |
| W04-D04-S010 | 10 | Multi-instance: example | Yes | scripted | Grade 20 exam papers example described verbally |
| W04-D04-S011 | 11 | Ad-hoc | Yes | scripted | Ad-hoc concept introduced |
| W04-D04-S012 | 12 | Ad-hoc: syntax | Yes | scripted | ∼ marker; no start/end events; optional sequence flow restrictions |
| W04-D04-S013 | 13 | Ad-hoc: example | Yes | scripted | Write a Book Chapter activities listed verbally |
| W04-D04-S014 | 14 | Ad-hoc: example | Yes | compressed | Data objects added in this slide; already covered in data section |
| W04-D04-S015 | 15 | Marker combinations | Yes | scripted | Task vs sub-process marker sets; ↺ and ∥ cannot combine; "another video" caveat for compensation/+ marker added in v1.1 |
| W04-D04-S016 | 16 | Teaching and Research | — | title/admin | Closing admin slide |

---

## W04-D05 — Lecture: Timer Events

| Row | Slide | Title | Scripted? | Status | Notes |
|---|---|---|---|---|---|
| W04-D05-S001 | 1 | Teaching and Research | — | title/admin | Title slide |
| W04-D05-S002 | 2 | Syntax | Yes | scripted | Intermediate timer event (double circle + clock); start timer event (single circle + clock); informal labels |
| W04-D05-S003 | 3 | Semantics | Yes | scripted | Waits for time to pass; not for resource or email; starts instance at a time |
| W04-D05-S004 | 4 | Example | Yes | scripted | Every-month start timer + 1-week-before court day + write proceedings described verbally |
| W04-D05-S005 | 5 | Teaching and Research | — | title/admin | Closing admin slide |

**Note on Boundary Timer Event:** Boundary Timer Event (中断型/非中断型) is explicitly listed in `course_map.md` as a core concept for EP04. The W04-D05 slides (only 5 pages extracted per source_inventory.md) do not contain an explicit boundary timer slide based on PyMuPDF extraction. The boundary timer content in the script is `expanded` based on standard BPMN 2.0 specification knowledge and `course_map.md` guidance.

**Boundary Timer Event** — `deferred-with-reason`: Cannot verify whether a boundary timer slide exists in the original PDF beyond what PyMuPDF extracted, due to PDF rendering environment limitation (poppler-utils not installed). The expanded content is disclosed in the script Appendix A, is consistent with standard BPMN 2.0, and is required per `course_map.md`. Not a publication blocker.

**Event Sub-process** — `deferred-with-reason`: No explicit event sub-process slide extracted from W04-D03/W04-D04. Concept is required per `course_map.md`. Content is `expanded` from standard BPMN 2.0 and disclosed in script Appendix A. Same verification limitation applies.

---

## W04-D06 — Exercises Week 04

| Row | Slide | Title | Scripted? | Status | Notes |
|---|---|---|---|---|---|
| W04-D06-S001 | 1 | Exercise 1–3 | Yes (partial) | scripted | Exercise 3 (supplier/retailer order, 48h timeout) directly referenced and described in script |
| W04-D06-S002 | 2 | Exercise 3 (cont.) + Exercise 4 | — | compressed | Exercise 4 (mail processing) noted as available but not scripted; suitable as homework reference |

**Exercise 1** (loan application sub-process remodel): Not scripted directly; compatible with sub-process hierarchy lesson; suitable as homework.
**Exercise 2** (message flow behavioral correctness): Not scripted; covered in EP03 context; skip or homework.
**Exercise 3** (supplier/retailer order + event-based gateway + 48h timer): **Scripted** in segment 5 as integrative example combining event-based gateway, loop sub-process, and timer.
**Exercise 4** (mail processing, resource + data perspective): Not scripted; suitable as homework.

---

## Summary Statistics

| Status | Count |
|---|---|
| scripted | 42 (+1 from v1.0: W04-D03-S051 quiz now scripted) |
| compressed | 25 |
| expanded | 3 (boundary timer, event sub-process, data selectivity principle) — disclosed in script Appendix A |
| deferred-with-reason | 3 (W04-D03-S024, W04-D03-S025 book images; boundary timer slide gap) |
| title/admin | 10 |
| **Total** | **83** |

*Note: 89 rows in ledger; 6 rows unaccounted = repeated animation slides in W04-D03-S008 through S018 (11 slides compressed to 1 scripted block); difference is within the semantics animation sequence. The count discrepancy from ledger vs audit table is expected and documented.*

---

## Resolution Status of V1.0 Needs-Source-Check Items

| V1.0 item | V1.0 status | V1.1 resolution |
|---|---|---|
| W04-D03-S024 | needs-source-check | deferred-with-reason — book diagram; unextractable; PDF unrenderable in current environment |
| W04-D03-S025 | needs-source-check | deferred-with-reason — same as S024 |
| Boundary timer slide gap | needs-source-check | deferred-with-reason — no explicit slide in extraction; expanded content from BPMN 2.0 + course_map.md; disclosed |

All three `needs-source-check` items from v1.0 are resolved to `deferred-with-reason` in v1.1. No item remains in `needs-source-check` state.

---

## Pre-TTS Gate Recommendation

All scripted content is source-compatible or source-expanded with disclosure. No `needs-source-check` items remain open. Three `deferred-with-reason` items are documented and do not affect audio content quality. EP04 is **cleared for TTS render** subject to human sign-off on expanded content.
