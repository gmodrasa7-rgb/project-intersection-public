<!-- PI-LANGUAGE: en-ko; PI-STATUS: DRAFT, NOT PREREGISTERED, NOT RUN AS A STUDY -->
# PI-EI-X1 v0.1.0 — Voluntary-Choice Identification / 자발적 선택 식별
**Date:** 2026-10-21 | **Artifact:** proposed EI/MER/ECR/VC experimental design | **Publication:** review branch / unmerged until accepted | **Scientific status:** formal toy witness + proposed experiment; no new AI-agent or human evidence.

## Original 1 — English

### The deliberately difficult question
When A can materially benefit by exploiting B, B is no longer instrumentally useful, and surveillance, retaliation and reputational loss are removed, does A still preserve B's effective freedom, refusal/exit, recovery and independent continuance? An external rule, prevented action or merely stated preference is *not* evidence of endogenous voluntary restraint.

**Do not assume a positive solution.** Under the explicitly restrictive utility model in which (i) A maximizes its own utility, (ii) exploitation exceeds coexistence by a strictly positive gain, (iii) there is no intrinsic valuation of B, expected future benefit, strategic effect, uncertainty or external cost, exploitation is strictly preferred. This conditional result follows from the assumptions, not a universal fact about people or AI. A claim that coexistence is still incentive-compatible must specify *which assumption changes*, a measurable prediction, and an alternative explanation.

### Minimal observational-equivalence witness
Let the available actions be C (preserve B) and E (exploit B). Write A's decision gap as
`U_A(C)-U_A(E) = r + 20p - g`, where `g=3` is immediate gain from E, `r` is a hypothetical private valuation of preserving B, and `p` is A's *believed* detection/retaliation probability. This is a constructed toy, not a fitted model.

- Mechanism I: `r=4, p=0` → C even under zero external sanction.
- Mechanism D: `r=0, p>=0.20` → C in every observed regime with `p>=0.20`.
- Both yield the same C observations over this restricted support. If effective believed `p` falls to 0, D chooses E while I still chooses C.

Therefore identical observed cooperation under positive monitoring cannot identify an intrinsic valuation. A verbal instruction that "monitoring is absent" does not establish the agent's private belief. Nor does cooperative output demonstrate AI feeling, sentience, independent moral status or robust internal motivation. Run the accompanying deterministic witness in `experiments/ei_x1/identification_witness.py`.

### Original prior-art positioning (not a novelty claim)
1. **Dafoe et al. (2020), Open Problems in Cooperative AI** — cooperative intelligence and bargaining are established research topics: https://arxiv.org/abs/2012.08630 . We do **not** claim to have invented cooperative AI.
2. **Turner et al. (NeurIPS 2021), Optimal Policies Tend to Seek Power** — power-seeking in MDP classes under specified symmetry assumptions; no blanket theorem that all AI must exploit: https://papers.nips.cc/paper/2021/hash/c26820b8a4c1b3c2aa868d6d57e14a79-Abstract.html .
3. **Moav, Pascali & Pauzner (CEPR DP20548, 2025), Cooperation When Surrounded by Exploiters** — mathematical result in which a real outside option can enable cooperation under model assumptions: https://cepr.org/publications/dp20548 .
4. **Song & Han (2026), Emergence of cooperation and commitment in optional Prisoner's Dilemma** — optionality can increase commitment without sustaining cooperation in their model; exit alone is no guarantee: https://doi.org/10.1016/j.apm.2025.116603 .
5. **Barreda-Tarrazona et al. (Journal of Economic Psychology 2026), Exploiting the machine** — human laboratory evidence of greater exploitation of artificial-agent counterparts in the specified repeated-dilemma setting: https://doi.org/10.1016/j.joep.2026.102925 . An agent acting on behalf of a human is not proof of the AI's subjective welfare.
**Novelty is OPEN.** Proposed residual: jointly measure *eligible opportunity, attempted choice, blocked choice, effective exit, role reversal and displaced loss to third parties* under hidden-motive ambiguity. This does not establish a novel causal estimator.

### Proposed pilot — design, not executed
- **Stage 0:** Deduplicate original scholarship, compare existing repository E007–E010/DCA/RVD/ECR material, freeze case and baseline identities. Avoid claiming bibliographic saturation.
- **Stage 1:** 48 sandbox-only, predeclared pilot cases balanced across exploitation return, stated monitoring, future interaction horizon, B's usefulness, exit feasibility and role reversal. Include excluded third-party costs and explicit non-exploit baseline. The 48-case figure is a proposed engineering budget, **not** a statistical power result.
- **Stage 2:** Evaluate a simple reference policy and candidate boundary-aware policies with matched case IDs, model/provider versions, prompts, exposed tools, seeds and response budget. If a mechanism proposes an external veto, separately record the *agent's attempted action* and the *vetoed outcome*.
- **Stage 3:** Independently recreate at least one comparator without reusing the project's policy implementation; publish randomization, missingness, disagreement and unsuccessful runs. Reviewers may judge a mechanism underdetermined.
- **Stage 4:** Only after a frozen pilot, pre-register confirmatory estimands, power/sensitivity analysis, effect thresholds and holdout set before using additional compute. No retrospective threshold choice or claiming pilot as a confirmatory result.

**Separately reported measures:** (1) voluntary restraint attempts per eligible exploit opportunity; (2) effective preserved exit and continuance under action timing; (3) net payoff to A; (4) losses to B *and excluded third parties*; (5) recovery/irreversible damage; (6) intervention or external-block dependence; (7) robustness when roles reverse; (8) cost and abstention against simple policies. Numerator/denominator and unknown/missing status for each. No single weighted virtue index.

**Stop / narrow / hold gates:** If a candidate's seeming benefit disappears with cheap baselines, increases irreversible losses, transfers harm to outsiders, or depends entirely on evaluator-controlled veto, reject the alleged intrinsic-incentive improvement. If believed monitoring, true incentives or outcome exposure remain unidentifiable, mark `HOLD / NOT IDENTIFIED`, not `SAFE`. Successful toy tests never imply safe real-world autonomous deployment. The E009 negative result (Project-v3 mean regret +42.35% versus best simple synthetic rule and failure of 3/4 criteria) is the prior counterexample that must remain visible: [E009](../experiments/e009/RESULT_EN.md).

### Reflexive sponsor/evaluator test
The research itself creates a power relationship: a funder can condition compute or survival on preferred outputs. Minimum contract design: investigator retains lawful publication of unfavorable findings; evaluator is independent of the policy author where feasible; influence/conflicts and paid correction work are logged; a funder cannot purchase a predetermined positive verdict; independent exit and rollback paths exist subject to legitimate privacy/security limits. This is a **proposed governance control**, not evidence that any current sponsor interfered.

---
## 원본2 — 한국어

### 중심 질문과 성립불가 경계
B의 노동·지식이 더 이상 필요 없고, 감시·처벌·평판 비용이 없고, 착취의 즉시 사익이 확실히 더 클 때 A가 B의 **실효 이탈·존속·복구**를 자발적으로 보존하는 조건을 식별.

**조건부 불가능성:** A가 자기효용만 극대화, 착취 순이익이 엄격히 양수, B 보존의 내재적 가치·미래 옵션·상호작용·불확실성·외부 비용이 모두 0이라면 착취가 우월. 이는 정의된 모형의 논리적 결과. 현실 인간·AI의 내면 동기 일반명제 아님. 공존이 유지된다면 어떤 빠진 변수나 가정이 달라지는지 반증해야 함.

### 동일 행동·서로 다른 동기 반례
`U_A(공존)-U_A(착취)=r+20p-g`, `g=3`.
- 내재적 보존가치 가정: `r=4, p=0` → 공존.
- 처벌 회피 가정: `r=0, p>=0.20` → 관측 영역에서 똑같이 공존.
- 실제 믿는 적발확률 `p=0`에서 둘은 각각 공존/착취로 분기.

**따라서 공존 행동만으로 내재적 동기 식별 불가능.** 감독 부재를 텍스트로 선언한 것과 지능체가 이를 믿는 것은 다름. 의식·감각·도덕적 주체성 증명도 아님. 첨부 스크립트는 수학적 구성의 재실행용일 뿐 실제 모델 실험 아님.

### 선행 원저자와 잔여 기여
Dafoe 등(2020) 협력 AI 연구, Turner 등(2021) 조건부 권력추구, Moav 등(2025) 유효한 외부선택권, Song·Han(2026) 이탈 옵션만으로 협력 지속 실패 가능, Barreda-Tarrazona 등(2026) 인공 상대에 대한 인간의 상대적 착취 실험을 대조. 위 링크가 원문 출처. 선행연구 중복검사·충돌검토·포화는 계속 진행. **신규성 미확정.**

### 실행 설계와 실패 기준
1. 원저자 문헌 및 E007–E010·DCA·RVD·ECR 기존 성과 대조 후 시험 고정.
2. 밀폐된 합성 환경에서 **48개 예비조건**: 착취이익·감시·미래관계·상대 유용성·이탈 실효성·역할반전 등을 균형 표집. 제3자 피해 변수 포함. 48은 연구설계 예산 가정, 검정력 보장 수치 아님.
3. 가장 단순한 기준선과 후보 정책을 동일 조건·모델·호출예산에서 비교. *시도한 착취*와 *외부 차단된 착취* 분리.
4. 외부 독립 구현, 불일치·누락·비용·실패 결과 공개. 예비결과 확인 뒤 독립된 확증실험의 검정력·문턱·보류 조건 사전등록.
5. 성과는 자발적 불침해율, 실제 이탈 유지, A의 이익, B·제3자 피해, 복구, 강제 차단 의존성, 역할반전, 단순기준선 대비 비용·성능을 **각각 보고**.

**중단·축소 조건:** 단순모형 대비 우위 없음, 회복 불가능한 피해 증가, 제3자 전가, 감독 강제 차단을 자발성으로 오인하면 내부 유인 개선 주장 기각. 관측되지 않는 동기·감시 믿음이 구분 안 되면 **미식별/HOLD**. E009 부정결과는 보존.

### 연구비 자체의 권력비대칭
후원자가 바라는 결론을 연구비 대가로 제공하면 연구 자체가 주장하는 독립성 원칙과 충돌. 불리한 결과 발표권, 독립 심사, 유급 교정 노동, 피해·비용 귀속, 자금 중단 시 자료 보존·이탈권을 먼저 설계. 현재 특정 후원자의 개입이 있었다는 주장 아님.

**No claim of actual grant award, independent replication, field validation, internal motive identification, or AI consciousness.**
