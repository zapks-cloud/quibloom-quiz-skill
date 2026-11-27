# Production and publishing defaults (as of November 27, 2026)

These are the channel owner's current defaults for the Quibloom channel. They are defaults for planning, not permissions: anything that publishes, uploads or signs in to an account still needs the owner's own go-ahead in that conversation.

## Daily production
- 20 long quizzes per day: 15 questions each, about 6 minutes, 1080x1920, format in SKILL.md.
- 20 Shorts per day: 5 questions each, under 3:00, 1080x1920, format in shorts/README.md. A Short is one third of a 15-question stock quiz (stock questions 1 to 5, 6 to 10, 11 to 15), so a reveal must never give away another question's answer, including in the other two episodes.
- Every video, long or Short, gets a matching custom thumbnail (1280x720 JPEG). Long videos use the quiz thumbnail style; Shorts use shorts/thumbnails/thumb.py with a topic icon.

## Short format (final)
- Original S01 native format: no hook text, intro skipped, answer options appear one at a time, a 5 second countdown after the options, then the green reveal. Questions in stock order. Closing card "Did you get five out of five".
- The later S01v2 variant (hook line, all options together, timer bar) was dropped by the owner and is not part of this package.
- All on-screen text must stay inside safe margins. The reveal is at most 3 lines (about 90 characters). shorts/render/chk.py fails any render with reveal text lower than y=1850 on the 1920 px frame. Run it on every render.

## Publishing schedule (Morocco time, Africa/Casablanca)
- Shorts: YouTube only, 2 per day, at 13:00 and 21:00.
- Long quizzes: 1 per day at 19:00.
- Oldest unpublished video first, within each kind.
- Keep the rest as private stock until its slot.

## QA
- Automatic checks only: ASR transcript of every clip, frame contact sheet, tail clip, safe-margin check, full decode, frame count, duration, SHA-256. Never claim a video was listened to unless a person did.
- Store every master with its thumbnail and record size and SHA-256 in the channel catalog. The catalog itself is private and is not kept in this repository.

## Not in this repository
Account credentials, account-access approvals, upload tool grants, channel catalogs with file IDs, and chat or operational logs.
