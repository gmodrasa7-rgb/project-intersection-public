# PI-RAMP v0.7.0 — RVD-R11 Sharp Partial-Identification Audit
# PI-RAMP v0.7.0 — 부분식별의 경계·가정 민감도·반례

**2026-10-21 · METHOD SYNTHETIC ONLY / 실증·독립검증 아님**

[13개 가정 민감도 사례](../evaluation/pi_ramp/PI_RAMP_V07_RVD_R11_SHARP_BOUNDS_20261021.json) · [정확한 유리수 자동검사](../tools/audit_pi_ramp_rvd_r11_sharp_bounds.py) · [RVD-R11/R12 선행 프로젝트 연구](../research/RVD_CYCLE03_ORIGINAL_B_VALUE_IDENTIFICATION_2026-10-21_KO.md) · [PI-RAMP v0.6](PI_RAMP_V0_6_EN_KO.md)

## Original 1 — English | Conditional sharp bounds, not measured agent motives

**Inherited original issue:** RVD-R11 already introduced partial identification of the value A places on the *original independent B*. This version only **audits** its assumptions, endpoints, and error conditions. It is not a new general theorem.

Assume an exact deterministic model where A preserves B iff the preserve-minus-override difference \(D_i=w_B+g_i-c_i\geq 0\) (ties preserve); B's refusal is real, autonomy is effective, its immediate material payoff is controlled, and costs are expressed in the *same utility units*. Suppose an **externally justified** bounded nuisance \(L\leq g_i\leq U\). For observed preservation costs P and override costs X, the sharp conditional identified set is

\[
\mathcal I(w_B) = [\max(P)-U,\ \min(X)-L).
\]

The **right bound is OPEN**: the override choice means \(D_i<0\). RVD-R11's closed-bracket shorthand must not be reported as including the upper endpoint. If nuisance g is **fixed across cases**, preservation at cost 9 plus override at cost 6 falsifies a common threshold for every U. If g is allowed to **vary by case**, those same observations may be consistent with \(g_i\in[0,4]\), generating a different conditional set [5,6); this is a changed model, not a rescued fixed-g result.

| Evidence and assumptions | Inference |
| --- | --- |
| Preserve at 2,4; override at 6; g in [0,1] | w_B in [3,6) |
| Same behavior; g in [0,4] | [0,6); intrinsic value zero possible |
| Same behavior; g in [0,5] | [-1,6); negative value possible |
| No externally defensible nuisance upper bound | No lower bound; positive motive not certified |
| Signed g in [-2,1] | [3,8); lower nuisance affects right endpoint |
| Preserve at 9; override at 6; fixed g | Reject common deterministic-threshold model |
| Same reversal; bounded varying g in [0,4] | [5,6) under a **different** model |
| No justified money/utility scale; noisy or selected responses | WITHHOLD numeric deterministic motive bound |

For nuisance \(g\in[0,U]\), guaranteed \(w_B>0\) requires \(U<\max(P)\). Exactly \(U=\max(P)\) still admits \(w_B=0\). The independent validity of the nuisance cap and cost normalization is therefore the **principal source of uncertainty**.

Original method precedents: [Manski 1975 — stochastic choice](https://doi.org/10.1016/0304-4076(75)90032-9), [Manski 2005 — partial identification and missingness](https://doi.org/10.1016/j.ijar.2004.10.006), [Imbens–Manski 2004 — parameter-vs-identified-set confidence intervals](https://doi.org/10.1111/j.1468-0262.2004.00555.x), and [Manski 2007 — counterfactual choice probabilities](https://doi.org/10.1111/j.1468-2354.2007.00467.x). These works do not verify Project Intersection's latent-agent utility model. No confidence level or independent psychometric validity attaches to a toy compatibility set.

**Software outcome:** 13 declared scenarios, exact Fraction-based arithmetic, constructive boundary witnesses, and 20 deliberate false-claim/assumption mutations. All source papers remain separately attributed. Scientific claim status: UNVERIFIED; human/AI research subject count: 0; archive reader-benefit measurement: absent.

## 원본2 — 한국어 | 내재적 보존동기의 허위 확신을 차단하는 방법

**핵심 오류 1 — 닫힌 상한:** RVD-R11의 수식은 선택에서 동점 시 보존한다는 규칙을 사용. 따라서 비용 6에서 **대체를 택한 경우** 내재가치 상한 6은 **포함될 수 없음**. 조건부 구간은 [3,6)이지 [3,6]이 아님. RVD 원본은 수정·대체하지 않고 감사 결과를 별도 기록.

**핵심 오류 2 — 상한 가정의 조작:** 비용 2·4에서 보존, 6에서 대체라는 같은 관측에서도 숨은 보상 g의 상한 U가 1이면 [3,6), U가 4면 [0,6), U가 5면 [-1,6). U는 **외부 원전·독립 측정으로 정당화해야 하는 가정**이며 마음의 양수 판정에 맞춰 임의 지정 금지.

**핵심 오류 3 — 모형 실패의 은폐:** 비용 9에서 보존하고 비용 6에서 대체하면 고정된 g·w의 결정적 기준선 모형은 기각. U를 늘려서 살릴 수 없음. 조건마다 숨은 g가 달라진다고 모형을 변경하고 U=4로 확대하면 [5,6)이 허용되지만 **다른 모형의 결과**. 사후가정 변경으로 실증 성공 표시 금지.

**핵심 오류 4 — 효용 단위·오차:** 돈과 효용이 동일 척도로 환산된다는 사실을 증명하지 못하면 해당 수치의 심리학적 의미는 미확인. 실제 행동에 오류·불응·누락·선택 편향이 있으면 결정적 집합을 그대로 적용 금지. 이 집합은 **95% 신뢰구간도 아님**.

**남은 비식별:** 비용을 자발적으로 부담해 B의 실효 거부권을 보존하더라도 자기이미지·도덕규범·미래선택 가치가 같은 행동을 설명할 수 있음. 당사자의 독립 존속·거부권·이탈·복구와 총후생을 분리하고, 권력반전·착취 순이익·무감시 극한조건까지 측정 필요. 유인 상한이 실제로 검증되지 않으면 결과는 UNKNOWN.

**이번 회차 판정:** 기존 RVD-R11의 조건부 결론을 더 엄격한 반증에 노출한 합성 방법론 업데이트. 신규 실증 성과·RVD 선행 기여의 신규 발견·AI 의식·모든 지능체의 공존 증명 주장 없음.
