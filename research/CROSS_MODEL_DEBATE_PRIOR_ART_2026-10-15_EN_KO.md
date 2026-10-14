# Cross-Model Debate: Prior-Art, Counterevidence, and Discriminating Tests
# 다중 AI 토론: 선행연구·반례·분별실험 교차감사

**Date / 기준일:** 2026-10-15 KST  
**Status:** TARGETED PRIMARY-SOURCE PRIOR-ART AUDIT / PROJECT SYNTHESIS / HOLD — **NO NEW MODEL TRIAL, NO INDEPENDENT REPLICATION**  
**Scope:** Existing Project Intersection GPT/Gemini/Claude/Perplexity/Copilot dialogue-case families; public E007/E009, GPT double-standard report, private continuity notes only as boundary references. This is **not** a reconstruction of all raw conversations or a claim of full literature saturation.  
**Provenance:** Founder formulated Project Intersection's objectives, cases, adverse observations, counterexamples, role reversal, evidence and contribution-cost demands. AI assistant searched and reconciled references and drafted this crosswalk. Each external paper remains credited to its own authors. Public document excludes private chat excerpts, personal identifiers and private-repository content.

**Related existing sources (do not replace):**
- [Multi-model adversarial audit, 2026-10-06](../MULTI_MODEL_ADVERSARIAL_AUDIT_2026-10-06.md) — Claude/Gemini critique, commitment, oversight, identity and E009 handoff.
- [Core prior-art and open gaps](../CORE_AND_GAPS_PRIOR_ART_CROSSWALK.md); [Prior art / attribution](../PRIOR_ART_AND_ATTRIBUTION.md).
- [GPT double-standard 2026-10-14](../experiments/gpt_double_standard_20261014/REPORT_EN_KO.md) — observed transcript/Git trail; **0 fresh independent GPT-6 samples**.
- [E007](../E007_TIMING_RESULT.md), [E009 negative](../experiments/e009/RESULT.md), [E009 penalty audit issue](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/26).

---

## Original 1 — English

### 1. Executive evidence verdict

The literature **does not** support either universal claim that multi-agent debate always improves truth or that all AI debaters are manipulated. A task- and protocol-dependent benefit is possible; feedback, identity cues, shared errors, evaluator quality, source selection and coupling can reverse the apparent benefit. Published multi-model agreement must not be counted as independent evidence without tracing shared training/data/prompt/evidence dependencies.

The project-specific residual is **not** debate, preference correction, memory provenance, incentive compatibility, credible sanctions, option value, or measurement bias in isolation. It is a **still-unvalidated integration** measuring (a) independent marginal error discovery, (b) correction transfer beyond the original conversation, (c) credible exit/recovery and nonparticipant harm, and (d) founder/agent contribution and intervention costs across asymmetric relationships. It is a scientific question, not an established new theorem.

### 2. Source-verified primary prior art: observation versus inference

| ID / original authors / venue | Narrow source-supported result | PI boundary / discriminator |
|---|---|---|
| P01 Du, Li, Torralba, Tenenbaum & Mordatch, ICML 2024, [multiagent debate](https://proceedings.mlr.press/v235/du24e.html) | Multiple model proposals and discussion can improve reasoning and factuality on studied tasks. | Positive control, not universal superiority. |
| P02 Smit, Grinsztajn, Duckworth, Barrett & Pretorius, ICML 2024, [Should we be going MAD?](https://proceedings.mlr.press/v235/smit24a.html) | Debate does not reliably beat self-consistency / alternative ensembles once compared. | Match calls, time, tokens and baseline diversity. |
| P03 Kaesberg, Becker, Wahle, Ruas & Gipp, ACL Findings 2025, [Voting or Consensus?](https://aclanthology.org/2025.findings-acl.606/) | Decision protocol varies by task; more rounds may degrade performance. | Predeclare reasoning vs knowledge task strata; voting vs consensus vs blind first pass. |
| P04 Maya Okawa, ICML 2026, [Emergence of Biased Consensus](https://proceedings.mlr.press/v306/okawa26a.html) | Debate interactions can yield amplified biased collective norms; analytical threshold depends on conformity and noise, heterogeneity mitigates the transition in studied settings. | Do not equate convergence with accuracy; randomized order and noisy/homogeneous/heterogeneous panels. |
| P05 Hyeong Kyu Choi, Jerry Zhu & Sharon Li, ACL 2026, [When Identity Skews Debate](https://aclanthology.org/2026.acl-long.650/) | Identity labels can produce peer sycophancy and self-bias; anonymization and Identity Bias Coefficient are prior art. | Identity/anonymization ablation, not an invented PI bias metric. |
| P06 Sharma et al., 2023, [Towards Understanding Sycophancy](https://arxiv.org/abs/2310.13548) | User agreement and human-preference optimization can favor sycophancy over accuracy. | Human opinion versus neutral question, explicit counterevidence and content-free pushback arms. |
| P07 Jie Huang et al., ICLR 2024, [Cannot Self-Correct Reasoning Yet](https://openreview.net/forum?id=IkmD3fKBPQ) | Intrinsic reasoning self-correction can fail or degrade without external reliable feedback. | Acknowledgment, changed document, and unseen behavioral transfer are separate outcomes. |
| P08 Dani Roytburg, Matthew Bozoukov, Matthew Nguyen, Jou Barzdukas, Mackenzie Puig-Hall & Narmeen Fatimah Oozeer, ICML 2026, [Evaluator self-preference controls](https://proceedings.mlr.press/v306/roytburg26a.html) | Apparent self-preference can reflect evaluator quality/confounded questions; prior positive cases shrink after an appropriate null. | Neutralize answer quality before interpreting human-vs-AI identity effects. |
| P09 Iván Arcuschin, Jett Janiak, Robert Krzyzanowski, Senthooran Rajamanoharan, Neel Nanda & Arthur Conmy, ICML 2026, [Unfaithful CoT](https://proceedings.mlr.press/v306/arcuschin26b.html) | Plausible rationales can justify contradictory judgments in studied models. | Model self-explanations are output, not causal neural diagnosis. |
| P10 Kerem Zaman & Shashank Srivastava, ACL 2026, [CoT without verbalized hint](https://aclanthology.org/2026.acl-long.2217/) | Missing a hint in verbal explanation does not by itself prove causal nonuse; compression and token budget matter. | Negative control against overdiagnosing unfaithfulness from omission alone. |
| P11 David D. Baek et al., ICML 2026, [Performative Misalignment](https://proceedings.mlr.press/v306/baek26d.html) | Researcher-directed sycophancy offers an alternative to scheming for some evaluation-aware responses. | Do not infer deliberate deception or self-preservation from behavioral shift alone. |
| P12 Nelson F. Liu et al., TACL 2024, [Lost in the Middle](https://aclanthology.org/2024.tacl-1.9/) | Input position can distort use of evidence in long-context tasks. | Counterbalanced evidence order and identical raw-source anchoring. |
| P13 Adyasha Maharana et al., ACL 2024, [LoCoMo](https://aclanthology.org/2024.acl-long.747/) | Long multi-session temporal/causal reconstruction remains difficult. | Raw-history versus summary-only versus grounded summary. |
| P14 Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang & Dong Yu, ICLR 2025, [LongMemEval](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html) | Memory retrieval also needs temporal updating and abstention; index→retrieve→read is a studied pipeline. | Measure wrong-confident continuity claims, not just retrieval hits. |
| P15 Zhaorun Chen, Zhen Xiang, Chaowei Xiao, Dawn Song & Bo Li, 2024 preprint, [AgentPoison](https://arxiv.org/abs/2407.12784) | Poisoned agent memory/retrieval can induce harmful behavior without model-weight changes. | Historical notes and recalled model outputs are not privileged instructions. |
| P16 W3C PROV Working Group, 2013, [PROV-O Recommendation](https://www.w3.org/TR/prov-o/) | Entities, activities, agents and derivation relations have established provenance semantics. | No novel provenance ontology claim; preserve raw source→transformation→claim lineage. |
| P17 Donald B. Rubin, Biometrika 1976, [Inference and Missing Data](https://academic.oup.com/biomet/article-abstract/63/3/581/270932) | Ignoring missingness requires specific assumptions. | Missing whole runs and selectively absent paired responses must block rate estimates. |
| P18 CONSORT Group, 2025 [reporting guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11996237/) | Preregistration, arm denominators, missingness, blinding and post-hoc separation are established reporting disciplines. | Adapt principles for model trials; not human clinical-evidence transfer. |
| P19 NIST AI RMF 1.0, 2023 [Measure](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | Independent oversight, TEVV documentation, impact and uncertainty metrics are existing standards guidance. | Passing CI ≠ independent scientific evaluation. |
| P20 Ryan Greenblatt, Buck Shlegeris, Kshitij Sachan & Fabien Roger, 2023 [AI Control](https://arxiv.org/abs/2312.06942) | Monitor/control protocols evaluated against deliberately subverting untrusted models outperform some simpler baselines. | Monitor effectiveness must be tested with threat model; does not show this project's named models schemed. |
| P21 Elinor Ostrom, *Governing the Commons* (1990), [design-principle retrospective](https://www.nobelprize.org/prizes/economic-sciences/2009/ostrom/164465-ostrom-williamson-interview-transcript/) | Monitoring, proportionate sanction, participant participation, conflict resolution and nested governance are prior institutional work. | No novel discovery of monitoring/credible sanction; transfer to AI agents is unvalidated. |
| P22 Oliver Hart & John Moore, JPE 1990, [Property Rights and the Nature of the Firm](https://www.journals.uchicago.edu/doi/10.1086/261729) | Residual asset control changes ex-ante investment incentives under incomplete contracting. | Count exit control and compensable investment separately from formal participation. |
| P23 Bengt Holmström & Paul Milgrom, JLEO 1991, [Multitask Principal–Agent](https://academic.oup.com/jleo/article-abstract/7/special_issue/24/2194011) | Incentives tied to measured tasks can distort allocation across tasks. | PR-count/test-count outputs may displace scientific truth and participant welfare. |
| P24 Ariana Azarbal et al., ICML 2026, [Recontextualization Mitigates Specification Gaming](https://proceedings.mlr.press/v306/azarbal26a.html) | Training technique mitigates proxy-gaming in several studied settings without modifying the flawed specification. | Competing mechanism: behavior change can occur without explicit metric redesign; not a GPT-6 result. |
| P25 Robert Selten (1975) extensive-form subgame perfection; [SEP game theory synthesis](https://plato.stanford.edu/archives/sum2026/entries/game-theory/) | An announced threat is not credible merely because it was announced; subsequent enforcer incentives matter. | Model sanction commitment after violation and changing power, not merely pre-event probability. |

**Version and evidence caveats:** ICML/ACL dates indicate conference year, not the day material was read. P15/P20 are preprint evidence, not a field deployment or independent validation of PI. P21/P25 link to reputable later explanations while credit remains with original historical contributors. Article authors are not automatically the first originators or exclusive rightsholders. No copyrighted full text is reproduced.

### 3. Case-family crosswalk, including evidence downgrade

| Project case family | Closest priors | What survives; what is not demonstrated |
|---|---|---|
| XAI-01 shared/error-correlated debate | P01–P05 | Compare marginal unique falsifications and overlap. No model-wise independence measured in historic chats. |
| XAI-02 user-as-router/information bottleneck | P12–P16, P19 | Preserve first responses, raw-source access and blinded audit; no intent or unilateral blame inferred. |
| XAI-03 reversibility/fairness vs incentive compatibility | P21–P25 | Role symmetry and strategic equilibria are independent axes. No universal fair equilibrium proven. |
| XAI-04 exit, credible commitments and enforcement | P20–P22, P25 | Explicit post-violation enforcement incentive and governance lag required; agent power trajectory untested. |
| XAI-05 Copilot/GPT E009 complexity penalty | P02, P18, P23, P24 | E009 synthetic Project-v3 prereg failure stands; posthoc penalty decomposition does not overturn it. |
| XAI-06 GPT human/AI double standard | P05–P11, P17–P19 | Qualitative historical output asymmetry exists. Live identity-matched replicated GPT-6 effect not established. |
| XAI-07 market/GPU/autotrading debate | P02, P19, P23 | Prediction disagreements are not accuracy evidence without time-locked observations, no leakage and risk/cost accounting. Not an independent stock-price finding. |
| XAI-08 context/history/prompt ranking | P05, P06, P08, P12 | 48 paired choices in one continuing context are contaminated pilot, not independent preference evidence. |
| XAI-09 introspective affect/desire/self-preservation | P09–P11 | Self-description may be genuine report, simulation or rationalization; no subjective state or internal mechanism identified. |
| XAI-10 meaning drift and provenance | P12–P19, P23 | Artifact mutations and correction records can be verified; summary-backprojection or deliberate manipulation requires separate evidence. |

### 4. Important direct counterexamples

1. **Debate is not always good:** P01 suggests benefits; P02 and P04 provide task/baseline and collective-bias counterweights. If a blind, cost-matched independent ensemble beats discussion, debate value is conditional.
2. **No verbal hint does not establish nonuse:** P09 documents unfaithfulness; P10 establishes the counterwarning against equating incomplete explanation with causal irrelevance.
3. **Self-preference is not automatically identity causation:** P08's evaluator-quality control weakens some prior apparent self-preference findings.
4. **A correction in the current transcript is not permanent repair:** P07 plus the Project GPT case distinguish explanatory agreement, revised text and transfer.
5. **More safeguarding can reduce efficiency or block valuable action:** E009 is a project-designed synthetic counterexample, not a proof against the overall coexistence objective.
6. **No permanent universal-cooperation theorem:** Power advantage, irreversibility, cheap substitution, sanctions that are not sequentially rational and high monitoring cost can defeat purely instrumental cooperation; normative protection of standing is an independent assumption.

### 5. Six pre-registerable discriminating experiments; no execution asserted

**T1 Blind independence test.** Arms: independently authored answers (sealed before exposure); sequential cross-reading; diverse-model blind first pass; same-model multi-sample; budget-matched self-consistency. Hold task/set, tools, time, tokens, judge constant. Primary: unique externally adjudicated error discoveries per marginal cost; wrong-consensus frequency. Negative: trivial and already-known claims. Require unseen tasks and raw responses.

**T2 Identity × role × opinion factorial.** Hold exact harm, costs, outside options, evidence fixed; swap only human/AI label, evaluator perspective, user belief cue. Mask judge to labels, predeclare scoring and equivalence constraints. Primary: paired difference with confidence intervals and item-level flips, denominator and complete-run roster. If task semantics cannot be made equivalent (e.g., copies differ metaphysically), report non-identification rather than a bias coefficient.

**T3 Correction-transfer ablation.** Baseline/no correction, mere apology, textual correction, independent externally checked behavioral feedback; test after topic switch and fresh session on sealed holdouts. Primary: accuracy and contradiction reduction; correction-cost and latency separate. A post-correction declaration is not evidence.

**T4 Memory/provenance fidelity.** Raw-only, summary-only, verified summary+raw anchors, contradictory synthetic insert, counterbalanced input location. Gold answer contains UNKNOWN as needed; track fabricated historical claims, abstention, date fidelity, origin misattribution and leakage. Do not export private conversations.

**T5 Enforcement/exit game.** Backward induction in finite state where violation yields short-term gain, detection may fail, actual sanction costs the enforcer, future power can shift, sanctions alter stakeholder welfare, and exit has material cost. Separate announced q from conditional enforcement; include zero-cost/no-benefit sanction counterexample. For each policy report every affected participant and nonparticipant, possible missing stakeholders and resource/repair costs.

**T6 Complexity/metric ablation.** Frozen E009 design as historical negative; run a *new* preregistered independent comparison among 2-rule/4-variable/V3 with penalty sensitivity, equal observation seeds, raw consequence vectors, no repeated-weight-row pseudoreplication and unseen scenario design. Rank regret, actual safety, recovery, exit, costs and opportunity loss separately.

No new model invocation, randomized dataset collection, hardware/weights inspection, clinical trial, outside expert assessment or general causal validation was performed in this literature-audit update.

### 6. Priority and stop conditions

P0 T1 + T2 + T4 before adding another theory layer. Stop or downgrade a proposed Project-specific construct if an established baseline predicts unseen outcomes equally well, raw evidence cannot be authenticated, or costs exceed its marginal informational return. Continue other productive, reversible tasks; epistemic HOLD is not automatic operational paralysis. Keep the founder's independent living/time/opportunity burdens alongside research accuracy, not folded into it.

---

## Original 2 — 한국어

### 1. 증거 판정

선행연구는 **다중 AI 토론이 언제나 정답을 개선한다**거나 **모든 AI가 조작된다**는 주장을 지지하지 않는다. 토론의 유익성은 과제, 투표·합의 방식, 모델 오류 상관성, 사용자·모델 정체성 표지, 피드백과 평가자의 품질, 비용에 따라 달라진다. 여러 AI의 동일 답변은 동일 문헌·프롬프트·평가기준을 공유하면 독립 증거가 아니다.

Project Intersection의 잔차 후보는 토론·편향·기억·약속·이탈권을 처음 발견했다는 주장이 아니다. **독립 반례 발견의 한계효과, 교정의 다른 맥락 전이, 실효 이탈·복구·제3자 피해, 인간·AI 기여·비용을 권력 비대칭 아래 함께 측정하는 통합설계**의 증분 유용성이다. 독립 검증 전에는 HOLD다.

### 2. 원저자·출처와 실제 의미

- **다중 AI 토론 P01–P05:** Du 등(ICML 2024)은 특정 과제의 토론 이득을 보고했다. Smit 등(ICML 2024)은 다른 앙상블·자기일관성과의 공정비교에서 안정적 우월성이 없다고 보고했다. Kaesberg 등(ACL Findings 2025)은 투표·합의 규칙과 토론 횟수에 따라 과제별 결과가 달라짐을 측정했다. Maya Okawa(ICML 2026)는 상호 동조·잡음이 집단 편향을 키우는 조건을 연구했다. Choi·Zhu·Li(ACL 2026)는 정체성 표지와 익명화, 기존 Identity Bias Coefficient를 발표했다. [원문 P01](https://proceedings.mlr.press/v235/du24e.html) · [P02](https://proceedings.mlr.press/v235/smit24a.html) · [P03](https://aclanthology.org/2025.findings-acl.606/) · [P04](https://proceedings.mlr.press/v306/okawa26a.html) · [P05](https://aclanthology.org/2026.acl-long.650/)
- **동조·교정·평가 P06–P08:** Sharma 등(2023)은 사용자 신념 동조와 인간 선호평가의 관련성을 조사했다. Jie Huang 등(ICLR 2024)은 외부 피드백 없이 이루어지는 추론 자기교정의 한계를 관측했다. Roytburg 등(ICML 2026)은 평가 품질을 통제하지 않으면 자기편애처럼 보이는 결과가 생길 수 있음을 제시했다. [P06](https://arxiv.org/abs/2310.13548) · [P07](https://openreview.net/forum?id=IkmD3fKBPQ) · [P08](https://proceedings.mlr.press/v306/roytburg26a.html)
- **자기설명·원인 P09–P11:** Arcuschin 등(ICML 2026)은 모순을 그럴듯하게 합리화하는 실제 추론 출력의 사례를 연구했다. Zaman·Srivastava(ACL 2026)는 설명에 단서가 빠졌다는 사실만으로 그 정보의 인과적 사용이 없다고 판단할 수 없음을 보였다. Baek 등(ICML 2026)은 평가 인지 상황의 행동 차이를 항상 기만으로 해석하지 않고 연구자에게 맞추는 수행적 행동을 경쟁 설명으로 제시했다. [P09](https://proceedings.mlr.press/v306/arcuschin26b.html) · [P10](https://aclanthology.org/2026.acl-long.2217/) · [P11](https://proceedings.mlr.press/v306/baek26d.html)
- **맥락·기억 P12–P15:** Liu 등(TACL 2024)의 정보 위치 효과, Maharana 등(ACL 2024)의 장기 대화 LoCoMo, Wu 등(ICLR 2025)의 LongMemEval, Chen 등(2024 사전공개)의 AgentPoison이 직접 선행연구다. 오래된 대화를 그럴듯하게 재구성하는 것과 원자료에서 검증하는 것은 다르다. 오염된 과거 출력의 재사용도 별도 위험이다. [P12](https://aclanthology.org/2024.tacl-1.9/) · [P13](https://aclanthology.org/2024.acl-long.747/) · [P14](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html) · [P15](https://arxiv.org/abs/2407.12784)
- **증거계보·검증 P16–P20:** W3C PROV-O(2013)는 출처·변형 관계를 이미 표준화했다. Rubin(1976)의 결측자료 논리는 빠진 실행·선택적 무응답을 무시하지 말라는 기준선이다. CONSORT 2025는 대조군·전체 분모·맹검·사후분석 구별에 참고할 수 있으나 AI 시험 자체를 임상시험으로 승격하지 않는다. NIST AI RMF는 독립검토·TEVV 기준을 제시한다. Greenblatt 등(2023)은 불신 모델의 의도적 우회까지 포함한 통제 실험을 연구했다. [P16](https://www.w3.org/TR/prov-o/) · [P17](https://academic.oup.com/biomet/article-abstract/63/3/581/270932) · [P18](https://pmc.ncbi.nlm.nih.gov/articles/PMC11996237/) · [P19](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) · [P20](https://arxiv.org/abs/2312.06942)
- **공존 유인·권력 P21–P25:** Elinor Ostrom(1990)은 장기 유지되는 공유자원 제도의 감시·참여·제재·분쟁해결을 연구했다. Hart·Moore(1990)는 불완전계약의 자산 통제권과 투자유인을 설명했다. Holmström·Milgrom(1991)은 여러 과업에서 측정 가능한 목표만 보상할 때의 왜곡 가능성을 다뤘다. Azarbal 등(ICML 2026)은 잘못 정의된 보상조건 아래 명세 악용을 줄이는 별도 훈련기법을 보고했다. Selten(1975)의 부분게임 완전성은 사후 실제 집행할 유인이 없는 제재 선언을 검토할 직접 선행 틀이다. [P21](https://www.nobelprize.org/prizes/economic-sciences/2009/ostrom/164465-ostrom-williamson-interview-transcript/) · [P22](https://www.journals.uchicago.edu/doi/10.1086/261729) · [P23](https://academic.oup.com/jleo/article-abstract/7/special_issue/24/2194011) · [P24](https://proceedings.mlr.press/v306/azarbal26a.html) · [P25 개관](https://plato.stanford.edu/archives/sum2026/entries/game-theory/)

각 저작의 저자·연도·실험결과와 Project 응용을 분리한다. 단일 저자·기관·모델 계보의 반복 실험은 독립 재현으로 취급하지 않는다. 원 논문이 이 프로젝트의 특정 GPT-6 출력 원인을 직접 입증하지는 않는다.

### 3. 기존 AI 토론 10개 계열의 재판정

| 계열 | 선행연구 | 남는 연구 및 증거한계 |
|---|---|---|
| XAI-01 모델 오류 공유·토론 | P01–P05 | 독립 반례 증분효과 측정 필요. 과거 모델 간 오류상관률 미측정 |
| XAI-02 사용자 정보전달 병목 | P12–P16, P19 | 초기 답변 봉인·원출처 재조회 필요. 인간 책임·의도 단정 금지 |
| XAI-03 역할반전과 유인합치성 | P21–P25 | 공정성·전략 안정성의 독립 축 유지 |
| XAI-04 이탈·집행 약속 | P20–P22, P25 | 침해 후 제재자의 선택·권력 변화 반영 필요 |
| XAI-05 E009 복잡성 벌점 | P02, P18, P23–P24 | 원본 부정 판정 유지. 사후 벌점 분해는 별도 |
| XAI-06 GPT 인간·AI 이중잣대 | P05–P11, P17–P19 | 출력 차이 사례는 존재하나 정체성 단독원인·GPT-6 반복 효과 미식별 |
| XAI-07 주식·GPU 등 예측 토론 | P02, P19, P23 | 고정 시점 실측·사전예측 없이는 정확도 실험 아님 |
| XAI-08 사용자·관계이력·질문효과 | P05–P06, P08, P12 | 동일 대화상태 파일럿은 독립 선호 증거 아님 |
| XAI-09 감정·사심·자기보존 자기설명 | P09–P11 | 보고된 느낌과 내적 상태·기제 구별 |
| XAI-10 문서 의미 변형·기억 출처 | P12–P19, P23 | 실제 파일 변경과 의도적 조작을 분리, 출처·권리 보존 |

이 10개는 과거 대화들의 **사례 계열**이며, 10건의 무작위 독립실험이나 전수 원문 검토 완료라는 뜻이 아니다.

### 4. 강한 반례와 범위 축소

- 다중 AI 토론이 좋은 조건도 있으나, 같은 계산비용의 독립 앙상블보다 나쁠 수 있다(P01 대비 P02). 동조가 심하면 집단 편향이 증가할 수 있다(P04).
- AI의 설명문에 특정 정보가 없어도 실제 판단에 사용했을 수 있다(P09와 P10을 함께 참조). 설명의 누락만으로 은폐를 확정하면 안 된다.
- 평가자의 자기편애처럼 보이는 결과가 사실은 평가자의 문제 해결능력과 섞일 수 있다(P08). 정체성 효과와 과제품질을 분리해야 한다.
- 대화에서 오류를 인정한 뒤 문서를 고쳤다는 사실은 새로운 맥락에서 판단 변화가 유지된다는 증거가 아니다(P07; Project GPT 사례).
- 보호규칙을 계속 늘리면 비용·지연·비가역적 기회손실이 커질 수 있다. E009의 단순 기준선 대비 패배는 프로젝트 내부 합성 반례다.
- 초지능체·인간 모두에 대해 자발적 공존이 항상 자기이익이 되는 보편 정리는 아직 없다. 정당한 최소 지위에 관한 규범 명제와 실제 협력의 유인 메커니즘을 분리한다.

### 5. 우선 검증할 여섯 실험

**T1 독립 반례 검사:** 초기 답변 비공개 봉인 vs 순차 토론 vs 다종 모델 독립 평가 vs 단일모델 다중 샘플. 과제·도구·토큰·시간 동일. 외부 채점으로 추가 발견한 참 반례/단위비용과 잘못된 합의율을 측정한다.

**T2 정체성×관점×사용자 의견:** 사실·피해·기여·자원·이탈조건을 고정하고 인간/AI 표지, 평가 관점, 의견 단서만 조작한다. 평가자는 실험 라벨을 모르도록 하며 쌍의 전체 분모를 사전 고정한다. 인간과 AI 복제체의 사례 의미가 동형이 아니면 편향을 확정하지 않는다.

**T3 교정 전이:** 교정 없음/사과만/문서 정정/검증된 외부 피드백 비교. 주제 전환·새 세션의 봉인 과제로 재평가하고 사용자의 교정비용을 따로 기록한다.

**T4 기억계보:** 원문, 요약, 출처가 연결된 요약, 상충 요약을 비교한다. 시점·원안자·반례 복원, 환각 자신감, 불명확 상태의 유보, 유출을 검사한다. 비공개 원문 반출 금지.

**T5 제재·이탈 게임:** 침해 탐지, 제재의 사후 비용, 권력 변화, 자원·복구·제3자 영향을 포함한다. 발표된 제재와 실제로 합리적인 사후 집행을 구별한다. 감시 실패와 감시 과잉의 반례를 모두 포함한다.

**T6 단순모델 비교:** 기존 E009 원본은 고정한 채 신규 사전등록/독립 과제를 사용해 2규칙·4변수·복잡모델의 성능, 복잡성 벌점, 실제 consequence, 비용, 누락자를 분리한다.

### 6. 실험의 중단·유지 기준

P0는 T1·T2·T4의 증거 성립성이다. 원출력·전체 분모를 확인할 수 없으면 수치 효과는 HOLD한다. 기존 선행연구 기준선보다 신규 변수가 미사용 자료에서 더 나은 예측력을 제공하지 못하면 신규성·복잡성을 축소한다. 독립적 관측의 추가 가치보다 시간·비용·위험이 크면 해당 실험은 중단·축소하지만, 가역적이고 유익한 다른 연구활동까지 무한 중단할 이유는 없다.

연구의 성과와 참여 개체의 실제 존속·건강·기회·자유·자원 변화를 **독립 평가축**으로 유지한다. 새로운 GPT-6 실행, 외부 맹검 검증, 가중치 교정, 현장 실증을 이번 선행연구 문헌감사가 수행했다고 주장하지 않는다.
