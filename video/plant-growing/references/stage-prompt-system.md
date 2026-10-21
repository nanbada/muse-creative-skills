# 단계 프롬프트 시스템 — 환경 락 + 구조 락 + 단계 + 제외

식물 키우기 스킬의 핵심 자산. 단계 프레임(스틸) 1장을 만드는 프롬프트는 4블록으로 구성된다.

| 블록 | 역할 | 시리즈 내 변동 |
|---|---|---|
| **환경 락** (LOCKED ENVIRONMENT) | 화분·흙·배경·빛·카메라·노출을 전 프레임 동일하게 고정 | 없음 — verbatim 고정 |
| **구조 락** (REFERENCE-LOCKED STRUCTURE) | 직전 프레임에서 이어받는 구조 (크라운·잎 수/위치/각도·열매 위치·실루엣) | 단계마다 "무엇이 그대로인가"를 명시 |
| **단계** (THE PLANT AT THIS STAGE) | 이 단계의 식물 상태 (높이·너비·잎 수·꽃/열매 수와 상태) | 단계마다 교체 |
| **제외** (EXCLUSION) | 이 단계에 **있으면 안 되는 것** (이전/이후 단계의 잔재) | 단계마다 교체 |

머리말 문형 (고정): `This is frame {{N}} in a continuous {{species}} growth series. It shows the exact same pot, soil, background, lighting, camera, framing, and environment as frame 1. The plant has grown from seed placement into the stage described below.`

품질 문형 (고정): `Ultra-realistic macro photograph, 9:16 vertical, photorealistic 8K.`

꼬리말 (고정, F2부터): `No hand is visible. Preserve identical exposure, colour temperature, shadow position, depth of field, pot placement, and soil line.` + `Detailed texture of {{species texture details}} under macro focus.` + `No text, logos, labels, borders, watermarks, insects, tools, extra seeds, or people.`

> F1(파종)만 예외: 손 허용 (`A hand gently placing seeds onto the soil surface` 등), 꼬리말의 `No hand is visible` 삭제.

## 마스터 템플릿

```
This is frame {{N}} in a continuous {{species}} growth series. It shows the exact same pot, soil, background, lighting, camera, framing, and environment as frame 1. The plant has grown from seed placement into the stage described below.
REFERENCE-LOCKED PLANT STRUCTURE: {{preserve the same crown/stem base, and carry over from the previous frame: leaf count, leaf positions, leaf angles, plant width, plant height, stem locations, overall silhouette — with only the stage changes below added}}
Ultra-realistic macro photograph, 9:16 vertical, photorealistic 8K.
THE PLANT AT THIS STAGE: {{stage description — size (cm), leaf count and form, flower/fruit count, positions, colours, surface details}}
EXCLUSION: {{what must NOT appear at this stage — remnants of earlier stages and previews of later stages}}
LOCKED ENVIRONMENT, identical in every frame of this series: {{pot, soil, surface, background, light direction, shadow, camera — verbatim, defined once in the species card}}
No hand is visible. Preserve identical exposure, colour temperature, shadow position, depth of field, pot placement, and soil line.
Detailed texture of {{texture details}} under macro focus.
No text, logos, labels, borders, watermarks, insects, tools, extra seeds, or people.
```

## 딸기 완성 예시 (샘플 영상 역설계)

환경 락 (전 프레임 공통, 종 카드에서 확정):
> one elegant terracotta pot, medium size, with a softly rounded rim and a warm weathered clay surface, sitting centred in frame on a plain wooden garden surface. The pot is filled with rich dark fertile soil, level with the rim, showing fine crumb texture and small scattered particles. Directly behind the pot is a softly blurred garden background of deep greens with gentle bokeh. Warm golden morning sunlight falls from the upper left, casting a soft shadow to the lower right. Static macro camera at fixed eye level with the pot rim, fixed lens, fixed framing, fixed distance. The pot, the soil surface, the background, the light direction, the shadow, and the camera position are IDENTICAL across every image in this series. Only the plant changes.

| 프레임 | 단계 | 단계 블록 요지 | 제외 블록 요지 |
|---|---|---|---|
| F1 | 파종 | 흙만. 씨앗 몇 알이 표면에 놓임. 손이 씨앗을 떨어뜨리는 중 (손 허용 유일 프레임) | 싹·잎·줄기 일절 없음 |
| F2 | 발아 | 작은 새싹 — 떡잎 2장 + 첫 본엽 눈. 높이 약 2cm | 삼출엽·꽃·열매 없음 |
| F3 | 잎 성장 | 어린株 — 삼출엽 2~3장 + 중앙 눈 뭉치. 높이 약 6cm (샘플 s_05) | 꽃봉오리·꽃·열매 없음 |
| F4 | 개화 | 흰 꽃 3송이 개화 + 봉오리 3개 아래로 처짐. **꽃+봉오리 = 6개 (최종 열매 수와 일치)** (샘플 s_09) | 열매(초록 포함) 없음 |
| F5 | 어린 열매 | 꽃이 있던 자리에 작은 초록 열매 6개. 꽃잎은 모두 떨어짐 | 흰 꽃잎·꽃·봉오리 없음 |
| F6 | 착색 | 열매 6개 분홍→빨강 착색 중. 큰 것 4 + 작은 것 2 위치 고정. 잎·열매에 이슬 (샘플 s_13) | 완전히 진한 빨강 완숙 열매 없음 |
| F7 | 완숙 | 아래 verbatim 예시 (worked example) | 꽃잎·꽃·봉오리·미숙 열매 없음 |

### F7 완숙 프롬프트 (worked example — verbatim)

```
This is frame 2 in a continuous strawberry growth series. It shows the exact same pot, soil, background, lighting, camera, framing, and environment as frame 1. The plant has grown from seed placement into the stage described below.
REFERENCE-LOCKED PLANT STRUCTURE: preserve the same crown, leaf count, leaf positions, leaf angles, plant width, plant height, stem locations, and overall silhouette from the previous frame. Every fruit has ripened fully in the exact same position. Four medium-to-large ripe strawberries hang from the same four stems, plus two slightly smaller ripe strawberries lower down. Six in total. Each is plump, heart-shaped, glossy deep red, covered with evenly spaced pale-yellow seeds, with a small fresh green calyx. Fine dew droplets cling to fruit and leaves.
Ultra-realistic macro photograph, 9:16 vertical, photorealistic 8K.
THE PLANT AT THIS STAGE: A mature strawberry plant filling the centre of frame, approximately eighteen centimetres tall and twenty-two centimetres wide, contained within the terracotta pot. Eleven mature trifoliate leaves with deep green serrated leaflets and defined veins. Six fully ripe strawberries hang bowed on short arching stems: four prominent plump heart-shaped strawberries and two smaller ripe strawberries lower down, all showing deep glossy crimson skin, recessed yellow seeds, and crisp green star-shaped calyxes.
EXCLUSION: There are absolutely no remaining white petals, flowers, unopened buds, faded blossoms, yellow flower centres, or pale-green immature berries. Only ripe fruit and foliage.
LOCKED ENVIRONMENT, identical in every frame of this series: one elegant terracotta pot, medium size, with a softly rounded rim and a warm weathered clay surface, sitting centred in frame on a plain wooden garden surface. The pot is filled with rich dark fertile soil, level with the rim, showing fine crumb texture and small scattered particles. Directly behind the pot is a softly blurred garden background of deep greens with gentle bokeh. Warm golden morning sunlight falls from the upper left, casting a soft shadow to the lower right. Static macro camera at fixed eye level with the pot rim, fixed lens, fixed framing, fixed distance. The pot, the soil surface, the background, the light direction, the shadow, and the camera position are IDENTICAL across every image in this series. Only the plant changes.
No hand is visible. Preserve identical exposure, colour temperature, shadow position, depth of field, pot placement, and soil line.
Detailed texture of glossy strawberry skin, recessed golden achenes, delicate morning dew beads, serrated leaf margins, and velvety stems under macro focus.
No text, logos, labels, borders, watermarks, insects, tools, extra seeds, or people.
```

> 주: 원문의 "frame 2" 표기는 원본 워크플로의 프레임 번호다. 이 스킬의 시리즈 순서에서는 완숙 단계(F7)에 해당하며, 머리말의 번호만 시리즈 순서에 맞게 바꿔 쓴다.

## 연속성 QA (프레임마다)

- [ ] 환경: 화분 위치·흙 표면선·배경 보케·빛 방향·그림자 위치가 F1과 겹쳐 대조해 동일한가 (원본 해상도로 확인)
- [ ] 개수 회계: 꽃 수(F4) = 어린 열매 수(F5) = 완숙 수(F7)인가. 잎 수는 단계표대로인가
- [ ] 구조 락: 열매·잎의 위치가 직전 프레임과 같은 자리에서 자랐는가 (갑자기 생긴 열매 = 실패)
- [ ] 제외 위반: 이전 단계 잔재(완숙 프레임의 꽃잎 등)나 다음 단계 선행 등장이 없는가
- [ ] 손·텍스트·워터마크·벌레 등 금지 요소가 없는가

## I2V 보간 (Gemini Omni 1.1 Flash)

- 모드: image_to_video, **시작 프레임 = F_n, 종료 프레임 = F_n+1** 로 구간 생성. 모델이 사이 모션을 채운다
- 구간 길이: 기본형은 구간당 1.5~2.5초 (8~15초 총), 확장형은 4~6초 (30~45초 총) 🛠
- 모션 지시 (구간 공통): `Seamless timelapse growth: the plant grows gradually and continuously from the start frame to the end frame. Camera completely static, locked framing, identical light and background throughout. No cuts, no zoom, no new objects appearing or disappearing — growth only.`
- 단계 점프가 큰 구간(F1→F2 발아, F4→F5 꽃→열매)은 중간 프레임 1장을 추가해 2구간으로 나누면 붕괴가 줄어든다 🛠
- 네이티브 오디오는 환경음 수준으로만 쓰고, 최종 BGM은 조립 단계에서 교체한다
