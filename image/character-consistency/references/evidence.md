# Evidence summary — character-consistency method (generic)

Numbers only, no reference photos. Full dated logs live outside this
repo with the working project.

## 2026-10-30 — Restart validation (test faces)

- Sheets (face anchor + frontal upper sheet + faceless full-body
  back sheet, separate images) held face across café, neon, park,
  and trench scenes with varied outfits and angles.
- Body standard (faceless mannequin, hourglass form): 7.4 heads,
  legs 56.8% of total height.
- Studio composite (face refs + mannequin, neutral outfit):
  6.8 → head-shrink 7.1 → head-shrink repeat 7.6 heads (target
  7.5–8 reached). Face-presence pull-down confirmed: mannequin 7.4
  → with-face 6.8 before the ladder.
- Scene transfer from the 7.6 composite, auto-ladder per scene:
  café pass (face, seated); neon 6.7 → head-shrink applied, pixel
  measure void (wind-blown ponytail merged into head bbox) →
  user-eye verdict ~8 heads accepted (final gate); park 7.7 pass
  (legs unmeasurable under long dress — reported as unmeasurable,
  not failure); trench 6.9 → 7.46 → 7.9 pass (two auto corrections,
  no manual prompts).
- Transfer comparison: old studio 7.35 → scene mean 6.6; new studio
  7.6 → scenes 7.7–7.9 (measured) plus café/neon passes.

## Standing failure modes (do not re-promise)

- Numeric head-count wording in a scene prompt does not move the
  generator's default (~6 heads).
- A one-image 3-cut sheet inflates full-body scale via the
  close-up face panel.
- Start-frame anchor alone does not hold identity through motion
  (verified on two engines; still-frame QA passing does not
  certify motion identity).
- Long coats/dresses occlude the hip line: legs% under them is
  invalid as an anatomical measure.
- Wind-blown tied-back hair merges into the head bbox: pixel
  head-count void, user eye governs.
- Tool-level integrity refusals for specific requests stand;
  never retry with changed arguments.
