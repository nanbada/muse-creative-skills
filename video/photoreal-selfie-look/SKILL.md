---
name: "photoreal-selfie-look"
description: "Inject a photorealistic smartphone front-camera look into AI video prompts: beauty filter, grain, motion blur, focus breathing, rolling shutter, SNS compression artifacts. Use when a prompt needs the 'TikTok influencer selfie' aesthetic instead of clean cinematic output."
---

# Photoreal Selfie Look

## Purpose
Turn any vertical selfie-style video prompt into a believable "shot on a smartphone front camera" look: softened skin from a beauty filter, fine random grain in midtones/shadows, motion blur and focus loss during fast moves, rolling-shutter skew, subtle exposure/white-balance drift, light noise-reduction smear, and block noise from platform compression. The look must never be studio-clean, HDR-heavy, or steadicam-smooth.

## Workflow
1. **Character lock**: confirm the subject anchor (face, hair, outfit, accessories) is fixed across the whole piece — this skill does not fix identity, it only fixes the look.
2. **Assemble the look block**: paste the English look block from `references/look-block.md` verbatim at the end of the video prompt.
3. **Motion sync**: if the scene has fast phone moves (pick up, put down, sudden approach), keep the "motion blur + momentary defocus on fast moves" clause — that is what sells the handheld illusion.
4. **Ban list**: always append the ban list (no text, no subtitles, no logos, no watermarks, never fully sharp, no HDR, no studio post-processing, no steadicam, no excessive shake).
5. **Resolution**: default 720p for credit saving unless the user explicitly wants 1080p.

## Output Contract
- The look block is in English, appended after the scene description in the video prompt.
- The ban list is appended after the look block.
- Output notes to the user stay in Korean.

## Operating Rules
1. This skill is look-only. It does not design shots, write dialogue, or choose music — pair it with `veo-vertical-clip` for full clip production.
2. Never claim the look guarantees a real-phone result; say what is verified in the generation tool vs. not.
3. Do not apply the photoreal look to a watercolor character anchor without the user's explicit decision — the two art directions are separate tracks.
4. Keep `SKILL.md` lean; the full English blocks live in `references/look-block.md`.
