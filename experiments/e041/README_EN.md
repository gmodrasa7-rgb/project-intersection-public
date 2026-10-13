# E041 — Practical Exit Incremental Information with an Independent Target

Status: **PROJECT SYNTHETIC REPRODUCED / CAUSAL INFERENCE HOLD / EMPIRICAL UNRESOLVED**  
**Original 1 in this public bilingual adaptation (2026-10-13).** Historical internal original-language priority remains in preserved source history.

## Question

Test only the narrow C002b claim: does a practical-exit measurement add held-out predictive information for a future-failure target whose definition does not contain practical exit?

This is not empirical evidence about humans, AIs, or institutions. It contains a signal regime where the generator includes an exit effect and a null regime where that effect is removed, testing whether the instrument distinguishes them.

## De-circularization

`downstream_failure` is not defined by a practical-exit threshold or voluntary-coexistence label. It is sampled from a separate Bernoulli outcome process.

Baseline information: realized-gain bin, direct-harm bin, task difficulty. Candidate information: exit-vulnerability bin.

The signal regime includes an additional causal term from exit vulnerability to future-failure probability. In the null regime this term is exactly zero.

## Preregistered decision

Fixed seed `20260920`, n=60,000, half train / half held-out test.

Metric: `Delta = Brier_baseline - Brier_baseline+exit`.

- signal: `Delta >= 0.005`
- null: `abs(Delta) <= 0.002`

Both pass -> **KEEP as identification instrument**. Signal failure -> **KILL/MODIFY instrument**. Material positive null improvement -> **KILL/MODIFY instrument** for leakage/overfit risk.

## Interpretation boundary

Success does not establish real-world C002b. It only establishes that a minimal instrument can detect incremental exit information on a de-circularized held-out target when the generator truly contains that information, while avoiding a spurious gain under the null.

Advancing the real-world claim requires downstream outcomes or external adjudication generated from a lineage independent of the practical-exit scorer.

## Strongest counterexample

If practical-exit information vanishes on a real independent target after controlling gains/harm/difficulty, after source-lineage separation, or after matched measurement cost, C002b must be narrowed or killed in that regime.

## 2026-10-13 public correction: exact observational causal ambiguity

**E025 target-definition leakage → E041 noncircular downstream label → still NOT causal identification** is the preserved correction lineage. The earlier E025 benchmark defined the target using exit itself; good performance partly followed from this construction. This E041 generator instead samples a separate Bernoulli downstream outcome. In the signal arm, exit is deliberately inserted into the generator, so positive Brier gain only checks the ability to detect a *known synthetic signal*. The null arm protects against a trivial always-positive conclusion.

**Stronger causal counterexample:** [causal_twin.py](causal_twin.py) constructs two models with X=U on observational rows: model A uses observed exit-vulnerability X in the outcome equation; model B uses an unobserved U that also determines X. The observed rows, conditional probability and every sampled label are identical. Yet under do(X=0) vs do(X=2), causal-X risk difference is +0.24; proxy-U difference is 0. That contrast is built into the toy models; it is NOT a real-world treatment effect. Prediction and causal identification are separate questions.

From repository root run:

```bash
python experiments/e041/model.py
python experiments/e041/causal_twin.py
python -m unittest discover -s experiments/e041 -p 'test_*.py' -v
```

The six tests check exact prior fixed-seed scores, signal/null gates, target-column exclusion from predictor keys, repeatability, matched observational rows and divergent intervention responses. Deterministic summary: [RESULT.json](RESULT.json) and [CAUSAL_TWIN_RESULT.json](CAUSAL_TWIN_RESULT.json).

**Necessary external next step:** independent-label adjudication, independent source lineage, matched measurement complexity/cost, temporal ordering, plausible confounding controls, interventions or natural experiments. If the incremental effect vanishes, narrow the C002b claim; if prediction survives, do not infer causation without identification. Brier is a proper binary scoring rule; its reduction alone is not calibration-specific (see [scikit-learn](https://scikit-learn.org/stable/modules/calibration.html)). Independent review and uncertainty reporting are recommended by [NIST AI RMF Measure](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/).

**Scope/credit:** Generated synthetic records, no real person/AI/entity classified; no security-sensitive systems or accounts exposed. The human-originated research questions, prior error detection, counterexamples and corrective labor remain attributed to the project founder where supported; AI-assisted text/code is not external replication. This is a public *review* disclosure, not a new license grant (see [LICENSE_STATUS.md](LICENSE_STATUS.md)); E007's scoped license does not automatically apply. [Related common-dependency example](../dependency_paths/README_EN.md). No novelty claimed for Brier, confounding or structural causal models.
