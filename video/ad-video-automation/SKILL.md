---
name: "ad_video_automation"
description: "Automate short product ad videos (15-20s, 9:16): concept research, hero image product lock, block video drafts with review gate, code overlay for text/graphics/BGM. 4-role pipeline (Muse directs, Claude writes copy/prompts, GPT reviews, human approves). Use when the user asks for ad video automation, virtual product ads, or brand sales samples."
---

# Ad Video Automation

## Purpose
Produce a 15–20s vertical (9:16) product ad from a product brief with minimal human touch: research → copy → hero image (product identity lock) → block video drafts → human review gate → code overlay → final assembly. Source pattern: @Promptwatch Pepero virtual-ad (2026-10-09, 17s, 2h, ~5 drafts + 3 finals).

## Pipeline (9 steps, 2 human gates)

1. **Concept research** (Muse): search existing products/flavors, exclude them, pick 2 concepts. Never invent a real brand's product as real — virtual ads only.
2. **Copy + prompt design** (Claude via `consult-claude`, Opus): ad copy, product naming, per-block video prompts (English). Muse supplies the brief; Claude returns copy pack.
3. **Hero image — L1 product lock** (Muse native first): one hero image per concept with packaging typography baked in. This is the identity anchor; every video block references it (image-to-video). If Muse output fails typography QC, escalate to GPT Image 2.5 API — requires user approval (paid key).
4. **Block drafts, low-res** (default: Veo 3.1 via Flow, Lite/Fast tiers): opening / concept A / concept B / closing, ~3–5s each. Draft at the cheapest tier that shows composition and motion.
5. **REVIEW GATE 1 (human)**: user picks passing blocks. Regenerate only failed blocks. This is the cost lever — never upscale rejects.
6. **Finals** (Quality tier or Seedance re-inference): passing blocks only, 1080p.
7. **Code overlay** (Muse, HyperFrames): subtitles, graphic callouts (price tags, gauges), BGM. See `code-animation-vertical` patterns.
8. **Assembly + QC** (Muse): ffmpeg mux, loudness −14 LUFS, typo sweep on all baked text, sync ±100ms.
9. **APPROVAL GATE 2 (human)**: final sign-off before any client/external delivery.

## 4-role contract

- **Muse — director/executor**: owns the pipeline, research, QC, assembly, and this skill file. Default thinker.
- **Claude — copywriter/prompter**: `consult-claude` for ad copy, naming, block prompts. Never the default executor.
- **GPT — challenger/reviewer**: `consult_codex` for concept review (brand safety, copy punch). Not an image API.
- **Human — review + approval**: gate 1 (block select), gate 2 (final). No auto-delivery to clients.

## Cost tiers (see `references/cost-notes.md` for dated numbers)

- **Flow path (default)**: ~400 credits per 17s ad — inside the 1,000/month + 50/day budget. Cash cost 0.
- **Seedance path (opt-in, paid API key required)**: ~$5–10 per ad. Draft Mode (480p draft → 1080p re-inference) cuts 57–77%.
- **GPT Image 2.5**: <$0.50 for 2 hero images (paid key required).

## Operating Rules
1. Paid API keys (Seedance third-party, OpenAI) are never issued, charged, or registered without explicit user approval. The paid-line rule applies.
2. Never claim full automation of Flow generation — semi-auto contract (Muse plans, human clicks generate).
3. Virtual ads of real brands carry a mandatory on-video/text disclaimer: "AI 컨셉 샘플 — 실제 출시 제품 아님". Never present a virtual ad as a real product.
4. Seedance carries unresolved copyright pressure (MPA vs ByteDance, 2026-07) — prefer Veo/Flow for commercial client work; document the risk if Seedance is used.
5. One concept → one pipeline run. Never reuse a hero image across different products (identity lock is per-product).
6. Cost numbers carry a date stamp (2026-10). Re-check pricing before committing to a client quote.
7. Prompts in English, user-facing notes in Korean. Internal docs in English.
