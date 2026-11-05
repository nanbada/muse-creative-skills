# Prompts (verbatim from upstream, slots converted to {{placeholder}} syntax)

Image prompts work best in English, so keep these blocks in English even when
the rest of your workflow is in another language. Replace only the
{{placeholder}} slots; keep every style constraint and the ban list in every
edit.

## Base illustration prompt

```
Anime-style watercolor illustration, hand-painted, soft shading, BOLD
SIMPLE shapes with clean readable linework — never dense or finely
detailed line rendering. The scene reads at a glance, with generous
whitespace around each object, no people, no text, no watermark.
Style variations per episode are allowed (Ghibli-style, pastel watercolor,
sketch watercolor). Flat vector with thick black outlines is excluded as
the default.
Scene: {{a cozy kitchen with a window, a stove, a table with fruit, morning light}}.
Composition: wide view, everything clearly visible, generous whitespace
around each object so individual items are easy to count.
Difference targets (for the B edit): LARGE, at edges or corners, in the
foreground or midground — broad-area color changes, large objects, never
a tiny, blurry, far-landscape detail and never a thin-lined or
small-pattern target.
Every planned target must stay clearly visible once circled, including to
senior viewers(senior visibility rule).
```

## B version edit prompt

```
Edit this image changing ONLY these things, and nothing else (Medium = 3,
Hard = 5; each item is a color change, an object removal, or a count change):
1. Color change: {{the curtains change from yellow to green}}.
2. Object removed: {{the red kettle on the stove is gone}}.
3. Count change: {{the oranges on the table go from 4 to 3}}.
Keep the background, layout, colors, and every other object exactly the same.
Do not add, move, recolor, or remove anything else. Do not add text.
When an object is removed, paint the natural background in its place
(leaves, grass, wall, sky) — never leave a flat solid-colored patch.
Targets must stay LARGE and clearly visible once circled — never shrink
a target into a tiny distant detail, a thin line, or a small pattern to
raise difficulty.
```

## Worked example of a valid difference set (from a real episode)

Kitchen: curtains yellow to green, red kettle gone, oranges 4 to 3. Notice each
mechanism appears once, each target is large, and the count change is easy to
verify.

## Parody and still-cut scenes (v1.16)
- Famous painting / photo parody: describe the MOOD and generalized
  composition ("swirling night sky over a quiet village",
  "sunflowers in a vase on a wooden table"), never the original work's
  title, artist, or distinctive details. No signature, no copied
  brushwork, no identifiable real person — faceless or generic figures.
- Still-cut to illustration: stage the moment as a fresh illustration
  ("two friends laughing on a rooftop at sunset, movie-still framing"),
  never "recreate" a specific film frame, character, costume, or logo.
- Ad-friendly staging: leave blank signboards, plain packaging, and
  unbranded props in the scene; never render a logo or brand name.
