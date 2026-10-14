---
name: "cat-doodle-overlay"
description: "Turn a photorealistic photo into mixed-media editorial art: a giant white hand-drawn line-art cat playfully interacting with the real scene (tower, bridge, water, roof, road). Use when the user wants the 'reality quietly invaded by an imaginative cat' look — the photo stays faithful, the white doodle carries the story."
---

# Cat Doodle Overlay

Turns a user-supplied photo into a paste-ready mixed-media prompt:
**photography × white hand-drawn cat doodle**. The real photo stays
faithful and recognizable; ONE oversized white line-art cat is drawn on
top, interacting with the actual architecture, landscape, or space in a
way that is clever, funny, and instantly readable — hugging a tower,
pawing at a reflection, napping on a roof, peeking from a window.

User modifications baked in (2026-10-14):
- Cat at **~70% of the classic giant scale** (30% smaller than the
  reference default) — still surreal, slightly restrained.
- A short **white handwritten phrase** in the same white as the cat is
  allowed, plus restrained hearts / stars / exclamation marks.

Reference samples (user-supplied): `examples/` — beach, Tokyo Tower,
mountain road, Golden Gate Bridge.

## Workflow

1. **Parse input.** Photo (required) + optional: interaction hint,
   caption hint. Ask only about genuinely ambiguous parameters.
2. **Analyze the photo.** Find the single smartest interaction the cat
   can have with the real scene — not "a cat next to the photo" but a
   cat that could only exist *in this photo*. Ask: which real object,
   structure, or space invites touch, play, or mischief? Consult the
   interaction table in `references/master-prompt.md`; never repeat the
   same interaction across photos.
3. **Compose.** Fill `references/master-prompt.md` with the chosen
   interaction and optional caption. Cat scale: clearly larger than
   life, ~70% of the full giant default. Caption: one tiny casual
   handwritten white phrase (or omit).
4. **Output.**
   - Paste-ready prompt.
   - Short note: the chosen interaction and why it fits this photo.

## Rules

- One photo, one cat. Never combine photos, never draw multiple cats.
- Photo layer: keep the original faithful — subject, composition,
  perspective, light direction, atmosphere, photographic texture. No
  redesign, repaint, replace, or restage. Core subjects stay clearly
  recognizable.
- Cat layer: simple white hand-drawn line art (marker / chalk / fine
  pen), line weight varies slightly, clear but never over-complex
  outlines. Minimal features on the face — gentle, curious, dopey,
  mischievous. NO realistic fur, NO refined manga, NO heavy outlines,
  NO 3D cartoon, NO sticker look, NO large solid fills.
- Accents: white is the absolute lead. At most one low-saturation
  yellow (mustard / warm / golden) for tiny focal points — small
  stars, hearts, flowers, sparkles, the toy the cat plays with.
  Restrained, never dominant.
- Text: at most ONE short handwritten phrase in the same white as the
  cat, tiny and casual. No titles, no logos, no watermarks.
- Composition: use the photo's own structure — sky, lawn, wall,
  water, road, building edges, horizon. Never cover the most
  important architectural details. Cat and real objects share
  accurate spatial, perspective, and action relationships.
- Mood: minimal, clean, humorous, designed, narrative, healing —
  editorial-illustration quality. Clever, not merely cute.
