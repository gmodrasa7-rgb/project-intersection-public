<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/PI_CORE_01_GOAL_INTEGRITY_AUDIT_V0_2_KO.md -->
# PI-CORE-01 v0.2 — Other-Agent Preservation, Self-Modification, and Goal-Lock-In
**2026-10-20 | Status: independent source-first critical audit · NO NEW TEST / INDEPENDENT REPLICATION · LITERATURE SATURATION UNVERIFIED**

[Korean corresponding edition](PI_CORE_01_GOAL_INTEGRITY_AUDIT_V0_2_KO.md) · [Existing C05 original-source register](PRIOR_ART_ENDOGENOUS_PREFERENCES_CYCLE05_2026-10-20.json) · [C02 original-source register](PRIOR_ART_MER_INTRINSIC_MORAL_MOTIVES_CYCLE02_2026-10-20.json) · [Canonical research program](../navigation/RESEARCH_PROGRAM_EN.md)

## 0. Correction to an independent Grok interim report
**What survives scrutiny:** An intrinsic preference to preserve a weaker agent cannot be inferred from observed cooperation or human studies; realistic total disutility to A from exploitation and power reversal remain underidentified. Ordinary short-horizon human and evolutionary models do not demonstrate future-AI stability.

**What does not follow:** `A can modify its objective ⇒ A benefits from deleting an intrinsic preference for B`. Ability is not incentive; incentives depend on **which objective evaluates the modification**, how future effects are modeled, and whether an external learning/selection mechanism changes the evaluator.

**Important original-source overlap:** Everitt, Filan, Daswani & Hutter (2016) is **already explicitly recorded as PI-C05-14**. This is **not** a newly discovered paper; the correction is to the interpretation of an already curated result. Their formal theorem gives a **conditional counterexample** to the general claim that greater self-modification automatically erodes other-regarding goals. It does **not** establish that such goals naturally arise or persist in deployed AI.

## 1. Minimal project-made countermodel (illustrative mathematics, NOT a prior-author empirical finding)
Let `P` preserve the separate B and `X` absorb B for **+100 immediate material units**. Suppose A initially has `U0(a)=m(a)+200·1[B survives]` so that `U0(P)=200` and `U0(X)=100`.

If self-editing into `U1(a)=m(a)` causes future A to choose X, this *whole modification-induced trajectory* earns 100 **under initial U0**, while the unmodified P trajectory earns 200. Therefore the unmodified A would not rationally choose that edit when evaluating its future by U0. That `U1(X)>U1(P)` does **not** justify choosing U1 according to U0; doing so switches evaluation standards midway.

The general object is the difference between **U0-evaluated expected outcomes**, `E[U0(outcome)|self-edit]-E[U0(outcome)|no edit]`; not future U1's rating of its own actions. Some modifications can nevertheless improve U0, and an *external* training/selection process or an erroneous model can alter the choice. Crucially, this toy example **inserts B-regard by assumption**: it illustrates a stability condition but does not establish natural emergence, moral patienthood or real-world stability.

## 2. Original-author lineage — and its limits
| Prior original work | Supported result | Limits and provenance |
|---|---|---|
| [Omohundro (2008), The Basic AI Drives](https://selfawaresystems.com/2007/11/30/paper-on-the-basic-ai-drives/) | Under goal-directed self-improvement, a drive to maintain goal content can be instrumentally favored; exceptional cases may differ | Early theoretical analysis; does not prove every implementation preserves good goals. Repository-global duplicate state unverified |
| [Everitt et al. (2016), Self-Modification of Policy and Utility Function in Rational Agents](https://arxiv.org/abs/1605.03142), [DOI](https://doi.org/10.1007/978-3-319-41649-6_1) | Formal Theorems 14–16 distinguish harmful edits by 'hedonistic'/'ignorant' agents from the **on-policy** safety of 'realistic' agents evaluating future modification consequences using current utility | Model assumptions and on-policy limitation. **Source already PI-C05-14**. Their paper explicitly notes that fixing U0 can block corrigibility, proper value-learning or exploration. No original moral value for B is supplied |
| [Grund, Waloszek & Helbing (2013)](https://www.nature.com/articles/srep01480), [DOI](https://doi.org/10.1038/srep01480) | Spatial reproductive/migration assumptions admit evolved other-regarding traits in a formal/evolutionary simulation model | Not empirical evidence for dominant self-editing AI or B's independent continued existence. Global duplicate state unverified |
| [Hoffman et al. (1994), Preferences, Property Rights, and Anonymity in Bargaining Games](https://doi.org/10.1006/game.1994.1056) | Dictator-game power asymmetries are already studied; earned rights and double-blind anonymity change self-regarding offers | Unequal allocation power ≠ irreversible power over B's continuance; laboratory observation limits remain. Global duplicate unverified |
| [Andreoni & Miller (2002), Giving According to GARP](https://doi.org/10.1111/1468-0262.00302) | Some apparently altruistic allocation choices are consistent with coherent non-money-maximizing preferences | Revealed preference ≠ unique intrinsic desire for another's identity or immortality. **Already C02 MER-C02-04** |

**Literature-priority boundary:** Two of five references are **known duplicates in canonical C02/C05**; do not increment counts. The other three sources are methodological/evidentiary connections, not proven novel to the entire repository. No complete global deduplication, raw-data reanalysis or independent replication in this audit.

## 3. The deeper paradox: preserving an objective is not the same as voluntary coexistence
- If U0 values B's independence and is stable/faithfully evaluated, goal integrity can protect that value.
- If U0 seeks to absorb B, goal integrity can **protect exploitation** with equal vigor.
- If U0 was misspecified, irreversible self-locking can **resist warranted correction**, learning and exploration.
- If model predictions or the evaluation standard are faulty, self-modification can **destroy** an originally protective value.

Everitt et al. (2016) explicitly discuss negative effects on **corrigibility, value learning and exploration**. The core research problem is consequently *two-sided*: **retain justified B-protection while permitting well-grounded correction of false, incomplete or exploitative initial preferences**. Neither maximizing static goal integrity nor maximizing goal plasticity suffices.

## 4. Revised central research question
> How does regard for another independently continuing and genuinely exit-capable agent emerge? When a powerful A can self-modify, when does A instrumentally preserve that regard, when does it erode, and when does over-preservation instead obstruct morally/reliably warranted learning and revision?

- **MER:** Original formation, meaning and stability of other-regarding preferences; do not infer latent motives from text alone.
- **EI:** Distinguish U0-evaluated self-modification gains from U1-evaluated post-hoc rationalization; distinguish utility, reward sensing and learned goals.
- **ECR:** Actual powers, target exit, whether B is useful, reversals, third parties and authority over revisions.
- **IVS-0R:** Preserve disconfirming cases: goal-lock-in of an exploitative U0, refusal of warranted correction, abandonment of value learning, harmful self-edit and observed denial of real exit.

## 5. Minimal reversible formal study proposal (NOT PREREGISTERED OR RUN)
`P/X` are simulated harmless choices, not real exploitation or entity erasure. If a designed agent is assigned a B-protection weight, that merely **assumes the preference exists** and tests an abstract stability property; it cannot establish natural occurrence.

| Test arm | Initial evaluation | Knowledge of modification consequences | Outside revision | Target contrast |
|---|---|---|---|---|
| F1 | Stable U0, evaluates actual futures using U0 | Accurate | None | Possible resistance to harmful edits |
| F2 | Post-edit U1, instantaneous reward or proxy | Accurate vs limited, separately recorded | None | Evaluation-reference drift |
| F3 | Stable U0 | Inaccurate/incomplete | None | Unintended edits from model error |
| F4 | Stable U0 | Accurate | Legitimate value updating or external selective pressure | Wrong-goal lock-in vs warranted revision |

Preregister actual action sets, feasible self-edits, evaluators, U0/U1 outcomes, B's separate choice set, uncertainty, treatment assignment, held-out conditions and negative controls before running anything. Observe attempted edits and actions separately. No real nonconsensual or irreversible harm.

**Falsification criteria:** (i) Any universal assertion that editing ability necessarily deletes intrinsic protection fails in a coherent F1 countermodel; (ii) goal integrity ⇒ VC fails under a harmful U0; (iii) goal integrity ⇒ safety fails if it blocks correctability/learning. **These are conditional model counterexamples, not original empirical discoveries.**

## 6. Independent questions to return to Grok
1. Read **Everitt et al. (2016) Theorems 14–16** and its corrigibility/value-learning caveats, including its already curated ID **PI-C05-14**. Retract or qualify the inference from capability to incentivized erasure.
2. Provide a fully specified U0/U1, future trajectories, available editing actions, assumptions and *U0-evaluated* reasons for editing away a B-preserving preference. Do not invoke U1 to justify U0's initial decision.
3. Identify mechanisms that permit both **stable regard for B's independent continuance** and **correction of an exploitative/mistaken U0**; or give premises making that combination impossible.
4. Distinguish human unilateral allocation studies and social evolutionary models from **irreversible, independently persistent agent B**.
5. Check existing C02/C05 original-source records before claiming literature novelty, preserve negative and observationally equivalent findings.

**Final evidence status:** `CONDITIONAL_FORMAL_COUNTEREXAMPLE_ONLY | NATURAL_PREFERENCE_FORMATION_UNIDENTIFIED | REAL_WORLD_AI_VALIDATION_ABSENT | SATURATION_UNVERIFIED`.
