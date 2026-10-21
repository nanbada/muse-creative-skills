# 퀵스타트 프롬프트 — 10초형 (이름만 교체)

정밀 시리즈형(`stage-prompt-system.md`)보다 빠른 제작 모드. 첫 프레임 이미지 1장 → I2V 10초 1클립으로 끝낸다. 종 교체는 이름 + 종 특성어만 바꾸면 된다.

**환경 변형 B — 투명 유리화분형**: 이 모드의 기본 룩은 테라코타 정원형(환경 변형 A)과 다르다. 투명 유리화분 + 검은 배경 + 스튜디오 조명 — **뿌리가 유리 너머로 보이는 것**이 이 룩의 핵심 볼거리다.

**사용 모델**
- 이미지: Google Gemini (Nano Banana), GPT Image, Midjourney 등
- 비디오: Google Flow (Omni Flash / Veo), Seedance 2.5, Kling 등

## 범용 템플릿 ({{...}}만 교체)

**첫 프레임 (씨앗 상태)**
```
Ultra-realistic macro photograph of a single {{species}} seed just placed beneath the soil surface inside a transparent glass pot, rich dark potting soil, soft even studio lighting, clean black background, fixed camera angle from slightly above, shallow depth of field, highly detailed texture of seed and soil, photorealistic, 4K, no hands, no text, no watermark
```

**중간 프레임 (성장 중 — 필요 시)**
```
Ultra-realistic macro photograph of a young {{species}} plant growing inside a transparent glass pot, {{young plant traits: leaves unfurling, stem, roots}}, white roots visible through the glass, same exact pot, same soil level, same black background, same fixed camera angle and lighting as previous frame, highly detailed, photorealistic, 4K
```

**마지막 프레임 (자란 상태 — 필요 시)**
```
Ultra-realistic macro photograph of a mature {{species}} plant {{mature traits: leaves, flowers, fruits}} inside a transparent glass pot, white roots clearly visible, same exact transparent glass pot, same soil, same clean black background, same fixed camera angle and soft even lighting, photorealistic, 4K, no text
```

**비디오 프롬프트 (I2V 10초)**
```
Smooth cinematic 10-second time-lapse of a {{species}} seed growing inside a transparent glass pot. Start with the seed just under the soil surface. The seed slowly swells and cracks open, a tiny white root grows downward, a green shoot emerges and rises, {{growth sequence: leaves unfurl and expand, flowers bloom, fruits form — 종에 맞게}}, Camera remains completely fixed, soil and pot stay unchanged, soft even lighting, no flicker, highly realistic plant growth, photorealistic, macro detail, natural motion, 9:16 vertical aspect ratio
```

## 오이 완성 예시 (worked example — verbatim)

**첫 프레임**
```
Ultra-realistic macro photograph of a single cucumber seed just placed beneath the soil surface inside a transparent glass pot, rich dark potting soil, soft even studio lighting, clean black background, fixed camera angle from slightly above, shallow depth of field, highly detailed texture of seed and soil, photorealistic, 4K, no hands, no text, no watermark
```

**중간/성장 프레임**
```
Ultra-realistic macro photograph of a young cucumber plant growing inside a transparent glass pot, small green leaves unfurling, white roots visible through the glass, same exact pot, same soil level, same black background, same fixed camera angle and lighting as previous frame, highly detailed, photorealistic, 4K
```

**마지막 프레임**
```
Ultra-realistic macro photograph of a mature cucumber plant with several healthy green leaves and small developing cucumbers inside a transparent glass pot, white roots clearly visible, same exact transparent glass pot, same soil, same clean black background, same fixed camera angle and soft even lighting, photorealistic, 4K, no text
```

**비디오 프롬프트**
```
Smooth cinematic 10-second time-lapse of a cucumber seed growing inside a transparent glass pot. Start with the seed just under the soil surface. The seed slowly swells and cracks open, a tiny white root grows downward, a green shoot emerges and rises, leaves unfurl and expand naturally, small cucumber fruits begin to form. Camera remains completely fixed, soil and pot stay unchanged, soft even lighting, no flicker, highly realistic plant growth, photorealistic, macro detail, natural motion, 9:16 vertical aspect ratio
```

## 사용 방법

1. 이미지 AI에 **첫 프레임 프롬프트**를 넣어 이미지를 생성한다
2. 그 이미지를 비디오 AI에 업로드하고 **비디오 프롬프트**를 붙여넣는다
3. 더 긴 영상이 필요하면: 생성된 영상의 **마지막 프레임을 저장해 다음 생성의 시작 이미지로** 쓰고, 프롬프트를 약간 수정해 이어서 만든다 (프레임 체이닝)
4. 중간/마지막 프레임 프롬프트는 첫 프레임만으로 성장이 어긋날 때 키프레임으로 추가 생성해 보간에 쓴다

## 강화 옵션 (연속성이 깨질 때)

- 비디오 프롬프트 끝에 고정 문구 추가: `the pot, soil level, background and lighting stay identical from the first frame to the last`
- 열매 종은 마지막 프레임에 개수를 못 박는다 (예: `exactly three small cucumbers`) — 개수 회계는 정밀형 규칙과 동일
- 손이 씨앗을 심는 장면이 필요하면 첫 프레임만 정밀형 F1 방식 (손 허용)으로 바꾸고, 이후 프레임은 `no hands`를 유지한다
- 메인 시리즈(수익화 간판 콘텐츠)는 정밀형(`stage-prompt-system.md`)으로, 퀵형은 대량 테스트·소재 발굴용으로 쓴다 🛠
