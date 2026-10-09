---
name: "place-video-prompter"
description: "Generate a paste-ready Korean video-production prompter (director prompt for GPT) for a real place — building, landmark, store, campus, restaurant, stadium, park, domestic or overseas — with strict realism guardrails: verify identity against real photos/sources, derive story and direction fresh per place, and ban generic interchangeable scenes."
---

# Place Video Prompter

## Purpose

Turn a real place name into a complete, paste-ready Korean prompter that instructs
GPT (or any video model) to produce a realistic live-action promo video of that
place. Every prompter is derived from verified facts about the place — never a
find-replace of a previous one.

Prompt design lineage: the "director prompt" pattern from a 20-second
Kyobo Bookstore Gwanghwamun promo prompter (user-supplied, 2026-10-01),
generalized by Claude (CLAUDE_DESIGN, 2026-10-01).

## When to use

- The user names a real building, landmark, store, campus, restaurant, stadium,
  park, etc. (domestic or overseas) and wants a video-production prompter for it.
- Do NOT use for fictional places. The skill's scope ends at the prompter text:
  no video generation calls, uploads, or publishing.

## Workflow

1. **Parse input.** Place name + optional: branch/location, reference URL or
   photos, duration (default 20s), aspect (default 16:9), resolution (default
   1080p), fps (default 24), sound (default music + SFX). Ask only about
   ambiguous parameters.
2. **Fix identity.** Resolve the exact target: branch, city/country,
   local-language name, operating status. Check same-name different places,
   closures, renovations. If it can't be narrowed to one, ask the user.
3. **Collect and verify.** Official site, map listings, real photos, press →
   fact sheet with per-item tags: **V** (verified: 2+ independent sources, or 1
   official source + photo), **P** (partial: single source or indirect evidence),
   **U** (unverifiable). Mark whether each item was photo-confirmed or
   text-only.
4. **Classify type.** Primary + secondary type by "why people come here".
   See `references/type-rules.md`.
5. **Extract uniqueness.** Per-type questions → signature inventory (space,
   objects, activities, light, sound, culture). **Swap test** every candidate
   scene: "would this shot look the same filmed at a competing place?" If yes,
   drop it.
6. **Decide direction.** Protagonist (= the reason people visit), audience, time
   of day (golden hour / blue hour / noon / night — chosen from evidence) /
   season, emotion, rhythm, music/SFX direction, and cinematic specs (camera
   and lens look, color grade, film grain). Attach fact-sheet evidence to each
   decision; mark the rest as "연출 선택" (director's choice).
7. **Assemble.** Fill `templates/master-prompt.ko.md` with parameters + fact
   sheet + type block. Apply `references/fallback.md` for U/P items.
8. **Self-audit.** Re-run the swap test, scan for fabricated facts,
   first-person testimonials, and parameter mismatches. On any failure, return
   to step 7.

## Output Contract

Emit three blocks, in order:

- **A. Paste-ready prompter** (Korean, one code block). GPT-ready; embeds the
  fact-sheet summary and the type block. The shot list is NOT embedded by
  default — the prompter directs GPT to decide shots from the material
  (pass `--shots=embed` to include block C as reference suggestions).
- **B. Pre-flight checklist** (for the user). Fact sheet with tags, sources, and
  photo-confirmation status; a "needs your check" list (U items, possible
  shooting / commercial-use restrictions); confirmed parameters and the type
  rationale.
- **C. Shot-list template** (reference). Per beat: time, scene, a one-line "why
  this shows THIS place", evidence IDs, sound. Default beats for 20s:
  0–3s recognition, 3–9s signature experience, 9–15s place-only details,
  15–18s climax, 18–20s close. Scale beats proportionally for other durations;
  for 9:16 keep the beats, switch framing to vertical.
- **D. English video-generation prompts** (optional, on request). Per-scene
  English prompts compatible with Sora / Runway / Luma, derived from block C:
  camera body + lens (e.g. 35mm anamorphic, f/1.8), lighting, motion, and
  photorealism keywords. Introduces no new facts beyond the fact sheet.

## Operating Rules

1. Never fabricate unverified details. Opening hours, prices, awards, founding
   year, visitor counts, events: V tag or don't write them. Time-sensitive facts
   stay out by default even when verified.
2. No first-person fabrication: no reviews, interviews, "I visited" narration,
   ratings, or quotes. On-screen people are anonymous visitors doing verified
   activities — staging, not testimony.
3. No real identifiable people. Signage, logos, on-screen text: confirmed
   spellings only; no invented slogans, prices, or numbers.
4. Re-derive story and direction for every place. Never recycle a previous
   video with a swapped name.
5. Overseas places: include the local-language original alongside the Korean
   rendering; reflect local signage script, traffic direction, dress norms, and
   etiquette from verified sources only — never stereotypes. Flag possible
   shooting / commercial-use restrictions in block B.
6. Read-only investigation. No generation calls, uploads, or publishing — and
   never claim a video was produced.
7. If Tier-1 identity facts (exterior, signage, signature space) are U: do not
   emit block A. Emit block B only and request photos or a URL.
