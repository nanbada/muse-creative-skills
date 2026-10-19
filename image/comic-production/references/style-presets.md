# Style Presets (panel-stable)

Curated from ComicCrafter AI's tested set: these styles hold up across
panels. Pick ONE per project and freeze it in the global config.

| Preset | Look | Best for |
|---|---|---|
| `manga` | clean ink, screentones, high-contrast clarity | Japanese manga pages |
| `anime` | cel shading, expressive faces, stable design | anime-style stories |
| `superhero` | bold inking, dramatic perspective, action impact | action comics |
| `ligne-claire` | clear line (Tintin), detailed backgrounds, clean shapes | adventure, all-ages |
| `webtoon` | modern digital render, soft gradients, vertical flow | vertical-scroll webtoons |
| `noir` | high contrast, shadow-driven, cinematic light | crime, mystery |

## Global config (locked at Stage 1)

```
style_preset: manga            # one of the above
palette: [ink black, paper white, 1 accent]
border: thin black / rounded / none (webtoon)
panel_spacing: normal / tight
aspect: per-panel or per-page
```

Style changes propagate to ALL panels or not at all — never restyle a
single panel mid-project.

## Style block (paste verbatim into every panel prompt)

```
Style: manga — clean black ink linework, screentone shading,
high-contrast clarity, flat paper-white background. Consistent
with the project's locked palette. No photorealism, no 3D
rendering, no painterly texture.
```

Adapt the block per preset; keep it identical across all panels.

## Hard rule

Never put nameable words in a style string ("sunday", "newspaper",
"vintage poster") — the model will paint them into the art.
(comic-maker, learned the hard way)
