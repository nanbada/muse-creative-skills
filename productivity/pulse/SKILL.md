---
name: "pulse"
description: "Take the pulse of any topic across Reddit, Hacker News, the open web, and X in a recent window (default 30 days): cited briefing with engagement signals and cross-platform patterns. Use for 'what's happening with X', trends, sentiment (Korean trigger: 최신 동향 조사, 여론 조사). Deep research: research-brief."
---

# Pulse — Multi-Source Recency Research

Ported 2026-10-14 from `aicodedecode/awesome-muse-skills` (MIT),
`skills-imported/pulse` v1.0.0 (`references/`, `scripts/` copied verbatim).
Adapted to this runtime — see Runtime adaptations below.

Captures the **current conversation**, not the canonical reference.

## Phase 0: Intake (max 4 questions, one at a time)
1. **Topic** — 1–2 sentences, specific. Push back once on "AI"-level mush.
2. **Angle** — trend / sentiment / problems / opportunities / comparison
   (default: trend).
3. **Window** — 7 / 14 / 30 / 60 / 90 days (default: 30).
4. **Platforms** — skip any that don't fit the angle; default all.

## Phases (1–3 in parallel, 1 q/sec per platform)
- **Reddit**: `social.search` (subreddit + keyword) + vibewatch digest as
  backup. Top posts in window, then top comments on the top 3–5.
- **HN**: Algolia API (`hn.algolia.com/api/v1/`) via curl — stories, then
  comments in window. Note HN's builder bias in synthesis.
- **Web**: `browser.search` — trusted publishers, recent reviews,
  problems/complaints queries. Fetch top URLs; never cite snippets alone.
- **X/Twitter** (optional, last): `social.search` where it reaches;
  otherwise skip with an explicit note. Never pretend to have data.

## Integrity rules
- Cite only sources returned by this session's tool calls. Training
  knowledge is `[Background — not from search]`, excluded from counts.
- Track queries sent / sources received / sources cited
  (`scripts/citation_tracker.py`).
- Retry once after 3s; after 3 consecutive failures across all sources:
  stop, share what was collected, never deliver an empty file.

## Synthesis
Consensus (3+ platforms agree) / controversy (platforms disagree) /
pain points / excitement / emerging trends (new vs top) / gaps. Every
pattern cites its source URLs. See
`references/cross_platform_synthesis.md` for heuristics.

## Output
Save to `<research-dir>/pulse/<slug>-<YYYY-MM-DD>.md` AND paste in
chat: TL;DR (2–3 sentences), per-platform sections with cited bullets,
cross-platform patterns, 3–5 key takeaways, content angles if applicable,
plus the audit line (queries sent / received / cited).

## Runtime adaptations (this VM)
- `reddit.com/search.json` is egress-blocked here — the Reddit phase runs
  on `social.search` + the vibewatch digest, not the raw JSON API.
- X has no login here; treat Phase 4 as usually-skipped with a note.
- Complements `research-brief` (deep, source-backed) and the
  `muse-vm-daily-research` cron (scheduled scans): pulse is the
  on-demand recency layer. Don't duplicate a scheduled scan — reference it.

## Scripts
- `scripts/time_window_calculator.py` — window → timestamps.
- `scripts/citation_tracker.py` — three-count audit log.
- `scripts/topic_slug_generator.py` — output slug + dedup.
