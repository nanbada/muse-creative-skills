---
name: "research-brief"
description: "Evidence-disciplined research method. Use when a question needs a source-backed answer: decompose, hit primary sources first, link every claim, mark uncertainty explicitly. Research only — no outreach, no publishing."
---

# Research Brief — evidence-disciplined research method

Adapted from the awesome-muse-connectors Research Brief template (MIT), fitted to
this environment: browser tools, subagents, skills, and memory.

## When to use

- A question needs a source-backed answer (pricing, policy, how-to, comparison).
- The answer will feed a decision, a draft, or a user-facing claim.

## Method

1. **Restate and decompose.** Restate the question in one sentence. List the
   subquestions that decide it. State what would make an answer unreliable
   (stale data, single source, marketing copy).
2. **Primary sources first.** Prefer official docs, primary announcements, and
   raw data. Use reputable secondary sources only for context. Prefer current
   sources; record publication dates.
3. **Separate evidence tiers** (inline labels, from the session-log pattern):
   - `VERIFIED(how)` — checked against a primary source just now.
   - `ASSUMED(why)` — reasonable inference, not directly confirmed.
   - `UNVERIFIED` — could not confirm; say exactly what was tried.
4. **Never present** a search snippet, marketing claim, or unsourced number as
   established fact. Quote only short excerpts when necessary and link the source.
5. **No outreach.** Do not contact people, subscribe to services, submit forms,
   or purchase reports. If a source is paywalled or inaccessible, say exactly
   what could and could not be verified.

## Output contract

1. Five-sentence executive summary.
2. Answer to each subquestion.
3. Evidence table: claim | source link | date | confidence.
4. Strongest counterargument or missing evidence.
5. Practical options with trade-offs.
6. Three follow-up questions worth investigating.

## Operating rules

- User-facing text is concise Korean; the evidence table keeps source titles verbatim.
- Check memory first (`muse.memory_search`) — the answer may already be known.
- For broad topics, fan out to subagents with minimal briefs; require 1–2k token
  summaries back, never raw dumps.
- Record durable findings in `~/MEMORY.md` or the relevant goal workspace; record
  the method lesson in your learning log when it is new.

## First supervised run

Use a small question with a five-source limit. Check every link and label which
conclusions are inference rather than direct evidence.
