---
name: museum-editorial
description: Generate paste-ready prompts for GPT Image 2.5 that produce museum-grade editorial posters — minimalist 9:16 vertical layouts with archival layers, in Korean or English. Verifies subject facts before composing so no invented dates, names, or specs end up as poster text.
---

# Museum Editorial

Turns a subject (artifact, classic car, artwork, craft object, …) into a
paste-ready image-generation prompt that yields a museum-exhibition-style
editorial poster: quiet, restrained, material-driven, knowledge-bearing.

Reference samples (user-supplied, Chinese versions): Ru ware celadon poster,
Mercedes-Benz 300 SL poster.

## Workflow

1. **Parse input.** Subject (required) + optional: output language
   (default 한국어, or English), format (default 9:16), reference photo.
   Ask only about genuinely ambiguous parameters.
2. **Verify facts.** Web-search the key facts that will appear as poster
   text: proper nouns, dates/eras, specifications, dimensions, collection or
   maker. Tag each V (official or 2+ independent sources), P (single /
   indirect source), U (unverifiable).
   - V/P facts may appear on the poster. **U facts are omitted from the
     poster entirely** — a poster cannot carry a "director's choice" note,
     so unverifiable claims simply don't get printed.
   - Never invent text to fill the layout. If facts are thin, the layout
     gets more whitespace, not more words.
3. **Compose.** Fill the master template (`templates/master-prompt.ko.md`
   or `.en.md`) with the subject and verified facts. The template lets the
   image model autonomously decide subject treatment, material, color,
   typography, archive elements, composition, and information hierarchy —
   do not pre-decide those in the prompt.
4. **Output.**
   - Paste-ready prompt in the chosen language.
   - Short fact note: which facts were verified (with sources), which were
     omitted as unverifiable.

## Rules

- Poster text is exactly three tiers: 대제목 (headline), 중형 설명
  (mid-size description), 소형 아카이브 정보 (small archival data).
  Nothing else. No slogans, no filler sentences, no meaningless text.
- Korean typography, two tracks:
  - **Model-native (default):** gpt-image-2-class models render Korean at
    ~95–99% accuracy (incl. CJK mixed with Latin). Maximize it with the
    verbatim technique baked into the template: wrap each text in quotes,
    demand verbatim rendering with no extra characters, and specify font
    weight, color, and position. Still not 100% — proofread the output.
  - **Deterministic (when text must be perfect):** generate the background
    with NO text (instruct "no text, leave empty space for typography"),
    then composite Korean type with PIL using a real Korean font
    (Noto Serif KR, 나눔명조, Pretendard). 100% accurate, full font
    control — the right choice for print or client-facing posters.
- Keep on-poster text short either way; long passages and tiny type break
  more often. If Korean glyphs keep breaking in model-native mode, switch
  to the English template or the deterministic track.
- The avoid-list in the template is binding: no busy layering, no
  decorative kitsch, no traditional-Chinese-style template look, no
  commercial-ad feel, no dead-center subject placement, no heavy antique
  processing, no CG-plastic feel.
- When the user supplies a reference photo of the subject, instruct the
  model to match the subject's real appearance (shape, glaze, patina);
  style follows the template, identity follows the photo.
- This skill writes prompts. It does not generate images itself and does
  not publish anything.
