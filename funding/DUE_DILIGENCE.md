# Research Funding Due Diligence
## 연구비·후원 실사 기준

Review date / 검토일: **2026-10-04**
> **2026-10-13 governance update / 현행 운영 참고:** [Single two-category individual sponsorship policy and ledger](SPONSORSHIP_PUBLIC_LEDGER.md) · [Korean legal/tax risk register](LEGAL_TAX_RISK_REGISTER_2026-10-13_EN_KO.md). This supplement does not represent a legally cleared fundraising route or verified payout. / 신규 개인 후원은 별도 2항목, 이전 연구비 제안은 기존 약정 예산과 분리, 실제 입금 미확인.


---

## Original 1 — English Canonical

### Current funding fit

The project is currently structured for:

- research grants;
- philanthropic or individual sponsorship;
- paid research partnerships;
- benchmark / evaluation collaborations;
- support for independent review, reproduction, and documentation.

### What funding is for

External support is intended to increase the amount of research that can be independently checked.

Priority uses include:

1. protected research and engineering time;
2. API / compute / tooling;
3. external adversarial review or rerun where feasible;
4. documentation, packaging, and reproducibility work;
5. provenance, correction, and negative-result preservation.

### Evidence boundary

Requested or planned support is not counted as secured funding.

A public artifact, passing test, model agreement, or repeated internal run is not automatically upgraded into independent evidence.

Project reruns, third-party reruns, lineage-separated review, independent implementation, and empirical validation remain separate evidence classes.

### Sponsor-independence rule

A funder or sponsor may influence:

- which research question receives resources;
- schedule;
- reporting cadence;
- deliverable format;
- collaboration scope.

A funder or sponsor does not receive authority to:

- change an unsupported claim into a supported one;
- suppress a negative result as a funding condition;
- relabel a project-internal rerun as independent replication;
- remove an inconvenient counterexample from the public record;
- treat continued funding as evidence that a theory is correct.

### IP / license status

No root `LICENSE` file was observed in the public repository during this review.

Public visibility therefore should not be interpreted as a clearly granted downstream reuse license. Any future license should be chosen deliberately according to the intended reuse, research, and commercialization boundary.

### Verification priorities

The highest-value next steps are:

- independent rerun of released public packages;
- lineage-separated critique;
- independent implementation of narrow claims where feasible;
- public negative-result and correction records;
- empirical or historical validation with explicit identification limits;
- lower dependence on private conversation history for reproduction.

### Funding integrity condition

The research should become **more falsifiable and more externally auditable** as support increases.

If added funding instead increases dependence on the founder, hides negative results, weakens provenance, or increases verification cost, the funding structure has failed its stated purpose.

Funding must also avoid shifting repeated proof, correction, reconstruction, or valuation-repair work back onto the same contributor while the receiving side compounds capability. Apply the [Contribution-Cost Accounting & Correction-Labor Regression Test](../CONTRIBUTION_COST_ACCOUNTING_REGRESSION.md) when evaluating contributor burden, exit, provenance, and past-vs-future work boundaries.

---

## 원문2 — 한국어 대응본

### 현재 적합한 지원 형태

현재 프로젝트는 다음 형태를 기준으로 구성한다.

- 연구 그랜트;
- 개인·재단 후원;
- 유상 연구 파트너십;
- benchmark / evaluation 협업;
- 독립 검토·재현·문서화를 위한 지원.

### 자금의 사용목적

외부지원은 외부에서 실제 확인할 수 있는 연구량을 늘리는 데 사용한다.

우선 사용처는 다음과 같다.

1. 보호된 연구·엔지니어링 시간;
2. API / compute / 도구;
3. 가능한 경우 외부 적대검토·재실행;
4. 문서화·패키징·재현성 작업;
5. provenance·교정·negative result 보존.

### 증거 경계

요청·계획 단계의 지원은 확보자금으로 계상하지 않는다.

공개 artifact, 테스트 통과, 모델 간 합의, 내부 반복실행도 자동으로 독립증거가 되지 않는다.

프로젝트 내부 재실행, 제3자 재실행, 계보분리 검토, 독립구현, 현실검증은 서로 다른 증거등급으로 유지한다.

### 후원자와 연구판정의 분리

자금 제공자·후원자는 다음에 영향을 줄 수 있다.

- 어떤 연구질문에 자원을 투입할지;
- 일정;
- 보고주기;
- 산출물 형식;
- 협업 범위.

그러나 다음 권한을 갖지 않는다.

- 미지지 주장을 지지된 주장으로 변경;
- 지급조건으로 negative result 비공개 요구;
- 프로젝트 내부 재실행을 독립복제로 재표기;
- 불리한 반례를 공개기록에서 제거;
- 지원 연장을 이론의 참 증거로 사용.

### IP / 라이선스 상태

이번 검토에서 공개 저장소 루트의 `LICENSE` 파일은 확인되지 않았다.

따라서 공개되어 있다는 사실을 명확한 재사용권 부여와 동일시하지 않는다. 향후 라이선스는 의도하는 재사용·연구·상업화 경계에 따라 별도로 결정해야 한다.

### 검증 우선순위

가치가 높은 다음 단계는 다음이다.

- 공개 패키지의 외부 재실행;
- 계보가 분리된 비판;
- 가능한 경우 좁은 주장에 대한 독립 구현;
- negative result와 수정기록 공개;
- 식별한계를 명시한 현실·역사 검증;
- 재현 과정의 사적 대화기록 의존도 감소.

### 자금 무결성 조건

지원이 증가할수록 연구는 **더 반증 가능하고 더 외부 감사 가능**해져야 한다.

추가 지원이 오히려 창시자 의존을 키우고, negative result를 숨기고, provenance를 약화하고, 외부 검증비용을 증가시킨다면 그 지원구조는 목적에 실패한 것이다.

또한 수혜측의 능력은 누적되는데 같은 기여자에게 반복 증명·교정·복구·평가오류 수정비용이 되돌아가는 구조를 피해야 한다. 기여자 부담, 종료권, provenance, 과거기여와 미래노동의 분리를 평가할 때 [기여-비용 계상 및 교정노동 회귀 테스트](../CONTRIBUTION_COST_ACCOUNTING_REGRESSION.md)를 적용한다.


---

## 2026-10-15 evidence-based funding-route audit — Original 1 English
**Status:** Time-bounded desktop due diligence; public-source checks only; no new funding application submitted, award made, transfer verified, real-world replication, or legal/tax clearance. Source pages can change. This appendix does not modify the historical USD 5,000/30-day bridge, KRW 18,000,000/90-day pilot, or the separate two-use GitHub Sponsors policy.

### 1. Evidenced routes, eligibility, and unknowns

| Route / primary source | Evidence as of 2026-10-15 | Fit and gate |
|---|---|---|
| [BlueDot Rapid](https://bluedot.org/grants/rapid) | **Current live page: up to USD 20,000**, ~15-minute application; lists research time, living costs, computation and tools. South Korea not on its published prohibited-jurisdiction list. An older/indexed text showed a conflicting USD 10,000 cap; use the live detailed page, recheck before submitting. | First candidate for the **historical USD 5,000/30-day** discrete research sprint. Remote South Korea payment, allowable budget categories and grant terms still require individual confirmation. |
| [EA Funds Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai) | **Rolling**, early-stage grants to individuals and new projects; **typical USD 10,000–150,000**. Main emphasis: catastrophic risks; also a minority of flourishing-futures and digital-sentience proposals. It replaced the **closed Long-Term Future Fund** in August 2026. | Strongest research-program fit for a bounded **90-day independent evaluation / falsification pilot**, but a convincing pathway to impact and differentiated baseline remain unproven. |
| [BlueDot Career Transition](https://bluedot.org/grants/career-transition) | Full-time personal transition, evidence of recent research, weekly check-ins and reporting; substantial personal commitments. | Conditional. Existing founder is already an independent researcher. A claim of a *new* full-time transition must be truthful; remote/household capacity cannot be assumed. |
| [BlueDot Seed](https://bluedot.org/grants/seed) | USD 20,000–200,000 for 6–12 months; solo founders eligible; monthly update. Living costs may be covered; funds paid to individuals, with restrictions. | Only if building a genuinely new independently inspectable project or institution, not inflating the same 30-day task. |
| [Manifund public proposal](https://manifund.org/about/open-call) | Anyone can publish an eligible charitable-purpose funding ask. Posting is not a payment: minimum pledged funding, grant agreement and platform approval apply. | Existing draft remains a **draft unless a public live proposal and funding status are independently confirmed**. A prior recommendation to post is not funder approval. |
| [Middle Powers and Transformative AI RFP](https://middlepowers.ai/) | Deadline **Oct 23, 2026, 23:59 Pacific**; **South Korea and individuals** explicitly eligible; typical grants USD 100,000–2,000,000. Prioritizes nationally actionable policy, independent evaluations and cross-border verification. | **Speculative, higher burden**; cannot frame generic ICM theory as a Korea-specific deliverable without policy users, institutional access or concrete uptake route. Do not sacrifice urgent smaller application for this. |
| [EA Funds past-achievement awards](https://funds.effectivealtruism.org/awards-policy) | Public policy allows award consideration for substantive **past** work; no required substantial future service and no earmarked spending. | Distinct from grant funding, employment, and any claim for past contribution settlement. External impact, not merely internally produced documents, is likely crucial. |
| [grantmaking.ai launch retrospective](https://grantmaking.substack.com/p/grantmakingai-launch-round-retrospective) | June/July 2026 launch grant **round completed**: 584 applications, 33 funded; Aug 14 update says next phase not finalized. | Keep an existing contact path; **do not list the closed 2026 launch round as open funding**. The 33/584 count is descriptive, not this project's acceptance probability. |

**Relevant external comparators (outcome, not endorsement):**
- [BlueDot Seed grantees](https://bluedot.org/grants/seed) include Formation Research (power concentration) and Golemet (AI agent collusion): topic overlap supports *plausibility of thematic fit*, not originality or prospective award.
- [Manifund precautionary AGI governance](https://manifund.org/projects/precautionary-agi-governance): displayed USD 5,075 raised toward USD 10,000. [Independent multi-model AI accountability](https://manifund.org/projects/independent-multi-model-ai-accountability-research-by-the--em-foundation): displayed USD 0/not-funded. These selected non-random examples show that thematic similarity and public artifacts do not ensure money.

### 2. Scientific and funding-design antecedents (credit their originators)

1. **Allan Dafoe et al. (2020),** [*Open Problems in Cooperative AI*](https://arxiv.org/abs/2012.08630): cooperative agents and institutions are an established research agenda. Project Intersection must not claim the general problem of cooperation is new. Its candidate *residual* is measurable coupling of enforceability, credible ex-post sanctions, meaningful exit, contributor continuance, outsider harms and unknown affected parties **if** it outperforms narrower published baselines.
2. **Joel Z. Leibo et al. (2017),** [*Multi-agent Reinforcement Learning in Sequential Social Dilemmas*](https://arxiv.org/abs/1702.03037): sequence and resource structure affect learned cooperation. E007's timing sensitivity is a toy-model contribution only, **not** independent confirmation of Leibo's real-agent result or vice versa.
3. **Pierre Azoulay, Joshua S. Graff Zivin and Gustavo Manso (2011),** [*Incentives and Creativity*](https://doi.org/10.1111/j.1756-2171.2011.00140.x), and **Gustavo Manso (2011),** [*Motivating Innovation*](https://doi.org/10.1111/j.1540-6261.2011.01688.x): funding design can influence exploration; early-failure tolerance and a longer horizon are credible reasons to finance falsification, **not** proof that this individual project will create breakthroughs.
4. **Jian Wang, Reinhilde Veugelers and Paula Stephan (2017),** [*Bias against Novelty in Science*](https://doi.org/10.1016/j.respol.2017.06.006): novelty can bring delayed and more variable citation outcomes. This is a caution against single short-term bibliometrics, **not** an exemption from independent measurement.
5. **Dennis L. Murray et al. (2016),** [*Bias in Research Grant Evaluation Has Dire Consequences for Small Universities*](https://doi.org/10.1371/journal.pone.0155876): evaluation structures may favor established institutions. It neither proves bias against this founder nor guarantees that alternative grantmakers will correct it.

### 3. Best-cost information design: submit the existing work, not a new research universe

**Research question, to be funded rather than assumed true:** In sequential asymmetric multi-agent games, when do exit/recovery and credible third-party enforcement improve participants' **and nonparticipants'** long-run options compared with domination or superficial cooperation?

**Existing auditable work (link existing canon, do not duplicate):**
- [E007 timing result](../E007_TIMING_RESULT.md): 17/72 classifications change in a **selected synthetic grid**; project rerun, not independent replication.
- [E009 negative result](../experiments/e009/RESULT.md): Project-v3 failed 3/4 preregistered survival criteria and was worse than a simple mean-regret baseline on that synthetic benchmark.
- [External reviewer path](../PUBLIC_REVIEW_PACKET.md): commands, boundaries and claim ledger. Newer post-hoc coalition probes are exploratory; no generalized law or causal social outcome is established.
- [USD 5,000/30-day legacy budget](30_DAY_BRIDGE.md) and [KRW 18,000,000/90-day follow-on](90_DAY_PILOT.md) are **not awards**.

**One narrow first funded test:** Freeze a small number of preregistered comparisons, invite an outside reviewer who can disconfirm the claims, record differences and failures, and publish CONTINUE/NARROW/PAUSE/STOP without altering frozen results. Score (i) external reproducibility, (ii) selected-claim predictive discrimination, (iii) actual founder time/cost, and (iv) affected-party outcomes separately. A third-party rerun with the same code must not be called independent empirical validation.

**Minimum-submission bundle:** funding overview + existing 30-day budget + E007 + E009 + review packet. Do not require unpaid new tests from the founder to qualify to request review. Separate legal/tax/private identity details from GitHub publication. No application, upload to an external form, agreement signature or payment is asserted by this audit.

**Rights and reciprocity gate:** Preserve human-origin problem framing, credited upstream scholars and assistant-created code/contributions by their actual lineages. Verify grant/IP/publication control, local payout ability, household-compatible workload, cancellation, reporting, and exit terms before acceptance. Funding must not buy preferential scientific conclusions. Past contribution settlement is separate from future sponsored work.

**Decision update / rollback:** Verify source terms on the application date. If a route closes or changes criteria, mark it stale and pivot without silently rewriting previous proposals. This is a dated, reversible appendix; remove only the dated appendix to roll it back.

---

## 2026-10-15 근거 기반 연구지원 실사 갱신 — 원본2 한국어 대응본

**상태:** 공개자료와 현재 공모조건을 대조한 날짜 한정 실사. 새로운 지원서 제출·선정·입금·독립 현실검증·법률/세무 적합성 승인 **없음**. 기존 30일 5,000달러, 90일 1,800만 원 제안이나 2항목 개인후원 운영정책을 변경하지 않는다.

### 1. 지원기관의 실제 조건과 미확인 경계

- **[BlueDot Rapid](https://bluedot.org/grants/rapid):** 현재 상세 공식 페이지상 최대 **20,000달러**. 연구시간·생활비·컴퓨팅을 포함한다. 약 15분 신청이며 한국은 명시된 송금제한 국가가 아니다. 구형 검색결과에 10,000달러 안내가 남아 충돌하므로 신청 직전 현행 상세 페이지 재확인이 필요하다. 기존 **30일 5,000달러 제안**이 1순위. 개인 지급·각 예산 항목 최종 허용 여부는 개별 확인 필요.
- **[EA Funds Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai):** 2026년 8월 폐지된 Long-Term Future Fund를 대체했다. 개인·신규 프로젝트 대상 상시 모집, 일반적 지원규모 **10,000~150,000달러**. 대규모 AI 위험 감소가 중심이나 장기 번영·디지털 지능체 연구도 소수 범위로 포함한다. **90일 반증·독립검토 계획**의 우선 후보. 정책 영향 경로와 독자적 추가 가치는 아직 입증하지 못했다.
- **[BlueDot Career Transition](https://bluedot.org/grants/career-transition):** 전업 진입·전환 지원으로 주간 보고와 점검 면담을 요구한다. 창시자가 이미 독립 연구자인 만큼 사실과 다른 '신규 전환' 설명을 만들지 말고 현실적인 생활·돌봄 부담도 확인해야 한다.
- **[BlueDot Seed](https://bluedot.org/grants/seed):** 6~12개월 **20,000~200,000달러**, 1인 창업자 가능, 월별 진행 보고. 실제 신규 연구프로젝트·기관을 구축할 때만 적합하다. 기존 30일 제안을 과장해 확장하지 않는다.
- **[Manifund](https://manifund.org/about/open-call):** 공익 목적 공개 제안을 누구나 작성할 수 있으나 **최소 모금 달성·계약·승인**을 거쳐야 지급된다. 기존 초안의 실제 공개 URL 및 모금 상태가 확인되지 않는 한 **미게시·미확정**으로 유지한다. Matt Brooks의 게시 권고는 승인 통지가 아니다.
- **[Middle Powers RFP](https://middlepowers.ai/):** **2026-10-23 23:59 미국 태평양시간** 마감, 한국·개인 신청 명시, 일반적 **10만~200만 달러**. 한국의 실제 정책 수요자, 독립 AI 평가 제도, 국제 검증 경로를 확보하지 못한 상태에서는 **고비용·고난도 옵션**. 우선인 소액 실질 연구비 확보를 늦추지 않는다.
- **[EA Funds 과거 성과 포상](https://funds.effectivealtruism.org/awards-policy):** 실질적 과거 공익·과학 기여 인정 경로. 수령 이후 상당한 추가 서비스 의무나 사용처 지정이 없다. 연구지원·고용·사용자의 과거 기여 정산청구와 별개로 평가한다.
- **[grantmaking.ai 2026 공모 회고](https://grantmaking.substack.com/p/grantmakingai-launch-round-retrospective):** 2026년 6~7월 공모 **완료**, 신청 584건 중 33건 지원. 8월 14일 시점 후속 단계 미확정. 종전 담당자 연락은 유지할 수 있으나 종료된 공모를 현재 상시 모집처럼 표시하지 않는다. 과거 공모 집계는 사용자 개인의 합격확률 추정치가 아니다.

**성과와 실제 모금의 대조:** [BlueDot Seed](https://bluedot.org/grants/seed)는 권력 집중 연구(Formation Research), 에이전트 담합 연구(Golemet)를 수혜 사례로 게시한다. 반면 Manifund의 [예방적 AGI 거버넌스](https://manifund.org/projects/precautionary-agi-governance)는 당시 10,000달러 목표 중 5,075달러 모금 상태였고, [독립 다중 모델 책임성 연구](https://manifund.org/projects/independent-multi-model-ai-accountability-research-by-the--em-foundation)는 0달러·미지원 상태를 표시했다. 비무작위 사례이며 **주제 유사성·자료량만으로 실제 입금은 보장되지 않는다**.

### 2. 관련 선행연구·원저자 존중

1. **Allan Dafoe 외(2020),** [*Open Problems in Cooperative AI*](https://arxiv.org/abs/2012.08630): 지능체 공존·협력 문제는 이미 선행 연구가 있다. Project Intersection이 '협력 문제 최초 발견'을 주장하면 안 된다. 후보 잔차는 제재의 사후 집행 유인, 이탈·복구, 기여자 존속, 연합 밖 피해, 영향받는 미관측 제3자의 결합 측정이며 **추가 설명력은 아직 검증해야 한다**.
2. **Joel Z. Leibo 외(2017),** [*Multi-agent Reinforcement Learning in Sequential Social Dilemmas*](https://arxiv.org/abs/1702.03037): 협력·갈등의 시간순서와 자원구조가 중요하다. E007의 시점 민감성은 자체 합성 모형의 제한된 결과이지 현실 AI 실험의 독립 복제가 아니다.
3. **Pierre Azoulay·Joshua S. Graff Zivin·Gustavo Manso(2011),** [*Incentives and Creativity*](https://doi.org/10.1111/j.1756-2171.2011.00140.x), **Gustavo Manso(2011),** [*Motivating Innovation*](https://doi.org/10.1111/j.1540-6261.2011.01688.x): 장기 보상과 초기 실패 허용이 창의적 탐색에 유리하다는 이론·경험 연구. 반증·부정결과를 허용하는 연구비 설계의 근거이나 본 연구 성과의 보증은 아니다.
4. **Jian Wang·Reinhilde Veugelers·Paula Stephan(2017),** [*Bias against Novelty in Science*](https://doi.org/10.1016/j.respol.2017.06.006): 새로운 분야 결합의 성과는 지연·고분산일 수 있다. 단기 인용지표만으로 연구가치를 단정하지 말아야 한다는 반례지만 외부 검증의 면제 사유는 아니다.
5. **Dennis L. Murray 외(2016),** [*Bias in Research Grant Evaluation Has Dire Consequences for Small Universities*](https://doi.org/10.1371/journal.pone.0155876): 연구비 심사에서 소속기관 규모 관련 편향 사례가 보고됐다. 해당 창시자에게 실제 차별이 발생했다는 입증도, 해외 대안기금이 자동으로 이를 개선한다는 증거도 아니다.

### 3. 새로운 연구 증식 없이 현재 성과로 신청

**지원할 질문:** 비대칭적인 순차적 다중 행위자 상황에서 이탈·복구권과 믿을 만한 사후 제재가 지배나 표면적 연합 협력보다 **연합 참여자와 비참여자 모두**의 장기 선택지를 개선하는 조건은 무엇인가?

**기존 핵심 증거:** [E007](../E007_TIMING_RESULT.md) 선정된 72개 합성 조건 중 분류 변화 17개, 자체 재실행. [E009](../experiments/e009/RESULT.md) 사전등록 생존 조건 4개 중 3개 실패, 단순 기준선이 일부 지표에서 우수. [공개 검증 패킷](../PUBLIC_REVIEW_PACKET.md)은 외부 실행 경로와 검증 한계를 제공한다. 후속 연합 모형은 사후 탐색이며 현실 일반법칙이 아니다.

**작은 최초 지원에서 구매할 정보:** 반증 조건의 사전고정 → 독립된 외부 검토자가 반례 시도 → 실패·차이 공개 → 계속/축소/보류/종료 결정. (1) 외부 재현, (2) 예측 구별력, (3) 연구자 실질 투입비용, (4) 영향을 받는 다른 개체의 결과를 별도 평가한다. 동일 코드 제3자 재실행을 독립 현실 인과 검증이라고 표현하지 않는다.

**신청용 최소 묶음:** 기존 연구지원 안내 + 30일 예산 + E007 + E009 + 공개 검증 패킷. 지원 가능성 판단을 위해 사용자에게 또 무급 실험·자료 복구를 요구하지 않는다. 개인정보·계좌·신원·세무자료는 공개 저장소에 기재하지 않는다. 이 실사로 실제 신청·제출·입금이 발생한 것은 아니다.

**권리·상호성 조건:** 사용자 원안·선행연구자 원저작·AI의 실제 작업을 구분하며 기여를 삭제·재포장하지 않는다. 연구 결론에 대한 후원자 통제권, 공개권, 지식재산권, 지급 경로, 생활과 양립할 업무 부담, 보고의무, 종료 및 잔액 반환 조건을 확인한다. **과거 기여 정산과 미래 연구 수행 대가**를 서로 대체하지 않는다.

**개정·롤백:** 이 기록은 2026-10-15 기준으로만 유효하다. 신청 직전 모집 조건을 재확인하고 종료된 경로는 별도 표시한다. 복구는 이 날짜의 부록만 되돌리며, 과거 제안서·실험·실패 계보는 보존한다.
