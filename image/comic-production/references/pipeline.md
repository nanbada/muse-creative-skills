# 6-Stage Pipeline (distilled)

Each stage names the source project(s) it distills. Keep the techniques;
the tools are interchangeable.

## Stage 1 — Lock (comic-maker, AI-Comic-Generator)

- One **locked look descriptor** per character: face, hair, outfit,
  age impression, identity marks. Verbatim, repeatable, immutable
  mid-project. This is the same pattern as a character bible.
- Optional: 3-view character sheet (front/side/back) as visual anchor;
  merge duplicate character extractions ("Butler Ma" vs "Old Ma").
- Global style config: one preset + palette + border + spacing.
- Per-character **seed family** for the renderer (same character →
  same seed family across panels). This plus the restated descriptor —
  not LoRA training — is what keeps characters recognizable.

## Stage 2 — Story (AI-Comic-Generator, ComicStudio)

- Idea → beats → panel breakdown, stored as JSON
  (`panel-contract.md`).
- Panel fields: scene, action, emotion, characters, props, dialogue,
  SFX, layout size.
- Dialogue: short lines that advance the story; silent panels stay
  silent. Emotion per panel drives later layout choices.

## Stage 3 — Validate (ComicStudio)

- Art-director pass over the JSON before any image is rendered:
  panel order, character continuity, actions feasible, required props
  present, dialogue consistent.
- Fix the JSON. Rendering is expensive; validation is cheap.

## Stage 4 — Render (StoryDiffusion, comic-maker, ComicStudio)

- Generate all panels in **one consistent batch/session** — the
  consistent self-attention effect: characters hold across 5–6+ panels
  when generated together, drift when generated in isolation.
- Every panel prompt = style block + locked look (verbatim) + panel
  specifics. Key phrases weighted; never silently truncate long
  prompts (Compel-style weighting).
- Manga path: render B&W line art first, then colorize from a color
  reference (MangaNinja) — line art and color stay independently
  stable.

## Stage 5 — QA (ComicStudio, ComicCrafter AI)

- Vision-check each rendered panel against its JSON row: subject
  present, action depicted, props visible, continuity with previous
  panel, no garbled baked-in text.
- **Targeted retry**: regenerate failed panels only, max 3 attempts.
  Dialogue-only fixes never re-render the image.
- Persistent session memory: keep story context across edits so a
  panel fix doesn't break continuity elsewhere.

## Stage 6 — Letter (comic-maker, ComicStudio)

- Speech bubbles, SFX, titles, and page composition happen AFTER
  rendering: wrapped bubbles with tails, character-aware placement
  (not top-center anchoring), diagonal gutters, title strip.
- Export: PNG pages, PDF, or CBZ.

## Source map

| Technique | Source |
|---|---|
| LLM story + SDXL render split, pluggable engines | ai-comic-factory |
| JSON-driven workflow, global config, 3-view sheets, context-aware panels | AI-Comic-Generator |
| Consistent self-attention batch rendering | StoryDiffusion |
| Session memory, targeted panel edits, stable style presets, emotion-aware layouts | ComicCrafter AI |
| Locked look + seed family, post-render lettering, no nameable words in styles, CBZ | comic-maker |
| LangGraph pipeline, validator + vision QA + ≤3 retries, Compel weighting, bubbles post-render | ComicStudio |
| Reference-based line-art colorization, point color guidance | MangaNinja |
