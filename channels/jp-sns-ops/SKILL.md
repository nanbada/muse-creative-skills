---
name: "jp_sns_ops"
description: "Japan-side Instagram/SNS operations playbook: early-20s colloquial captions, carousel templates, hashtag and timing rules. Use when drafting Japanese captions, planning posts, or setting up a new Japan-targeted SNS account."
---

# JP SNS Ops Playbook

## Purpose
Apply the researched Japan-market Instagram/SNS operating rules to any Japan-side account, without re-deriving them each time.

## Workflow
1. **Caption draft** — write in the early-20s colloquial style per `references/caption-style.md`; run its 10-item pre-publish checklist before finalizing.
2. **Hashtags** — max 5 per post, end block, JP+EN mix; rules in `references/caption-style.md`.
3. **Carousel posts** — apply the 10-pattern production template in `references/carousel-playbook.md`.
4. **Timing** — default to the account's own insights (follower active hours); Japan-specific measured data unavailable. Measured reference (2026-10-11): carousel-focused weekday 8–10 / 12–14 JST, overall prime 19–21 JST.
5. **New account setup** — follow `references/account-setup.md` so a new Japan-side account ships with these defaults pre-applied.
6. **Render card-news via Canva** (connector verified connected 2026-10-14, `canva status` → authenticated) — build the carousel copy from step 3 into a design with `canva create-design`, export PNGs with `canva export-design`. Read `/opt/hatch/skills/canva/SKILL.md` before first use (schemas are live). Human approval before anything is published.

## Output Contract
- Captions are delivered in final, checklist-verified Japanese.
- New accounts start with the playbook defaults; any deviation is flagged to the user before publishing.

## Operating Rules
1. A user-given caption direction always wins over this playbook.
2. AI-generated content label stays ON for AI-persona accounts, every post.
3. Never exceed 5 hashtags per post (Instagram 2026 limit).
4. Posting time is set per account from its own insights (or the measured reference in Workflow step 4) — never claim a Japan-specific "golden hour" without measured data.
5. Keep this file lean; load a reference file only when its step is active.
