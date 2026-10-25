---
name: "seo-audit"
description: "Run a structured SEO audit — keyword research, on-page analysis, content gaps, technical checks, competitor comparison — with a prioritized quick-wins vs strategic action plan. Use when the user asks for an SEO audit, keyword opportunities, or a content-gap analysis (Korean trigger: SEO 진단, 키워드 분석)."
---

# SEO Audit

Ported 2026-10-11 from `anthropics/knowledge-work-plugins` (Apache-2.0),
`marketing/skills/seo-audit`. Adapted to this runtime: Claude Code/MCP
connector references removed; research runs on `browser.search` /
`social.search` / `browser.open`.

## When to use
- User asks for an SEO audit, keyword research, content-gap analysis,
  technical SEO check, or competitor SEO comparison.
- Naver Blog channel work: pair with the `naver-blog-editor` skill —
  Naver's ranking (UGC-first, freshness-weighted) differs from Google's,
  so apply the Naver-specific checks from that skill alongside this structure.

## Inputs (ask if missing)
1. **URL or domain** (or a topic/keyword for keyword-research mode).
2. **Audit type** — full site audit (default) / keyword research /
   content gap analysis / technical SEO check / competitor comparison.
3. **Target keywords** (optional).
4. **Competitors** (optional; if needed and not given, identify 2–3 via
   web search).

## Process
1. **Keyword research** — via `browser.search`: primary/secondary keywords,
   long-tail and question-based ("how to / what is") variants, intent
   classification (informational / navigational / commercial /
   transactional). Mark volume/difficulty as high/medium/low from
   observable signals; never invent numbers.
2. **On-page audit** — per key page: title tag (50–60 chars, keyword),
   meta description (150–160, CTA), single H1, H2/H3 hierarchy, keyword
   in first 100 words, internal links + orphan pages, image alt text,
   clean URL structure.
3. **Content gap analysis** — competitor topics you don't cover, stale
   pages (12+ months), thin content (<300 words for informational
   queries), missing formats (guides, comparisons, glossaries, tools),
   funnel-stage gaps (awareness / consideration / decision).
4. **Technical checklist** — page speed, mobile-friendliness, structured
   data opportunities, crawlability (robots.txt, sitemap, canonicals),
   broken links, HTTPS, indexation risks. Verify with `browser.open`
   where possible; mark unverifiable items as such.
5. **Competitor comparison** — keyword overlap/gaps, content depth and
   publishing frequency, backlink signals, SERP feature ownership.

## Output contract
- Executive summary (3–5 sentences: biggest strength, top 3 priorities,
  overall verdict).
- Keyword opportunity table (15–25 rows, sorted by opportunity score).
- On-page issues table (Page / Issue / Severity / Fix).
- Content-gap recommendations (topic, why, format, priority, effort).
- Technical checklist (Pass / Fail / Warning).
- Prioritized action plan: **Quick wins** (<2h, this week) vs
  **Strategic investments** (this quarter), each with impact + effort.
- Follow-up offers: content briefs for top keywords, title/meta rewrites,
  content calendar from the gap analysis.

## Operating rules
1. Never invent ranking positions, search volumes, or traffic numbers —
   mark estimates as estimates.
2. For Naver Blog audits, Naver-specific rules (from `naver-blog-editor`)
   take precedence over generic Google-centric checks.
3. Publishing or editing the user's site needs the standing approval gate;
   the audit itself is read-only.
