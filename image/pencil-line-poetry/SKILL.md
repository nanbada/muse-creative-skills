# Delicate Pencil Line Poetry (동양미 스타일)

Generates paste-ready prompts in a line-art mixed-media style grounded
in 32 real reference posts (analyzed 2026-10-17 — see
`examples/sample-01..32.jpg`): **tiny line-drawn characters living
inside an oversized, photorealistic natural world**. Fine lines carry
the character; real flowers, dew, feathers, and light carry the world.
Quiet, poetic, healing — a tiny person in a vast gentle world with an
East Asian aesthetic.

IMPORTANT — what the references actually show (the earlier
"monochrome pencil sketch" description was wrong; this skill was
rewritten from the samples):
- The dominant pattern is NOT pure pencil realism. It is mixed media:
  delicate line characters + photorealistic macro nature.
- Characters are small with minimal dot-eyes faces, thread-like hair,
  stick-thin limbs — never detailed anime beauties.
- Nature is the giant: oversized flowers, leaves, dewdrops, feathers
  become the character's architecture (scale play with NATURE, not
  buildings).
- Light is warm: golden-hour backlight, sun flare, glowing edges; or
  glowing gold/red lines on dark backgrounds.

Distinct from siblings:
- `local-doodle-overlay` → giant white doodle character ON TOP of a
  faithful photo.
- `local-photo-memo-annotation` → white annotation memos on a photo.
- **This skill** → generation-first artwork: line character + real
  nature fused into one poetic scene.

## Trigger words (Korean)

- "동양미 스타일" / "연필선 스타일" / "라인 시학"
- "작은 선 캐릭터" / "선 그림 동화"

## Modes (observed from the 32 samples — pick ONE)

- **A. Tiny line world** (dominant, ~samples 1,3,4,5,9,11,12,16,
  19,22,23,25,27,30):
  a tiny line-drawn girl (dot eyes, minimal features, simple dress,
  sometimes a small dog) inside an oversized photorealistic nature
  macro world — dewdrops like crystal balls, giant cosmos petals as
  staircases, a ginkgo leaf as a boat, a snowdrop flower towering
  overhead, a feather as a raft. Paper-cut / thread-embroidery
  textures allowed on hair and clothes.
- **B. Glow lines** (~samples 2,6,10,15): luminous line art —
  golden-white lines in a sunlit field with butterflies and flower
  glow, or red glowing lines on black (umbrella in red rain, profile
  portrait with light-ribbon hair). Light-painting feel.
- **C. Line over landscape** (~samples 12,17,18,21,24): a translucent,
  delicately-lined woman standing in a photorealistic landscape —
  lake at dusk, sunset cosmos field, flower hill. Fine pencil lines,
  dress and hair dissolving into light.
- **D. Soft painterly** (~samples 7,14,20,26,28,29,31,32): semi-realistic soft painting,
  hazy morning light, gentle anime illustration. Use when the user
  wants the calmest, most realistic variant.
- **E. Photo minimalism** (~sample 8): pure photography — light and
  shadow on Korean architecture (e.g. bird shadows on a hanok lattice
  door). No character. Only on explicit request.

## Workflow

1. **Parse input.** Scene/character idea (required) + mode
   (default: A) + medium (image / video). Ask only about genuinely
   ambiguous parameters.
2. **Compose.** Fill `references/master-prompt.md`. Keep the
   character tiny relative to the nature world (mode A), keep ONE
   emotional moment, keep vertical composition with generous
   negative space.
3. **Output.**
   - Paste-ready prompt.
   - Short note: mode chosen, key slots filled, and why they fit.

## Rules

- One scene, one emotion. Never crowd the frame; negative space is
  composition.
- Character design (modes A–C): minimal — dot eyes or closed eyes,
  small gentle smile, simple dress, thread-like hair. No detailed
  faces, no exaggerated anime features.
- Scale play: the character is small, nature is giant. Dewdrops,
  petals, leaves, feathers, flower stamens become landscape.
- Light: warm golden-hour backlight, sun flare, glowing edges
  (daylight modes); glowing gold/red lines on near-black (mode B
  dark variant).
- Palette: warm pastels — peach, cream, soft pink, gold, pale
  green; watercolor washes; translucent layered petals.
- Video: subtle motion only — petals drift, dew glistens, hair
  stirs, light flickers, butterflies hover. 6–15 s quiet loops.
- Reference index: `examples/sample-01..32.jpg` with per-sample
  notes in `references/sample-notes.md`.
