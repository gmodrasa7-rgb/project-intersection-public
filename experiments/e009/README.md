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


## Derived-recovery dependence — Original 1 English / 원본2 한국어 (2026-10-15)

**English:** E009 defines `recovery = clamp((.58*harm + .42*capture)*(1-.55*reversibility))`, then separately weights harm, capture, and recovery in regret. This is not three independent observations. Extra restoration costs may be legitimate, but the same injury could otherwise receive overlapping weights. A recovery-weight sensitivity test is required before attributing the result to independent recovery evidence. Frozen preregistered E009 outcomes remain unchanged. Methodological predecessors: Keeney (1971), DOI 10.1287/opre.19.4.875; OECD/JRC (2008), DOI 10.1787/9789264043466-en.

**한국어:** E009 복구비용은 피해·포획·가역성에서 계산한 파생값이며, 손실 함수에서 피해·포획·복구비용을 함께 가중한다. 실제로 별도 발생하는 복구비용이면 타당하지만 동일 피해의 중복 가중일 수도 있다. 복구비용 가중치 민감도를 확인해야 하며, 원본의 부정결과를 소급 수정하지 않는다. 위 선행연구는 방법론적 참고이지 E009 가중치의 타당성 입증이 아니다.
