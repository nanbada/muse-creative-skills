# Muse Creative Skills

[한국어](README.ko.md) | English

Image & video production skills for AI agents (Muse, Claude Code, and
compatible assistants). Each skill is a `SKILL.md` plus its references —
install one skill or the whole collection.

## Install

```bash
# one skill
npx skills add nanbada/muse-creative-skills/image/photoreal-realness

# or clone everything
git clone https://github.com/nanbada/muse-creative-skills.git
```

## Starter pack (start here)

New to Muse? Install in priority order — see
[STARTER-PACK.md](STARTER-PACK.md) for the full ranking and rationale.

- **P0 — everyone first:** `productivity/voice-dump-dispatch`,
  `productivity/research-brief`, `productivity/deep-thinking`,
  `productivity/goal-tracker`, `productivity/method-capture`,
  `productivity/defuddle`
- **P1 — content creators:** `productivity/content-studio`,
  `productivity/editorial-writing`, `channels/character-channel-ops`,
  `channels/ig-outlier-research`, `channels/ig-caption-craft`,
  `channels/memo-handwriting`, `productivity/pulse`,
  `productivity/social-sourcing`, `channels/coupang-reviewer`,
  `channels/jp-sns-ops`, plus the `image/` and `video/` skills below
- **P2 — long-term ops:** `ops/PLAYBOOK.md` (recurring-job management,
  improvement harness, memory discipline, proof-of-done, read offload,
  routing policy, approval gates), `productivity/competitive-brief`,
  `productivity/seo-audit`

## Image skills (`image/`)

| Skill | What it does |
|---|---|
| `photoreal-realness` | "휴대폰샷" — intentional-degradation prompt blocks that make AI photos read as real smartphone snaps of real people. Four stages: snapshot philosophy, technical imperfection, facial asymmetry, human noise. |
| `pose-reference` | Pick a pose for character image generation from 8 anatomy reference sheets (133 poses). Select by situation/mood or at random, verify visually. |
| `character-consistency` | Keep one person's face, hair, and body consistent across image and video generation: face-photo anchor + fixed-block verbatim + role-labeled references + separate face/full sheets + faceless mannequin body standard + relative-edit ladder with auto-repeat + pixel measurement. First resort for any person generation. |
| `museum-editorial` | Paste-ready prompts for GPT Image 2.5 that produce museum-grade editorial posters — minimalist 9:16 vertical layouts with archival layers, in Korean or English. Verifies subject facts before composing. |
| `second-world` | Turn a photo into a "Second World" poster — vertical 3:4 canvas, upper half faithful photography, lower half ivory paper where one structure continues under new physical rules. |
| `doodle-overlay` | "고양이 손그림" / "귀여운 아이 손그림" / "손그림 낙서" — mixed-media art over a photorealistic photo: a giant white hand-drawn doodle character (cat or cute kid) interacting with real architecture and landscapes; the photo stays faithful. Overlay modules: handwritten text, doodle icons, doodle scatter, postcard, magazine cover lines, promo copy. |
| `comic-production` | "만화 제작" — 6-stage pipeline for consistent multi-panel AI comics: character lock, batch rendering, validation gates, targeted retries, post-render lettering. Distills 7 open-source comic projects. |
| `pencil-line-poetry` | "동양미 스타일" — tiny line-drawn characters (dot eyes, minimal features) living inside an oversized photorealistic natural world: dewdrops, petals, leaves, feathers as landscape. Fine lines + macro-nature mixed media, warm golden-hour light, poetic vertical compositions. Modes: tiny line world, glow lines, line over landscape, soft painterly. |

## Video skills (`video/`)

| Skill | What it does |
|---|---|
| `phone-shot-video` | "휴대폰으로 찍은 영상" — make AI videos feel shot on a real smartphone: 1st-person selfie lock, intentional imperfections (shake, autofocus hunting, exposure drift), diegetic sound only, GRWM 30s beat structure. |
| `photoreal-selfie-look` | Inject a photorealistic smartphone front-camera look into AI video prompts: beauty filter, grain, motion blur, focus breathing, rolling shutter, SNS compression artifacts. |
| `veo-vertical-clip` | Design Veo 3.1 native 9:16 vertical clip prompts + credit-aware production plan for Google Flow. |
| `place-video-prompter` | Paste-ready Korean video-production prompter for a real place (building, landmark, store, campus…) with strict realism guardrails. |
| `ad-video-automation` | Automate short product ad videos (15–20s, 9:16): concept research, hero image product lock, block drafts with review gate, code overlay for text/graphics/BGM. |
| `youtube-shorts-growth` | YouTube Shorts channel growth strategy: topic consistency + frame control, execution strategies, title/thumbnail patterns. |
| `plant-growing` | "식물 키우기" — plant-growth timelapse production: locked-environment stage-frame prompt series (seed→ripe) → Gemini Omni 1.1 Flash frame interpolation, or a 10-second quick mode → handwritten keyword overlays + rolling life-tip text for mass middle-aged/elderly audiences → 3–6 stills → seed/fertilizer link monetization. Species packs included. |
| `fashion-motion-video` | "옷입기 영상" / "패션 동작 영상" — turn a fashion photo + a shop detail-page link into a short fashion video: mannequin display image → 20s hourglass character conversion → start-frame approval → doll-mask face cover (88% size) → motion video with core-only white handwriting (product name, price, features) and background music only. New-product texture rule: express the fabric as brand-new, never washed/worn. Post text is minimal: 1–2 lines of vibe/situation + product name, fabric, colour + detail-page link. |

## Productivity skills (`productivity/`)

| Skill | What it does |
|---|---|
| `voice-dump-dispatch` | Turn a rambling voice memo or multi-task message into a numbered list, fan independent tasks out in parallel, return one compressed report. |
| `research-brief` | Evidence-disciplined research: primary sources first, every claim linked, uncertainty marked explicitly. |
| `deep-thinking` | Tiered reasoning: self-interview, Socratic probing, product teardown, recursive self-critique. |
| `goal-tracker` | Turn a goal into milestones and measure progress from evidence, never intentions. |
| `method-capture` | Save a pasted workflow, method, or SKILL.md text as a versioned skill file instead of letting it dissolve into chat history. |
| `defuddle` | Extract a page's main content as clean Markdown with metadata — a token-cheap alternative to a full page dump. |
| `pulse` | Take the pulse of any topic across Reddit, Hacker News, the open web, and X (default 30 days), with a cited briefing. |
| `social-sourcing` | Fetch X/Twitter and Reddit posts over plain HTTPS without login or API keys. |
| `competitive-brief` | Competitor research → positioning/messaging comparison, content gaps, opportunities, threats, battlecard takeaways. |
| `seo-audit` | Structured SEO audit — keyword research, on-page analysis, content gaps, technical checks, competitor comparison — with a quick-wins vs strategic action plan. |
| `content-studio` | Turn source material into channel-ready drafts without losing the original meaning. Drafts are automatic; publishing, sending, or scheduling always needs human approval. |
| `editorial-writing` | Write, revise, and polish publishable text in a human voice with evidence discipline; layers Naver-blog-specific rules (home-feed targeting, publication guardrails) on top of the general method. |

## Channel skills (`channels/`)

| Skill | What it does |
|---|---|
| `character-channel-ops` | Operate a virtual-character Instagram channel (fictional persona): launch setup, character-consistency workflow, weekly cadence, caption/hashtag playbook, growth tactics, monetization pipeline, compliance rules (AI labels, virtual-persona ad disclosure). |
| `ig-outlier-research` | Rank reels by outlier multiple (views ÷ the account's own median), name the hook formula each used, build a swipe file to shoot from. |
| `ig-caption-craft` | Write, lint, and humanize an Instagram caption end to end: 125-char visible cut, one ask, search terms, max 5 hashtags, machine-fingerprint removal with before/after detection proof. |
| `memo-handwriting` | Crumpled-notepad handwritten message composites over a background photo (9:16/4:5) — scroll-stopper hooks, reel covers, carousel covers. |
| `coupang-reviewer` | Draft human-sounding Korean Coupang product reviews from your own photos and product info, with a user approval gate before anything is published. |
| `jp-sns-ops` | Japan-side Instagram/SNS operations: early-20s colloquial captions, carousel templates, hashtag and timing rules. |

## Ops playbook (`ops/`)

| Document | What it covers |
|---|---|
| `PLAYBOOK.md` | Running an assistant long-term: recurring-job management (job cards, probation, monthly audit), improvement harness, memory discipline, proof-of-done, read offload, routing policy, approval gates. |

## Trigger words (Korean)

Some skills carry a Korean trigger word in their description — say it and
the assistant applies the skill:

- **휴대폰샷** → `photoreal-realness` (images)
- **휴대폰으로 찍은 영상** → `phone-shot-video` (videos)
- **고양이 손그림** / **귀여운 아이 손그림** / **손그림 낙서** → `doodle-overlay` (images)
- **만화 제작** → `comic-production` (images)
- **동양미 스타일** / **연필선 스타일** → `pencil-line-poetry` (images)
- **식물 키우기** → `plant-growing` (videos)
- **옷입기 영상** / **패션 동작 영상** → `fashion-motion-video` (videos)

## Notes

- Prompt blocks that go to image/video models are in English; notes to the
  user stay in the user's language.
- These skills never help pass an AI persona off as a real human for
  deceptive purposes (fake reviews, undisclosed identity). Keep AI-generated
  labels on per each platform's policy.

## License

MIT — see [LICENSE](LICENSE).
