---
name: "veo_vertical_clip"
description: "Design Veo 3.1 native 9:16 vertical clip prompts + credit-aware production plan for Google Flow. Use when the user asks to plan or generate short-form AI clips (Shorts/Reels), vertical Veo 3.1 prompts, or clip pipelines with Flow credits."
---

# Veo 3.1 Vertical Clip

## Purpose
Produce paste-ready Veo 3.1 prompts and a credit-aware production plan for vertical (9:16) AI clips via Google Flow — no crop/re-frame post-processing, zero-cost planning with Muse.

## Workflow
1. **Input**: topic, script, or persona (e.g., fixed character persona). If the user hasn't picked a fixed persona, ask before proceeding — consistency of the persona is the revenue lever (see `character-channel-ops` skill).
2. **Shot list**: design 8–9 clips of ~10s each (SNS Factory pipeline). Per clip: Korean scene note + English Veo prompt + framing note.
3. **Native 9:16 framing**: every prompt includes a vertical framing cue, e.g. `vertical portrait framing, subject centered`. Avoid wide landscapes or multi-person crowd scenes unless the subject hierarchy is explicit.
4. **Credit tiering** (user is on Google AI Pro as of 2026-10 — see `references/credit-notes.md` before committing numbers): 1,000 credits/month + 50/day free, no rollover.
   - Lite (10): drafts / rejected candidates — iterate freely.
   - Fast (20): main generation.
   - Quality (100): hero shots.
   - Monthly budget ≈ 100 Lite / 50 Fast / 10 Quality. 1080p upscale free for subscribers.
5. **Character consistency**: free-tier answer is image-to-video with a reference image, not text-only prompts (faces drift otherwise). Ingredients to Video on the free tier is unverified — verify in the Flow UI before promising it.
6. **Semi-auto contract**: Muse designs shot lists + prompts in parallel; the human clicks generate in Flow. There is no public generation API — never claim full automation.

## Output Contract
- Per-clip block: Korean scene note, English Veo prompt, framing note, credit tier assignment.
- Credit plan: clips × tier = total, within the 50/day budget (or split across days).
- If producing for the SNS pipeline: note the follow-on edit step (8–9 clips → one video).

## Prompt corpus reference (ai-video-prompts, 2026-10-06)
- 545 real viral AI-video prompts with source URLs: https://github.com/aicodedecode/awesome-muse-skills/tree/main/skills/ai-video-prompts (`data/videos.json` index, `prompts/<slug>.md` texts).
- For Veo 3.x direction: filter `model=gemini` + `tech_tags` contains `veo` (39 entries). For code-driven motion: `model=claude`/`chatgpt`.
- Adapt the technique, not the wording (a Veo prompt's shot language — "slow dolly-in, 35mm" — transfers across video models). Credit the creator via `post_url` when publishing derived work. `prompt_partial=true` entries are inspiration only, not recipes.

## Operating Rules
1. Never claim Muse runs Veo directly or automates Flow generation.
2. Never invent first-person experience of testing Veo 3.1 vertical generation — say what is verified vs. not.
3. Credit numbers carry a date stamp (2026-10). Tell the user to check the Flow credits page before spending.
4. Ingredients to Video on the free tier and max free-tier resolution are unverified — mark them as such until checked in the Flow UI.
5. Prompts in English, shot list and user-facing notes in Korean. Internal docs in English.
