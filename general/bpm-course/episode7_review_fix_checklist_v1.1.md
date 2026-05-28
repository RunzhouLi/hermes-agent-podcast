# EP07 Review/Fix Checklist v1.1

Review source: `episode7_gemini_review_v1.0.md`
Reviewer: Official Gemini CLI TUI, requested/observed model `gemini-3.1-pro-preview`
Verdict: `PASS_WITH_MINOR_FIXES`
Final editor: Hermes Autoproducer
Codex usage: none

## Accepted review findings

- [x] Script Step 7 / Exercise 6: Replace standalone English `survival` occurrences with smoother Chinese audible wording (`存活概率` / `还没寄到的概率`) to avoid TTS language-switching glitches.
  - Fixed in: `episode7_script_v1.1.md`
  - Verification: no standalone `survival` remains in `episode7_script_v1.1.md`.

- [x] Show notes provenance: correct stale `制作链路` line that incorrectly said `初稿 Gemini 3.1 Pro → 审阅 Claude → 终编 Hermes Autoproducer`.
  - Fixed in: `episode7_show_notes_v1.1.md`
  - Corrected provenance: `初稿 Claude CLI artifact（exact model not captured）→ Gemini CLI gemini-3.1-pro-preview 独立审阅 → Hermes Autoproducer 终编修订`.

## Deferred items

None. Gemini marked coverage/math/terminology/listenability as pass with only the two minor fixes above.

## Next stage

TTS-clean/render-prep for EP07: convert `episode7_script_v1.1.md` into parseable A/B TTS lines, preserve audible terminology explanations, record render provenance, and prepare Doubao/Volcengine renderer constants. Do not render until the render-prep gate passes.
