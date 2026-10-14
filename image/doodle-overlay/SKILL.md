---
name: "doodle-overlay"
description: "Turn a photorealistic photo into mixed-media editorial art: a giant white hand-drawn doodle character (cat, cute kid, animal, cartoon figure) playfully interacting with the real scene. Use for the 'reality reimagined by a doodle' look — '고양이 손그림' summons the cat, '귀여운 아이 손그림' summons a cute kid figure. The photo stays faithful, the white doodle carries the story."
---

# Doodle Overlay

Turns a user-supplied photo into a paste-ready mixed-media prompt:
**photography × white hand-drawn doodle character**. The real photo stays
faithful and recognizable; ONE oversized white line-art character is drawn
on top, interacting with the actual architecture, landscape, or space in a
way that is clever, funny, and instantly readable.

Two subject modes share one pipeline:

- **Cat** (trigger: "고양이 손그림") — the cat plays mischief with real
  structures: hugging a tower, pawing at a reflection, napping on a roof.
  Cat scale: ~70% of the classic giant scale (user decision 2026-10-14:
  30% smaller than the reference default) — still surreal, slightly
  restrained. A short white handwritten phrase in the same white as the
  cat is allowed, plus restrained hearts / stars / exclamation marks.
- **Figure** (trigger: "귀여운 아이 손그림" / "손그림 인물") — a cute
  kid, animal, or cartoon figure that *reinterprets* real objects: a
  tower becomes a microphone or pencil, a roof becomes a hat, a bridge
  becomes guitar strings. Figure scale: clearly larger than life,
  typically larger than the buildings (no reduction). No text, no
  titles, no logos, no watermarks.

Reference samples (user-supplied): `examples/` — beach, Tokyo Tower,
mountain road, Golden Gate Bridge.

## Workflow

1. **Parse input.** Photo (required) + subject type (cat / figure;
   default to cat on "고양이 손그림", figure on "귀여운 아이 손그림")
   + optional interaction hint, caption hint (cat only). Ask only about
   genuinely ambiguous parameters.
2. **Analyze the photo.** Find the single smartest interaction for the
   chosen subject — not "a character next to the photo" but one that
   could only exist *in this photo*. Cat → mischief table; figure →
   object-reinterpretation table in `references/master-prompt.md`.
   Never repeat the same interaction across photos. One photo keeps
   ONE core visual idea.
3. **Compose.** Fill `references/master-prompt.md` with subject type,
   the chosen interaction, and optional caption (cat only).
4. **Output.**
   - Paste-ready prompt.
   - Short note: the chosen subject, the interaction, and why it fits
     this photo.

## Rules

- One photo, one character. Never combine photos, never draw multiple
  characters.
- Photo layer: keep the original faithful — subject, composition,
  perspective, light direction, atmosphere, photographic texture. No
  redesign, repaint, replace, or restage. Core subjects stay clearly
  recognizable.
- Doodle layer: simple white hand-drawn line art (marker / chalk / fine
  pen), line weight varies slightly, clear but never over-complex
  outlines. Minimal features on the face — gentle, curious, natural,
  humorous. NO realistic detail, NO refined manga, NO heavy or black
  outlines, NO 3D cartoon, NO sticker look, NO large solid fills.
- Accents: white is the absolute lead. At most one low-saturation
  yellow (mustard / warm / golden) for tiny focal points — scarf,
  yarn, balloon, food, ribbon, music notes, small stars, the prop the
  character plays with. Restrained, never dominant.
- Composition: use the photo's own structure — sky, lawn, wall,
  water, road, building edges, horizon. Never cover the most
  important architectural details. Character and real objects share
  accurate spatial, perspective, and action relationships.
- Mood: minimal, clean, humorous, designed, narrative, healing —
  editorial-illustration / international creative-ad quality.
  Clever, not merely cute.
