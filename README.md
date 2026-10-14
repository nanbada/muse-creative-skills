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

## Image skills (`image/`)

| Skill | What it does |
|---|---|
| `photoreal-realness` | "휴대폰샷" — intentional-degradation prompt blocks that make AI photos read as real smartphone snaps of real people. Four stages: snapshot philosophy, technical imperfection, facial asymmetry, human noise. |
| `pose-reference` | Pick a pose for character image generation from 8 anatomy reference sheets (133 poses). Select by situation/mood or at random, verify visually. |
| `museum-editorial` | Paste-ready prompts for GPT Image 2.5 that produce museum-grade editorial posters — minimalist 9:16 vertical layouts with archival layers, in Korean or English. Verifies subject facts before composing. |
| `second-world` | Turn a photo into a "Second World" poster — vertical 3:4 canvas, upper half faithful photography, lower half ivory paper where one structure continues under new physical rules. |
| `doodle-overlay` | "고양이 손그림" / "귀여운 아이 손그림" — mixed-media art over a photorealistic photo: a giant white hand-drawn doodle character (cat or cute kid) interacting with real architecture and landscapes; the photo stays faithful. Overlay modules: handwritten text, doodle icons, postcard, magazine cover lines, promo copy. |

## Video skills (`video/`)

| Skill | What it does |
|---|---|
| `phone-shot-video` | "휴대폰으로 찍은 영상" — make AI videos feel shot on a real smartphone: 1st-person selfie lock, intentional imperfections (shake, autofocus hunting, exposure drift), diegetic sound only, GRWM 30s beat structure. |
| `photoreal-selfie-look` | Inject a photorealistic smartphone front-camera look into AI video prompts: beauty filter, grain, motion blur, focus breathing, rolling shutter, SNS compression artifacts. |
| `veo-vertical-clip` | Design Veo 3.1 native 9:16 vertical clip prompts + credit-aware production plan for Google Flow. |
| `place-video-prompter` | Paste-ready Korean video-production prompter for a real place (building, landmark, store, campus…) with strict realism guardrails. |
| `ad-video-automation` | Automate short product ad videos (15–20s, 9:16): concept research, hero image product lock, block drafts with review gate, code overlay for text/graphics/BGM. |
| `youtube-shorts-growth` | YouTube Shorts channel growth strategy: topic consistency + frame control, execution strategies, title/thumbnail patterns. |

## Trigger words (Korean)

Some skills carry a Korean trigger word in their description — say it and
the assistant applies the skill:

- **휴대폰샷** → `photoreal-realness` (images)
- **휴대폰으로 찍은 영상** → `phone-shot-video` (videos)
- **고양이 손그림** / **귀여운 아이 손그림** → `doodle-overlay` (images)

## Notes

- Prompt blocks that go to image/video models are in English; notes to the
  user stay in the user's language.
- These skills never help pass an AI persona off as a real human for
  deceptive purposes (fake reviews, undisclosed identity). Keep AI-generated
  labels on per each platform's policy.

## License

MIT — see [LICENSE](LICENSE).
