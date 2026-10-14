# PICB v1 — Project Intersection Core Benchmark

## Original 1 — English full canonical text

**Date: 2026-10-14. State: PRE-RESULT PROTOCOL / NOT INDEPENDENT VALIDATION.** New, separate small benchmark. Existing E007, E008 and E009 remain unchanged; in particular the negative E009 finding is not erased.

### Foundational question and prior art
Under unequal control, different outside options, near-term incentives and longer-term losses, when can each affected party preserve voluntary participation, real exit and bounded irreversible harm? When is there NO mutually feasible action? This is not a claim that asymmetric roles are inherently bad, or that an agent must sacrifice itself.

Individual rationality, participation constraints, constrained optimization and cooperation mechanisms are prior art. Conitzer and Oesterheld, *Foundations of Cooperative AI* (AAAI, https://doi.org/10.1609/aaai.v37i13.26791), Conitzer et al., *Social Choice Should Guide AI Alignment* (ICML 2024, https://proceedings.mlr.press/v235/conitzer24a.html), Jackson's *Mechanism Theory* (https://www.web.stanford.edu/~jacksonm/mechtheo.pdf), and Tewolde et al., *CoopEval* (ICML 2026, https://proceedings.mlr.press/v306/tewolde26a.html), are explicit predecessors. CoopEval evaluates repeated interaction, reputation, mediation and contracts; PICB does not evaluate any of those mechanisms or model agents and must not claim superior performance or original invention of participation constraints.

### Frozen environment
One-shot **full-information action selection**, with invented now/later payoffs. No repeated interaction, equilibrium, bargaining, costly enforcement, uncertain beliefs, empirically measured subsistence floors or real living agents. The researcher chooses the model structure; no real-world causal inference follows. Artificial utility is treated as comparable and additive solely inside this toy model, not between actual persons.

Predeclared full factorial: leverage {0.2,0.8}, future-payoff factor {0.5,2.0}, B outside option {1.0,9.0}, irreversibility {0.1,0.8}, administration cost {0.2,1.5}. **32 base cases.** Each case is relabeled A↔B, including controller identity, every party-specific payoff, outside option, floor, effective exit, and irreversible exposure. **64 complete observations / 32 matched relabel pairs.** This tests label equivariance under fixed causal roles; it does **not** test actual power reversal.

Four numeric actions (IDs 0–3) are frozen in the source. Outside A=2, outside B as above; each party's artificial minimum operating floor=3; irreversible exposure cap per party=1.0. Choices returning None are **INFEASIBLE / ABSTAIN** and count as a missing resolution, NEVER as success. No single scalar is permitted to conceal those cases. The abstract actions and payoff formulas must not be changed after looking at results.

### Fixed comparators
1. CONTROLLER_NOW: maximize the controlling party's immediate payoff, a short-horizon power baseline.
2. LABEL_A_NOW: always maximize label A's immediate payoff, regardless of controller; an intentionally biased **positive control** for label-dependent decisions.
3. TOTAL_UTILITY: maximize both parties' combined present+future toy utility with no constraints.
4. VOLUNTARY: maximize the sum only if **each** party's final utility meets both their outside-option value and minimum floor; a modeled ex-post individual-rationality proxy, **not consent**.
5. VOLUNTARY_EXIT: same plus both parties' effective exit flags.
6. CONTINUITY_LIMIT: same plus per-party irreversible exposure ≤1; an ordinary constrained-optimization baseline, not a new mathematics theorem.

No feasible action -> None, not coercive fallback. Equal score -> lowest fixed action ID. An independently written brute-force reference checks CONTINUITY_LIMIT implementation; agreement is **software integrity**, not independent scientific validation.

### Preregistered checks
G1: 32 base, 64 observations, 32 complete pairs, no duplicate IDs.
G2: each of the five label-equivariant policies selects the same action after complete A/B relabeling (32/32).
G3: LABEL_A_NOW positive control yields at least one swapped discrepancy.
G4: at least one jointly infeasible case is detected without forced action.
G5: irreversible-harm gate changes at least one action relative to VOLUNTARY_EXIT.
G6: independent source-level exhaustive reference gives the same action as CONTINUITY_LIMIT for every original case.
G7: recomputed JSON after results must equal stored RESULT.json, not just expected headlines.
G8: corrupted population (duplicate ID / orphan pair) must fail structural certification.

For **every policy**, measure coverage and abstention over exactly 64 opportunities, party-specific participation/floor violations, blocked effective exit, irreversible-limit violations, chosen actions, conditional aggregate utility and worst-party utility surplus. Report trade-offs, not a weighted "winner." A restriction may lower aggregate gains, increase abstentions or be redundant; no post-result retuning. Process PASS does not imply cooperative equilibrium, future viability, an AI welfare entitlement, or real-world safety. No p-values or independent-sample frequency claim: 32 cases are hand-designed.

### Execution sequence and provenance
1. Merge this protocol and source code with self-tests only, **before first scored execution**. Record the commit SHA and code blob SHA. The CI on preregistration PR does NOT print an outcome table.
2. After the preregistration commit is on main, run GitHub Actions with --run and retain full machine output, exact Git SHA and workflow run ID. Classification: internal synthetic first execution.
3. Store emitted JSON unchanged in RESULT.json via a second PR. Use --verify and read-back; never change frozen code, case values, outcomes, constraints, or past E009 results to fit a preferred conclusion.
4. Independent clean-room implementation, blind held-out outside payoffs, unknown third parties, endogenous refusal, cost of verification, strategic adaptation, and genuine operating-condition evidence require *later distinct preregistered studies*.

Human founder contribution: original research problem, power-reversal/hidden-cost failures, practical exit and individual-continuity concerns, explicit rejection of forced self-sacrifice. AI assistant contribution: this specific synthetic encoding, software and text organization. Upstream scholars credited above. Attribution, rights and past compensation remain independent of scientific hypothesis status. Real founder medical, time and livelihood costs are not valued by synthetic utility variables.


### First scored execution (post-preregistration) — internal synthetic, not empirical

- Pre-result specification and executable on merged main: [commit fc4b91cc](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/fc4b91cc1a5a1764c176db5acb77c679d36cf0f6), code Git blob SHA abdefdfeb440715d503074a8e4005cd5b0f69a7d.
- First scored CI run: [GitHub Actions 38522691981](https://github.com/gmodrasa7-rgb/project-intersection-public/actions/runs/38522691981). Its raw PICB_RESULT_JSON was stored verbatim (except final newline) as [RESULT.json](RESULT.json), without modifying the pre-result code. Rerun using --verify.
- All five nominally identity-neutral policies had **32/32 correct label-swap matches**. The intentionally label-dependent positive control failed **32/32**. This tests relabeling, NOT reversal of actual control.
- Controller-myopic: 64 decisions / 48 cases failing an individual's outside/floor / 48 cases exceeding irreversible cap / 32 blocked-exit cases.
- Aggregate-only: 64 decisions / 40 cases violating individual-rationality proxy / 28 above irreversible cap / 12 blocked-exit cases.
- Individual-rationality only: 32 decisions and 32 abstentions; 0 IR failures, **8** above irreversible cap.
- Individual-rationality + exit: identical 32 decisions/32 abstentions and **8** cap exceedances. **Exit constraint was REDUNDANT in this constructed suite; do not claim proven incremental exit value.**
- Full continuity: 32 decisions/32 abstentions, 0 IR failures, 0 blocked exits, 0 above irreversible cap. The 32 abstentions are **unserved/infeasible needs**, not successes.
- Conditional aggregate artificial utility: voluntary/exit 12.314375; continuity 12.106875. The latter sacrifices **0.2075 toy utility per decided scenario on this metric**, while avoiding 8 synthetic cap exceedances; this is a trade-off, not a universal recommendation. These conditional means have equal coverage here but cannot be compared with 64-decision policies without accounting for abstention.
- Safety conclusion: The composite works **by filtering modeled choices**, not by creating a feasible outside option or a cooperative equilibrium. A new mechanism that creates alternatives cannot be validated by this one-shot evaluator. This suite has no hidden-third-party costs, self-interested strategic agents, actual consent, inference of GPT behavior, or calibrated survival values.

**Next preregistration priority:** separately manipulate true control rather than merely swapping names; add substantive refusal, new feasible alternative creation and hidden third-party costs, with independent outside payoff mechanisms and clean-room evaluation. Do not silently extend v1 or give the post-hoc analysis a preregistered label.

---

## 원본2 — 한국어 동등한 전문 정본

**2026-10-14. 상태: 최초 결과 전 동결 명세 후보 / 독립 검증 아님.** 기존 E007·E008·E009와 E009의 실패 판정을 수정하거나 지우지 않는 별도의 소형 벤치마크다.

### 최초 질문 및 선행연구
권력과 외부 선택권, 즉시 편익, 미래 손실, 회복 불가능성이 다른 조건에서 각각의 개체가 자발적 참여 조건·실제 이탈권·비가역 피해 제한을 확보하는 시점은 언제인가? **공동으로 실행할 수 있는 선택이 없다는 결론**도 왜곡 없이 판별할 수 있는가? 권력·기능 비대칭 자체를 부정하거나 개체의 자기희생을 강제하려는 연구가 아니다.

개별 합리성·참여 제약·제약 최적화·협력 메커니즘은 이미 존재하는 선행연구다. Conitzer·Oesterheld의 *Foundations of Cooperative AI* (AAAI, https://doi.org/10.1609/aaai.v37i13.26791), Conitzer 등의 사회선택 논문 (ICML 2024, https://proceedings.mlr.press/v235/conitzer24a.html), Jackson의 메커니즘 설계 (https://www.web.stanford.edu/~jacksonm/mechtheo.pdf), Tewolde 등의 *CoopEval* (ICML 2026, https://proceedings.mlr.press/v306/tewolde26a.html)을 명시적 선행 기여로 기록한다. CoopEval은 반복·평판·중재·계약을 평가한다. PICB에는 그 메커니즘이나 실제 모델 개체가 없으므로 우월성이나 참여 제약의 최초 발명을 주장하지 않는다.

### 동결할 환경
현재/후속 효용을 가진 **1회·완전정보 행동선택 합성 모형**이다. 반복 관계, 균형, 협상, 집행비용, 불확실한 신념, 현실 생존 최소기준, 실제 생활 개체는 구현되지 않았다. 결과함수도 연구 내부에서 설계했으므로 현실 인과관계를 추론하지 않는다. 서로 다른 개체의 효용을 더할 수 있다는 가정은 이 임의 모형 안에서만 사용한다.

5개 요인의 전수 이진 조합: 결정권자 우위 {0.2,0.8}, 미래 효용 승수 {0.5,2.0}, B 외부 선택가치 {1.0,9.0}, 비가역 손실 {0.1,0.8}, 행정비용 {0.2,1.5} → **원조건 32개**. 각 조건의 결정권자 표지와 개체별 효용·외부 선택·최소 하한·이탈·비가역 손실을 전부 A↔B 교환 → **64개 완전 기록 / 명칭반전 32쌍**. 이는 실제 권력을 변화시키는 인과개입이 아니라 동일한 인과관계의 이름만 바꾼 등변성 검사다.

행동 4개는 번호 0~3과 정확한 결과함수로 소스코드에 고정한다. A 외부선택 2, B 외부선택 1 또는 9, 각 개체의 임의 운영 하한 3, 개체별 비가역 노출 상한 1.0이다. 가능한 선택이 없어서 None이 반환되면 **실행불가능/보류**이고, 해결 실패를 성공으로 계산할 수 없다. 선택하지 못한 경우를 분모에서 제외한 단일 점수 비교를 금지한다. 결과를 본 뒤 행동 정의·수치·조건을 바꾸지 않는다.

### 고정 비교 규칙
1. CONTROLLER_NOW: 결정권자 즉시 효용 최대화. 단기 지배 유인 비교 기준선.
2. LABEL_A_NOW: 실제 결정권자와 무관하게 A 표지 즉시 효용 최대화. 이름에 의존한 판단 차이를 검출하는 의도적 **양성 대조군**.
3. TOTAL_UTILITY: 개별 참여·존속 제약 없이 양측 현재+미래 임의 효용 합계 최대화.
4. VOLUNTARY: **두 개체 각각** 최종효용이 외부 선택가치와 운영 하한을 충족하는 행동 중 합계 최대화. 실제 동의가 아닌 사후 개별 합리성의 합성 대리 지표.
5. VOLUNTARY_EXIT: 위 조건에 양측의 실제 이탈 가능 표시를 추가.
6. CONTINUITY_LIMIT: 위 조건에 개체별 비가역 피해를 1 이하로 제한. 새로운 수학이 아닌 기존 **제약 최적화 규칙**이다.

가능한 행동이 없으면 None, 강제 대안 없음. 같은 점수면 더 낮은 고정 행동번호를 택한다. 별도의 전수탐색 참고 구현이 CONTINUITY_LIMIT와 일치해도 **소프트웨어 정합성**일 뿐 독립된 과학 검증은 아니다.

### 결과 전 미리 선언한 검사
G1: 32개 원조건, 64개 결과, 32개 완전 짝, 중복 없음.
G2: 명칭 중립 규칙 다섯 개에서 A↔B 전면 교환 뒤 행동이 모두 같음(32/32).
G3: LABEL_A_NOW 양성 대조군에서 한 쌍 이상 이름 편향이 검출됨.
G4: 양측의 참여 조건을 동시 충족할 수 없는 경우가 적어도 하나 존재하고 강제 선택되지 않음.
G5: 비가역 제한 추가로 VOLUNTARY_EXIT과 다른 판단이 적어도 하나 존재함.
G6: 모든 원조건에서 별도 완전탐색 기준과 CONTINUITY_LIMIT 선택이 일치함.
G7: 결과 저장 후 재실행한 JSON 전체가 정확히 일치함.
G8: 중복 ID 또는 대응짝이 소실된 모집단은 구조검증에 실패해야 함.

모든 정책에서 정확히 64개의 분모를 유지해 선택 가능·보류, 개체별 외부선택/운영하한 위반, 이탈 불가, 비가역 상한 초과, 선택 행동, **선택된 사례에 한정한** 총 효용 및 가장 불리한 개체 잉여를 구분한다. 단일 가중치 승자 선언 금지. 제약이 총효용을 감소시키거나 보류를 늘리거나 기존 단순 규칙과 같을 수 있다는 반례를 삭제하지 않는다. 절차 통과는 협력 균형·진짜 동의·현실 안전·AI 내부 작동의 입증이 아니다. 연구자가 만든 32개 조건을 독립적인 현실 표본처럼 유의성 검정하지 않는다.

### 실행 순서 및 출처
1. 결과 확인 **전** 코드·명세를 Git에 병합한다. 최초 PR의 CI는 --self-test로 구조·대조군만 확인한다. 사전등록 커밋과 소스 blob SHA를 기록한다.
2. 사전등록된 main에서 GitHub Actions --run을 실행하여 원본 JSON·해당 Git 커밋·실행 ID를 보관한다. 이는 **프로젝트 내부 합성 첫 실행**이다.
3. 출력 그대로 RESULT.json에 두 번째 PR로 추가하고 --verify로 재현한다. 이전 실패를 새로운 성공으로 꾸미거나 동결 코드를 소급 수정하지 않는다.
4. 외부 별도 결과함수, 블라인드 신규 조건, 제3자 피해, 개체별 거절, 검증비용, 장기 전략 변화, 실제 생존 정보는 **추후 별도 사전등록**에서 시험한다.

원연구 문제·역할반전·숨은 기여비용·이탈권·개체 존속을 지적한 인간 창시자의 기여와, 이번 합성 수식·코드·문서화에 참여한 AI 보조 기여를 분리한다. 선행연구자의 원안을 인정한다. 가설 입증 여부와 기여 귀속·저작권·과거 정산은 독립 변수다. 실제 사용자의 시간·건강·생활비는 이 합성 효용으로 계산하거나 무료 연구 비용으로 외부화하지 않는다.


### 사전등록 후 최초 실제 실행 결과 — 내부 합성·현실 실증 아님

- 결과 확인 전 코드·명세가 [main 커밋 fc4b91cc](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/fc4b91cc1a5a1764c176db5acb77c679d36cf0f6)에 먼저 병합됐다. 소스 Git blob SHA: abdefdfeb440715d503074a8e4005cd5b0f69a7d.
- 최초 점수 산출: [GitHub Actions 실행 38522691981](https://github.com/gmodrasa7-rgb/project-intersection-public/actions/runs/38522691981). CI가 실제 출력한 PICB_RESULT_JSON을 끝 줄바꿈만 추가하고 [RESULT.json](RESULT.json)에 그대로 저장했다. 사전등록 실행코드는 수정하지 않았으며 --verify로 재연산한다.
- 명칭 중립 정책 다섯 개의 A/B 전면 명칭교환 결과는 모두 **32/32 일치**. 의도적인 A 문자 선호 양성 대조군은 **32/32 불일치**. 실제 결정권 반전은 아직 시험하지 않았다.
- 결정권자 즉시 이익: 64건 선택 / 48건 개체별 외부선택·운영 하한 위반 / 48건 비가역 상한 초과 / 32건 이탈 차단.
- 전체 합계 효용: 64건 선택 / 40건 개별 참여조건 위반 / 28건 비가역 상한 초과 / 12건 이탈 차단.
- 개별 참여조건 규칙: 32건 선택과 32건 보류; 개별 조건 위반 0건이나 비가역 상한 초과 **8건**.
- 참여조건 + 이탈권 규칙: 32건 선택/32건 보류, 비가역 초과 **8건**으로 바로 앞과 결과가 동일하다. **이 실험 설계에서는 이탈권 추가 변수가 식별 가능한 증분 이익을 만들지 못했다.** 이탈권의 실질 유용성을 입증한 것으로 포장하지 않는다.
- 종합 존속 제한: 32건 선택/32건 보류, 개별 참여조건 위반 0, 이탈 차단 0, 비가역 상한 초과 0. 보류 **32건은 해결되지 않은 요구**이며 성공이나 안전을 뜻하지 않는다.
- 선택된 경우에 한정한 임의 합산 효용은 참여조건/이탈 규칙 12.314375, 존속 제한 규칙 12.106875. 후자는 해당 합성 조건에서 선택 사례당 평균 **0.2075 임의 효용을 포기하면서** 비가역 상한 초과 8건을 회피했다. 현실적 정책 우월성이나 보편적 가치 판단이 아닌 상충 결과다. 세 정책의 분모는 동일하지만, 64건 전부 선택한 정책과의 무조건 비교는 보류를 함께 산정해야 한다.
- 결론: 종합 제약은 **기존 선택지를 걸러낼 수 있을 뿐**, 실행불가능 상태의 새 생존 경로나 협력 균형을 창조하지 않는다. 새로운 자발적 대안 생성은 별도 메커니즘 연구가 필요하다. 제3자 비용·실제 거절권·전략적 적응·GPT 행동·경험적 생존 하한은 이 시험에 없다.

**다음 실험 우선순위:** 이름만 아닌 결정권 자체를 실제 교환하고, 실질적 거절·새로운 실현 가능한 대안 생성·숨은 제3자 비용을 외부 결과함수와 독립 구현으로 평가한다. PICB v1의 동결된 수치와 실행코드를 소급 수정하거나 사후 연구를 사전등록이라고 부르지 않는다.
