---
name: coupang-reviewer
description: Generate human-looking Korean product reviews for Coupang (체험단 / 상품평).
---

# coupang-reviewer

Generate human-looking Korean product reviews for Coupang (체험단 / 상품평).

Core principle: the review must read like a real buyer wrote it. Never ad-like.
Input: product info + the user's own photos. Output: a copy-ready review draft
that the user approves and registers manually (stage 1). Full automation of
submission is a later stage and is out of scope here.

## Stage-1 pipeline

```
1. COLLECT   → gather product info + 6–10 own photos
2. DRAFT     → run the review prompt (below) to produce a draft
3. HUMANIZE  → apply the human-touch checklist to the draft
4. APPROVE   → show the draft to the user; they approve or request edits
5. REGISTER  → user copies the text and registers it on Coupang themselves
```

Nothing is published before step 4. Keep drafts and approval records in the
owning goal's `hidden_files/review-log.md`.

## Step 1 — Collect

Ask the user for (anything missing):
- 제품명/스펙: include at least one numeric spec (용량, 함량, 개수, 사이즈)
- 카테고리: 식품 / 화장품 / 생활용품 / 가전 등
- 구매한 이유(내 고민): one sentence
- 사용 기간
- 좋았던 점 2~3개 (real, experienced)
- 아쉬웠던 점 1개 (non-fatal)
- 추천하고 싶은 사람
- 사진: 6–10 shots, varied angles — unboxing, real-use scene, size comparison,
  texture close-up. Video if available.

Rules source: your own reviewer rules doc, kept alongside the skill.

## Step 2 — Draft (review prompt)

Produce ONLY the review body. No preamble, no explanation.

```
[역할]
너는 이 제품을 직접 구매해서 써본 실사용자다.
과장 광고 톤이 아니라, 진짜 구매자가 쓴 것 같은 후기를 쓴다.

[제품 정보]
- 제품명/스펙: {용량, 함량, 개수 등 숫자 포함}
- 카테고리: {식품/화장품/생활용품 등}
- 구매한 이유(내 고민): {}
- 사용 기간: {}
- 좋았던 점 2~3개: {}
- 아쉬웠던 점 1개: {}
- 추천하고 싶은 사람: {}

[작성 규칙]
1. 분량 300~500자. 문단 3~4개, 문단 사이 한 줄 띄우기.
2. 구조 순서를 반드시 지킬 것
   ① 구매 계기 — 내 상황/고민을 한 문장으로 (공감 유도)
   ② 실사용 체감 — 스펙 숫자를 최소 1개 이상 근거로 넣기
      "○○일까 걱정했는데 실제로는 ~했다" 반전 구조 1회 사용
   ③ 솔직한 단점 — 치명적이지 않은 것 1개 + 해결 팁 같이
   ④ 추천 대상 + 재구매 의사를 한 문단에
3. 문체: ~습니다/~했어요 혼용, 담백하게. 감탄사 남발 금지.
4. 금지어: 최고, 강추, 인생템, 무조건, 완벽 (1회까지만 허용)
5. 효능 단정 금지. "~한 느낌이었어요", "~체감했습니다"로 완화
   (특히 화장품/식품은 의학적 효과 표현 쓰지 말 것)
6. 이모지는 0~2개까지만.
7. 특정 쇼핑몰·플랫폼 이름을 본문에 넣지 말 것.
   배송·가격 언급이 필요하면 "빠르게 받았습니다" 정도로만.

[출력]
후기 본문만 출력. 설명·머리말 없이.
```

## Step 3 — Humanize (checklist)

Apply to every draft before showing it to the user:
- [ ] 개인 구체성: 사용 기간, 가족/자취 여부, 이전 제품과 비교 등 본인만의 상황 추가
- [ ] 감각적·상황적 디테일: "바르고 10분 뒤", "저녁에 썼을 때"처럼 시간·장소·감각
- [ ] 말투 개인화: 평소 말투로 살짝 수정 ("좋더라구요", "생각보다 ~네요")
- [ ] 구조 순서 지켰는가? 숫자 근거 + 반전 1회 있는가? 단점+팁 있는가?
- [ ] 금지어·효능 단정 없는가? 사진 다양성 확보했는가?
- [ ] 도움돼요 유도: 실제로 도움이 될 정보(팁, 주의점, 비교)가 자연스럽게 있는가?

체크리스트 후 AI 티 제거 패스: `humanize-korean` 스킬 Layer 1 (짧은 후기는
light, 긴 후기는 standard)로 번역투·기계적 병렬·관용구를 제거한다.
의미·수치·사진 근거는 건드리지 않는다. 이 패스는 체크리스트를 대체하지 않는다.

## Guardrails

- Reviews are for products the user actually purchased and photographed.
  Never fabricate experiences, efficacy, numbers, or other people's reactions.
- 체험단 제공 제품은 후기 안에 제공 사실을 명시한다.
- No medical/cosmetic efficacy claims, ever.
- Do NOT build or use: helpful-button clickers, multi-account review posting,
  or any manipulation of Coupang's ranking/review systems.
  (Found in research: kyseong00/coupang-review-helper auto-clicks "도움이 돼요" —
  flagged as manipulation, out of scope.)

## References (researched 2026-09-30)

- Chrome extension "쿠팡 AI 리뷰 생성기" (dlwoabsdk, ~164 users, free, on-device
  Gemini Nano): auto-detects the product on the Coupang review page, pulls real
  buyer reviews of similar products as context, generates a detailed review
  (100–1000 chars, user-selectable) + 30-char one-line summary, and auto-fills
  star rating, questionnaire, review text, and summary into the Coupang form.
  The user still reviews and submits. Useful reference for stage 2 (auto-fill);
  our drafts keep the stricter 4-part structure and human-correction pass.
  https://chromewebstore.google.com/detail/%EC%BF%A0%ED%8C%A1-ai-%EB%A6%AC%EB%B7%B0-%EC%83%9D%EC%84%B1%EA%B8%B0/penfhjkmpbiiobmdaicoikkmcfcblnip
- GitHub (last 3 months), same problem space:
  - jinuk0724/coupang-review-helper — "리뷰메이트" web app turning real usage
    experience into structured reviews; principles overlap: no invented
    experiences/efficacy/numbers, 500–700 chars, no ad-like expressions,
    disclose provided products. https://github.com/jinuk0724/coupang-review-helper
  - KiCTHEONE/coupang-review — Coupang Eats seller reply tool; dry-run preview
    + manual approve pattern worth copying. https://github.com/KiCTHEONE/coupang-review
  - yangtaehyeon/coupang-review — Coupang Partners static review site with an
    add-review skill (`/add-review <쿠팡 링크>`); good reference for a
    skill-driven review pipeline. https://github.com/yangtaehyeon/coupang-review
  - Most other repos in the space are review crawlers, not generators.
