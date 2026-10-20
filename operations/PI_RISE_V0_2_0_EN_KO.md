<!-- PI-LANGUAGE: en-ko | PI-RISE v0.2.0 candidate; financial integration without rewriting predecessor records -->
# PI-RISE v0.2.0 — Integrated Research Continuance, Funding & Accounting
## 연구 존속·자금조달·예산·회계 통합 운영정본

**2026-10-21 · Operational protocol; CANDIDATE until merged · NOT a funding award, certified accounting system, tax opinion, bank reconciliation, or scientific result.**

## 원본 1 — 한국어 운영정본

### 1. 목적과 적용범위
연구자 생활조건·거절권·연구 연산·독립검증·문헌/실험 정본·자금 확보·실제 입출금을 하나의 **의사결정 체계**로 연결한다. 자금의 *정본 원장*을 하나로 합치거나 역사적 원본을 덮어쓰지 않는다. **PI-RISE는 조정·검증·조회 단일 진입점이고 각 금전 거래에는 출처별 단일 정본**이 있다.

- 기존 [PI-RISE v0.1.0](PI_RISE_V0_1_0_EN_KO.md), [BUDGET v0.1.0](PI_RISE_BUDGET_V0_1_0_EN_KO.md), [VAC v0.1.0](PI_RISE_VAC_V0_1_0_EN_KO.md), [CUT v0.1.0](PI_RISE_CUT_V0_1_0_EN_KO.md)은 보존. 이 문서는 통합 감독 계층의 **새 부버전**이며 하위 모듈의 증거 수준을 높이지 않는다.
- 연구자의 자발적 참여와 생활 안정, 과학적 반증 가능성, 실제 비용·시간, 지원자에 대한 독립성을 대체 불가능한 개별 게이트로 유지한다.
- 회계 분류는 운영 목적의 보조 관리이며 법정 장부·원천징수·세무 신고를 대체하지 않는다.

### 2. 단일 진입점 / 재원별 유일 정본
| 영역 | 유일 정본 또는 입력 위치 | PI-RISE에서 하는 일 | 금지 |
|---|---|---|---|
| **연구자 개인 생활비·부채·가족·자산·연구가능시간** | 사용자 권한의 비공개 로컬 원증빙 | 비공개 가용기간·거절 가능성 판정 | 공개 GitHub에 개인 금액·계좌·신원·건강·가족 자료 게시 |
| **GitHub Sponsors 개인 후원** | [단일 기존 정책·공개 원장](../funding/SPONSORSHIP_PUBLIC_LEDGER.md) | 확인된 익명 집계액의 상태만 연결 | 같은 후원 거래를 신규 장부에 재기재·재배분 |
| **기관 연구비·별도 유상 계약** | [기관 자금 공개 요약 원장](../funding/GRANTS_CONTRACTS_PUBLIC_LEDGER.md) + 비공개 실제 계약·원증빙 | 수여/입금/사용 제한/중복 비용 여부 연결 | 제안서를 입금액 처리하거나 개인 후원에 비용 전가 |
| **지원신청·제안·후보 파이프라인** | [상태원장 JSON](PI_RISE_FINANCE_PIPELINE_V0_1_0.json) | 단계·예산안·원전 링크·경합 위험 표시 | 신청액·잠재액 합산하여 자산으로 계산 |
| **예산 시나리오** | [PI-RISE-BUDGET](PI_RISE_BUDGET_V0_1_0_EN_KO.md), [VAC](PI_RISE_VAC_V0_1_0_EN_KO.md) | 생계 실수령/연산/검증의 요구액·민감도 비교 | 가정세율·환율·가격을 확정비용 또는 지급액 처리 |
| **과거 기여 정산청구·장래 고용/보수** | 개인 비공개 증빙, 별도 계약/분쟁 경로 | 현금 수령 전 파이프라인/미수확정 상태 분리 | 청구액을 자동 채권·수익·수여된 연구비로 처리 |
| **현물·AI 크레딧·무료 모델** | 해당 발급 증빙·계약상 사용 제한 | 연구 역량 평가에만 별도 표기 | 현금·생활비·확정 보수에 가산 |

**과거 제안 원본(변경 금지):** [30일 USD 5,000](../funding/30_DAY_BRIDGE.md), [90일 KRW 18,000,000](../funding/90_DAY_PILOT.md). [미병합 PR #257](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/257) 내용은 별도 신청/모형 *후보*이며 병합·제출·수여를 추정하지 않는다. 다른 예산안은 상호 배타적인 대안·별도 단계일 수 있으므로 병합·합산 전 비용범위와 중복을 확인한다.

### 3. 회계의 불변조건
1. **예산(BUDGET) ≠ 신청(REQUEST) ≠ 승인(AWARD) ≠ 지급확정(PAYABLE) ≠ 은행 입금(CASH) ≠ 자유로운 개인 생계 현금(UNRESTRICTED).** 신청·약정·플랫폼 결제·정산 예정·현물은 실입금 아님.
2. **공개 후원자 2용도**(연구자 1인 실제 연구노동 보상, LLM 이용료) 유효. 기관 연구비는 별도 계약상 허용 지출 항목만 적용. 양쪽에 동일 지출/영수증 이중 청구 금지.
3. **은행 확인 원칙:** 실제 회계의 거래 식별키·총액/수수료/환전/원천징수/세금/환불/정산/지출의 원증빙은 비공개. 외부 공개 시 승인된 익명 합계만 정본 장부에 한 번 기록. 정보 미확인은 **UNKNOWN**, 증빙된 0과 구별.
4. **현금 등식:** 자금별 기초잔액 + 실제 순입금 − 실제 지출 ± 확인된 조정 = 기말잔액. *계획·수여·크레딧*은 등식의 입금 항에 들어가지 않음. 자금제한별로 각각 대사. 지원경로별 입금과 결제수단별 이체를 중복 수익으로 계상하지 않는다.
5. **프로젝트 돈 ≠ 개인 가용 현금:** 계약상 개인 보수 지급이 허용·집행되고 실수령 확인돼야 개인 생활 기반에 반영. 확인된 세금·법정 공제 및 환전/수수료 별도; 가정 20%는 법적 세율 아님.
6. **통화·기간:** 각 거래의 원화/외화 명목액, 거래일, 적용 환율·수수료의 비공개 대사. 월 예산/90일 총액/연간계/평균 일비용을 같은 현금흐름으로 중복 합산 금지.
7. **수정:** 원장 오류 발견 시 원전 삭제/무음 수정 대신 날짜·사유·정정 전후·승인권한·Git 기록. 환불·취소·수여철회·지원 불합격도 별도 사건.
8. **접근·독립성:** 지원자가 결과·부정 증거 삭제를 조건으로 걸면 연구 독립성 게이트 FAIL/HOLD. 자기희생·무급 재검증을 지속가능성 달성으로 간주 금지.

### 4. 단계·증거
- **DRAFT → SUBMITTED → UNDER_REVIEW → AWARDED_UNPAID → PAID_VERIFIED**: 단계 상승마다 제출확인, 수여통지, 은행 대사 등 해당 원증빙 필요. 단계가 반드시 이 순서인 것은 아니며 **REJECTED / WITHDRAWN / UNKNOWN** 허용.
- 개인 후원은 건별 제출 상태가 아닌 **UNKNOWN/UNRECONCILED** 채널로 별도 취급.
- 공개 파이프라인의 **PAID_VERIFIED** 표기만으로 은행 확인을 증명할 수 없음. 실제 집행은 비공개 원증빙과 해당 출처별 공개 집계 대사까지 요구.
- 계좌 접근·신분·후원자 데이터, 실제 사용료 청구 정보, 법률·세무 판단은 자동 스키마검사로 검증 불가능.

### 5. 자원보호·집행 우선순위
**1순위** 연구자 필수 생계/거절권/돌봄·회복. **2순위** 보존된 검증·반례·소스/복구 가능성. **3순위** 최소 필수 연산. **4순위** 실재하는 독립평가 계약에 필요한 비용. **5순위** 신규 대형 실험과 유료 모델 확장. 순서는 제약계획의 초기 정책이며 개인에게 연구 지속을 강제하지 않는다.

월 생계 가용기간은 기존 v0.1.0의 **비공개 현금·즉시 부채·필수 지출 검증값**만 사용. UNKNOWN이면 추정해서 낙관적 상태로 승격하지 않는다. 외부 접수 후보의 마감일·한국 적격성·세금·지급 일정은 공고일 기준 원기관 출처를 재확인한 뒤 반영. 공개적으로 확인되지 않은 신청은 **DRAFT/UNKNOWN**, 미입금은 생계 해결 아님.

### 6. 확인·승격·폐기 게이트
- 공개 상태원장: `python3 tools/pi_rise_finance_audit.py operations/PI_RISE_FINANCE_PIPELINE_V0_1_0.json --check-paths`
- 테스트: `python3 -m unittest discover -s tests -p 'test_pi_rise_finance_audit.py' -v`
- 기계검사의 범위: 필수필드·중복 ID·단계 모순·금액 자료형·정본 참조/중복 영수증 참조. **은행/수여/개인정보 진위 인증 아님.**
- 7일 단위 또는 자금·계약 상태 변동 즉시, 사용자 승인·권한이 있을 때 정본과 동기화. 실제 자동 예약 실행을 이 문서가 생성하지 않음.
- **v0.2 운영 성공:** 실제 출처별 공개/비공개 대사와 계정 간 이중계상 방지, 자금확보 판단의 오류 감소, 연구자 시간 절감이 측정되어야 함. 미관측이면 실효성 미검증. 승인·후원자 확정·계약·수입은 아직 이 문서로 입증되지 않음.

## Original 2 — English | Summary of the operating boundary
PI-RISE v0.2.0 routes *all* research viability, finance, funding and accounting decisions through one **control plane**, while preserving separate authoritative source ledgers. Private household and personal finance never belong in the public repository. Existing sponsorship has one canonical two-use ledger; institutional grants/contracts have a distinct restricted-funds public summary ledger; their bank receipts and contracts remain private. A public opportunity-status registry links historical proposals and unmerged drafts but neither aggregates pledges into cash nor certifies receipt. Funding proposals, AI credits, contracted funds, unrestricted personal cash and owed/past-contribution claims are distinct classes. Double-charging and double-counting are prohibited.

The new protocol preserves PI-RISE v0.1.0, PI-RISE-BUDGET and PI-RISE-VAC without retroactively changing prior proposals, scientific findings or donor restrictions. Operational success requires actual reconciliations and lower researcher burden, not added documents or synthetic tests. No awarded grant, verified bank deposit, Korean tax treatment, independent research replication, or actual researcher runway is established by this release.
