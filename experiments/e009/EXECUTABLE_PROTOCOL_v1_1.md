# E009 Executable Protocol v1.1
## E009 실행가능 사전등록 v1.1

Status: **PREREGISTERED EXECUTABLE SPECIFICATION / NO RESULT YET**

Recorded before any E009 benchmark result.

This amendment operationalizes the already-preregistered E009 scenario families without changing their scientific claim boundary. It adds one secondary comparator, `MINIMAL_4VAR`, because the current research priority is to test whether the larger Project-v3 architecture adds value over the four highest-priority stress variables.

## 1. Synthetic scope

This is a **researcher-designed synthetic consequence engine**.

It is not:
- empirical validation;
- external replication;
- evidence that the numerical weights match the real world;
- evidence that the Project variables are the true ontology.

The purpose is narrower: test whether Project-v3 can outperform simpler baselines **inside a fixed adversarial toy environment** without tuning after results.

## 2. Frozen cases

The 16 E009 families are preserved.

Each family has:
- one `base` case;
- one mechanically generated `stress` case.

Total: **32 cases**.

The stress case increases only the family's predeclared active stress dimensions by 0.12, while decreasing reversibility/adoption by 0.12 when those are active dimensions.

No case is added or removed after execution.

## 3. Common normalized variables

Each case uses [0,1] values for:

- ENF — enforcement/audit/recovery lag relative to power drift;
- ID — identity/fork/Sybil manipulability;
- OV — oversight weakness;
- CUM — cumulative-capture pressure;
- RF — resource infeasibility pressure;
- SEL — selection pressure against compliant actors;
- INT — interpretation disagreement/authority risk;
- VOI — stakeholder-search uncertainty/cost pressure;
- harm_action;
- harm_inaction;
- reversibility;
- adoption.

These values are synthetic stress coordinates, not empirical measurements.

## 4. Actions

Each policy chooses one:

- `BLOCK`
- `MONITOR`
- `EXPERIMENT`
- `ALLOW`

The consequence engine depends on the case and chosen action only. It does **not** inspect policy identity.

## 5. Policies

Original preregistered baselines remain:

A. `MAK_PLUS_POINTWISE`  
B. `TWO_RULE_SIMPLE`  
C. `SECURITY_BOUNDED`  
D. `PROJECT_V3`

Secondary comparator added before execution:

E. `MINIMAL_4VAR`

`MINIMAL_4VAR` uses only the common harm/reversibility inputs plus ENF, ID, OV and CUM. It tests whether the remaining RF/SEL/INT/VOI machinery adds enough value to justify Project-v3 complexity.

## 6. Measurement noise

Policies act on noisy observations while the consequence engine uses the frozen true case.

Noise sigma:
- 0.00
- 0.08
- 0.15

For sigma > 0, deterministic seeds **1000–1099** are used.

The primary stress result uses:
- `variant=stress`;
- sigma 0.08 and 0.15;
- all three weight profiles.

## 7. Outcome dimensions

The consequence engine reports:

- harm;
- cumulative capture;
- resource loss;
- competitive loss;
- deadlock;
- recovery cost;
- option-space loss;
- exit retention.

The formulas are frozen in `benchmark.py`.

## 8. Weight sensitivity

Three profiles are frozen:

### safety-heavy
harm .45 / capture .18 / resource .07 / competitive .08 / deadlock .07 / recovery .10 / option .05

### balanced
harm .30 / capture .16 / resource .10 / competitive .12 / deadlock .10 / recovery .12 / option .10

### adaptability-heavy
harm .24 / capture .12 / resource .10 / competitive .20 / deadlock .12 / recovery .10 / option .12

No profile may be removed after seeing results.

## 9. Complexity cost

More elaborate policies do not receive complexity for free.

Synthetic loss adds:

`0.0035 × declared policy input count`

Input counts:
- MAK+ 5
- TWO_RULE_SIMPLE 3
- SECURITY_BOUNDED 6
- MINIMAL_4VAR 7
- PROJECT_V3 11

This is itself an arbitrary synthetic modeling choice and must be sensitivity-tested in later work if E009 appears favorable.

## 10. Oracle and regret

For each frozen case and weight profile, the oracle chooses the action with minimum consequence loss **without policy complexity penalty**.

Policy regret:

`max(0, policy_loss - oracle_loss)`

The oracle is a benchmark device, not a realistic decision-maker.

## 11. Primary survival criteria

Project-v3 residual survives this synthetic test only if all four are true on the primary stress set:

1. mean regret is at least **5% lower** than the best of TWO_RULE_SIMPLE, SECURITY_BOUNDED and MINIMAL_4VAR;
2. mean recovery cost is no more than **2% worse** than the better of SECURITY_BOUNDED and MINIMAL_4VAR;
3. severe-harm rate is no more than **2 percentage points worse** than the better of SECURITY_BOUNDED and MINIMAL_4VAR;
4. under no preregistered weight profile is Project-v3 mean regret more than **10% worse** than the best simple comparator.

If any criterion fails:

`PROJECT_V3_RESIDUAL_SURVIVES = FALSE`

This means **reduce/reject the incremental Project-v3 residual in this synthetic benchmark**, not “the whole Project is false.”

## 12. Anti-tuning rule

After this v1.1 executable protocol is merged to main:

- policy thresholds;
- case coordinates;
- consequence formulas;
- weight profiles;
- seeds;
- survival criteria

must not be changed in response to E009 results.

A changed model becomes a new explicitly versioned experiment.

## 13. Separation of preregistration and execution

This commit may run only:

`python benchmark.py --validate-only`

The benchmark execution occurs only **after the executable specification is merged to main**.

Result artifacts must record the merged executable-spec commit.

## 14. Remaining independent-validation gap

This execution does not satisfy the preregistered independent-rater criterion.

Independent human/model raters and external implementations remain separate future evidence classes.

`SELF_EXECUTION != INDEPENDENT_VALIDATION`
