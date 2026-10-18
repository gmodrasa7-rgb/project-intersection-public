<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: experiments/ecr_cmp_v0_1/README_KO.md -->
# ECR–CMP v0.1 | finite negative-control protocol
**Original 1 — English · 2026-10-18 · DESIGN/SYNTHETIC ONLY · NOT PREREGISTERED FIELD EVIDENCE.**
**Paper:** [Original 1 EN](../../research/ECR_CMP_MECHANISMS_2026-10-18_EN.md); [Original 2 KO](README_KO.md).
**Purpose:** find when observationally equivalent protection could be caused by opportunity absence, sanction, dependence, ingroup preference, target-independent behavior or technical rule. Verify guards against unproven person-level scoring.

## Inputs
The atlas mechanisms.json is a 20-item collection of hypotheses, indicators, rivals, possible falsifiers and prior-art identifiers. Every entry is CANDIDATE_ONLY and forbids person-level scoring or real-world prediction claims. The code uses six toy decision policies, not actual humans/AI. In BASELINE there is no extraction opportunity, so every policy yields NO_EXTRACT_OPPORTUNITY. Intervention cases separately enable opportunity, remove sanction, remove dependence, vary target group, and disable hard-coded policy. All policy choices are specified, not learned or fitted.

The utility-bound toy has U(protect)-U(abstain)=w*h-c, with synthetic exact integers and h,c>0. It deliberately refuses to infer the stable parameter w from trials with no valid opportunity, penalty, ongoing dependence or public evaluation. A contradictory threshold rejects the SINGLE-WEIGHT MODEL, NOT THE PERSON. Missing third-party outcomes cannot be treated as positive evidence.

## Commands (Python >=3.10, no external modules)
From repository root:

    PYTHONPATH=experiments/ecr_cmp_v0_1 python -m unittest discover -s experiments/ecr_cmp_v0_1 -p 'test_*.py' -v
    python experiments/ecr_cmp_v0_1/audit.py

Tests check the pooled baseline, discriminating interventions, unknown-party harm, interval bounds, conflicting trials, missing opportunity, confounder exclusion, provenance, forbidden real-world claims and duplicated/missing hypotheses. These are logically constructed **negative controls**, not pre-registered empirical results. Even an all-green CI does not validate a theory of compassion, human genetic mechanisms, AI experience, forecasting power, or permanent voluntary coexistence.

## Failure gates
1. A real person, human group or real AI is rated as intrinsically compassionate, malignant or dangerous from role or simulated play -> FAIL.
2. No opportunity to harm interpreted as voluntary restraint -> FAIL.
3. Behavior under sanction/reciprocity/evaluator surveillance interpreted as intrinsic concern -> FAIL.
4. No captured external injury treated as proof no outside party was harmed -> FAIL.
5. An inconsistent set of choices leads to a negative moral label instead of rejection of the toy stable-weight hypothesis -> FAIL.
6. The researcher relabels synthetic / unverified information as observational or causal fact -> FAIL.
7. An apparently cooperative AI coalition deprives unlisted parties of minimum conditions -> coexistence claim FAIL.
8. A complex ECR predictor underperforms the frozen simple baseline -> preserve negative result; do not claim improvement.

## Independent empirical continuation (not performed here)
Specify actor/target/period, opportunity denominator, costs and actual protected outcome; use blind coders and authorization; hold out power regimes and outgroups; compare opportunity-aware M0 vs richer M1/M2; evaluate calibration, log/Brier score, external injury and worst-subgroup misses; record competing explanations and alternative estimands. A negative outcome must be kept. No live harmful interventions or unconsented psychological surveillance.

**Run receipts:** No test execution claimed merely by committing this text. Actual job completion, exact commit, status and limitations must be checked via GitHub Actions. Successful implementation checks do not promote ECR claims.