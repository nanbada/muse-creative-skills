---
name: watercolor-studio
description: 'Turn a text prompt or a reference photo into an expressive watercolor painting: floral-fashion fantasy, European storybook atmosphere, botanical, loose wash, or ink-and-wash. Use when the user asks for watercolor, a photo-to-watercolor conversion, or a watercolor-style image. Not for pencil-line poetry (use pencil-line-poetry), doodle characters over a photo (use doodle-overlay), or photorealistic phone snaps (use photoreal-realness).'
---

# Watercolor Studio

Generate watercolor artwork from a text prompt, or convert a reference
photo (person, pet, landscape, architecture, fashion) into a watercolor
painting. Prompts are composed in English; the two predefined core styles
below are the defaults — they come from reference images the user supplied
(fine pen line + translucent flower dresses; warm European alley and cafe
storybook scenes).

## When to use

- The user asks for a watercolor painting, drawing, or watercolor-style image.
- The user uploads a photo and asks to turn it into watercolor.
- The user names a watercolor variation: botanical, loose wash, ink-and-wash
  (pen-and-wash), splash, wet-on-wet.
- Trigger words: "수채화", "watercolor".

## Core styles (defaults)

1. **Floral-fashion fantasy** — figures in dresses woven from translucent
   flowers, rainbow clouds, stardust, or autumn foliage; ultra-fine pen
   outlines; translucent layered washes; pastel luminous tones; clean white
   or light paper background. Default for portraits and fashion. When the
   user wants the vivid attached-reference look, apply the reference DNA
   in `references/style-prompts.md` section 1b instead of the soft pastel
   default: fitted bodice with a skirt that IS a bouquet of oversized
   blooms, slender elongated figure, matching floral heels and flower
   crown, vivid saturated flowers on a pale luminous ground.
2. **European storybook atmosphere** — cozy cafe terraces, vintage
   cobblestone streets after rain, black cats under the moon, warm cottage
   interiors; detailed ink linework; warm lantern light, wet-road
   reflections, muted vintage tones, deep indigo night skies, rough paper
   grain. Default for scenery and animals.
3. **Botanical / loose / ink-and-wash** — flowers, pets, landscapes,
   portraits, still life; loose spontaneous washes, botanical precision, or
   East Asian ink-wash fusion. See `references/style-prompts.md` for the
   modifier blocks.

If the user names no sub-style, infer from the subject (fashion/portrait
-> 1, scenery/animal -> 2) instead of asking.

## Workflow

1. **Read the request.** Text-only or reference photo? Subject? Sub-style
   (default per above if unspecified)?
2. **Pick the aspect ratio.** Full-body fashion / portrait: 3:4 or 9:16.
   Panoramic landscape / street scene: 16:9 or 4:3. Standard canvas: 1:1.
3. **Compose the prompt in English.** Subject first (pose, lighting,
   expression), then the style block from `references/style-prompts.md`:
   technique words (wet-on-wet washes, pigment pooling, granulating
   washes, delicate outlines, paper texture) are mandatory, not decoration.
4. **Photo input.** Pass the reference photo to the image generation tool
   alongside the prompt, led by a transformation instruction: "Transform
   the reference into a delicate watercolor illustration while preserving
   the subject's features and pose." Never describe the photo as the
   output; it is the input.
5. **Present.** Show the artwork, name the applied technique (palette,
   texture, paper style) in one line, and offer the next adjustment
   (palette shift, background element, more pigment bleed, another
   sub-style).

## Gates (do not skip)

- **Medium honesty.** Emphasize painted texture, water blooms, and
  transparency. Overly busy or photo-realistic prompt words fight the
  medium — cut them.
- **Faces.** For human figures, always specify delicate facial features
  and fine line art; otherwise faces go muddy or distorted. Floral-fashion
  figures: small delicate face, often in profile or downcast
  three-quarter view, minimal features — never a large detailed front face.
- **Backgrounds.** Keep fashion/floral backgrounds airy and light so the
  watercolor bleeding reads.
- **Floral-fashion DNA check.** Silhouette must read as bouquet, not
  garment: fitted bodice, skirt exploding into oversized translucent blooms
  that extend beyond the body outline; blooms larger than the torso;
  slender elongated figure with matching floral high heels and a flower
  crown; vivid saturated flowers against a pale cream or pale pink ground;
  splatters, drips, color bleeding beyond ink lines, thin swirling
  flourishes, scattered petals and sparkles. A soft muted dress-shape with
  a detailed front face fails this check.
- **No copying.** A reference photo's composition may guide the painting;
  never reproduce another artist's finished artwork. The two core styles
  above are style descriptions, not copies of any single work.

## Examples

- "비 오는 날 찻잔을 앞에 두고 창밖을 보는 고양이를 동화풍 수채화로
  그려줘" -> storybook style, cozy interior, rain on window, warm light.
- "꽃잎이 흩날리는 파스텔톤 드레스를 입은 소녀를 그려줘" -> floral-fashion
  style, translucent petal dress, pastel palette, airy background.
