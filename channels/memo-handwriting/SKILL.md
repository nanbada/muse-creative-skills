---
name: "memo_handwriting"
description: "Wadded-paper handwritten message composites for Instagram: crumpled notepad paper + handwritten Japanese message over a background photo (9:16/4:5). Use when making scroll-stopper hooks, reel covers, or carousel covers in the anti-AI handwritten trend style."
---

# Memo Handwriting — Wadded Paper Message Tool

## Purpose
Generate "gu-shattered memo" (구겨진 메모장) hook images: a crumpled lined-note paper
with a handwritten Japanese message, composited over a background photo.
Based on Your Social Team's "Wadded Paper Message Reel" (Oct 2026 trend):
a wadded paper unfolds to reveal a handwritten note ("stop scrolling and …")
over fast-moving aesthetic photos. Why it works: handwriting feels human,
the paper is a tiny reveal, and it doesn't look like a design — a scroll-stopper
about stopping your scroll, riding the anti-AI-handwritten wave.

## Tooling
`bin/memo_make.py` — PIL composite generator (no API, no cost).

```bash
# lines separated by "|"; ink: blue|red|black|pink
python3 bin/memo_make.py --bg photo.jpg --text "スクロール|ストップして" --out out.png
python3 bin/memo_make.py --bg photo.jpg --text "見て！" --ink pink --ratio 4:5 --out out.png
# --tilt (paper angle, default -5 + jitter), --seed (reproducible layout)
```

- Output: 1080×1920 (9:16, reel/cover) or 1080×1350 (4:5, carousel).
- Paper asset: `assets/crumpled-note.png` (true transparency, cleaned).
- Font: `assets/fonts/Yomogi-Regular.ttf` (Google Fonts, OFL — handwritten Japanese).

## Cute-voice message patterns (20s, かわいい voice)
- Hook: 「スクロール|ストップして」「ちょっと|待って！」「見てほしいの」
- Confession/cute: 「今日の|ひとこと」「あのね、|聞いて」
- CTA: 「保存してね」「コメントで|教えて？」
- Keep it to 1–3 short lines; the caption carries the rest (jp-sns-ops style).

## Channel role (example: virtual-character channel)

- This is the channel's standard hook layer: reel **start frames** (first
  1–2s) and carousel covers. Custom covers cannot be set via web posting,
  so the memo image is baked into the reel as its start frame.
- Language split: in-image handwriting stays Japanese (visual aesthetic,
  matches the doodle-overlay line). Captions are English per the
  2026-10-20 channel language rule — handwriting and caption are separate
  layers, so the jp-sns-ops voice below governs ONLY the handwritten text.
- Utility boundary: stills and frame sequences only; character motion
  still comes from the video pipeline. Do not use for in-scene dialogue.

## Operating Rules
1. Message text follows the jp-sns-ops caption voice (colloquial, かわいい), never stiff ですます-only.
2. Ink colors that read as "real pen": blue, red, black. Pink for extra かわいい.
3. Background: aesthetic photo or character shot; paper must stay readable (avoid busy centers).
4. Stills are v1. For the full reel motion (paper unfolding over moving photos),
   build the video in Canva from these stills or generate a frame sequence with
   this script (vary --tilt/--seed per frame) and encode with ffmpeg.
5. Asset licenses: Yomogi font is OFL (free). The paper PNG is from a free
   non-commercial clipart source — fine for this account's organic posts;
   replace before any paid/commercial use.
