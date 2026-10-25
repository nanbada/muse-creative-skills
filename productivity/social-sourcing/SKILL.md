---
name: "social-sourcing"
description: "Fetch X/Twitter posts and Reddit posts over plain HTTPS without login or API keys. Use when a task needs the text of a specific X post, or to search Reddit posts by subreddit and keyword. Token-cheap alternative to browser automation."
---

# Social Sourcing

## Purpose
Look up social posts for research (blog sourcing, case collection) without a browser session: single X posts via the FxTwitter public API, Reddit search via the Arctic Shift archive API. No login, no API keys, stdlib only.

## Tooling
Helper: `bin/social_fetch.py` (Python 3, stdlib only).

```bash
# One X post, human-readable (text + author + stats + URL)
python3 bin/social_fetch.py xtext "https://x.com/<handle>/status/<id>"

# One X post, full JSON
python3 bin/social_fetch.py x "https://x.com/<handle>/status/<id>"

# Reddit search: titles + scores + permalinks
python3 bin/social_fetch.py reddit <subreddit> "<query>" [limit]

# Reddit search with post bodies (first 600 chars)
python3 bin/social_fetch.py redditself <subreddit> "<query>" [limit]
```

## Operating Rules
1. X search-by-keyword is not supported on this path (X requires login for search). Discover candidate post URLs with `browser.search` first, then fetch their text here.
2. Reddit via Arctic Shift is rate-limit sensitive: leave minutes between calls; on repeated 422s, back off and fall back to `browser.search`.
3. Attribute everything fetched: "사용자 후기에 따르면" / "보도에 따르면". Never present a social anecdote as a verified fact.
4. Do not fetch private/deleted posts; the API returns an error for those — report it, don't work around it.
