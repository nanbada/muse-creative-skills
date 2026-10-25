---
name: "competitive-brief"
description: "Research competitors and produce a structured brief: positioning/messaging comparison, content gaps, opportunities, threats, and battlecard-ready takeaways. Use when the user asks for competitor research, a market comparison, or 'what are competitors doing' (Korean trigger: 경쟁사 분석, 경쟁 조사)."
---

# Competitive Brief

Ported 2026-10-11 from `anthropics/knowledge-work-plugins` (Apache-2.0),
`marketing/skills/competitive-brief`. Adapted to this runtime: connector /
MCP references removed; research runs on `browser.search`,
`social.search`, `browser.open`, and the `social-sourcing` skill.

## When to use
- User asks for a competitive analysis, competitor research, market
  comparison, or a sales battlecard.
- Pairs with `seo-audit` (SEO dimension) and the video-planning
  `competitive-scan.md` research (content-format dimension) — don't
  duplicate those; cross-reference them.

## Inputs (ask if missing)
1. **Competitor name(s)** (required).
2. **Your context** (recommended): what you sell/sell to, positioning,
   differentiators to highlight.
3. **Focus areas** (default: all) — messaging/positioning, product
   comparison, content strategy, recent news, pricing (if public),
   market presence.

## Research process (per competitor)
1. **Primary sources** — website (homepage, product, pricing, about,
   careers), blog/resource center (themes, frequency, depth), social
   profiles, press/newsroom (last 6 months), job postings (strategy
   signals).
2. **Secondary sources** — review sites (G2, Capterra, TrustRadius),
   news coverage, community sentiment (Reddit, X via `social.search`),
   SEO signals (keyword overlap, content gaps).
3. Mark every claim with its source; separate confirmed facts from
   inference. No invented funding numbers, user counts, or launch dates.

## Output contract
- Executive summary (2–3 sentences: landscape, biggest opportunity,
  biggest threat).
- Competitor profiles (positioning, messaging, content strategy, recent
  moves, pricing if public).
- Head-to-head comparison table (dimensions × you vs competitors).
- Content/positioning gaps competitors haven't claimed.
- Opportunities and threats, each one line with evidence.
- Battlecard takeaways: 3–5 talking points with a one-line proof each.

## Cadence
- Deep brief: quarterly. Monitoring scan: monthly (new announcements,
  messaging changes). This skill does one-shot briefs; recurring
  monitoring belongs in a cron job card, not here.

## Operating rules
1. Evidence discipline: every comparative claim carries a source;
   unverified items are marked, not smoothed over.
2. Don't re-run `seo-audit` or the video competitive scan inside this
   skill — reference their outputs.
3. No contact with competitors, no fake signups, no scraping behind
   logins.
