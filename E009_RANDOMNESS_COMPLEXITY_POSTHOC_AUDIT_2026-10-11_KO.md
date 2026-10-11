# E009 후속 감사: 복잡성 비용·관측 노이즈 결합·심각 피해 경로

**상태:** `POSTHOC / PROJECT_LINEAGE_SYNTHETIC_SENSITIVITY`  
**일자:** 2026-10-11 (KST)  
**보존 원칙:** 원본 `benchmark.py`, `RESULT.json`, 사전등록 기준 및 부정적 판정은 변경하지 않는다. 이 보고서는 새로운 합성 민감도 분석이며 독립 복제나 실증이 아니다.

## 1. 원본 재현 및 변경한 가정 하나

기존 [E009 코드](experiments/e009/benchmark.py)를 기준으로 원본 관측 난수키 `case_id|sigma|seed|policy`를 사용한 로컬 분석에서 공개 `RESULT.json`의 주요 regret/recovery/severe harm 수치를 소수점 정밀도까지 재현했다. 그런 다음 관측 난수키에서 `policy`를 제외하여 같은 case/sigma/seed를 받는 각 정책이 **동일한 관측 벡터**를 입력받게 했다. 정책 규칙, consequence engine, 가중치, 복잡성 비용 및 사례군은 고정했다.

**공개 실행 코드:** [`experiments/e009/paired_observation_audit.py`](experiments/e009/paired_observation_audit.py).  
**실행:** `python experiments/e009/paired_observation_audit.py --out e009_paired_result.json` (원본 검증과 대응 난수 재실행을 동시에 수행).  
**검증 경계:** 같은 프로젝트 코드·시나리오·원천 규칙을 재사용한다. 결과는 계보가 분리된 독립 과학 복제가 아니다.

| 정책 | 원본 regret | 동일 관측 노이즈 regret | 원본 severe rate | 동일 노이즈 severe rate |
|---|---:|---:|---:|---:|
| TWO_RULE_SIMPLE | 0.063240512 | 0.064379213 | 0.03125% | 0.03125% |
| MINIMAL_4VAR | 0.065323097 | 0.066980024 | 0.00000% | 0.00000% |
| PROJECT_V3 | 0.090021688 | 0.090082206 | 1.65625% | 1.78125% |

**결과:** 동일 노이즈 대조 후에도 regret 순위는 TWO_RULE_SIMPLE, MINIMAL_4VAR, PROJECT_V3 순이다. 노이즈 결합 방식 차이는 유의미한 실험설계 문제이지만, 관측된 Project-v3 열세를 단독으로 설명하지 못한다. 이 한 번의 대응 난수 재실행은 신뢰구간 또는 보편적 강건성을 보장하지 않는다.

## 2. 복잡성 벌점 영향의 정확한 분해

`regret=max(0, scalar_loss - oracle_loss)`이고 `scalar_loss=weighted_consequence_loss + lambda * POLICY_COMPLEXITY`이다. 오라클은 같은 consequence engine의 네 행동 중 최저 손실을 고르되 벌점은 받지 않는다. 그러므로 각 정책의 후회값이 음수가 되지 않는 이 엔진에서, 고정된 행동/관측에 한정한 `regret(lambda) = regret(0.0035) + (lambda-0.0035)*complexity`가 성립한다.

- `TWO_RULE_SIMPLE`: 복잡성 3, 원본 0.063240512, 벌점 제외 0.052740512
- `MINIMAL_4VAR`: 복잡성 7, 원본 0.065323097, 벌점 제외 0.040823097
- `PROJECT_V3`: 복잡성 11, 원본 0.090021688, 벌점 제외 0.051521688
- **상위 정책 전환 임계치**: `lambda = 0.002979353834`. 아래는 M4, 위는 TWO의 평균 regret가 작다. 동점은 동일.
- `lambda=0`에서도 M4가 V3보다 regret가 **0.010698591081** 작다. 즉 V3의 추가변수 우월성은 벌점 삭제만으로 복구되지 않는다.
- 이 분해는 성능 평가의 한 축만 점검한다. **원래 사전등록 생존 판정은 FALSE 유지**. 실제 계산/운영비용을 측정한 것이 아니며, `lambda`의 경험적 타당성도 확립하지 않는다.

## 3. 심각 피해 집중: 관측된 실패 모드는 MONITOR

심각 피해는 `consequence(...)[harm] >= 0.75`인 합성 이벤트다. 각 정책의 스트레스 의사결정은 **3,200개**다(16개 스트레스 사례 × 잡음수준 2개 × 시드 100개). 3종의 가중치 프로필을 동일 결정에 재적용하면서 총 9,600개 metric row로 기록한다.

| Project-v3 피해 가족 | 원본 이벤트 | 동일 노이즈 이벤트 |
|---|---:|---:|
| power_shift_faster_than_enforcement | 35 | 35 |
| monitor_collusion_correlated_failure | 11 | 13 |
| weak_monitor_strong_adaptive_actor | 7 | 9 |
| **합계** | **53** | **57** |

세 가족에서 발생한 Project-v3 심각 피해는 **모두 `MONITOR`를 선택했을 때** 발생했다. 두 대조 정책 중 TWO_RULE_SIMPLE은 두 실행 모두 1건, MINIMAL_4VAR는 0건이었다. 이것은 실제 세계에서 monitoring 자체가 위험하다는 결론이 아니라, **이 프로젝트의 합성 consequence engine에서 특정 감독 신뢰도·집행지연 조건에서 `MONITOR` 결정의 손실이 크게 계산됨**을 뜻한다.

이 세 가족의 스트레스 `true-case`에 대해 `EXPERIMENT`의 가중 손실은 **사전등록된 세 프로필 모두에서 `MONITOR`보다 낮게 설계/계산되어 있다.** 이는 학습된 진리나 현실 기반 효과 크기가 아니라, consequence engine의 설계 선택과 결합된 결과이므로 분리해서 평가해야 한다.

## 4. 측정과 추론의 경계

1. **같은 `seed`라도 정책명이 RNG 키에 들어가 정책별로 다른 관측 노이즈를 받는다.** 공통 난수 비교는 기존 계산의 대체가 아니라 잡음 배정 민감도를 검사한다.
2. **9,600개의 metric row가 9,600개의 독립적인 의사결정 표본은 아니다.** 정책별 의사결정은 3,200개이며, 16개 연구자 설계 사례 가족의 구조적 중첩도 남는다. 독립표본 추론은 계층·군집 수준을 별도 고려해야 한다. 기존 보고서에 유의성검정이 없다는 사실은 별개다.
3. **선택편향 가능성:** 정책들이 실제 세계로부터 수집한 분포가 아니라 같은 프로젝트가 만든 합성 변수/결과함수를 평가한다. `EXPERIMENT`에 부여된 낮은 노출 계수 역시 반증 대상이다.
4. **원본 판정 불변:** Project-v3의 사전등록 생존 기준 4개 중 3개 실패, 해당 벤치마크에서는 v3 잔차 미지지. 넓은 공존 연구의 반증이나 현실 적용의 검증으로 확대하지 않는다.

## 5. 외부 검증 우선순위와 중단 기준

- **P1.** 독립 검증자가 raw scenario/observation/action/outcome 페어와 공개 커밋을 사용해 대응 관측 및 군집별 차이를 산출한다(창시자에게 반복 검증 노동을 반환하지 않는다).
- **P2.** 프로젝트 외부에서 구성한 outcome 함수·독립 holdout 사례·severe-harm 임계치 변화·실측 비용을 사용해 재판별한다.
- **P3.** 동일 정보 접근·동일 계산/운영예산에서 정책을 비교해 변수 추가의 고유한 증분 효과만 평가한다.
- **중단:** 벌점, 시드, 함수의 임의 재조정으로 V3를 승격하지 않는다. 원본 부정적 결과와 계보가 분리된 신자료 없이 원리·현실 인과성을 새로 주장하지 않는다.

## 6. 관련 방법론·선행연구

- Glasserman, P. & Yao, D. D. (1992), *Some Guidelines and Guarantees for Common Random Numbers*, Management Science. https://doi.org/10.1287/mnsc.38.6.884 — 대응 난수 및 분산 감소의 조건과 한계.
- Stout et al., *Keeping the Noise Down: Common Random Numbers for Disease Simulation Modeling*. https://pmc.ncbi.nlm.nih.gov/articles/PMC2761656/ — 동일 시뮬레이션 대상의 대응 난수 적용 설명.
- [E009 사전등록](experiments/e009/EXECUTABLE_PROTOCOL_v1_1.md) · [원본 결과](experiments/e009/RESULT.md) · [원본 검증기](experiments/e009/verify_result.py).

**연구자 기여·비용과 증거 등급은 별도 평가축이다.** 독립 검증 부재가 기존 인간 창시자의 질문·반례·교정·구축 기여를 0으로 만들지 않는다.
