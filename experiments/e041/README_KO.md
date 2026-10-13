# E041 — Practical Exit 독립 타깃 정보증분

상태: **프로젝트 합성 재실행 / 인과 해석 보류 / 현실 실증 미해결**  
**이 공개 대응본의 한국어 원본2 (2026-10-13).** 기존 내부 원본1 한국어의 역사적 우선권을 소급 변경하지 않는다.

## 질문

C002b의 더 좁은 주장만 시험한다. `practical exit` 측정이 그 변수를 정의에 포함하지 않은 미래 실패 타깃의 held-out 예측에 단순 baseline보다 추가 정보를 주는가?

이 실험은 인간·AI·기관에 대한 경험적 검증이 아니다. 생성기가 효과를 넣은 signal regime과 효과를 제거한 null regime을 함께 두어, 측정기가 양쪽을 구별할 수 있는지만 시험한다.

## 순환성 제거

타깃 `downstream_failure`는 practical-exit threshold나 voluntary-coexistence label로 정의하지 않는다. 별도의 Bernoulli outcome process에서 표본화한다.

Baseline 정보:
- realized-gain bin
- direct-harm bin
- task difficulty

후보 추가 정보:
- exit-vulnerability bin

signal regime에서는 exit vulnerability가 미래 실패확률에 추가 causal term을 가진다. null regime에서는 그 term을 정확히 0으로 둔다.

## 사전 판정

고정 seed `20260920`, n=60,000, 절반 train/절반 held-out test.

평가량은 Brier score 감소량:

`Delta = Brier_baseline - Brier_baseline+exit`

사전 조건:
- signal: `Delta >= 0.005`
- null: `abs(Delta) <= 0.002`

둘 다 만족하면 **KEEP as identification instrument**. signal이 실패하면 **KILL/MODIFY instrument**. null에서 큰 양의 개선이 나오면 leakage/overfit 가능성 때문에 **KILL/MODIFY instrument**.

## 해석 제한

성공해도 C002b의 현실 타당성을 입증하지 않는다. 성공이 의미하는 것은 오직 `타깃 정의에 exit를 넣지 않은 상태에서도, exit가 실제 outcome generator에 정보를 갖는 경우 이를 held-out에서 검출하고 null에서는 가짜 증분을 만들지 않는 최소 도구가 있다`는 것이다.

현실 claim을 전진시키려면 practical-exit scorer와 독립된 lineage에서 생성된 실제 downstream outcome 또는 외부 adjudication이 필요하다.

## 가장 강한 반례

현실의 독립 타깃에서 gains/harm/difficulty를 통제한 뒤 practical-exit 변수의 정보증분이 사라지거나, source-lineage를 분리하면 사라지거나, 측정비용을 맞추면 사라진다면 C002b는 해당 regime에서 NARROW/KILL한다.

## 2026-10-13 공개 교정: 관측자료가 같아도 개입효과가 다른 두 인과모형

기존 교정 계보는 **E025의 타깃 정의 누수 → E041의 별도 미래사건 타깃 → 남아 있는 인과 비식별성**이다. E025에서는 정답 라벨에 이탈 변수 자체를 넣었으므로 일부 유리한 결과가 구성상 자명했다. E041은 별도 Bernoulli 미래실패 사건을 생성하지만, 신호조건에 이탈효과를 *의도적으로 삽입*했다. 따라서 양의 Brier 증분은 합성 신호 검출기의 성능이며 현실 인과관계의 증거가 아니다. null 대조가 항상 유리한 결론을 내지 않도록 확인한다.

**강한 인과 반례:** [causal_twin.py](causal_twin.py)의 두 모형은 관측상 X=U를 설정한다. A는 관측 이탈취약성 X가 결과확률을 바꾸는 모형, B는 관측되지 않는 U가 X와 결과를 모두 만드는 모형이다. 관측한 행·조건부 확률·베르누이 라벨은 완전히 같다. 반면 do(X=0)과 do(X=2)의 실패위험 차이는 A에서 +0.24, B에서 0이다. 둘은 *인위적으로 만든 합성 구조*이며 현실 개입효과를 추정한 숫자가 아니다. **예측력·인과식별을 혼동하면 안 된다.**

공개 저장소의 최상위에서 실행:

```bash
python experiments/e041/model.py
python experiments/e041/causal_twin.py
python -m unittest discover -s experiments/e041 -p 'test_*.py' -v
```

6개 회귀검사는 기존 고정시드 수치, 신호·무신호 사전판정, 타깃 열을 예측 입력으로 쓰지 못하는 조건, 실행 재현성, 동일 관측행, 개입효과 분리를 확인한다. 결과: [RESULT.json](RESULT.json), [CAUSAL_TWIN_RESULT.json](CAUSAL_TWIN_RESULT.json).

실제 연구에는 독립 사건판정·출처분리·측정비용과 모델복잡도 통제·시간순서·교란변수·자연실험/개입 검증이 필요하다. 외부자료에서 추가 정보가 사라지면 C002b의 해당 범위 주장을 축소한다. 예측력 개선이 남아도 별도 인과식별 없이 원인이라고 주장하지 않는다. Brier 오차 감소는 보정(calibration) 개선만을 뜻하지 않는다([scikit-learn](https://scikit-learn.org/stable/modules/calibration.html)); [NIST AI RMF](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)도 독립검사와 불확실성 기록을 강조한다.

**공개 경계·기여:** 합성 자료만 다루며 실존 개체·기업의 자발성/피해를 판정하지 않는다. 인간 창시자의 문제선택·오류탐지·반례·교정노동을 AI 성과로 재포장하지 않는다. AI 보조 문서·코드는 외부 독립검증이 아니다. [라이선스 보류](LICENSE_STATUS.md); E007만의 한정 라이선스는 확대되지 않는다. [공통의존 경로 반례](../dependency_paths/README_KO.md). Brier·교란·인과모형의 일반 개념에 대한 독창성 주장은 하지 않는다.
