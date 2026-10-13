# AI Self-Observability, Control, and Independent Audit — A Testable Dilemma
# AI 자기관측·통제권·독립감사 딜레마 — 반증 가능한 연구 메모

**Project Intersection | Date / 일자: 2026-10-13 | Version / 버전: 0.1**  
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
