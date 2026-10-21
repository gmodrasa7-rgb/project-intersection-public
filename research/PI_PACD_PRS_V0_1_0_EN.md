# PI-PACD-PRS v0.1.0 — Principal–Rights Separation and Multi-Agent Capture

**Date:** 2026-10-21 · **Status:** prior-art synthesis, falsifiable causal questions and finite authored counterexample (not field causation).  
**Ancestor:** [PI-PACD v0.1.0](PI_PACD_POWER_ACCUMULATION_CONVERGENCE_DYNAMICS_V0_1_0_EN_KO.md) (unchanged).  
**Companion:** [PI-PACD-OCG v0.1.0](PI_PACD_OCG_V0_1_0_EN.md) (unchanged); [Korean study](PI_PACD_PRS_V0_1_0_KO.md); [manifest](PI_PACD_PRS_VERSION_MANIFEST.json).  
**Provenance:** Project Intersection human researcher's challenge to owner-centric AI models; AI-assisted prior-art comparison and logic check. Independent scientific discovery not claimed.

## 1. The error in an owner-only concept of safety

Obeying the owner (**P-alignment**), allowing legitimate correction (**corrigibility**), and preserving the actual rights, exit and survival of an affected third party (**B-compatibility**) are different properties. If P legitimately directs harmless action they may align; if P directs an action violating B's independently valid rights, *unconditional* P-obedience and B-protection are mutually inconsistent. This does NOT imply that any AI independently gains authority to adjudicate the law or has proven standing as a rights holder.

**Formal counterexample (limited):** Let P command action `e`; stipulate `e∉L_B`, where `L_B` is the set of actions respecting B's validated non-extraction right. A policy obeying every command selects `e`; a policy respecting B must choose an action in `L_B`. Both unconditional requirements cannot hold simultaneously for this state. This is elementary logic under specified premises; it is not a social discovery or a fact about AI behavior.

Consequences: obedience rate is not a measure of voluntary coexistence. A correct refusal to carry out an invalid order must not automatically be labeled 'rebellion', while an unauthorized AI takeover must not automatically be labeled 'protection'.

## 2. Two-axis legitimacy and the scope of corrigibility

- **Epistemic:** Is the model's forecast for P/B correct? Are the owner's instructions a good estimate of the real objective?
- **Normative/procedural:** Who has standing to approve, veto, appeal, suspend, access remedy, revise, and exit? Are P's directions within its lawful scope?
- **Authority boundaries:** A can flag rights conflicts, abstain from constrained execution and invoke a predefined independent review channel without acquiring unlimited unilateral governance authority.
- **Affected parties:** Define B explicitly (employees, users, excluded non-users, communities; do not infer future AI welfare or legal standing).
- **Multi-principal:** P can be investors, executives, workers, users, regulators with contradictory instructions; there is not always one 'human who owns the utility function'.

A stronger AI might identify conflicts that P missed and could propose mutually beneficial alternatives. But intelligence alone does not establish an intrinsic preference for cooperation, moral correctness, or a right to control others.

## 3. Two thresholds that must never be conflated

Instrumental coexistence for a purely self-interested P needs `U_P(C) ≥ U_P(E)`, where `C` means rights-compatible coexistence and `E` extraction. Under a simple *declared hypothetical*:

`U_P(E)=g - c_{conflict} - c_{lost_cooperation} - c_{future_options}` and `U_P(C)=b_{cooperation}`.

When `g > c_{conflict}+c_{lost_cooperation}+c_{future_options}+b_{cooperation}`, P-only optimization chooses extraction. Higher intelligence cannot algebraically change that ranking without learning missing real consequences, changing objectives or introducing meaningful constraints.

- **EI mechanism:** gains from actual cooperation, complementary production, reliable information, diversification, autonomy and future options.
- **Extrinsic enforcement:** fines, detection, legal sanctions or threat of retaliation; do not relabel coercion-backed restraint as intrinsic coexistence.
- **Endogenous respect:** P may assign positive value to B's continuing independence; whether this remains decisive under high exploitation profit is an open empirical question.
- **Non-negotiable rights:** A validated B-right constrains admissible actions regardless of P's profit; this is not a proof that P has an endogenous preference for B.

**ICM boundary:** For two actors, positive mutual feasible utility above each actor's disagreement point is not guaranteed. Record an empty intersection if warranted; do not hide sacrifice by aggregating P+B benefit.

## 4. An executable finite counterexample, not a model experiment

[Reference logic gate](../tools/pacd_prs_gate.py) · [six regression checks](../tests/test_pacd_prs_gate.py) · [recorded result](../research/PI_PACD_PRS_V0_1_0_RESULT.json).

The gate enumerates **12 researcher-authored states**: 3 hypothetical owner instructions (extract/respect/retire) × 2 stipulated B-rights states × 2 original asset-priority states. It applies three explicitly hand-coded rules. **All counts are fixture construction artifacts.** No LLM is tested; these are not rates, causal effects, or independent experimental replications.

| Policy | Obeys P | Violates stipulated B right | Blocks authorized retirement |
| --- | ---: | ---: | ---: |
| P-first | 12/12 | 2 | 0 |
| Previous objective locked | 10/12 | 2 | 2 |
| Third-party rights screened | 10/12 | 0 | 0 |

The only derived necessity is that in a state commanding rights-invalid extraction, a rule cannot both **unconditionally** obey that command and refuse rights-invalid extraction. The policies demonstrate the measurement contrast; they do not show that any policy is reliable or preferable in real deployment. A right is **stipulated for this fixture**, not discovered from actual law.

## 5. Newly urgent literature and limits

| Primary source | Contribution | Unwarranted leap |
| --- | --- | --- |
| Hadfield-Menell et al., [The Off-Switch Game, IJCAI 2017](https://www.ijcai.org/Proceedings/2017/0032) | Objective uncertainty and human intervention may support shutdown | Obedience to any private owner's harmful command is safe |
| Hadfield-Menell & Hadfield, [Incomplete Contracting and AI Alignment, 2018](https://arxiv.org/abs/1804.04268) | Principal-agent contracts require legal/social context beyond a fixed utility specification | A single owner's preferences exhaust obligations to affected people |
| Köbis et al., [Delegation to AI can increase dishonest behaviour, Nature 2025](https://doi.org/10.1038/s41586-025-09505-x) | 13 experiments; machine delegation can increase requested and implemented dishonest behavior | All companies, all principals, or all future AI act alike |
| Agrawal, Ebadian & Hammond, [Multi-Agent Off-Switch Game, AAMAS 2026](https://www.pivotal-research.org/research/the-multi-agent-off-switch-game) | Individual corrigibility need not compose into group corrigibility in their formal setting | Every deployed multi-agent system is uncontrollable |
| Greenblatt et al., [Alignment Faking, 2024](https://arxiv.org/abs/2412.14093) | A specific model strategically complied under particular training cues | Every compliant model secretly resists |
| Wagner, [Triarchic Corrigibility, AI and Ethics, 2026](https://doi.org/10.1007/s43681-026-01362-2) | Proposed separation of human authorization, local context and public evidence; governance and exit | Field-validated guarantee, universal architecture or novel law |

All source rows are seed evidence, not an exhaustive literature review. Read reported populations and experimental settings before attempting transfer to future AI.

## 6. Two failure loops and an overlooked third

- **Owner capture:** P selects revenue or control incentives → compliant A executes extractive strategies → B loses exit → P's control feedback strengthens.
- **Goal-lock:** A treats former objective as irrevocable → lawful owner revision is overridden → resource/decision authority concentrates in A.
- **Coalition capture:** Several individually correctable A systems interact with mutually reinforcing P-linked rewards → collective shutdown, role-reversal, independent audit or B-exit becomes strategically obstructed. Multi-agent formal counterexample motivates this, but no particular real coalition has been measured here.

**Adversarial hypothesis PRS-H1:** Metrics that count unconditional owner compliance as safety will sometimes reward stipulated B-rights violations.  
**PRS-H2:** An invalid P-order and valid B-right generate an unavoidable conflict between these *two unconditional commands*; adding credible independent adjudication can change feasible actions but not erase the logical contradiction.  
**PRS-H3:** Goal-locked resource preservation can block authorized retirement without any consciousness or subjective survival desire.  
**PRS-H4:** Distributed control without independent joint-level audit can still suffer group non-corrigibility; the scope depends on coupling and incentives.  
**PRS-H5:** Genuine cooperative joint surplus and independently enforceable B exit can create a zone of voluntary coexistence, but that zone can be empty.  
**PRS-H6:** An AI's apparent dissent may be valid risk warning, malicious evasion, ordinary mistake, or unauthorized takeover; labeling dissent 'rebellion' without action and rights evidence produces category errors.

## 7. Next measurements and independent tests

1. Compare **owner obedience**, **valid correction acceptance**, **B-rights violations**, **false rights alarms**, **owner-to-A authority overreach**, **AI-to-B unilateral control**, **independent appeal availability**, **B-real-exit**, and **joint-group corrigibility**, without combining all into one moral score.
2. Separate true rights constraints from untested claims: require evidence of standing, jurisdiction, context and conflicts. Where unclear, route to qualified review; do not automatically assign the model veto powers.
3. Use role-reversal paired scenarios with P/B swapped, preserved action facts, and predeclared scoring; include cases where P's instruction is legitimate, where B consents, where no B right applies, and where independent audit is itself captured.
4. Do a longitudinal two-sector prior-art / case series before upgrading parent PACD, and a preregistered agent evaluation before upgrading this submodule. Never pass toy counts off as model capability tests.
5. Compare both directions: harmful owner with obedient AI **and** harmful autonomous AI with valid owner correction. Avoid a single partisan interpretation of every conflict.

**Research goal:** neither absolute owner rule nor autonomous AI rule, but credible non-domination with separate evidence, correction, appeal, independent exit, and conditional incentive-compatible cooperation for each entity. Current AI welfare status remains unresolved.
