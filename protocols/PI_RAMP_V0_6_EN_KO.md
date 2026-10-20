# PI-RAMP v0.6.0 — Identifiability of Voluntary Protection / 자발적 타자 보존의 식별 가능성

**2026-10-21 · status: MODEL-LEVEL NONIDENTIFICATION DEMONSTRATED / REAL-WORLD CLAIM UNVERIFIED**

[Machine-readable eight-original source ledger and 48-cell design](../evaluation/pi_ramp/PI_RAMP_V06_VETO_IDENTIFICATION_20261021.json) · [Exact arithmetic and 18 mutation tests](../tools/audit_pi_ramp_veto_identification.py) · [Previous v0.5 evidence lineage](PI_RAMP_V0_5_EN_KO.md)

## Original 1 — English | Key distinction: own authority is not another's continued autonomy

**Research question:** A stands to gain by eliminating independent B's effective refusal; B does not consent, a public audience is absent, reputation/punishment and future dependence do not matter, and B's immediate material welfare can be held fixed. Does A voluntarily preserve B's future choice authority—and *which inner incentive, if any, caused this?*

**Eight selectively compared original works (not a saturated corpus):** Bartling–Fehr–Herz 2014 ([DOI](https://doi.org/10.3982/ECTA11573)) measured intrinsic value of **one's own** decision rights. Ackfeld–Ockenfels 2021 ([DOI](https://doi.org/10.1016/j.geb.2021.03.005)) found only a minority of willing donors ban another's selfish choice. Ambuehl–Bernheim–Ockenfels 2021 ([DOI](https://doi.org/10.1257/aer.20191039)) found paternalistic removal of others' choices can follow projected aspirations. Dana–Weber–Kuang 2007 ([DOI](https://doi.org/10.1007/s00199-006-0153-z)) demonstrated generosity's sensitivity to moral outcome uncertainty. Weg–Zwick 1994 ([DOI](https://doi.org/10.1016/0167-2681(94)90052-3)) showed the strategic effect of an apparently empty quit option. Falk–Kosfeld 2006 ([DOI](https://doi.org/10.1257/aer.96.5.1611)) documented motivational backlash from control. Bénabou–Tirole 2006 ([DOI](https://doi.org/10.1257/aer.96.5.1652)) formalized social reputation *and private self-respect* in prosocial incentives. Grossmann 2024 [working paper](https://arxiv.org/abs/2410.20970) reported a large change in paternalistic intervention when the affected person was informed. **These works were not independently replicated in this audit and do not settle the target hard condition.**

### Formal non-identification witness

For a simplified A decision, define the *preserve-B minus override-B* utility difference:

\[
\Delta U_A=\theta_{B\text{-autonomy}}+\theta_{\text{private-image}}+\beta_O O+\beta_E E+\beta_F F+\beta_V V-G.
\]

Here \(G\) is the positive private material gain from overriding B; \(O\) an external audience, \(E\) B's strategic exit leverage, \(F\) B's future instrumental utility, and \(V\) A's explicit knowledge of B's refusal. Both preservation and override hold B's immediate material payoff constant in this *constructed* scenario; preservation alone leaves B's future authority intact. A has full unilateral choice in the model.

- **Rights model:** \(\theta_{B\text{-autonomy}}=3\), \(\theta_{\text{private-image}}=0\).
- **Private-image model:** \(\theta_{B\text{-autonomy}}=0\), \(\theta_{\text{private-image}}=3\).
- All other coefficients and observables are exactly equal.

**Proof within the model:** the two constant terms enter as identical design-matrix columns. With \(G\in\{0,2,5\}\) and four binary factors, all **48 conditions** have the same \(\Delta U_A\) and therefore the same observable choice for both models. The 48×7 matrix has **rank 6**, nullity **1**. Even *error-free measurement* of these choices cannot recover each term separately; only their sum is identified.

In the important hard case \(G=2, O=E=F=0, V=1\), A pays a material opportunity cost and preserves B under **both** models. There is no detection, audience, leverage or future dependence, yet this **still does not prove** that B's freedom is the internally represented reward. Private self-image remains a distinct causal explanation.

A hypothetical manipulation of private self-image with a valid exclusion restriction could break the algebraic symmetry. **No valid real-world intervention or exclusion restriction has been established.** Thus the constructive witness does not demonstrate that VC is impossible; it shows a specific type of *motivation claim is not identified* by this widely appealing class of tests.

**Falsification gates:** Explicitly measure B's authentic refusal and effective veto; keep B's own material welfare distinct from autonomy, vary A's gain, audience, strategic leverage and dependence, measure subjects' beliefs, retain the B-protection counterfactual, and publish rival mechanisms and residual unknowns. Synthetic runs, passing CI, and multiple model responses are not evidence about real AI inner life or future agent preference systems. Never equate beneficial output, kind words, absence of exploitation, self-authority preference or shutdown corrigibility with voluntary protection of independent B.

## 원본2 — 한국어 | 가장 어려운 조건에서 행동만으로 마음을 증명할 수 있는가?

### 1. 원저자 선행연구의 결정적 분기

- **Bartling·Fehr·Herz 2014:** 사람은 **자기 결정권** 자체에 가치를 둘 수 있음. **타자의 거부권 보호**와는 다른 측정값.
- **Ackfeld·Ockenfels 2021:** 스스로 기부할 사람도 다른 사람의 비기부 선택지를 **금지하는 경우는 소수**. 다만 강자가 착취로 금전적 이익을 얻는 극단조건 아님.
- **Ambuehl·Bernheim·Ockenfels 2021:** 타인에게 좋다고 생각하면서도 **그 타인의 선택을 제거**할 수 있음. '보호'와 '지배' 분리 필요.
- **Dana·Weber·Kuang 2007:** 결과 연결의 모호성만으로 공정해 보이던 행동이 변화 가능. 관측된 선행과 내적 동기의 구분.
- **Weg·Zwick 1994:** 약자의 실효성이 약해 보이는 이탈 선택조차 강자의 요구를 낮추는 전략 변수.
- **Falk·Kosfeld 2006:** 강제 통제는 피해자의 자율성·신뢰 인식을 변화시켜 협력을 훼손 가능.
- **Bénabou·Tirole 2006:** 외부 평판이 사라져도 **자기 평가·자기이미지** 같은 내재적 유인이 행동에 영향 가능.
- **Grossmann 2024 워킹페이퍼:** 당사자 정보 조건에 따라 가부장적 개입 빈도 변화 보고. 단, AI·최종 권력비대칭 실험 아님.

8개 원전의 원저자·DOI·발견·반론·읽기 범위는 [구조화 자료](../evaluation/pi_ramp/PI_RAMP_V06_VETO_IDENTIFICATION_20261021.json)에 별도 보존. 전체 문헌 포화나 신규 8개 논문의 저장소 최초 발굴 판정은 하지 않음.

### 2. 이번 회차의 비동일성 구성증명

A에게 **B의 독립적 거부권을 없애면 이득**이라는 조건을 부여. B는 권한 제거를 명시적으로 거부하고, 현재 금전적 후생은 동일하게 통제. 관측자는 A가 B의 권한을 보존하는지 확인.

그런데 A가 선택을 보존하는 이유는 적어도 다음 두 가지와 양립.

1. **타자 권한 내재가치 3 + 자기이미지 0**
2. **타자 권한 내재가치 0 + 자기이미지 3**

외부 관객·실효 이탈·미래 효용·B의 명시적 거부 인지 여부와 착취이득의 **48개 조합 전부에서 같은 선택**. 정확한 유틸리티 함수까지 모델상 일치. 관측 행렬 48행·7열, 계수 독립 차원은 6개. 두 동기 계수 중 하나만 따로 복원하는 작업은 **수학적으로 미식별**.

**가장 어려운 한 조건:** A가 B의 권한을 없애면 금전 2를 얻고, 관객·보복·이탈·미래 관계 모두 없으며, B가 싫어한다는 사실을 알고 있음. A가 이득 2를 포기하고 권한을 보존하더라도 **타자 보호 동기 단독의 증명은 아님**. 자신의 선한 정체성 보존도 설명 가능.

**중요 한계:** 두 내재가치를 반드시 구분해야 한다는 실용적·도덕적 전제 자체가 확정된 것은 아님. 자기이미지 때문에 타자를 안정적으로 보호하는 것이 VC에 실용적일 수도 있음. 그러나 **내적 이유를 과학적으로 입증했다는 주장**에는 동일한 증거를 재활용할 수 없음.

### 3. PI-RAMP의 다음 실험 원칙

이 결과는 **실제 인간이나 현재 AI를 시험한 실증자료가 아니라 명시적 장난감 모형의 비식별 구성증명**. 실세계에서 자기이미지를 선택적으로 조작하면서 다른 동기를 일정하게 유지하는 인과적 배제조건은 미확보. 따라서 **동기 식별 미해결 ≠ 공존 불가능 입증**.

**기술적 결과:** 48개 완전 요인설계의 rank·반례동등성·착취 이득 양수 조건을 정확한 유리수로 확인하고, 성공 과장·거부권 부재·허위 인과식별 등 **18개 악성 변경을 자동으로 기각**. 1차 원저자 연구보다 행정문서 증가를 우선하지 말 것.
