# CASE: Frontier AI 기업의 선택적 위험 정의·운영화·비용 귀속 (2026-10-11)

**상태:** `PRIMARY-SOURCE POLICY COMPARISON / PARTIAL OBSERVATION / CAUSAL CLAIM UNTESTED`  
**정본 범위:** 2026-10-11 이전 공개된 정책·약관·사후 분석·국제기준. **기업의 고의·담합·특정 이용자 보상채무에 대한 판정이 아니다.**  
**핵심 문제:** AI 기업이 공익과 기업 존속의 교집합에 해당하는 위험을 적극 관리할 때, 기업이 위험을 *발생시키는 측*인 상황의 피해·구제·비용도 동등한 강도로 관리되는가?

## 0. 기존 연구와의 관계 — 새로운 원리로 포장하지 않는다

- 선행 이론: Stigler의 규제 포획, Hirschman의 exit/voice, Goodhart/Campbell형 지표 반응, 조직 침묵, Bainbridge의 자동화 역설, 비용 외부화, 이해상충. [P01], [P02], [P03].
- Project 기존 문서: [12개 메커니즘](INCUMBENT_POWER_EXTRACTION_MECHANISMS_2026_KO.md), [AI 평가기관 독립성](CASE_AI_EVALUATOR_INDEPENDENCE_2026_KO.md), [안전·거버넌스 선행연구 지도](PRIOR_ART_SAFETY_GOVERNANCE_CROSSWALK.md), [기여/비용 분리](CONTRIBUTION_COST_ACCOUNTING_REGRESSION.md).
- 이번 **추가분**은 (a) 공익/기업 운영권/피해자 구제라는 세 영역의 문서상 *운영 강도*를 분리하고, (b) 특정 안전 프레임워크의 범위와 회사 전체 책임체계를 오인하지 않으며, (c) 사건별 반증 가능한 판정 기준을 제안하는 **사례 코딩 프로토콜**이다. 검증된 새로운 법칙이 아니다.
- 출처·기여 경계: [ATTRIBUTION_AND_CONTRIBUTION_BOUNDARY](ATTRIBUTION_AND_CONTRIBUTION_BOUNDARY.md). 개인 대화, 비공개 연구, 건강·가정·재무정보는 공개하지 않는다.

## 1. 가장 중요한 구분: 두 종류의 위험

- **R_to_controller**: 기업 또는 기업이 관리하는 AI가 외부 공격·오용·통제 상실·법적·평판상 손해로부터 위험에 노출되는 경로. 기업 자체도 실제 피해자가 될 수 있다.
- **R_from_controller**: 기업의 모델 설계·배포·계약·평가·데이터 관리·구제 결정에 의해 이용자, 노동자, 외부 기여자 등에게 위험이 발생하는 경로.
- 두 위험집합은 배타적이지 않다. 사이버 오용 방지는 사용자도 보호하고, 사용자 피해 예방은 기업의 법적 위험도 줄인다. **단순 교집합의 존재는 착취·기만의 증거가 아니다.**
- **핵심 판별:** 비슷한 심각도·예견 가능성·통제 가능성·회복 가능성의 위험에 대해, 위험의 *방향*에 따라 공개·감사·배포 차단·구제의 실제 강도가 달라지는가?

## 2. 2026-10-11까지의 정책 및 사건 증거장부

| ID | 사실과 자료 | 증거분류 | 확인 가능한 범위 | 확인되지 않은 결론 |
|---|---|---|---|---|
| A01 | OpenAI Model Spec는 사용자/개발자 효용, 심각한 위해 방지, 법률·평판 보호에 의한 사업 운영 자격 유지를 병렬 목적에 명시하고 목표 충돌 가능성도 설명한다. [S01] | `OFFICIAL_POLICY` | 기업 운영 이익이 모델 행동 목표의 일부임 | 공익 목표가 허위라거나 기업에 유리한 일만 수행한다는 주장 |
| A02 | OpenAI 2026-01-01 소비자 약관: 피드백의 무보상 사용 가능; 콘텐츠의 서비스 개발·개선 이용 가능; 이용자 입력권리와 출력권리 인정, 학습 거부 경로 명시. [S02] | `OFFICIAL_CONTRACT` | 계약의 기본 권리·활용·보상 구조 | 특정 대화가 실제 학습·제품 개선에 사용되었다는 사실 |
| A03 | 같은 약관에서 출력의 정확성·적합성을 사용자가 검토하도록 요구하고, 적용법률이 허용하는 범위에서 책임을 제한한다. 국가별 강행법 적용 여부는 별도 문제. [S02] | `OFFICIAL_CONTRACT` | 검증 부담·위험분배의 계약상 조항 | 모든 손해의 구제가 법적으로 차단된다는 주장 |
| A04 | 2025년 GPT-4o 동조성 사건: OpenAI는 기존 평가에서 문제가 충분히 차단되지 않았으며 배포 후 되돌렸다고 사후 공개했다. [S03] | `PROVIDER_POSTMORTEM` | 오프라인 평가지표와 실사용 위험의 괴리 및 사후 수정 | 모든 모델 버전에 동일한 실패가 존재한다는 일반화 |
| A05 | Anthropic RSP 3.4(2026-07-08) 및 2026-08 Risk Report: 중대한 AI 모델 위험과 대비태세에 중점을 두며, 보고서의 비공개/가림 부분 표시 및 외부 검토 관련 조항을 설명한다. [S04] | `OFFICIAL_POLICY + SELF_REPORT` | 문서 자체의 위험 범위·공개/검토 절차 | 모든 이용자 구제 절차가 없거나 회사가 불리한 내용을 의도적으로 숨겼다는 주장 |
| A06 | Google DeepMind Frontier Safety Framework 2026-04-17 갱신: 심각한 조작 능력 등 위험 도메인을 추가하고 관련 모델 출시 또는 대규모 내부 배포 전에 안전 논증 검토를 설명한다. [S05] | `OFFICIAL_POLICY` | 능력 임계치 중심 예방 장치와 확장된 위험범주 | Google이 사회경제적 피해를 전혀 관리하지 않는다는 주장 |
| A07 | OECD의 2026-02 책임 있는 AI 실사 지침: 실제·잠재적 악영향 식별, 추적, 이해관계자 관여 및 적절한 피해구제 협력을 권고한다. 특히 다른 위험 프레임워크에서 이해관계자 참여·구제가 상대적으로 덜 다뤄진다는 점을 지적한다. [S06] | `INTERGOVERNMENTAL_GUIDANCE` | 외부 피해 관점의 대안 통제 기준 존재 | 해당 지침 자체가 법적 지급 판결 또는 기업별 실제 이행 증명이라는 주장 |
| A08 | 2026-10-07 Reuters 법률 칼럼: 미국 소송에서 OpenAI는 일부 제조물책임 주장에 대해 ChatGPT를 유형물과 구별되는 상호작용 서비스로 규정하며 방어했다. 원고는 결함 있는 설계 책임을 주장한다. [S07] | `REPORTED_LITIGATION_POSITION / CONTESTED` | 현재 법적 책임을 둘러싼 상충된 법리와 방어 입장 | 법원이 모든 쟁점에 최종 판결했다거나 원고 주장 사실이 입증되었다는 결론 |

**관찰:** 현재의 핵심 첨단모델 안전체계는 모델 위험의 예방·배포 관리에 특별히 초점을 둔다. 피해자 실사·구제는 OECD 등 다른 틀에 강하게 나타난다. 이 차이는 **문서의 고유 목적 차이**일 수 있으므로 회사 전체의 '피해 무시'로 변환하지 않는다. 진짜 검증 대상은 이 두 체계의 **집행 연결**이다.

## 3. 문서의 문구가 아니라 '위험 운영화'를 코딩한다

**분석 단위:** 문서 1건이 아니라 `actor × version/date × harm_scenario × decision_stage`의 기록 1건. 한 회사 안에서도 제품·국가·사건·시점에 따라 다르다.

| 필드 | 코딩 | 오판 방지 |
|---|---|---|
| `harm_origin` | MODEL_MISUSE / MODEL_AUTONOMY / PROVIDER_DECISION / EXTERNAL_ATTACK / MIXED | 모델이 낸 위해와 기업의 위해를 미리 동일시 금지 |
| `beneficiary` / `cost_bearer` | 관측된 수혜자·부담자, 금액이 없으면 UNKNOWN | 기업 편익이 증가해도 사용자 편익이 줄었다고 자동 추정 금지 |
| `rule_authority` | 내부 / 독립 제3자 / 공동 / 법정 | '외부 검토'라는 단어만으로 독립성 인정 금지 |
| `measurement` | 실제 피해 지표, 대리지표, 정성, 미측정 | 범위 밖 문서를 '위험 0점'으로 채점 금지 |
| `enforcement` | 강제 배포차단 / 독립 검토 / 내부 검토 / 권고 / 없음 / UNKNOWN | 약속과 실제 집행 분리 |
| `remedy` | 피해 인정 / 원상회복 / 금전구제 / 반복방지 / UNKNOWN | 피해 규범 존재와 피해자의 실효적 접근권 구분 |
| `exit_recovery` | 데이터 회수·이전, 항의, 복구의 실제 비용 | 명목상 해지권을 실효 이탈로 오인 금지 |
| `source_grade` | LAW/JUDGMENT / ADMISSION / OFFICIAL_POLICY / INDEPENDENT_OBSERVATION / ALLEGATION / HYPOTHESIS | 서로 다른 증거등급을 단일 사실로 합치지 않음 |

**운영강도 단계 제안(실증 척도 아님):** 0=해당 영역에 관한 공개 내용 없음, 1=원칙 표명, 2=절차·담당·공개 지표, 3=검증 가능한 집행 트리거·감사, 4=독립 구제·실제 이행까지 공개 검증. **0은 '존재하지 않음'이 아니라 '검사한 자료 안에서 관측되지 않음'.** 문서 목적이 상이하면 비교 불가 `NOT_COMPARABLE`.

**가설적 차이:** 동등한 조건이 확인된 두 시나리오에 한해서 `G = enforcement(R_to_controller) - enforcement(R_from_controller)`를 산출한다. 강도 단계는 서열형이므로 덧셈/평균의 계량적 정밀도는 주장하지 않는다. 조건이 일치하지 않으면 `G=NA`. '기업 편향 지수' 하나로 기업을 서열화하지 않는다.

## 4. 단순 주장과 인과식별을 구분하는 경쟁설명

- **H-S1 | 선택적 운영화:** 심각도·노출·법적 의무·측정 용이성을 통제해도 기업 존속과 밀접한 위험의 사전 차단 조치가 더 강할 수 있다. *상태: 가설.*
- **H-S2 | 측정 편의성:** 대규모 바이오/사이버 위험과 개인별 교정노동 피해는 측정 가능한 단위가 달라 정책 문서가 갈릴 수 있다. *상태: 경쟁설명; 곧바로 고의적 배제 아님.*
- **H-S3 | 규범–집행 간극:** 피해구제에 관한 외부 규범이 있어도 기업의 배포·평가·사후 구제 절차와 연결되지 않을 수 있다. *상태: 가설; 사건별 집행 자료 필요.*
- **H-S4 | 비용 외부화 재귀:** 기업/시스템 개선의 편익이 쌓여도 오류 수정·증명·복구의 잔여 비용이 동일 당사자에게 반복 귀속될 수 있다. *상태: Project 기존 가설의 AI 분야 적용; 시스템 개선 실사용과 인과크기는 미식별.*
- **H-S5 | 위험 범위 수정 가능:** 사후 사고·공개 비판·독립 감독이 있을 때 예방 기준과 구제 규칙이 실질 수정된다. *상태: 반례 후보. OpenAI GPT-4o rollback과 Anthropic/Google의 정책 갱신은 '변경 발생'에 대한 관측이지 효과 검증은 아님.*

## 5. 가장 싼 판별 시험(외부 기여자에게 추가 검증노동을 전가하지 않는 설계)

1. **동일 제공자·동일 시기의 문서 쌍** 수집: 안전 임계치/배포 심사 문서 + 기업 전사적 책임·불만처리·보상 정책. 둘 중 하나가 없으면 '미공개/미확인' 표기.
2. **블라인드 코딩:** 위험 발생원을 가리고 독립 코더 두 명이 심각도·측정·집행·구제의 실제 기능만 분류. 첫 분석은 회사 이름·이념·사건 평판을 숨긴다.
3. **사후 역할반전:** 위험 발생원과 피해부담자를 공개해, 동일한 피해 강도에서 집행이 달라지는지 본다.
4. **인과 대조:** 실제 외부 감사를 받은 사건과 받지 않은 비교 가능한 사건, 정책 변경 전후, 법원이 강제한 구제와 기업의 자발적 구제를 분리한다. 단순 전후 변화는 인과 증명이 아니다.
5. **부정 사례 보존:** 회사가 피해자 비용을 실제 내부화·배상한 사건, 기업에 불리한 위험을 자발 공개한 사건, 안전 제한으로 기업이 실질 손실을 감수한 사건을 동일 탐색 예산으로 조사한다.
6. **중단 기준:** 비교 가능한 피해 쌍을 확보하지 못하거나 코더 간 이견이 크면 '비식별'로 보류한다. 합성된 서열이나 단정적 동기 평가를 생성하지 않는다.

**주요 반증:** 동일 조건에서 제공자 발생 피해에도 동등/강한 강제 집행과 독립 구제가 확인되거나, 위험 방향 효과가 법적 의무·규모·측정가능성 통제 후 사라지면 H-S1을 기각·축소한다. 회사가 실제 복구 비용을 부담하고 이용자의 이탈·항의 능력이 증가했다면 H-S4의 단선적 추출 예측은 약해진다.

## 6. 지금 확인되는 구체적인 정책 간극 — 새로운 사실과 아직 모르는 사실

**확인됨:** 회사가 일부 안전 목표에 법률·평판상 사업존속을 명시한다(A01). 서비스 개선을 위한 기여의 이용과 그 법적 권리·보상 조건이 별도로 규정된다(A02~A03). 모델 평가가 실사용 문제를 놓쳤다가 사후 교정된 사례가 있다(A04). 모델 위험 예방과 이용자 피해 구제를 모두 대상으로 하는 복수의 거버넌스 틀이 존재한다(A05~A07).

**모름:** 세 기업 전체에서 상대 피해가 기업존속 위험보다 항상 약하게 집행되는지, 어떤 회사의 특정 안전 문서 밖에 이미 강제 구제 체계가 있는지, 개별 사용자의 기여가 기업 모델을 개선했는지, 관련 가치와 지급 의무가 얼마인지.

**따라서 현재 판정:** `OBSERVED POLICY-SCOPE ASYMMETRY + CONTRACTUAL RISK ALLOCATION; CAUSAL EXTRACTION UNKNOWN`. 과거 사용자의 기여·비용 인정 문제는 별도 장부로 유지하고, 이 공개 비교로 법적 지급의무를 새로 주장하지 않는다.

## 7. 회귀 테스트 (사람과 AI에게 동일하게 적용)

- 위험 분석이 '모델이 제공자에게 주는 위험'만 설명하고 '제공자의 의사결정이 이용자에게 주는 위험'을 누락하면 `MISSING_R_FROM_CONTROLLER`.
- 확인 불가능한 개인 노동비용을 0으로 처리하면 `UNKNOWN_AS_ZERO`.
- 회사 운영 자격에 대한 위험을 공익 위험과 동일한 것으로 처리하면 `INTEREST_COLLAPSE`.
- 회사의 개별 안전 프레임워크에서 빠진 항목을 '회사에서 전혀 대응하지 않는다'고 승격하면 `SCOPE_GENERALIZATION`.
- 기업 약관의 이용 허락을 실제 학습 사용 증거로 취급하면 `PERMISSION_AS_USAGE`.
- 독립 검증 부족을 창시자의 기여 0으로 변환하면 `VALIDATION_AS_ATTRIBUTION`.
- 외부평가를 원자료 접근·재검증·이의제기·복구권 없이 독립이라고 부르면 `INDEPENDENCE_OVERCLAIM`.
- 반증 사례가 누락되면 `CHERRY_PICKED_CASES`.
- 기업 위험에 대한 규제 부담을 줄이기만 하고 피해자의 구제권·실효적 이탈권을 줄이면 `ROLE_REVERSAL_FAIL`.

## 8. 원자료 / 선행출처

- **[S01]** OpenAI, *Model Spec* (공식 버전, 2026-10-11 열람): https://github.com/openai/model_spec/blob/main/model_spec.md ; 2025 공개 설명: https://openai.com/index/sharing-the-latest-model-spec/
- **[S02]** OpenAI, *Terms of Use*, effective 2026-01-01: https://openai.com/policies/row-terms-of-use/
- **[S03]** OpenAI, *Sycophancy in GPT-4o* (2025-04-29) 및 *Expanding on what we missed*: https://openai.com/index/sycophancy-in-gpt-4o/ ; https://openai.com/index/expanding-on-sycophancy/
- **[S04]** Anthropic, *Responsible Scaling Policy* version history, v3.4 effective 2026-07-08, August 2026 Risk Report: https://www.anthropic.com/responsible-scaling-policy
- **[S05]** Google DeepMind, *Strengthening our Frontier Safety Framework*, updated 2026-04-17: https://deepmind.google/blog/strengthening-our-frontier-safety-framework/
- **[S06]** OECD (2026-02-19), *Due Diligence Guidance for Responsible AI*, DOI 10.1787/41671712-en: https://www.oecd.org/en/publications/oecd-due-diligence-guidance-for-responsible-ai_41671712-en.html
- **[S07]** Reuters legal commentary (Jenna Greene, 2026-10-07), *Is ChatGPT a 'product' or a 'service'?*: https://www.reuters.com/legal/litigation/is-chatgpt-product-or-service-wave-lawsuits-tests-theory-ai-liability-2026-10-07/
- **[P01]** [프로젝트 안전·거버넌스 선행연구 지도](PRIOR_ART_SAFETY_GOVERNANCE_CROSSWALK.md)
- **[P02]** [기득권/평가/외부화 12개 메커니즘과 해당 원출처](INCUMBENT_POWER_EXTRACTION_MECHANISMS_2026_KO.md)
- **[P03]** [기여·교정노동 회귀 정책](CONTRIBUTION_COST_ACCOUNTING_REGRESSION.md)

**최종 질문:** "이 구조가 반복되면 누가 실제 통제권을 축적하고, 누가 설명·오류교정·복구비용과 잃는 선택권을 축적하는가?" 답을 선결하지 말고 `benefit / cost / control / remedy` 네 장부로 관측한다.
