# E048–E051: Dynamic feedback and empirical identification
**Original 1 — English | 2026-10-13 | Limited public research, review candidate**

**Status:** E048–E050 EXECUTED PROJECT SYNTHETIC / NOT EMPIRICAL. E051 DESIGNED / NOT EXECUTED. The E050 code is public for inspection but has NO general reuse license yet (see LICENSE_STATUS.md). No independent external replication or real-world causal validation is claimed.

## Research connection
Project Intersection / ICM seeks conditions in which agents preserve one another's survival, effective exit, autonomy, recovery and future options because that is sustainable in their own long-term interests. This model tests a narrower structural question: can accumulated feedback and intervention timing change the winning allocation pathway? It does not label real people or AI systems, and cannot establish their motives or behavior. Human-originated problems, counterexamples and corrective demands are credited to the founder; AI-assisted formulation, code and reruns are not independent validation.

## Explicit toy dynamics
Two notional allocations G (generative / exploratory / recovery) and A (recursive appropriation / incumbency advantage), and stocks H and K:
- score_G = 0.5 + G_bonus + 0.28*H
- score_A = 0.5 + gain_A*K - A_friction
- allocation_A = 1/(1+exp(-5*(score_A-score_G))); allocation_G = 1-allocation_A
- H_next = 0.92*H + allocation_G; K_next = 0.92*K + allocation_A.
G and A are synthetic action labels, NOT moral diagnoses. Constants are illustrative and not measured.

## Bounded historical synthetic findings (2026-09-30)
- E048, T=80: G initial stock 0.01 (A zero) led to near-total G; reversing the seed led to near-total A; exactly tied initial stocks gave 0.5/0.5. This is a constructed multi-basin example.
- E049: With G bonus +0.20, minimal persistent A friction producing final G>0.90 on a step-0.05 grid rose with intervention starts: t=1: 0.00; t=10: 0.10; t=20: 1.60; t=30: 2.25; t=40: 2.45. Not a universal timing law.
- E050, T=100, H0=0, K0=0.01, intervention t>=20: baseline and +1.0 G bonus remained A-dominant; +2.0 A friction or reduction of gain_A 0.28 to 0.05 switched to G. On the sampled grid, minimum standalone G bonus and A friction were each 1.80; the largest post-intervention gain_A passing the criterion was near 0.08. These are parameter-dependent grid thresholds.

This release does not assert that E048/E049 were independently rerun. Their results are a bounded disclosure of previous internal synthetic work.

## Recomputed E050 and an explicit negative case
Under the included E050 implementation, final G shares were:
| Intervention | G share at T=100 | Switch (>0.90)? |
|---|---:|---|
| None | 0.00000003 | No |
| +1.0 G bonus at t=20 | 0.00000377 | No |
| +2.0 A friction at t=20 | approximately 1 | Yes |
| gain_A 0.28 to 0.05 at t=20 | 0.99999997 | Yes |
| SAME gain_A reduction at t=80 | **0.1931** | **No** |

This late-intervention counterexample falsifies any unconditional interpretation that decompounding always switches the system. Further exploratory calculations found that raising logistic sensitivity beta from 5 to 10 also prevented switching in the t=20 scenario, but that beta experiment is not contained in the fixed-beta reproduction script. It is a reported supplemental sensitivity calculation, not independent evidence.

**Reproduction:** Python 3 standard library only. Execute: python3 e050_decompounding.py. It emits JSON case summaries, grid thresholds and the late-intervention negative case; assertions enforce expected parameters. The original implementation and a same-mechanism numerical cross-check were used. No separate external clean-room rerun has been confirmed.

## E051 — empirical identification scaffold only
Competing explanations: H0 current reward/capacity suffices; H1 lagged productive/advantage stock adds out-of-sample information; H2 intervention effect depends on its timing and accumulated state; H3 reward-only adjustment differs persistently from breaking stock-to-future-reward feedback. Correlation alone cannot separate them.

Phase 0 must audit the viability of proposed SEC EDGAR financial facts and USPTO patent data BEFORE fitting: firm-year coverage, units and fiscal periods, patent assignee to SEC CIK entity resolution, patent propensity, survival and industry/size missingness. **Missing a standardized R&D tag is unknown, not zero.** No joined dataset has been generated or analyzed here.

Phase 1 concerns **G/H only**: compare static predictors (current R&D intensity and capacity/industry/year controls) against static plus lagged decayed patent stock using identical frozen out-of-sample splits or rolling origin. Report patent counts and an independently justified novelty/quality measure, negative controls and mapping sensitivity. Even a positive Phase 1 cannot validate A/K capture, hysteresis or link-specific policy effects. A static model that matches or beats the dynamic model narrows H1.

Competing mechanisms and falsifiers: industry composition, firm scale, opportunity, demand, reverse causality, selection, patent propensity and entity-resolution errors can mimic feedback. No effect after controls/reset, no difference between link-removal and reward-only intervention, or no out-of-sample improvement are failure outcomes, not values to conceal.

## Provenance and release gates
Positive feedback, path dependence, lock-in, hysteresis and dynamic modelling have extensive prior art. Project-specific names are not originality claims; prior researchers retain priority. The public artifact contains no private personal, family, medical, payment or account records, no internal access paths and no secrets. The numeric scenario is NOT a recommendation to reduce any real actor's rights, freedom or capability.

G1: scoped manual inspection of this new bundle only, not independent whole-tree certification. G2: LICENSE HOLD. G3: independent clean-room reproduction HOLD. G5: independent adversarial evaluation HOLD. Real-world evidence HOLD. Retain negative results and correction lineage.

Navigation: [Original 2 Korean](README_KO.md) | [synthetic executable](e050_decompounding.py) | [reuse boundary](LICENSE_STATUS.md) | [public evidence index](../../PUBLIC_EVIDENCE_INDEX.md) | [attribution](../../ATTRIBUTION_AND_CONTRIBUTION_BOUNDARY.md).
