# GRWM Video Blocks (English, append after scene/character description)

## Core principle
Never prompt "realistic" vaguely. Decompose WHO shoots, WITH WHAT, HOW:
the woman herself holds the phone at arm's length for the entire clip.

## Camera & visual spec
One continuous handheld front-facing smartphone selfie vlog, filmed entirely
by her with the phone held in her own hand at arm's length. No third-person
camera, tripod, cinematic shots, professional camera movement, or external
filming.

Make it look like an authentic modern smartphone recording:
Mild handheld movement and natural arm motion. Small framing imperfections.
Occasional autofocus adjustments. Natural exposure fluctuations. Realistic
front-camera lens distortion. Soft morning window light. Natural smartphone
colors. No beauty filter, skin smoothing, or cinematic color grading. Same
woman, same face and hair throughout. She holds the phone herself at all
times. No subtitles, logos, watermarks, captions, or on-screen text.

## 30s GRWM beats
She starts in her bedroom shortly after waking up, holding the phone toward
herself with a sleepy smile. She looks into the camera and says:
{{opening_line}}. She laughs, briefly turns the camera toward her closet,
then returns it to her face. She casually fixes her hair, applies a small
amount of makeup while occasionally looking into the phone camera, chooses
an outfit, and walks around her room. Include tiny natural moments:
adjusting her hair, checking herself in a mirror, realizing she forgot
something, laughing, and briefly looking away from the camera. She grabs
her bag and heads toward the door. Before leaving, she looks into the
camera and says: {{closing_line}}. She gives a quick smile and lowers the
phone slightly as the clip ends.

Default lines (replace per {{locale}}, never mix languages):
- EN open: "Okay, I have approximately ten minutes to look like I have my
  life together." / EN close: "Okay, that's good enough. Let's go."
- JP open: 「おはよう。あと10分で出なきゃなのに、まだ何も準備してない（笑）」
  / JP close: 「よし、こんなもんかな。行ってきます！」

## Audio spec
Diegetic sound only. Include quiet bedroom ambience, fabric movement,
footsteps, drawers opening, subtle street ambience, and natural room tone.
No background music.

## Identity reference block (prepend when using a reference image)
Use the attached image as the identity reference for the adult woman in the
video. Preserve her facial features, face shape, hair color, hairstyle, and
overall appearance consistently throughout the entire video. If the
reference contains multiple views, treat them as different views of ONE
woman. Show only one woman in the video. Use the image for character
identity only. Do not reproduce its layout, background, or pose.
Order: attach reference → identity block → main prompt. Start-image (scene
entry frame) and identity reference serve different roles — do not conflate.

## Localization ({{locale}})
JP/KR daily vlog arrangement: compact studio apartment, small vanity,
beige curtains; simple knit outfit. Fully replace dialogue per locale.

## Failure checkpoints
Confirm target length (30s) and voice/audio availability on the generation
screen. If too many actions fail (makeup + outfit + bag), simplify beats:
"fix hair → grab bag → leave".

## Imperfection QC checklist (reshoot only if "too perfect")
[ ] visible mild hand shake / arm motion
[ ] at least one framing imperfection or tilt
[ ] autofocus or exposure breathing somewhere in the clip
[ ] no beauty-filter look, no cinematic grade
[ ] identity identical first frame to last
