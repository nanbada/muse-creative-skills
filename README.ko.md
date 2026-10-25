# Muse Creative Skills

[한국어](README.ko.md) | English

AI 에이전트(Muse, Claude Code 및 호환 어시스턴트)용 이미지·영상 제작
스킬 모음입니다. 각 스킬은 `SKILL.md` + 참고 자료로 구성되어 있으며,
스킬 하나씩 또는 전체를 설치할 수 있습니다.

## 설치

```bash
# 스킬 하나만
npx skills add nanbada/muse-creative-skills/image/photoreal-realness

# 전체 클론
git clone https://github.com/nanbada/muse-creative-skills.git
```

## 스타터 팩 (여기서 시작)

Muse를 새로 시작한다면 우선순위 순으로 설치 — 전체 순위와 이유는
[STARTER-PACK.md](STARTER-PACK.md) 참조.

- **P0 — 모두 먼저:** `productivity/voice-dump-dispatch`,
  `productivity/research-brief`, `productivity/deep-thinking`,
  `productivity/goal-tracker`, `productivity/method-capture`,
  `productivity/defuddle`
- **P1 — 콘텐츠 제작자:** `productivity/content-studio`,
  `productivity/editorial-writing`, `channels/character-channel-ops`,
  `channels/ig-outlier-research`, `channels/ig-caption-craft`,
  `channels/memo-handwriting`, `productivity/pulse`,
  `productivity/social-sourcing`, `channels/coupang-reviewer`,
  `channels/jp-sns-ops`, 아래 `image/`·`video/` 스킬
- **P2 — 장기 운영:** `ops/PLAYBOOK.md` (반복 작업 관리, 개선 하니스,
  메모리 규율, proof-of-done, read offload, 라우팅 정책, 승인 게이트),
  `productivity/competitive-brief`, `productivity/seo-audit`

## 이미지 스킬 (`image/`)

| 스킬 | 설명 |
|---|---|
| `photoreal-realness` | "휴대폰샷" — AI 사진을 실제 스마트폰으로 찍은 것 같은 느낌으로 만드는 의도적 열화 프롬프트 블록. 4단계: 스냅샷 철학, 기술적 불완전함, 얼굴 비대칭, 인간적 노이즈. |
| `pose-reference` | 캐릭터 이미지 생성용 포즈 선택 — 8개 해부학 포즈 시트(133개 포즈)에서 상황/분위기로 고르거나 랜덤 선택, 시각 검증. |
| `museum-editorial` | GPT Image 2.5용 박물관급 에디토리얼 포스터 프롬프트 생성 — 미니멀 9:16 세로 레이아웃, 아카이브 레이어, 한국어/영어 지원. 작성 전 사실 검증. |
| `second-world` | 사진을 "Second World" 포스터로 변환 — 세로 3:4 캔버스, 상반부는 충실한 사진, 하반부는 아이보리 종이 위에 사진 속 구조물 하나가 새로운 물리 법칙으로 이어짐. |
| `doodle-overlay` | "고양이 손그림" / "귀여운 아이 손그림" / "손그림 낙서" — 실사 사진 위에 거대한 흰색 손그림 캐릭터를 얹는 믹스드미디어: 사진은 그대로, 고양이는 장난·인물(아이)은 사물 재해석으로 실제 건축물·풍경과 상호작용. 오버레이 모듈: 손글씨 문구·아이콘·낙서 흩뿌리기·엽서·매거진 커버라인·홍보 카피. |
| `comic-production` | "만화 제작" — 일관된 멀티 패널 AI 만화 제작 6단계 파이프라인: 캐릭터 락·배치 렌더·검증 게이트·타겟 재시도·후반 레터링. 7개 오픈소스 프로젝트 기법 통합. |
| `pencil-line-poetry` | "동양미 스타일" — 거대한 실사 자연 속에 사는 작은 선 캐릭터(점눈·최소 표정): 이슬방울·꽃잎·잎·깃털이 풍경이 됨. 섬세한 선 + 매크로 자연 믹스드미디어, 따뜻한 황금빛 역광, 시적인 세로 구도. 모드: 작은 선 세계·발광선·풍경 위 선·부드러운 페인터리. |

## 영상 스킬 (`video/`)

| 스킬 | 설명 |
|---|---|
| `phone-shot-video` | "휴대폰으로 찍은 영상" — AI 영상을 실제 스마트폰으로 찍은 느낌으로: 1인칭 셀카 고정, 의도적 불완전함(흔들림, 오토포커스 헌팅, 노출 변화), 다이제틱 사운드 only, GRWM 30초 비트 구조. |
| `photoreal-selfie-look` | AI 영상 프롬프트에 포토리얼 스마트폰 전면 카메라 룩 주입: 뷰티 필터, 그레인, 모션 블러, 포커스 브리딩, 롤링 셔터, SNS 압축 아티팩트. |
| `veo-vertical-clip` | Veo 3.1 네이티브 9:16 세로 클립 프롬프트 설계 + Google Flow 크레딧 고려 제작 플랜. |
| `place-video-prompter` | 실제 장소(건물, 랜드마크, 가게, 캠퍼스…)용 한국어 영상 제작 프롬프터 생성 — 엄격한 리얼리즘 가드레일 포함. |
| `ad-video-automation` | 숏폼 상품 광고 영상(15–20초, 9:16) 자동화: 컨셉 리서치, 히어로 이미지 상품 락, 블록 단위 초안 + 리뷰 게이트, 텍스트/그래픽/BGM 코드 오버레이. |
| `youtube-shorts-growth` | 유튜브 쇼츠 채널 성장 전략: 주제 일관성 + 프레임 컨트롤, 실행 전략, 제목/썸네일 패턴. |
| `plant-growing` | "식물 키우기" — 식물 성장 타임랩스 제작 시스템: 환경 락 단계 프레임 프롬프트 시리즈(씨앗→완숙) → Gemini Omni 1.1 Flash 프레임 보간 또는 10초 퀵 모드 → 손글씨 키워드 + 생활꿀팁 롤링 텍스트로 중년·노년 대량 공략 → 스틸컷 3~6장 → 씨앗·비료 링크 수익화. 종별 팩 포함. |

## 생산성 스킬 (`productivity/`)

| 스킬 | 설명 |
|---|---|
| `voice-dump-dispatch` | 두서없는 음성 메모·복합 메시지를 번호 매긴 작업 목록으로 정리하고 독립적인 일은 병렬로 돌려 하나의 보고서로 압축. |
| `research-brief` | 근거 규율을 갖춘 조사: 1차 출처 우선, 모든 주장에 링크, 불확실성 명시. |
| `deep-thinking` | 단계별 사고: 셀프 인터뷰·소크라테스식 질문·제품 해체·재귀 자기비판. |
| `goal-tracker` | 목표를 마일스톤으로 쪼개고 의지가 아니라 증거로 진척 측정. |
| `method-capture` | 붙여넣은 워크플로·방법·SKILL.md 텍스트를 버전 있는 스킬 파일로 저장. |
| `defuddle` | 웹페이지 본문을 메타데이터와 함께 깨끗한 마크다운으로 추출 — 토큰 절약형 대안. |
| `pulse` | Reddit·Hacker News·웹·X를 훑어 주제별 동향 브리핑 (기본 최근 30일). |
| `social-sourcing` | 로그인·API 키 없이 일반 HTTPS로 X·Reddit 글 조회. |
| `competitive-brief` | 경쟁사 조사 → 포지셔닝·메시징 비교, 콘텐츠 격차, 기회, 위협, 배틀카드. |
| `seo-audit` | 구조화된 SEO 진단 — 키워드·온페이지·콘텐츠 격차·기술 점검·경쟁 비교 + quick-win vs 전략 액션플랜. |
| `content-studio` | 자료를 채널용 초안으로 변환하되 원뜻을 유지. 초안은 자동, 발행·전송·예약은 항상 사람 승인. |
| `editorial-writing` | 증거 규율을 갖춘 인간적인 문체로 발행 가능한 글쓰기 + 네이버 홈판 레이어. |

## 채널 스킬 (`channels/`)

| 스킬 | 설명 |
|---|---|
| `character-channel-ops` | 가상 캐릭터 인스타 채널 운영: 론칭 셋업, 캐릭터 일관성 워크플로, 주간 케이던스, 캡션/해시태그 플레이북, 성장 전술, 수익화 파이프라인, 컴플라이언스(AI 표시·가상 인물 광고 고지). |
| `ig-outlier-research` | 조회수÷계정 중앙값으로 릴스 순위 매기기, 훅 공식 명명, 촬영용 스와이프 파일 구축. |
| `ig-caption-craft` | 캡션 작성·검수·인간화를 한 번에: 125자 컷, 질문 1개, 검색어, 해시태그 5개 이하, 기계적 흔적 제거 + 전후 검출 증명. |
| `memo-handwriting` | 구겨진 메모지 + 손글씨 메시지 합성 (9:16/4:5) — 스크롤 스토퍼 훅·릴스 커버·캐러셀 커버. |
| `coupang-reviewer` | 직접 찍은 사진·상품 정보 기반의 사람 같은 쿠팡 후기 초안. 발행 전 사람 승인 게이트 포함. |
| `jp-sns-ops` | 일본향 인스타/SNS 운영: 20대 초반 구어체 캡션, 캐러셀 템플릿, 해시태그·타이밍 규칙. |

## 운영 플레이북 (`ops/`)

| 문서 | 내용 |
|---|---|
| `PLAYBOOK.md` | 어시스턴트 장기 운영: 반복 작업 관리(job card·probation·월간 감사), 개선 하니스, 메모리 규율, proof-of-done, read offload, 라우팅 정책, 승인 게이트. |

## 트리거 워드 (한국어)

일부 스킬은 설명란에 한국어 트리거 워드가 있습니다 — 말하면
어시스턴트가 해당 스킬을 적용합니다:

- **휴대폰샷** → `photoreal-realness` (이미지)
- **휴대폰으로 찍은 영상** → `phone-shot-video` (영상)
- **고양이 손그림** / **귀여운 아이 손그림** / **손그림 낙서** → `doodle-overlay` (이미지)
- **만화 제작** → `comic-production` (이미지)
- **동양미 스타일** / **연필선 스타일** → `pencil-line-poetry` (이미지)
- **식물 키우기** → `plant-growing` (영상)

## 참고

- 이미지/영상 모델에 들어가는 프롬프트 블록은 영어, 사용자에게
  전달하는 설명은 사용자 언어로 작성합니다.
- 이 스킬들은 AI 페르소나를 실존 인물로 속이는 용도(가짜 후기,
  신원 미공개 등)에 사용하지 않습니다. 각 플랫폼 정책에 따라
  AI 생성 표시를 유지하세요.

## 라이선스

MIT — [LICENSE](LICENSE) 참고.
