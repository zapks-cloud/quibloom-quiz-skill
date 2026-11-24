# Quibloom quiz video: production specification (factual, from the working renderer)

Output: 1080x1920 (9:16), 30 fps, H.264 (libx264 crf 15, preset medium, yuv420p) video, AAC 192k audio, faststart. About 350-375 s per video, 15 questions.

## Structure
1. Intro: Quibloom logo, "Quibloom", "15 QUESTIONS" (yellow underline), "NO SECOND CHANCES" (cyan). Hook narration.
2. Per question: header (logo + "Quibloom", counter "NN / 15" top right), category pill (e.g. PLANTS), question text (wrapped, white bold), label "CHOOSE YOUR ANSWER" over a yellow progress bar. Options A-D appear one by one as each is spoken (card pop-in, yellow letter badge). After the last option, a 5 second countdown (circle + ring, progress bar drains). Reveal: label turns green "CORRECT ANSWER", the correct card turns green with a green badge and white tick, other cards dim, confetti particles, tick sound, then the spoken line "Option X is correct. <answer>".
3. Outro: "WHAT IS YOUR SCORE?" with "? / 15", LIKE and SHARE buttons (cyan) and a yellow SUBSCRIBE button with bell. CTA narration.

## Typography and colors (r.py)
Font Noto Sans (Bold, Regular). Navy background (16,46,68), card (24,61,82) with border (38,86,108), highlighted card border cyan (38,190,217), yellow (255,208,48), green (110,190,70), green card bg (38,87,44), light green (175,240,150), dim text (120,150,170). Cards 952x140 px, radius 24. Badges 86x86, radius 16. Large faint ring shapes in the background and small floating dots.

## Audio
Narration by a TTS voice (Sadachbia) with the instruction: "Engaging English quiz host, bright and clear at a natural pace. Give each answer option a distinct beat. No rushed delivery." One WAV per clip: hook, cta, vNN_qXX (question + options read aloud), vNN_aXX (answer line). Small synthesized sound effects (pop, tick, ding, whoosh) are mixed under it.
Option timing: the renderer finds the last 8 speech segments of each question clip (the question stem is excluded) and uses the 4 option-letter onsets, using the two largest gaps as separators with a 0.12 then 0.2 s gap pass. Validation (cmp.py): letter segments under 0.6 s, spacing between options 1.2-3.4 s.

## Rendering pipeline
- python3 scripts/main2.py videoNN.json clipdir out/vNN mix   (builds mix + timeline)
- python3 scripts/main2.py videoNN.json clipdir out/vNN chunk A B  (900-frame chunks, keyframe every 30 frames, ranges must not overlap; last chunk ends at int(total*30))
- scripts/fin.sh NN name.mp4: concat with stream copy (no re-encode), AAC 192k, checks frame count, duration, sha256.
- scripts/qa.py: contact sheet of stills, audio extract for answer checks.
Required: Pillow, numpy, ffmpeg, Noto Sans fonts. About 10 min render per video on 2 cores.

## Content
videoNN.json holds 15 questions each with options, correct_index, answer_letter, question_speech, answer_speech and a Wikipedia source URL. Facts were checked per question against the source page, with a semantic review, and no repeated questions across videos.

## QA workflow
1. ASR (speech to text) every narration clip; fix mismatches.
2. Standalone letters are often misheard by ASR; regenerate answer clips as "Option X is correct. <answer>" and re-check.
3. After render: view the contact sheet, ASR the answer clips on the final audio, check frame count/duration, sha256, and a motion clip across chunk boundaries.
4. Never re-encode the final file; delivery is the stream-copy concat.
