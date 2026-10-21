---
name: "photoreal-realness"
description: "Add 'this person could really exist' realism to photorealistic AI image prompts: four-stage degradation blocks that kill the over-polished AI-beauty look, so a photo reads as a real smartphone snap. Korean trigger: 휴대폰샷. Not for video (use phone-shot-video)."
---

# Photoreal Realness

## Purpose

Stop the scroll with believability, not perfection. Over-beautified AI faces get scrolled past; faces that read as "this person could really exist" stop thumbs. This skill injects intentional imperfection into photorealistic image prompts instead of adding more polish.

Method: こけぞう (@gaget12090105) "崩す (break down), not 盛る (dress up)" — X, 2026-10-07. Community know-how; attribute as such when cited publicly.

## When to use

- A photoreal AI photo must read as a real person on SNS (character channels, AI influencer content, lifestyle shots).
- Pair with `photoreal-selfie-look` when the output is front-camera video: this skill covers still-image realism logic (asymmetry, skin, candid framing); the selfie skill covers motion/look.
- Do NOT use to make an AI persona pass as a real human for deceptive purposes (fake reviews, fake testimonials, undisclosed identity). Keep AI-persona disclosure labels on per each platform's policy.

## Workflow

1. **Character lock first**: fix the identity anchor (face, hair, outfit) before realism — this skill never changes identity, only believability.
2. **Start with the quick trio** (blocks 1a + 4a + 4e, the post's recommended minimum): append in English after the scene/character description. For keyword-style or terse prompts, use the smartphone-snap one-liner from `references/realness-blocks.md` instead. For an analog-film camera class, use the 35mm film one-liner (user keyword: 아날로그 35mm 필름) — never stack both one-liners.
3. **Escalate by feel**: image too clean → add Step 2 blocks; face too "AI" → add Step 3; skin/hair uncanny → add Step 4. Never paste all 20 — more blocks ≠ more real.
4. **Append the negative list** after the realism blocks.
5. **Keep output class realistic**: smartphone-tier rendering; never promise flagship-sharp "shot on DSLR" output when the goal is a candid snap.

## Output Contract

- Realism blocks in English, appended after the scene/character description, negative list last.
- Notes and explanations to the user stay in Korean.

## Operating Rules

1. Realism blocks only — this skill does not design shots, write captions, or build stories; pair with prompt/production skills for those.
2. Do not apply to a watercolor art direction without the user's explicit decision (separate tracks, same as `photoreal-selfie-look`).
3. Keep `SKILL.md` lean; the full English blocks live in `references/realness-blocks.md`.
4. Hands are the highest-ROI fix: block 4b (anatomy + realistic phone grip) is the single biggest "not-AI" signal.
5. Never claim the blocks guarantee a real-photo result; report what the generation tool actually produced.
