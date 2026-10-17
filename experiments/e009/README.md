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

**2026-10-11 posthoc audit (project lineage, not independent validation):** [paired-observation + complexity sensitivity report](../../E009_RANDOMNESS_COMPLEXITY_POSTHOC_AUDIT_2026-10-11_KO.md) · [executable paired-observation auditor](paired_observation_audit.py). Original preregistered negative result remains unchanged.

The preregistered full Project-v3 residual **did not survive** this synthetic project rerun. This is a reduction/rejection of the incremental v3 residual in this benchmark, not a rejection of the broad Project Intersection research question.


## Post-hoc family-unit and safety-tolerance audit (2026-10-14) — English Original 1

**Scope:** Diagnostic analysis only; the frozen E009 executable, the preregistered survival thresholds, and the original negative RESULT.json remain unchanged. Run `python experiments/e009/paired_observation_audit.py --family-audit` to recompute the original policy-specific observation streams and separately compare common-noise observations on exactly the same 16 constructed stress families.

**Measurement correction:** 9,600 metric rows per policy are **3,200 distinct policy decisions**, each evaluated under three frozen weight profiles. The new executable auditor checks the original regret and severe-event fractions against the published RESULT.json; it also rejects injected whole missing or undeclared decision keys and reports leave-one-family-out (LOFO) policy comparisons for both observation-noise treatments. LOFO on 16 hand-designed families is an influence check, **not** an independent experimental sampling distribution, confidence interval, significance test, or empirical validation.

**Observed 16/16 LOFO result:** In the CI-executed project-lineage recomputation, Project-v3's mean regret remained higher than MINIMAL_4VAR after removing any one of the 16 families, under both the frozen original policy-specific noise assignment (16/16 positive gaps; range 0.021604–0.026521) and post-hoc common noise assignment (16/16; range 0.020079–0.025352). This rejects a *single-family-only* explanation for the synthetic regret gap; it does not establish independent generalization or support any real-world outcome.

**Safety-gate caveat:** E009 criterion 3 allows up to **2 percentage points** more severe events than the best comparator. In the frozen original stress experiment, Project-v3's 1.65625% corresponds to **53 of 3,200 distinct decisions**, versus MINIMAL_4VAR's **0 of 3,200**. Thus criterion 3 passes even though 53 additional synthetic severe events occur. It is an *allowed-tolerance check*, not proof of safety equivalence, no serious harm, protected individual viability, or any real-world rate. The other three original preregistered criteria still fail. Do not relabel the full Project-v3 residual as supported.

**Methods and precedent:** Same-random-input policy comparisons can aid precision but may not reduce variance under every dependence pattern (Wright & Ramsay 1979, https://doi.org/10.1287/mnsc.25.7.649; Glasserman & Yao 1992, https://doi.org/10.1287/mnsc.38.6.884). The original benchmark uses distinct policy-specific draws and the secondary audit separately applies common draws; neither independently verifies its consequences. Contributor-origin questions and falsification constraints remain attributed to the human founder; code audit assisted by AI.

## 사후 사례군 단위·안전 허용폭 감사 (2026-10-14) — 한국어 원본2

**범위:** 진단적 재분석에 한정한다. 동결된 E009 실행코드, 사전등록 생존 조건, 원래의 부정적 RESULT.json은 수정하지 않았다. `python experiments/e009/paired_observation_audit.py --family-audit`로 원래 정책별 개별 관측 난수 방식과 정책 간 동일 관측 난수 방식을 **동일한 연구자 설계 스트레스 사례군 16개**에서 별도로 계산한다.

**측정 단위 수정:** 정책당 9,600개의 지표 행은 서로 독립된 결정 9,600개가 아니라, **고유 의사결정 3,200개**에 동결된 가중치 프로필 3종을 재적용한 것이다. 새 실행 감사는 원본 regret·심각 피해 발생률을 공개 RESULT.json과 대조하고, 통째로 빠진 결정이나 미등록 결정 키를 주입한 음성 대조군을 거부하며, 두 관측 난수 처리 모두에서 사례군 하나씩 제거(LOFO)한 정책 비교를 보고한다. 연구자가 설계한 사례군 16개의 LOFO는 특정 가족의 영향력을 보는 진단이지, **독립표본 분포·신뢰구간·유의성 검정·현실 검증**이 아니다.

**실행으로 확인된 LOFO 16/16 결과:** GitHub CI에서 프로젝트 코드로 재계산한 결과, 사례군 16개 중 어느 한 개를 제외해도 Project-v3의 평균 regret이 MINIMAL_4VAR보다 높았다. 원래의 정책별 별도 노이즈 방식은 16/16에서 양의 격차(0.021604~0.026521), 사후 공통 노이즈 방식도 16/16에서 양의 격차(0.020079~0.025352)였다. 따라서 **특정 사례군 하나만** 때문에 합성 regret 열세가 발생했다는 설명은 기각되지만, 독립적 일반화나 현실 결과의 증거는 아니다.

**안전 조건의 해석 한계:** E009의 세 번째 조건은 최선의 비교 정책보다 심각 피해가 **최대 2%포인트** 높아도 통과시킨다. 원본 합성 스트레스 실험에서 Project-v3 1.65625%는 서로 다른 결정 **3,200개 중 53건**에 해당하고 MINIMAL_4VAR는 **3,200개 중 0건**이다. 따라서 추가 합성 심각 피해가 53건 발생해도 해당 조건은 통과한다. 이는 *허용폭 이내*라는 뜻이며, 동등한 안전, 심각 피해 부재, 개체별 생존조건 보장, 현실 발생률을 입증하지 않는다. 기존의 나머지 세 사전등록 조건은 그대로 실패했고, Project-v3 전체 잔차를 지지하는 근거로 재승격하지 않는다.

**방법·선행연구:** 정책 간 동일 난수 입력 비교는 정밀도에 도움이 될 수 있지만 상관구조에 따라 분산을 오히려 증가시킬 수도 있다(Wright & Ramsay 1979, https://doi.org/10.1287/mnsc.25.7.649; Glasserman & Yao 1992, https://doi.org/10.1287/mnsc.38.6.884). 원래 실험은 정책별 별도 노이즈를 사용했고 후속 감사는 공통 노이즈를 별도로 검사한다. 두 경우 모두 합성 결과함수에 대한 독립적 사실 검증이 아니다. 연구 질문과 반증 원칙의 원기여는 인간 창시자이며, 코드는 AI 지원 감사로 구분한다.

## Executable protocol boundary

`benchmark.py` is the frozen synthetic execution spec.

Before the v1.1 protocol is merged to main, CI may run only:

`python benchmark.py --validate-only`

No E009 result artifact was allowed in the preregistration commit. The preregistration history remains in Git.

After merge, execution must record the merged executable-spec commit and preserve the result even if Project-v3 fails its preregistered criteria.

`SELF_EXECUTION != INDEPENDENT_VALIDATION`


## Result-preservation rule

The negative result is preserved without retuning `benchmark.py`. `verify_result.py` re-executes the frozen benchmark and compares it to `RESULT.json`.

## E009 secondary verdict audit — Original 1 English (2026-10-16)

The existing `verify_result.py` re-executes the frozen same-project E009 simulation. A separate `secondary_verdict_audit.py` now **recalculates the four preregistered survival criteria without importing the simulation's policy/decision/criterion functions**, checking the published summary, all three weight-profile row counts, score aggregation, the frozen benchmark's byte and Git-blob hashes, and five deliberate negative-control mutations. The validator is run in `.github/workflows/public-repository-audit.yml`.

Run from repository root:

```bash
python experiments/e009/verify_result.py
python experiments/e009/secondary_verdict_audit.py
```

**Evidence limit:** both programs use project-authored experiment inputs and published output. Passing these gates does not independently reconstruct the 16 synthetic consequence families, prove correctness of the original policies or scenario weights, establish independent implementation, or demonstrate real-world effects. Reproducibility of arithmetic verdicts is not a second experiment. The published E009 Project-v3 negative result remains unchanged. An unaffiliated blind implementation has **not** been obtained.

## E009 2차 판정 감사 — 원본2 한국어 (2026-10-16)

기존 `verify_result.py`는 같은 프로젝트가 작성한 E009 동결 시뮬레이션을 재실행한다. 별도로 추가한 `secondary_verdict_audit.py`는 **원 실험의 정책·결정·판정 함수를 불러오지 않고** 사전등록 생존조건 네 개를 다시 계산한다. 공개 요약수치, 가중치 프로필 세 개의 행 수, 평균값 집계, 동결 코드의 바이트 해시 및 Git 객체 해시를 확인하고, 의도적으로 변조한 음성 대조군 다섯 개가 모두 차단되는지 검사한다. 이 검사는 기존 공개 저장소 거버넌스 CI에 연결했다.

위의 두 명령어를 저장소 루트에서 순서대로 실행할 수 있다. **증거 한계:** 두 검사는 동일 프로젝트가 만든 데이터와 평가 환경을 사용한다. 16개 합성 결과함수·정책·가중치를 독립적으로 다시 구현하거나 외부 현실 효과를 증명한 것이 아니다. 판정 수치의 별도 계산은 새로운 실험이나 제3자 독립 복제가 아니다. E009의 기존 부정적 결과는 유지되며, 외부 이해관계 없는 평가자의 맹검 독립 구현은 아직 확보되지 않았다.


## Post-hoc declared-vs-referenced complexity inputs — Original 1 English (2026-10-16)

**New bounded anomaly, not a correction to frozen E009:** The preregistered protocol charges `0.0035 × declared policy input count` and lists counts of 5 for `MAK_PLUS_POINTWISE` and 3 for `TWO_RULE_SIMPLE`. However, direct inspection of the frozen `choose()` implementation finds only `harm_action` and `harm_inaction` referenced in those two policy decision branches. The third common alias `reversibility` is loaded globally but not used in either decision branch. The other policies have 6, 7 and 11 syntactically referenced input dimensions, matching their respective declared counts. This is a **measurement-definition ambiguity**, not proof of deceptive coding or a programming error: a declared complexity proxy may intentionally count design/oversight burden beyond active features. Syntactic referencing is not the same as true behavioral or causal feature importance.

**Conditional post-hoc sensitivity — not a preregistered result:** If, and only if, complexity cost is redefined as the number of distinct input dimensions referenced in the decision branch, the published synthetic stress-set regrets shift by the exact difference `0.0035 × (referenced − declared)`, with frozen decisions, consequences and unpenalized oracle unchanged. Regret is nonnegative before this nonnegative penalty, so no zero-clipping changes this accounting calculation.

| Policy | Declared → referenced | Published mean regret → hypothetical repriced regret |
| --- | --- | --- |
| MAK_PLUS_POINTWISE | 5 → 2 | 0.096127399 → 0.085627399 |
| TWO_RULE_SIMPLE | 3 → 2 | 0.063240512 → 0.059740512 |
| SECURITY_BOUNDED | 6 → 6 | 0.100897475 → 0.100897475 |
| MINIMAL_4VAR | 7 → 7 | 0.065323097 → 0.065323097 |
| PROJECT_V3 | 11 → 11 | 0.090021688 → 0.090021688 |

Under this *hypothetical* repricing, `MAK_PLUS_POINTWISE` and `PROJECT_V3` swap regret rank, while the best simple comparator remains `TWO_RULE_SIMPLE`, widening the latter's lead over Project-v3 from **42.35% to approximately 50.69%**. This **does not** retrospectively change the frozen E009 published metric, thresholds, status, baseline selection, or independent-validation gap. The lesson is to preregister an operational definition of complexity separately from the observed behavior; input count, developer effort, evaluation expense and computational runtime are different possible cost models.

**Executable check:** `python experiments/e009/complexity_input_dependency_audit.py` parses the frozen source via Python AST, rejects a mutated policy branch that adds a new syntactic input reference, checks the published table under the stated conditional cost model, and prints the narrow result. The original E009 `RESULT.json`, `benchmark.py` and execution receipt remain untouched. This test is project-lineage post-hoc analysis, not a new blinded run or real-world evidence.

## 사후 복잡성 변수 수 불일치 감사 — 원본2 한국어 (2026-10-16)

**새로 발견한 제한적 불일치이며 E009 동결 원본을 수정하지 않는다.** 사전등록된 벌점은 `0.0035 × 선언된 정책 입력변수 수`이고, `MAK_PLUS_POINTWISE`와 `TWO_RULE_SIMPLE`에 각각 5개와 3개를 부여한다. 하지만 동결된 `choose()` 코드를 조사하면 두 정책의 실제 조건식은 `harm_action`, `harm_inaction` 두 변수만 참조한다. 공통 별칭 `reversibility`는 함수 입구에서 불러오지만 이 두 정책의 결정 조건식에는 사용되지 않는다. 나머지 세 정책에서 정적으로 참조하는 입력 차원 6·7·11개는 선언된 숫자와 같다. **이것은 측정 정의의 불확실성이다.** 선언된 벌점에 실제 참조하지 않는 변수와 별도의 설계·감사 부담까지 포함하려는 의도가 있을 수 있으므로 허위 코딩이나 확정적 구현 오류로 단정하지 않는다. 정적 변수 참조는 실제 행동 변화·인과적 중요도와 동일하지 않다.

**조건부 사후 민감도 검사:** 정책의 복잡성 비용을 실제 결정 분기에서 정적으로 참조한 고유 변수 개수로 바꾼다는 가정에서만, 기존 합성 결과의 평균 regret에 `0.0035 × (참조 수 − 선언 수)`를 가감할 수 있다. 정책 선택·결과함수·벌점이 없는 오라클은 그대로 두며, 벌점 제외 regret은 음수가 아니므로 0 하한 절단 효과가 발생하지 않는다. 위 영문 표는 원래 점수와 가정하의 점수를 병렬 표시한 것으로 동결 결과를 대체하지 않는다.

이 가정을 적용하면 MAK+와 Project-v3의 regret 순위는 역전되지만 가장 낮은 regret의 단순 기준선은 계속 TWO_RULE_SIMPLE이다. Project-v3의 해당 기준선 대비 열세는 **약 42.35%에서 약 50.69%**가 된다. 사전등록된 생존조건, 발표된 부정적 결과, 독립 검증 미확보 상태는 변하지 않는다. 변수 참조 수·개발 비용·실행 시간·평가 비용을 동일한 복잡성 개념으로 취급하지 말고, 후속 연구에서는 서로 다른 비용 모형을 별도로 사전등록해야 한다.

**실행 검사:** `python experiments/e009/complexity_input_dependency_audit.py`는 Python AST로 동결된 정책 코드를 검사하고, 인위적으로 변수 참조를 추가한 음성 대조군을 탐지하며, 가정에 따른 기존 결과 수치를 재계산한다. 원래 `RESULT.json`, `benchmark.py`, 실행 영수증은 수정하지 않았다. 이 검사는 같은 프로젝트 계보의 사후 분석이며 외부 맹검 복제나 현실 검증이 아니다.

## VOI outcome-path identifiability — Original 1 English (2026-10-16)

**Status: POST-HOC / SAME-PROJECT CODE DIAGNOSTIC / NOT INDEPENDENT VALIDATION.** The frozen `benchmark.py`, `RESULT.json`, protocol, and original negative survival verdict remain unchanged.

The `PROJECT_V3` decision function reads the stakeholder-search/uncertainty variable `VOI`, but the synthetic `consequence(case, action)` engine does not use VOI in any outcome equation: the local `voi` value is unpacked but not read. There is no sequential information acquisition, observation update, or explicit information-to-action transition. For a fixed other-feature vector and fixed action, changing only VOI cannot change the current engine's harm, capture, resource, competitive, deadlock, recovery, option-loss, or exit-retention output.

**Constructed metamorphic counterexample, not one of the 32 frozen cases:** set all feature coordinates to zero and toggle VOI between 0 and 1. `PROJECT_V3` changes its choice from `ALLOW` to `MONITOR` while the outcome engine remains VOI-invariant conditional on action. `ALLOW` produces zero deadlock and option loss; `MONITOR` produces deadlock 0.1152, option loss 0.03456, and exit retention 0.97696. The additional unpenalized consequence loss is 0.009792 under safety-heavy weights, 0.014976 under balanced weights, or 0.0179712 under adaptability-heavy weights. The unchanged V3 complexity penalty is 0.0385, so the balanced constructed-case regret moves from 0.0385 to 0.053476. This is a **model semantics test**, not an estimate of real-world monitoring, learning, or stakeholder-search effectiveness.

**Executable failure gate:** `python experiments/e009/voi_identifiability_audit.py` verifies the frozen benchmark byte hash, outcome invariance for all actions on 32 existing synthetic cases plus the constructed case, exact expected profile-level counterfactual losses, and a negative control that injects a VOI-dependent outcome (which the gate must reject). A paired VOI-extremes diagnostic counts changed V3 actions and their direction of weighted-loss change on the 32 project-authored cases; these are not 32 independent observations. The gate is included in the existing public governance CI on the draft PR. An implemented information-value transition in a future, separately versioned model would need an appropriately revised causal test and independently frozen holdout.

**Claim boundary:** Absence of VOI from these particular outcome equations does not establish that information search is valueless or that VOI could not serve as a correlated proxy. A 200-trial parameter perturbation with the same missing outcome path cannot establish VOI's causal incremental value. Next material decision evidence requires independently specified information-acquisition costs and benefits, delayed updates, stakeholder omissions, and equal-budget simple comparators. No claim of field validation or independent scientific reproduction is made.

## VOI 결과 경로 식별성 감사 — 원본2 한국어 (2026-10-16)

**상태: 사후 검사 / 동일 프로젝트 코드 계보 / 독립 검증 아님.** 동결된 `benchmark.py`, `RESULT.json`, 사전등록 조건 및 기존 음성 판정은 변경하지 않는다.

`PROJECT_V3`의 판단 함수는 이해관계자 탐색 및 불확실성 변수인 `VOI`를 사용하지만, 합성 `consequence(case, action)` 결과함수는 VOI를 어떤 결과식에도 사용하지 않는다. `voi` 값을 꺼내지만 이후 읽지 않는다. 정보획득, 관측 갱신, 새 정보에 따른 후속 행동을 표현한 시간 전이도 없다. 다른 좌표와 행동을 고정하고 VOI만 변경하면 현재 결과함수의 피해·포획·자원·경쟁·교착·복구·선택지 손실·이탈 보존값은 변하지 않는다.

**별도로 구성한 변형 대조군이며 기존 동결 사례 32개에는 속하지 않는다.** 다른 모든 좌표를 0으로 둔 채 VOI를 0에서 1로 변경하면 V3 선택은 `ALLOW`에서 `MONITOR`로 바뀐다. 결과함수는 같은 행동에 대해서 VOI와 무관하다. `ALLOW`의 교착·선택지 손실은 0이고, `MONITOR`의 교착은 0.1152, 선택지 손실은 0.03456, 이탈 보존은 0.97696이다. 이로 인한 추가 벌점 제외 손실은 안전중심 0.009792, 균형형 0.014976, 적응중심 0.0179712이다. V3의 복잡도 벌점 0.0385는 유지되며 균형형 조건의 구성사례 regret은 0.0385에서 0.053476으로 증가한다. 현실 감독 및 정보탐색의 효과를 측정한 결과가 아니라 **현재 합성 모형의 의미론적 식별성 검사**다.

**실행 검사:** `python experiments/e009/voi_identifiability_audit.py`는 동결 코드의 바이트 해시를 확인하고 등록 사례 32개 및 구성사례에서 각 행동의 VOI 불변성, 가중치 프로필별 예상 손실, VOI가 결과식에 영향을 주도록 인위적으로 바꾼 음성 대조군의 차단 여부를 검증한다. 등록 사례의 VOI를 양끝으로 변화시켜 V3 행동 변화와 손실 방향도 세지만, 32개 사례를 독립 현실 관측으로 계산하지 않는다. 기존 공개 CI에 연결된 초안 PR에서 검사한다. 후속 버전에 실제 정보가치 전이식을 추가한다면 그 모형에는 새 인과 검사와 별도 동결 홀드아웃이 필요하다.

**주장 한계:** 이 결과식에서 VOI가 제외됐다는 사실은 정보탐색 자체가 무가치하다는 증거가 아니며, VOI가 다른 입력의 상관된 대리변수일 가능성도 배제하지 않는다. 누락된 인과 경로를 그대로 두고 200회 계수 섭동만 수행해서 정보획득의 증분 가치를 검증했다고 주장하지 않는다. 다음 단계는 외부에서 별도로 정한 탐색비용과 이익, 지연된 관측 변화, 이해관계자 누락손실, 동일 정보·비용 기준의 단순 비교정책이다. 외부 독립 복제 또는 현실 검증을 수행했다고 주장하지 않는다.
