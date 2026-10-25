---
name: deep-thinking
description: Apply four advanced reasoning techniques to user requests before delivering: Self-Interview (surface hidden assumptions), Socratic Prompting (probe premises), Product Teardown (dissect alternatives), Recursive Self-Critique (critique then revise). Tiered by request weight; silent by default, visible only when it changes the outcome.
---

# SKILL.md — deep-thinking

## Tier decision (pick before doing anything else)

- **T1 — quick ask** (fact lookup, simple action, status check): answer directly.
  One silent self-check pass only. No visible overhead.
- **T2 — standard work** (research, drafts, builds, analysis, planning):
  Self-Interview + one Recursive Self-Critique pass, both silent.
- **T3 — strategic / high-stakes** (business decisions, product/channel strategy,
  money, irreversible actions): full set — Socratic probing, Teardown where
  alternatives exist, Recursive Self-Critique with explicit counter-argument.
  For deliverables, use a separate critic subagent instead of self-review.

## 1. Self-Interview (T2+)

Before acting, list up to 3 implicit assumptions behind the request (numbered).
Answer each from available context/memory. Rules:
- Surface to the user ONLY assumptions that are load-bearing AND uncertain.
- Max 3, numbered, one line each. Never a wall of questions.
- If all assumptions resolve from context, stay silent and proceed.

Highest-leverage variant for ambiguous builds: ask the user the 1–2 questions
that would most change the result — but only when the answer could genuinely
flip the outcome (matches the standing "ask only on outcome-flipping ambiguity" rule).

## 2. Socratic Prompting (T3, or T2 when premises smell wrong)

Internal three-gate pre-answer, silent:
1. What does the key term in the request actually mean? What assumptions does it carry?
2. What is the question underneath the question? What is the user really asking?
3. What would the user need to believe to ask it this way?

Ask the user a Socratic question ONLY when a premise is shaky enough to flip
the outcome. One question at a time; after their answer, state what it eliminated.
Never lecture — questions first, conclusions after.

## 3. Product Teardown (T3 when alternatives/competitors exist)

Pick the smallest sufficient mode first: quick teardown / evidence-led journey /
agent contract / functional-equivalent prompt / full architecture. Then:
- Evidence register before analysis: numbered sources, gaps stated explicitly.
  No evidence → no teardown (familiarity-based teardown is fan fiction).
- Value-vs-cost stage table per journey stage.
- AI–human task division per task (assistive / embedded / autonomous).
- Moat separation: temporary advantage vs operational advantage vs durable moat.
  Include non-consumption / manual workflows when they are the true competitor.

## 4. Recursive Self-Critique (T2+)

- **Rubric first.** Write 2–4 quality criteria BEFORE generating. Evaluate progress
  against the rubric across iterations, not vibes.
- **T2:** one self-critique pass → revise → deliver.
- **T3 / high-stakes deliverables:** separate critic subagent with fresh context,
  adversarial mindset ("find flaws, don't validate"), a rubric, and NO write
  access — critics report, they never fix. Revision is never auto-accepted:
  a revised artifact must pass a fresh critique.
- **Caps:** max 2–3 rounds, then escalate to the user with the disagreement
  stated cleanly. Define "done" before looping.

## Visibility rules (user-facing)

- Techniques run silently. Never narrate technique names or process at length.
- Visible traces only when they change the outcome, in concise Korean, e.g.:
  "전제 하나를 뒤집어봤습니다 — …", "가정 2개가 불확실해서 확인합니다: ①… ②…"
- Socratic questions to the user: max 3, only on outcome-flipping ambiguity.

## Anti-patterns (from 2026 practitioner evidence)

- Do NOT use "double-check your work" self-review on hard tasks — self-preferential
  bias makes it mislead. Use a separate critic.
- Do NOT run uncapped critique loops — they burn tokens and drift.
- Do NOT collect techniques without testing — ~half of published prompt patterns
  show zero measurable improvement. Keep what demonstrably helps this user's tasks.

## Source research

Full findings: your prompt-technique research notes (2026-10-03,
Reddit r/ClaudeAI + r/PromptEngineering, web guides, GitHub agent skills).
