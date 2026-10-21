# Realness Prompt Blocks

Source: こけぞう (@gaget12090105), X 2026-10-07 — "崩す (break down), not 盛る (dress up)".
Philosophy: a real-person feel beats a perfect beauty. Strip the AI look
(over-retouch, symmetry, gloss) by deliberately breaking the finish.
Community know-how — attribute as such when citing publicly.
Original post: https://x.com/gaget12090105/status/2107760816728732075

How to use: paste selected blocks in English after the scene/character
description. Start with the Quick Trio (1a + 4a + 4e — the post's recommended
minimum), then escalate by what still feels wrong. All 20 at once is not
recommended; "more" is not "more real".

## Quick Trio (start here)

1a. "Finish this as a candid everyday photo of a real adult, casually shot on a smartphone — not an artwork."
4a. "Do not render the skin uniformly — keep visible pores, fine vellus hair, a faint blush, and natural shading."
4e. "Above all, prioritize realness, lived-in feel, and natural imperfection over perfection."

## Step 1 — Break the "artwork" (snapshot philosophy)

1a. "Finish this as a candid everyday photo of a real adult, casually shot on a smartphone — not an artwork."
1b. "Suppress CG-like smoothness, excessive whitening or retouching, and unnatural gloss."
1c. "Keep the beauty, but do not perfect the face and skin — leave the finish deliberately imperfect."
1d. "The mood of an ordinary person shooting for SNS, not an advertisement or promo shoot."
1e. "Prioritize a natural frame that could plausibly appear on a real SNS feed — not an AI artwork."

## Step 2 — Break the image quality (slight technical degradation)

2a. "Smartphone snapshot texture, not a DSLR — reject the over-sharpened high-resolution feel."
2b. "Light it only with light sources that would plausibly exist in that place — window daylight or indoor room light."
2c. "Keep a trace of slight hand shake, smartphone sensor noise, and mild resolution roughness."
2d. "Do not center the composition perfectly — keep a slight tilt or a left-right margin difference."
2e. "A moment caught off-guard in daily life, not a posed photograph."

## Step 3 — Break facial symmetry

3a. "Contour, bone structure, eyes, brows, nose, and lips in natural human proportions and placement."
3b. "No oversized pupils — keep a natural amount of sclera, left-right eye differences, and eyelid thickness variation."
3c. "A soft natural smile — the corners of the mouth and eyes gently relaxed, not a full posed grin."
3d. "Gaze shifted very slightly off the camera, not staring straight into the lens."
3e. "Leave tiny left-right differences in the brows, eyes, and mouth corners — never perfect bilateral symmetry."

## Step 4 — Add human noise

4a. "Do not render the skin uniformly — keep visible pores, fine vellus hair, a faint blush, and natural shading."
4b. "Hands and fingers anatomically natural — correct count, joints, lengths, and overlap; a realistic way of holding the smartphone."
4c. "Keep cleanliness and charm, but prioritize the approachability of someone who could actually exist on the street or on SNS."
4d. "Do not tidy every strand of hair — keep flyaways, loose strands, and irregular clumps natural."
4e. "Above all, prioritize realness, lived-in feel, and natural imperfection over perfection."

## Negative list (append last)

"no CGI-smooth skin, no porcelain or doll skin, no airbrushed beauty retouch, no perfectly symmetrical face, no oversized anime eyes, no studio lighting, no HDR glow, no beauty-dish catchlights, no centered perfect composition, no posed model expression, no full toothy grin, no DSLR-shallow-bokeh glamour look, no over-sharpened detail, no glossy plastic hair, no every-strand-in-place hair"

## Smartphone snap one-liner (user-supplied, 2026-10-08)

Paste-ready tag cluster for keyword-style image prompts. Use internally
whenever generating realistic smartphone photos — terse models, or when
the 4-step blocks are too verbose.

```
smartphone photo, shot on iPhone, unedited, natural documentary style, handheld camera shake, slight autofocus hunting, mixed ambient lighting, imperfect candid composition, edge color fringing, extreme photorealism, no post-processing color grading
```

Combines freely with Step 3/4 blocks (face asymmetry, human noise) and the
negative list. Overlaps with Step 2 (shake, mixed lighting) — duplicates
are harmless, don't stack both mechanically.

## Analog 35mm film one-liner (user keyword: 아날로그 35mm 필름, 2026-10-21)

Paste-ready tag cluster for an analog-film camera class instead of a
smartphone. Use when the user asks for the "아날로그 35mm 필름" look.

```
shot on 35mm analog film, natural film grain, soft halation on highlights, gently faded colors, warm analog tones, slightly imperfect exposure, candid documentary feel, no digital sharpening, no HDR, no post-processing color grading
```

Combines freely with Step 3/4 blocks (face asymmetry, human noise) and
the negative list. Do not stack with the smartphone one-liner — pick one
camera class per image.

## Tuning notes

- Face still reads "AI"? → Step 3 first (3e + 3c), then 1c.
- Skin still porcelain? → 4a is non-negotiable; 1b reinforces.
- Hands wrong? → 4b alone is worth more than any other single block.
- Too clean / too sharp? → Step 2 (2c + 2a), then 2d for framing.
- Combining with `photoreal-selfie-look`: use this skill's Step 3 + Step 4 blocks for the face, the selfie skill's look block for motion/grain/compression.
