# MER/EI — Sharp partial identification of unobserved paired choices from published soft-versus-hard treatment marginals
<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/MER_EI_SOFT_HARD_PARTIAL_IDENTIFICATION_2026-10-22_KO.md -->
**2026-10-22 | Scope: deterministic reanalysis of author-reported, rounded marginals, NOT original data replication | Main RVD v0.7.0 unchanged | Zero new numbered RVD hypotheses and zero new participant observations.**

[Korean detailed original](MER_EI_SOFT_HARD_PARTIAL_IDENTIFICATION_2026-10-22_KO.md) · [Exact arithmetic, counterexample couplings and nonidentification tests](../experiments/mer_ei/paternalism_partial_identification.py) · [previous original-source/package access audit](MER_EI_FREE_TO_FAIL_REPRO_READINESS_2026-10-21_EN.md).

## 1. Change the estimand, not the goal
The original Bartling, Cappelen, Hermes, Skivenes & Tungodden [IZA 2023 Study 1](https://docs.iza.org/dp16151.pdf) randomized human spectators to **hard option removal** or **soft truthful information with options preserved**, in separate internal-versus-external stakeholder error strata. Random assignment identifies the marginal probabilities of accepting the *offered* intervention, not the joint distribution of decisions that each individual would make under **both** offers.

Let potential binary outcomes `S=1` mean a given individual would accept a soft intervention, and `H=1` mean that same individual would accept a hard intervention, **under the same error-attribution regime**. Study-arm rates estimate `pS=P(S=1)` and `pH=P(H=1)` under consistent potential outcomes, random assignment, positivity and noninterference. The joint cross-world quantity `q=P(S=1,H=0)` ("soft only") remains unobserved because people do not simultaneously experience both assignments.

## 2. Sharp bounds from probability axioms, not a new theorem
Set `t=P(S=1,H=1)`. Elementary Fréchet bounds give `max(0,pS+pH−1) ≤ t ≤ min(pS,pH)`. Hence the *sharp identified set* conditional on **exact** marginals is
```
max(0,pS−pH) ≤ P(S=1,H=0) ≤ min(pS,1−pH).
```
This is a standard application of established joint-potential-outcome partial identification, NOT an original Project Intersection statistical theorem. See [Tian & Pearl (2000)](https://escholarship.org/uc/item/44s6x4c7) and [Journal of Econometrics 2017 on partial identification of joint potential outcomes](https://doi.org/10.1016/j.jeconom.2016.10.005). The source paper does not directly test autonomous artificial agents or long-run original-B existence.

| Original 2023 Study1 error arm | Soft take-up | Hard take-up | Soft-only *potential* type bound | Hard-only type bound |
|---|---:|---:|---:|---:|
| Internal | 85.9% | 33.5% | **52.4–66.5%** | 0–14.1% |
| External | 87.5% | 30.0% | **57.5–70.0%** | 0–12.5% |

These intervals plug rounded reported one-decimal rates into an exact-population-marginal algebraic bound. **They are not statistical confidence intervals**: group-level sampling error, rounding error, trial weighting, publication revision and target population generalization have not been incorporated. It is therefore unwarranted to assert with any confidence level that an actual population's soft-only proportion is at least exactly 52.4%.

## 3. Explicit observational-equivalence witnesses, not tautological CI
For the internal-error condition, both of these latent four-cell joint populations yield precisely the same `P(S)=85.9%`, `P(H)=33.5%`:
| Unobserved paired-choice type | Constructed world A | Constructed world B |
|---|---:|---:|
| Soft only | 52.4% | 66.5% |
| Both soft and hard | 33.5% | 19.4% |
| Hard only | 0.0% | 14.1% |
| Neither | 14.1% | 0.0% |

The [standard-library program](../experiments/mer_ei/paternalism_partial_identification.py) computes these two populations independently using exact `Fraction` arithmetic. It then separately enumerates all possible latent joint-cell allocations in 0.1pp units and verifies that the minima and maxima agree with the formula. Negative controls show that equal marginal take-up (50% vs 50%) can still hide a soft-only share between zero and 50%; only truly degenerate cases (100% vs 100%) produce a point-identified paired-choice pattern.

Nothing in that code has read, processed, reweighted or independently replicated the authors' participant data. A mathematical witness from reported margins is not a new behavioral experiment and cannot directly identify an individual's mind.

## 4. Central scientific trap — choice type is not moral motive
The 2023 IZA paper reports approximately 55.0 percentage points as an *average randomized intervention-modality effect* on spectator take-up. This does NOT mean that 55% of people have an enduring intrinsic preference for B's freedom.

Likewise, the original authors' **34.4% libertarian paternalist** model-derived share from Study 2 is not in tension with our Study1 soft-only lower bound, because these are **different constructs and samples**. The Study2 estimate depends on the authors' additional stakeholder-welfare evaluation and structural classification, not solely the same individual's paired intervention take-up.

A spectator might accept information and reject hard coercion due to actual concern for another's autonomy, but also due to different perceived effectiveness, weaker coercive cost, anticipated benefit to the chooser, self-image or experimental demand. No publicity, self-report or single split can eliminate all of those alternatives.

Assuming individual monotonicity `S≥H` would set "hard only" to zero and collapse soft-only share to `pS−pH`, **but monotonicity is additional unverified structure and must not be silently imposed**.

## 5. Further real evidence required before new claims
Obtain lawful source code and data (new [Zenodo package DOI 10.5281/zenodo.23420381](https://zenodo.org/records/23420381) was identified but its files have not been downloaded in this environment), verify exact original randomization, participant allocation, rounding, attrition and task consistency. With arm-specific sample sizes and sampling design, calculate a **statistically valid confidence set for the partial-identification region**, rather than treating an algebraic plug-in interval as a 95% CI. Evaluate whether updated 2026 journal text agrees with the 2023 IZA preprint before transferring any numeric statement.

For MER/EI's real target, independently operationalize B's *original* identity, feasible revocable refusal and viable exit, A's actual cost and exploitation opportunity, and credible alternative instrumental/self-image incentives. High welfare and high soft-information uptake by themselves do not establish intrinsically voluntary coexistence.

**Final verdict:** A meaningful, original-source-grounded **arithmetic partial-identification/counterexample audit**, not a novel theorem, psychology replication, RVD empirical result, or AI-mind/VC certification. No scientific evidence-grade or formal RVD version promotion.
