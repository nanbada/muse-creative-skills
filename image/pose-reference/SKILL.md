---
name: pose-reference
description: Pick a pose for character image generation from 8 anatomy reference sheets (133 poses). Select by situation/mood or at random, verify visually, and emit an English pose descriptor plus optional visual reference for the image prompt.
---

# Pose Reference

Applies poses from the user's 7 uploaded pose sheets to future character
image generation — situation-matched or random. The sheets are anatomical
drawing references (mannequins, non-sexualized); they are used strictly as
posing guides for clothed, tasteful character art.

## Library

- `assets/pose-sheet-01.jpg` … `assets/pose-sheet-08.jpg` — the 8 sheets
  (08 = bold-style variants, added 2026-10-03).
- `references/pose-index.md` — all 133 poses with short English descriptors
  (`S<sheet>-<num>`), plus pose-family quick-pick lists.

Read the index for finding; read the sheet image for confirming. The
descriptor is a finding aid — always open the sheet with `muse.read` and
look at the numbered pose before committing to it.

## Workflow

1. **Read the brief.** Extract: character, outfit, setting, mood, framing
   (full-body / half / seated), and any pose constraint ("standing",
   "walking", "seated at a cafe").
2. **Choose the mode.**
   - *Situation-matched (default):* map mood + framing to a pose family from
     the index (e.g. fashion lookbook → standing-elegant / walking;
     cozy cafe → sitting-ground / reclining-lying; energetic reel cover →
     dance-dynamic), then pick the best-fit pose number.
   - *Random:* only when the user asks for random/surprise. Use
     `shuf` over the eligible family (respect framing constraints —
     never pick a lying pose for a "standing full-body" brief). Check
     `usage-log.md`; skip the last ~10 used poses so repeats don't cluster.
3. **Visually confirm.** Open the sheet image via `muse.read`, find the
   number, confirm the pose reads correctly at a glance.
4. **Emit the pose package:**
   - Pose ID (e.g. `S2-05`) — for the log and for user reference.
   - English pose descriptor (from the index, lightly adapted to the
     character/outfit — never describe nudity; describe the *pose*).
   - Optional: attach the sheet image (or a crop of the single pose) as a
     visual reference alongside the text prompt when the image pipeline
     accepts reference images.
5. **Log it.** Append `date | brief | pose ID` to `usage-log.md`
   (create it if missing).

## Prompt phrasing

- Pose descriptors go in English, as a separate sentence in the image
  prompt: e.g. "Pose: standing contrapposto, one hand on hip, weight shifted
  to one leg."
- Keep character-consistency tokens first (character name, style, outfit),
  then setting, then pose, then mood/lighting.
- If the brief names a real person or a fixed character (e.g. a fixed character), the
  pose must not contradict established character traits.

## Rules

- Poses are anatomical references only. Generated characters are always
  clothed and the framing stays tasteful — no sexualized poses, angles,
  or descriptions, regardless of what the reference sheet shows.
- Never invent a pose number. If the index has no fit, say so and describe
  the needed pose in words instead of forcing a wrong ID.
- Random mode still respects the brief's hard constraints (framing,
  setting, outfit logic).
- Pairs with character-channel operation skills for channel art: pose variety
  across posts matters — consult the usage log before repeats.
