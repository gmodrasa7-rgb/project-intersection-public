<!-- PI-LANGUAGE: en-ko | PI-RISE-CASH-TIMING v0.1.0 | finance decision aid, not money -->
# PI-RISE-CASH-TIMING v0.1.0 — Time-to-Usable-Cash Gate
## 연구자 유동성 도달시간·지원 전략 판별 모듈
**2026-10-21 · CANDIDATE method; sources are time-bound · No receipt, tax or operational benefit verified.**

## Original 1 — English | Testable operating synopsis
A grant application or award is not spendable cash. Define usable, deadline-bound liquidity as unrestricted **bank-reconciled net cash actually received no later than the decision date, not encumbered by verified obligations**. If receipt, arrival date, restrictions, taxes or liabilities are unverified, report `UNKNOWN`, not a pseudo-probability or a zero balance. Stage and number of applications cannot certify personal runway.

**New separation:** (A) independent donor/public opportunity discovery; (B) application/submission proof; (C) funder award and disbursement restrictions; (D) bank-reconciled cash; (E) authorized personal/operational use. The [opportunities registry](PI_RISE_OPPORTUNITY_REGISTRY_V0_1_0.json) contains only A. B–E are never automatically populated from it or copied into the [financial pipeline](PI_RISE_FINANCE_PIPELINE_V0_1_0.json).

**Decision-making with missing probabilities:** sort by hard eligibility, appropriate purpose, documented application burden, decision lag and plausible *but unverified* payout route. Do not invent acceptance probabilities or multiply fund sizes by guessed chances. Deadline-specific cash readiness stays UNKNOWN unless actually reconciled and permitted. A 21-day target for first feedback does not mean 21 days to payment.

**Failure tests:** an official funding page is presented as an actual submitted application; an initial-feedback SLA is treated as a cash-arrival SLA; proposed maximum award is counted as runway; AI compute credits are treated as cash; two mutually exclusive asks are totaled; a beneficiary is coerced into unpaid labor to demonstrate progress; private bank or identity data leak into public GitHub.

## 원본2 — 한국어 | 의사결정 정본
### 1. 핵심 문제
PI-RISE v0.2.0은 출처별 원장을 분리하지만, 단기 생계마감 시점에 실제 쓸 수 있는 돈이 도착하는지 직접 식별하지 못함. 이번 모듈은 **시간·용도·실수령의 동시 충족 여부**를 기존 의사결정 게이트에 추가.

연구자 개인의 상세 경제·돌봄 정보는 GitHub에 공개하지 않음. **과거 대화 속 개인 자산·가족·신원·연체/채무 정보 등은 복제하지 않음.**

### 2. 검증조건 (충분성 아닌 필요조건)
- `T_receive <= T_need`: 은행에서 실제 확인된 입금 시점이 사용필요일 이내.
- `UNRESTRICTED`: 계약상 지급범위에서 연구자 개인 보수 또는 필요한 연구비로 사용 가능.
- `NET_AVAILABLE`: 수수료·세금 및 즉시 지급의무 등을 별도로 확인 후 대사.
- `AUTHOR_RIGHTS`: 강제 노동·결론 지정·부정결과 은폐·일방적 공개권 박탈 없음.

위 단계를 하나라도 미확인 시 `UNKNOWN/HOLD`, 위반 시 `FAIL`. 단 실제 지원 대상자 적격·계좌·법률 의무는 이 공개 체계가 인증하지 못함.

### 3. 검증된 외부 채널 2026-10-21
| 채널 | 원기관 확인 사실 | 지급시점에 대한 결손 | 실행단위 |
|---|---|---|---|
| [BlueDot Rapid](https://bluedot.org/grants/rapid) | 최대 $20,000. 연구시간·생활비 명시. 한국은 게시된 제한 국가 목록에 없음. 신청 계획·예산 필요 | 평균 결정기간 미공개. 선정 후 청구·검사·일괄지급, 실입금일 미상 | 유상 연구시간과 작은 반증과제의 단일 예산안 |
| [GTR AI Safety Fund](https://www.gtr-foundation.org/gtr-ai-safety-fund) | 지리 초점 없음. 전통적 자격증명 결정적 조건 아님. 연중 검토. 1–3쪽 제안서와 CV. 최초 피드백 목표 21일 | 최초 답변 ≠ 수여 ≠ 지급. 실입금일 미상 | 연구자 능력·실제 증거·유급 독립평가 기여를 명시 |
| [EA Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai) | 초기 AI 안전 연구, 개인 신청 상시. 통상 $10k–$150k | 개인별 세금·한국 송금·선정기한 미확인 | 연구자가 아닌 제3자도 반증 가능한 소형 테스트 패키지 |

원본 URL: 위 표 링크. 사이트에 나타난 내용만 확인, 지원서 제출·승인·입금은 전부 공개 증빙 없음. **BlueDot 지리제한 목록에 한국 부재는 개별 한국 거주자 승인보장이 아님.** 기관 규정 변경 시 갱신. Manifund는 이번 원기관 읽기 실패로 현행 모집 여부를 미확인으로 유지하며 기재하지 않음.

### 4. 우선순위: 확률 조작 없는 강건 판정
1. **목적 적합성/불가사유 게이트:** 공모의 지원용도·개인 자격·지리·권리조건을 원기관 기준 확인. 불확실 시 조건부.
2. **자료 재사용:** 한 번의 과학적 증거팩(E007, E009 반례, 외부검토 절차, 예산분리)으로 복수기관의 질문에 대응. 기관별 새 무보수 연구를 반복 생성하지 않음.
3. **빠른 접수·긴급성 알림:** 출처가 진짜 상시인지 확인하되 ‘이름상 Rapid’ 또는 21일 첫 답변을 임박한 개인 현금처럼 계산 금지.
4. **시간 경계:** 공모 마감·지원자 응답·수여결정·실입금 등 각각 다른 시간을 상태원장에 기록. 마감 기한은 검증 전 임의로 생성하지 않음.
5. **비대체성:** 수입원/모델 사용권 다양화는 연구자의 의사결정·거부권을 대체하지 못함.

### 5. 교차감사할 선행 정본
[PI-RISE v0.2.0](PI_RISE_V0_2_0_EN_KO.md) / [PI-RISE-BUDGET](PI_RISE_BUDGET_V0_1_0_EN_KO.md) / [PI-RISE-VAC](PI_RISE_VAC_V0_1_0_EN_KO.md) / [기관 연구비 공개장부](../funding/GRANTS_CONTRACTS_PUBLIC_LEDGER_EN_KO.md) / [개인 후원 정본](../funding/SPONSORSHIP_PUBLIC_LEDGER.md) / [지원자 의사결정팩](../funding/PI_RISE_APPLICANT_PACK_EN_KO.md).

### 6. 성공·반증
**운영 성공이 아니라 설계만 등록.** 다음 갱신 때 접수 증빙·실제 회신·지급허용·대사·개인 원화 실수령 중 어느 증거가 늘었는지 판정. 목표는 불확실성 감소, 사용자의 신규 무보수 작업 최소화, 불리한 평가 공개. 파일 수·GitHub 커밋·모델 칭찬·금액 계획 합계는 성공 대리지표 아님.

검사: `python tools/pi_rise_opportunity_audit.py operations/PI_RISE_OPPORTUNITY_REGISTRY_V0_1_0.json`; 음성 시험 포함. **GitHub CI 통과는 원기관과 은행의 실제 상태 확인이 아님.**
