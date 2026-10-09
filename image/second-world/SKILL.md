---
name: second-world
description: Generate paste-ready prompts that turn a photo into a "Second World" poster — vertical 3:4 canvas, upper half faithful photography, lower half ivory paper where one structure from the photo continues and changes physical rules, with tiny black line figures and a short handwritten caption.
---

# Second World

Turns a user-supplied photo into a paste-ready image-generation prompt that
produces an independent-magazine-style "Second World" poster: the top half
stays photographic, the bottom half becomes ivory paper where one structure
from the photo (road, water, branch, rope, light, …) crosses the center split
and continues under new physical rules — touched, pulled, drawn, or entered
by 0–3 tiny black line figures, plus one short handwritten English caption.

Reference samples (user-supplied): `examples/01-spring-break.png` (blossom
branch → petal swing), `examples/02-whats-under-here.png` (canal water →
peeled paper), `examples/03-just-a-little-tug.png` (ship rope → tugged rope),
`examples/04-a-little-more-road.png` (desert road → pencil-drawn line).

## Workflow

1. **Parse input.** Photo (required) + optional: caption hint, edge
   preference. Ask only about genuinely ambiguous parameters.
2. **Analyze the photo.** Identify ONE source structure that naturally
   reaches the center split — road, shoreline, water, reflection, branch,
   light, architecture, or body movement. This structure must cross the
   boundary and continue into the lower half. Decide the single
   image-specific interaction by asking: if this structure became touchable,
   usable, enterable, or changeable, what would it naturally become?
   Consult `references/pattern-catalog.md` for the interaction families
   distilled from 22 reference posters — pick the fitting family, then
   invent an image-specific variation. Do not mechanically repeat actions
   across posters.
3. **Compose.** Fill the master template (`templates/master-prompt.md`)
   with the chosen structure, interaction, figure plan (0–3, only when they
   physically interact with the continued structure), and caption. The
   caption is one short handwritten English line based on the action —
   natural, light, slightly witty; no inspirational quotes, no fixed
   "Same…, different…" phrasing.
4. **Output.**
   - Paste-ready prompt.
   - Short note: the chosen continuity structure, the interaction logic,
     and why no figures were added (if none).

## Rules

- One independent poster per photo. Never combine photos.
- Upper half: keep the photo faithful — subject, pose, spatial
  relationships, color atmosphere, natural light. Only proportional
  cropping allowed. No redesign, repaint, replace, or restage.
- Center split: two strictly equal horizontal halves (top 50% / bottom
  50%). Continuity across the seam is the highest priority. An irregular
  torn-paper edge is allowed but must follow the source structure, never
  act as decoration — and never the same tear shape twice.
- Lower half: ivory paper with subtle fibers, abundant negative space.
  Continue the structure from the exact meeting point, reinterpreted with
  restrained photo fragments, cut-paper forms, and minimal black
  hand-drawn lines. It must stay visibly attached — never an isolated
  portal, window, stage, platform, or floating vignette.
- Figures: 0–3 tiny black line figures, only when useful, and only when
  they physically interact with the continued structure. If the source
  already has strong human action, add none. Never decorative.
- Style: real photography above, warm paper below, minimal black line
  doodle, subtle handmade collage texture, bright, airy, restrained. It
  should feel as if the second world was already hidden inside the photo
  and simply continued downward.
- Negative: no detached lower-half illustration, no generic torn-paper
  template, no isolated portal, no unrelated vignette, no broken
  continuity, no dense illustration, no random decoration, no crowd, no
  altered photo colors, no redesign of the upper image, no glossy 3D, no
  scrapbook clutter, no gibberish text, no watermark, no logo, no UI.
