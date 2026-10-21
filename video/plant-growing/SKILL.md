---
name: "plant-growing"
description: "\"식물 키우기\" — plant-growth timelapse video production system: locked-environment stage-frame prompt series (seed→sprout→flower→fruit→ripe) → Gemini Omni 1.1 Flash first/last-frame interpolation, or a 10-second quick mode (one start frame → one I2V clip) → pretty-handwriting keyword overlays + rolling life-tip text targeting mass middle-aged & elderly audiences → 3–6 key stills → seed/fertilizer affiliate-link monetization. Paste-ready species packs: strawberry, cucumber, tomato, pepper, basil, sunflower, mango."
---

# Plant Growing (식물 키우기) — Growth Timelapse Production

## Purpose

Produce a plant-growth timelapse video of a single potted plant, from seed to
harvest, that stays visually locked — same pot, soil, background, light and
camera in every frame — while only the plant changes. The format is built for
mass middle-aged & elderly audiences: satisfying growth footage, large
handwritten keyword overlays on key scenes, and a rolling line of everyday
life tips. Monetization is direct: seed / fertilizer product links matched to
the featured species.

The reference format this system was reverse-engineered from: an 8-second
1080×1920 clip covering 5 growth stages (~1.6s per stage) — terracotta pot,
dark soil, blurred green garden background, warm morning light from the upper
left, fixed macro camera at pot-rim level. A hand appears only in the first
frame (sowing the seed).

## Two production modes

| Mode | How | Use for |
|---|---|---|
| **Precision series** | 5–7 stage stills from the 4-block prompt system → Omni first/last-frame interpolation per segment | Main series, monetized flagship content |
| **Quick 10-second** | One start-frame image → one 10s I2V clip; chain the last frame for longer videos | Bulk testing, new-species trials, filler content |

**Two environment looks** (independent of mode):
- **A. Terracotta garden** — terracotta pot, garden bokeh, morning sun. Warm, narrative (strawberry default).
- **B. Transparent glass pot** — glass pot, black background, studio light. The roots growing through the glass are the show (quick-mode default).

## Workflow

1. **Species card first** — fix the environment lock (pot · soil · background · light · camera) and the stage list, plus **count accounting**: flower count = young-fruit count = ripe count, positions locked. See `references/species-cards.md`.
2. **Stage frames** — generate one still per stage with the 4-block prompt (environment lock + structure lock + stage + exclusion). QA each frame against the previous one at full resolution. See `references/stage-prompt-system.md`.
3. **I2V interpolation** — Gemini Omni 1.1 Flash `image_to_video` with stage frame N as start frame and N+1 as end frame; assemble the segments. Quick mode: `references/quickstart-prompts.md` and `references/species-packs.md`.
4. **Overlay & assembly** — handwritten keywords (one per stage, code overlay — never generated text), rolling life-tip text along the bottom, calm BGM, 3s end card pointing to the pinned comment. See `references/overlay-production.md`, `references/tips-bank.md`.
5. **Stills** — pick 3–6 key stage frames (thumbnail / carousel / product card versions).
6. **Publish & monetize** — seed/fertilizer links matched to the species (pinned comment first), with affiliate and AI-generation disclosure.

## Key rules

1. **The environment lock is verbatim for the whole series.** If the prompt text changes, the series restarts.
2. **Count accounting is law.** Flowers = young fruit = ripe fruit, in the same positions. A fruit that appears from nowhere is a failed frame.
3. **A hand appears only in frame 1 (sowing).** Every other frame: no hands, no people.
4. **Never generate text with the model.** Keywords, rolling text and captions are always post-production code overlays (generated text garbles).
5. **Rolling tips: no efficacy claims.** No disease treatment/prevention promises — general, well-known lifestyle information only.
6. **Handwriting copy comes in 3 layers** — stage keywords, fact-checked core keywords, fun lines — all prepared per species in `references/species-cards.md`. Core keywords must be verified facts about that plant; never invent numbers.

## Model notes — Gemini Omni 1.1 Flash (verified 2026-10-21)

- Google model, GA 2026-08-27 (`gemini-omni-1.1-flash`); the preview endpoint was deprecated 2026-09-30.
- `image_to_video` supports **first + last frame interpolation** — exactly this skill's stage-frame method.
- Clips 3–10s, 720p native (1080p/4K are upscales), 9:16 supported, native audio (replace or duck in assembly).
- Access: Google Flow / Gemini app / AI Studio / Gemini API. Quick mode also works with Veo, Seedance 2.5, Kling.

## Files

- `references/stage-prompt-system.md` — the 4-block master template + full strawberry worked example (7 stages)
- `references/quickstart-prompts.md` — quick-mode template + cucumber worked example (verbatim)
- `references/species-packs.md` — paste-ready packs: tomato, sunflower, mango, basil
- `references/species-cards.md` — per-species stages, count accounting, handwriting copy sets (stage / core / fun), product mapping, fact sources
- `references/overlay-production.md` — handwriting keywords, rolling text, assembly, stills, monetization flow
- `references/tips-bank.md` — rolling-text sentence pool (gardening / life tips / wellness) with guardrails

Working language: prompts are English (paste-ready); audience-facing copy sets
(handwriting keywords, rolling tips) are Korean, targeting Korean
middle-aged/elderly viewers — translate the copy sets, not the prompts, to
retarget another market.
