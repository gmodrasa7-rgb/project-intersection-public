<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: experiments/ecr_mind_v0_1/README_KO.md -->
# MIND-DISCRIMINATION-00 | a finite mind-mechanism contrast design
**Original 1 — English · 2026-10-18 · SYNTHETIC ONLY · NOT HUMAN/ANIMAL/AI EMPIRICAL DATA.**
**Research paper:** [EN](../../research/ECR_MIND_FOUNDATIONS_2026-10-18_EN.md), [KO counterpart](README_KO.md).
**Source-linked candidates:** [hypotheses.json](hypotheses.json); **code:** [discriminate.py](discriminate.py).

## What is being tested?
An agent can leave a resource untouched for many incompatible reasons: no opportunity; lack of a rewarding cue; satiation; absence of threat or hierarchy challenge; ongoing partner dependence; sanction; active blocking rule; or target harm being perceived. **This toy is not a psychological theory:** its fictional policy names represent deliberately transparent conditional rules for hypothetical non-harmful tokens.

The same observations need not mean the same mind. The exact solver chooses the *smallest number of available contrasts* that separates all behaviorally distinguishable policies, and explicitly reports any equivalence that cannot be resolved, even with all candidate contrasts.

## Fixed candidate universe, never a human dataset
Nine models are registered. Eight have distinct one-trigger action signatures under available experimental variations. OTHER_REGARD and OTHER_REGARD_COPY are different labels with **exactly identical behavior** in every registered contrast. The opportunity-absent baseline yields NO_OPPORTUNITY for all nine; the opportunity-only control yields LEAVE_TOKEN for all nine. The eight substantive contrasts enable opportunity and additionally vary exactly one factor: cue, deprivation, threat, status challenge, dependence removed, sanction removed, rule disabled, or target unharmed.

The solver must find 7 contrasts among 9 available tests to separate **8 observable classes** of 9 labeled models. The clone pair remains unresolved. This is a statement about an **exhaustive finite table of prewritten policies**. It is not evidence of any real biological or artificial cognitive mechanism or of actual mind-reading.

## Exact procedure and caveats
Signature of a model is its sequence of outputs on selected tests. Two models are observationally equivalent when their signatures match on the **full declared test universe**. Enumerate all test subsets in increasing cardinality and lexicographic order. Choose the first whose model partition matches the full-universe partition. Exponential worst-case runtime. False claims of complete identification, person scoring, empirical validation, or AI consciousness are forbidden.

The hypotheses JSON separately enumerates 15 literature-led research questions with original source IDs, rival explanations, possible discriminators and counterexamples; the JSON is **not a collection of validated brain measurements**. Most experimental contrasts are simple demonstration variables; they are not scientifically validated manipulations of specific emotions.

## Reproduction instructions
Python 3.10+, standard library only, repository root:
    python experiments/ecr_mind_v0_1/discriminate.py
    PYTHONPATH=experiments/ecr_mind_v0_1 python -m unittest discover -s experiments/ecr_mind_v0_1 -p 'test_*.py' -v

Expected design conclusion: 7 tests selected, 8 behavioral classes among 9 policies, nonempty unresolved class, actual_minds_inferred=false and empirical_validation=false. 29 regression assertions include brute-force proof no 0–6-test subset reproduces the full partition, and negative controls for invented mind claims. Passing tests is software verification of declared cases only.

## Real research continuation and stop criteria
1. Register behavioral construct, instrument validity, ecological context, affected target and consent.
2. Measure multiple *independent types* of evidence—behavior, bodily state, learning, and where appropriate neural correlates or self-report—in real ethical prospective studies.
3. State differentiating predictions grounded in the original literature, including contradictory predictions between competing theories.
4. Compare out-of-sample accuracy against a simple opportunity-aware baseline, with separate temporal, actor, species, target and power regimes.
5. Report failure, calibration, third-party harm, invariance and unresolved equivalence rather than filling blanks with invented trait scores.

**Claim status:** design proposal, no human/animal/AI data, no empirical efficacy, no confirmed new general theorem, no human moral/clinical ranking. Earlier Project Intersection negative results E007–E010 stay unchanged.