---
name: "phone-shot-video"
description: "Make AI videos feel shot on a real smartphone: 1st-person selfie lock, intentional imperfections (shake, autofocus hunting, exposure drift), diegetic sound only, GRWM 30s beat structure. Korean trigger word: 휴대폰으로 찍은 영상 — when the user says 휴대폰으로 찍은 영상, apply this skill to produce smartphone-shot-feel videos."
---

# Phone-Shot Video

## Purpose

Same "break down, not dress up" philosophy as `photoreal-realness`, for
video: believability through deliberate imperfection. For GRWM/vlog-style
videos that must feel like a real person filmed herself on her phone.

Method: @_creatorzz_ "intentional imperfection" (X, 2026-10-07); canonical sample analysis bundled with this skill's references.
Detailed skill record: video planning app skill #9 (Smartphone GRWM Vlog),
skill #3 (selfie-intro, music-driven variant).

## When to use

- The user says 휴대폰으로 찍은 영상, or asks for smartphone-shot-feel
  video (vlog, GRWM, selfie-style).
- Pair with the app's skill #9 for full planning; this skill is the trigger
  plus the core blocks.
- Do NOT use to make an AI persona pass as a real human for deceptive
  purposes (fake reviews, undisclosed identity). Any AI persona keeps its AI-generated label per each platform's policy.

## Workflow

1. **Identity lock first**: your character's identity lock, or an attached reference + the
   identity block from `references/grwm-video-blocks.md`. Never change
   identity for believability.
2. **Pick the beat structure**: GRWM 30s beats
   (`references/grwm-video-blocks.md`), or adapt beats to the brief.
3. **Append the camera/visual + audio specs** in English after the
   scene/character description.
4. **Dialogue in the target language** (e.g. Japanese for a Japanese persona): fully localized,
   never mixed.
5. **QC against the imperfection checklist**; reshoot only if a take looks
   "too perfect."

## Output Contract

- Technique blocks in English, appended after the scene/character
  description.
- Notes and explanations to the user stay in Korean.

## Operating Rules

1. This skill covers the smartphone-shoot technique only; pair with
   prompt/production skills for planning, series, and assembly.
2. Real-shoot variant: the same beats double as a shot list for actual
   smartphone filming.
3. Keep `SKILL.md` lean; the full blocks live in
   `references/grwm-video-blocks.md`.
4. Never claim the technique guarantees indistinguishable-from-real output;
   report what the generation actually produced.
