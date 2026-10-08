# 정량 주장 검증 큐 — 2026-10-09

> **2026-10-09 부분 검증:** [원문 정량대조](PRIMARY_SOURCE_NUMERIC_CHECK_2026-10-09_KO.md) — Wang/Bol/Ross 출판사 본문·Ross 정정 확인. 원자료 재현은 미완료.

**상태:** P0 EVIDENCE HYGIENE / NO NEW RESULT

공개 문서의 숫자는 인상강화용 장식이 아니다. 모집단·기간·분모·단위·모형·불확실성까지 원문에서 복구되지 않으면 Project의 확정 근거로 사용하지 않는다.

## P0 — 재검증 전 인용 제한

**상태 갱신:** Wang/Bol/Ross = PRIMARY TEXT VERIFIED; Ross correction VERIFIED. 세 연구 모두 SUPPLEMENTARY/RAW REPRODUCTION PENDING. 나머지는 미검증.
| 연구 | 현재 확인해야 할 주장 | 실패하기 쉬운 지점 | 검증 완료 전 처리 |
|---|---|---|---|
| Wang, Jones & Wang 2019 | near-miss와 10년 NIH-system attrition | 12.6%의 의미, 절대수준/차이/상대효과 혼동 | 방향만 유지; 효과크기 보류 |
| Bol, de Vaan & van de Rijt 2018 | 8년 후속 연구비, €180k, 2배+, full-professor 결과 | 초기 grant 포함 여부, 회귀/기술통계, % vs %p | 원표 대조 전 숫자로 Project 효과 계산 금지 |
| Tham et al. 2024 | funding gap→US employment, earnings, publication | working-paper 판본, 3pp/40%, 20%, 90%의 정확한 outcome | 판본 고정 후 표/부록 대조 |
| Hill & Stein 2025 | scooping→citation/top-journal/publication | 상대%와 percentage-point 혼동 | 원표 대조 전 범용계수 금지 |
| Ross et al. 2022 | women credit gaps, survey exclusion | adjusted relative gap vs raw/pp, correction 반영 | 최신 correction 포함 후 확정 |
| Stavropoulou & Viney 2026 | funding→income/publication/citation, sex heterogeneity | outcome 정의·추정모형·새 논문 판본 | 원문/보충자료 대조 |
| university royalty study 2020 | royalty share와 patent/licensing output | 이전 coding error가 어느 연구/추정에 해당하는지 | 반증 방향만 유지 |
| Azoulay et al. 2011 | HHMI-style support와 high-impact/failure | selection adjustment와 causal language | association/design 범위 넘는 인과표현 금지 |
| Jacob & Lefgren 2011 | NIH grant effect on publications/topics | RD/IV 추정대상과 effect magnitude | '단순 비례 아님' 이상 확대 금지 |

## 검증 레코드 필수필드
- exact source/version/date
- authors
- DOI/persistent identifier
- population/sample
- treatment/exposure
- comparator/control
- outcome definition
- observation window
- raw rate if available
- absolute difference
- relative difference
- model-adjusted estimate
- uncertainty (SE/CI/p)
- table/figure/page
- correction/erratum
- what the paper **does not** establish
- Project claim affected

## 자동 강등 규칙
다음 중 하나면 숫자를 문서 본문의 확정 주장으로 사용하지 않는다.
1. 원문 표/그림 위치를 못 찾음.
2. 분모/모집단 불명.
3. %와 %p 구분 불명.
4. adjusted와 raw 혼재.
5. preprint/accepted/VOR 판본 혼재.
6. correction 존재 여부 불명.
7. 2차 기사·요약만 확인.
8. 연구비를 개인소득으로 변환.
9. 특정 분야 추정치를 전체 과학계 상수로 일반화.
10. 서로 다른 연구의 계수를 곱해 '소멸확률' 생성.

## 완료 기준
정량값마다 독립 검토자가 원문에서 동일 값을 재현할 수 있는 위치정보가 있어야 한다. 그렇지 않으면 **DIRECTIONAL EVIDENCE / EFFECT SIZE UNVERIFIED**로 남긴다.
