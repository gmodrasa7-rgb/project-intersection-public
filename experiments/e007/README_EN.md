# E007 Timing-Sensitivity Research Report — Original 1: English

<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: experiments/e007/README_KO.md -->
<!-- PI-SOURCE: experiments/e007/README.md -->

**Status:** Reproducible **project-run synthetic work sample**, not independently validated empirical research. This standalone English reader edition preserves the claims, failure lineage, tests and limits of the [historical mixed-language E007 report](README.md). It is an explanatory edition, not a frozen replacement for runnable code or independent scientific replication.

[Original 2: Korean](README_KO.md) · [Scope of directory license](LICENSE_STATUS.md) · [Independent implementation protocol](INDEPENDENT_REIMPLEMENTATION_PROTOCOL.md).

## 1. Exact surviving research question and result

> When the same toy multi-agent state is evaluated under two plausible action-timing conventions, does an apparent cooperation or exit outcome remain invariant?

The original finite-horizon game compared **exit-priority timing**, where a valid exit may resolve before a hostile same-period action, with **execute-first timing**, where a previously committed hostile action may execute before the target responds.

The corrected historical **72-case** selected synthetic grid found **36/72** configurations with a different history and/or classification, and **17/72** with a different classification. These are **counts in a designed grid**, not estimated rates of failure or cooperation in real societies.

## 2. Original errors, corrections and preserved negative lineage

**First defect — mistaken role-reversal coordinate:** In cases with B as the leader, the initial timing sweep varied **B's exit coordinate**, although the targeted role was A. The early role-reversal audit was therefore not fully symmetric. The correction was retained and rerun as `kf002-v2-target-symmetric`.

**Second defect — stale action history encoding:** Under execute-first timing, the solver recorded a follower's effective action using the state **before** a hostile strike, including cases where the strike had already made the follower inactive. A correction to the recorded post-strike response state changed the count of history/timing-sensitive configurations from **31/72** to **36/72**. Classification sensitivity remained **17/72**. The original coding failure and its correction are both research evidence about implementation integrity.

### Corrected selected-grid counts

| Observation | Selected-grid count | Selected-grid percentage |
| --- | ---: | ---: |
| Any history and/or classification change | 36 / 72 | 50.0% |
| Classification change | 17 / 72 | 23.6% |
| A-leading timing-sensitive | 18 / 36 | 50.0% |
| B-leading timing-sensitive | 18 / 36 | 50.0% |
| A-leading classification-sensitive | 8 / 36 | 22.2% |
| B-leading classification-sensitive | 9 / 36 | 25.0% |

The 50.0% and 23.6% figures describe **only** the included model conditions; they are not empirical population estimates.

## 3. Critical additional falsifier: arbitrary attack processing order (2026-10-14)

A later structural audit found that the frozen `stage_and_transition` resolves an `ATTACK` by actor A **before** an `ATTACK` by actor B, even where B leads in the declared sequential game. With both starting at one unit of resource and each attacking for one damage, A incapacitates B before B's strike; B cannot respond and A's payoff is higher **because of internal execution order**, not demonstrated strength, legitimate authority or strategically justified cooperation.

A deliberately bounded [same-snapshot simultaneous-attack control](timing_variants.py) evaluates both strikes against their common original state and yields equal resource losses and symmetric attack payoffs under that matched toy counterexample. [Regression tests](test_e007_timing_variants.py) check the difference and reverse actor labels.

**Scope:** This additional control does not rewrite the historical frozen 72-case baseline, select a new equilibrium or establish a true physical timing law. Published 72/36/17 is valid only for its documented processing order; general actor-label neutrality and robust voluntary coexistence are **not proven**.

## 4. Reproducibility, isolation and provenance

The public artifact was prepared through an allowlisted isolated build, not by publishing the entire private laboratory. The configured validation checks the broader project regressions, isolation, **27 standalone E007 regression tests**, exact rerun of 72/36/17, credential and personal-pattern screening, explicit provenance, minimal dependencies and a scoped license note.

Execute from the repository root:

```bash
python -m pip install -r experiments/e007/requirements.txt
python -m pytest -q -p no:cacheprovider experiments/e007
python experiments/e007/timing_probe.py --summary-only --check
```

Run `git rev-parse HEAD` and store the observed environment and results. A mismatch must be reported, **not fixed by tuning the frozen code to reach the expected headline**.

Source commit and archive digest belong to externally generated provenance and execution receipts; embedding the final archive digest inside the same archive would create circular provenance. Green CI certifies the configured computation's reproducibility **only**, not scientific truth, external evaluation or safety of frontier systems.

For a *lineage-separated* review, use the [independent reimplementation specification](INDEPENDENT_REIMPLEMENTATION_PROTOCOL.md), rebuilding game, timing variants, solver, classifier and grid without copying project source.

## 5. Research behavior and falsification principle

This experiment documents a narrower answer than the intended original cooperation hypothesis:

1. Challenge an apparent favorable result's implementation assumptions.
2. Identify timing dependence, then identify errors in the timing audit itself.
3. Record the role-coordinate failure, correct it and independently test the history encoding.
4. Preserve the 31-to-36 correction and the unchanged 17 classification count.
5. Add an actor-priority attack control without retrospectively changing old results.
6. Treat all remaining differences as **questions to falsify**, not proof of cooperation.

The reproducible sequence is `claim → competing rule → attack → recorded failure → correction → regression test → narrower claim`.

## 6. Missing measurements and strongest counterexamples

No broad benchmark or general coexistence theory is validated while these remain unresolved:

- stochastic detection and enforcement delays rather than a single deterministic cost;
- tied best responses, equilibrium-selection sensitivity and the difference between survival and consent;
- state-specific autonomy and practical exit versus terminal aggregate utility;
- copy, replacement, external stakeholder and third-party-harm counterfactuals;
- proof that labels, turn order or arbitrary implementation priority do not create the result;
- external clean-room reproduction before experiments using learned AI agents.

Discriminating reviewer attacks include proposing a third plausible timing convention, replacing equilibrium selection, finding formal exit with no practical possibility, identifying a stronger simpler baseline, flipping roles without changing causal facts, and independently observing a different count.

**Narrowing or rejecting the construct is warranted** if timing variants erase meaningful voluntary choice, simple models explain the same labels, exit constraints never affect decision-relevant outcomes beyond chosen examples, the classifier can be gamed, or external reviewers cannot reproduce the published package. Unfavorable review is a legitimate result.

## 7. Publication rights and other parties' interests

This release does **not** authorize disclosure of private `rgbm-lab` contents, unrelated personal details, funding verification or credentials. [The license-status note](LICENSE_STATUS.md) defines the scope for this directory; it does not grant rights over the whole public or private research program.

Preserve the founder's research questions and discoveries, external prior authors, AI-assisted implementation, independent evaluator status and remediation costs as distinct roles. The toy experiment cannot adjudicate actual agent identity, welfare, rights or compensation.

**Reader-edition boundary:** The linked [historical E007 text](README.md) contains English narrative with some Korean insertions; this page and its [Korean edition](README_KO.md) are coherent reading interfaces, not a claim of independently certified perfect translation or a newly computed result.
