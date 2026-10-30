---
name: "character-consistency"
description: "Keep one person's face, hair, and body consistent across AI image and video generation: face-photo anchor + fixed-block verbatim + role-labeled references + separate face/full sheets + faceless mannequin body standard + relative-edit ladder with auto-repeat + pixel measurement. First resort for any person generation. Includes a beginner start-up section: input checklist + user-interview format. Not pose selection — for poses, use pose-reference."
---

# Character Consistency — Person Method

Keep the SAME person across generated images and video: same face,
same hair, same body. The method is anchor-first, measurement-gated,
and correction-laddered. It is the first resort for any person
generation — apply it before other approaches.

Beginners: start at §0 — it lists every input and gives the
interview script. Do not skip it.

## 0. Start here — inputs + interview (beginner template)

Do NOT generate anything until the inputs below are confirmed.
Muse interviews the user first; the user can answer "defaults" at
any point to accept all remaining defaults.

### What Muse needs (checklist)

1. Face photo (anchor) — REQUIRED for face consistency. One
   clear photo: face visible, good light, no sunglasses or mask,
   hair visible. Use only a photo you own or have the right to
   use; never copy a real person's identity without consent.
   No photo? Say "generate one": Muse creates a first portrait
   from your description, you approve it, and that approved image
   becomes the anchor.
2. Character basics (5–8 visual anchors): face shape, eyes, nose,
   lips, hair (style + color + part), skin tone, build. If a photo
   is supplied, Muse reads these from the photo; the user only
   corrects what is wrong.
3. Proportion target — default: 7.5–8 heads, legs more than half
   of total height. The user may set other numbers or keep the
   default.
4. Default outfit (optional) — default: neutral full-coverage
   clothing for the body-standard composite. Scene outfits are
   chosen per request.
5. Goal (optional) — stills only, or video (video always runs
   still-first, see §12).

### Interview format (Muse asks, one question at a time)

- Q1: "Please upload one clear face photo to use as the anchor.
  If you don't have one, say 'generate one' and I'll create a
  first portrait from your description for your approval."
- Q2: "From the photo I read: [list the anchors]. Correct anything
  that's wrong, or say 'correct'." (No photo: ask hair style /
  color / part, face shape, and build in one short round.)
- Q3: "Proportion target: default is 7.5–8 heads with legs more
  than half of height. Keep the default, or set your own numbers?"
- Q4: "Default outfit for the composite is neutral full-coverage
  clothing. Any outfit you want as the default instead?"
- Q5: "Ready to build: face sheet + upper-body sheet + faceless
  body standard + composite. Shall I start?"
- Rules: one question at a time; every question shows its
  default; "defaults" accepts all remaining defaults; no
  generation before the Q5 confirmation.

### Fill-in template (if the user prefers to give everything at once)

```
Character name: ...
Face photo: [attached, or "generate one"]
Hair: style / color / part
Face: shape / eyes / nose / lips
Skin: ...
Build: ...
Proportion target: 7.5–8 heads (default) / other: ...
Default outfit: neutral full-coverage (default) / other: ...
Goal: stills / video
```

## 1. Anchor + fixed block verbatim

- Start from a face photo (the anchor). Distill 5–8 visual anchors
  (face shape, eyes, nose, lips, hair style + color + part, skin,
  build) into ONE paragraph, pasted verbatim into every prompt,
  never rewritten between shots.
- NEVER name a defect noun in a prompt (naming a mark multiplies
  it — observed twice). The reference photo carries it.
- No size words for eyes ("large eyes" pulls young); add "adult
  proportions" instead.

## 2. Role-labeled references

- Label every attached reference's role in the prompt (face /
  outfit / background / style). A source claim of "up to 10
  references" is untested here (max used: 3) — not disproven, not
  promised.

## 3. Same-thread continuity (first-class)

- Work in the SAME chat thread throughout; each generated image
  becomes the next call's anchor. The source method calls this the
  most important factor.

## 4. Sheets as separate images

- Face sheet (the anchor itself) + upper-body sheet + faceless
  full-body sheet, each its OWN image. NEVER a one-image 3-cut
  sheet: the close-up face inflates the full-body scale. A 3-cut
  example sheet's headless full-body panel carries no face scale
  at all.

## 5. Body standard (separate, faceless)

- Faceless mannequin, black bodysuit, frontal, 85–135mm,
  waist-height camera, distant framing, seamless light-gray
  background. It carries the proportion spec as FORM (hourglass:
  defined bust, narrow waist, wide hips, legs more than half of
  total height) — not exposure. Measured: 7.4 heads (hourglass
  form) / 8.3 (neutral form).

## 6. Composite

- Face refs (anchor + frontal upper sheet) + mannequin body
  standard → full-body portrait, neutral outfit by default (full
  coverage). Face-presence pull-down is real: mannequin 7.4 →
  with-face composite 6.8 before correction; the ladder below
  closes it.

## 7. Full-body camera (never break these)

- 85–135mm, distant, waist-height. Never high angle, wide angle,
  or close framing. Numeric head-count wording ("8 heads") in a
  scene prompt does NOT move the generator's default (~6 heads) —
  use photo type, camera conditions, and body-part relationships.

## 8. Hair for measurement

- Tied-back / ponytail / behind-ear hair so head size reads
  cleanly; voluminous loose long hair inflates apparent head size.
  CAUTION: a wind-blown ponytail in a dynamic scene merges into
  the head bbox and voids pixel measurement → the user's eye
  governs (see §11).

## 9. Relative-edit ladder (one change at a time)

- Template (verbatim): "Keep everything else exactly the same,
  only make the head smaller than now. Do not change the face
  features, body, pose, or background." If one attempt does not
  reach target, repeat the SAME request 1–2 times, then switch
  body part ("legs longer"). Absolute targets edit worse than
  relative ones. Never edit two elements at once.

## 10. Auto-ladder

- After EVERY measurement, if below target and the face holds,
  apply the next rung AUTOMATICALLY — no manual prompt per rung.
  Rung budget: initial + up to 2 repeats; stop a rung early on
  target / worse ratio / face break. Face gate: a step that breaks
  the face stops that image's ladder; keep the last face-holding
  version. End: target reached → stop + report; all rungs
  exhausted → stop + report (escalate, never loop forever);
  per-response generation budget may defer remaining rungs as
  explicit pending auto-steps, never as completed work.

## 11. Measurement

- Pixel grounding bboxes (0–1000 normalized) for head / full body
  / legs from the actual file. Head-count = full height / head
  height. Legs% = legs height / full height. Face verdict by eye
  vs anchor (zoomed crops for stills). Long coats/dresses occlude
  the hip line → legs% under them is NOT a valid anatomical
  measure (report as unmeasurable, not failure). Contaminated head
  bbox (hair merged) → pixel count VOID → user eye verdict
  governs (final gate).

## 12. Video

- Still-first (approved still → image-to-video). Small motion
  first; increase only after identity holds. Start-frame anchor
  alone does NOT hold identity through motion (verified failure
  on two engines: face changes in playback despite still-frame QA
  passing). Structural fix still untested on this content:
  keyframe PAIR (start + end frames, same shot scale, short 2–4s
  beats).

## 13. Scope and limits (honest)

- Validated on test faces: studio composite 7.6 heads
  (ladder-closed); scenes café (face), neon (user eye ~8), park
  7.7, trench 7.9. Transfer from improved studio (7.6) beats the
  old studio (7.35 → scene mean 6.6).
- Tool-level integrity refusals for specific requests stand;
  never retry with changed arguments.
- This skill is the generic method only. Any single character's
  private canon (reference photos, identity marks, project rules)
  lives outside it and wins on conflict for that character's work.

Evidence summary: `references/evidence.md`.
