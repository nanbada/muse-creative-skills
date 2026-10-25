---
name: "defuddle"
description: "Extract the main content of any web page as clean Markdown with metadata (title, author, published date). Use when research needs article text without the token cost of a full browser page dump. Token-cheap one-liner alternative to browser.open for articles."
---

# Defuddle

Article-extraction engine (MIT, by Stephan Ango / kepano — the engine behind Obsidian Web Clipper). Takes a URL or HTML, finds the main content, returns cleaned Markdown or HTML plus rich metadata. More forgiving than Mozilla Readability: keeps footnotes/code blocks/callouts, preserves math as MathML with LaTeX in `data-latex`, extracts author, published date, schema.org data, word count.

Verified working in this VM 2026-10-05 via `npx defuddle` (no install needed).

## When to use

- Research needs article text as clean Markdown for LLM input — cheaper than `browser.open` page dumps (no nav/footer/ads, no DOM noise).
- Need metadata in one call: author, published date, word count (useful for V/P/U source verification in research-brief).
- JavaScript-rendered pages: defuddle parses a DOM — combine with a saved HTML file from a browser task (`browser.spawn_task` can dump page HTML to /tmp), then parse locally.
- Prefer over heavy scraping when Firecrawl isn't needed (no API key, free, instant).

## CLI one-liners (no install)

```bash
# URL -> Markdown with YAML frontmatter (title, author, source, published date, word count)
npx defuddle parse https://example.com/article --markdown --frontmatter

# JSON: metadata + content in one call
npx defuddle parse https://example.com/article --json

# Single property (e.g. check freshness before a full fetch)
npx defuddle parse https://example.com/article --property published

# Local HTML file or stdin (e.g. HTML saved by a browser task to /tmp)
npx defuddle parse /tmp/page.html --markdown
cat /tmp/page.html | npx defuddle parse --markdown

# Debug a bad extraction
npx defuddle parse https://example.com/article --debug
```

## Operating rules

1. Research source hygiene: record the `published` date and `source` URL from frontmatter for every citation (feeds research-brief V/P/U checks).
2. If extraction returns junk or a paywall shell, fall back to `browser.open` or the firecrawl-style path — don't force it.
3. Never print the full fetched page into chat; summarize and cite. defuddle output is still page content — keep to relevant excerpts.
