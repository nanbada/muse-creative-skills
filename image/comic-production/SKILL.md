---
name: "comic-production"
description: "Produce consistent multi-panel AI comics (manga, webtoon, strips): a 6-stage pipeline distilling 7 open-source comic projects — locked character descriptors, batch-consistent panel rendering, validator + vision-QA gates with targeted retries, post-render lettering. Use when the user wants 만화 제작 — turning a story into panels with stable characters. Korean trigger: 만화 제작."
---

# Comic Production

Turns a story idea into a consistent multi-panel comic. The pipeline is
distilled from 7 open-source projects (ai-comic-factory, AI-Comic-Generator,
StoryDiffusion, ComicCrafter AI, comic-maker, ComicStudio, MangaNinja) —
keeping their proven techniques, dropping their infrastructure.

Core insight across all 7: **consistency comes from the pipeline, not the
model.** Locked descriptors + batch rendering + validation gates beat any
single "better" generator.

## Workflow (6 stages)

1. **Lock.** Character sheet first: one locked look descriptor per
   character (face, hair, outfit, age impression — verbatim, repeatable)
   + a global style config (one preset from
   `references/style-presets.md`, palette, border style, panel spacing).
   Never start panels without the lock. (comic-maker, AI-Comic-Generator)
2. **Story.** Beats → panel breakdown as JSON: panel id, scene, action,
   emotion, characters present, dialogue, SFX. Dialogue stays short;
   silent panels stay silent. (AI-Comic-Generator, ComicStudio)
3. **Validate.** Storyboard validator before any render: panel order,
   character continuity, required props present, dialogue consistent.
   Fix the JSON, not the images. (ComicStudio)
4. **Render.** Generate panels in ONE consistent batch/session — never
   isolated one-offs. Every panel prompt restates the locked look
   verbatim + global style; use a per-character seed family. Long
   prompts: weight key phrases, never silently truncate.
   (StoryDiffusion, comic-maker, ComicStudio)
5. **QA.** Vision-check each panel: missing subject/prop/action,
   continuity break, dialogue mismatch. Targeted retry on failed panels
   only (max 3); dialogue-only fixes never re-render images.
   (ComicStudio, ComicCrafter AI)
6. **Letter.** Speech bubbles, SFX, and titles are added AFTER
   rendering — character-aware placement, never baked into generation.
   Export PNG / PDF / CBZ. (comic-maker, ComicStudio)

Manga path: draw black-and-white line art first, then colorize from a
color reference (MangaNinja) — separating line art from color keeps both
stable.

## Rules

- Character descriptors are immutable mid-project. New outfit or new
  character = new locked descriptor, never a silent edit.
- One style preset per project. Style changes propagate to all panels
  or not at all.
- Never put nameable words in a style string ("sunday", "newspaper") —
  the model will paint them into the art. (comic-maker)
- Image models garble text: keep in-image dialogue to a few words or
  overlay it in post. Lettering is a post step, always.
- Emotion-aware layouts: panel size, borders, and color temperature
  follow the panel's emotion. (ComicCrafter AI)
- Panel edits are targeted: regenerate only the failed panel, keep the
  rest. (ComicCrafter AI, ComicStudio)
