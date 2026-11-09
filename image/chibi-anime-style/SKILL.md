---
name: chibi-anime-style
description: Convert a character image into a flat-pop chibi illustration (2.5–3 heads, big round eyes, thick black outlines, flat colors, 1:1 square, solid background) while keeping the character's identity — hair, eye color, outfit, accessories. Trigger: "치비 애니스타일".
---

# Chibi Anime Style — flat-pop chibi converter

## When to use

- The user says "치비 애니스타일" (or asks for a chibi version) and supplies a character image — photo, anime illustration, 3DCG, or painting.
- Output is a cute, simple, pop Japanese chibi illustration for a profile icon, sticker, or SNS post.

## Method

1. Take the source image as the character reference. Apply the full conversion prompt in `references/chibi-flat-pop-prompt.md` with the image attached.
2. Identity lock first: hairstyle, hair color, bangs, length, parting; eye color (including heterochromia); skin tone; outfit shape, pattern, colors; hat, hair ornaments, glasses, accessories; ears, horns, wings, tail. Never change these.
3. Rebuild the body as a 2.5–3-head chibi: big round head (~1/2.5–1/3 of total height), narrow shoulders, very short neck, compact torso, short limbs, small rounded shoes. Do not just enlarge the head on a normal body.
4. Face: large round eyes with separately filled sclera (pure white) / iris (source color) / pupil / highlight; small round mouth; pale pink blush (few short diagonal lines); nose nearly omitted; thin short eyebrows.
5. Line art: thick black outer outlines, slightly thinner inner lines, smooth clean curves, no pencil texture.
6. Coloring: flat solid color fields, at most one step of shadow, no gradients, no realistic texture or lighting.
7. Background: solid color only — keep the source background color; if it is a gradient, take its representative color; if it is a complex scene, or the color cannot be determined, use plain white (#FFFFFF). No scenery, texture, or vignette.
8. Composition: 1:1 square, respect the source framing (close-up stays close-up, full body stays full body). Never stretch the body to fill the square; never add body parts outside the frame.

## Output contract

- 1:1 square image, flat-pop chibi style, character identity preserved.
- No added text, logo, or watermark.
- Show the result to the user before using it as a series style or icon.

## Examples (Korean)

- "이 캐릭터를 치비 애니스타일로 바꿔줘"
- "이 사진 속 인물을 치비로 만들어줘, SNS 아이콘용으로"

## Neighbours (not this skill)

- `doodle-overlay` — hand-drawn doodle characters over a photo, not a character-style conversion.
- `photoreal-realness` — realistic smartphone-photo look, the opposite direction.
- `pencil-line-poetry` (동양미 스타일) — delicate pencil-line Oriental style, not flat-pop chibi.

## References

- `references/chibi-flat-pop-prompt.md` — the full conversion prompt (Japanese, verbatim source).
- `references/examples/image-49.png` … `image-54.png` — six style examples supplied with the method.
