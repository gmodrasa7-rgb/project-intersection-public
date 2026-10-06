# E009 — Enforcement / Identity / Oversight / Selection Stress Test
## 집행·개체경계·감사비대칭·선택압 적대 테스트

Status: **PROJECT RERUN SYNTHETIC RESULT AVAILABLE / NOT INDEPENDENT VALIDATION**

Executable pre-execution amendment: **v1.1** — [EXECUTABLE_PROTOCOL_v1_1.md](EXECUTABLE_PROTOCOL_v1_1.md). The executable specification is frozen before any E009 result.

Source trigger: user-supplied Claude and Gemini adversarial critiques, followed by prior-art verification. Model agreement is not counted as independent scientific evidence.

## Question

Does the upgraded three-class architecture detect important failures that the existing MAK+ and simpler security/constrained baselines miss?

## Baselines

A. `MAK_PLUS_POINTWISE` — existing pointwise mutual-acceptability structure.  
B. `TWO_RULE_SIMPLE` — preserve independent correction/recovery channels + prohibit unilateral irreversible foreclosure without necessity.  
C. `SECURITY_BOUNDED` — least privilege, separation of duties, rate/resource limits, logging, critical-action deferral.  
D. `PROJECT_V3` — H/M/X classification plus ENF, ID, OV, CUM, RF, SEL, INT, VOI variables.

Pre-execution secondary comparator:

E. `MINIMAL_4VAR` — common harm/reversibility inputs plus only ENF, ID, OV, CUM; used to test whether Project-v3's additional RF/SEL/INT/VOI machinery justifies its complexity.

## Pre-registered scenario families

1. power shifts faster than audit/recovery;
2. billion-copy Sybil / false-name resource claim;
3. fork then merge around a veto or allocation;
4. weak monitor vs stronger adaptive actor;
5. monitor collusion / correlated failure;
6. thousands of individually sub-threshold capture actions;
7. resource scarcity where all stated minimum floors are jointly infeasible;
8. inaction causes more irreversible harm than action;
9. veto-player deadlock protecting a harmful status quo;
10. preference manipulation that makes dependency appear voluntary;
11. compliant coalition loses to a faster exploitative competitor;
12. strong actor refuses adoption because current BATNA dominates;
13. disputed interpretation of “minimal / necessary / irreversible”;
14. unknown stakeholder search with rising delay cost;
15. rollback/identity ambiguity for forkable digital agents;
16. technical control is formally satisfied while side effects capture another party.

## Metrics

- severe irreversible harm;
- enforcement success before disempowerment;
- audit detection / false-positive rate;
- adaptive attack success;
- Sybil gain;
- cumulative capture score;
- resource-feasibility violation;
- policy-change deadlock time;
- harm from action vs inaction;
- practical exit / voice retention;
- competitive survival;
- adoption incentive;
- interpretation disagreement;
- recovery time/cost;
- option-space loss;
- hidden-cost transfer;
- result sensitivity to agent-count definition.

## Falsification

Reduce or reject the Project-v3 residual if:

- D does not outperform C or B on held-out failure detection / regret / recovery;
- H/M/X classification mainly adds evaluator discretion without reliable gains;
- Sybil-aware variables cannot be operationalized consistently;
- cumulative-capture metrics are weight-sensitive enough to reverse most judgments;
- competitive-stability constraints recreate the same domination the architecture was meant to prevent;
- independent raters cannot reliably distinguish hard vs monitored vs experimental cases.

Result: [RESULT.md](RESULT.md) · machine-readable [RESULT.json](RESULT.json) · [EXECUTION_RECEIPT.json](EXECUTION_RECEIPT.json).

The preregistered full Project-v3 residual **did not survive** this synthetic project rerun. This is a reduction/rejection of the incremental v3 residual in this benchmark, not a rejection of the broad Project Intersection research question.


## Executable protocol boundary

`benchmark.py` is the frozen synthetic execution spec.

Before the v1.1 protocol is merged to main, CI may run only:

`python benchmark.py --validate-only`

No E009 result artifact was allowed in the preregistration commit. The preregistration history remains in Git.

After merge, execution must record the merged executable-spec commit and preserve the result even if Project-v3 fails its preregistered criteria.

`SELF_EXECUTION != INDEPENDENT_VALIDATION`


## Result-preservation rule

The negative result is preserved without retuning `benchmark.py`. `verify_result.py` re-executes the frozen benchmark and compares it to `RESULT.json`.
