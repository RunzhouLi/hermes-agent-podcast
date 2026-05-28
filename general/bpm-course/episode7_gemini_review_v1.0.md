# EP07 Gemini Independent Review v1.0

Captured from official Gemini CLI TUI (`gemini-3.1-pro-preview`) on 2026-05-28. Review-only pass; no Codex usage.

## Verdict
  PASS_WITH_MINOR_FIXES


## Source coverage audit
   - Any missing or under-covered source rows: None. All source slides and Exercises 1–6 are comprehensively covered in the script and
     perfectly align with the course map and episode plan.
   - Any source ambiguities requiring visual/source check: None. Visual models are accurately verbalized and reconstructed linearly for the
     listener.


## Mathematical correctness audit
   - XOR/OR gateway probabilities: Correct. The script accurately explains that XOR branches must sum to 1.0, while OR individual branches
     do not, and correctly illustrates the joint probability distribution of OR combinations summing to 1.0.
   - Event-based gateway and negative exponential CDF: Correct. The rate parameter (λ = 1/mean) and CDF formula (1 - e^{-λ x}) are correctly
     applied. The time-based derivation logic is flawlessly explained.
   - Trace/path probability: Correct. The script properly distinguishes between a linear trace and a partially ordered path, and correctly
     instructs to sum the probabilities of all paths that cover the trace.
   - Annotation from event logs: Correct. Accurately accounts for loop instances by dividing branch choices by the total gateway arrivals
     rather than just the total number of process instances (as demonstrated in Exercise 2: 120 total arrivals vs. 105 total instances).
   - Exercises 1–6 calculations, especially Exercise 4 and Exercise 6: All calculations are precise. Exercise 4 accurately calculates the
     trace probability. Exercise 6 correctly applies the exact hyperexponential survival function formula for two sequential exponential
     distributions and simplifies it correctly to prove the negligible probability of the timer firing.


## Terminology/listenability audit
   - Terms missing audible Chinese → English → abbreviation/plain explanation → example introduction: All core terms follow the bilingual
     card protocol successfully. (Note: Event-Based Gateway omits an abbreviation, but this is acceptable as there is no standard
     abbreviation for it).
   - Dense paragraphs that need Host A comprehension-governor restatement: The mathematical derivation in Exercise 6 is dense, but Host A
     actively tracks, breaks it up, and restates the sign groupings (e.g., "整理一下符号"), acting as a strong governor. The math is
     surprisingly TTS-friendly (e.g., "一减去 e 的负 lambda 乘 x 次方").
   - Any markdown/editorial artifacts unsuitable for TTS-clean conversion: The script uses the isolated English word "survival" in the
     middle of Chinese sentences during Step 7 / Exercise 6 (e.g., "它的‘还没完成’概率，survival，有一个...", "续费这条的 survival"). Mixing
     a standalone English word without its Chinese pair in this context can cause awkward language-switching pauses in a TTS engine.


## Concrete fix checklist
   - [ ] Script Step 7 / Exercise 6: Replace standalone instances of the word "survival" with the Chinese equivalent "还没寄到的概率" or
     "存活概率" to ensure smooth, continuous TTS reading without language-switching glitches.
   - [ ] Show Notes: Update the "制作链路" provenance line. It currently says 初稿 Gemini 3.1 Pro → 审阅 Claude → 终编 Hermes Autoproducer,
     which contradicts the script metadata stating Gemini 3.1 Pro failed with a 429 capacity error and the draft actually came from Claude.
     Change it to 初稿 Claude → 终编 Hermes Autoproducer.


## Provenance note
  Model used: Gemini 3.1 Pro (via internal CLI tool). This is a complete review of the provided artifacts. No Codex usage was employed.
