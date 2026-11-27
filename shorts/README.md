# Quibloom Shorts production source

Contains the portable renderer, QA, thumbnail and layout-check code, plus one sample quiz source and one sample TTS manifest. No credentials, account IDs, catalogs or Drive/YouTube state.

## Pipeline (5-question Short, 1080x1920, 30 fps, YouTube Shorts only)
1. Write a source JSON (see samples/short_l14_3_landmarks.json): 5 questions, 4 options, correct_index, question_speech, answer_speech, short on-screen reveal, source URL, source_keyword, stock_q (internal only, never spoken).
2. Write a TTS manifest (samples/tts_manifest_l14_3_orig.json): voice, instruction, pronunciation directions, one clip per question and per answer (IDs vNNN_qNN / vNNN_aNN). Numbers and years are spelled as words in speech text. Spoken question numbers are always "Question one" to "Question five".
3. Put the 10 generated wavs plus cta.wav (closing clip, reused) in a clip dir. Build the project JSON (video id, topic, category, intro_line, skip_intro=true, questions).
4. `python3 main2.py project.json clipdir out/vNNN mix` writes out/vNNN.wav and out/vNNN.tl.json (timeline, total seconds).
5. Render video in chunks of 900 frames, two per call: `python3 main2.py project.json clipdir out/vNNN chunk A A+900` for A = 0, 900, 1800, ... while A < frames (frames = int(total*30)). Chunks are joined by stream copy with no re-encode.
6. `bash fin.sh NNN Name.mp4` joins the chunks, adds AAC 192k audio, prints frame count, duration, sha256, size, and splits into 18 MB parts.
7. `python3 chk.py NNN final/Name.mp4` is the safe-margin check (below). `python3 qa2.py NNN Name.mp4` makes the QA contact sheet, a tail clip and 4 ASR audio windows.
8. Thumbnails: thumbnails/thumb.py `make(topic, category, out, icon, bt0='5 QUESTIONS  |  SCORE 5/5?')`, 1280x720 JPEG with a topic icon.
fix1.sh / pack.sh / fixrev.py in qa/ are helpers that re-render only the chunks covering one changed reveal, and that package hashes, parts and full-size reveal frames.

## Format history
- RETAINED, final: original S01 format. Intro skipped, no hook text, answer options appear one at a time, a 5 second countdown after the options, then the reveal. Questions in stock order. Closing "Did you get five out of five" card.
- DISCARDED: the S01v2 / pilot v2 variant (hook line, options together, timer bar). The channel owner chose the original format. The v2 backup files are not included on purpose.

## Latest accepted layout and safe-margin rule
- The reveal text is at most 3 lines (about 90 characters of on-screen text; the speech may be longer). A 4-line reveal ends at y=1895 to 1909 on the 1920 px frame, which is too tight. 5 lines are cut off.
- chk.py samples the last 0.4 s of each question scene, finds the lowest bright text row below y=1500, and flags the render if any row is lower than y=1850. Three-line reveals measure about 1760 to 1841. Run it after fin.sh on every render, before the QA sheet.
- To fix an overflow, shorten the on-screen reveal in the project JSON only, re-mix (timeline must stay identical), re-render only the chunks that cover that reveal, run fin.sh and chk.py again.
- QA is ASR and frames only. It never claims anything was listened to. ASR spelling or number-format differences are "uncertain", not failures.

## Content rules
- Facts are checked at claim level against the cited source page. A reveal must not give away another question's answer, including in the other two episodes of the same 15 question stock quiz.
- A 5Q Short must stay under 3:00. Masters so far are 130 to 168 s.
- Hardcoded paths to adjust when porting: /tmp/t/..., /tmp/th/..., /downloads/ (qa2.py, thumb.py), QUIBLOOM_LOGO env var (path of render/quibloom-logo.png). Fonts: Noto Sans (system path or ../assets/NotoSans-*.ttf).
- Requires: python3, numpy, Pillow, ffmpeg and ffprobe.

See ../docs/PRODUCTION-DEFAULTS.md for the daily volume and publishing defaults, and ../SKILL.md section 13 for how Shorts fit with the long quizzes.
