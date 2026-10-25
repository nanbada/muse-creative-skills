---
name: "editorial-writing"
description: "Write, revise, and polish publishable text in a human voice with evidence discipline; layers Naver-blog-specific rules (home-feed targeting, publication guardrails) on top of the general method. Supersedes local-humanlike-writing and local-naver-blog-editor."
---

# Editorial writing

Merged from local-humanlike-writing (general method plus Korean fluency, 2026-10-02) and local-naver-blog-editor (Naver layer plus home-feed strategy, 2026-10-10). Supersedes both; search for either old name still finds this skill.

Trigger: whenever the user asks to draft, write, revise, or polish text other people will read. Blog posts, articles, social posts, newsletters, public docs. Private notes, chat replies, and internal documents stay concise and functional and do not trigger this skill.

## Build the evidence ledger

- Restate the reader question in one sentence before writing.

- Build a short ledger of claim | firsthand, official, community, or unverified | source plus date | limits.

- Check changing product facts against a current primary source and keep community reports as attributed anecdotes.

- Remove claims with no evidence or label them unverified. Never invent personal experiences, dialogue, screenshots, test results, dates, or outcomes.

- Never write to evade AI detection. Never claim the user wrote everything manually when assistance was used.

## Write in a human voice

- Start from the author's concrete obstacle and outcome, then the steps that mattered, the failures, and the limits.

- Use specific nouns and natural varied sentence lengths. Write connected paragraphs of two to four sentences with functional subheads. Use lists only for real steps or comparisons.

- Skip template intros, repetitive conclusions, excessive emoji, keyword stuffing, manufactured typos, and repeated hype words. Never force uniform paragraph length.

- Write first-person sentences only when the user's evidence supports them. Separate what was personally confirmed from what others reported. A conversational tone cannot repair unsupported facts.

- Scope personal outcomes as personal, reconcile contradictory claims into one scoped statement, match the title to the actual coverage, and verify the rendered output on desktop and ~390px mobile before declaring layout fixed.

- Disclose referral or affiliate benefit next to the code, mention it once, and tell the reader to verify current terms on the service's own screen. Never present a code as an access bypass.

- Use original images only with authorization and redact emails, codes, IPs, account IDs, and billing details. Write captions that explain the decision or error the image shows.

- End with who this helps and what remains unverified, not by repeating the introduction.

## Keep the Korean fluent

- Keep particles and endings intact. Restore endings when brevity turns a sentence into a noun pile.

- Avoid translated tone. Drop narrator adverbs that sound like a presenter.

- Never use an em dash in the body. Use commas or wa/gwa instead of the middle dot.

- Keep one ending style through a draft. Titles and outline items may use the plain form.

- Keep technical terms and product names in English and write general loanwords in Korean.

- Check these five items during the read-aloud pass before delivery.

## Apply the Naver layer for Naver blog posts

- Read the general sections above first, then apply these Naver-specific rules. On a conflict for a specific post, the user's explicit instruction wins; note the deviation.

- Drafting and revision are the default scope. Never publish, schedule, or edit a live post without explicit authorization for that exact post and destination URL.

- Stop and notify on any 2FA or CAPTCHA challenge. Never bypass it.

- Target the Naver AI home feed: trend topics, hook-style titles with angle variants, one sharp representative image, mobile-readable body text. Never promise ranking or cite invented algorithm rules. Never quote unverified revenue figures as fact. Strategy reference: your own Naver home-feed strategy notes.

## Run pre-delivery checks

- Verify factual support, first-person voice accuracy, chronology, links, privacy redactions, disclosure, mobile readability, and repeated phrasing.

- Read the draft aloud mentally once.

- Mark unverified checks honestly, for example with a note that it was not directly confirmed.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Ask the user the one or two questions that would most change the result, but only when the answer could genuinely flip the outcome.

- Record durable findings in memory or the goal workspace and record a new method lesson in the self-improvement learn log.