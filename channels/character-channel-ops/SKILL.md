---
name: "character-channel-ops"
description: "Operate a virtual-character Instagram channel (fictional persona): launch setup, character consistency, content cadence, caption/hashtag playbook, growth, monetization, and launch-blocking compliance (Meta AI labels, Korea FTC rules). Trigger: running/growing/posting/monetizing a virtual-character channel. JP caption drafting: jp-sns-ops."
metadata: { "includeInPrompt": true }
---

# Character Channel Ops (character-channel-ops)

Narrow-scoped skill for operating a fictional-persona Instagram channel.
Pilot character (example): a 21-year-old Japanese woman (university student,
photoreal style, 168cm), pillars: student/campus life 35 / fashion 40 /
Tokyo life 25.
Full research playbook: keep your own research notes (27 sources in the original) alongside the skill.
Benchmark data: keep your own AI-influencer benchmark alongside the skill.
Character bible: your character's bible file (appearance + non-visual traits).
Reference images: your character's reference folder.

Trigger ONLY when the user asks about the character channel: content planning,
posting, growth, monetization, or compliance for the virtual persona.
Do not activate for general Instagram questions or the Naver blog goal.

## Preconditions

- Never publish, schedule, or log in to Instagram on the user's behalf without
  explicit authorization for that exact action. Drafting and planning need no
  special approval; anything that touches the live account does.
- Never present the character as a real human. Never write fake firsthand
  testimonials ("I tried this product and my skin cleared") — Korea FTC treats
  them as false advertising even WITH disclosure.

## Step 1 — Compliance first (launch blockers, not afterthoughts)

1. Profile-level "AI-generated" label must be ON from day one (Meta policy
   2026-08-31). Unlabeled AI-persona profiles are excluded from
   Reels/Explore recommendations to non-followers. Labeled = no reach penalty.
2. Per-post "AI info"/"Made with AI" toggle ON for every AI-generated or
   AI-edited post, reel, and story. Caption text saying "made with AI" does
   NOT count as disclosure.
3. Korea FTC (2026-06-01): in any paid/recommendation content on Instagram,
   keep the text "가상인물" near the character, continuously visible while
   she appears. For text media: put it in the title or lead.
4. Korea FTC back-ad rules: ANY compensation (cash, product, coupon, affiliate
   commission) → Korean-language `광고`/`협찬` at the BEGINNING of the post,
   adjacent to the recommendation. `#ad`, buried hashtags, or "체험단" alone
   do not satisfy this.

Pre-publish checklist: profile AI label on → per-post AI toggle on →
`광고`/`협찬` at post start if compensated → `가상인물` overlay on paid video
→ no fake experience claims.

## Step 2 — Character consistency (the core technical work)

Consistency ladder, weakest to strongest:
1. Fixed seed — cheap, breaks easily.
2. Reference anchoring (`--cref`/`--sref`/IP-Adapter) — good for series work.
3. Character sheet (10+ angles: front, 3/4, profile, close/medium/full body,
   smile/neutral/pensive, signature pose) — the reference bank.
4. LoRA (rank 16–32, 20–50 images, rare trigger token) — for hundreds of
   images. **Reference-based anchoring is the 2026 standard for photoreal
   characters like the example persona**; LoRA stays the right call for stylized
   (non-photoreal) characters.

Practical order: lock one hero shot → build the 10-angle sheet with
`--cref {hero} --cw 50` (face features only) → train LoRA, captioning
everything EXCEPT identity so the token absorbs identity → test 50–100
images, require 80%+ same-person recognition → reject drifted images from
the bank, never feed them back in. Lock style too: fixed `--sref` palette
and lighting language in every prompt.

## Step 3 — Weekly cadence (after the 21-day warmup)

- Reels 50–60% (3–4/week, discovery), carousel 20–25% (1–2/week, saves),
  single photo 10–15% (1/week, world-building), stories daily (polls/Q&A).
- Reels: 7–15s sweet spot, hook in the first 3 seconds (50–70% drop off
  otherwise), captions ON (muted viewers), cut every 1.5–3s, loopable edit,
  1080×1920 minimum, no TikTok/CapCut watermarks.
- Ranking signals in order: watch time (70–90% completion) > DM shares >
  saves > early engagement. Design every reel to be worth DMing to a friend.
- Posting times KST: weekdays 11–13 / 19–21, weekends 9–11; re-personalize
  from Insights after 1–2 weeks. Never post at exactly the same minute daily;
  rotate the 3–5 hashtag set per post (hashtag cap is 5 since Dec 2025:
  2–3 niche <50k posts + 1–2 mid + 0–1 broad).
- Caption structure: hook in first 125 chars → story/value → ONE CTA
  (save / tag a friend / comment / follow-for-series). 80% value,
  20% promo.

### Hook-first edit rules (adopted 2026-10-23)

- Strongest frame at 0:00 — no fade-ins, logos, or slow starts. The end
  frame visually rhymes with the start frame so the loop is seamless.
- Flop recovery: if a reel underperforms, recut ONLY the first 2 seconds,
  swap the cover frame, and repost as a new reel — one variable at a time,
  so the result teaches whether the hook or the body failed.

### Trial Reels gate (adopted 2026-10-23)

- New formats and unproven hooks debut as **Trial Reels** (shown to
  non-followers only, off the main grid). Judge after 24–48h on completion
  rate and DM shares against the channel median: winners graduate to a
  regular post, losers get the 2-second recut or are dropped.
- Proven series formats may skip the trial only by explicit user decision.

### Weekly trend slot (adopted 2026-10-23)

- One slot per week is a current text-overlay trend format, selected with
  `ig-outlier-research`. Prefer original-audio formats (business-account
  safe); the format must map to a content pillar; log format + outcome in
  the weekly review.
- Starter candidates (Oct 2026): "Not all angels are in heaven…",
  "Money can't buy happiness but…", "Some people call me…".

### Handwritten hook layer

- `memo-handwriting` is the standard tool for reel start-frame hooks and
  carousel covers (anti-AI handwritten trend). Because custom covers
  cannot be set through web posting, bake the memo image in as the reel's
  start frame instead of supplying a separate cover file. In-image
  handwriting stays Japanese (visual layer); captions stay English.

### Smartphone vlog formats (GRWM) — active technique

- For vlog-style reels, use the smartphone-GRWM technique: 1st-person
  selfie lock (phone in her own hand, no tripod), intentional imperfections
  (mild shake, autofocus hunting, exposure drift, no beauty filter),
  diegetic sound only (no BGM), 30s beat structure (wake → prep beats →
  door). Full spec: video planning app skill #9 "Smartphone GRWM Vlog"
  (includes an example-persona application guide); canonical sample analyzed in your own research notes.
- Example series mapping: before-class prep (student) / outing outfit prep
  (fashion, affiliate-linkable) / heading-out-in-Tokyo (Tokyo life).
  Identity: the example persona's L1 hero lock as the reference. Dialogue in Japanese.
  Compliance per Step 1 (AI labels on, no fake experience claims).
- Structure update (2026-10-23): GRWM runs the storytime-hybrid form — a
  mini-story thread across the prep beats with the payoff in the final
  beat and one closing question; see `phone-shot-video` "Format updates
  integrated 2026-10-23" for the full spec, including the 12–15s
  reel-length variant.

## Scheduling option — MagicSync (evaluated 2026-10-05, not deployed)

- MagicSync (leamsigc/MagicSync, open-source, self-host via Docker) exposes
  its scheduler + content studio as an MCP server (18 tools + 4 resources)
  and a custom AI-assistant connector: an assistant can draft, schedule,
  publish, and analyze across 18 platforms incl. Instagram, with scoped
  (read-only or full) access and audit logging on every call.
- Fits the draft → human-approval → schedule pipeline: keep the Preconditions
  gate above (never publish/schedule without explicit authorization for that
  exact action); the connector's scoped access + audit log is the mechanism.
- Not deployed: needs a Docker host and an Instagram API connection (Meta
  app + tokens). User decision required before setup.

## Step 4 — Monetization stages

| Stage | Followers | Revenue source |
|---|---|---|
| Month 1–3 | 1K–3K | Affiliate links only (start anytime) |
| Month 3–6 | 5K–10K | Affiliate + first brand outreach (20 DMs → ~3 deals) |
| Month 6–12 | 10K+ | Recurring brand partnerships |

Korea affiliate default: Coupang Partners (base 3%, up to 15%; 24h cookie
on ANY purchase; payout on the 15th two months later; needs 30+ posts before
applying, final approval at ₩150k cumulative sales). With affiliate links,
the §Step 1 disclosures are mandatory.
Digital products (e.g. a Tokyo fashion guide PDF) are the high-margin small-
channel play; character IP goods come after 10K.

## Step 5 — Weekly review (30 min)

Track: net follower growth (target +3–5%/week early), reach per reel,
engagement rate (healthy: 4–6% at 1K–10K; <4% is a problem; sub-1K accounts
naturally underperform — that is not a content failure), 3-second views and
completion rate (<50% completion → redesign the hook), saves, DM shares,
story replies, bio-link clicks. Pick best/worst post weekly, write a
one-line cause hypothesis, and shift pillar weight toward what gets saved
and shared.

## Operating rules

- If this skill's checklist conflicts with the user's explicit instruction
  for a specific post, the user's instruction wins; note the deviation.
- Numbers that change (policy dates, payout thresholds, benchmark rates):
  re-verify against a current primary source before quoting them to the user.
  Mark estimates as estimates.
