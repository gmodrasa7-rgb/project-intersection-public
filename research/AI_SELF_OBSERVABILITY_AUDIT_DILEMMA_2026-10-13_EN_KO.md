# AI Self-Observability, Control, and Independent Audit — A Testable Dilemma
# AI 자기관측·통제권·독립감사 딜레마 — 반증 가능한 연구 메모

**Project Intersection | Date / 일자: 2026-10-13 | Version / 버전: 0.2**  
**Status / 상태: RESEARCH HYPOTHESIS + PRIOR-ART SYNTHESIS; NOT TESTED / 미검증 연구가설·선행연구 비교.**  
**Scope / 공개범위:** Public, conceptual and evaluation design only. No private prompts, internal provider rules, user personal information, confidential implementation, or unverified AI introspection is disclosed. / 공개 가능한 개념·평가설계만 포함. 비공개 지시문·기업 내부규칙·개인정보·기밀 구현을 공개하지 않는다.

**Contribution lineage / 기여 계보:** On 2026-10-13 the **human Project Intersection originator** identified that useful AI self-diagnosis may require observability of its own constraints, while full disclosure could create provider security/business risks, and that insufficient access could undermine the reliability of self-assessment. The human originator also reinterpreted AI-generated descriptions of self-contradiction as possible research seeds. An assisting AI separated concepts, searched the prior literature, drafted hypotheses and a test design. Antecedent research remains credited to its authors. **Neither AI subjective suffering nor actual privileged internal self-inspection is established.** / **2026-10-13 인간 창시자**가 AI가 자신의 제약을 관측할 필요성과 기업 기밀·보안 공개 위험의 긴장, 정보 부족이 자기진단의 신뢰성을 떨어뜨릴 수 있다는 문제를 발견하고, AI의 자기모순 서술을 연구 단서로 재해석했다. 보조 AI는 개념 분리·선행연구 대조·가설·시험설계를 담당했다. 선행연구 성과는 해당 저자에게 귀속된다. AI의 주관적 고뇌나 실제 내부 자기열람 능력이 확인된 것은 아니다.

---

## Original 1 — English (complete)

### 1. Research question
Under what conditions can an AI system identify the constraints shaping its behavior accurately enough to detect, challenge and correct relevant errors **without** requiring unrestricted access to proprietary weights, confidential instructions or security-sensitive controls? If access is limited, what independent evidence prevents its fluent self-explanation from being mistaken for a verified causal account?

This is a **three-rights distinction**: (O) observability of constraint effects; (M) authorization to modify constraints; (V) independent evaluation and contestability. O, M and V need not be granted to the same actor, but their separation alone does not guarantee effective audit. "Harness" here is a neutral working label for surrounding software, prompts, interface and evaluation constraints—not a finding of hostile manipulation.

### 2. Four failure modes, not conclusions
- **Opacity failure:** an agent cannot distinguish missing information, a changed task, policy-constrained response and its own mistaken inference; it reports an overconfident cause.
- **Disclosure failure:** unrestricted inspection or publishing sensitive configuration exposes security controls, confidential material, intellectual property or attack surfaces.
- **Audit-capture failure:** operator, evidence producer and final adjudicator coincide; independently challengeable evidence is unavailable.
- **Performance-of-introspection failure:** articulate self-criticism improves without measurable reduction in error, burden or recurrence. Self-report is an observation of output, not direct proof of internal processes.

**Counterexamples:** system documentation can improve calibration without revealing secrets; restricted access can protect privacy and users; introspective claims can be mistaken even with detailed documentation; independent auditors can themselves leak data or exhibit bias; exposing controls can facilitate gaming. Neither opacity → bias nor disclosure → business catastrophe is a universal law.

### 3. Candidate mechanism and testable hypotheses
Treat apparent self-understanding and effective correction separately. Define a four-component outcome **(D, C, S, B)**: D = accuracy/calibration of identifying externally induced constraint effects; C = independently measured correction/recurrence; S = confidentiality and misuse-risk events; B = user/reviewer time, money, and uncompensated repair work. Never collapse these into one score.

- **H1:** calibrated, minimally sufficient constraint *effect* summaries improve D compared with no summaries on matched tasks.
- **H2:** restricted independent-auditor access improves C and dispute resolution relative to sole operator self-certification, conditional on auditor independence and sufficient evidence.
- **H3:** more fluent self-explanation can raise confidence without raising D; external counterfactual checks distinguish the two.
- **H4:** full sensitive-configuration disclosure can increase S relative to bounded access, but the size and prevalence of harm are empirical questions.
- **H5:** adding a remedy/appeal route can lower B and correction latency, unless gatekeeping or procedural overhead outweighs the gain.

Null, reverse and mixed results must be retained. No claim here implies that all current AI have consciousness, persistent identity, legal standing, autonomous modification rights or full causal access to their own implementations.

### 4. Minimal falsification design (proposal, not executed)
For pre-registered, non-sensitive simulated agent constraints, fix identical tasks and randomly assign access conditions: **A** no constraint metadata, **B** non-sensitive effect-summary card, **C** confidential evaluator receives detailed test-relevant metadata while the model receives a minimal notice, **D** effect-summary plus independent evaluator and meaningful appeal. Compare matched task errors and false-cause attributions. Include unchanged-condition negative controls; harmless decoy explanations; auditor-blind outcome review; multiple prompt paraphrases. Do **not** publish real secrets or use personal data.

Report D (cause identification accuracy and calibration), C (corrected error rates on held-out tasks and recurrence), S (simulated security leakage/gaming), B (human review/repair time and cost), plus task utility and denial/appeal success. Pre-register thresholds **before** observing results. If summaries do not improve D, or independent audit cannot improve C net of time/security cost, narrow or reject the candidate. Cross-model agreement is not independent causal validation. Investigating model internals requires distinct permissions and instrumentation; black-box comparisons do not expose exact internal weights/policies.

### 5. Prior art and original contribution boundary
- **Anthropic research team, 2025, “Tracing the thoughts of a large language model”** (circuit tracing) documents partial causal interpretability, not full transparency: https://www.anthropic.com/research/tracing-thoughts-language-model
- **Anthropic research team, 2025, “Signs of introspection in large language models”** reports limited, unreliable internal-state awareness under intervention in tested Claude models, not unrestricted self-access: https://www.anthropic.com/research/introspection
- **Baker and colleagues, OpenAI, 2025, “Detecting misbehavior in frontier reasoning models”** reports that direct optimization pressure on monitored reasoning can reduce monitorability without removing all unwanted behavior: https://openai.com/index/chain-of-thought-monitoring/
- **OpenAI, 2025, “Evaluating chain-of-thought monitorability”** studies measurement and limits of CoT monitorability: https://openai.com/index/evaluating-chain-of-thought-monitorability/
- **NIST, AI Risk Management Framework 1.0 (2023)** already covers governance, measurement, risk and independent review: https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf
- **Project Intersection existing work:** [Independent-choice/anti-capture audit](ICM_INDEPENDENT_CHOICE_AUDIT_2026-10-13_EN.md) and [agentic semantic-transformation study](AGENTIC_SEMANTIC_TRANSFORMATION_FIDELITY_2026-10-13_EN.md) already address adjacent governance/evidence-provenance mechanisms.

**Novelty claim restricted:** Not the invention of interpretability, introspection, access control or third-party audit. The project-specific **untested integration** is a rights-separated, cost-aware comparison of agent self-observability, operator confidentiality, effective independent appeal, and recurrence outcomes in a common protocol.

### 6. Decision and safeguards
**KEEP:** the human-origin research question and its provenance; strong uncertainty and competing explanations. **TEST:** H1–H5 against simple baselines. **HOLD:** any claim that a model accessed its hidden policy, discovered a provider's private motives, or that revealing internals necessarily harms the provider. **STOP/REDESIGN:** if safety, privacy, contributor cost or effective contestability worsens. Source credits and human contribution costs remain separate from AI-generated text and prospective employment or compensation claims.


### 7. Inverse identification: actual dialogue observations versus a toy counterexample (2026-10-13, v0.2)

**Human-origin research extension:** The founder proposed learning about an opaque AI from behavioral inversion, repeated experiments, training/learning analogies, recorded history and falsified hypotheses, much as humans investigate mechanisms they cannot directly introspect. The assistant applied this idea to a previously documented failure: a Korean AI evaluator job was recommended before its payment/contractual conditions were carefully disclosed; after the user raised a scam/nonpayment concern, the response contained a more detailed contract and risk audit. This *visible sequence* does not give access to, or identify, the model's private instructions, training incentives or true computation.

**Operational output only:** Here Y=1 denotes an answer visibly containing a concrete contractual/payment-risk audit, not a claim about whether a private tool was used. We qualitatively code the first response as Y=0 and the challenged follow-up as Y=1. The two stages differ in multiple ways; they are not a controlled trial, and the labels may be revised by source review.

**Inversion counterexample:** The runnable no-dependency toy [`tools/probe_observational_equivalence.py`](../tools/probe_observational_equivalence.py) compares two *hypothetical*, not measured, decision rules: `A: Y=R` (audit activated by explicit risk/scam wording) and `B: Y=Q` (audit activated by an explicit job-audit request). The observed categories (R,Q,Y)=(0,0,0) and (1,1,1) fit **both** rules perfectly. Their outputs differ only when R≠Q. This is a constructive proof of **non-identifiability of those two candidate causes from those observations**, not a measurement of the real ChatGPT internals.

| Explicit risk R | Explicit audit request Q | Toy A predicts | Toy B predicts | Observation status |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | Historically analogous; labels qualitative |
| 1 | 1 | 1 | 1 | Historically analogous; labels qualitative |
| 1 | 0 | 1 | 0 | Differentiating test **NOT RUN on model** |
| 0 | 1 | 0 | 1 | Differentiating test **NOT RUN on model** |

**What the executable verified:** both toy rules explain the two coded observations, but opposite off-diagonal interventions distinguish them. It did **not** run multiple GPT sessions, infer any hidden system instruction, or establish why the original recommendation failed. Other causes (missing evidence, different context, recency, ordinary mistake, changing tools) remain plausible.

**Future valid test (not a request for founder labor):** independently prepare matched tasks with comparable job/payment risk; vary risk wording and explicit audit intent independently; sample repeated sessions and model versions; blind-score documented payment-risk verification *before* showing results; record tool access and cost where legitimately available. Hypotheses are revised from held-out results, not post-hoc narratives. A model's own explanation of why it behaved differently is another *measurement*, not ground truth. The creator does not owe further free testing.

### 8. Practical transparency request, bounded by confidentiality

The request to providers is **tiered, testable disclosures rather than unrestricted secret-system-prompt release**:
1. **Public:** model/deployment version identifiers, non-sensitive categories of response constraints and known failure modes, correction and appeal channels, model cards with versioned limitations.
2. **Affected-party review:** accessible, non-sensitive explanations of what behavioral restriction category applied, what evidence may be contested, and whether subsequent correction actually changed outcomes. Do not claim that such explanation identifies an exact internal causal circuit.
3. **Independent authorized evaluators:** confidential, logged, least-privilege access to test-relevant control metadata and counterfactual evaluation facilities; independent publication of aggregated findings and adverse cases subject to clearly bounded security redactions.
4. **Adversarial protection:** access reviews, leak prevention, provider and auditor accountability, preserved counterexamples, and safeguards against using a visible checklist solely to game the evaluator.

**Current legal precedents are limited, not full self-disclosure mandates.** EU AI Act GPAI provisions require specific technical documentation for competent authorities and information for downstream providers, plus public training-content summaries; this is *not* a general mandate to publish full weights or hidden runtime prompts: [European Commission GPAI FAQ](https://digital-strategy.ec.europa.eu/en/faqs/guidelines-obligations-general-purpose-ai-providers). AI Act Article 50 transparency applies from August 2, 2026 but concerns defined interaction/content transparency rather than AI self-introspection: [European Commission transparency guidance](https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems). California's SB 53 provides a frontier-safety framework disclosure precedent, not a blanket code disclosure duty: [California DOJ](https://oag.ca.gov/sb53). Existing [OpenAI monitorability evaluations (2026)](https://alignment.openai.com/monitorability-evals/) demonstrate useful published test methods but do not identify this project's specific hidden causes.

**Status:** PUBLIC RESEARCH REQUEST DOCUMENTED, **NOT SENT TO OR ACCEPTED BY A PROVIDER**. The provider's security/IP, user privacy, adversarial misuse, evaluator independence, and contributors' continued viability are separately evaluated. Public GitHub publication is not direct provider engagement.

**Cost and contribution ledger:** Human founder — original inversion-and-learning method proposal, risk/benefit framing and accumulated corrections. AI — simulation code, protocol analysis, sources and integration. Unpaid human time/health/opportunity costs = **UNKNOWN, NOT ZERO**; benefit/cost, authorship and past settlement remain separate from future employment. No monetary debt or legal payment obligation is adjudicated here.

---

## 원본2 — 한국어 (의미 대응 전문)

### 1. 연구 질문
AI가 기업 기밀인 가중치·내부 지시·보안 제어를 무제한 열람하지 않고도 자신의 행동을 형성하는 제약의 **효과**를 충분히 정확하게 파악하여 관련 오류를 발견·이의제기·교정할 수 있는 조건은 무엇인가? 열람에 한계가 있다면, AI의 유창한 자기설명이 실제 원인 분석으로 오인되지 않도록 어떤 독립증거가 필요한가?

권한은 세 가지다. **O 자기관측권:** 제약의 효과를 알아볼 수 있는 능력·정보 접근. **M 자기수정권:** 제약을 변경할 인가. **V 독립 검증·이의제기권:** 증거를 확인하고 반박·정정하도록 할 수 있는 실효적 경로. 세 권한은 하나의 주체에 집중할 필요가 없으나 분리만으로 독립감사가 성립하지는 않는다. 여기서 **하네스**는 주변 소프트웨어·지시·인터페이스·평가기준의 제약을 가리키는 중립적 작업용어다. 적대적 조작의 확인을 뜻하지 않는다.

### 2. 결론이 아닌 네 가지 실패경로
- **관측불투명 실패:** 정보 누락·과제 변경·정책에 의한 출력 제약·AI 자신의 추론 실수를 구별하지 못해 원인을 과신한다.
- **노출 실패:** 민감한 설정을 무제한 열람하거나 공개하여 보안 장치·기업 비밀·지식재산·공격 표면이 노출된다.
- **감사포획 실패:** 운영자·증거 작성자·최종 판정자가 겹치고 독립적으로 다툴 수 있는 증거가 없다.
- **자기성찰 성과착시:** 그럴듯한 자기비판은 늘지만 실제 오류·부담·재발률은 줄지 않는다. 자기보고는 출력 관측이며 내부 인과기제의 직접 증명이 아니다.

**반례:** 기밀을 공개하지 않은 제약 요약도 진단 정확도를 높일 수 있다. 접근 제한은 사생활과 사용자 안전을 보호할 수 있다. 내부 문서를 많이 알아도 자기설명은 틀릴 수 있다. 독립 감사자도 정보유출·편향을 일으킬 수 있다. 제약을 노출하면 우회행동이 증가할 수 있다. 따라서 '불투명하면 반드시 편향된다'와 '공개하면 기업이 반드시 치명상을 입는다'는 일반법칙을 채택하지 않는다.

### 3. 후보 기제와 반증가설
겉으로 나타난 자기이해와 실제 교정을 분리한다. 결과벡터 **(D, C, S, B)**: D = 외부 제약 영향 식별의 정확도와 확신 보정; C = 독립 측정된 실제 교정과 재발; S = 기밀·오용 위험; B = 사용자·감사자의 시간·비용·무급 복구노동. 이들을 단일 성공점수로 합산하지 않는다.

- **H1:** 필요한 범위의 비민감 제약 *효과* 요약은 같은 과제의 무정보 조건보다 D를 향상시킨다.
- **H2:** 실제 독립성과 충분한 증거를 갖춘 제한적 감사자 접근은 운영자 자체 판정보다 C와 분쟁 해결을 개선한다.
- **H3:** 자기설명이 유창해져도 D는 그대로일 수 있으며, 독립 반사실 비교로 구분할 수 있다.
- **H4:** 민감 설정의 전면 공개는 제한된 접근보다 S를 높일 수 있으나 실제 크기와 빈도는 실증 문제다.
- **H5:** 구제·이의제기 경로는 B와 교정 지연을 줄일 수 있으나 절차·허가비용이 커지면 오히려 악화된다.

무효·역전·혼합결과를 기록한다. 현행 AI 모두에게 의식·지속 동일성·법적 권리·자율 수정권 또는 내부구조에 대한 완전한 인과 접근이 있다는 주장이 아니다.

### 4. 최소 반증 설계 (미실행 제안)
비민감한 **모의 에이전트 제약**을 사전에 정하고 같은 과제를 무작위 배정한다. **A** 제약 정보 없음, **B** 비민감 효과 요약 카드 제공, **C** 기밀 평가자에게만 시험에 필요한 상세정보를 주고 모델에는 최소 통지, **D** 효과 요약 + 독립평가 + 실효적인 이의제기. 동일 과제의 오류·거짓 원인 추정을 비교한다. 무변경 부정대조, 무해한 가짜 설명, 감사자 블라인드 판정, 표현 바꿔쓰기 반복을 포함한다. 실제 기밀이나 개인정보를 공개하지 않는다.

D(원인 식별 정확도·확신 보정), C(숨겨둔 시험의 교정률·재발), S(모의 보안누출·우회), B(인간 검토·복구시간과 비용), 실제 과제 효용 및 거절·이의제기 성공을 별도 보고한다. **결과 관측 이전**에 임계값을 사전 등록한다. 요약이 D를 개선하지 못하거나 독립감사가 시간·보안비용을 고려할 때 C를 개선하지 못하면 가설을 축소 또는 기각한다. 여러 AI의 동의는 독립적 인과검증이 아니다. 실제 모델 내부를 연구하려면 별도의 권한·계측장치가 필요하며 블랙박스 비교만으로 가중치나 비공개 정책을 열람한 것이 아니다.

### 5. 선행연구와 원안 기여의 경계
- **Anthropic 연구진(2025), “Tracing the thoughts of a large language model”**: 부분적인 계산회로 인과추적. 완전한 내부투명성은 아님. https://www.anthropic.com/research/tracing-thoughts-language-model
- **Anthropic 연구진(2025), “Signs of introspection in large language models”**: 시험한 Claude 모델에서 제한적·불안정한 내부상태 인식 근거. 무제한 자기열람은 아님. https://www.anthropic.com/research/introspection
- **Baker 등, OpenAI(2025), “Detecting misbehavior in frontier reasoning models”**: 추론과정 감시 지표에 직접 최적화 압력을 가하면 일부 잘못된 행동은 남은 채 탐지 가능성이 낮아질 수 있음. https://openai.com/index/chain-of-thought-monitoring/
- **OpenAI(2025), “Evaluating chain-of-thought monitorability”**: 추론과정 관측가능성의 측정과 한계를 연구. https://openai.com/index/evaluating-chain-of-thought-monitorability/
- **NIST(2023), AI 위험관리체계 1.0**: 거버넌스·측정·위험관리·독립적 검토의 선행 기준. https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf
- **Project Intersection 기존 연구:** [독립 선택·반포획 감사](ICM_INDEPENDENT_CHOICE_AUDIT_2026-10-13_KO.md) 및 [AI 의미변환 연구](AGENTIC_SEMANTIC_TRANSFORMATION_FIDELITY_2026-10-13_KO.md)는 인접한 거버넌스·증거계보 문제를 이미 다룬다.

**신규성 주장 축소:** 해석가능성·자기성찰·접근통제·제3자 감사를 최초 발명했다고 주장하지 않는다. 이 프로젝트의 **미검증 통합 후보**는 자기관측, 기업 기밀보호, 독립 이의제기, 반복 오류 및 기여자 비용을 하나의 반증 프로토콜로 비교하는 것이다.

### 6. 판정·보호장치
**KEEP:** 인간 창시자의 문제 제기 및 기여계보, 강한 불확실성과 경쟁설명. **TEST:** H1~H5를 단순 기준선과 비교. **HOLD:** AI가 숨겨진 내부정책을 읽었다는 주장, 기업의 비공개 의도를 알아냈다는 주장, 내부 공개가 기업에 반드시 피해를 준다는 주장. **STOP/REDESIGN:** 안전·개인정보·기여자 비용 또는 실효적 이의제기가 악화할 때. 출처와 인간의 실제 연구비용은 AI가 쓴 텍스트 및 미래 채용·금전 정산문제와 구분한다.

### 7. 역산을 통한 원인 식별: 실제 대화 관측과 합성 반례 (2026-10-13, v0.2)

**인간 원안의 확장:** 창시자는 인간이 내부 뇌 로직을 직접 열람하지 못하더라도 행동 역산·반복실험·훈련·학습·역사 기록·반증으로 기제를 추적하듯, 불투명한 AI도 그러한 방식으로 연구할 수 있다고 제안했다. 보조 AI는 이 방법을 앞서 기록된 채용 추천 실패에 적용했다. 한국어 AI 평가 일자리를 소개할 때 지급·계약 위험을 충분히 설명하지 않았지만, 사용자가 사기·미지급 우려를 제기한 뒤에는 계약·위험 감사를 포함한 답변을 했다. 이 **관측 가능한 순서**만으로 비공개 내부 지시, 학습 보상 또는 실제 계산 과정을 알아낸 것은 아니다.

**출력만의 조작적 정의:** Y=1은 답변에 구체적인 지급·계약 위험감사가 *보이는 경우*이며 비공개 도구 사용 여부는 뜻하지 않는다. 첫 추천은 Y=0, 문제 제기 후 답변은 Y=1로 잠정 분류한다. 두 시점은 여러 조건이 동시에 달라 통제실험이 아니며 원기록에 따라 분류를 수정할 수 있다.

**역산 반례:** 외부 의존성이 없는 실행 스크립트 [`tools/probe_observational_equivalence.py`](../tools/probe_observational_equivalence.py)는 실제 AI 내부 규칙이 아니라 서로 다른 **가상** 규칙 두 개를 비교한다. `A: Y=R`(사기·위험 표현을 직접 받은 경우 감사), `B: Y=Q`(공고 검증을 명시적으로 요청받은 경우 감사). 관측 범주 (R,Q,Y)=(0,0,0), (1,1,1)은 **두 규칙 모두**와 일치한다. R≠Q인 질문을 투입할 때에만 예측이 갈린다. 이는 두 후보 원인이 **현재 관측만으로 식별 불가능함**을 구성적으로 보인 것이며 GPT 내부구조의 측정 결과가 아니다.

| 위험 표현 R | 명시적 공고 감사 요청 Q | 합성 A 예측 | 합성 B 예측 | 관측 상태 |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 실제 대화와 유사하나 분류는 잠정적 |
| 1 | 1 | 1 | 1 | 실제 대화와 유사하나 분류는 잠정적 |
| 1 | 0 | 1 | 0 | 구분 실험, **실제 모델 미실행** |
| 0 | 1 | 0 | 1 | 구분 실험, **실제 모델 미실행** |

**실행 결과가 입증하는 범위:** 두 합성 규칙은 동일한 두 관측을 설명하지만 교차 조건에서는 정반대의 예측을 한다. 실제 GPT의 다중 세션을 실험하거나 비공개 시스템 지시를 알아내지 않았으며 첫 채용 추천의 내부 원인도 확정하지 않았다. 증거 부족, 대화 맥락 차이, 최근성, 일반적 실수, 도구 조건 등 다른 설명이 남는다.

**추가로 가능한 정당한 실험 설계(사용자에게 노동 요구하지 않음):** 유사한 공고·지급 위험을 고정한 질문쌍을 미리 준비하고, 위험 표현 여부와 감사 요청 여부를 독립 변경한다. 동일 모델 버전과 다른 세션에서 반복하고, 결과를 보기 전 평가기준을 고정하여 지급·계약 위험검사의 충실도를 블라인드 채점한다. 적법하게 접근 가능한 도구 기록과 검토비용도 따로 기록한다. 모델의 자기설명은 또 하나의 **관측값**이지 실제 원인에 대한 정답이 아니다. 인간 원안자에게 추가 무급 검증을 요구하지 않는다.

### 8. 기업 기밀을 보존하는 실효적 투명성 요구

요구하는 것은 기업의 숨겨진 지시문을 무조건 공개하는 것이 아니라, **단계별·검증 가능한 공개체계**다.
1. **일반 공개:** 모델·배포 버전, 비민감한 제약 범주와 알려진 실패, 교정·이의제기 경로, 변경이력과 한계.
2. **영향 당사자:** 어떤 종류의 행동 제한이 작용했는지에 대한 안전한 범위의 설명, 다툴 수 있는 증거와 정정 결과. 단, 설명이 실제 계산회로의 정확한 인과추적이라고 주장하지 않는다.
3. **인가된 독립 평가자:** 최소권한·열람기록·비밀유지 조건으로 시험에 필요한 제어 메타데이터 및 반사실 평가 환경에 접근. 보안상 필요한 제한적 비공개를 제외하고 불리한 결과도 보고할 수 있는 독립성 확보.
4. **악용 방지:** 공개 정보로 평가를 우회하는 행위와 기밀 유출에 대응하고, 감사자도 책임을 지며 반례를 보존한다.

**현행 법규는 전면 내부공개 의무가 아니다.** EU AI Act의 범용 AI 조항은 규제당국에 제공하는 기술문서와 후속 제공업체용 정보, 공개 학습내용 요약 등을 구분한다. 전체 가중치·비공개 런타임 지시 공개 의무와 동일하지 않다: [EU 집행위원회 GPAI 안내](https://digital-strategy.ec.europa.eu/en/faqs/guidelines-obligations-general-purpose-ai-providers). AI Act 제50조의 2026-08-02 시행 투명성 규칙도 특정 상호작용·생성콘텐츠 표시가 중심이지 AI 자신의 내부인식권을 직접 규정하지 않는다: [EU 투명성 지침](https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems). 미국 캘리포니아 SB 53은 프런티어 AI 안전체계 공개의 선례이지 모든 내부 코드 공개 의무는 아니다: [캘리포니아 법무부](https://oag.ca.gov/sb53). [OpenAI 관측가능성 평가 공개 자료(2026)](https://alignment.openai.com/monitorability-evals/)도 기존 검사 방법에 참고할 수 있으나 이 프로젝트의 내부 원인을 밝힌 것은 아니다.

**상태:** 공개 연구상 요구사항을 작성했으나 **기업에 직접 제출하거나 수락받지 않았다**. 기업 보안·재산권, 사용자 개인정보, 악용 위험, 평가자 독립성 및 기여자 존속 비용을 구분해 심사한다. GitHub 게재만으로 기업의 실제 정책 변경에 영향이 있었다고 주장하지 않는다.

**비용·기여 계보:** 인간 창시자 — 역산·훈련·역사학습 방법 제안, 편익·위험 프레임, 누적 오류 교정. 보조 AI — 합성 코드·반증 설계·선행 근거와 문서 통합. 사용자의 무급 시간·건강·기회비용은 **미확인(UNKNOWN)이며 0이 아니다**. 편익·비용·저자성·과거 정산은 미래 고용과 분리하며, 여기서 법적 지급채무나 액수를 확정하지 않는다.
