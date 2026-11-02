# Interview cards (fashion-motion-video)

Stage-by-stage user interview cards, 2026-11-03. This is how the
skill is managed, not an optional chat style: each stage ends with
a card, and the next stage does not start until the user answers
or approves that card — unless the user has already told Muse to
proceed through the whole job, in which case only the two blocking
cards (Texture Lock and Start Frame) still stop the job.

## Card format (every card)

- **Stage:** name and pipeline step.
- **Show:** exactly what Muse presents (image, text lock, or list).
- **Ask:** 1–3 short questions, with concrete options where a
  choice exists. Never ask an open question that the detail page
  already answers.
- **Lock:** what the user's answer freezes. A locked item is not
  re-decided in a later stage.
- **Gate:** what happens if the user does not answer — the job
  stops at that card, it does not guess and move on.

## Card 0 — Inputs

- **Show:** the fashion image(s) received and the detail-page
  link, plus the fetch date.
- **Ask:** (1) Is this image + link the full job, or is another
  colour / image coming? (2) Is there a background you want, or
  should it be picked from the random pool?
- **Lock:** product, colour for this video, background mode
  (named vs random).
- **Gate:** do not analyse until both inputs are present. Never
  invent a name or price for a missing link.

## Card 1 — Detail analysis

- **Show:** product name, price, coupon price, colours, fabric
  as written on the page, sizes, and the 3 core features.
  Mark anything the page does not show (e.g. fibre %) as
  "not shown", never as a guessed value.
- **Ask:** (1) Is the core split right — video shows name /
  price / features only, post is minimal? (2) Which colour is
  this video?
- **Lock:** video core, post colour, and the "not shown" list.
- **Gate:** do not generate until the core split is confirmed.

## Card 1A — Texture Lock (BLOCKING)

This card is why the worn/washed look happens, and why it stops
here: no mannequin is generated before this card is locked.

- **Show:** (a) the texture descriptors from the detail page
  (processing, gauge, hand, surface, colour), (b) the selected
  texture close-ups in scroll order, each with position and a
  one-line description (flat surface / folded stack / hand
  pressed into fabric — never a model full shot alone), and
  (c) whether a close-up file is attached or only a written lock
  is available.
- **Ask:** (1) Upload a texture close-up file, or proceed with
  the written lock? (2) Does this written lock read as
  brand-new for this material — or does it still read as
  washed/worn? (3) If a file is attached, is it the right
  close-up for this colour?
- **Lock:** texture file (if any) + written texture lock, to be
  passed unchanged into every later prompt.
- **Gate:** BLOCKING. If the user says the lock still reads as
  washed/worn, do not generate. Ask for a close-up upload or
  screenshot instead of regenerating the same guessed texture.
  ABLY mobile detail stills have no image URL or download
  target (verified 2026-11-01), so a file lock normally needs a
  user upload or screenshot.

## Card 2 — Character and background

- **Show:** body lock (early-20s, hourglass, 7.5 heads, legs
  more than half of total height), hair behind shoulders, and
  the background pick from the random pool (with the reason it
  fits this outfit, and confirmation it is not a repeat of the
  previous job unless the user asked for a repeat).
- **Ask:** (1) Background: accept this pick, or name another
  pool background? (2) Pairing for the full body (e.g. denim,
  black skirt, boots) — accept, or name another neutral pairing?
  The pairing is never presented as the product.
- **Lock:** body proportions, background, pairing.
- **Gate:** do not convert until the background and pairing are
  locked.

## Card 3A — Mannequin

- **Show:** the mannequin display image, with the texture lock
  noted next to it.
- **Ask:** (1) Outfit, colour, and wrap / pocket / ribbon details
  match the detail page? (2) Does the texture read as
  brand-new at a zoomed crop — fibre, fuzz, volume?
- **Lock:** outfit shape and texture as rendered on the
  mannequin. A texture failure here is fixed here, not carried
  into the character stage.
- **Gate:** do not convert until the mannequin is approved.

## Card 3B — Character conversion

- **Show:** the character image on the chosen background, on
  the floor, no pedestal, with matching shoes.
- **Ask:** (1) Body proportions held? (2) Outfit and texture
  unchanged from the mannequin? (3) Hair and background as
  locked?
- **Lock:** character image as the base for the mask stage.
- **Gate:** do not apply the mask until the character is
  approved.

## Card 3C — Start frame (BLOCKING)

- **Show:** the full-body + handwriting start frame, with the
  doll mask already applied at 88%, and core handwriting in
  the side margins (name / price / features only, never
  covering model or outfit).
- **Ask:** (1) Does this frame match the video's full-body +
  handwriting moment? (2) Is the handwriting readable and
  correctly placed? (3) Mask size and position right?
- **Lock:** the exact first frame of the video. The video's
  texture, framing, and handwriting are this frame's texture,
  framing, and handwriting.
- **Gate:** BLOCKING. No video is generated from an unapproved
  start frame.

## Card 3D — Doll mask (inside Card 3C)

The mask is not a separate stop unless the user asks for one:
it is checked inside the start-frame card.

- **Show:** mask size (88% of the original large size), centred
  on eyes, nose, and mouth, hair visible at the sides.
- **Ask:** mask size / position: accept, or adjust?
- **Lock:** mask size and position for this job.
- **Gate:** a mask failure blocks the start frame, and therefore
  the video.

## Card 4 — Video

- **Show:** the video, plus the three points the user must
  check in playback (this environment cannot verify them):
  mask stays on the face, handwriting is present on the first
  frame and again at every full-body moment, and the texture
  holds through movement and zoom.
- **Ask:** (1) First frame = start frame? (2) Full-body moment
  (e.g. the 7-second shot in the ribbon-wrap job) matches the
  start frame's composition and handwriting? (3) Texture still
  reads as brand-new, not washed/worn, in motion?
- **Lock:** the video as delivered, or the named segment to fix
  (with its timestamp).
- **Gate:** a failed segment is fixed by name and timestamp,
  not by regenerating the whole job blindly.

## Card 5 — Post text

- **Show:** the minimal post only: 1–2 lines of recommended
  vibe / situation, plus product name, fabric, and colour,
  plus the detail-page link. No spec dump, no review dump
  unless the user asked for reviews for this job.
- **Ask:** (1) Vibe / situation line right? (2) Post or hold?
- **Lock:** post text as approved. Publishing itself always
  needs a separate explicit approval.
- **Gate:** do not publish from an unapproved post card.

## How cards solve the texture problem

The old failure was not a single bad prompt — it was a missing
gate. Texture was guessed in Card 3A's place, before any close-up
was selected, and each later stage inherited the guess. With
cards, texture is selected and locked in Card 1A, checked at a
zoomed crop in Card 3A, carried unchanged into Cards 3B and 3C,
and re-checked in motion in Card 4. A texture that fails at any
card stops that card; it is never carried forward hoping the
zoom scene will rescue it.
