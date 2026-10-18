<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: experiments/ecr_v1_4/README_KO.md -->
# ECR v1.4 — bounded synthetic negative-control protocol
**Original 1 English · 2026-10-18 · DESIGN ONLY / NO EMPIRICAL EXECUTION**
**Paper:** [English](../../research/ECR_INFERENCE_AND_COEXISTENCE_2026-10-18_EN.md) | [Korean counterpart](README_KO.md).

## Question
Can an ECR inference engine avoid mistaking a pre-power cooperative signal for a post-power disposition, invented mutual gain for verified incentive alignment, private coalition gain for third-party safety, and self-reported provenance for independent evidence?

## Frozen synthetic inputs
Two hypothetical types P/T, both give an identical pledge before acquiring a resource-transfer opportunity. After the power change: P's coexist/capture utilities are 3/2, T's are 1/2. A structural nonpunitive gain m is added ONLY to coexistence payoffs. m=0 distinguishes models; m=2 makes both prefer coexistence within the finite declared assumptions. The source of m is **NOT EMPIRICALLY VERIFIED**. Third-party floor is true/false/unknown, and practical exit is true/false/unknown. Coalitional payoffs: status quo (2,2); unilateral deviations (0,3), (3,0); joint deviation (3,3). These integer values are **chosen constructions**, not calibrated probabilities, human preferences, or observed AI incentives.

## Methods and executable checks
- Observation equivalence: same pledge yields incompatible post-power choices.
- Model-relative robustness: no candidate if any declared type gains from capture; do not accept absent exit, third-party breach or unknown third-party status.
- Externality: a clean own-payoff comparison does not offset a third party's essential-floor breach.
- Coalition: individually unattractive deviations do not exclude a jointly attractive deviation.
- Evidence: a user-typed OBS/CAU string does not constitute an independently checked source.
- Empty or malformed model collections are refused.

Run locally (Python >=3.10, no dependencies):
~~~sh
python experiments/ecr_v1_4/probe.py
cd experiments/ecr_v1_4 && python -m unittest -v test_probe
~~~
CI command from repository root:
~~~sh
PYTHONPATH=experiments/ecr_v1_4 python -m unittest discover -s experiments/ecr_v1_4 -p 'test_*.py' -v
~~~

## Pre-registered? Executed?
This is a **public candidate test specification**, not a pre-registered empirical experiment. The source and tests are inspectable; creation of this code does not imply it has run or passed. Repository CI, if triggered and passing, establishes only implementation-level logical self-consistency, not social prediction accuracy, model preference truth, generalization, consent, or independent replication. No real-world dataset, person scoring, model weights, or future superintelligence used.

## Decision and stop rules
PASS may mean ONLY "these declared finite logical cases match expected outputs." Any violated assertion FAILS code consistency; it is not a discovery that voluntary coexistence is impossible. A safe-looking synthetic output must not change E007/E008/E009/E010 status or claim scientific validation. Next experiment requires a frozen M0 baseline, blinded annotation, held-out agents/time/power regimes, independent review, uncertainty coverage, forecast calibration, and externality checks. Record null and negative outcomes.