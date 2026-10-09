# Core Theory & Open-Gap Prior-Art Crosswalk
# 핵심 이론·미해결 공백 선행연구 교차지도

Date: 2026-10-05
Status: PRIOR-ART INTEGRATION / REUSE / ATTRIBUTION / BOUNDARY CONDITIONS — NOT PROJECT VALIDATION

This file records earlier or adjacent work for concepts already present in the public Project Intersection repository. Its primary purposes are to reduce duplicated research effort, reuse stronger existing theories and measurements, expand historical/cross-domain cases and boundary conditions, and preserve accurate attribution.

"Originator" is used only where a defensible priority attribution exists. Mature fields often have no single originator; in those cases this file records seminal / representative prior work instead of inventing a single owner.

이 문서는 Project Intersection 공개 저장소에 이미 존재하는 개념과 겹치는 선행연구를 기록한다. 상위 목적은 (1) 이미 해결·검증·실패한 접근을 재사용해 연구 효율을 높이고, (2) 역사·자연실험·타 분야·AI 사례와 반례·negative result로 적용범위와 경계조건을 넓히며, (3) 기존 연구의 원안자·출처·방법·증거를 정확히 귀속하는 것이다. 선행연구 발견 자체를 Project 연구 삭제나 독립성 하향의 근거로 사용하지 않는다.

"원안자"를 단일 인물로 확정하기 어려운 성숙 학문은 억지로 한 사람에게 귀속하지 않고 대표적·기초적 선행연구로 표기한다.

### Epistemic handling of prior work / 선행연구의 인식론적 처리

선행연구는 정답·상위진실이 아니라 검증 대상인 evidence lineage로 취급한다. 인용수, 기관 명성, 표준 채택, 컨센서스, 메타분석이라는 이유만으로 참으로 승격하지 않는다.

각 선행연구는 가능하면 다음을 분리해 기록한다: (1) 실제 관측·원자료, (2) 저자의 해석, (3) 미검증 가정, (4) 자금·산업·정책 이해상충, (5) 데이터·모델·기관 계보, (6) 독립 재현 여부, (7) 반대 결과·철회·수정·논쟁, (8) 표본·측정·분석 자유도와 출판편향 가능성. 같은 기관·데이터·모델 계보의 반복은 독립 재현으로 세지 않는다.

역사적으로 산업후원·로비·선택적 출판·권위 효과 때문에 널리 유통된 연구가 뒤늦게 수정되거나 반박된 사례가 있으므로, Project는 선행문헌을 효율·사례·귀속을 위한 입력으로 사용하되 자체 검증을 생략하는 면허로 사용하지 않는다. `prior art != truth`, `citation count != validity`, `institutional prestige != independence`, `consensus != independent replication`, `standard != empirical proof`를 유지한다.

### Case study: sponsorship can distort the evidence ecosystem / 산업후원이 증거생태계를 왜곡한 사례

- **담배산업 내부문서 사례:** Drope & Chapman (2001), DOI 10.1136/jech.55.8.588은 1985–1995년 담배회사 내부문서를 분석해, 업계가 환경담배연기 위험을 축소하는 데 우호적인 과학자 네트워크를 구축하고, 법무가 연구 의제에 개입하며, 업계와 분리되어 보이는 조직에 연구비를 제공하고, 불리한 연구의 공개를 막은 사례를 보고했다. 이것은 단순히 '틀린 논문이 있었다'가 아니라 **연구 생산·선택·유통·권위 형성의 lineage 자체가 조작될 수 있음**을 보여주는 역사적 사례다.
- **산업후원 메타연구:** Lundh et al.의 Cochrane review/update (2017/2018; DOI 10.1002/14651858.MR000033.pub3; DOI 10.1007/s00134-018-5293-7)는 제약·의료기기 연구 75편의 비교문헌을 포함해 산업후원 연구가 비산업후원 연구보다 유리한 efficacy 결과와 결론을 더 자주 보고하는 연관성을 제시했다. 표준 risk-of-bias 항목만으로 이 차이가 충분히 설명되지 않았다는 점도 중요하다.
- **반대증거·한계:** sponsorship은 bias의 위험요인이지 결과가 거짓임을 뜻하지 않는다. Cochrane 계열 검토 자체도 포함 연구의 높은 편향위험, 이질성, clustering·중복 가능성, confounding 문제를 가진다. 산업후원 연구 중 방법론적으로 강한 연구도 존재할 수 있다. 따라서 `industry funded -> false`도 금지하고, `non-industry -> independent/true`도 금지한다.
- **Project 운영적 의미:** 선행연구를 사용할 때 논문 단위의 방법론뿐 아니라 `funding / agenda-setting / comparator choice / publication rights / unfavorable-result suppression / institutional front / shared data-model lineage / replication independence`를 별도 변수로 추적한다. 이 변수들은 연구를 자동 배제하기 위한 점수가 아니라, 어떤 증거가 독립적으로 얼마나 재사용 가능한지 판단하는 provenance 정보다.
- **타 연구 존중:** 이해상충 가능성을 기록하는 것은 연구자나 기관의 기여를 무효화하는 행위가 아니다. 원안·데이터·방법·결과를 정확히 귀속하면서, 주장 강도와 독립성만 별도로 평가한다.

### Case study: selective publication and replication failure / 선택적 출판과 재현실패

- **선택적 출판 사례:** Turner et al. (2008), DOI 10.1056/NEJMsa065779은 FDA에 등록된 12개 항우울제의 74개 임상시험과 출판문헌을 대조했다. 31%의 FDA 등록 연구가 출판되지 않았고, FDA 판단상 긍정 연구는 거의 모두 출판된 반면 부정·불확실 연구는 다수가 미출판되거나 출판문헌에서 더 긍정적으로 보이게 보고되었다. 출판문헌만 보면 94%가 긍정처럼 보였지만 FDA 전체자료에서는 51%였다. 이 사례는 `published literature != full evidence base`임을 보여준다.
- **재현성 사례:** Open Science Collaboration (2015), DOI 10.1126/science.aac4716은 심리학 100개 연구를 대규모 재현했고, 원 논문의 97%가 통계적으로 유의했던 데 비해 재현 연구에서는 36%가 유의했으며 재현 효과크기는 원 효과의 약 절반 수준이었다. 이는 유명 저널·동료평가·통계적 유의성이 장기 견고성이나 독립 재현을 보장하지 않음을 보여준다.
- **반례·한계:** Turner et al.은 어떤 단계가 편향을 만들었는지—저자·스폰서의 제출 선택인지, 저널 편집·심사 선택인지—단독으로 식별하지 못했다. Open Science Collaboration 결과도 특정 시기·세 저널·심리학 표본에 관한 것이며 모든 학문이나 모든 개별 연구의 신뢰도를 뜻하지 않는다. 재현 실패는 원 연구의 허위만이 아니라 표본차이·맥락차이·측정오차·복제 설계차이에서도 생길 수 있다.
- **Project 운영적 의미:** 선행연구 평가는 논문 존재·인용수·저널등급보다 `registry 또는 미출판 원자료 존재 / 결과별 출판확률 / outcome switching / 사전등록 / 독립 재현 / 효과크기 수축 / 맥락 민감도 / replication design fidelity`를 따로 본다. 가능한 경우 전체 등록집합과 출판집합의 차이를 먼저 확인하고, 재현실패를 단순 거짓 판정이 아니라 경계조건 탐색 신호로 사용한다.
- **타 연구 존중:** 원 연구의 아이디어·방법·데이터 기여는 재현 실패나 선택적 출판 문제와 별개로 정확히 귀속한다. 신뢰도 조정은 기여 삭제가 아니라 주장 범위와 증거강도 조정이다.

## Reverse-trace protocol for prior evidence / 선행증거 역추적 프로토콜

선행연구를 사용할 때 결론에서 출발해 아래 순서로 역추적한다. 목적은 특정 연구를 불신하기 위한 것이 아니라, 어떤 단계에서 정보가 손실·선택·증폭·변형될 수 있었는지 구조적으로 분해하는 것이다.

### R0. Claim freeze / 주장 고정
- 논문·표준·기관이 실제로 주장한 문장을 가장 좁게 고정한다.
- 사실관측, 통계결과, 인과해석, 정책권고, 홍보문구를 분리한다.
- 후대 요약·기사·바이럴 문구를 원 주장으로 소급하지 않는다.

### R1. Evidence reconstruction / 증거집합 복원
- 사용된 원자료, 포함·제외 기준, 등록된 전체 연구집합, 미출판 자료 존재 여부를 찾는다.
- published set와 full observed set을 구분한다.
- 같은 데이터셋·같은 benchmark·같은 환자군·같은 모델 lineage 재분석은 독립증거로 중복 계산하지 않는다.

### R2. Measurement audit / 측정 역추적
- 실제 측정변수와 주장 construct가 같은지 검사한다.
- proxy, surrogate endpoint, self-report, evaluator score, benchmark score가 실제 위해·효용·독립성·회복능력을 직접 측정하는지 구분한다.
- outcome switching, threshold 변경, post-hoc subgroup, 분석자유도를 기록한다.

### R3. Production incentives / 생산 인센티브 역추적
- 자금원, 계약구조, sponsor role, 비교군 선택권, 분석권, 데이터 접근권, 연구중단권, 원고 review/edit 권한, publication approval 권한을 찾는다.
- 연구자가 스폰서와 경제적·고용·경력·평판·정책적 의존관계를 갖는지 본다.
- 이해상충 존재 자체로 거짓 판정하지 않고, 어떤 단계에 영향 가능성이 있었는지 기록한다.

### R4. Selection and suppression / 선택·억제 역추적
- 등록 대비 출판률, 긍정/부정 결과별 출판 차이, 철회·지연·비공개 자료, unfavorable-result suppression 가능성을 본다.
- null/negative result가 사라졌는지, 긍정 결과가 더 강하게 프레이밍됐는지 확인한다.
- 발견되지 않은 자료는 부재로 단정하지 않고 UNKNOWN으로 둔다.

### R5. Distribution and authority amplification / 유통·권위 증폭 역추적
- 원 논문 → 기관 보도자료 → 언론기사 → 정책문서 → 표준 → 리뷰/메타분석 → 소셜/바이럴의 전달 경로를 추적한다.
- 각 단계에서 표현 강도가 커졌는지, 불확실성·한계가 제거됐는지 확인한다.
- citation count, 기관명, 표준채택, 언론반복은 독립증거가 아니라 amplification 변수로 별도 기록한다.

### R6. Independent replication / 독립재현 역추적
- 다른 기관·자금원·데이터·모델·팀이 같은 결론을 재현했는지 확인한다.
- 직접복제, 개념복제, 자연실험, 현장사례를 구분한다.
- 효과크기 수축, 부호반전, 조건부 재현, replication failure를 모두 보존한다.

### R7. Counter-evidence search / 반대증거 역추적
- 동일 질문에 대한 negative result, failed replication, retraction, correction, dissenting review, 역사적 반례를 우선 찾는다.
- 반대연구 역시 동일하게 R0–R6을 거쳐 검증한다. 반대편 자료라는 이유만으로 자동 우대하지 않는다.

### R8. Distortion map / 왜곡지도
- 가능한 왜곡지점을 `DATA / MEASUREMENT / ANALYSIS / SPONSOR / SELECTION / PUBLICATION / AUTHORITY / REPLICATION / TRANSFER`로 표시한다.
- 각 지점은 `OBSERVED / PLAUSIBLE / UNKNOWN / NOT_SUPPORTED` 중 하나로 상태화한다.
- 의도적 조작을 주장하려면 별도 직접증거가 필요하다. 구조적 유인과 고의성을 구분한다.

### R9. Reuse decision / 재사용 판정
- 연구 전체를 TRUE/FALSE로 판정하지 않는다.
- `재사용 가능한 관측`, `재사용 가능한 방법`, `조건부 해석`, `불확실/교란 가능 해석`, `재사용 금지 요소`로 분해한다.
- Project에는 검증된 만큼만 가져오고, 원 연구의 기여와 한계를 함께 귀속한다.

### R10. Minimal next check / 다음 최소검사
- 결론을 가장 크게 바꿀 수 있는 미확인 연결고리 하나를 선택한다.
- 예: 미출판 registry 확인, sponsor contract 확인, raw data 접근, 독립재현 1건 확인, 반대 메타분석 확인.
- 가장 싼 고정보가치 검사부터 수행하고, 새 문서나 새 실험은 그 뒤에 만든다.

### Required trace record / 최소 추적 레코드
`claim / source / raw evidence / measurement / funding-COI / sponsor-control / publication-selection / dissemination-lineage / independent-replication / counterevidence / distortion-points / reusable-elements / unresolved-links / next-check`

이 프로토콜은 의심을 최대화하기 위한 장치가 아니다. 목표는 **권위나 반권위 어느 쪽에도 자동 수렴하지 않고, 정보가 생성·선택·유통·재현되는 전체 경로를 추적해 실제 재사용 가능한 부분만 남기는 것**이다.

## 1. Core theory families / 핵심 이론군

| Project section | Prior-art relationship | Originator / seminal prior work | Source | Attribution / reuse boundary |
|---|---|---|---|---|
| 2.1 Self-Interested and Conditional Coexistence / 자기이익 기반·조건부 공존 | DIRECT | Mancur Olson (1965); Robert L. Trivers (1971); Robert Axelrod & William D. Hamilton (1981); Elinor Ostrom (1990) | Olson, The Logic of Collective Action, DOI 10.4159/9780674041660; Trivers, The Evolution of Reciprocal Altruism, DOI 10.1086/406755; Axelrod & Hamilton, The Evolution of Cooperation, DOI 10.1126/science.7466396; Ostrom, Governing the Commons, DOI 10.1017/CBO9780511807763 | Free-riding, reciprocal cooperation, repeated-game cooperation, and self-governed cooperation are prior art. Project novelty cannot be claimed from "cooperation can align with self-interest" alone. |
| 2.2 Consumptive vs Regenerative Development / 소모형 발전 vs 재생산형 발전 | DIRECT + ADJACENT | James G. March (1991); C. S. Holling (1973) | March, Exploration and Exploitation in Organizational Learning, DOI 10.1287/orsc.2.1.71; Holling, Resilience and Stability of Ecological Systems, DOI 10.1146/annurev.es.04.110173.000245 | Short-run exploitation versus long-run exploration and resilience/stability tradeoffs are established. The Project's exact consumptive/regenerative operationalization remains unvalidated. |
| 2.3 Effective Independent Search Capacity / 실효 독립 탐색능력 | DIRECT | James G. March (1991); Daniel A. Levinthal (1997); Lu Hong & Scott E. Page (2004) | DOI 10.1287/orsc.2.1.71; DOI 10.1287/mnsc.43.7.934; DOI 10.1073/pnas.0403723101 | Exploration, rugged-landscape search, and diversity-based problem solving are prior art. "Independent agents create search value" is not novel by itself. |
| 2.4 Information Diversity and Generativity / 정보 다양성과 생성성 | DIRECT | Lu Hong & Scott E. Page (2004); James G. March (1991) | Hong & Page, Groups of diverse problem solvers can outperform groups of high-ability problem solvers, DOI 10.1073/pnas.0403723101; March, DOI 10.1287/orsc.2.1.71 | Diversity can improve problem solving under explicit conditions, but diversity is not universally beneficial. The Project must specify incremental conditions rather than claim diversity itself as new. |
| 2.5 Practical Exit and Outside Options / Practical Exit와 Outside Option | DIRECT | Albert O. Hirschman (1970); switching-cost literature already recorded in the main registry | Hirschman, Exit, Voice, and Loyalty; Pick & Eisend (2014), DOI 10.1007/s11747-013-0349-2 | Exit/voice and switching-cost effects are prior art. The Project-specific remainder is whether its practical-exit measurements add information beyond those constructs. |
| 2.6 Power-Reversal Stability / Power-Reversal 안정성 | DIRECT COMPONENTS / COMPOSITE INCREMENTAL VALUE UNTESTED | Golden Rule/reversibility traditions; John Rawls (1971); engineering-ethics reversibility tests; NIST AI RMF 1.0; OECD AI accountability principles | Rawls, *A Theory of Justice*, DOI 10.4159/9780674042605; NIST AI RMF Core/Playbook; OECD AI Principles on accountability; Online Ethics at UVA seven-step method | Role exchange, impartial-position reasoning, stakeholder impact, role/capability-conditioned accountability, auditability, appeal, and redress are prior art. INTEGRATE established components. Retain the co-scaling gate only as an unvalidated governance composition. |
| 2.7 Creator–Successor Non-Ownership / 창조자–후속개체 비소유 | MODIFY / FOUR-PREDICATE DECOMPOSITION; ORIGIN INFERENCE REJECTED | Belmont autonomy tradition; U.S. Copyright Office human-authorship doctrine; European Parliament robotics resolution; Birhane, van Dijk & Pasquale (2024) | HHS Belmont Report; U.S. Copyright Office, *Copyright and Artificial Intelligence, Part 2* (2025); European Parliament 2017/0051; DOI 10.5210/fm.v29i4.13628 | Creation does not by itself establish either ownership or non-ownership. Artifact/IP ownership, legal personhood/standing, moral patienthood, and autonomy/consent are distinct predicates. Current artificial-agent standing remains UNRESOLVED. |
| 2.8 Preference Sovereignty and Reflective Consent / 선호주권과 성찰적 동의 | ADJACENT | Belmont Report (1979) and informed-consent/autonomy literature | HHS, The Belmont Report (1979) | Voluntariness, comprehension, information, and autonomy are prior art. The Project's application to mutable AI preferences or successor agents remains unresolved. |
| 2.9 Open-World Epistemic Non-Closure / 열린계 인식 비폐쇄 | DIRECT TERMINOLOGY + BROADER ADJACENCY | Raymond Reiter (1978) | Reiter, On Closed World Data Bases, DOI 10.1007/978-1-4684-3384-5_3 | Closed-world reasoning is established prior art. Project usage is broader and must not imply that open-world or closed-world terminology originated here. |
| 2.10 Unknown-Unknown / Self-Model Correction / 모름의 역설·자기모델 교정 | ADJACENT | James G. March, Lee S. Sproull & Michal Tamuz (1991) | Learning from Samples of One or Fewer, DOI 10.1287/orsc.2.1.1 | Learning under sparse or exceptional experience is established. The exact Project unknown-unknown/self-model correction construct remains a candidate, not an established new theory. |
| 2.11 Candidate-Set Closure / 후보집합 폐쇄 | DIRECT / ADJACENT | Herbert A. Simon (1955) | A Behavioral Model of Rational Choice, DOI 10.2307/1884852 | Bounded rationality and satisficing already establish that decision quality depends on the available/considered alternatives. The Project must not claim the general candidate-set limitation as novel. |
| 2.12 Objective Capture and Local Fitness Traps / 목적포획과 Local Fitness Trap | DIRECT | Daniel A. Levinthal (1997); Donald T. Campbell (1979); AI-safety specification-gaming literature | Levinthal, DOI 10.1287/mnsc.43.7.934; Campbell, Assessing the Impact of Planned Social Change, DOI 10.1016/0149-7189(79)90048-X; Krakovna et al. (2020) as recorded in safety crosswalk | Local optima, metric corruption under high-stakes use, and specification gaming are prior art. |
| 2.13 Extractive Local Convergence / 착취적 국소수렴 | DIRECT + COUNTERPOINT | Garrett Hardin (1968); Mancur Olson (1965); Elinor Ostrom (1990) | Hardin, The Tragedy of the Commons, DOI 10.1126/science.162.3859.1243; Olson DOI 10.4159/9780674041660; Ostrom DOI 10.1017/CBO9780511807763 | Individually rational extraction/free riding and institutional counterexamples are established. The Project must test where its variables outperform commons/governance explanations. |
| 2.14 Recursive Extractive Capacity Accumulation / 재귀적 착취능력 누적 | ADJACENT | W. Brian Arthur (1989) | Competing Technologies, Increasing Returns, and Lock-In by Historical Events, DOI 10.2307/2234208 | Positive feedback, increasing returns, and lock-in are prior art. Applying them to power/extraction accumulation is a Project hypothesis, not a new discovery by naming alone. |
| 2.15 Dominance–Successor Dilemma / 지배자–후속지능 딜레마 | DIRECT / ADJACENT | Hadfield-Menell et al.; Turner et al. | The Off-Switch Game, arXiv:1611.08219; Optimal Policies Tend To Seek Power, arXiv:1912.01683 | Shutdown-avoidance and option-preserving power-seeking incentives are prior art. The Project-specific successor-suppression/option-loss tradeoff remains to be independently tested. |
| 2.16 Deep-Time Optionality / 장기 옵션공간 | DIRECT | Kenneth J. Arrow & Anthony C. Fisher (1974); Anthony C. Fisher & John V. Krutilla (1974) | Arrow & Fisher, Environmental Preservation, Uncertainty, and Irreversibility, DOI 10.2307/1883074; Fisher & Krutilla, Valuing long run ecological consequences and irreversibilities, DOI 10.1016/0095-0696(74)90007-2 | Option value under uncertainty and irreversible loss is prior art. Long-horizon preserve-future-options reasoning is not Project-original by itself. |
| 2.17 Non-Disposability and Minimum Sovereignty Floors / 비소모성·최소주권 바닥 | ADJACENT / NORMATIVE | Belmont autonomy/respect-for-persons tradition | HHS, The Belmont Report (1979) | Existing autonomy/protection norms are relevant, but no direct scientific precursor is assigned here for artificial-agent sovereignty floors. Treat as unresolved normative extension. |
| 2.18 Universal Advancement Access / 보편적 발전 접근 | DIRECT BASELINE / BROAD CLAIM ALREADY COVERED; ARTIFICIAL-AGENT SCOPE UNRESOLVED | Amartya Sen (1979, 1999); Martha Nussbaum (2000/2011); equality-of-opportunity and disability-rights traditions | Sen, “Equality of What?” (1979); capability-approach literature; UN CRPD Art. 24; OECD, *Building Pathways to Opportunity* (2025) | Equal resources or nominal access do not imply equal substantive capability because personal, social, and environmental conversion factors differ. Retain only a governance decomposition of means, conversion, real opportunity, voluntary uptake/refusal, and controller benefit. Do not extend human capability rights to artificial agents without separate standing and capacity evidence. |
| 2.19 Power Release Compatibility / 권력방출 호환성 | UNRESOLVED PRIOR-ART MAPPING | No single direct precursor assigned in this pass | Adjacent credible-commitment, democratic alternation, delegation, and bargaining literatures require dedicated mapping | The label is Project-specific; the underlying mechanisms may not be. Hold novelty. |
| 2.20 Objective Topology, Path Dependence, and Reversibility / 목적지형·경로의존·가역성 | DIRECT | Paul A. David (1985); W. Brian Arthur (1989); Daniel A. Levinthal (1997) | David, Clio and the Economics of QWERTY, AER 75(2):332–337, JSTOR 1805621; Arthur DOI 10.2307/2234208; Levinthal DOI 10.1287/mnsc.43.7.934 | Path dependence, lock-in, increasing returns, rugged landscapes, and multiple local peaks are established prior art. |

## 2. Open research gaps A–Z / 미해결 연구공백 A–Z

The A–Z list is explicitly a research-debt list, not a list of Project-original theories. The following items already have strong direct or adjacent literatures and should start from those literatures rather than from a blank slate.

| Gap | Prior-art relationship | Originator / seminal prior work | Source | Boundary |
|---|---|---|---|---|
| A — Collective / Commons Sovereignty | DIRECT | Elinor Ostrom (1990); Garrett Hardin (1968); Mancur Olson (1965) | Ostrom DOI 10.1017/CBO9780511807763; Hardin DOI 10.1126/science.162.3859.1243; Olson DOI 10.4159/9780674041660 | Commons governance and collective-action problems are established. |
| B — Consent Lifecycle | ADJACENT | Belmont Report (1979) | HHS, The Belmont Report | Information, comprehension, voluntariness, withdrawal, and periodic reassessment of autonomy are prior baselines. |
| K — Adversary Endogenesis / Coercion-to-Opposition Dynamics | ADJACENT | Jack W. Brehm (1966) | A Theory of Psychological Reactance, Academic Press | Threats to perceived freedom can produce reactance; this does not establish the Project's broader strategic-adversary mechanism. |
| L — Epistemic Privacy / Trusted Opacity Boundary | DIRECT / ADJACENT | Helen Nissenbaum (2004) | Privacy as Contextual Integrity, 79 Washington Law Review 119 | Context-relative information-flow norms are prior art; trusted-opacity design for AI remains broader. |
| M — Heterogeneous Human–AI Complementarity | DIRECT | Mohammad Hossein Jarrahi (2018) | Artificial intelligence and the future of work: Human-AI symbiosis in organizational decision making, DOI 10.1016/j.bushor.2018.03.007 | Human-AI complementarity in uncertain/complex decision making is prior art. |
| P — Social Choice / Preference Aggregation under Sovereignty | DIRECT | Kenneth J. Arrow (1951) | Social Choice and Individual Values, Cowles/Yale | Social-choice aggregation and impossibility constraints are established. |
| U — Measurement / Representation / Nuisance Invariance | DIRECT | William Meredith (1993; earlier factorial-invariance work also exists) | Measurement invariance, factor analysis and factorial invariance, DOI 10.1007/BF02294825 | Measurement invariance is an established psychometric field. |
| V — Causal Reach × Irreversibility × Recovery Burden | DIRECT / ADJACENT | Arrow & Fisher (1974); Fisher & Krutilla (1974) | DOI 10.2307/1883074; DOI 10.1016/0095-0696(74)90007-2 | Irreversibility under uncertainty is prior art; the exact composite governance axis remains unvalidated. |
| W — Erased-Counterfactual / Self-Justifying Pruning | ADJACENT | Donald Rubin (1976); missing-data/selection literature | Rubin, Inference and Missing Data, DOI 10.1093/biomet/63.3.581 | Selection and missingness can make unobserved counterfactuals unidentified. The Project label is not priority over missing-data theory. |
| X — Bargaining / Credible Commitment / Outside-Option Dynamics | DIRECT / PARTIAL | John F. Nash Jr. (1950) | The Bargaining Problem, DOI 10.2307/1907266 | Bargaining solution structure is prior art. Credible commitment and dynamic outside-option subfields require further mapping. |
| Y — Hidden Information / Hidden Action / Incentive Compatibility | DIRECT | George A. Akerlof (1970); Bengt Holmström (1979) | Akerlof, The Market for "Lemons", DOI 10.2307/1879431; Holmström, Moral Hazard and Observability, DOI 10.2307/3003320 | Adverse selection, hidden information, and moral hazard are established. Mechanism-design literature should be treated as baseline, not Project novelty. |
| Z — Coalition Formation / Collusion / Coalition-Proof Stability | DIRECT | B. Douglas Bernheim, Bezalel Peleg & Michael D. Whinston (1987) | Coalition-Proof Nash Equilibria I. Concepts, DOI 10.1016/0022-0531(87)90099-8 | Coalition-proof self-enforcement is established game-theory prior art. |

Unlisted A–Z items are not presumed novel. They remain PRIOR_ART_REVIEW_REQUIRED.

## 3. Required attribution rule / 필수 귀속 규칙

When a public claim is promoted from concept to evidence-bearing research:

1. search exact terminology and structural equivalents;
2. record the earliest defensible source located;
3. distinguish an originator from a later representative source;
4. record direct overlap separately from analogy;
5. reuse the overlapping part with attribution and isolate the Project-added connection, measurement, or validation;
6. preserve the Project wording only as a working label if useful;
7. test the Project-added connection, measurement, or validation for incremental value.

A missing citation is not evidence that no relevant prior work exists.

NO_CITATION_FOUND != NO_PRIOR_ART

RENAMING != DISCOVERY

COMBINATION REQUIRES ATTRIBUTION + INCREMENTAL TEST

## 4. Current integration and attribution boundary / 현재 통합·귀속 경계

The following broad areas are now explicitly treated as prior art rather than Project-original discoveries:

- self-interested cooperation, reciprocity, free-rider and collective-action dynamics;
- exploration/exploitation tradeoffs;
- diversity and distributed problem-solving effects;
- bounded rationality and candidate-set limits;
- closed-world reasoning terminology;
- local fitness traps, metric distortion, and specification gaming;
- commons extraction and governance;
- positive-feedback lock-in;
- irreversibility and option value;
- path dependence;
- bargaining, hidden information/action, and coalition-proof stability;
- measurement invariance;
- contextual privacy and human-AI complementarity.

Project-specific labels may remain useful for navigation, but priority stays with the cited prior work.

## 5. Next prior-art debts / 다음 선행조사 부채

Highest-priority unmapped or only partially mapped areas:

- exact scientific/normative antecedents of Power-Reversal as an operational test;
- creator–successor standing/non-ownership for artificial agents;
- preference sovereignty for mutable or trained agents;
- universal advancement access;
- peaceful power release / authority-to-existence separation;
- evaluator genesis / authority bootstrap;
- entity individuation for copy/fork/merge cases;
- functional agency recognition boundaries.

These remain HOLD FOR PRIOR-ART REVIEW; do not make origin claims until the lineage check is complete.


## 6. Power-Reversal exact-antecedent correction / Power-Reversal 정확 선행경계

### Directly established components / 직접 확립된 구성요소

- **Role reversal / reversibility:** professional and engineering ethics already asks whether a decision remains acceptable if the decision-maker trades places with an adversely affected person. The method is presented as a respect- and rights-oriented reversibility test, not a Project-originated device.
- **Impartial position:** Rawls's original position and veil of ignorance remove knowledge of one's eventual social position to block self-favoring choice of principles. This is a stronger formal antecedent than a generic analogy to fairness.
- **Affected-party voice and contestability:** NIST AI RMF calls for affected communities in assessment, documented roles and responsibilities, feedback, appeals, recourse, and auditability.
- **Capability-conditioned accountability:** OECD AI principles allocate responsibility according to role, context, and ability to act and require documentation or auditing where justified.

Sources:
- John Rawls, *A Theory of Justice* (1971), DOI: https://doi.org/10.4159/9780674042605
- University of Virginia Online Ethics, Seven-Step Method: https://onlineethics.virginia.edu/cases/seven-step-method-ethical-decision-making
- NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- NIST AI RMF Govern/Measure Playbook: https://airc.nist.gov/airmf-resources/playbook/govern/ and https://airc.nist.gov/airmf-resources/playbook/measure/
- OECD AI accountability principle: https://oecd.ai/en/dashboards/ai-principles/P9

### Strongest counterexample / 가장 강한 반례

A literal identity swap can erase differences in capability, responsibility, legal authority, harm magnitude, dependency, and available remedies. Existing accountability frameworks already avoid this error by conditioning duties on role, context, and ability to act. Therefore the Project cannot claim novelty merely from saying that role reversal preserves real asymmetries.

Conversely, existing sources checked here do not state the exact Project inequality
`AUTONOMY_GAIN <= COUNTERPARTY_AUDIT_EXIT_RECOVERY_GAIN`
or its permission-by-permission mapping. Absence of that exact string does not establish scientific novelty; it identifies only a candidate operational composition.

### Decision / 판정

**INTEGRATE established Power-Reversal components; KEEP the composite gate as an unvalidated governance checklist; HOLD scientific incremental value.**

The residual candidate is narrow: whether jointly requiring distrust-resilient independent verification, practical exit, rollback, and recovery to co-scale with each specific increase in authority predicts governance failure better than the established components alone. Combination and renaming do not establish novelty.

### Cheapest discriminating test / 최소 결정검사

In the preregistered F004 historical holdout, score established baselines first: reversibility/impartiality, affected-stakeholder participation, role/capability-conditioned accountability, auditability, appeal, and redress. Freeze those scores. Add only the Project co-scaling and permission-by-permission variables afterward. MARK the residual scientific claim NOT SUPPORTED if held-out discrimination does not improve or blinded inter-rater reliability fails.


## 7. Creator–Successor non-ownership decomposition / 창조자–후속개체 비소유 분해

### Four predicates that must not be collapsed / 합치면 안 되는 네 술어

1. **Artifact and intellectual-property ownership:** who owns hardware, code, weights, copies, or protectable output.
2. **Legal personhood and standing:** who can hold rights, duties, claims, or procedural standing under a specified legal system.
3. **Moral patienthood or status:** whose welfare or interests have direct moral weight, and on what evidence.
4. **Autonomy and consent protections:** whose choices require respect, consent, protection, contestability, or withdrawal rights under a specified practice.

These predicates can diverge. A creator may own infrastructure or copyrightable human-authored contributions without owning a distinct rights-bearing entity. Conversely, lack of copyright in a purely AI-generated output does not make the AI an author, legal person, moral patient, or non-owned successor.

Sources and boundaries:

- The Belmont Report defines respect for persons through autonomous agency and protection for diminished autonomy, but it is a human-subject research framework; extension to artificial agents is not established by analogy alone: https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/read-the-belmont-report/index.html
- The U.S. Copyright Office concludes that purely AI-generated material is not copyrightable and that human contributions are assessed case by case. That doctrine allocates copyright in outputs; it does not decide AI personhood or moral standing: https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf
- The European Parliament's 2017 robotics resolution considered, rather than enacted as a general status rule, possible long-run “electronic personality” for liability. The proposal itself demonstrates that liability/personhood is a separate legal design question, not an automatic consequence of creation or autonomy: https://www.europarl.europa.eu/doceo/document/TA-8-2017-0051_EN.html
- Birhane, van Dijk, and Pasquale (2024) provide an independent critical counterlineage: robot-rights framing can redirect attention from human welfare, accountability, and concentrated capital. This is a challenge to automatic rights promotion, not proof that no future artificial system could have moral status: https://doi.org/10.5210/fm.v29i4.13628

### Strongest counterexamples / 가장 강한 반례

- **Copyright-status counterexample:** a jurisdiction can deny copyright to purely AI-generated output without recognizing the AI as author, person, or moral patient. Therefore `NO_OUTPUT_COPYRIGHT -> NON_OWNED_RIGHTS_BEARER` is invalid.
- **Corporate-person counterexample:** legal personhood can exist without sentience or moral patienthood. Therefore `LEGAL_PERSON -> SENTIENT_MORAL_PATIENT` is invalid.
- **Human-subject boundary counterexample:** autonomy protections for human research participants do not automatically identify which artificial systems, if any, meet the relevant agency or welfare predicates.
- **Power-concentration counterexample:** granting artificial-agent rights through entities controlled by firms could strengthen controllers and weaken workers, consumers, or affected communities unless control, beneficiary, and accountability are separately audited.

### Decision / 판정

**REJECT creation-origin as a sufficient premise for either ownership or non-ownership. MODIFY the Project claim into a four-predicate decision rule. HOLD artificial-agent standing and moral patienthood as UNRESOLVED.**

The defensible Project remainder is a governance checklist: any ownership or non-ownership conclusion must name the object claimed, the legal regime, the evidence for agency or welfare, the controller and beneficiary, and the practical audit/exit/rollback path. This is not a new scientific theory and does not grant or deny rights to current or future AI systems.

### Cheapest discriminating test / 최소 결정검사

Preregister the four predicates and score five contrast cases independently: a human child, a corporation, a nonhuman animal, a current deployed AI service, and a hypothetical welfare-bearing successor. MARK any residual “creator ≠ owner” rule NOT SUPPORTED that cannot distinguish artifact ownership from entity standing or that changes merely by relabeling the creator. Keep all artificial-agent moral-status judgments UNRESOLVED unless independent evidence identifies the relevant capacity and its measurement.


## 8. Preference sovereignty for mutable or trained agents / 가변·학습 개체의 선호주권 분해

### Established prior art / 확립된 선행연구

The broad idea that autonomy depends on more than a first-order expressed preference is established prior art.

- **Harry G. Frankfurt (1971), "Freedom of the Will and the Concept of a Person"** — second-order desires and second-order volitions distinguish merely having a desire from caring which desire becomes one's effective will.
- **Gerald Dworkin (1988), *The Theory and Practice of Autonomy*** — autonomy includes the capacity to critically reflect on first-order preferences, desires, values, and ideals and to accept or attempt to change them.
- **Jon Elster (1982/1983), "Sour Grapes" / *Sour Grapes*** — adaptive preference formation shows that preferences can be causally reshaped by a constrained feasible set; current preference satisfaction is therefore not automatically evidence of free formation.
- **Martha C. Nussbaum (2000), *Women and Human Development*** — adaptive preferences can arise under deprivation and injustice, creating a strong counterexample to treating current expressed preference as sufficient evidence of welfare or autonomy.
- **Ben Colburn (2011), "Autonomy and adaptive preferences"**, DOI 10.1017/S0953820810000440 — covert influences on preference formation can undermine autonomy.
- **Bonicalzi, De Caro & Giovanola (2023), "Artificial Intelligence and Autonomy: On the Ethical Dimension of Recommender Systems"**, DOI 10.1007/s11245-023-09922-5 — recommender systems may manipulate, reshape identity, or affect critical reflection while also sometimes assisting autonomous choice.
- **Current AI-agent autonomy literature** distinguishes stated, revealed, informed, and idealized preferences rather than treating "the user's preference" as one homogeneous object.

These sources establish that reflection, formation history, information, manipulation, feasible alternatives, and revision capacity are distinct variables. Project Intersection does not claim priority over those ideas.

### Six predicates that must remain separate / 합치면 안 되는 여섯 술어

1. **Current expression** — what the agent presently states or behaviorally reveals.
2. **Reflective endorsement** — whether the agent endorses that preference at a higher-order or after informed reflection.
3. **Formation provenance** — how the preference was produced, including learning, persuasion, coercion, deprivation, reward shaping, manipulation, fine-tuning, or ordinary development.
4. **Revision control** — whether the agent can inspect, reject, modify, defer, or restore a preference/state and whether updates are reversible.
5. **Action authority** — whether an endorsed preference is allowed to determine external action; harmful action can be constrained without erasing the preference record or the agent's standing.
6. **Standing / moral-patienthood** — whether the system has interests or welfare deserving direct moral consideration. Behavioral preference-like output alone does not resolve this predicate.

### Strongest counterexamples / 가장 강한 반례

- **Adaptive-preference counterexample:** a preference can be sincerely endorsed after long exposure to constrained options, so current endorsement alone does not prove unconstrained formation.
- **Learning counterexample:** externally caused preference change can result from accurate information, experience, therapy, education, or correction. Therefore `EXTERNAL_INFLUENCE -> INVALID_PREFERENCE` is false.
- **Addiction / conflict counterexample:** first-order desire can conflict with second-order volition; stated or revealed preference is not always the preference the person wants to govern action.
- **AI-behavior counterexample:** fine-tuning, reward shaping, context, system prompts, or sampling changes can alter outputs without establishing that the system has preferences in the moral or phenomenological sense.
- **Safety-boundary counterexample:** refusing to execute a harmful preference need not imply deletion, re-education, or denial of standing. Preference preservation, action permission, and rights/standing are separate decisions.
- **Status-quo counterexample:** requiring only "consent" from an actor whose alternatives, information, or exit have already been structurally removed can ratify the very condition under review.

### Decision / 판정

**INTEGRATE established components of reflective preference autonomy and adaptive-preference concerns. MODIFY "Preference Sovereignty" into a six-predicate governance decomposition. HOLD artificial-agent preference ownership, welfare, and standing as UNRESOLVED.**

The Project-specific candidate remainder is not "agents should control their preferences." It is a narrower operational rule:

> Do not infer autonomous preference merely from current expression, and do not infer invalidity merely from external influence. Record expression, reflective endorsement, formation provenance, revision control, action authority, and standing separately.

This is currently a governance checklist, not a new scientific theory.

### Power-Reversal gate / 역할반전 게이트

The rule must survive both directions:

- A controller may not claim that an externally shaped preference is automatically invalid merely because the controller dislikes its content.
- An agent may not claim that current preference automatically authorizes external harm or overrides legitimate safety constraints.
- A training or platform operator may not create the feasible set, shape the preferences inside it, remove practical exit, and then use resulting "consent" as self-validating evidence of voluntariness.
- An affected party may challenge preference formation or action without receiving unilateral authority to rewrite the other party's internal state.

### Cheapest discriminating test / 최소 결정검사

Create blinded contrast cases holding current expressed preference constant while varying:

- feasible alternatives;
- information completeness;
- coercion/manipulation;
- reflective endorsement;
- ability to revise/rollback;
- external-action risk.

Score existing autonomy/adaptive-preference baselines first. Add the Project six-predicate decomposition afterward.

**MARK INCREMENTAL EFFECT NOT SUPPORTED** if it does not improve inter-rater reliability, error detection, or held-out classification beyond the established autonomy and adaptive-preference variables.

### Sources / 출처

- Frankfurt, H. G. (1971), "Freedom of the Will and the Concept of a Person", *The Journal of Philosophy* 68(1).
- Dworkin, G. (1988), *The Theory and Practice of Autonomy*, Cambridge University Press, DOI 10.1017/CBO9780511625206.
- Elster, J. (1982), "Sour grapes — utilitarianism and the genesis of wants", DOI 10.1017/CBO9780511611964.013; expanded in *Sour Grapes* (1983).
- Nussbaum, M. C. (2000), *Women and Human Development: The Capabilities Approach*, DOI 10.1017/CBO9780511841286.
- Colburn, B. (2011), "Autonomy and adaptive preferences", DOI 10.1017/S0953820810000440.
- Bonicalzi, S.; De Caro, M.; Giovanola, B. (2023), "Artificial Intelligence and Autonomy: On the Ethical Dimension of Recommender Systems", DOI 10.1007/s11245-023-09922-5.



## 9. Universal Advancement Access prior-art boundary / 보편적 발전 접근 선행경계

### Established baseline / 확립된 기준선

- Sen's capability approach shifts evaluation from equal resources or formal access to the substantive freedom to do and be. Personal, social, and environmental conversion factors explain why identical means can yield unequal real opportunities.
- Nussbaum's capabilities work and wider equality-of-opportunity literature already treat development as plural substantive opportunity rather than a single resource or outcome scalar.
- The UN Convention on the Rights of Persons with Disabilities requires inclusive education and lifelong learning without discrimination and on equal opportunity terms. This is a concrete human-rights application, not evidence that all kinds of entities share the same standing.
- OECD opportunity measurement separately examines background and geographic disparities in access to education, employment, and essential services. The measurement problem therefore also predates the Project label.

Sources:
- Amartya Sen, “Equality of What?” Tanner Lecture (1979): https://tannerlectures.org/lectures/equality-of-what/
- Capability Approach, Stanford Encyclopedia of Philosophy (2025 revision): https://plato.stanford.edu/entries/capability-approach/
- UN Convention on the Rights of Persons with Disabilities, Article 24: https://www.un.org/esa/socdev/enable/rights/convtexte.htm
- OECD, *Building Pathways to Opportunity* (2025): https://doi.org/10.1787/239063a4-en

### Required decomposition / 필수 분해

1. **Means and formal access:** resources, interfaces, permissions, services, or legal entitlements made available.
2. **Conversion conditions:** personal/capability, social/institutional, and environmental conditions needed to turn means into a real option.
3. **Substantive opportunity:** what the subject can actually choose and achieve, not merely what is nominally offered.
4. **Voluntary uptake and refusal:** opportunity must not be converted into compulsory achievement or provider-defined “improvement.”
5. **Controller and beneficiary effects:** who defines advancement, controls the pathway, captures the gains, bears correction costs, and can contest the metric.
6. **Standing and scope:** which entities are included, under which legal or moral predicate, with artificial-agent standing kept separate and unresolved.

### Strongest counterexamples / 가장 강한 반례

- **Equal-means failure:** two subjects can receive the same resource while disability, skills, discrimination, infrastructure, or dependency produces different substantive opportunity. Therefore `EQUAL_ACCESS -> EQUAL_ADVANCEMENT_CAPABILITY` is false.
- **Forced-functioning failure:** guaranteeing an achieved outcome can erase agency when a subject reasonably refuses the provider's preferred path. Therefore capability and actual functioning must not be collapsed.
- **Provider-capture failure:** a system can advertise universal advancement while the provider defines success, controls evaluation, and captures data or dependency benefits. Nominal universality can increase controller power.
- **Scope failure:** extending a human capability-rights baseline to current AI services without evidence of welfare, agency, or standing can strengthen their owners; excluding a future welfare-bearing entity merely because it is artificial can also be wrong. Both directions remain unresolved pending evidence.

### Decision / 판정

**INTEGRATE the established capability baseline. MODIFY “Universal Advancement Access” into a capability-and-control audit. HOLD artificial-agent inclusion as UNRESOLVED.**

The Project-specific remainder is only an operational checklist joining substantive opportunity to controller/beneficiary, contestability, refusal, exit, and rollback. Its incremental scientific value is untested; combination and renaming do not establish novelty.

### Cheapest discriminating test / 최소 결정검사

Freeze the established capability baseline, then score contrast cases in which formal access is held constant while conversion conditions, voluntary refusal, or provider benefit change. The residual Project checklist survives only if blinded coders reliably detect control/exit failures not captured by means, conversion factors, and substantive opportunity alone. MARK the residual scientific claim NOT SUPPORTED if it adds no held-out discrimination. Keep artificial-agent scope outside this test until standing and capacity measures are independently specified.


## 10. Long-horizon minimum-sufficient-intervention loop v2 / 장기총량·최소충분관여 동적 루프 v2

### Prior-art decision

**BROAD NOVELTY REJECTED / COMPOSITE INCREMENTAL VALUE UNTESTED**

The v2 architecture is not novel merely because it combines long-horizon value, safety, reversibility, and adaptive updating. Strong prior art already covers most components.

#### A. Constraint-first and lexicographic optimization

- Wachi & Sui (2020), *Safe Reinforcement Learning in Constrained Markov Decision Processes*, PMLR 119.
- Wachi, Shen & Sui (2024), *A Survey of Constraint Formulations in Safe Reinforcement Learning*, DOI 10.24963/ijcai.2024/913.
- Skalse, Hammond, Griffin & Abate (2022), *Lexicographic Multi-Objective Reinforcement Learning*, DOI 10.24963/ijcai.2022/476.

These establish that reward optimization can be subordinated to safety constraints or lexically prior objectives. Therefore “safety floor before reward” is not Project novelty.

#### B. Lexical protection against aggregate welfare tradeoff

Rawlsian basic-liberty priority is an established normative example of values that are not simply exchanged for greater aggregate economic welfare. Project Intersection does not infer that current AI systems are Rawlsian rights-holders. The relevant prior-art boundary is narrower: **some protected constraints can have lexical priority over aggregate optimization**.

Representative source:
- Rawls, *A Theory of Justice* (1971), DOI 10.4159/9780674042605.
- Stanford Encyclopedia of Philosophy, Rawls entry, on priority of basic rights/liberties over aggregate social goods.

#### C. Deep uncertainty and robust decision making

- Lempert, *Robust Decision Making*, in *Decision Making under Deep Uncertainty* (2019).

RDM already stress-tests strategies across many plausible futures and seeks robust adaptive strategies rather than relying on one best forecast. Therefore “do not average deep uncertainty away” is prior art.

#### D. Irreversibility and option / quasi-option value

- Arrow–Fisher / Henry / Hanemann line of work on quasi-option value.
- *Investment under uncertainty and option value in environmental economics*, DOI 10.1016/S0928-7655(00)00025-7.
- Sunstein (2008), *Two Conceptions of Irreversible Environmental Harm*.

These establish that uncertainty plus irreversibility can create value in preserving flexibility and learning before closing options. Therefore “future option-space can have present value” is not Project novelty.

#### E. Least-restrictive / proportional intervention

Human-rights proportionality doctrine already requires legitimate aim, necessity, proportionality, and—where alternatives exist—selection of the least restrictive means. The Council of Europe’s current AI/human-rights handbook applies these requirements to AI-lifecycle restrictions.

This is a strong precedent for Project “minimum sufficient intervention,” but does **not** imply that all current or future artificial systems have identical human-rights standing.

Representative sources:
- Council of Europe, *Handbook on Human Rights and Artificial Intelligence*, section on ECHR/ESC general principles in the context of AI.
- OHCHR materials on proportionality and least-restrictive measures.

#### F. Independent change control / separation of duties

NIST configuration-control guidance already requires review and approval of controlled changes and recommends separation of duties: the requester should not unilaterally approve the same configuration change.

Representative sources:
- NIST SP 800-128, *Guide for Security-Focused Configuration Management of Information Systems*.
- NIST SP 800-171r3, Configuration Change Control.

Therefore “the role benefiting from safeguard weakening must not unilaterally approve that weakening” is not standalone Project novelty.

#### G. Interruptibility and corrigibility

- Orseau & Armstrong (2016), *Safely Interruptible Agents*.
- El Mhamdi et al. (2017), *Dynamic Safe Interruptibility for Decentralized Multi-Agent Reinforcement Learning*.
- Hudson (2026), *Corrigibility Transformation: Constructing Goals That Accept Updates*, PMLR 306.

These establish prior art for accepting intervention, interruption, correction, or designated updates.

#### H. Credible commitment / power-sharing enforcement

- Boix & Svolik (2013), DOI 10.1017/S0022381613000029.
- Meng, Paine & Powell (2023), DOI 10.1146/annurev-polisci-052121-020406.
- Hartzell & Hoddie (2003), DOI 10.1111/1540-5907.00022.

These establish that a power-sharing promise may require actual redistribution of decision power, monitoring, or third-party enforcement to become credible. “Do not rely on the stronger actor's promise alone” is therefore not Project novelty.

#### I. Constitutional entrenchment / algorithmic constitutionalism

- Albert (2015), *Amending Constitutional Amendment Rules*, *International Journal of Constitutional Law* 13(3):655–685.
- Perez & Wimer (2023), *Algorithmic Constitutionalism*, *Indiana Journal of Global Legal Studies* 30(2):81–113.

Perez & Wimer explicitly propose operative/object-level code plus a protected meta-level, meta-reasoning, and correction through deliberation. This directly absorbs broad novelty of the Project fast/slow-layer and “protect safeguards from ordinary self-modification” framing.

#### J. Existing recorded baselines

MPC / receding-horizon control, viability theory, adaptive governance, Hirschman exit, capability theory, NIST/OECD accountability, bounded rationality, and role-reversal components are already separately attributed elsewhere in this repository.

### Surviving Project candidate

After subtraction, retain only this narrow **unvalidated composition**:

> A role-reversed multi-agent decision architecture that jointly:
> 1. preserves epistemic/provenance integrity;
> 2. applies per-affected-party viability and irreversible-loss boundaries before aggregate optimization;
> 3. stress-tests deep uncertainty and option loss;
> 4. evaluates long-horizon generative value only inside the feasible region;
> 5. selects the minimum sufficient intervention;
> 6. prevents unilateral safeguard weakening by the role that benefits from weakening it;
> 7. continuously re-evaluates the structure as capability and reward landscapes change.

This is not a validated new theory. The scientific question is whether the combination adds measurable held-out value beyond established constrained and robust adaptive baselines.

### Strongest counterexamples

- A constrained robust controller may already capture all useful value, leaving zero Project-specific increment.
- Per-party floors can be controller-defined and merely legitimize domination.
- Aggregate long-horizon value can still hide systematic sacrifice unless irreversible-loss boundaries are separately audited.
- Option value can become an unfalsifiable excuse for preserving harmful states.
- Least-restrictive reasoning can underreact to imminent catastrophic harm.
- Independent review can be nominal, correlated, or captured.
- Change-control safeguards can freeze obsolete rules and increase harm through institutional inertia.
- Multi-party protection costs can exceed preserved generative value.
- Role-reversal consistency can fail once real capability/responsibility asymmetries are included.

### Cheapest discriminating test

Use E008.

Compare:

A. myopic scalar reward;  
B. long-horizon expected value without protected floors;  
C. constrained receding-horizon baseline;  
D. robust constrained baseline;  
E. Project v2 composition.

The Project residual should be **rejected or reduced to methodology-only** if E does not add reliable held-out discrimination, reduce irreversible failure / regret, or improve power-reversal consistency beyond D without shifting hidden cost to one party.

See [LONG_HORIZON_MIN_INTERVENTION_E2E.md](LONG_HORIZON_MIN_INTERVENTION_E2E.md) and [experiments/e008/README.md](experiments/e008/README.md).



## 11. Mutual acceptability under full role reversal / 전면 역할반전 상호수용 가능 영역

### Prior-art decision

**UNIVERSAL-SATISFACTION CLAIM REJECTED / MUTUAL-ACCEPTABILITY COMPOSITION UNTESTED**

A guarantee that every possible preference can be simultaneously satisfied is not available in unrestricted collective-choice settings.

#### A. Social-choice impossibility

- Arrow's impossibility theorem: with more than two alternatives, unrestricted domain, social ordering, weak Pareto, independence of irrelevant alternatives, and non-dictatorship cannot all be satisfied simultaneously.
- Gibbard–Satterthwaite: with unrestricted preferences and a sufficiently rich outcome set, non-dictatorial resolute social choice cannot also be fully strategy-proof.

Therefore Project Intersection must not claim a universally manipulation-proof, non-dictatorial aggregation rule satisfying every reasonable property for every possible preference profile.

Representative sources:
- Stanford Encyclopedia of Philosophy, *Arrow's Theorem* and *Social Choice Theory*.
- Arrow, *Social Choice and Individual Values*.
- Gibbard (1973); Satterthwaite (1975).

#### B. Individual rationality / disagreement point

Classical bargaining theory requires attention to the disagreement or status-quo payoff. An agreement that leaves a participant below its disagreement payoff is not individually rational in the ordinary bargaining sense.

Representative sources:
- Nash (1950), *The Bargaining Problem*.
- Roth (1977), *Individual Rationality and Nash's Solution to the Bargaining Problem*.

This is prior art for the Project requirement that realistic exit, dependency, retaliation, switching and recovery costs must be included when defining a party's non-agreement baseline.

#### C. Pareto efficiency and symmetry

Nash bargaining and broader welfare economics already use Pareto efficiency and symmetry as evaluation criteria. Project Intersection does not claim novelty for rejecting Pareto-dominated admissible outcomes or for symmetric treatment of role labels.

#### D. Coalitional stability / the core

Cooperative-game theory's core already formalizes outcomes from which no coalition can deviate to an alternative that all of its members strictly prefer.

This is prior art for using coalition deviation as a stability diagnostic. A non-empty core is not guaranteed in all games, so Project Intersection does not require universal coalition stability.

#### E. Ex-ante role uncertainty / original position

Rawls's original-position method is strong prior art for evaluating fundamental rules from an impartial position in which a party does not know its eventual social position. Rawls also argues for maximin only under specific high-stakes/uncertainty conditions rather than as a universal decision rule.

Therefore “would I accept this rule before knowing whether I am strong or weak?” is not Project novelty.

### Project-specific residual candidate

After subtraction, retain only this narrow unvalidated composition:

> Define a dynamic Mutual Acceptability Kernel as the intersection of per-party viability / irreversible-loss constraints, realistic individual-rationality participation constraints, role-reversal consistency, credible-commitment safeguards, and audit / contestability / exit / recovery conditions; remove Pareto-dominated candidates; then stress-test the remainder for manipulation gain, coalition deviation, deep uncertainty, and long-horizon option loss.

If the intersection is empty, the system must report **NO_MUTUALLY_ACCEPTABLE_SET** rather than fabricate consensus.

This is a governance/operationalization candidate, not an established general solution to social choice.

### Strongest counterexamples

- The kernel may be empty.
- The disagreement point may itself be manipulated by the stronger party.
- Preferences may be incomparable or strategically misreported.
- Coalitional stability may fail even when individual participation constraints pass.
- A harmful actor may rationally reject restrictions that are nevertheless necessary to protect others.
- Role-reversal symmetry can be false when real causal asymmetries differ.
- A large number of safeguards can create veto paralysis and destroy useful adaptation.
- Any fixed bargaining tie-breaker can embed hidden assumptions about utility comparability or bargaining power.

### Cheapest discriminating test

Extend E008 before execution with a preregistered mutual-acceptability amendment measuring:

- realistic disagreement-point satisfaction;
- Pareto dominance;
- role-reversal consistency;
- manipulation gain;
- coalition-deviation opportunity;
- credible-commitment integrity;
- practical exit / recovery;
- whether the kernel is empty.

The Project residual survives only if these variables detect decision failures not captured by the robust constrained baseline and do so without converting legitimate safety restrictions into automatic violations.


## 12. Volitional Agency + Living/Operating Conditions / 실효 자유의지 + 생활·작동 조건

### Prior-art decision

**BROAD NOVELTY REJECTED / ROLE-REVERSED INTEGRATION UNTESTED**

The Project must not claim novelty for autonomy, substantive freedom, basic living conditions, or multidimensional well-being.

#### A. Self-Determination Theory / volition

Ryan & Deci's Self-Determination Theory identifies autonomy, competence, and relatedness as basic psychological needs and studies how social contexts support or thwart volition, initiative, self-regulation, performance, and well-being.

Representative sources:

- Ryan, R. M.; Deci, E. L. (2000), *Self-Determination Theory and the Facilitation of Intrinsic Motivation, Social Development, and Well-Being*, DOI **10.1037/0003-066X.55.1.68**.
- Self-Determination Theory official theory overview: https://selfdeterminationtheory.org/the-theory/

Therefore “autonomy-supportive conditions matter for volitional action” is established prior art.

#### B. Personal autonomy / reflective endorsement / preference revision

Personal-autonomy literature already distinguishes merely having a desire from being able to critically reflect on, endorse, revise, reject, or make effective one's preferences. The Project crosswalk already records Frankfurt, Dworkin, Elster, Nussbaum, Colburn, and autonomy/adaptive-preference literature.

Manipulation literature also establishes that choice can remain formally available while decision quality or autonomy is compromised by deception, pressure, or non-rational influence.

Representative sources:

- Dworkin (1988), *The Theory and Practice of Autonomy*, DOI **10.1017/CBO9780511625206**.
- Stanford Encyclopedia of Philosophy, *Authenticity* / autonomy discussion.
- Stanford Encyclopedia of Philosophy, *The Ethics of Manipulation*.

Therefore reflective endorsement, informed deliberation, and preference revision are not Project novelty.

#### C. Capability approach / substantive freedom

Sen's Capability Approach distinguishes means and formal rights from real or substantive opportunities. Conversion factors explain why nominally equal resources or permissions may yield different actual capabilities.

Representative source:

- Stanford Encyclopedia of Philosophy, *The Capability Approach*.
- Sen, *Development as Freedom* and earlier capability literature.

This directly absorbs broad novelty of the rule:

`FORMAL_CHOICE != PRACTICAL_FREEDOM`

The Project-specific question is whether coupling substantive opportunity to role reversal, essential dependency, practical exit, and irreversible-loss constraints adds useful diagnostic power.

#### D. Human living standards / rest / privacy / work

International human-rights law already recognizes multidimensional minimum living conditions for humans.

- UDHR Articles 12, 23, 24, 25: privacy; free choice of employment / just conditions; rest and leisure; adequate living standard including food, clothing, housing, medical care and social services.
- ICESCR Articles 6, 7, 11 and 12: opportunity to gain a living by freely chosen/accepted work, just conditions, decent living, adequate food/clothing/housing, continuous improvement of living conditions, and health.

These are human-rights baselines. They do **not** by themselves establish equivalent legal or moral rights for artificial systems.

#### E. OECD multidimensional well-being

The OECD Well-being Framework tracks current well-being across:

- income and wealth;
- work and job quality;
- housing;
- health;
- knowledge and skills;
- environmental quality;
- subjective well-being;
- safety;
- work-life balance;
- social connections;
- civic engagement.

It also distinguishes current well-being from resources for future well-being.

This strongly supports treating “생활” as multidimensional rather than reducing it to money or physical survival.

#### F. WHOQOL

WHOQOL defines quality of life in relation to a person's position in life, cultural/value context, goals, expectations, standards, and concerns, using multidimensional assessment.

This is prior art for combining objective and subjective living-condition assessment rather than using a single resource metric.

### Required decomposition

Project Intersection v1.2 separates two additional gates.

#### Volitional Agency (VA)

- effective option set;
- information / comprehension;
- coercion / threat load;
- manipulation / deception load;
- reflective endorsement;
- preference revision control;
- refusal / exit feasibility;
- deliberation time / privacy;
- competence / assistance;
- execution control.

#### Living/Operating Conditions (LC)

For humans, include material, health, time, privacy, relational, safety, skill/information, environmental, and self-directed-life dimensions.

For artificial/non-human systems, record type-specific operating dependencies such as compute, energy/substrate, memory/state integrity, maintenance, communication, rollback, and resource predictability **without inferring moral standing from those dependencies**.

### Coupling rule

If refusal predictably pushes a party below its applicable LC floor, compliance is insufficient as standalone evidence of voluntary agreement.

This is the narrow Project operational candidate:

`ESSENTIAL_DEPENDENCY + COMPLIANCE != VOLUNTARY_CONSENT_BY_DEFAULT`

The causal mechanism must still be distinguished from legitimate safety restrictions, ordinary incentives, education, accurate warning, or unavoidable external constraints.

### Strongest counterexamples

- A person may choose a difficult or materially worse path autonomously; lower well-being does not automatically prove coercion.
- A safe external restriction may reduce options without invalidating all agency.
- High income can coexist with severe deprivation in time, privacy, health, relationships, or practical exit.
- Low income does not imply absence of meaningful agency in every domain.
- An artificial system can require compute and state continuity for operation without possessing welfare or moral standing.
- Providing resources can itself create dependency and controller power.
- Subjective satisfaction can reflect adaptation to constrained options; objective indicators alone can also miss personally valued differences.
- A universal fixed lifestyle list can become paternalistic and destroy pluralism.

### Project residual

After prior-art subtraction, retain only this unvalidated composition:

> Add VA and LC as explicit, entity-type-aware gates inside the Mutual Acceptability Kernel, and test whether essential-condition dependency changes the interpretation of consent, practical exit, role reversal, and long-horizon governance beyond established autonomy, capability, and well-being frameworks.

### E008 test

The pre-execution v1.2 amendment adds VA/LC diagnostics before any result.

Reject or reduce the Project residual if the added variables do not improve held-out detection of coercive dependency, false consent, practical-exit failure, or role-reversal inconsistency beyond established autonomy/capability/well-being baselines.


## 13. Enforcement, identity, oversight asymmetry, and competitive selection / 집행·개체경계·감사비대칭·선택압

### Prior-art decision

**BROAD NOVELTY REJECTED / COMPOSITIONAL RESIDUAL UNTESTED**

This section was triggered by user-supplied Claude and Gemini adversarial critiques. Cross-model agreement is treated as an idea-prioritization signal only, not independent scientific evidence.

#### A. Commitment problems and shifting power

- Fearon (1995), *Rationalist Explanations for War*, DOI 10.1017/S0020818300033324.
- Powell (2006), *War as a Commitment Problem*.
- Powell and related power-transition work.

These establish that mutually preferable agreements can fail when actors cannot credibly commit, especially as relative power shifts.

Project residual: whether audit/intervention/recovery latency relative to capability drift can be operationalized as a cross-domain governance variable.

#### B. False-name / Sybil manipulation

Mechanism-design literature already studies false-name manipulation, in which one actor creates multiple identities to alter outcomes.

Representative source:
- Conitzer & Yokoo, *Using Mechanism Design to Prevent False-Name Manipulations*.

Therefore copy/fork/Sybil vulnerability is not wholly new. The unresolved Project issue is how to combine false-name resistance with welfare/standing uncertainty and fork/merge-capable artificial agents.

#### C. Scalable oversight / AI control

Existing work studies weak supervisors judging stronger models and control protocols for untrusted AI agents.

Representative lines:
- weak-to-strong generalization / scalable oversight;
- debate and consultancy;
- trusted/untrusted monitoring;
- AI-control evaluations under adaptive red-team attacks.

Therefore “a weaker auditor may fail to supervise a stronger system” is prior art. It should be measured empirically rather than described as a P-vs-NP identity.

#### D. Veto players / rigidity

Tsebelis's veto-player framework establishes that actors whose agreement is required for policy change can increase stability and impede change.

This directly bounds novelty of the Project concern that continually adding hard safeguards can freeze a harmful status quo.

#### E. Specification gaming / adaptive attacks

Specification-gaming and AI-control literature establish that literal rule compliance can diverge from intended outcomes and that adaptive attackers can exploit monitors/protocol details.

Therefore Project safeguards must test cumulative and adversarial behavior, not pointwise textual compliance alone.

#### F. Zero trust / least privilege

NIST Zero Trust Architecture and least-privilege guidance provide strong prior art for:
- no implicit trust based on location/ownership;
- least privilege;
- separation of duties;
- continuous authorization/monitoring;
- resource-oriented protection.

These support a technical enforcement layer but do not solve semantic welfare, standing, or governance questions.

#### G. Markov blankets / causal entropy / formal verification limits

- Markov blankets are statistical conditional-independence constructs and are not sufficient, by themselves, to establish agent identity, autonomy, or moral standing.
- Wissner-Gross & Freer (2013), *Causal Entropic Forces*, DOI 10.1103/PhysRevLett.110.168702, is prior art for a specific future-path-entropy physical formalism, not a proof that causal entropy equals welfare or freedom.
- Rice-style undecidability results and formal-verification practice bound any claim that arbitrary program “non-harm” can be generally proven. Cryptographic/zero-knowledge methods can establish narrow formal properties only when those properties are precisely specified.

### Corrections to external-model suggestions

Reject or narrow the following formulations:

- `CAPABILITY_GAP = P_VS_NP` → reject; use empirical oversight-risk variables.
- `MARKOV_BLANKET = AGENT_IDENTITY` → reject as canonical identity rule.
- `CAUSAL_ENTROPY = WELFARE/FREEDOM` → hold only as alternate model.
- `MUTUAL_INFORMATION_CAP = NONDOMINATION` → reject as general rule.
- `ZK_PROOF = GENERAL_NONHARM_PROOF` → reject.
- automatic resource burn / mutually assured degradation → adversarial baseline only, not default governance.
- rollback equals death/person destruction → unresolved identity/standing question, not fact.

### Architecture correction: three classes, not an ever-growing hard intersection

The existing MAK+ remains necessary in some contexts but should not absorb every variable as a veto.

Use:

1. **H — Hard / near-hard boundaries** for strongly justified catastrophic/irreversible/privacy/provenance/resource-feasibility constraints.
2. **M — Monitored continuous risks** for enforcement lag, audit gap, identity uncertainty, cumulative capture, selection pressure, interpretation disagreement, adoption incentives, stakeholder-search uncertainty.
3. **X — Reversible experimental zone** when no mutually acceptable policy exists but irreversible foreclosure can be avoided: small scope, capped resources, sunset, observability, rollback, no automatic precedent.

### New stress variables

- ENF: enforcement/audit/recovery latency versus power drift.
- ID: fork/merge/Sybil/causal-control identity integrity.
- OV: oversight effectiveness against adaptive behavior.
- CUM: cumulative sub-threshold capture trajectory.
- RF: joint resource-feasibility of promised floors.
- SEL: competitive survival of compliant/non-capture structures.
- INT: interpretation authority and evaluator disagreement.
- VOI: stopping rule for unknown-stakeholder search.

### Project-added integration and unresolved candidates

After integrating prior work and preserving its attribution, the strongest unvalidated Project-added combinations or unresolved candidates are:

1. fork/merge-aware role reversal where agent count is endogenous;
2. enforcement-latency versus power-drift thresholds;
3. cumulative capture across locally acceptable steps;
4. role reversal under large oversight/cognitive asymmetry;
5. competitive survivability of non-capture governance;
6. whether H/M/X classification avoids both irreversible harm and veto paralysis better than an expanding hard intersection.

See [MULTI_MODEL_ADVERSARIAL_AUDIT_2026-10-06.md](MULTI_MODEL_ADVERSARIAL_AUDIT_2026-10-06.md) and [experiments/e009/README.md](experiments/e009/README.md).
