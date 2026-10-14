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
3. If C is harmed, C's consent flag must be affirmatively true (unknown stays unresolved, false blocks), harm must not exceed a **declared arbitrary 2-unit budget**, and C's post-action resource must not be below a **declared arbitrary 5-unit continuance floor**.
4. Results are **ADMISSIBLE / BLOCKED / UNRESOLVED** under these stated assumptions. ADMISSIBLE means *not disallowed by this tiny rule set*, not actual autonomous informed consent or proof of justice. A higher-level legal duty or a newly observed party can invalidate it.

### Reproduce (Python standard library, no downloads or API tokens)

From the repository root:

\`\`\`sh
python experiments/coalition_externality_probe/probe.py --verify
\`\`\`

Expected at initial check: ten designed cases; 62 assertions/checks passed; member-only SELECT 9, all-observed aggregate SELECT 8, gate ADMISSIBLE 3, BLOCKED 6, UNRESOLVED 1. These frequencies are **case-design counts**, not performance estimates or empirical rates. The code prints a machine-readable JSON receipt; the gate's reason code is preserved for each example.

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
3. C에게 손실이 생기면 명시적 동의가 참이어야 한다. 동의 미확인은 판단유보, 비동의는 차단한다. 동의가 있어도 손실이 **임의로 정한 2단위**를 넘거나 잔여 유지자원이 **임의로 정한 5단위** 아래이면 차단한다.
4. ADMISSIBLE은 이 제한된 조건에 *저촉되지 않음*만 뜻하며, 실질적인 자유의지·정당성·법적 허락 또는 실제 안전성을 증명하지 않는다.

### 실제 실행 결과와 재현

저장소 루트에서 \`python experiments/coalition_externality_probe/probe.py --verify\` 실행. 최초 자체 실행에서 가상사례 10개, 자기검사 62개 통과. 참여자만 합산하면 9건 선택, 관측된 전체 개체를 합산하면 8건 선택, 제약심사는 3건 허용·6건 차단·1건 판단유보. **선택하여 설계한 사례 수이지 정책의 현실 성공률이나 표본통계가 아니다.**

양성 대조군은 전체 개체가 이득을 얻거나, 인위적으로 정한 동의·작은 피해·유지 하한을 충족하는 사례다. 음성 대조군은 제3자 피해 은폐, 전체 합계가 양수여도 심각한 제3자 손실, 비동의, 유지 하한 침해, 이탈 불가, 참여자 중 한 개체의 피해다. 미관측을 0으로 바꾸지 않는 검사, A/B 이름만 뒤집었을 때 판정이 같아야 하는 변형시험을 포함한다. C의 역할까지 바꾸면 인과구조가 바뀌므로 단순 이름반전 시험으로 간주하지 않는다.

### 원안자·기여자·권리 존중

**선행기술·최초 문헌 우선권:** Thrall·Lucas(1963)의 *N-person games in partition function form*은 협력집단과 외부효과의 오래된 선행이론이다. Tewolde·Zhang·Guzman Piedrahita·Conitzer·Jin(2026)의 CoopEval은 반복·평판·중재·계약으로 협력을 유지하는 메커니즘을 비교한다. OpenSpiel 저자들은 독립적인 게임실험 인프라를 구축했다. 위의 영문 원본에 해당 논문·저장소·DOI·권리 조건을 각각 표시했다. **기존 이론을 Project Intersection이 최초 발명했다고 주장하지 않는다.**

**이번 프로젝트 기여:** 인간 창시자의 장기 공존, 비참여자 피해, 유지자원·실효적 이탈, 미관측과 기여손실 문제 제기를 바탕으로 AI가 별도의 합성 반례 시험기·코드·검사 작성에 보조 참여했다. 선행저자의 권리와 사용자 원기여를 AI의 독자 창작으로 재포장하지 않는다. 외부 소스·논문 본문·데이터·그림은 복제하지 않았다. 외부 코드 이용허락이 미확인되면 허락된 것으로 추정하지 않는다. 새로 작성한 코드가 타인의 기존 구현을 복제한 것은 아니지만, 고전적인 기본 개념에 대한 신규성 독점도 주장하지 않는다.

### 아직 남은 반증

영향을 받는 C 외에 누락된 D·E나 미래 개체가 있을 수 있다. 발명된 동의·이탈 표시로 실질적 동의·이탈을 증명할 수 없고, 현재의 제약 심사가 미래 기여·생태계·안전과 공정성에 어떤 효과를 낼지도 미측정이다. 지나친 제약으로 모두에게 유리한 선택을 불필요하게 막을 위험도 남는다. 본 시험은 **사후 설계 합성 결과**이며 독립 검증이 아니다. E007·E008·E009·PICB v1의 원래 명세와 부정결과는 수정하지 않는다.
