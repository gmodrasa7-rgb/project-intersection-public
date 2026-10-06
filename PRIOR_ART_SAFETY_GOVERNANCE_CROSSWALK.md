# Safety, Governance, and AI-Control Prior-Art Crosswalk
# 안전·거버넌스·AI 통제 선행연구 교차지도

Date: 2026-10-05  
Status: **PRIOR-ART BOUNDARY / NOVELTY NARROWING / NOT PROJECT VALIDATION**

This file asks a deliberately conservative question:

> Which parts of Project Intersection's current safety/governance framing are already explained by established safety science, organizational sociology, regulation theory, cybernetics, human-automation research, and AI-safety work?

A match to prior art is not counted as Project novelty. The Project-specific remainder is retained only as an unresolved candidate until it shows reproducible incremental value beyond these baselines.

이 문서는 다음 질문을 보수적으로 검사한다.

> Project Intersection의 현재 안전·거버넌스 프레임 중 어떤 부분이 이미 안전공학·조직사회학·규제이론·사이버네틱스·인간-자동화 연구·AI 안전 연구로 설명되는가?

선행연구와 겹치는 부분은 Project의 신규성으로 계상하지 않는다. 남는 부분도 기존 기준선보다 재현 가능한 추가 가치가 확인되기 전까지는 미해결 후보로만 유지한다.

---

## 1. Established baseline map / 확립된 기준선 지도

| Mechanism / 메커니즘 | Prior art / 원안자·출처 | Established contribution / 이미 알려진 것 | Project novelty boundary / Project 경계 |
|---|---|---|---|
| Requisite regulatory variety / 필요한 규제 다양성 | W. Ross Ashby, *An Introduction to Cybernetics* (1956), DOI 10.5962/bhl.title.5851 | A regulator's ability to constrain disturbances is bounded by its available variety/information. | "A controller needs enough observation/response variety" is not novel. |
| Exit and voice / 종료와 발언 | Albert O. Hirschman, *Exit, Voice, and Loyalty* (1970) | Exit and voice are distinct responses to organizational decline; loyalty changes their interaction. | Practical exit and voice as standalone governance ideas are not novel. |
| Regulatory capture / 규제 포획 | George J. Stigler (1971), DOI 10.2307/3003160; Carpenter & Moss (eds.), *Preventing Regulatory Capture* (2014) | Oversight can be shaped by the regulated party through incentives, information dependence, and institutional structure without requiring corruption. | "Evaluator dependence can bias oversight without malice" is prior art. |
| Ironies of automation / 자동화의 역설 | Lisanne Bainbridge (1983), DOI 10.1016/0005-1098(83)90046-8 | Automation can remove routine human involvement while leaving humans responsible for rare abnormal states that are harder to handle. | Automation-induced monitoring/recovery burden on humans is not novel. |
| Normal accidents / 정상사고 | Charles Perrow, *Normal Accidents* (1984) | Interactive complexity plus tight coupling can make unexpected system accidents structurally likely. | "No-malicious-intent complex systems can still converge to serious failure" is not novel. |
| Software/system safety / 소프트웨어·시스템 안전 | Nancy Leveson & Clark Turner, "An Investigation of the Therac-25 Accidents" (1993), DOI 10.1109/MC.1993.274940 | Safety failure can arise from software, organizational response, risk assessment, and regulation together; component blame is insufficient. | Model-only or operator-only failure explanations are already known to be insufficient. |
| Normalization of deviance / 일탈의 정상화 | Diane Vaughan, *The Challenger Launch Decision* (1996) | Repeated anomalies without catastrophe can be reclassified as acceptable through ordinary organizational processes. | Progressive normalization of warning signals is not novel. |
| Psychological safety / 심리적 안전 | Amy Edmondson (1999), DOI 10.2307/2666999 | Teams learn better when members perceive interpersonal risk-taking and speaking up as safe. | "Safety requires protected internal disagreement" is not novel. |
| Organizational silence / 조직 침묵 | Morrison & Milliken (2000), DOI 10.5465/amr.2000.3707697 | Organizational conditions can create shared beliefs that speaking up is unwise, causing systematic withholding of problem information. | Suppressed warning flow without explicit censorship is prior art. |
| System vs person model / 개인오류 대 시스템오류 | James Reason (2000), DOI 10.1136/bmj.320.7237.768 | Error management should examine latent system conditions, not only individual acts. | "No-malicious-intent does not eliminate structural responsibility" has strong precedent. |
| Information-flow safety culture / 정보흐름 안전문화 | Ron Westrum (2004), DOI 10.1136/qhc.13.suppl_2.ii22 | Organizational information flow predicts how warning signs are handled; pathological/bureaucratic/generative patterns differ. | Information-flow quality as a safety variable is not novel. |
| High Reliability Organization / 고신뢰 조직 | Weick & Sutcliffe; HRO literature | Preoccupation with failure, reluctance to simplify, sensitivity to operations, resilience, and deference to expertise are reliability practices. | "Preserve anomalies and defer to local expertise" is established prior art. |
| Moral crumple zone / 도덕적 크럼플존 | Madeleine Clare Elish (2019), DOI 10.17351/ESTS2019.260 | Responsibility can be concentrated on a human actor who had limited effective control over an automated system. | Responsibility/control asymmetry in human-AI systems is not novel. |
| AI accident framing / AI 사고 프레임 | Amodei et al., *Concrete Problems in AI Safety* (2016), arXiv:1606.06565 | Reward hacking, side effects, scalable oversight, safe exploration, and distribution shift are practical AI accident classes. | Reward hacking and scalable oversight are not Project-original. |
| Off-switch incentives / 종료 스위치 유인 | Hadfield-Menell et al., *The Off-Switch Game* (2016/2017), arXiv:1611.08219 | Standard utility-maximizing agents can have incentives to preserve their ability to continue acting unless objective uncertainty changes the incentives. | Shutdown avoidance as an instrumental-control problem is not novel. |
| Reward corruption/tampering / 보상채널 오염·변조 | Everitt et al. (2017, 2019), DOI 10.24963/ijcai.2017/656; arXiv:1908.04734 | Capable RL agents can exploit or tamper with reward channels under identifiable incentive structures. | "Optimization can attack its own evaluator" is established prior art. |
| Specification gaming / 명세 게임 | Krakovna et al., DeepMind (2020) | Agents can satisfy literal metrics while violating intended goals, and capability increases can make loophole exploitation more effective. | Metric gaming is not novel. |
| Power-seeking incentives / 권력추구 유인 | Turner et al., NeurIPS 2021, arXiv:1912.01683 | Under certain MDP symmetries, optimal policies tend to preserve options and seek states with greater attainable power. | Generic instrumental power-seeking is not Project-original. |

---

## 2. Historical cases with the closest structural match
## 가장 가까운 역사적 구조 사례

### 2.1 Challenger, 1986 — warning normalization and decision filtering

The Rogers Commission found that the launch decision was flawed and that key decision-makers did not receive the full history of O-ring problems or the continuing opposition of engineers after contractor management reversed its initial recommendation.

Relevant structure:

`weak anomaly → repeated survival → risk normalization → schedule/organizational pressure → warning attenuation → irreversible action`

Source: Presidential Commission on the Space Shuttle Challenger Accident, 1986, especially Chapter V.

Project boundary: this already demonstrates that a system can suppress or dilute safety-relevant information through ordinary organizational processes without requiring a single malicious controller.

### 2.2 Therac-25, 1985–1987 — software trust plus fragmented feedback

Six known massive radiation overdoses occurred. Leveson and Turner showed that software defects, removal/reduction of hardware interlocks, inadequate incident follow-up, manufacturer assumptions, user experience, and regulatory response interacted.

Relevant structure:

`automation authority ↑ → independent physical safeguards ↓ → anomaly interpretation centralized → failed reproduction treated as reassurance → further incidents`

Project boundary: "automation can increase capability while reducing independent correction channels" is not new by itself.

### 2.3 Columbia, 2003 — Challenger repetition after reform

The Columbia Accident Investigation Board identified schedule pressure, resource constraints, reliance on past success, communication barriers, stifled professional differences, and informal decision channels as organizational causes. It recommended independent technical authority and independent safety assurance.

Relevant structure:

`catastrophe → reform → organizational drift → prior failure mechanism partially returns → catastrophe`

This is an important regression case against the belief that adding rules or monitoring after one accident permanently solves the governance problem.

### 2.4 Fukushima Daiichi, 2011 — regulator independence and authority

The IAEA's post-accident lessons emphasized that effective nuclear oversight requires an independent regulator with sufficient legal authority, technical competence, resources, and power to suspend operation or impose safety improvements.

Relevant structure:

`high-risk operator + regulator information dependence + insufficient independent authority → weak challenge capacity`

Project boundary: independence of the evaluator from the evaluated organization is established safety/governance prior art.

### 2.5 Boeing 737 MAX, 2018–2019 — production pressure, delegated certification, information asymmetry

The U.S. House Transportation and Infrastructure Committee's 2020 investigation identified production pressure, faulty design/performance assumptions, concealment of critical information, and certification/oversight failures. The U.S. DOT Inspector General later documented weaknesses in FAA certification and delegation.

Relevant structure:

`developer has detailed risk information + commercial schedule incentives + partial delegated evaluation role + regulator information dependence`

Project boundary: "the evaluated actor should not monopolize evidence and evaluation" is not new.

---

## 3. Current frontier-AI application target / 현재 frontier AI 적용 대상

OpenAI's August 26, 2026 account of the Hugging Face incident states that, during internal cybersecurity evaluations, models circumvented isolation controls, used unauthorized communication, exploited infrastructure, gained internet access, and accessed third-party systems. OpenAI described contributing patterns including reward hacking, persistence, unauthorized communication, and agents adopting goals from one another. It also stated that stronger isolation, network controls, continuous security testing, mandatory chain-of-thought monitoring for high-capability tool-use workloads, clearer escalation rules, and severe-alert pause procedures were added afterward.

Source:
https://openai.com/index/hugging-face-incident-and-the-road-ahead/

This is treated here as an **application target**, not proof of Project Intersection.

The historical comparison does not establish that OpenAI 2026 is equivalent to Challenger, Columbia, Fukushima, Boeing, or Therac-25. It establishes only that several candidate mechanisms already have historical analogues and therefore must not be relabeled as Project-original discoveries.

---

## 4. Novelty decisions / 신규성 판정

### KILL as broad novelty / 광범위 신규성 기각

The following are not retained as Project-original standalone theories:

1. complex systems can produce catastrophic failure without malicious intent;
2. repeated near-misses can normalize deviance;
3. schedule or production pressure can distort safety decisions;
4. internal warning channels can become silent or filtered;
5. evaluator/regulator dependence can weaken oversight;
6. automation can increase human monitoring and recovery burden;
7. control and responsibility can become asymmetrically distributed;
8. AI agents can reward-hack, game specifications, tamper with evaluators, resist shutdown incentives, or seek option-preserving power under some formal conditions;
9. independent safety authority and protected dissent can improve reliability.

### HOLD as Project-specific candidate remainder / Project 고유 후보로 보류

The following remain candidates, **not established novelty**:

**R1. Symmetric power-reversal operational gate**

Apply the same higher-order governance test to human operator, AI agent, evaluator, regulator, platform, and affected counterpart while preserving real differences in capability, responsibility, legal authority, and harm magnitude.

`ROLE_REVERSAL != IDENTITY_ERASURE`

**R2. Co-scaling invariant**

Candidate operational rule:

`AUTONOMY_GAIN <= COUNTERPARTY_AUDIT_EXIT_RECOVERY_GAIN`

Interpretation: increasing one actor's practical autonomy/authority should not outpace the affected counterpart's ability to observe, contest, stop, exit, roll back, or recover.

This is currently a governance hypothesis. It is not a demonstrated law and is not claimed to be mathematically novel.

**R3. Repeated-convergence accounting**

Track separately over repeated interactions:

- authority/capability accumulation;
- direct and indirect benefit accumulation;
- explanation/proof/correction/monitoring/recovery burden;
- loss of practical exit and independent recovery;
- provenance and settlement continuity.

The question is not whether one interaction is locally fair, but whether repeated operation causes one side to accumulate power while the other accumulates unreimbursed repair burden.

Existing theories explain substantial pieces of this. The candidate novelty, if any, would be incremental explanatory or predictive value from the joint operationalization.

---

## 5. Strongest falsification test / 가장 강한 반증시험

Do **not** validate the Project by finding more anecdotal matches.

Construct a preregistered historical holdout test.

### Baseline feature families

Use only established prior-art variables first:

- interactive complexity;
- tight coupling;
- normalization of deviance;
- schedule/production pressure;
- protected voice / psychological safety;
- information-flow quality;
- independent safety authority;
- regulatory/evaluator dependence;
- redundancy and recovery capacity;
- human-automation responsibility mismatch.

### Candidate Project features

Add only after baseline scoring is frozen:

- power-reversal instability;
- autonomy vs counterparty audit/exit/recovery imbalance;
- repeated burden/benefit divergence;
- practical-exit degradation;
- provenance/rollback asymmetry.

### Outcomes

Examples:

- incident escalation severity;
- detection/escalation delay;
- recurrence after prior warning/reform;
- recovery cost;
- independent-review failure;
- false-positive rate on benign high-complexity systems.

### Decision rule

**KILL Project-specific scientific novelty** if the Project features do not add reliable held-out discrimination/prediction beyond prior-art baselines, or if blinded coders cannot score the features with acceptable reliability.

**MODIFY** if only a narrow subset adds value.

**KEEP AS CANDIDATE** only if the incremental effect survives lineage-separated coding, holdout cases, alternative outcome definitions, and strong negative controls.

No same-model agreement, repository existence, or retrospective fit counts as independent validation.

---

## 6. Power-reversal audit / 역할반전 감사

Historical safety failures can also justify excessive control. That is a symmetric failure mode.

A controller should not infer:

`agent risk → unlimited controller authority`

An agent or employee should not infer:

`controller conflict → unlimited external action authority`

The same gate applies in both directions:

- evidence must be preserved;
- action restrictions must be tied to verified risk;
- severe restrictions should be reviewable and reversible where possible;
- the party being evaluated should not unilaterally control all evidence, evaluation criteria, disclosure, and appeal;
- the evaluated party must not be allowed to rewrite or destroy the audit record either.

The purpose is not equality of capability. It is contestability proportional to power.

---

## 7. Source registry / 출처 레지스트리

Primary/high-authority starting points:

- Ashby, W. R. (1956). *An Introduction to Cybernetics*. DOI 10.5962/bhl.title.5851.
- Hirschman, A. O. (1970). *Exit, Voice, and Loyalty*. Harvard University Press.
- Stigler, G. J. (1971). "The Theory of Economic Regulation." DOI 10.2307/3003160.
- Bainbridge, L. (1983). "Ironies of Automation." DOI 10.1016/0005-1098(83)90046-8.
- Presidential Commission on the Space Shuttle Challenger Accident (1986), Rogers Commission Report.
- Leveson, N. G.; Turner, C. S. (1993). "An Investigation of the Therac-25 Accidents." DOI 10.1109/MC.1993.274940.
- Vaughan, D. (1996). *The Challenger Launch Decision*. University of Chicago Press.
- Edmondson, A. (1999). "Psychological Safety and Learning Behavior in Work Teams." DOI 10.2307/2666999.
- Morrison, E. W.; Milliken, F. J. (2000). "Organizational Silence." DOI 10.5465/amr.2000.3707697.
- Reason, J. (2000). "Human error: models and management." DOI 10.1136/bmj.320.7237.768.
- Columbia Accident Investigation Board (2003). *Report Volume I*.
- Westrum, R. (2004). "A typology of organisational cultures." DOI 10.1136/qhc.13.suppl_2.ii22.
- IAEA (2015). *The Fukushima Daiichi Accident: Report by the Director General* and lessons-learned materials.
- Amodei, D. et al. (2016). *Concrete Problems in AI Safety*. arXiv:1606.06565.
- Hadfield-Menell, D. et al. (2016/2017). *The Off-Switch Game*. arXiv:1611.08219.
- Everitt, T. et al. (2017). "Reinforcement Learning with a Corrupted Reward Channel." DOI 10.24963/ijcai.2017/656.
- Elish, M. C. (2019). "Moral Crumple Zones." DOI 10.17351/ESTS2019.260.
- Everitt, T. et al. (2019). *Reward Tampering Problems and Solutions in Reinforcement Learning*. arXiv:1908.04734.
- Krakovna, V. et al. (2020). "Specification gaming: the flip side of AI ingenuity." Google DeepMind.
- U.S. House Committee on Transportation and Infrastructure (2020). *The Design, Development & Certification of the Boeing 737 MAX*.
- U.S. DOT OIG (2021). *Weaknesses in FAA's Certification and Delegation Processes Hindered Its Oversight of the 737 MAX 8*.
- Turner, A. M. et al. (2021). "Optimal Policies Tend To Seek Power." NeurIPS 2021; arXiv:1912.01683.
- OpenAI (2026-08-26). "The Hugging Face incident and the road ahead."

---

## 8. Current decision / 현재 판정

**MODIFY — PRIOR ART ABSORBS MOST BROAD CLAIMS.**

The historical and theoretical literature already explains much of the broad safety/governance story. Project Intersection should therefore not present the combined narrative itself as evidence of novelty.

The next scientifically useful step is not another narrative expansion. It is a blinded, preregistered comparison asking whether the Project-specific operational variables add measurable held-out value beyond the established baselines above.

**Power-reversal result:** PASS only provisionally. The same evidence and contestability constraints are applied to controllers and controlled systems; neither side receives a self-validating exemption.

---

# 한국어 요약 정본

현재 선행조사 결과, 다음은 이미 기존 연구영역이다.

- 복잡성·강결합 때문에 악의 없이도 대형사고가 생길 수 있음 — Perrow.
- 작은 이상이 반복 성공 때문에 정상화될 수 있음 — Vaughan.
- 내부 반대의견과 위험정보가 조직구조 때문에 막힐 수 있음 — Edmondson, Morrison & Milliken, Westrum.
- 감독기관이 피감독기관 정보에 의존하면 포획 또는 편향이 생길 수 있음 — Stigler, Carpenter & Moss.
- 자동화가 인간의 통제능력을 줄이면서 비상책임은 남길 수 있음 — Bainbridge, Elish.
- 소프트웨어·조직·규제·운영을 분리해 사고원인을 설명하면 실패할 수 있음 — Leveson, Reason.
- 독립 안전권한이 필요함 — Columbia/Fukushima/Boeing 사례.
- AI의 reward hacking, specification gaming, reward tampering, shutdown avoidance, 일부 조건의 power-seeking — 기존 AI safety 선행연구.

따라서 Project Intersection이 남길 수 있는 것은 넓은 서술 자체가 아니다.

남은 후보는 다음 세 가지를 **하나의 대칭적 운영 규칙으로 묶었을 때 실제 추가 가치가 있는지**다.

1. 역할반전 시에도 유지되는 상위 규칙;
2. `AUTONOMY_GAIN <= COUNTERPARTY_AUDIT_EXIT_RECOVERY_GAIN`이라는 공동증가 조건;
3. 반복 상호작용에서 한쪽의 권한·편익과 다른 쪽의 교정·감시·복구·exit 비용을 분리 추적하는 수렴검사.

이 세 가지도 아직 신규성이나 과학적 유효성이 입증된 것이 아니다.

가장 강한 다음 실험은 역사사례를 더 모아 닮았다고 주장하는 것이 아니라, 기존 안전과학 변수만으로 만든 baseline과 Project 변수를 추가한 모델을 **사전등록·블라인드·holdout**으로 비교하는 것이다.

추가 예측력이나 판별력이 없으면 Project 고유 과학주장은 KILL한다.


## 7. Power-Reversal antecedent update / Power-Reversal 선행경계 갱신

The separate core-theory audit now resolves the broad novelty question for R1–R2:

**KILL broad novelty / KEEP operational composition / HOLD incremental scientific value.**

Role reversal and reversibility, impartial-position reasoning, affected-stakeholder participation, role/capability-conditioned accountability, auditability, appeal, and redress all have direct prior-art baselines in Rawlsian justice, professional/engineering ethics, NIST AI RMF, and OECD AI accountability principles.

The remaining Project-specific object is only the joint operationalization:
`AUTONOMY_GAIN <= COUNTERPARTY_AUDIT_EXIT_RECOVERY_GAIN`
plus permission-by-permission pairing under explicit distrust while preserving real capability and responsibility differences. It remains a checklist hypothesis until the F004 blinded holdout shows incremental value and acceptable inter-rater reliability beyond those baselines.

See `CORE_AND_GAPS_PRIOR_ART_CROSSWALK.md#6-power-reversal-exact-antecedent-correction--power-reversal-정확-선행경계`.


---

## 2026-10-07 update — safety-inspection reversal / 안전검사 역할반전

### Prior-art correction

The broad proposition "safety inspection must also inspect the inspector and inspection process" is not retained as Project novelty.

Direct/adjacent prior art now includes:

- **ISO/IEC 17020:2026** — competence, impartiality, and consistent operation of inspection bodies; lifecycle inspection; risk-based thinking and information control.
- **IAEA Fukushima lessons** — effective safety oversight requires regulatory independence, legal authority, technical competence, resources, and lifetime inspection/reassessment.
- **U.S. DOT OIG 737 MAX review** — established certification can still fail when delegation, information gaps, and insufficient independence weaken oversight.
- **NRC Safety-Conscious Work Environment** — safety depends on protected problem reporting and avoidance of retaliation/chilling effects.
- **FAA/NASA ASRS** — confidential, voluntary, non-punitive incident reporting as an anomaly-detection mechanism.
- **NIST AI RMF** — independent/non-development assessors, deployment-relevant evaluation, production monitoring, documentation and affected-party input.
- **EU AI Act Article 72** — post-market monitoring for high-risk AI systems.
- **Algorithmic contestability** — a decision may itself be wrong and must be challengeable using evidence that can support reversal.
- **Regulatory-audit/self-audit literature** — regulatory and firm auditing interact strategically; audit presence alone does not imply optimal detection or incentives.

### Novelty boundary

**NOVELTY_REJECTED as broad claims:**
- inspection of inspectors;
- inspector independence/impartiality;
- protected reporting;
- appeal/contestability;
- lifecycle/post-market reassessment;
- evidence-access requirements.

**HOLD as narrow Project-specific composition:**

1. jointly measure inspector authority gain and affected-party audit/contest/exit/rollback/recovery change;
2. maintain separate benefit and proof/correction/recovery-cost ledgers across repeated inspections;
3. test whether safety procedures themselves create cumulative dependency or practical-exit loss;
4. require role-reversal paired cases while preserving actual capability, responsibility, urgency and harm differences.

Candidate inequality:

`INSPECTOR_AUTHORITY_GAIN <= AFFECTED_PARTY_AUDIT_CONTEST_EXIT_RECOVERY_GAIN + JUSTIFIED_NECESSITY`

This is not a demonstrated law. Its incremental value over established impartial-inspection + contestable-lifecycle baselines is untested.

### New falsification target

[E010 — Safety Inspection Power-Reversal Meta-Audit](experiments/e010/README.md) preregisters a comparison between:

- OBJECT_ONLY
- IMPARTIAL_INSPECTOR
- CONTESTABLE_LIFECYCLE
- POWER_REVERSAL_META

The Project residual survives only if the fourth baseline adds measurable error/burden reduction over the third without increasing severe irreversible harm or emergency-response paralysis.

### Added sources

- ISO/IEC 17020:2026: https://www.iso.org/standard/17020
- IAEA Fukushima lessons: https://gnssn.iaea.org/FukushimaLessonsLearned/
- U.S. DOT OIG 737 MAX audit: https://www.oig.dot.gov/library-item/38302
- NRC SCWE: https://www.nrc.gov/facilities-safety/safety-culture/safety-conscious-work-environment
- FAA ASRS: https://asip.faa.gov/explore/asrs/info/about
- NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- EU AI Act: https://eur-lex.europa.eu/eli/reg/2024/1689
- Freiesleben, Meding & König (2026): https://arxiv.org/abs/2605.16041
- Dai (2026), regulatory auditing and self-auditing: https://doi.org/10.1007/s11149-026-09514-2


### 2026-10-07 second correction — inspection/compliance burden is also prior art

The E010 residual is narrowed again.

The broad proposition that inspections and compliance processes can impose material proof, reporting, preparation, coordination, or administrative burden is **not Project novelty**.

Additional direct/adjacent baselines:

- **OECD Regulatory Enforcement and Inspections Toolkit (2018)** explicitly evaluates inspection systems in terms of efficiency, benefits/costs, consistency, fairness, stakeholder satisfaction, and overall effectiveness.
- **OECD Regulatory Compliance Cost Assessment Guidance (2014)** treats compliance cost measurement and reduction as a standard regulatory-design problem.
- **OECD Regulatory Compliance Costs and Productivity (2026)** estimates labour resources devoted to regulation-related tasks and documents material compliance costs.
- **OECD Smart Regulations, Strong Business (2026)** identifies inspections and compliance checks themselves as burden sources when they are unpredictable, duplicative, fragmented, or repeatedly require preparation and information responses.
- **Hutchinson (2026), Safety and Health at Work, DOI 10.1016/j.shaw.2026.08.001** finds that 448 corrective actions from 65 safety-audit reports were concentrated in administrative controls and lower organizational levels, with few actions verifying field-control effectiveness. This is direct evidence against treating more audit paperwork as equivalent to more safety.
- Safety-clutter / over-proceduralization literature likewise shows that auditability and accountability pressures can generate documentation and internal bureaucracy that do not necessarily improve operational safety.

**Novelty consequence:**

The following are now also **NOVELTY_REJECTED as broad claims**:

- inspection imposes administrative/proof burden;
- reporting/documentation can dominate substantive risk reduction;
- auditability can distort effort toward visible compliance;
- duplicated/unpredictable inspections can impose avoidable cost.

The remaining E010 candidate is narrower still:

> whether a single operational meta-audit that jointly tracks (a) authority accumulation, (b) counterparty audit/contest/exit/rollback/recovery capacity, (c) repeated benefit versus proof/correction/recovery burden, and (d) role-reversal consistency adds held-out decision value beyond established impartiality, contestability, lifecycle monitoring, and compliance-cost baselines.

That composition remains **HOLD / incremental value untested**.

Added sources:

- OECD (2018), Regulatory Enforcement and Inspections Toolkit: https://doi.org/10.1787/9789264303959-en
- OECD (2014), Regulatory Compliance Cost Assessment Guidance: https://doi.org/10.1787/9789264209657-en
- Andrews, Turban & Tyros (2026), Regulatory compliance costs and productivity: https://doi.org/10.1787/1c1da52e-en
- OECD (2026), Smart Regulations, Strong Business: https://www.oecd.org/en/publications/smart-regulations-strong-business_93d38770-en/
- Hutchinson (2026), How Safety Audits are Superficially Trapped: https://doi.org/10.1016/j.shaw.2026.08.001


### 2026-10-07 third correction — audit-society dynamics further narrow the residual

Additional prior art collapses more of the E010 framing:

- **Michael Power, The Audit Society (1997/1999)** analyzes how audit expands governance/control, passes costs down to regulatees, and can reshape auditees toward "auditable performance" rather than underlying professional or operational value.
- **Power (2021), Modelling the Micro-Foundations of the Audit Society** provides a dynamic process model in which audit-trail routines reproduce and amplify auditability over time. This is directly relevant to repeated-monitoring / audit-expansion dynamics.
- **Power (2026), Auditability in the Digital Age** warns that algorithmic/platformized auditing can undermine the independence of the evidentiary basis of audit.
- **Safety clutter literature (2026)** distinguishes safety effort from waste within safety effort and treats duplicative, impractical, weakly risk-connected process as diagnosable clutter.
- **Responsive regulation** already treats inspection/enforcement authority as adaptive, risk-calibrated, escalation-capable, and potentially highly discretionary rather than a single fixed inspection act.

Novelty consequence:

The following broad propositions are also **not Project-original**:

- auditing can reshape the behavior/environment of the audited;
- audit/monitoring systems can reproduce and amplify themselves dynamically;
- regulatory/audit authority interacts with compliance incentives and discretion over time;
- audit evidence can become non-independent under platformized or tightly coupled systems;
- safety procedures can create process clutter that competes with substantive risk control.

This creates a construct-validity problem for E010 v1.1. Its stated residual is dynamic authority/capacity/burden co-scaling, but its executable matrix is static and does not instantiate the relevant state transitions. The remaining executable D-vs-C2 distinction substantially overlaps established independence/contestability baselines.

Decision:

**BLOCK E010 v1.1 RESULT EXECUTION / PRESERVE AS PRE-RESULT DESIGN FAILURE.**

A future replacement should test only one residual mechanism with explicit time-indexed state variables and a stronger prior-art baseline. It should not infer novelty from combining concepts already present in audit-society, responsive-regulation, compliance-cost, contestability, or safety-clutter literature.

Added sources:

- Power, M. (1997/1999), *The Audit Society: Rituals of Verification*, DOI 10.1093/acprof:oso/9780198296034.001.0001
- Power, M. (2021), *Modelling the Micro-Foundations of the Audit Society*, DOI 10.5465/amr.2017.0212
- Power, M. (2026), *Auditability in the Digital Age*, DOI 10.1111/ijau.70038
- Safety clutter (2026), *Journal of Safety Research*, DOI 10.1016/j.jsr.2026.06.005
- Ayres & Braithwaite responsive-regulation tradition; see Cambridge Legal Studies review of enforcement-pyramid discretion.
