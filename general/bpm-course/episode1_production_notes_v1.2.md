# EP01 V1.2 Production Notes

## Source
- Course: Week 01 - Introduction to BPM
- Main script: `ep01_script_v1.2.md`
- TTS-clean script: `ep01_tts_script_v1.2.txt`
- Source inventory: `../source_inventory.md`
- Coverage ledger: `../coverage_ledger.csv`

## V1.2 Changes
- Added explicit coverage for Slide 8: organisation elements such as assets, knowledge, suppliers/customers, culture, IT assets, dynamic capabilities, and business processes.
- Strengthened Slides 6-7: activity lists are not yet processes; activities must be connected into end-to-end paths by customer outcome.
- Expanded Ford case with actors, customer/value, and possible outcomes.
- Added TQM, Business Process Re-engineering, and stochastic/probabilistic process mining to the related-disciplines/course-highlights segment.
- Adjusted Chinese listening flow: replaced awkward wording like “整理洗衣”, reduced “bad process is better than none” ambiguity, and localized dense English terms in the TTS script.
- Independent review path used GPT-5.5; Claude Code CLI remains the fallback route if GPT-5.5 is unavailable.

## TTS Parameters
- Provider: Gemini TTS
- Stable model: `gemini-2.5-flash-preview-tts`
- Chunk target: <= 650 Chinese characters per request to avoid 60s read timeout.
- Required speech speed: **0.9x current default**.
- Implementation: synthesize chunked 24kHz mono PCM/WAV at provider default, then apply `ffmpeg` `atempo=0.9` to produce the final MP3. This gives an exact 10% slowdown even though the current Gemini TTS API wrapper does not expose a native speed field.
