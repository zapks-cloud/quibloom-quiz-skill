# Quibloom Quiz Video Skill

A complete, reusable recipe for producing full-length vertical quiz videos in
the Quibloom format: 15 multiple-choice questions per video, English
narration, animated option cards, a 5-second countdown, and a green answer
reveal. The finished videos are about 6 minutes long, not short clips.

Use this skill when the user asks for a quiz video, a trivia video, or a new
episode for a quiz channel. This repository holds the renderer, the content
pipeline, a verified example question script, and the brand asset. Voice
recordings (WAV clips) are NOT included; section 4 describes how to produce
them with any text-to-speech provider or a human voice.

---

## 1. What the finished video looks like

- Vertical 1080x1920, 30 fps, H.264 (crf 15) + AAC 192 kbps, faststart.
  About 5.5 to 6.5 minutes for 15 questions at a natural pace.
- Deep navy background with slowly rotating rings and drifting particles.
- Brand header on every question: small logo, channel name, and a
  "03 / 15" counter.
- Hook intro: the logo spins in, then "15 QUESTIONS", "NO SECOND CHANCES",
  three "?" dots, and a yellow "LET'S FIND OUT" pill.
- Question loop, 15 times:
  1. A category pill (for example SPACE) and the question text fade in.
  2. The narrator reads the question and the four options.
  3. Each option card slides in from the left exactly when the narrator
     says it, with a pop sound. The card pulses while it is being read.
  4. "CHOOSE YOUR ANSWER" with a yellow timer bar that drains over a
     5-second countdown. A circular countdown appears at the bottom with
     a tick each second.
  5. Reveal: the bar turns green, the correct card turns green with a
     drawn checkmark and a sparkle burst, wrong options dim, and a ding
     plays. The narrator says the answer ("C is correct, Mercury.").
  6. Short beat, then the next question.
- Outro: "WHAT IS YOUR SCORE? ? / 15", animated LIKE and SHARE buttons,
  then a SUBSCRIBE button that flips to SUBSCRIBED.

Never speed up the questions. The viewer needs thinking time. Natural pace
is a hard requirement from the channel owner.

## 2. Brand identity

Exact palette (RGB), defined at the top of `renderer/r.py`:

| Role | Name | RGB |
|---|---|---|
| Background navy | NAVY | (16, 46, 68) |
| Card fill | CARD | (24, 61, 82) |
| Card border | CARDB | (38, 86, 108) |
| Accent cyan | CYAN | (38, 190, 217) |
| Accent yellow | YEL | (255, 208, 48) |
| Correct green | GREEN | (110, 190, 70) |
| Correct green background | GREENBG | (38, 87, 44) |
| Check light green | GREENL | (175, 240, 150) |
| Dimmed text | DIM | (120, 150, 170) |

Typography: Noto Sans Bold everywhere. Question text starts at 88 px and
shrinks by 4 px until it fits 3 lines inside 900 px. Option text starts at
56 px and shrinks by 2 px until it fits 760 px. The wordmark is "Quibloom".

Logo: `assets/quibloom-logo.png` (turquoise Q with a yellow stem on navy).
The renderer makes the navy background of the logo transparent at load.
To rebrand, replace this one file and adjust the palette in
`renderer/r.py`.

## 3. Content pipeline

Each video is driven by one JSON file (`content/videos/video01_space.json`
is a complete verified example; that directory holds the verified scripts
for all 20 channel videos):

```json
{
  "video": 1,
  "topic": "Space",
  "category": "SPACE",
  "hook": "Fifteen questions, no second chances. Can you score fifteen out of fifteen? Let us find out.",
  "questions": [
    {
      "n": 1,
      "question": "Which planet is closest to the Sun?",
      "options": ["Venus", "Earth", "Mercury", "Mars"],
      "correct_index": 2,
      "answer_letter": "C",
      "question_speech": "Question one. Which planet is closest to the Sun? A. Venus. B. Earth. C. Mercury. D. Mars.",
      "answer_speech": "C is correct, Mercury.",
      "source": "https://science.nasa.gov/mercury/"
    }
  ]
}
```

Rules for writing questions:

- 15 questions per video, one clear topic per video. The channel so far:
  Space, Animals, Ocean life, Human body, Geography, Science, History,
  Technology, Earth, Food, Dinosaurs, Chemistry, Mathematics, Landmarks,
  Birds, Music, Sports, Mythology, Art, Plants.
- Every question must have one unambiguously correct answer that a reader
  can verify on a cited source page (Wikipedia or an official reference
  such as nasa.gov). Record the source URL per question.
- Three plausible wrong options of the same type as the answer. No joke
  options, no "all of the above".
- Spread the correct letter across A, B, C, D. The generator
  (`content/gen.py`) rotates the correct position through a fixed pattern
  and shuffles distractors with a seeded random generator, so runs are
  reproducible.
- Speech text is explicit: "Question three. What is the largest ocean on
  Earth? A. Atlantic. B. Pacific. C. Indian. D. Arctic." and
  "B is correct, the Pacific." Write numbers and symbols as spoken words
  ("3.14" as "three point one four", "H2O" as "H two O"). If speech
  recognition keeps mishearing a standalone letter or short answer,
  record the answer line in the fuller form "Option B is correct. Ra."
  and, when needed, extend the answer itself ("Ra, the sun god").

Fact-check before rendering. `content/ver.py` downloads every cited page
and confirms the answer string actually appears on it. `content/sem.py`
prints the matching sentence so a human or model can confirm the page
supports the claim, not just the string. Never render a question whose
answer failed verification; fix the question or the source first.

## 4. Voice production (external, provider-neutral)

This repository does not include voice audio. You supply one WAV clip per
spoken unit, from any TTS provider or a recorded voice:

- Filenames inside the clip directory: `hook.wav`, `cta.wav`,
  `vNN_q01.wav` to `vNN_q15.wav` (question plus options, exactly the
  `question_speech` text), `vNN_a01.wav` to `vNN_a15.wav` (the
  `answer_speech` text). NN is the video number, zero-padded.
- Format: WAV, 16-bit PCM, mono. Any sample rate works; the mixer
  resamples to 48 kHz. Keep silence at the edges short (under 300 ms),
  because option card timing is detected from the audio.
- Voice direction used for the channel: one consistent narrator for the
  whole series, a bright, clear English quiz-host voice at a natural
  pace, each answer option given a distinct beat, no rushed delivery.
  The reference videos use Google's "Sadachbia" TTS voice.
- `content/gen.py` shows how the speech texts and a TTS manifest are
  generated from the question bank; adapt it to your provider's API.
- `content/reg.sh` assembles a clip directory for one video from a pool
  of WAV files.

Quality check on the audio itself: transcribe every clip (any speech
recognition tool) and confirm the question, all four options, and the
answer are said correctly. Watch out for homophones: a recognizer may
write "Raw" for a correct "Ra". Judge the sound in context; do not
regenerate forever chasing a spelling the voice already pronounces right.

## 5. Rendering

Requirements:

- Python 3.9+ with `pip install pillow numpy`
- ffmpeg with libx264 on PATH
- Noto Sans Bold and Regular. The renderer looks for
  `NotoSans-Bold.ttf` / `NotoSans-Regular.ttf` in common Linux font
  directories, then in `assets/`. On Debian/Ubuntu:
  `apt install fonts-noto-core`. Or copy the two TTF files into
  `assets/`.
- The logo: `assets/quibloom-logo.png`, or point the `QUIBLOOM_LOGO`
  environment variable at another PNG.

Build one video:

```
python3 renderer/main2.py content/videos/video01_space.json CLIPDIR out.mp4
```

`CLIPDIR` holds the WAV clips named as in section 4. The builder:

1. Detects option timing from each question clip (see `opt_times` in
   `renderer/main2.py`).
2. Builds the timeline: intro, 15 question scenes, outro. Each question
   scene is 0.4 s lead-in, the question clip, 0.4 s pause, a 5 s
   countdown, 0.25 s, the answer clip, 1.3 s tail.
3. Draws every frame with PIL (`renderer/r.py`): animated background,
   header, cards, countdown ring, reveal with check and sparkles.
4. Mixes audio: narration clips at their times plus synthesized sound
   effects (pop on card entrance, tick each countdown second, ding on
   reveal, whoosh on transitions), peak-normalized to 0.92.
5. Encodes H.264 crf 15 preset medium, yuv420p, AAC 192k, faststart.

Other modes:

```
python3 renderer/main2.py PROJ CLIPDIR out.mp4 mix          # audio mix only -> out.mp4.wav
python3 renderer/main2.py PROJ CLIPDIR out.mp4 still 12.0 47.5  # single frames -> out.mp4.s_0012.0.png
python3 renderer/main2.py PROJ CLIPDIR out.mp4 chunk 0 5400     # frames 0..5400 -> out.mp4.c00000.mp4
```

Use `chunk` to split a long render across processes or machines (the
production pipeline uses 900-frame chunks), then concatenate the chunk
files and mux with the mixed audio. Chunks are plain frame ranges, so
plan them to cover the full timeline exactly once with no gaps and no
overlaps, and always check the seconds around each boundary on the
final file (`renderer/qa.py` cuts an 8-second motion-proof clip across
a boundary for this).

Finishing and QA helpers in `renderer/`:

- `fin.sh NN out.mp4`: joins the chunks with stream copy (never
  re-encodes), muxes the mixed audio as AAC 192k with faststart, prints
  frame count, duration and SHA-256, and splits the master into 18 MB
  delivery parts.
- `qa.py NN out.mp4 q1,q2`: builds a contact sheet of stills (intro, a
  mid-question frame, reveals of the listed questions, outro), extracts
  the answer audio of the listed questions for transcription checks, and
  cuts an 8-second motion-proof clip across a chunk boundary.
- `cmp.py NN`: prints the detected option onsets per question and the
  speech-segment counts, for checking the alignment described in
  section 6.

## 6. Alignment fallback and manual overrides

Option card entrances are timed automatically from the question audio:

1. Preferred: the detector finds the last eight speech bursts in the
   clip, takes every second one as an option start, and accepts them if
   each burst is under 0.6 s and starts 1.2 to 3.4 s apart.
2. Fallback: it finds the pause before the options (at least 0.7 s of
   silence after 2 s of speech), then picks the option starts that best
   match expected option lengths.

If a clip still aligns badly, add explicit times to that question in the
video JSON, in seconds relative to the start of its question clip:

```json
"option_start_times": [3.2, 5.2, 7.2, 9.2],
"option_end_times": [3.6, 5.6, 7.6, 9.6]
```

`option_end_times` is optional; without it each card stays highlighted
until 0.15 s before the next one starts.

## 7. Quality checks before delivery

- Audio transcript check on every clip (section 4).
- Still-frame check: dump frames of the intro, one question mid-countdown,
  several reveals, and the outro with `still` mode. Confirm the green card
  is the correct option, no text is clipped or overlapping, and the
  countdown shows.
- Full motion check: watch the final MP4 end to end at normal speed.
  Confirm option entrances land on the spoken options, the countdown is
  never cut short, scene transitions are clean, and the sound effects
  match the visuals. If the video was rendered in chunks, also watch the
  seconds around each chunk boundary.
- Final file check: 1080x1920, 30 fps, about 5.5 to 6.5 minutes, audio
  present, and record the file size and SHA-256 in the channel catalog.

## 8. Reproducibility

- Question shuffle and answer positions come from a seeded random
  generator (`content/gen.py`), so the same bank produces the same
  question JSON.
- Sound effects are synthesized with a fixed seed, so the mix is
  deterministic for the same clips.
- A video rebuilt from the same JSON and the same WAV clips produces the
  same timeline. The encoded bytes can differ across ffmpeg versions;
  compare duration, frame count, and streams rather than checksums across
  machines.

## 9. Troubleshooting

- Text overflows or touches a card edge: the auto-shrink floor is
  reached. Shorten the question or option text; long options are the
  usual cause.
- Option cards land off the narration: the clip has unusual pauses. Add
  `option_start_times` for that question (section 6).
- Countdown feels rushed: the question clip has long trailing silence.
  Re-export the clip with tighter edges; do not pad the countdown instead.
- Font not found: install `fonts-noto-core` or drop `NotoSans-Bold.ttf`
  and `NotoSans-Regular.ttf` into `assets/`.
- Render is slow: use `chunk` mode to split the frame range across
  processes or machines.
- Recognizer hears "Raw" instead of "Ra": known homophone limitation,
  judge by ear; the on-screen text is the source of truth for spelling.

## 10. Publishing metadata

Per video, prepare a title, description, hashtags, and a pinned comment,
following the channel catalog's pattern:

- Title: "Space Quiz: 15 Questions, Can You Score 15/15?" (topic swapped
  per video).
- Description: "15 questions about <topics>. Pick A, B, C or D before the
  5 second timer ends. No second chances. Comment your score out of 15!"
- Hashtags: a few topic tags plus quiz tags, as decided per video.
- Pinned comment: "What was your score out of 15? Tell us below, and
  subscribe to <channel> for the next quiz!"

Publish only when the channel owner says when. Deliver originals at full
quality; never recompress the master file for delivery.

## 11. Licensing and credits

What is verified:

- Noto Sans fonts are distributed under the SIL Open Font License; get
  them from your OS package manager or Google Fonts.
- Each question cites the page its answer was verified against (mostly
  Wikipedia, some official sites such as nasa.gov). Those sources keep
  their own licenses; keep the per-question source links so readers can
  check them. Wikipedia article text is generally CC BY-SA, but images
  and other media on those pages can have different terms.

Not settled, by design:

- No open-source license file is included and no explicit reuse license
  is granted. The code and the Quibloom brand assets were produced for
  the channel owner's own project; whether and how to license them for
  reuse is the owner's decision and has not been made.

## 12. Repository layout

```
SKILL.md                  this file
docs/PRODUCTION-SPEC.md   factual spec of the production pipeline
renderer/r.py             all drawing: palette, background, cards, reveal
renderer/main2.py         timeline builder, audio mix, encoder
renderer/fin.sh           chunk join, mux, checks, delivery parts
renderer/qa.py            contact sheet, answer audio extract, motion proof
renderer/cmp.py           option-alignment printout
assets/quibloom-logo.png  brand logo (replace to rebrand)
content/data.py           question bank with sources (videos 11-20)
content/qs.py             question bank with sources (videos 2-10)
content/gen.py            builds video JSON + speech manifest from the bank
content/ver.py            fact-check: answer string must appear on source page
content/sem.py            prints the supporting sentence for manual check
content/reg.sh            assembles the clip directory for one video
content/videos/           the 20 verified video JSON scripts
docs/PRODUCTION-DEFAULTS.md  daily volume, Shorts format, publishing schedule
shorts/                   5-question Shorts: renderer, QA, thumbnails, samples
```

## 13. Shorts and daily plan

Besides the 15-question long quizzes, the channel makes 5-question Shorts
(1080x1920, under 3:00, YouTube Shorts only). The code, QA scripts,
thumbnail generator and a sample source and TTS manifest are in `shorts/`.
Read `shorts/README.md` for the pipeline.

- Format: the original native format. No hook text, options appear one at
  a time, 5 second countdown, green reveal, closing card. A Short is one
  third (questions 1 to 5, 6 to 10, 11 to 15) of a 15-question stock quiz.
- Safe margins: keep all text inside the frame with room to spare. The
  reveal is at most 3 lines. Run `shorts/render/chk.py` on every render; it
  rejects reveal text below y=1850 on the 1920 px frame.
- Every video, long or Short, gets a matching custom thumbnail.
- Defaults: 20 long plus 20 Shorts produced per day. Shorts are published
  on YouTube only, 2 per day at 13:00 and 21:00 Morocco time. Long videos
  are published 1 per day at 19:00 Morocco time. Oldest first. See
  `docs/PRODUCTION-DEFAULTS.md`. These are planning defaults, not
  permission to publish; the channel owner decides when.
- Section 10's one-quiz-per-day wording applies to long videos only.
