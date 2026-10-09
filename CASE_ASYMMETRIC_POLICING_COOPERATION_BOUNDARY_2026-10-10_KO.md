# 비대칭적 치안이 협력을 안정화하는 경계조건

- 기록일: 2026-10-10
- 상태: `MATERIAL_COUNTEREXAMPLE / MEASUREMENT_DELTA / NOT_PROJECT_REPLICATION`
- 목적: 권력·제재 능력의 집중이 언제 착취가 아니라 갈등 억제와 협력 안정화로 이어지는지, 그리고 언제 그 이익이 단일 실패점·종속·숨은 부담으로 뒤집히는지 구별한다.
- 상위 판정: 새 1차 causal kernel은 아니다. 기존 K1 `DEPENDENCE–POWER`, K2 `POSITIVE-FEEDBACK–LOCK-IN`, K6 `COUNTERFACTUAL EXTINCTION` 및 경쟁가설 M6 `VOLUNTARY_SPECIALIZATION / DELEGATION`의 방향성을 좁히는 강한 반례와 측정 개선이다. `PRIOR_ART_FIRST_ORDER_SATURATED` 상태는 유지한다.

## 1. strongest counterexample

단순 명제 `POWER_ASYMMETRY -> EXPLOITATION`은 두 외부 실험계보와 양립하지 않는다.

1. Flack et al.은 한 대형 포획 돼지꼬리마카크 집단에서 소수 개체가 드물게 수행하던 policing 기능을 선택적 제거하는 knockout 실험을 실시했다. policing 부재 시 grooming·play·proximity·contact-sitting 네트워크의 평균 연결도와 reach가 줄고, clustering과 assortativity가 증가해 사회적 자원망이 더 작고 덜 다양하며 덜 통합된 방향으로 변했다. 이는 고권력 조정자의 제거가 약자의 독립성을 자동 회복시키는 것이 아니라 공동체의 협력 기반을 약화시킬 수도 있다는 직접 반례다.
2. Baldassarri & Grossman은 우간다 50개 생산자 협동조합의 농민 1,543명을 대상으로 중앙 monitor를 둔 public-goods field experiment를 수행했다. baseline 대비 무작위 monitor 조건의 기여는 평균 15.0%, 선출 monitor 조건은 25.4% 높았고, 선출 monitor 조건은 무작위 monitor보다 평균 9% 높았다. 실제 제재 이전 round 3에서도 차이가 나타났으며, 저자들은 이를 제재 기대와 선출 절차가 만든 정당성의 효과로 해석했다.

따라서 비대칭의 방향은 권력량 하나가 아니라 적어도 다음 조절변수에 의존한다.

- conflict-management 기능의 실제 수행
- 권한 취득 절차(`elected/consented` 대 `assigned/arbitrary`)
- 제재자의 국지 정보와 대상과의 거리
- 제재 오류·편향과 부담 분포
- 교체·회수·이탈 가능성
- 조정자 제거 후 네트워크 회복성과 대체 가능성

## 2. 원출처·귀속·lineage

| 계보 | 원안자·연도 | 실제 관측 | DOI/공식 링크 | 자금·이해상충 | 독립성·한계 |
|---|---|---|---|---|---|
| L-A 영장류 perturbation | Jessica C. Flack, Michelle Girvan, Frans B. M. de Waal, David C. Krakauer, 2006 | 소수 policing 개체의 선택적 제거 전후 사회망 구조 변화 | [Nature, 10.1038/nature04326](https://doi.org/10.1038/nature04326) | Packard, McDonnell, Wenner-Gren, Proteus, NSF, NIH 지원; 논문은 경쟁적 금전 이해관계 없음 보고 | 단일 포획 집단·종 특이성·policer 제거가 policing 외 기능도 함께 제거할 가능성. 낮은 서열 암컷 제거 통제가 있으나 장기 일반화와 복지는 별도 미검증 |
| L-B 인간 lab-in-the-field | Delia Baldassarri, Guy Grossman, 2011 | baseline/무작위 monitor/선출 monitor 비교; 50개 협동조합, 총 1,543명 | [PNAS, 10.1073/pnas.1105456108](https://doi.org/10.1073/pnas.1105456108) | NSF SES(IOS)-0924778, Princeton Institute 지원; 저자들은 conflict 없음 보고 | 게임 기여가 장기 복지·자율성·공존과 동일하지 않음. APEP로 형성된 협동조합 표본, 단기 6-round 설계, 선출 monitor의 관측되지 않은 속성 가능성을 완전히 배제하지 못함 |

L-A와 L-B는 연구팀·종·측정·데이터가 달라 상호 독립적인 보완 계보다. 그러나 같은 프로토콜의 재현도 아니고 Project Intersection의 독립재현도 아니다. 두 결과의 일치만으로 인간 조직 전반이나 AI-agent governance에 외삽하지 않는다.

## 3. 사실 / 해석 / 미검증 가정 분리

### 사실로 기록

- L-A: selective-removal 조건에서 보고된 사회망 지표가 policing 존재 조건보다 약화됐다.
- L-B: 중앙 monitor 조건과 선출 monitor 조건에서 게임 기여가 비교 조건보다 높았다.
- L-B: 선출/무작위 monitor는 유사한 수의 참여자를 제재했고, 실제 제재 전에 기여 차이가 관측됐다.

### 저자 해석

- L-A: policing이 사회적 niche의 robustness mechanism으로 작동한다.
- L-B: 선출 절차가 권위의 정당성을 높여 협력을 촉진한다.

### 미검증 또는 남은 가정

- 높은 게임 기여가 참여자의 장기 자기이익·독립성·복지 증가를 뜻한다.
- policing 이익이 장기간의 권력 고착·제재 편향·exit cost 증가보다 크다.
- 선출이 recall, contestability, practical exit까지 보장한다.
- 한 종·한 집단의 network knockout 효과가 이질적 지능체·조직에 그대로 유지된다.

## 4. Project claim 변화

판정: `MODIFY / SCOPE NARROWING`.

- 유지: `POWER_ASYMMETRY != EXPLOITATION` 및 `STRUCTURAL_EXPOSURE != CAUSAL_EFFECT`.
- 추가 경계: 높은 권력집중과 높은 협력은 동시에 관측될 수 있다. 따라서 협력량만으로 착취 부재를 판정하지 않는다.
- M6 확장: 자발적 분업뿐 아니라 `legitimate/functional centralized enforcement`를 경쟁가설로 명시한다.
- K1/K6 연결: 기능적 조정자가 필수화되면 단기 협력 이익과 장기 종속·단일 실패점이 동시에 증가할 수 있다. `cooperation benefit != independence preservation`.
- Project 고유 잔차: 기존 연구가 중앙 제재·정당성·policing 제거 효과를 제공하므로 이 개념 자체는 Project 고유 기여가 아니다. 남는 기여 후보는 동일 프레임에서 협력 이익, 부담 비대칭, practical exit, 대체 가능성, 제거 후 회복을 함께 측정하는 구별 설계다.

## 5. 최소 구별검사

### 고정 측정변수

1. `authority_acquisition`: 선출/동의/무작위 배정/자기지정
2. `contestability`: recall·교체·이의제기 가능성과 실제 비용
3. `sanction_error_distribution`: false positive/negative 및 집단별 부담
4. `cooperation`: 기여·갈등 빈도뿐 아니라 장기 유지
5. `network_integration`: mean degree, clustering, reach, assortativity
6. `replacement_recovery`: 핵심 조정자 제거 후 기능 대체·회복 시간
7. `exit_and_autonomy`: 이탈 가능성, 독립 실행 가능성, 재진입/복구 비용
8. `burden_share`: 조정 비용·감시 비용·오류 비용을 누가 반복 부담하는가

### 경쟁가설 판별

- 중앙화 직후, 실제 제재 전에 협력이 오르고 선출/동의 조건에서 증가폭이 더 크면 `legitimacy/expectation` 설명이 강화된다.
- 핵심 조정자 제거 시 통합도가 하락하지만 독립적으로 선발한 대체자가 같은 기능을 회복하면 `functional policing` 설명이 강화되고 개인 고유성 설명은 약해진다.
- 협력은 오르지만 특정 집단의 제재 오류·exit cost·복구 부담이 함께 커지면 `aggregate cooperation masking exploitation` 설명이 강화된다.
- recall·교체 가능성을 높여도 협력과 네트워크 통합이 유지되면 `indispensable concentrated power` 설명은 약해진다.
- 낮은 서열 또는 비policing 개체 제거에서도 같은 변화가 나타나면 policing 특이적 인과해석은 약해진다.

새 실험을 만들기 전, 공개 원자료가 확보될 경우 위 변수로 재분석 가능한지 우선 확인한다. 원자료 미확보는 효과 부재로 기록하지 않는다.

## 6. 역할반전과 반복구조 판정

- 이 구조가 반복되면 단기적으로 더 강해지는 주체: monitor/policer, 중앙 조정기구, 조정에 의존하는 집단 전체의 협력 능력.
- 반복적으로 더 소모될 수 있는 주체: 제재 오류를 많이 받는 하위 집단, 이탈권이 약한 구성원, 조정자 부재를 복구해야 하는 집단.
- 역할반전 검사: 현재 제재 대상이 monitor가 되었을 때도 같은 규칙·정보·recall 제약을 수용하는가. 현재 monitor가 피감시자가 되었을 때 이의제기와 독립 복구가 실질적으로 가능한가.
- 결론: 기능적 비대칭은 착취의 반례가 될 수 있지만, 그 반례는 `cooperation` 하나로 닫히지 않는다. 정당성·대체 가능성·오류 부담·exit·recovery를 함께 통과해야 장기 공존 조건으로 승격한다.

## 7. 현재 결정상태

- scientific delta: `STRONG_COUNTEREXAMPLE + DISCRIMINATING_MEASUREMENT`
- new first-order edge: `NO`
- independent Project replication: `NO`
- claim action: `MODIFY`
- saturation: `PRIOR_ART_FIRST_ORDER_SATURATED` 유지
- next decisive observation: 선출/동의와 recall·교체 가능성을 분리하고, 조정자 제거·대체 후 협력과 독립성 지표가 함께 회복되는지 보는 frozen comparison


## 8. 역전 경계: 제재자의 사적 수익이 협력 신호를 훼손할 때

- 판정일: 2026-10-10
- scientific delta: `EDGE REVERSAL + NEW DISCRIMINATING VARIABLES`
- 원출처: Raihan Alam & Tage S. Rai (2025), “Profitable third-party punishment destabilizes cooperation,” *Proceedings of the National Academy of Sciences* 122(34), e2508479122. [DOI 10.1073/pnas.2508479122](https://doi.org/10.1073/pnas.2508479122)
- 귀속: 제3자 처벌자의 profit motive가 처벌의 사회적·도덕적 신호를 약화시켜 협력을 떨어뜨린다는 실험적 연결은 Alam과 Rai의 기여다. Project 고유 발명으로 세지 않는다.

### 실제 관측

저자들은 9개의 경제게임·판단실험 중 4개를 사전등록했다.

- Experiment 1(`N=950`): 처벌자가 처벌할 때 bonus를 받는 조건은 무처벌 조건보다 초기 협력 선택을 낮췄다(`β=-0.39, p=.03`). 무급 처벌자 조건은 무처벌 조건과 유의한 차이가 없었다.
- Experiment 2(`N=668`, 12 rounds): 무급 처벌자는 직전 무처벌 round 대비 협력을 안정화했지만(`p=.54`), 유급 처벌자 조건에서는 협력이 감소했다(`β=-1.81, p<.001`). 이 감소는 실제 처벌을 경험하기 전부터 나타났다.
- Experiment 3(`N=994`): 이기적 선택은 항상 처벌하고 공정한 선택은 전혀 처벌하지 않는 최적 feedback을 8 rounds 제공해도 유급/무급 조건의 협력 격차가 수렴하지 않았다.
- Experiment 4(`N=1,011`): 공정한 선택을 처벌하는 antisocial punishment를 구조적으로 불가능하게 만들자 유급 처벌의 파괴효과가 완화됐다. 즉 실제 처벌 정확도만이 아니라 `공정행동도 처벌될 수 있는가`라는 가능성 자체가 구별변수다.
- 사전등록 internal meta-analysis(Experiments 1–4): `N=3,099`, 12,395 decisions에서 유급 처벌자 조건의 협력 가능성이 낮았다(`β=-1.62, SE=.13, z=-12.92, p<.001`).
- Experiment 6(`N=399`, 사전등록): 수혜자 다수는 유급·강한 처벌자를 선택했고, 무처벌자를 택했을 때보다 예상 보상이 약 20% 낮아지는 선택을 했다. 이는 제도 선택자의 단순합리모형 `더 많은 처벌 -> 더 많은 협력`이 자기이익에도 실패할 수 있음을 보인다.
- Experiment 9(`N=403`, 사전등록): 유급 처벌 조건에서는 게임 목적을 공정성보다 자기수익 극대화로 보는 비율이 더 높았다(72% 대 53%).

### 독립성·신뢰도·한계

- 무작위 조건배정, 반복·일회성 설계, 사전등록 4건, 공개 익명화 원자료·처리자료·코드·결과·일부 사전등록 OSF가 장점이다.
- 9개 실험은 같은 두 저자와 동일 연구프로그램의 internal lineage다. 실험 수를 독립재현 9건으로 세지 않는다.
- 온라인 경제게임의 binary sharing은 실제 사법·감사·AI evaluator 환경의 장기 공존·복구·독립성을 직접 측정하지 않는다.
- 저자들은 competing interest 없음으로 보고했다. 본문 acknowledgement에는 별도 외부 funding 문구가 확인되지 않았으므로 sponsor-control은 `UNKNOWN/NOT REPORTED`로 둔다.
- 메커니즘 `profit motive -> 신호 훼손 -> 규범의 자기이익 재해석 -> 협력 감소` 중 협력 감소와 규범 인식 변화는 실험 관측이지만, 장기 현실제도에 대한 전체 인과연쇄는 아직 외삽이다.
- Project Intersection의 독립재현은 아니다.

### claim 재수정

직전의 `legitimate/functional centralized enforcement` 경쟁가설에 다음 필요조건을 추가한다.

```
CENTRALIZED_ENFORCEMENT_EFFECT
  is conditional on
  punisher_private_return
  × antisocial_punishment_feasibility
  × perceived_normative_purpose
  × beneficiary_forecast_error
  × contestability/replacement/exit
```

- `MORE/STRONGER PUNISHMENT != MORE COOPERATION`.
- 처벌자가 처벌량으로 사적 보상을 얻으면 올바른 처벌 feedback을 제공해도 협력 저하가 지속될 수 있다.
- 처벌 정확도만 높이는 것은 충분조건이 아니다. 공정행동에 대한 처벌 가능성을 구조적으로 제거하고 그 제약을 대상에게 신뢰 가능하게 보여야 한다.
- 제도 수혜자가 스스로 유급·강한 처벌을 선택해도 `VOLUNTARY CHOICE != INFORMED LONG-TERM SELF-INTEREST`다.
- 따라서 SAIA 또는 중앙 evaluator의 행동을 판정할 때 위치뿐 아니라 `marginal_private_return_per_adverse_action`과 그 수익구조의 공개·검증 가능성을 별도 측정한다.
- 이 연결은 K1 `DEPENDENCE–POWER`, K3 `ENDOGENOUS-OBSERVATION`, K4 `METRIC–CONTROL FEEDBACK`, K5 `SUPPRESSION–APPARENT CONSENSUS`로 흡수 가능하므로 새 first-order kernel은 열지 않는다.

### 역할반전과 반복구조

- 반복될수록 더 강해지는 주체: 처벌·감사·적발 건수에서 수익을 얻는 evaluator/enforcer, 그 지표를 소유한 중앙기관.
- 더 소모되는 주체: 처벌 대상뿐 아니라 협력 증가를 기대하고 그 제도를 선택·비용부담한 수혜자. 실험에서는 이들이 자기 예상보상을 약 20% 줄였다.
- 역할반전 검사: evaluator가 피평가자가 되어도 `행위 건수당 평가자 수익`, 공정행동 오제재 가능성, 이의제기 비용을 같은 조건으로 수용하는가.
- 결론: 제재 존재와 제재 독립성은 분리해야 한다. 제재자의 사적 한계수익이 양(+)이면 협력 보호장치가 평가권·수익의 자기강화 장치로 역전될 수 있다.

### 다음 frozen 검사

최소 `2 × 2` 비교를 사전고정한다.

1. 제재자 사적수익: `paid / unpaid`
2. 공정행동 오제재 가능성: `possible / structurally impossible`

동시에 다음을 blind로 기록한다.

- 협력 선택과 장기 유지
- 실제 prosocial/antisocial punishment
- 처벌자 의도에 대한 신뢰
- 규범 목적 인식(`fairness / profit maximization`)
- 수혜자의 제도 선택과 선택 전 예상효과
- 선택 후 실제 보상·후회·switch/exit
- evaluator 수익과 대상 손실의 반복 누적

유급 조건의 협력 저하가 독립팀·현실제도 자료에서도 재현되고, 오제재 불가능성과 수익분리를 통해 회복되면 `profit-linked enforcement reversal`을 Project의 현실 경계조건으로 승격한다. 미재현은 부재가 아니라 해당 모집단·기간·제도경계에서의 negative result로 남긴다.
