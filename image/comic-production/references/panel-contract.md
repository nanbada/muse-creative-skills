# Panel Contract (JSON) + Prompt Template

The JSON is the contract between stages. Stages 2–5 all read and write
it; humans edit the JSON, never the images directly.

## Storyboard JSON

```json
{
  "project": "title",
  "style_preset": "manga",
  "palette": ["#1a1a1a", "#f5f0e8"],
  "characters": {
    "rina": {
      "locked_look": "21-year-old Japanese woman, elegant oval face, almond dark-brown eyes, long dark-brown hair with side part, tiny mole beside right mouth corner, cream knit top"
    }
  },
  "panels": [
    {
      "id": "p01",
      "scene": "morning kitchen, warm window light",
      "action": "rina pours coffee, smiling softly",
      "emotion": "calm",
      "characters": ["rina"],
      "props": ["mug", "kettle"],
      "dialogue": "morning already?",
      "sfx": null,
      "layout": "medium"
    }
  ]
}
```

## Panel render prompt (fill per panel)

```
[STYLE PRESET BLOCK — verbatim from references/style-presets.md]
Character lock (restate verbatim, every panel):
- rina: 21-year-old Japanese woman, elegant oval face, almond
  dark-brown eyes, long dark-brown hair with side part, tiny mole
  beside right mouth corner, cream knit top
Panel p01 — morning kitchen, warm window light.
Action: rina pours coffee, smiling softly. Emotion: calm.
Props in frame: mug, kettle.
Composition: single character medium shot, clean panel border,
no text in image, no speech bubbles.
```

Key phrases carry the weight: character lock > action > emotion >
props > scene. If the prompt must be shortened, cut from the end.

## Validator checklist (Stage 3, before render)

- Panel order follows the beats; no beat skipped or duplicated.
- Every character in a panel has a locked descriptor.
- Required props listed; no prop appears before introduction.
- Dialogue lines are short; silent panels have null dialogue.
- No nameable words in the style block.

## Vision QA checklist (Stage 5, after render)

- Subject present and recognizable (locked look intact)?
- Action depicted? Required props visible?
- Continuity with previous panel (outfit, setting, time of day)?
- No garbled text baked into the art?
- Fail → targeted retry of that panel only (max 3), then escalate.
