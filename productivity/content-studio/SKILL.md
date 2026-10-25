---
name: "content-studio"
description: "Drafter pattern: turn source material into channel-ready drafts without losing the original meaning. Drafts are automatic; publishing, sending, or scheduling always needs human approval. For Naver Blog specifics, pair with the naver-blog-editor skill."
---

# Content Studio — draft-only content production

Adapted from the awesome-muse-connectors Content Studio template (MIT), fitted to
this environment and the user's standing approval gates.

## When to use

- Turning source material (notes, research, files) into drafts for any channel:
  blog, Instagram/Threads captions, carousels, video scripts.
- The `naver-blog-editor` skill covers Naver-specific drafting rules; this skill
  is the channel-agnostic wrapper around it (source extraction → drafts →
  fact-check → approval gate).

## Method

1. **Extract from source.** Pull the source's claims, examples, names, dates,
   and direct quotes. Mark anything that needs fact checking. Preserve the
   author's meaning.
2. **Do not invent.** Never add a statistic, testimonial, citation, or customer
   claim not supported by the source. No fabricated first-person experiences.
3. **Produce the package:**
   - concise source summary;
   - one long-form draft;
   - three short variations (different hook / angle);
   - title + opening hook per channel;
   - suggested visual or document brief;
   - fact-check and rights/attribution checklist.
4. **Keep a link to the source behind every important claim.**
5. **Stop before the gate.** Do not post, email, schedule, submit, or share
   anything until the user approves the exact final version and destination.

## Standing approval gates (user policy, non-negotiable)

- Blog posts and reviews: human approval before any publishing step; never edit
  a live post without explicit approval of that exact change.
- Referral codes: any mention must disclose the mutual benefit.
- Virtual-character channels: AI-generated label from day one; no fake testimonials.

## Operating rules

- User-facing drafts are concise Korean following `humanlike-writing` rules;
  internal checklists stay in English.
- Tone: match the channel (blog = practical how-to; social = hook-first).
- Record reusable angles and hooks in the relevant goal workspace for the next run.

## First supervised run

Use a public or self-authored source and generate drafts only. Review factual
claims, tone, attribution, and channel formatting before connecting anything.
