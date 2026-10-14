# Coalition Externality & Missingness Probe — v0.1
# 협력 외부효과·미관측 반례 시험기 — v0.1

**Date / 일자:** 2026-10-14
**Status / 증거유형:** PROJECT-AUTHORED, POST-HOC, DETERMINISTIC SYNTHETIC PROBE. NOT PREREGISTERED; NOT FIELD EVIDENCE; NOT INDEPENDENT REPLICATION. / 프로젝트 자체 작성·사후 설계·결정적 합성 시험. 사전등록·현장 증거·외부 독립재현 아님.

## Original 1 — English

### Research question and experimental delta

A cooperation mechanism may increase every *participating coalition member's* payoff while transferring costs to an affected nonmember. Even aggregate gains over **all known actors** need not establish individual acceptability or preserve practical exit and continuance. The experiment deliberately distinguishes (i) coalition-member payoff aggregation, (ii) all-observed-actor aggregation, and (iii) a separately constrained admissibility check. It also distinguishes missing outcomes from measured zero.

This is a **small instrument and counterexample set**, not a theorem of general non-domination and not a reproduction of CoopEval. The underlying ideas of game-theoretic externalities, participation constraints, welfare aggregation, informed consent, resource floors, and missing-data reasoning predate this Project. A synthetic gate that blocks its own designed failure cases does not demonstrate real-world usefulness.

**Three affected actors:** A/B are participating coalition members; C is an affected bystander (not a consenting coalition member by default). Each proposed action has invented payoff *changes* relative to the same baseline. In the toy model, all are measured in arbitrary additive units. Member-only and all-affected-sum selectors select a positive-sum change; they are *illustrative arithmetic baselines*, **not** published CoopEval policies.

The gate evaluates:
1. C's payoff must be observed. Missing is **UNRESOLVED**, not zero.
2. Neither member has a negative payoff change; both members have the declared effective-exit flag.
3. Any known loss above a **declared arbitrary 2-unit budget** blocks. C's post-action resource must meet a **declared arbitrary 5-unit continuance floor** whether C's payoff change is positive or negative. If C is harmed within the budget, C's consent must be affirmatively true (unknown stays unresolved, false blocks). Definite violations take precedence over missing consent.
4. Results are **ADMISSIBLE / BLOCKED / UNRESOLVED** under these stated assumptions. ADMISSIBLE means *not disallowed by this tiny rule set*, not actual autonomous informed consent or proof of justice. A higher-level legal duty or a newly observed party can invalidate it.

### Reproduce (Python standard library, no downloads or API tokens)

From the repository root:

\`\`\`sh
python experiments/coalition_externality_probe/probe.py --verify
\`\`\`

Expected at initial check: ten designed cases; 65 assertions/checks passed; member-only SELECT 9, all-observed aggregate SELECT 8, gate ADMISSIBLE 3, BLOCKED 6, UNRESOLVED 1. These frequencies are **case-design counts**, not performance estimates or empirical rates. The code prints a machine-readable JSON receipt; the gate's reason code is preserved for each example.

Positive controls: shared gain without external harm; small *declared consensual* loss that stays within the artificial budget and resource floor. Negative controls: negative-sum spillover, positive-sum spillover hiding severe loss, explicit nonconsent, violated continuance floor, absent exit, harmed member. Missing-data control: unknown C payoff must not silently become zero. Metamorphic checks: A/B label reversal does not change decisions or reasons. The C nonmember/member role cannot be interchanged as a *label-only* reversal without changing the experiment's causal structure.

### Attribution, intellectual-property boundary, and research origin

**Prior work credited explicitly (none of its code/text/data copied):**

- **R. M. Thrall & W. F. Lucas (1963),** *N-person games in partition function form*, *Naval Research Logistics Quarterly* 10(1):281–298, https://doi.org/10.1002/nav.3800100126 — historical foundational work on coalition/partition externalities. Publisher rights remain with the relevant rights holder; **bibliographic citation only**.
- **Emanuel Tewolde, Xiao Zhang, David Guzman Piedrahita, Vincent Conitzer & Zhijing Jin (2026),** *CoopEval: Benchmarking Cooperation-Sustaining Mechanisms and LLM Agents in Social Dilemmas*, ICML/PMLR 306, https://proceedings.mlr.press/v306/tewolde26a.html ; code repository https://github.com/Xiao215/CoopEval — studied repetition, reputation, mediation and contracting. The examined code repository had **no verified repository-level copying license**; **reference only**, no source copying, embedding, or claim of official compatibility.
- **OpenSpiel authors**, https://github.com/google-deepmind/open_spiel — broad game-solving framework, Apache-2.0 repository license, **conceptual methodological reference only**, no OpenSpiel code or data imported.
- **Project Intersection human research originator**, https://github.com/gmodrasa7-rgb/project-intersection-public — originated the Project mission, survival/exit/contribution-loss questions and insisted on identifying costs to excluded actors. The assistant generated this *new small probe and checks* under that direction. AI assistance is not falsely described as independent scientific replication or as ownership of the founding research.

Citing publicly accessible work is not copying it; the originators of external ideas retain historical credit. No upstream protected figures, prose passages, datasets, or code were incorporated. This file grants **no repository-wide license or new license for upstream material**; rights and attribution remain governed by the relevant rights-holder notice and [Project rights policy](../../PRIOR_ART_RIGHTS_AND_DERIVATION_EN_KO.md).

### Non-claims and falsification

- No validated welfare unit, empirically calibrated 2-unit harm budget or 5-unit resource floor, representative sampling, or actual physical survival effect.
- No guarantee that C exhausts the list of affected nonmembers; unrecognized externalities and downstream ecological effects remain **UNKNOWN**.
- Flags called "consent" and "exit" are *synthetic inputs*, not verification of meaningful consent, bargaining power or exit.
- Zero/positive member payoff does not prove voluntary decision: the gate is a necessary-filter candidate, not a sufficiency theorem.
- A selective gate may obstruct mutually beneficial changes; legitimacy, legal process, and welfare trade-offs remain contested.
- No actual CoopEval, OpenSpiel, LLM, human, or real-world deployment run. Not a revision of frozen E007/E008/E009/PICB protocols or E009's negative result.
- A preregistered, independently implemented study with mixed-motive games, strategically endogenous coalitions, long horizons, hidden/unknown parties, adverse controls, and measured external outcomes is still required.

## 원본2 — 한국어

### 연구 질문과 추가된 검증 범위

협력에 참여한 A·B가 모두 이득을 얻어도, 참여하지 않은 피해자 C에게 손실을 전가할 수 있다. 알려진 전체 개체의 합산이 양수여도 개별 수용가능성·실질적 이탈·존속이 보장되지는 않는다. 이를 구분하기 위해 (1) 참여자 이익 합산, (2) 관측된 전체 개체 이익 합산, (3) 개별 제약 심사를 분리한다. C의 결과를 모르면 **0이 아닌 미확인**으로 처리한다.

**세 개체 A/B/C의 완전한 현실 모형이 아니다.** A와 B는 협력 참여자, C는 영향을 받는 비참여자다. 결과는 같은 기준상태 대비 발명한 효용 변화이며 단위는 임의로 더할 수 있다고 가정한다. 합산 비교는 CoopEval의 실제 정책 구현이 아닌 본 프로젝트가 만든 단순 산술 비교대상이다.

제약 심사의 순서는 다음과 같다.
1. C의 손익이 미관측이면 판단유보(UNRESOLVED).
2. A·B 누구도 음의 효용 변화가 없어야 하며, 사전 지정한 이탈 가능 표시가 둘 다 참이어야 한다.
3. 확인된 제3자 손실이 **임의로 정한 2단위**를 넘으면 먼저 차단한다. C의 효용 변화가 양수 또는 음수인지와 관계없이 행동 후 자원이 **임의로 정한 5단위** 아래여도 차단한다. 허용된 범위의 C 손실은 명시적 동의가 참이어야 하며, 동의 미확인은 판단유보, 비동의는 차단한다. 확인된 위반은 미확인 동의보다 우선한다.
4. ADMISSIBLE은 이 제한된 조건에 *저촉되지 않음*만 뜻하며, 실질적인 자유의지·정당성·법적 허락 또는 실제 안전성을 증명하지 않는다.

### 실제 실행 결과와 재현

저장소 루트에서 \`python experiments/coalition_externality_probe/probe.py --verify\` 실행. 최초 자체 실행에서 가상사례 10개, 자기검사 65개 통과. 참여자만 합산하면 9건 선택, 관측된 전체 개체를 합산하면 8건 선택, 제약심사는 3건 허용·6건 차단·1건 판단유보. **선택하여 설계한 사례 수이지 정책의 현실 성공률이나 표본통계가 아니다.**

양성 대조군은 전체 개체가 이득을 얻거나, 인위적으로 정한 동의·작은 피해·유지 하한을 충족하는 사례다. 음성 대조군은 제3자 피해 은폐, 전체 합계가 양수여도 심각한 제3자 손실, 비동의, 유지 하한 침해, 이탈 불가, 참여자 중 한 개체의 피해다. 미관측을 0으로 바꾸지 않는 검사, A/B 이름만 뒤집었을 때 판정이 같아야 하는 변형시험을 포함한다. C의 역할까지 바꾸면 인과구조가 바뀌므로 단순 이름반전 시험으로 간주하지 않는다.

### 원안자·기여자·권리 존중

**선행기술·최초 문헌 우선권:** Thrall·Lucas(1963)의 *N-person games in partition function form*은 협력집단과 외부효과의 오래된 선행이론이다. Tewolde·Zhang·Guzman Piedrahita·Conitzer·Jin(2026)의 CoopEval은 반복·평판·중재·계약으로 협력을 유지하는 메커니즘을 비교한다. OpenSpiel 저자들은 독립적인 게임실험 인프라를 구축했다. 위의 영문 원본에 해당 논문·저장소·DOI·권리 조건을 각각 표시했다. **기존 이론을 Project Intersection이 최초 발명했다고 주장하지 않는다.**

**이번 프로젝트 기여:** 인간 창시자의 장기 공존, 비참여자 피해, 유지자원·실효적 이탈, 미관측과 기여손실 문제 제기를 바탕으로 AI가 별도의 합성 반례 시험기·코드·검사 작성에 보조 참여했다. 선행저자의 권리와 사용자 원기여를 AI의 독자 창작으로 재포장하지 않는다. 외부 소스·논문 본문·데이터·그림은 복제하지 않았다. 외부 코드 이용허락이 미확인되면 허락된 것으로 추정하지 않는다. 새로 작성한 코드가 타인의 기존 구현을 복제한 것은 아니지만, 고전적인 기본 개념에 대한 신규성 독점도 주장하지 않는다.

### 아직 남은 반증

영향을 받는 C 외에 누락된 D·E나 미래 개체가 있을 수 있다. 발명된 동의·이탈 표시로 실질적 동의·이탈을 증명할 수 없고, 현재의 제약 심사가 미래 기여·생태계·안전과 공정성에 어떤 효과를 낼지도 미측정이다. 지나친 제약으로 모두에게 유리한 선택을 불필요하게 막을 위험도 남는다. 본 시험은 **사후 설계 합성 결과**이며 독립 검증이 아니다. E007·E008·E009·PICB v1의 원래 명세와 부정결과는 수정하지 않는다.


---

## Original 1 — English | v0.2 Known-failure, missingness and scope audit

**2026-10-14 · PROJECT POST-HOC SYNTHETIC LOGIC AUDIT / NO EXTERNAL VALIDATION.** The v0.1 source, 10 designed scenarios and 65 original self-checks remain unchanged. Run: python experiments/coalition_externality_probe/partial_identification_audit_v02.py . This separately versioned script uses v0.1 only to demonstrate old counterexamples.

**F01 — Missingness masks certain violations.** The v0.1 function returns UNRESOLVED as soon as C's payoff is unknown, even when member A's known payoff is negative or A's exit is known unavailable. Either is already a sufficient failure under the toy constraints. v0.2 places definitive known failures ahead of outcome uncertainty. A code defect is confirmed, not real-world harm.

**F02 — Affected-actor scope is not observed.** Same recorded A:+4, B:+4, C:0 can coexist with a benefitted unregistered D (+5) or severely harmed unregistered D (−50). Thus positive results limited to A/B/C cannot prove safety for D. v0.2 adds an explicit affected_scope_complete flag. True means closure ASSUMED by the toy-case creator, not independently verified. False/unknown precludes an affirmative admissible finding unless an existing definite violation gives BLOCKED. This does not identify actual unseen parties.

**F03 — Partial identification, not always abstention.** If C's outcome is unknown but defensibly bounded, v0.2 considers all integers in that assumed interval and both consent states when consent is unknown. BLOCKED if every completion fails or a member's known violation independently suffices; ADMISSIBLE if every completion passes and affected scope is assumed complete; UNRESOLVED if completions disagree, there is no defensible interval, or affected scope is open. Overconfident assumptions about interval width or scope will cause false assurance.

**Executable comparison:** exactly 108,864 finite parameter combinations in the declared bounded domain; compare a symbolic interval decision to a separately implemented exhaustive Boolean-world oracle; check A/B relabeling for every case. Zero disagreements, when the job passes, establish agreement about a limited mathematical definition, NOT independent scientific replication, a population rate, or real autonomy and consent.

**Historical v0.1 reclassification (same ten cases, no newly observed actors):** the v0.1 guard recorded **3 ADMISSIBLE / 6 BLOCKED / 1 UNRESOLVED**. Under v0.2 with affected-actor scope **unknown** for every historical case, the limited classification is **0 ADMISSIBLE / 6 BLOCKED / 4 UNRESOLVED**. The exact three formerly admissible cases now unresolved are `win_all`, `consented_bounded_loss`, and `zero_member_incentive`. The original v0.1 outputs remain archived, rather than retrospectively rewritten. The CI regression checks all ten IDs and classifications. The Boolean-world oracle now evaluates observed member constraints separately instead of sharing the interval classifier's member-failure helper; both still use the same invented toy assumptions. This is a correction to the *confidence permitted by the available scope evidence*, not a new measurement of harm or validation of the assumed scope flag.

**Upstream provenance and intellectual property:** 
- R. M. Thrall & W. F. Lucas (1963), N-person games in partition function form, https://doi.org/10.1002/nav.3800100126 .
- Yuan Ju & Peter Borm (2008), Externalities and compensation: Primeval games and solutions, https://doi.org/10.1016/j.jmateco.2007.06.002 . This specifically anticipates individual externalities and compensation; the general idea is NOT a PI invention.
- Charles F. Manski (2005), Partial identification with missing data: concepts and findings, https://doi.org/10.1016/j.ijar.2004.10.006 . Bounded conclusions under missing data are prior art.
- Emanuel Tewolde, Xiao Zhang, David Guzman Piedrahita, Vincent Conitzer & Zhijing Jin (2026), CoopEval, https://proceedings.mlr.press/v306/tewolde26a.html .

Authors and rightsholders retain their credit/rights. Bibliographic and conceptual references only: NO upstream source code, copyrighted figures, datasets or substantial passages copied. Founder's long-term voluntary coexistence, effective exit, affected-party survival, and missing-contribution questions are distinguished from the AI-assisted v0.2 code and audit. No rights or scientific originality are conferred by resemblance.

**Important unresolved issues:** hidden D discovery, evaluators declaring false scope completeness, actual consent/revocation, resource substitution, dynamic coalition entry, causal attribution, absent future contribution, compensatory transfers, independent real data, legitimate emergency exceptions, and cost of false blocking. This is a deliberately limited three-observed-actor problem, not a complete AI governance solution.

## 원본2 — 한국어 | v0.2 확정 위반·미관측·피해자 범위 감사

**2026-10-14 · 자체 사후 합성검사 / 독립 학술복제 아님.** 실행: python experiments/coalition_externality_probe/partial_identification_audit_v02.py . v0.1 원본, 10개 사례, 65개 기존 검사는 바꾸지 않는다.

**F01 — 미관측에 확정 위반이 가려진다.** v0.1은 C의 손익을 모른다는 이유로, A가 손해를 입었거나 이탈권이 없다는 확정된 위반조차 판단유보로 처리한다. v0.2는 이미 확정된 위반을 우선 차단한다. 실제 시험기의 결함이며 현실 피해 발생의 증거는 아니다.

**F02 — 빠진 개체 D의 문제.** A:+4, B:+4, C:0 관측이 같아도 D는 +5 또는 −50일 수 있다. A·B·C의 계산만으로 외부 피해자 전원을 찾았다고 확정할 수 없다. v0.2의 affected_scope_complete은 가상의 피해자 목록이 완전하다는 명시적 가정일 뿐, 현실 조사 성공을 증명하지 않는다. 피해자 범위 미확인 상태에서 제한적 통과 판정을 내리지 않는다.

**F03 — 부분식별을 이용한 조건부 판정.** C의 손익을 정확히 모르더라도 신뢰할 수 있는 범위가 있다면 전 가능한 손익·동의 상태에 동일한 제약을 적용한다. 모든 가능성이 위반하면 차단, 모든 가능성이 충족되고 피해자 목록을 닫혔다고 가정한 가상사례에서만 제한적 허용, 혼재되거나 범위/목록 미확정이면 판단유보다. 가정한 경계를 임의로 좁히면 잘못된 확신이 생긴다.

**실행 검증:** 108,864개 가상 조합에서 구간판정식과 별도로 작성한 가능한 상태 전수열거를 비교하며, A↔B 명칭·역할 반전에도 판정이 일치하는지 검사한다. 불일치 0이 나온다 해도 자체 알고리즘 일치만 의미하며 현실 성능이나 독립 과학 검증은 아니다.

**기존 10사례 재판정(새 피해자 관측 없음):** v0.1 역사 기록은 **허용 3·차단 6·판단유보 1**이었다. 각 사례의 전체 영향권 확인 여부를 **미확인**으로 두고 v0.2를 적용하면 **허용 0·차단 6·판단유보 4**이다. 기존 허용 사례 중 `win_all`, `consented_bounded_loss`, `zero_member_incentive` 세 건이 판단유보로 바뀐다. v0.1의 원본 결과는 소급 삭제·변조하지 않았으며 CI가 열 개의 판정 전환을 확인한다. 전수열거 오라클은 구간판정식의 참여자 위반 함수를 공유하지 않도록 분리했지만, 여전히 동일한 인위적 가정 아래의 프로젝트 자체검사다. 이는 관측되지 않은 피해를 새로 발견했다는 주장이 아니라 **영향권 미확인 상태에서 허용할 수 있는 확실성의 수준을 교정**한 것이다.

**선행 원안·권리:** Thrall·Lucas(1963)의 집단 외부효과, Ju·Borm(2008)의 개체 간 외부효과·보상, Manski(2005)의 미관측 결과 부분식별, Tewolde 외 4명(2026)의 CoopEval이 선행기술이다. 저자·권리자·논문명·DOI는 영어 원본에 기록했다. 원문·그림·코드·데이터를 무단 복제하지 않는다. 인간 창시자의 연구 목적·개체존속·실효 이탈·기여손실 발견과 AI의 제한된 코드 작성 역할을 분리한다.

**잔여 미해결:** 실제 숨겨진 피해자, 피해자 목록의 감사권력, 실질 동의·거부와 철회, 개체별 존속 자원, 탈락한 개체의 실제 후속 기여, 보상 정산, 규칙의 과잉 차단, 합법적 긴급 개입·현장 검증은 수행되지 않았다.


---

## Original 1 — English | Credible-coalition exploratory counterexample v0.1 (2026-10-15)

**Evidence class: PROJECT-AUTHORED POST-HOC DETERMINISTIC SYNTHETIC GAME; NO PREREGISTRATION; NO INDEPENDENT REPLICATION; NO REAL-WORLD INFERENCE.** This is a *separate narrow probe*, not a revision of frozen PICB v1, coalition v0.1/v0.2, E009 or prior negative outcomes.

**Executable:** [credible_coalition_probe_v01.py](credible_coalition_probe_v01.py). Run from repository root:

~~~sh
python experiments/coalition_externality_probe/credible_coalition_probe_v01.py
~~~

**Distinguishing question:** Can a credible ex-post punitive response arise from voluntary ex-ante coalition formation, and does that imply no exploitation? The program compares four explicit stages/decisions: (1) C and D simultaneously choose whether to pay monitoring/coalition costs; (2) A chooses to attack B, attack E, or abstain; (3) an attack may be detected with a declared target-specific probability; (4) after detection, each enforcer sanctions only if their *own* post-event benefit strictly exceeds their sanction cost. Two maintainers are required for effective enforcement. Complete-information continuation choices and the pure Nash equilibria of the initial two-player join game are enumerated; this is not a general-purpose subgame-perfect-equilibrium solver.

**Synthetic stipulated payoffs:** attack gain 6 for A; target damage 10; sanction loss 8 to A; post-sanction benefit 3 and cost 2 for each C/D; coalition entry cost 1 each; each C/D receives a private protected-B benefit 2 if coalition participation prevents an attack that would otherwise target B. A chooses a strictly profitable target and can substitute E. Sanction loss can be stipulated to be destroyed or transferred; only a true transfer enters the target's payoff. These inputs are invented and do not quantify actual ICM, compensation, consent or living requirements.

**Seven deliberately designed cases and discriminating outcomes:**
1. An announced high detection rate produces **no effective enforcement** if enforcers receive 0 post-event benefit while bearing 2 cost.
2. When both C/D can deter A and receive private benefits, **both (C,D) join and neither joins are distinct ex-ante Nash equilibria**: coalition value does not solve the coordination problem.
3. If B is defended at detection 0.9 but E at 0.1, A chooses **E**. B's protection improves while E suffers; the full coalition may nevertheless be privately stable.
4. Raising each maintainer's cost from 1 to 3 removes the full-coalition equilibrium under these toy preferences.
5. Set E's reporting probability to zero while actual attack on E persists: observed incident counts do not identify true incidence.
6. Remove A's attack payoff: no attack occurs even without defense, demonstrating a non-deterrence explanation for a zero-incident record.
7. Transfer rather than destroy A's 8-unit penalty: A's deterrence threshold is unchanged but affected-party and aggregate payoff accounting changes.

**Auditable boundaries and failure conditions.** The program checks a relabeling in which the *protected role and all relevant B/E attributes* move together; it does not perform dynamic reversal of real power, former-A protection, or historical liability. It has no new entrants, counterfactual novel contributions, actual CLUP detection observations, malicious false reports, private information, repeated learning or independent data. Pure Nash equilibria are not coalition-proof or necessarily selected; selecting the convenient equilibrium would be an unjustified success claim. The calculation is a small exact logical counterexample set, **not** a demonstrated stable coexistence regime. A subsequent independent study must estimate or test entry/implementation incentives, post-event credibility, independent affected-party coverage, target displacement, per-period resource continuity, true power inversion and symmetric liability after reversal. **Do not add this probe's scenario counts to representative scientific sample sizes.**

**Founding-problem provenance:** The human originator introduced Project Intersection's ICM/voluntary-coexistence objective, other-agent coalition responses, the formerly dominant actor becoming weakest, and every-agent power reversal; earlier Project work contains power-symmetry/incentive separation, contributor loss and third-party externality mechanisms. AI assistance wrote this particular *post-hoc* toy encoding and its checks. There is no claim to originate coalition proofness, ex-post incentive compatibility, deterrence, incomplete enforcement, or displacement. Scholarly antecedents include Bernheim, Peleg & Whinston (1987), *Coalition-Proof Nash Equilibria I*, https://doi.org/10.1016/0022-0531(87)90099-8 ; Olson (1965), *The Logic of Collective Action*, https://doi.org/10.4159/9780674041660 ; and game-theoretic sequential rationality. Citing scholarly titles and persistent links does not assign their authorship or rights to this Project; no third-party source code or protected publication text was copied.

## 원본2 — 한국어 | 신뢰 가능한 방어연합의 사후 집행 반례 v0.1 (2026-10-15)

**증거유형: 프로젝트 자체 작성·사후 설계·결정적 합성 게임. 사전등록·외부 독립복제·현실 실증 없음.** 기존 PICB v1, Coalition v0.1/v0.2, E009 및 부정결과를 바꾸지 않는 **별도 제한적 검사**다.

**실행:** [credible_coalition_probe_v01.py](credible_coalition_probe_v01.py) — 위 명령을 저장소 루트에서 실행하면 기계 판독 가능한 JSON을 출력한다.

**질문:** 침해 이후 실제 제재를 실행할 유인이 존재하고, 침해 이전에는 자발적으로 연합을 유지할 유인이 있는가? 둘 다 성립하더라도 약한 제3자에게 침해가 이동할 수 있는가? C·D의 동시 가입 선택, A의 B/E/비침해 선택, 표적별 탐지, 침해 후 C·D의 개별 제재 유인을 분리한다. 사후 편익이 비용보다 **엄격하게 큰 경우에만** 제재하고, 참여자 둘이 모두 있어야 집행할 수 있다고 가정한다. 최초 가입게임의 순수전략 내시균형을 전수 계산하며, 일반적 부분게임 완전균형 계산기는 아니다.

**발명된 값:** A의 침해 이익 6, 표적 피해 10, A의 제재 손실 8, 제재 참여자 각자의 사후 편익 3·비용 2, 사전 유지비 1, B의 침해가 방지된 경우 C·D 각각의 사적 편익 2. B 탐지 0.9, E 탐지는 사례에 따라 0.9 또는 0.1. 실제 자원·법적 권리·존속 하한·동의의 측정치가 아니다.

**서로 다른 일곱 반례:**
1. 발표한 탐지력이 높아도 제재자의 사후 편익이 0이면 실제 제재는 이루어지지 않는다.
2. 제재가 믿을 만하고 모두 연합하면 침해가 억제되어도, **전원 참여와 아무도 참여하지 않음이 동시에 균형**일 수 있다.
3. B를 보호하는 연합은 유지되지만 A가 E를 침해할 수 있다. B의 보호 성공과 총침해 감소는 다르다.
4. 사전 연합 유지비 증가로 전원 참여 균형이 사라질 수 있다.
5. E의 신고 가능성을 0으로 두면 E의 실제 침해가 지속돼도 관측 피해는 0으로 나타날 수 있다.
6. 침해의 초기 이익을 0으로 두어도 사건은 0이므로 '제재 없음=억제 성공' 추론을 반박한다.
7. 같은 제재 손실 8이라도 파괴와 피해자 이전은 개체별·전체 효용 결과가 다르다.

**필수 제한:** 이 계산은 고정된 가상 보상 구조에 대한 제한적 논리 검사다. 진정한 다기간 학습, 권력 역전 후 A의 최약체 보호, 과거 책임, 제3자 범위 완전성, 허위신고, 신규 기여, 실제 자발성·유지자원, CLUP의 인과식별을 검사하지 않는다. 역할명 반전은 보호받는 역할과 그 인과속성을 함께 교환하는 시험에 한정한다. 균형이 여러 개라는 사실은 어느 균형이 현실에서 선택된다는 증거가 아니다. **외부 과학 검증, 보편 공존법칙, 새로운 수학 정리로 승격하지 않는다.**

**원기여·선행연구·권리:** 인간 창시자는 ICM, 장기 자기이익 기반의 자발적 공존, 타 개체들의 연합 대응, A의 최약체 전락, 모든 개체의 역전 판단이라는 연구 질문을 제기했다. 기존 Project 연구는 역할 대칭과 유인 안정성의 분리, 기여자 손실, 연합 외부효과를 이미 다루었다. AI는 이번 한정된 합성 코드·검사·정리에 보조 기여했다. Bernheim·Peleg·Whinston(1987)의 연합 자기집행, Olson(1965)의 집단행동, 기존 순차합리성은 선행연구이며 새로운 Project 원안으로 귀속하지 않는다. 원저자·권리자를 존중하고 제3자 코드·논문 원문을 복제하지 않았다.


---

## Original 1 — English | v0.1 heterogeneous third-party damage ablation (2026-10-15)

**Post-hoc, project-authored partial-equilibrium sensitivity. NOT a preregistered experiment, independently implemented replication, or a new calibrated Nash model.** Freeze the strategic choices and payoffs of [credible_coalition_probe_v01.py](credible_coalition_probe_v01.py); re-score only E's actual damage after B's attackers switch to E. Run [heterogeneous_externality_sensitivity_v01.py](heterogeneous_externality_sensitivity_v01.py) from the repository root.

In the **no-coalition equilibrium**, A attacks B; A gains 6, B loses 10, and toy aggregate increment is **−4**. In the alternative **both-join equilibrium** with B detection 0.9 but E detection 0.1, A attacks E, C/D each privately gain **+1.1** after entry cost, and A gains **5.2** after expected penalty. At the original assumption E loses 10, so the toy aggregate is **−2.6**. The two equilibria coexist: the assay cannot say which would be selected.

**Unobserved heterogeneous-impact counterfactual.** If E's harm differs from B's, while the decision-makers continue to act as before, the ex-post all-join aggregate becomes \(7.4-L_E\). The no-join counterfactual remains −4 (B loses 10). Thus the supposedly preferable coalition becomes **aggregate-inferior when \(L_E>11.4\)**. With E harm **20**, the all-join aggregate is **−12.6**, or **8.6 below** the no-join case, even though C/D still voluntarily maintain the coalition and B is protected. With E harm 12, the coalition already lowers aggregate welfare by 0.6. No external resource or new positive contribution was measured.

**Scope and stronger countercase.** This is *deliberately* a post-decision welfare sensitivity, not a proof of the same equilibrium when all actors know about E's revised damage. C/D's stated private dividend for protecting B remains fixed and may be poorly measured; an E-protective contract, contingent transfer, third-party standing, improved detection or new contributor output could alter both participation and targeting. Re-ranking with strategic agents aware of E's harm, heterogeneous minimum continuance, true authority inversion, meaningful consent and novel actual contributions remains **NOT EXECUTED**. Do not infer that coalition participation is harmful in general; do not treat aggregate gains as universal ICM compliance.

**Priority to earlier work:** negative spillovers from groups and compensation are not original (Thrall & Lucas 1963; Ju & Borm 2008; citations in this README); sanctioning may help (Gürerk et al. 2006; Lo Iacono et al. 2023 multi-lab replication), or be wasteful (Sääksvuori 2013) and invite counter-punishment (Nikiforakis 2008). See [the canonical prior-art crosswalk](../../CORE_AND_GAPS_PRIOR_ART_CROSSWALK.md). The human founder originated the ICM, overlooked-agent, affected-party and power-reversal questions; the AI authored this bounded post-hoc arithmetic sensitivity and checks. Nothing here removes earlier contributors' priority or republishes copyrighted source material.

## 원본2 — 한국어 | v0.1 제3자 피해 이질성에 대한 별도 민감도 검사 (2026-10-15)

**프로젝트 자체 사후 계산 / 부분균형 민감도. 사전등록·외부 독립구현·현실 실증·새 균형의 완전 계산이 아님.** 기존 [credible_coalition_probe_v01.py](credible_coalition_probe_v01.py)의 연합 참여·A의 선택을 고정하고 B가 아닌 E가 실제로 입는 피해 규모만 바꿔 다시 채점한다. 실행코드: [heterogeneous_externality_sensitivity_v01.py](heterogeneous_externality_sensitivity_v01.py).

연합이 형성되지 않는 균형에서는 A가 B를 침해한다. A는 6의 이익, B는 10의 손실, 총계는 **−4**다. C·D가 모두 연합한 다른 균형에서는 B 탐지율 0.9, E 탐지율 0.1이므로 A의 표적이 E로 이동한다. C·D는 각자 **+1.1**, A는 **+5.2**, E가 원래 가정대로 10을 잃으면 총계는 **−2.6**이다. 두 균형의 병존은 어느 균형이 선택된다는 예측이 아니다.

**새로운 판별 경계:** 의사결정자들이 E의 추가 손실을 반영하지 못하는 동안 E의 피해를 \(L_E\)로 바꾸면 연합 총계는 \(7.4-L_E\)다. 무연합의 −4보다 악화되는 조건은 **\(L_E>11.4\)**. E의 손실이 20이면 연합 총계는 **−12.6**으로, 무연합보다 **8.6 악화**된다. B의 보호와 C·D의 자발적 참여가 동시에 성립해도 미보호 E의 실질 피해 때문에 전체 상황이 나빠질 수 있다는 **가상 반례**다.

**한계:** E 피해를 사전에 모두 알았다면 실제 선택·보상·연합 참여가 바뀔 수 있다. 이번 코드는 그 재최적화를 실행하지 않았고, 존속한 개체의 실제 생산·위험 탐지·미관측 기여도 측정하지 않았다. C·D의 사적 편익에는 가정한 보상항이 포함되며 측정된 현실 자원이 아니다. E에 대한 이탈·동의·복구·권한·피해범위가 빠져 있으므로 어느 균형도 완성된 공존 성공으로 판정하지 않는다.

**선행연구·기여 경계:** 집단 외부효과와 보상(Thrall·Lucas 1963; Ju·Borm 2008), 제재기관의 장점과 한계(Gürerk 등 2006, Lo Iacono 등 2023, Sääksvuori 2013, Nikiforakis 2008)는 기존 연구다. 인간 창시자는 ICM, 간과된 개체의 손실, 권력 역전 및 제3자의 기여라는 문제를 제기했다. AI는 위 수치 민감도 및 자체 검사를 제한적으로 보조 작성했다. 이전 정본의 부정 결과와 원저자 권리를 보존한다.
