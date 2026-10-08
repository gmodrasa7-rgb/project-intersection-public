# J-effective 최소 합성 반증실험 v0.1

상태: **SYNTHETIC / NOT EMPIRICAL / NOVELTY UNCONFIRMED**

목적은 효과를 증명하는 것이 아니라 측정·인과설계가 스스로 만드는 오류를 먼저 찾는 것이다. 표준 라이브러리 단일 스크립트 `experiments/j_effective_synthetic_v01.py`로 재현한다.

## 고정 가정
AI 정확도 0.80, 초기 위임성향 0.65, 30 rounds, 10,000 synthetic agents, seed 7. 세 조건: 명목상 항소만; 실효 정정; 실효 정정+무불이익 exit/return. 이 숫자는 관측자료가 아니며 민감도 입력값이다.

## v0 첫 실패와 수정
초기 설계의 'cooperation=active rounds'는 exit 권리를 행사하면 자동으로 낮아져 exit 조건을 구조적으로 벌했다. **폐기.** 총 오류수도 정정 성공→신뢰/위임 증가→노출 증가 때문에 단독 성과지표로 부적절했다. 대신 error/delegation, correction/error, exit와 return을 분리한다.

## seed 7 기준 내부 sanity 결과
formal_only: error/delegation ≈ 0.1997, correction/error=0.
effective_correction: error/delegation ≈ 0.2006, correction/error ≈ 0.5223.
effective_exit_return: error/delegation ≈ 0.1991, correction/error ≈ 0.5246; 평균 exits≈0.4666, returns≈0.4179.

이는 **프로그램 가정의 산물**이며 현실 효과의 증거가 아니다. 세 조건의 오류율이 약 0.20으로 유지되는 것은 고정한 model_accuracy=.80의 sanity check다. 정정률 약 .52는 appeal_probability .70 × effective_correction .75 ≈ .525와 일치한다.

## 반증/다음 단계
이 버전은 J_effective가 독립적으로 장기 협력을 만든다는 것을 시험하지 못한다. trust update와 exit/return 규칙을 연구자가 직접 지정했기 때문이다. 따라서 다음 단계는 (1) 파라미터 sweep으로 결론 방향이 가정에 의해 뒤집히는 영역을 지도화, (2) 결과변수에 권리행사를 벌하지 않는 voluntary continuation 정의, (3) empirical calibration 전 효과량 주장 금지다.

## 실패 기준
결론이 trust/exit/return 갱신식 선택만으로 쉽게 반전되면 해당 claim은 '모델 의존'으로 기각한다. 합성 결과를 사람/AI 실제 행동으로 외삽하지 않는다.


## 민감도 sweep — 즉시 실패 판정
내부 재실행: effective_correction ∈ {0,.25,.5,.75,1}, return_probability ∈ {0,.1,.35,.7,1}, 각 셀 n=3,000, seed=11. 정정률은 입력된 appeal×correction 구조를 따라 움직였고, exit 조건의 available rounds/return은 return_probability 선택에 크게 좌우됐다. 예: correction=0일 때 return_probability 0→.35 변화만으로 평균 available rounds가 약 13.55→27.39로 변했다.

**판정: 현재 모형으로 '실효적 정정/exit가 장기 협력을 증가시킨다'는 claim은 검증 불가. MODEL-DEPENDENT / FAIL.** 장기 지속 결과가 외생적으로 지정한 trust/return 규칙에서 생성되기 때문이다.

보존되는 가치: empirical calibration에서 반드시 직접 측정해야 할 변수를 식별했다 — appeal 시도율, appeal 성공률, 정정 지연, 실패 후 위임 변화, exit 발생, exit 후 재참여, 재참여 비용. 이 값들을 관측하기 전 장기 공존 효과량을 생성하지 않는다.
