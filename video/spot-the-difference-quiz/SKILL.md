---
name: spot-the-difference-quiz
description: Build a complete YouTube-optimized spot-the-difference quiz package from one scene idea: problem card, answer cards, Shorts video with the answer revealed inside (Medium 30s / Hard 28s), long-form problem set, captions, and an episode tracker. Medium = 3 differences, Hard = 5 differences, Easy excluded. Use for 틀린그림찾기, 틀린그림찾기 쇼츠, 틀린그림찾기 유튜브, spot the difference quiz, quiz Shorts 제작.
---

# Spot the Difference Quiz (YouTube-Optimized)

> v1.0.2 — updated 2026-11-03: simplified art style + large difference targets; one owned acoustic BGM (looped long-form, random sections for Shorts).
> v1.0.1 — updated 2026-11-01: random BGM per episode, no consecutive repeat.
> v1.0.0 — public release 2026-11-01. Sanitized for public use from the
> local v0.4.2 standard: channel-specific paths, channel IDs, and episode
> history are generalized; the production rules are unchanged. Where this
> skill and an older local patch note disagree, this version wins.
>
> Resolved here (previously scattered or contradictory):
> - Countdown is ONLY the title-end badge (radius 48, Fredoka 54). The
>   divider circle (radius 85, font 72) and the center-screen countdown
>   are both superseded and must not be used.
> - Answer sound effect: NONE. The ding is removed entirely.
>   Answer circles appear one at a time in silence over the BGM bed
>   only. The loud original ding, the first soft ding, soft2, and
>   soft3 are all superseded — do not use any ding, bell, or chime
>   for answer reveals.
> - Long-form per-problem counts (Medium 3 / Hard 5) are confirmed, not an
>   interpretation. The "not yet confirmed" note in v0.3.x is removed.
> - Title number is orange #C65A1E, not red. The "big red N" checklist
>   wording in v0.3.x is corrected.
> - The title-end magnifier (v1.8) was removed in v1.9. No magnifier on
>   any quiz card.
>
> History: optimized 2026-10-31 from upstream
> `cherry12002/muse-skill` (`spot-the-difference-quiz`). This public
> version is the reusable YouTube production standard built from that
> original plus production rules proven in a daily series.

## Purpose

Build a complete YouTube spot-the-difference quiz package from one scene
idea: a problem card, answer cards, a Shorts video with the answer
revealed inside the video, captions, and an episode tracker. One Short
answers one question only. Nothing in this skill depends on a specific
account, tool, or paid service. Follow the sections in order and do not
skip the verification steps.

## What good looks like (YouTube optimization)

- The first frame already tells the viewer what to do. Title, the two
  pictures, and the footer carry the whole video with no narration needed.
  The Shorts cover is the problem card, so the problem card must work as
  a thumbnail: title readable, both pictures visible, nothing covered.
- One Short answers one question only. The viewer compares two pictures
  and finds the differences before the timer ends, then the video itself
  reveals the answers in order, one at a time.
- Every difference is obvious once pointed out, but not obvious at first
  glance. If a viewer needs a magnifier, the difference is badly designed.
  Target real search time is at least 30 seconds: a first viewing inside
  the video's find window should not be enough; pause and replay are
  expected. That pause/replay behaviour is the retention loop, not a flaw.
- The user's eye is the final difficulty and likeness judgment. If a
  production label and the user's reading disagree, adopt the user's
  reading and correct the label.
- Comments are part of the format: viewers post "Found it!", ask for a
  hint, and count how many they spotted. Design the caption and the
  reply rules to feed that loop (see Production steps, step 10).

## Format standard

- **Card size:** 1080 by 1920. Panels 940 by 627 at x=70, upper panel
  y=170, lower panel y=820; separator line at y=1470; footer at font 46,
  ending about 385 pixels above the bottom edge.
- **Title (series identity, identical on every card except the number):**
  background cream #FDF6E9; font Fredoka Bold (rounded bold, OFL,
  weight 700; supply the Fredoka font file).
  Write FIND in black, then the number matching the difference count in
  orange #C65A1E, then DIFFERENCES in black. Never use the old rainbow
  FIND + red number composition — it looks like other YouTube content.
  No magnifier on any quiz card.
- **Footer:** stars plus difficulty in black, the phrase in orange
  #C65A1E. Stars are drawn with DejaVu Bold, because Fredoka has no star
  glyphs. Problem footer: `★★☆ MEDIUM · Can you find all 3?` (number
  matches the count). Answer footer: `★★☆ MEDIUM · How many did you spot?`
  Never reuse the problem footer on an answer card — the problem is over.
  Footer lines are in `references/captions.md`.
- **Shorts video:** 9:16, 1080 by 1920, 30 fps, H.264, AAC. Problem
  15 seconds (5 seconds with no timer, then countdown cards 10 to 1,
  one per second) + answer announcement 3 seconds + answers, circles
  added one at a time with no sound effect. Answer
  segment: Medium 12 seconds (4 seconds per difference, total 30
  seconds), Hard 10 seconds (2 seconds per difference, total 28 seconds).
- **Long-form video:** 5–8 problems per episode. Per problem, a 60-second
  find limit, then the answer, then the next problem. Per-problem counts
  are Medium 3 / Hard 5. Hard answer segment is 15 seconds per problem.
  Long-form upload time is 12:00 America/New_York (lunch), alternate days.
- **Countdown (only this form):** a Warm Grey #8B7E6E badge, radius 48,
  white Fredoka 54, fixed at the end of the title, with the title
  position unchanged from the problem card. Nothing overlays the two
  pictures — never a center-screen timer, never a divider timer, never
  any element over a picture. A divider countdown could cover a
  difference area, so it is banned, not just discouraged.
- **Answer announcement card (common to all content, no count shown):**
  an announcement card with your channel name on top, then
  "Eagle eyes? Let's see! / Time to reveal the answers!"
- **Answer sound effect: NONE.** No ding, bell, or chime at answer
  appearances. Answer circles appear one at a time over the BGM bed
  only. This replaces every earlier ding rule (original, soft, soft2,
  soft3) — all are superseded and must not be used.

- **Background music:** a bright, bouncy quiz bed under the whole Short,
  made by looping a short section infinitely (`--music-loop`) — bouncy
  piano or marimba melody, light cute rhythm, swing/jazz or bright vlog
  feel. Mix: BGM bed only, music at -16 dB, fade-in 1 second, music
  fade-out 2 seconds. No ding track, no ducking (there is nothing to
  duck to). Use an original
  loop to avoid any licensing or other-channel asset reuse. If you use a stock track instead, verify the actual downloaded file
  and its license before publishing. Never report an unverified download
  as a file.
- **BGM selection (per episode, standing rule):** use one good owned
  acoustic track as the standard BGM. Long-form loops the full track
  to the video length; Shorts use one randomly picked section of the
  same track per episode, excluding the immediately previous episode's
  section. Record the chosen track/section in the episode tracker.
  A single fixed synthesized loop for every episode is superseded.
- **Art style:** anime watercolor, hand-painted with soft shading — and
  other watercolor animation styles may vary per episode (Ghibli-style,
  pastel watercolor, sketch watercolor). Flat vector with thick black
  outlines is excluded as the default: it looks too similar to existing
  spot-the-difference content. Keep the linework BOLD AND SIMPLE: no
  dense, finely detailed line rendering. Shapes read at a glance, with
  generous whitespace — a viewer must be able to scan the scene in
  seconds, especially for Shorts. Difference targets are LARGE:
  broad-area color changes and large objects, never thin lines, small
  patterns, or blurry textures.
  Do not put people in the scene unless the scene genuinely needs them.
- **Safe zones (YouTube Shorts UI):** keep all text, difference marks,
  and key elements out of the bottom 340 pixels and, for Shorts, out of
  the right ~120 pixels action rail. Check top-UI collision on a phone
  preview before posting — if the title collides, add top padding rather
  than moving the title.
- **Language:** English-optimized main title plus Japanese and Chinese
  support; landmark items also add that country's language (Eiffel Tower
  → French, Colosseum → Italian, Sagrada Família → Spanish). English main
  title + multilingual description/tags. AI disclosure ON, not made for
  kids.
- **Files per quiz:** one problem card image, timer cards, one answer
  card image per step (circles accumulating), one announcement card, and
  one Shorts video. Name them clearly, for example
  `quiz-01-kitchen.png`, `quiz-01-kitchen-answer.png`,
  `reel-quiz-01-kitchen-30s.mp4`.

## Difference design rules

- **Count by difficulty:** Medium = 3, Hard = 5. For long-form this
  applies per problem.
- **Mechanisms only:** color change; a clear object disappears (the
  object must be unmistakable, not a background twig); a count change in
  the 2 to 4 range. Use any combination that reaches the count.
- **Banned at every difficulty:** subtle tone or brightness shifts, small
  detail changes, density changes, anything arguable after the answer is
  revealed.
- **Placement and difficulty:** Medium or above only — Easy is excluded.
  Differences sit at edges and corners, are mid-size, and the scene is
  detailed enough to take time to scan. Hard uses the same mechanisms
  only, toward edges and corners, with a mid-size color-change target.
  Never make a Hard episode by breaking the ban list.
- **Banned as "too easy":** a large central object plus a large
  foreground object combination (for example: hot-air balloon
  color change plus foreground bicycle disappearance, solved in
  10 seconds).
- **Visibility (audience: students through seniors):** never make a
  difference a tiny, blurry, far-landscape detail. Make the target large
  enough, colour-distinct, or placed forward enough to be clearly visible
  once circled, including to senior viewers. All problems need not be
  senior-focused, but no difference may be invisible to a senior viewer
  once it is pointed out. A distant, small bird in the sky is the
  counter-example: too small and too far to see clearly.
- **Scene identity:** keep the background and layout identical in both
  pictures. Only the planned differences change.

## Production steps

1. Pick a topic. Item priority: (1) iconic world film/drama scenes, only
   at a copyright-safe level; (2) world landmarks; (3) fun everyday
   scenes. Copyright rules: never copy original stills, characters,
   distinctive costumes, logos, or music; reproduce only a generalized
   composition/situation as an original illustration; never reproduce a
   specific character's distinctive appearance; if a scene cannot be made
   safely, substitute the next-priority item. Never repeat a topic
   already posted in the same series — check the episode tracker
   (`references/episode-tracker.md`) first. Number the series so viewers
   can collect episodes.
2. Generate the base illustration with the prompt in
   `references/prompts.md`. Check that the scene is complete and detailed
   before moving on.
3. Generate the B version by editing the base illustration with the edit
   prompt. Change only the planned differences. Nothing else may move,
   recolor, appear, or disappear.
4. Run the QA gate below. If anything else changed, regenerate the B
   version. Never patch a bad pair by hand-waving.
5. Build the problem card. Stack the two illustrations, add the FIND N
   DIFFERENCES title on top, and add the problem footer line at the
   bottom.
6. Build the answer cards. Copy the problem card, replace the footer with
   the answer footer, and draw a red circle plus a number on each
   difference, added one at a time in the video (one card per step,
   circles accumulating). Check every circle sits exactly on its
   difference.
7. Assemble the Shorts video. Problem 15 seconds (5 seconds still, then
   the title-end countdown badge cards 10 to 1), then the answer
   announcement card 3 seconds, then the answer cards in order with no
   sound effect. The answer is revealed inside the video
   — there is no separate answer post.
8. Run the full quality checklist below. Fix and re-verify the whole
   package if anything fails. Never post a package with a known defect.
9. Post the Shorts video. At the crop step choose the Original ratio and
   check the full frame is visible before sharing. Upload JPG or PNG
   files — the web uploader rejects WebP, so convert first if needed.
   Verify the channel ID before publishing, and verify actual publication
   on the public page afterwards — never report "published" unverified.
   Verify your own channel ID before publishing, and never upload an
   episode to the wrong channel.
10. Reply to comments. Congratulate viewers who found them all. When
    someone comments asking for a hint, give exactly one location hint
    for one difference. Never give the full answer in a hint reply.

### Execution routes

- Image generation and image edit: the built-in media pipeline (base
  image, then edit call for the B version). Any image model works; the
  prompts in `references/prompts.md` are model-agnostic.
- Card assembly and answer circles: deterministic code overlay (PIL or
  equivalent). Text and circles are never generated inside the image model.
- Video assembly: `ffmpeg-skill` (or equivalent ffmpeg scripts) for all
  mechanical video editing — problem card still 5 seconds, then one
  title-end countdown badge card per second (10 to 1, Warm Grey badge as
  specified above, code overlay on the problem card), then the
  announcement card 3 seconds, then the answer cards in order, joined
  with no transitions, plus a looped BGM bed as specified above and no
  answer sound effect.
  Never overwrite source files.
- Publishing: a video that passes the QA gate may be published. A video
  that passes the eye check but fails only the pixel map enters a
  user-review hold (see QA gate below) and is published only after the
  hold expires without a veto, or after an explicit approval. A video
  that fails the eye check must NOT be published: regenerate or hold
  and report. Keep a separate per-upload approval gate unless
  auto-publish has been explicitly pre-approved for the series.

## QA gate (deterministic, before the eye check)

Run these in order. A pair that fails any step is regenerated, not repaired.

1. **Pixel-diff.** Align A and B, compute a thresholded difference map.
   It must show exactly N connected change regions, matching the N
   planned differences (N = 3 for Medium, 5 for Hard). An extra region is
   the most common failure — the edit almost always changes something
   unplanned. (Example measurement settings: threshold 30, minimum
   component 500 px.) **Pixel-gate review rule (settled 2026-11-01):** if the eye
   check, count check, and safe zones pass but only the pixel map fails,
   the video is NOT published immediately. It enters a 3-day user-review
   hold: record the hold start date in the tracker and run log, and
   report the video plus the pixel report to the user. If the user does
   not veto within 3 days, auto-publish it on day 3 (a later daily run
   checks the hold queue and publishes it). A video that fails the eye
   check itself is NOT eligible for this rule — regenerate or hold it
   only. An earlier explicit user approval publishes it sooner.
2. **Object count.** List every countable object in both pictures and
   confirm only the planned count change differs.
3. **Target check.** Confirm the color-change target and the missing
   object, and confirm nothing else moved or recolored.
4. **Eye check at full resolution.** Never judge a pair from a thumbnail.
   Confirm each difference is obvious once pointed out, that the answer
   circles sit exactly on their differences, and that no difference is a
   tiny far-landscape detail (senior visibility rule above).

## Quality checklist (final pass)

- Problem card: title reads FIND, orange number, DIFFERENCES. Panels
  940 by 627 as specified. Problem footer line is correct. No text or
  key element sits in the bottom 340 pixels or the right ~120 pixels.
- Timer cards: title-end Warm Grey badge (radius 48, Fredoka 54),
  title position unchanged from the problem card, no element over either
  picture.
- Answer cards: every red circle plus number sits exactly on a real
  difference. There are exactly N marks on the final card, added one at
  a time. Answer footer line is correct (not the problem footer). No
  stray marks or margins.
- Pair: QA gate above passed in full (or 3-day hold, if only the pixel
  map failed).
- Shorts video: Medium 30 seconds / Hard 28 seconds, problem 15 seconds
  with the title-end countdown badge, announcement 3 seconds, answers in
  order with no sound effect, BGM bed throughout.
  Transitions are clean.
- Post: crop ratio is Original and the full frame is visible. Files are
  JPG or PNG. Caption lines and hashtags match `references/captions.md`.
  Channel ID verified before publishing and publication verified on the
  public page afterwards.

## Common mistakes

- Designing a fourth accidental difference. Verify the pair instead of
  trusting the edit.
- Making differences subtle to raise difficulty. Subtle is not hard, it
  is unfair. Raise difficulty with placement and target size, never with
  subtlety.
- Putting the countdown over a picture or on the divider. It can cover a
  difference area; it belongs only at the end of the title.
- Reusing the problem footer on the answer card. The problem is over —
  use the answer footer instead.
- Putting text in the bottom band or the right action rail. The Shorts UI
  covers it and viewers miss the timer or the title.
- Putting a magnifier on the title. It was tried in v1.8 and removed in
  v1.9; the title ends with the countdown badge only.
- Changing captions and hashtags at the same time as the format. Change
  one variable at a time or you cannot tell what moved the numbers.
- Reporting an unverified download as a file. A download button that
  changed to "Downloading…" is not a verified file.

## Variations

- Adapt the language, not the structure, for another audience. Captions,
  footer lines, and the guide comment translate directly. Keep the title
  format, the mechanisms, and the in-video answer structure unchanged.
- Senior audience: see `references/variants.md` (large elements, high
  contrast, large countdown badge, senior visibility rule).
- Superseded (v0.2.0 Instagram format, no longer the default): 13-second
  reel (3-second hold + 10-second countdown + loop), no answer in the
  reel, and a separate answer carousel 12 hours later. Also superseded:
  the divider countdown, the title magnifier, and every answer ding
  (original, soft, soft2, soft3) — there is no answer sound effect.
- Series discipline beats bursts. Fixed days and fixed times build return
  visits. Start the posting run early enough that the post lands on the
  hour.
