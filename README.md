# Quibloom Quiz Videos

Full-length vertical quiz videos (about 6 minutes, 15 questions each):
animated option cards synced to narration, a 5-second countdown, and a
green answer reveal, in the Quibloom navy/cyan/yellow brand.

Start with [SKILL.md](SKILL.md): the full production recipe, from question
writing and fact-checking through voice production, rendering, QA, and
publishing metadata. Arabic quick start for the channel owner:
[README.ar.md](README.ar.md).

## Quick start

Voice clips are not included; see SKILL.md section 4 for the required WAV
format and voice direction.

```bash
pip install pillow numpy        # plus ffmpeg and Noto Sans fonts
python3 renderer/main2.py content/videos/video01_space.json CLIPDIR out.mp4
```

`CLIPDIR` is a folder of WAV clips: `hook.wav`, `cta.wav`, `v01_q01.wav`
to `v01_q15.wav`, `v01_a01.wav` to `v01_a15.wav`.

## Shorts

5-question Shorts (1080x1920, YouTube Shorts only) have their own pipeline in [shorts/](shorts/README.md). Daily volume and publishing defaults: [docs/PRODUCTION-DEFAULTS.md](docs/PRODUCTION-DEFAULTS.md).

## License

No license file is included on purpose: the channel owner decides whether
and how to license this material. Question sources keep their own
licenses (Wikipedia text is generally CC BY-SA); Noto Sans fonts are SIL
OFL. See SKILL.md section 11.
