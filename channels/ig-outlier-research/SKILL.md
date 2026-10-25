---
name: "ig-outlier-research"
description: "Find what's working in an Instagram niche now: rank reels by outlier multiple (views ÷ account's own median), name each hook formula, build a swipe file. Use when the user asks what's working or what to make next (Korean trigger: 바이럴 분석, 스와이프 파일). Captions: ig-caption-lint."
---

# IG Outlier Research

Ported 2026-10-14 from `Jakeschincariol/instagram-agent-skill` (MIT),
`skills/ig-viral` (+ `hooks.json`, `hookscore.py` from `skills/ig-reel`).
Adapted: paths are relative to the skill folder.

## The one idea
**Raw views are not evidence.** An account with 2M followers doing 400K
views had a quiet Tuesday. An account with 4K followers doing 400K views
found something copyable. Rank everything on the **outlier multiple**:
views ÷ that account's own recent median. Above 3x = signal. Below 1.5x =
their normal day, teaches nothing.

## Workflow
1. **Pick 6–12 accounts** (4 direct niche, 4 adjacent audience, 2–4
   outsized for format only) within ~10x of the user's size. Ask the user
   or propose + get approval. Their Saved collection is the fastest corpus.
2. **Go and look** (monthly, not daily — formulas last a season). Capture
   per reel: account, followers, median (eyeball last 12 reels), views,
   hook (first line, verbatim), on-screen text, length, CTA. Write to a
   TSV with header `account followers median views hook`.
3. **Rank it**: `python3 swipe.py captured.tsv --out swipe.md`. It computes the outlier
   multiple, names hook formulas (26 in `hooks.json`), and scores hooks.
4. **Report three things**: which formulas over-index in the top third
   (with counts), what the top third share structurally (hook length,
   visual payoff, first-frame motion), and the unclassified rows (read by
   hand — most valuable column). State sample size and confidence plainly.
5. **Shoot from it**: for the top 3 formulas, write the user's own version
   — their story, their number, in the working shape. Never "make a reel
   like this one."

## Scripts
- `swipe.py` — ranks the TSV, names formulas, writes the swipe file.
- `hooks.json` — 26 hook formulas. `hookscore.py` — hook scorer.

## Operating rules
1. **Never log into Instagram on the user's behalf; never ask for a
   password.** If a page needs login, the user drives or pastes.
2. **Reading, not scraping.** ~10 accounts × ~12 reels at human speed.
   No crawlers, no scraping services, no background loops (ToS + action
   blocks).
3. **Copy the formula, never the video.** Hook shape, structure, length,
   cut pattern — not their script or voice. Attribute every swipe-file row.
4. When Instagram won't show enough: YouTube Shorts is a legitimate second
   corpus (public view counts, auto-captions for the spoken hook).
5. Nothing is posted, followed, liked, or messaged by this skill.
