# Starter Pack — 우선순위 순으로 시작하기

새로 Muse를 시작하는 사용자를 위한 설치 순서. P0부터 깔고, 필요할 때
P1·P2로 넓혀가면 된다. 스킬 하나씩 설치하거나 전체를 클론해도 된다.

```bash
# 스킬 하나만 (예시)
npx skills add nanbada/muse-creative-skills/productivity/voice-dump-dispatch

# 전체 클론
git clone https://github.com/nanbada/muse-creative-skills.git
```

## P0 — 먼저 설치 (모든 사용자)

| 순서 | 스킬 | 왜 먼저인가 |
|---|---|---|
| 1 | `productivity/voice-dump-dispatch` | 두서없는 음성 메모·복합 메시지를 번호 매긴 작업 목록으로 정리하고 독립적인 일은 병렬로 돌려 하나의 보고서로 압축. 체감이 제일 크다. |
| 2 | `productivity/research-brief` | 1차 출처 우선, 모든 주장에 링크, 불확실성 명시. 근거 없는 수치를 산출물에 인쇄하지 않게 만든다. |
| 3 | `productivity/deep-thinking` | 셀프 인터뷰·소크라테스식 질문·제품 해체·재귀 자기비판의 단계별 사고 프로토콜. |
| 4 | `productivity/goal-tracker` | 목표를 마일스톤으로 쪼개고 의지가 아니라 증거로 진척을 잰다. |
| 5 | `productivity/method-capture` | 채팅에 붙여넣은 워크플로를 버전 있는 스킬 파일로 저장하는 습관. 이 팩 자체가 이 습관에서 나왔다. |
| 6 | `productivity/defuddle` | 웹페이지 본문만 마크다운으로 싸게 추출. 토큰 절약용. |

## P1 — 콘텐츠 제작자

| 스킬 | 용도 |
|---|---|
| `productivity/content-studio` | 자료를 채널용 초안으로 변환. 초안은 자동, 발행·전송은 항상 사람 승인. |
| `productivity/editorial-writing` | 증거 규율을 갖춘 인간적인 문체로 발행 가능한 글쓰기 + 네이버 홈판 레이어. |
| `channels/character-channel-ops` | 가상 캐릭터 인스타 채널 운영 풀세트: 론칭·케이던스·캡션·성장·수익화·AI 표시·광고 고지. |
| `channels/ig-outlier-research` | 조회수÷계정 중앙값으로 진짜 바이럴 릴스를 골라 훅 공식을 뽑는 스와이프 파일 방식. |
| `channels/ig-caption-craft` | 캡션 작성·검수·인간화를 한 번에: 125자 컷, 질문 1개, 해시태그 5개 이하, AI티 제거. |
| `channels/memo-handwriting` | 구겨진 메모지 + 손글씨 메시지 합성 — 릴스 시작 프레임 훅·캐러셀 커버용. |
| `productivity/pulse` | Reddit·HN·웹·X를 훑어 주제별 동향 브리핑 (기본 최근 30일). |
| `productivity/social-sourcing` | X·Reddit 글을 로그인·API 키 없이 조회. |
| `channels/coupang-reviewer` | 직접 찍은 사진 기반의 사람 같은 쿠팡 후기 초안. 승인 게이트 포함. |
| `channels/jp-sns-ops` | 일본향 인스타 운영: 구어체 캡션, 캐러셀 템플릿, 타이밍 규칙. |
| `image/*`, `video/*` | 이미 있는 이미지·영상 스킬 (README 본문 참조). P0·P1과 함께 쓰면 제작 파이프라인이 완성된다. |

## P2 — 운영 심화 (Muse를 오래·깊게 쓸 때)

| 스킬/문서 | 용도 |
|---|---|
| `ops/PLAYBOOK.md` | 반복 작업 관리(job card + probation + 월간 감사), 개선 하니스, 메모리 규율, proof-of-done, read offload, 라우팅 정책, 승인 게이트. 스킬이 아니라 운영 규칙 모음이다. |
| `productivity/competitive-brief` | 경쟁사 조사 → 포지셔닝·콘텐츠 격차·기회·위협·배틀카드. |
| `productivity/seo-audit` | 키워드·온페이지·콘텐츠 격차·기술 점검 + quick-win vs 전략 액션플랜. |

## 의도적으로 제외한 것 (환경 전용, 참고용으로만)

- VM 브라우저 한글 IME 입력 문제 대응, Mac 전체 디스크 접근 가드, 특정
  기기·계정 구조에 맞춘 연결 규칙 — 내 환경 한정이라 그대로 복사하면 안
  된다. 같은 부류의 문제를 만나면 패턴(가드 → 안내 → 중단)만 참고할 것.
