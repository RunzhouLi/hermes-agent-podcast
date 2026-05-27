# EP03 Gemini CLI Review

Reviewer: Gemini CLI terminal client
Model shown by CLI: `gemini-3.1-pro-preview`
Mode: `--approval-mode plan --screen-reader`
Prompt: `ep03_gemini_review_prompt.md`

## Verdict

NEEDS_FIX

Gemini judged the Markdown master script as conceptually strong and accurate, but found two fix-before-TTS issues.

## Required fixes

1. **High priority — TTS script dialogue lost/compressed near the ending**
   - Location: `ep03_tts_script_v1.0.txt` ending / exercise section.
   - Issue: the Markdown script's fifth section contains a multi-turn dual-host exercise discussion, especially the Token Game walkthrough, but the TTS script compressed it into a long Speaker B monologue.
   - Fix: restore the exercise section as dual-host dialogue in the TTS script, following the Markdown script's interaction pattern.

2. **Medium priority — exercise coverage disclosure incomplete**
   - Location: `ep03_script_v1.0.md` fifth section and `ep03_show_notes.md`.
   - Issue: Week 03 exercises contain 5 questions, but the script/show notes focus on the first 3 and do not mention Exercise 4 or 5.
   - Fix: either cover exercises 4 and 5 or explicitly state that the episode focuses on the first 3 representative exercises and leaves exercises 4 and 5 for after-class practice.

## Positive findings

- BPMN conceptual correctness is high.
- OR Join deadlock risk, Message Flow vs Sequence Flow boundary, and Semantic Correctness are explained accurately.
- No obvious hallucination or public-release risk was flagged.
- English terms such as Inclusive Gateway and Soundness are introduced clearly enough for audio.

## Recommendation

GO_AFTER_FIX — after restoring the TTS ending dialogue and adding the exercise-scope disclosure, proceed to TTS production and publication.
