# EP03 v3.0 — Gemini Review

**Reviewer:** Gemini CLI 3.1 Pro (gemini-3.1-pro-preview)
**Generator:** Gemini CLI 3.1 Pro (gemini-3.1-pro-preview)
**Date:** 2026-05-29

**Verdict:** NEEDS_FIX
**Publish recommendation:** GO_AFTER_FIX

## Findings

### Priority 1 — CRITICAL: OR Join 死锁语义错误 (Line 67-69)
- **Issue:** Script described "bus driver leaving early" as deadlock, but this is "Proper Completion" violation per BPMN semantics
- **Fix:** Rewrote to the correct scenario — two OR Joins waiting for each other (mutual dependency deadlock)
- **Status:** ✅ FIXED

### Priority 2 — Missing Quality Assurance content (after Line 93)
- **Issue:** Source slides dedicate 3 pages to human-vs-computer QA division (computer → structural/behavioural; human → semantic/conventions). Missing from script.
- **Fix:** Added B dialogue on Quality Assurance: "前两层电脑自动检查，后两层必须人工同行评审（Peer Review）"
- **Status:** ✅ FIXED

### Priority 3 — Terminology protocol: missing example sentences
- **Issue:** Behavioural Correctness (Line 81) and Model Conventions (Line 93) missing required 例句
- **Fix:** Added example sentences for both terms
- **Status:** ✅ FIXED

## Positive Findings
- Map metaphor (国家/桥梁/道路/检查站) threaded consistently throughout
- Host A heuristic exploration strong (burger toppings exercise)
- Causal bridges between sections, not checklist transitions
- Exercise walkthrough engaging (Token Game, semantic absurdity catch)
