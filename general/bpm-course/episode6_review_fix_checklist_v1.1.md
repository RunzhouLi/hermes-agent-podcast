# EP06 Review/Fix Checklist v1.1

## Provenance
- Source review: `ep06_gemini_review_v1.0.md` (Gemini CLI TUI, completed footer `gemini-3-flash-preview`).
- Final editor: Claude CLI print mode, `--model sonnet`, `--effort high`.
- Input script: `ep06_script_v1.0.md`.
- Output script: `ep06_script_v1.1.md`.
- Codex usage: none.

---

## Critical Fixes (Gemini-designated "before TTS-clean")

### CF-01 — Terminology protocol: 结构正确性 (Structural Correctness)
**Gemini finding:** Missing concrete example at first introduction.
**Status:** `fixed`
**Location in v1.1:** Part 1 — 模型质量的五个维度, 结构正确性 paragraph.
**Change applied:** Added plain explanation ("模型的各个部分是不是都连在一起的") and a concrete spoken example: a task with no incoming or outgoing sequence flow is an isolated island — structurally broken. Replaces the previous text that only listed checks without an illustrative instance.

---

### CF-02 — Terminology protocol: 语法正确性 (Syntactical Correctness)
**Gemini finding:** Missing concrete example at first introduction.
**Status:** `fixed`
**Location in v1.1:** Part 1 — 模型质量的五个维度, 语法正确性 paragraph.
**Change applied:** Added plain explanation ("每一种 BPMN 元素，都有它被允许连接的规则") and a concrete spoken example: a sequence flow pointing into a start event is a syntax error, because start events cannot be triggered mid-flow. Previously only the general rule was stated.

---

### CF-03 — Terminology protocol: 行为正确性 (Behavioural Correctness)
**Gemini finding:** Strengthen with token-game notation/meaning and a concrete example at first introduction.
**Status:** `fixed`
**Location in v1.1:** Part 1 — 模型质量的五个维度, 行为正确性 paragraph.
**Change applied:** Added: (a) named the token game as the checking tool at the point of first introduction; (b) described the token-game method in one sentence; (c) added a concrete example of a parallel-split / XOR-join mismatch producing a stranded token, making the behavioural error tangible before the full Token Game section in Part 2.

---

### CF-04 — Terminology protocol: 块结构化 (Block-structuredness) — SESE
**Gemini finding:** Add SESE / Single Entry Single Exit notation and example.
**Status:** `fixed`
**Location in v1.1:** Part 3 — 池内检查 → 块结构化 opening paragraph.
**Change applied:** Added "英文叫 Single Entry Single Exit，缩写 SESE" at first introduction of 块. Added a plain explanation using a single-door-room analogy. Added a sentence making explicit that SESE enables independent verification and compositional combination. "SESE" is also used in the micro-recap and in the closing summary.

---

### CF-05 — Terminology protocol: 信号 (Signal) — plain explanation and broadcast analogy
**Gemini finding:** Add plain explanation and a clear broadcast/public-address-system example.
**Status:** `fixed`
**Location in v1.1:** Part 6 — 信号事件：广播式通信, Signal introduction paragraph and Signal vs Message contrast paragraph.
**Change applied:** Added a plain explanation sentence at the very first introduction ("信号不针对特定接收者——它是一种向所有人公开发出的通知"). Replaced the sole UDP analogy with a primary public-address-system (大楼广播喇叭) vs phone-call (打电话) analogy. Retained a secondary mention of UDP as a technical parallel for listeners who know networking, framed explicitly as secondary ("如果你熟悉网络协议…"). The PA-system analogy is re-used briefly in the PO example walkthrough for coherence.

---

### CF-06 — NSC-02: Intra-pool anti-pattern visual grounding (XOR / AND-join deadlock)
**Gemini finding:** Add an audible spoken description of the XOR/non-concurrent branch feeding a parallel AND-join anti-pattern; clarify the deadlock / lack-of-synchronization distinction.
**Status:** `fixed`
**Location in v1.1:** Part 3 — 池内反模式, Anti-pattern 1 paragraph and the new deadlock/lack-of-sync clarification paragraph.
**Change applied:**
- Replaced the previous generic "if there's only one token but a parallel join is waiting" description with a concrete spoken-diagram description: XOR split produces one token on one branch; that branch leads to a parallel AND-join; AND-join waits for tokens from all branches; the other branch was never taken; its token never exists; AND-join waits forever → deadlock.
- Added a new B paragraph explicitly distinguishing: **死锁** = process stuck forever, token held at a join that will never be satisfied; **缺少同步** = parallel paths not properly waited upon, allowing flow to proceed before all concurrent activities complete. Both labelled as behaviour errors with the contrast "卡住了" vs "漏掉了等待".

---

### CF-07 — NSC-05: Exercise 2 specific deadlock answer
**Gemini finding:** Script explains analysis method but does not name the specific violation. Add: the violation is a deadlock/message-flow mismatch where Pool A and Pool B can end up waiting on each other.
**Status:** `fixed`
**Location in v1.1:** Part 7 — 练习 2：消息流正确性, B's closing response.
**Change applied:** The generic closing "这道题的核心考查点就是这个分析方法" is replaced with a named specific answer: Pool A is waiting for a message from Pool B; Pool B is simultaneously waiting for a message from Pool A; neither acts first; the process deadlocks permanently. The term "消息流互锁死锁" (message-flow mutual deadlock) is used and the pattern is labelled as a behavioural-correctness violation.

---

## Recommended Fixes / Improvements (Gemini-designated non-critical)

### RF-01 — Micro-recap after block-structuredness, before single-token reasoning
**Gemini finding:** Part 3 is dense; add a short micro-recap between the two sub-sections.
**Status:** `fixed`
**Location in v1.1:** Part 3 — between the end of 块结构化 and the start of 单令牌推理.
**Change applied:** Added a two-exchange A/B micro-recap. A summarises: blocks are SESE structures, matching gateway pairs, sub-blocks first, composition second, type-match is the critical constraint. B confirms and transitions to the next section. This gives listeners a pause and synthesis point before the single-token section opens.

---

### RF-02 — Signal/Message analogy: public-address-system vs phone-call
**Gemini finding:** Replace or supplement UDP/TCP analogy with a more accessible PA-system vs phone-call analogy.
**Status:** `fixed` (combined with CF-05 above)
**Location in v1.1:** Part 6 — Signal vs Message contrast paragraph; also closing summary.
**Change applied:** See CF-05. The PA-system / phone-call analogy is the primary framing. UDP/TCP remains as an optional technical note. The closing summary uses "就像打电话和大楼广播喇叭的区别" to reinforce the analogy without requiring technical background.

---

### RF-03 — Exercise 6: Assessment Manager as hub visualisation
**Gemini finding:** Help the listener visualise the Assessment Manager as the hub so the list of message flows has a mental map.
**Status:** `fixed`
**Location in v1.1:** Part 7 — 练习 6：电子土地开发申请协作图, B's opening paragraph.
**Change applied:** Added a hub-and-spoke framing sentence before the decision list: listener is asked to picture the Assessment Manager as the central hub; other parties (applicant, cadastre, roads, natural resources, environment, council) radiate from it; messages flow outward as queries and inward as responses; the final approval flows back to the applicant through the hub. This gives a spatial/structural mental model before the 12-point message list.

---

### RF-04 — Markdown artifacts before TTS-clean
**Gemini finding:** Before TTS-clean, remove/convert markdown artifacts (horizontal rules, tables, editorial headings).
**Status:** `deferred` — to TTS-clean stage (next stage)
**Reason:** The fix instructions specify this as a pre-TTS-clean action, and the production stage boundary explicitly says "Do not create the TTS-clean file in this stage." Tables, horizontal rules, and section headings are editorial scaffold that belong in the v1.1 source script for human review; they will be stripped in the TTS-clean pass. Recorded here so the TTS-clean operator does not miss it.

---

## Source-Check Findings Status

| NSC ID | Area | Gemini verdict | Status in v1.1 |
|---|---|---|---|
| NSC-02 | W06-D01-S007/S008 intra-pool anti-patterns | PARTIAL → needs audible visual sentence | Fixed: concrete XOR→AND-join oral description added (CF-06) |
| NSC-04 | W06-D02-S003 PO signal example | PASS/acceptable with caution | No new topology claim added; signal/message distinction kept clear; PA-system analogy used in walkthrough for coherence |
| NSC-05 | Exercise 2 diagram | FAIL until fixed | Fixed: specific deadlock answer added (CF-07) |

---

## Terminology Audit — v1.1 Compliance

| Term | Chinese → English → notation/SESE → plain explanation → example | Status |
|---|---|---|
| 结构正确性 | Structural Correctness | ✓ all components present (CF-01) |
| 语法正确性 | Syntactical Correctness | ✓ all components present (CF-02) |
| 语义正确性 | Semantic Correctness | ✓ explanation + counter-example (unchanged from v1.0, was compliant) |
| 行为正确性 | Behavioural Correctness | ✓ token-game tool named + concrete example (CF-03) |
| 块结构化 | Block-structuredness → SESE | ✓ SESE notation added + single-door-room example (CF-04) |
| 信号 | Signal → broadcast plain explanation → PA-system example | ✓ (CF-05) |
| 令牌游戏 | Token Game | ✓ chess-piece analogy in Part 2 (unchanged from v1.0, was compliant) |
| 消息 | Message | ✓ registered-letter analogy (unchanged from v1.0, was compliant) |

---

## Coverage Audit — v1.1

All 19 coverage ledger rows (W06-D01-S001 through W06-D03-S003) are present in `ep06_script_v1.1.md`. The coverage checklist at the end of the script has been updated to note which rows received new content in the v1.1 edit. No rows were dropped.

---

## Codex Usage Confirmation

None. No Codex CLI, Hermes-bound Codex, or Codex tokens were used in any part of the review/fix stage.

---

*End of ep06_review_fix_checklist_v1.1.md*
