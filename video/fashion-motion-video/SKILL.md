---
name: fashion-motion-video
description: Make a fashion motion video from a fashion photo plus a shop detail-page link — a 20s hourglass character wears the detail-page outfit, core info appears only as clean white handwriting, and the face is covered with a doll mask just before video. Use when the user asks for a fashion motion video, a mannequin fashion video, or a fashion video with product info (Korean triggers: 패션 동작 영상, 패션 영상, 마네킹 패션 영상, 옷입기 영상).
---

# Fashion Motion Video

Turn a fashion photo and a shop detail page into a short fashion video
plus a separate Instagram post text. The person in the video must wear
the outfit from the detail page, not a look invented from the photo
alone. Final version is fixed 2026-10-30, from the session that started
2026-10-30 18:50 KST with a mannequin plus fashion-photo info.

## Inputs (both required)

1. **Fashion image** — the outfit reference, front and back if available.
2. **Detail-page link** — the shop page for that outfit.

If either is missing, ask for it. Never invent a product name, price,
or feature. Fetch the detail page first and quote what it actually
says, with the fetch date, because prices can change.

## Stage interview cards (2026-11-03, mandatory management method)

The skill is managed stage by stage with user interview cards.
Full card set: `references/interview-cards.md`. Each stage ends
with a card — Show / Ask / Lock / Gate — and the next stage does
not start until the user answers or approves that card, unless
the user has already told Muse to proceed through the whole job.

- Two cards are always blocking, even in proceed-through mode:
  Card 1A Texture Lock and Card 3C Start Frame. No mannequin is
  generated before the texture card is locked, and no video is
  generated from an unapproved start frame.
- A locked item is not re-decided later. A card that fails stops
  that card; the job does not guess and move on, and a failed
  texture is never carried forward hoping the video zoom scene
  will rescue it.
- Interview cards are the management record for the job: what
  was shown, what the user chose, and what was locked. Keep that
  record in the job notes, not just in chat.

## Step 1 — Analyse the detail page

- Identify the exact outfit item(s) in the photo and match them to the
  detail page: garment type, colour, silhouette, and distinguishing
  details (for the 2026-10-30 example: black semi-bootcut flared
  trousers, hip flap pockets, detachable hip pads).
- Split the product information into two groups, and keep the split
  for the whole job:
  - **Video core, shown on screen:** product name, price, features
    only. Nothing else goes into the video handwriting.
  - **Post text only (2026-10-31 revision, supersedes the full-spec
    post):** do NOT dump colour, fabric, sizes, and lengths into the
    post. Interested viewers go to the detail page for details.
    The post is minimal: 1–2 lines only — the recommended vibe or
    situation ("where / when I would wear this"), plus product
    name, fabric, and colour, plus the detail-page link. See
    `references/post-template.md` for the revised layout.
- Reviews: only summarise popular reviews for the post if the user
  asks for them for that job, and only from reviews actually on
  the page. If there are no usable reviews, omit the review
  section — never fabricate a review, a rating, or a quote.
- Record the source link and the values you will use before you
  generate anything. See `references/post-template.md` for the split
  and the post-text layout.

## Step 1A — Texture Lock (2026-11-01, mandatory, the fix for
the worn/washed look)

Texture is locked BEFORE any image is generated, and the same lock
is carried through every stage. The worn look happened because
early stages guessed texture from a model selfie alone, while the
detail-page close-up was only used later, if at all. In card
terms this is Card 1A, a blocking gate: see
`references/interview-cards.md`.

1. **Text lock.** From the detail page, extract the material
   descriptors verbatim in substance: processing (e.g. brushed /
   shaggy), gauge, hand (thick, soft, voluminous, light), surface
   (e.g. down-like fuzz obscuring the knit loops, matte, no crisp
   rib or stitch definition), and colour. Record them in the job
   notes. Never invent a fibre percentage the page does not show.
2. **Image lock — select, do not guess.** Scroll the detail
   section in order and select texture close-ups by these
   criteria, in this order of preference:
   - Fabric fills the frame (flat surface, folded stack of
     colours, or a hand pressed into the fabric).
   - A texture label on the image (e.g. "Soft Texture").
   - NOT a model full shot, and NOT a model torso shot alone —
     those show fit, not fibre.
   Record each selected close-up by its position in the scroll
   order and by what it shows (colour, fibre length, fuzz
   density, stitch visibility), even when the file itself cannot
   be downloaded — see the limitation below.
3. **File lock, when a file exists.** If a texture close-up file
   is available — user upload, or a screenshot/save from the
   detail page — pass that file as a reference image in EVERY
   image stage: mannequin, character conversion, mask/start
   frame. This is proven: in the 2026-10-31 Whisper knit job,
   texture only improved once the user-supplied close-ups were
   passed as references. Never pass the texture file only at the
   video zoom stage.
4. **Description lock, when no file exists.** If no close-up file
   is available, do not pretend one is attached. Put the written
   texture lock from (1) and (2) verbatim into every prompt, and
   add the forbidden list: faded, matted, flattened, pilled,
   washed-out, worn-looking, thin, or crisp-ribbed fabric when
   the real texture is fuzzy.
5. **Limitation, verified 2026-11-01 (ABLY mobile).** The browser
   cannot reliably download detail stills from an ABLY mobile
   detail page: the close-ups appear as rendered visuals with no
   image element reference, link, or direct URL, so there is no
   download target. This is a page-exposure limitation, not a
   bot block or sign-in wall. Therefore the automatic path is
   (1) + (2) + (4), and the file path (3) needs a user upload or
   a user screenshot/save of the close-up. When the written lock
   alone still reads as worn, ask for that upload instead of
   regenerating the same guessed texture again.
6. **Video lock.** The video takes only the start frame as its
   image, so the start frame's texture IS the video's texture.
   The video prompt must carry the same texture lock, and its
   zoom scene must be described as a close-up of that same
   texture — never as a new texture invented at zoom time.

## Step 2 — Character (body locked, face free)

- Early-20s woman, hourglass silhouette: bust volume, slim waist,
  wide hips.
- Proportions: 7.5 heads tall, legs more than half of total height,
  so the legs read long. Measure by head count, not by a centimetre
  claim, when a check is possible.
- Hair: all hair behind the shoulders, so the top and neckline stay
  visible.
- Shoes: add shoes that match the outfit (for the example trousers:
  black shoes).
- Face: the face may change during generation. That is acceptable.
  Body shape is not negotiable — if the body changes, regenerate,
  do not accept it and move on.
- The character is fictional. Do not copy a real person's face or
  identity from a reference photo.

## Step 3 — Pipeline (in this order)

### A. Mannequin display image

A professional 3D display image first: one adult female model,
vertical composition, entire body fully visible, wearing the
detail-page outfit. This is the safe starting point when a direct
video request is refused (see Refusal fallback). Pass the Step 1A
texture reference (file or written lock) in this prompt — do not
leave texture to be guessed from the fashion photo alone.

### B. Character conversion

Convert the mannequin image to the Step 2 character:

- Remove the display pedestal. The model stands on the floor
  of the chosen background, no pedestal.
- Set the background from the Background pool below (Step 2A),
  randomly chosen unless the user names one. This replaces the
  earlier plain-background final version.
- Keep the outfit unchanged. Add matching shoes.
  Carry the Step 1A texture reference forward unchanged — a
  character conversion that loses the texture is a failed stage,
  even if the silhouette is right.
- Give the face a 20s-woman feel.
- Put all hair behind the shoulders.

### Step 2A — Background (random, researched)

Female customers judge an outfit by imagining themselves wearing
it in a real place, so the background answers "where does this
outfit belong?" A clean background is best for reading garment
detail, while a real place communicates lifestyle — use both
reasons when picking, and never let the background outshine or
cover the outfit.

Random pool (pick one per job, do not repeat the same background
for the next job unless the user asks for it, and record the pick
in the job notes):

- Clothing store / fitting area — purchase context, closest to
  the buying decision.
- Department store / shopping street — where the customer would
  actually shop and walk in the outfit.
- Park / garden — daily, relaxed, picnic and walk looks.
- Cafe — daily life, meeting friends, working alone; the most
  common daily-look preview place.
- Street / city walk — street style, relatable, shows the outfit
  in motion.
- Office / work — office and daily work looks.
- Home / living room — mirror and daily home looks.
- Plain studio / seamless background — detail-evaluation fallback
  when the outfit's colour, pattern, or texture must read without
  distraction.

Background rules, from fashion-photography guidance:

- Check contrast: a black outfit against a dark background loses
  its outline; a busy patterned outfit against a busy background
  loses readability. Pick a background tone that keeps the
  outfit's outline clear.
- No background line crossing the body awkwardly, no distracting
  sign or visible brand logo, no reflective surface or object
  appearing to grow from the head or shoulders.
- The background stays behind the model. It never covers the
  model, the outfit, or the side-margin handwriting.

### C. Start frame — approval gate

Present the converted image as the video start frame and confirm it
with the user before making the video, unless the user has already
told you to proceed. Never overwrite an original; every stage gets
its own file name.

### C1. Start frame must already show the full-body + handwriting
composition (2026-10-31, mandatory, all jobs)

The start frame is not a bare model shot. It must already contain
the composition that appears in the video at a full-body moment
(for the 2026-10-31 ribbon-wrap job: the 7-second full-body shot):

- Full body, entire outfit visible, same framing as that video
  full-body moment.
- Core handwriting already on the frame, in the side margins:
  product name, price, features only, white handwriting, never
  covering the model or the outfit.
- Doll mask already applied (Step D), so the start frame is the
  exact first frame of the video, not a pre-mask draft.
- If the video's full-body + handwriting composition changes,
  update the start frame to match it — do not leave the start
  frame as a different composition.

### D. Doll mask — last step before video

Cover the face with the doll mask the user supplied (2026-10-30:
a white cat-face doll mask, called "나비인형" by the user):

- Size (2026-10-31 revision 2): 88% of the original large mask
  size. This supersedes both the 100% original size (2026-10-31
  revision 1) and the 70% size (2026-10-30). Centre it on the eyes,
  nose, and mouth.
- Hair behind the shoulders stays visible at the sides.
- The mask is applied to create the start frame (Step C1), just
  before video production, not earlier in the pipeline, so
  earlier stages can still be checked without it.

### D1. New-product texture (2026-10-31, mandatory)

The outfit in the video must read as a brand-new product the
customer wants to buy, never as worn several times or washed
dozens of times. This section is now executed through Step 1A
Texture Lock, not by a single prompt line:

- Express the texture to fit the material: for knit, fluffy,
  voluminous, soft (뽀송뽀송), crisp shaggy hair, vivid colour —
  use the detail page's fabric close-up as the texture reference
  when one exists. When the close-up reads cloud-like and soft,
  lean into a cotton-candy softness (2026-10-31, Whisper knit),
  not a flat or matted finish.
- The texture reference (file or written lock) must be present
  in mannequin, character, mask/start frame, AND video prompts.
  A texture that appears only in the video zoom scene does not
  fix the other scenes.
- Forbid, in every prompt: faded, matted, flattened, pilled,
  washed-out, or worn-looking fabric.
- If a generated frame reads as washed/worn, regenerate the
  texture — do not accept it and move on to video.

### E. Video

Pick one motion, or let the user pick, from this set — the set is
randomisable, not a fixed sequence:

- 360-degree rotation: the model turns, the camera orbits like a
  drone shot, or both at once. A full 360 is not required: a video
  that lets the viewer judge the outfit through the model's movement
  is acceptable.
- Natural movement and model motion that shows fit, drape, flare,
  and pockets.
- Product zoom in and zoom out on details (fabric, pocket, flare,
  hem).

Audio: no narration voice. Background music only, exciting in tone.
Use music that is licensed for the intended use; do not use a
copyrighted track without permission.

## Step 4 — Handwriting on video (핵심정보 손글씨)

Use the named template `핵심정보 손글씨` (core-info handwriting:
product name, price, and features only, in pretty white
handwriting directly on the video, side margins only):

- Pretty white handwriting plus doodles, directly on the video.
  No paper panel, no memo-paper composite.
- Doodles: outfit-related drawings only.
- Placement: side margins only. Never cover the model or the outfit
  with a text panel. In the image stage the split was left = bottom
  info, right = top info; in the video stage only the core 3 items
  are shown.
- Content: product name, price, features only, cleanly, without
  overloading the screen.
- Duration: keep the handwriting visible to the end so the viewer
  has time to read it, or let it disappear briefly in the middle
  and reappear. Both are acceptable (2026-10-31: disappearing in
  the middle and reappearing is allowed). In either case the
  handwriting must be present on the first frame and again at
  every full-body moment, so the start frame and the video's
  full-body shot match.
- If Korean handwriting comes out garbled, simplify to the core
  3 items and regenerate the handwriting layer. Do not add extra
  explanatory text to compensate.

## Step 5 — Post text (separate from the video)

Write the post text from `references/post-template.md` (2026-10-31
revision): minimal, 1–2 lines — recommended vibe/situation, plus
product name, fabric, and colour, plus the detail-page link.
Full specs live on the detail page, not in the post. The
popular-review summary is no longer a standing post section; add
it only if the user asks for it for that job.

## Refusal fallback (do not retry the denied request)

If a video (or image) generation is refused:

- Do not repeat the same request, with changed arguments, through
  another tool or endpoint, in order to bypass the refusal.
- Report plainly that it could not be generated. Do not speculate
  about what triggered the refusal.
- Step back internally along the pipeline instead: mannequin
  display image, then 20s-character conversion, then video
  conversion from the approved start frame.
- Offer a genuinely different, safer direction and wait for the
  user's decision before generating it.

## QA before delivery

Use `references/qa-checklist.md` and check, at minimum: outfit
matches the detail page, body proportions are maintained, the
mask covers the face, handwriting shows core only and stays
readable, no narration is present, background music is present,
zoom shows product details, and no info panel covers the model
or the outfit. Video playback in this environment cannot prove
motion, mask persistence, or audio — say so plainly and ask the
user to check playback for those points, rather than claiming a
playback result you did not see.

## Recommended additions (from the 2026-10-30 session)

These were not in the user's original list, but they close gaps
that appeared during that session:

- **Start-frame approval gate (Step 3C).** Every video in the
  session that went wrong went wrong from an unapproved frame.
- **Price-date note.** Always note the date the detail page was
  fetched; re-check the price before posting, because shop prices
  change.
- **No fabricated reviews.** Review summaries come only from
  reviews actually shown on the detail page.
- **Music licensing.** "Exciting background music" is not a
  licence. Use royalty-free or otherwise licensed music for any
  video that will be posted or monetised.
- **Mask asset record.** Keep the user-supplied mask file path
  with the job. Do not substitute a different doll face, and do
  not reuse the mask to cover a real person's face.
- **Stage files, never overwrites.** Mannequin, character,
  start frame, and video each keep their own file, so a later
  correction does not destroy an approved stage.
- **Handwriting garble rule.** Korean handwriting in generated
  video is the most fragile layer. When it garbles, cut text,
  do not add text.
