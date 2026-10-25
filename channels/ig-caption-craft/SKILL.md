---
name: "ig-caption-craft"
description: "Write, lint, and humanize an Instagram caption end to end; 125-char visible cut, one ask, search terms, max 5 hashtags, machine-fingerprint removal with before/after detection proof. Supersedes local-ig-caption-lint and local-ig-humanize."
---

# IG caption craft

Merged from local-ig-caption-lint (structure plus caption.py) and local-ig-humanize (humanize.py, detect.py, slop.json), both ported 2026-10-14 from Jakeschincariol/instagram-agent-skill (MIT). Supersedes both; search for either old name still finds this skill.

Trigger: when the user asks to write or check an Instagram caption (Korean trigger: 캡션 작성, 캡션 검수) or when text sounds like AI (Korean trigger: AI티 제거, 인간화).

## Shape the caption

- Decide the caption's job first and say which. Job A: the video already hooked them, so the caption carries the ask, the context that makes the ask make sense, and search terms. Job B: the caption is the content, so line one is the hook, concrete and short, cut at a cliff.

- Keep line one within 125 visible characters. Never open with a greeting, hashtag, or emoji.

- Write two to six short paragraphs with one blank line between them. Put search terms in the body as human sentences, not a hashtag block.

- Never put a link in the caption; links are not clickable.

- Make exactly one ask: comment a keyword, save, or DM. Keyword asks need a typeable single word.

- Keep hashtags to five at most on their own line at the end. Cut generic tags that describe nothing.

- Keep emoji as punctuation, not decoration. Add alt text for carousels and photos.

- Stay under 2,200 characters. Short captions that earn the tap beat long ones that do not.

## Strip the machine fingerprint

- Run the humanize tooling on every draft, always. Never eyeball it.

- Run detect before and after so the delta is proven, not claimed.

- Fix invisible characters, typography, and slop lexicon words per the tool report. Keep slop.json current when a new tell appears in the wild.

- Remember the tools cannot fix voice, rhythm, or truth. Read the result out loud. For your channel, the caption voice in your notes is the target; this skill checks structure, never voice.

## Run the loop

- Draft the caption, then run the humanize tooling on it.

- Run the caption linter with the search keywords, fix every FAIL, and decide every WARN out loud.

- Deliver the copy-ready block plus a receipt: job, visible characters, ask, hashtags, search terms, linter status.

- Post nothing. The user pastes it.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Write captions in your channel's default language. The jp-sns-ops early-20s colloquial Japanese style applies to Japan-targeted accounts.

- When a caption keeps failing the linter, shorten the ask or split the post instead of stuffing more in.
