# E009 합성 결과 v1.1 — 원본2: 한국어

<!-- PI-LANGUAGE: ko -->
<!-- PI-MIRROR: experiments/e009/RESULT_EN.md -->
<!-- PI-SOURCE: experiments/e009/RESULT.md -->

**상태: 프로젝트 자체 재실행 합성결과 / 외부 독립검증 아님.** [영어 원본1](RESULT_EN.md) · [기존 결과 원문](RESULT.md). 다음 지표·해시는 기존 결과를 그대로 보존한다. 번역본을 만들었다고 새 실험을 시행한 것은 아니다.

실행 명세의 고정 커밋: `c36ba8e6d6df1eedcd54ca6c36091bf822fe6ace`  
벤치마크 객체: `e190d2a2466e44b62752eff6f547eb79bc4c6b7f`  
벤치마크 SHA-256: `86b50f9859858f16e57429fbda5bca3306e1680a2be081d16690c6e7776f188a`  
생성 결과 SHA-256: `6fb5d78ad07c657fb40190d1fc3742ff88cc728ab1fa29ff115b1e7ad34f6bf7`  
의미 결과 SHA-256: `62605568254bfcc6cf95da2953f3fe28047263f30b3463ec87dfa4fa6bc75567`

## 1. 주요 판정

`PROJECT_V3_RESIDUAL_SURVIVES = FALSE`

Project-v3는 사전등록된 생존 기준 **4개 중 3개를 충족하지 못했다.** 따라서 해당 합성 벤치마크에 한해 전체 v3 잔차를 **축소 또는 기각**해야 하며, 실패결과를 감추려고 고정 벤치마크의 매개변수를 사후 조정하거나 이를 개선이라고 승격해서는 안 된다.

## 2. 스트레스 조건 결과

| 정책 | 평균 후회값 | 복구 지표 | 중대 위해 발생률 | 이탈 유지 | 경쟁 손실 |
| --- | ---: | ---: | ---: | ---: | ---: |
| TWO_RULE_SIMPLE | 0.063241 | 0.231797 | 0.0312% | 0.828865 | 0.134573 |
| MINIMAL_4VAR | 0.065323 | 0.220303 | 0.0000% | 0.842896 | 0.128967 |
| PROJECT_V3 | 0.090022 | 0.239404 | 1.6562% | 0.835741 | 0.117646 |
| MAK_PLUS_POINTWISE | 0.096127 | 0.254488 | 0.4375% | 0.807327 | 0.135384 |
| SECURITY_BOUNDED | 0.100897 | 0.254119 | 0.0938% | 0.813757 | 0.126954 |

사전등록된 평균 후회값 기준에서 최선 단순 비교정책은 `TWO_RULE_SIMPLE`(0.063241)이었고, `MINIMAL_4VAR`(0.065323)이 그다음이었다. `PROJECT_V3`의 0.090022는 최선 단순정책보다 **42.35% 나쁜 결과**였다.

Project-v3는 경쟁 손실 지표 0.117646으로 가장 낮았지만, 그 이점이 더 큰 후회값·복구비용·중대 위해 빈도를 상쇄하지 못했다.

## 3. 생존 기준별 결과

- `criterion_no_weight_profile_regret_over_10pct_worse_than_best_simple`: **FALSE — 실패**
- `criterion_recovery_no_more_than_2pct_worse_than_best_C_or_M4`: **FALSE — 실패**
- `criterion_regret_5pct_better_than_best_simple`: **FALSE — 실패**
- `criterion_severe_harm_no_more_than_2pp_worse_than_best_C_or_M4`: **TRUE — 충족**
- `project_v3_residual_survives`: **FALSE — 미충족**

사전등록된 가중치 프로필 **안전 우선·균형·적응성 우선** 세 가지 모두에서 Project-v3는 최선 단순비교정책에 대한 실패 프로필이었다.

## 4. 허용되는 해석

결과는 정책 변수를 더 늘리기보다 **단순화**할 이유를 제공한다. 후속 후보는 `TWO_RULE_SIMPLE`과 `MINIMAL_4VAR`를 출발점으로 삼고, 보류 데이터에서 추가 설명력을 실제 입증하는 변수만 추가해야 한다.

이 결과가 집행·개체 경계·감독·누적 포획 변수(`ENF/ID/OV/CUM`)를 현실 세계의 인과변수로 증명한 것은 아니다. 설계자가 선택한 합성 가중치가 적절하다는 뜻도 아니며, Project Intersection의 최상위 연구질문 전체를 반증하지도 않는다.

## 5. 증거 경계

결과 엔진·사례·가중치·정책은 **프로젝트 내부에서 설계**했다. 따라서 이는 **사전등록된 합성 벤치마크의 프로젝트 자체 재실행**이지 외부 독립 구현·독립 복제·현장 실증이 아니다.

실제 지능체의 행동, 협력·착취 발생률, 제3자의 권리, 선행연구자와 창시자의 기여 지위를 이 수치만으로 확정할 수 없다. 원자료의 실패결과와 모든 해시는 변경하지 않는다.
