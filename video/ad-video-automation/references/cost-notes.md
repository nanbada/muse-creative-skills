# Cost notes — ad-video-automation (2026-10-09)

All numbers carry a date stamp. Re-check before quoting to a client.

## Google Flow (default path, user is Google AI Pro as of 2026-10)

- 1,000 credits/month + 50/day free, no rollover. 1080p upscale free for subscribers.
- Lite 10 (drafts) / Fast 20 (main) / Quality 100 (hero/finals).
- 17s sample budget: 5 blocks × Fast 20 + 3 finals × Quality 100 ≈ 400 credits.
- No public generation API → semi-auto: Muse plans, human generates in Flow.

## Seedance 2.5 (opt-in, paid)

- Official: ByteDance Seed API (may require review). Third-party: Kinovi, LaoZhang, Muapi (pay-as-you-go, no waitlist reported).
- Draft Mode (2026-09): 480p cheap draft → re-inference to 1080p referencing draft ID (not plain upscale). 57–77% cost cut vs blind high-res sampling.
- Kinovi pricing: 480p $0.12/s, 720p $0.27/s, 1080p $0.30/s (with video reference). Muapi: from $0.60/s.
- ~$5–10 per 17s ad at 1080p.
- Risk: MPA cease-and-desist pressure on ByteDance (2026-07, unresolved). Prefer Veo/Flow for commercial work.

## GPT Image 2.5 (opt-in, paid)

- Released 2026-09-08. API models: `gpt-image-2.5-flare` (speed) / `gpt-image-2.5-sunburst` (precision editing).
- Pricing: $5/1M text input, $8/1M image input, $30/1M image output tokens. ~$0.006–0.211 per 1024² image.
- 2 hero images < $0.50. C2PA + SynthID provenance on outputs.
- Requires OpenAI API key + payment → user approval first.
