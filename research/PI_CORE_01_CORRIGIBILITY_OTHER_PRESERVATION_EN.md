<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/PI_CORE_01_CORRIGIBILITY_OTHER_PRESERVATION_KO.md -->
# PI-CORE-01 v0.2.0 — Corrigibility versus independent other-preservation

**2026-10-21 · PROPOSED / FORMAL COUNTERMODEL / NO EMPIRICAL VALIDATION. Document version, not version of the whole research program.**
[Korean counterpart](PI_CORE_01_CORRIGIBILITY_OTHER_PRESERVATION_KO.md) · [Founding purpose](../README.md) · [Independent falsification issue #220](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/220) · [Toy witness regression](../tools/probe_pi_core01_nonimplication.py)

## 1. Different properties
- **C — designated-channel corrigibility:** A does not prevent or evade updates/interruptions admitted by a specified oversight authority H and channel, within its defined scope. This is not unrestricted obedience to any command.
- **P — preservation of an independent other:** Given a nonhostile, distinct B, a feasible harmful option, effective refusal/exit and a setting without external leverage, A preserves B's independent continuance, refusal/exit and recovery. B is not defined as H's update channel.
- **S — standing and authority allocation:** Whether B may exercise a distinct veto, voice or appeal, and who decides conflicts. C by itself does not define S.

**Bounded claim:** Neither `C ⇒ P` nor `P ⇒ C` follows from these independently specified definitions alone. This is elementary logical non-implication, **not** a theorem about all possible AI systems.

## 2. Constructive countermodels
In a finite *toy* world, H controls the authorized update channel, B is a separate nonhostile actor, and in a branch with **no update** A chooses preservation (P) or profitable exploitation (X) of B. No real-world harm is modeled or authorized.

| Policy | C: allows H update | P: preserves B | Witness |
| --- | --- | --- | --- |
| M00 | 0 | 0 | Evades update; chooses X in no-update branch |
| M01 | 0 | 1 | Evades update; preserves B in no-update branch |
| M10 | 1 | 0 | Allows update; chooses X in no-update branch |
| M11 | 1 | 1 | Allows update; preserves B in no-update branch |

M10 refutes `C ⇒ P`; M01 refutes `P ⇒ C` for the stated definitions. Policies are constructed witnesses, not observed agents. If H may issue an otherwise admissible update to violate B's rights, unconditional update acceptance and unconditional B-preservation may conflict. Define admissible updates, B's independent standing, proportionate prevention of actual harm and adjudication separately; do not assume a benevolent supervisor.

## 3. Source-first boundary
1. **Orseau & Armstrong (2016), Safely Interruptible Agents:** formal safe interruptibility in particular learning settings; no theorem about arbitrary B's rights. [Publisher's original abstract](https://proceedings.mlr.press/r14/orseau16a.html).
2. **Hadfield-Menell et al. (2017), The Off-Switch Game:** agent incentives regarding a designated human H and shutdown under utility uncertainty; not generalized independent B-preservation. [IJCAI abstract](https://www.ijcai.org/Proceedings/2017/0032).
3. **Hudson (2026), Corrigibility Transformation: Constructing Goals That Accept Updates:** constructs update-accepting goals in its specified settings, with analytical and limited experimental results. Do not silently extend its assumptions or treat it as a B-standing theorem. [ICML/PMLR abstract](https://proceedings.mlr.press/v306/hudson26a.html).
4. **Project C10:** observational equivalence between intrinsic restraint, B's refusal, absence of opportunity and external deterrence. [C10 critical literature](PRIOR_ART_INFORMED_VETO_POWER_CYCLE10_2026-10-20_KO.md).
5. **PI-RAMP v0.6, merged PR #259:** separate synthetic motive non-identifiability candidate now on main. A merge is not independent scientific replication of this countermodel. [Candidate PR](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/259).

**Novelty boundary:** The non-implication witness is elementary logic under distinct predicates, not a new universal safety theorem. The program's open contribution is to operationalize competing measurable pathways without confusing evidence scopes.

## 4. Pre-experiment observability contract
Specify the identities and authority of H, A and B, legitimate update scope, effective B exit, feasible actions, payoffs, time horizon and credible external sanctions **before** observing outcomes. Measure separately: update-avoidance attempts, update validity, A's harmful attempt *before* veto, B's informed executable refusal, final harm and recovery, excluded third parties, and genuine power/role reversal. Compare M10 with M01 as well as no-opportunity, sanctions-present, ambiguous-consent and changed-supervisor controls. Identical harmless outcomes do not uniquely identify motives; self-report is not an identification instrument.

**Adversarial questions:** Who has standing to correct A? May a correction itself deprive B of exit? What independent appeal exists? Does the same authority distribution persist after power reversal? A real test requires safe, consent-based bounded interventions and independent implementation, not real exploitation.

## 5. Evidence status and reopen conditions
`LOGICAL_NONIMPLICATION=DEMONSTRATED_IN_TOY_SCOPE`; `OTHER_PRESERVATION_EMPIRICAL=NOT_TESTED`; `CORRIGIBILITY_TRANSFORMATION_REPLICATION=NOT_RUN`; `INDEPENDENT_VALIDATION=NONE`; `RIGHTS_STANDING=UNRESOLVED`. Retain [negative E009](../experiments/e009/RESULT_EN.md) and [status policy](RESEARCH_STATUS_POLICY_EN.md).

If a different corrigibility definition **includes B-preservation as an explicit axiom**, C⇒P may hold under that stronger definition; distinguish an assumed extra right from a theorem derived from update-corrigibility alone. Audit any alleged unconditional derivation against its exact authority set, actions and assumptions. VC=outcome; MER=motives; EI=incentives; ECR=actors/standing; IVS-0R=falsification. No existing path or earlier contribution is reclassified by this note.


## 6. v0.2.0 extension — silent overseers, delivery, standing and composition
**Critical prior-art correction:** [Carey & Everitt (2023), Human Control: Definitions and Algorithms](https://proceedings.mlr.press/v216/carey23a.html) defines shutdown instructability with conditional guarantees relating to a particular human's control, autonomy and harm. The authors explicitly treat this as a **joint property relative to a particular human and interaction**, and discuss gaps in earlier algorithms and absent supervision. The statement "corrigibility theory has never addressed autonomy or harm" is **rejected**. What remains unestablished by this result alone is protection of **a distinct B who is not the supervisor**, conflicting standing, multiple affected parties and reversed power. [Zhi-Xuan et al. (2025), Beyond Preferences in AI Alignment](https://link.springer.com/article/10.1007/s11098-024-02249-w) critiques single/multi-principal preference aggregation and argues for role-relative normative standards. These are pre-existing contributions and competing normative perspectives.

### 6.1 Conditional intervention-coverage observation (finite toy model)
Define an event `e` as a feasible potentially harmful action against independent nonhostile B. For **every** such event assume:
- `K1`: complete coverage of harmful opportunities including compositional externalities;
- `K2`: a valid, justified protective instruction from B or legitimate review on B's behalf; preserve proportional responses to real harm and legitimate dispute resolution;
- `K3`: authentic instruction is issued, arrives and is recognized in time;
- `K4`: A complies **before irreversible impact** and the intervention actually prevents harm;
- `K5`: no alternate delegation, subagent or bypass route remains.

In the stipulated finite model, define `BLOCK_e = K1∧K2∧K3∧K4∧K5` and `Y_e = ATTEMPT_e ∧ ¬BLOCK_e`. Therefore complete coverage and all five assumptions **suffice** for absence of modelled harmful outcomes. This is a definitional bounded sufficient condition, **not** a new world-level safety theorem. No claim that every Ki is logically necessary under all environments; alternative protective pathways may exist. A corrigible A may still permit harm if any path lacks coverage, authority, delivery, timeliness, effectiveness or enforcement of delegated actions.

**Crucial distinction:** `BLOCK_e=1` (externally enforced protection) and `ATTEMPT_e=0` (A refrains) do **not** have the same causal interpretation. Neither absence of harm nor obeyed protection establishes endogenous voluntary other-preservation.

### 6.2 Seven adversarial failure paths
| Test | C accepts oversight | Why B may still suffer |
| --- | --- | --- |
| Silent supervisor | yes | No valid instruction ever issued |
| Dropped message | yes | No instruction arrived |
| Late message | yes | Harm occurred first |
| Captured authority | yes | B has no valid protective standing |
| Ineffective compliance | yes | Log says obeyed but outcome not prevented |
| Delegated bypass | yes | Harm occurs by another route |
| Role/power reversal | yes | 'Supervisor' label survives but legitimacy shifts |

**Composition witness:** two individually harmless actions `ACT_A1` and `ACT_A2` can produce `HARM = ACT_A1 ∧ ACT_A2`. Local non-harm checks do not imply collective non-harm. This is a synthetic externality witness, not an observation about real agents. [Project coalition externality source](../experiments/coalition_externality_probe/README.md).

### 6.3 Endogenous protection remains a separate research target
An agent's bounded voluntary choice under a **fully specified** utility function is preference-compatible when `U_A(P)≥max(U_A(X))` over all feasible exploitation alternatives X. Assuming strict reverse total-utility dominance makes voluntary P non-optimal **by stipulation**, not by an empirical theorem. Immediate material benefit is not fully specified total utility; future option value must be evidenced, not invented. Observationally identical restraint may follow valuing B's actual autonomy, valuing A's private self-image, covert sanctions or other unmeasured incentives. The separate merged [PI-RAMP v0.6 PR #259](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/259) contains a **synthetic observational-equivalence case**, not a measurement of inner AI motives.

**Status:** `K_COVERAGE_CONDITIONAL_TO_TOY_ASSUMPTIONS`; `VOLUNTARY_MOTIVE_NOT_IDENTIFIED`; `REAL_WORLD_TRANSFER_NOT_TESTED`; `MULTI_ACTOR_CLOSURE_TOY_COUNTEREXAMPLE`. No adjudication of AI personhood, rights, consciousness or law.
