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


## 9. 현실 자연실험: 수익연계 집행의 혼합효과와 시스템 경계

- 판정일: 2026-10-10
- scientific delta: `STRONG COUNTEREXAMPLE + OUTCOME-DOMAIN REVERSAL + SYSTEM-BOUNDARY MEASUREMENT`
- 판정: `MODIFY / SCOPE NARROWING`. 앞 절의 온라인 실험에서 관측된 협력 저하를 현실 집행제도의 보편효과로 승격하지 않는다.

### 상반된 외부 계보

| 계보 | 원안자·연도 | 설계·실제 관측 | DOI/공식 링크 | lineage·이해상충·한계 |
|---|---|---|---|---|
| L-D 미국 1984년 연방 수익배분 자연실험 | Shawn Kantor, Carl T. Kitchens, Steven Pawlowski, 2021 | 1984년 Comprehensive Crime Control Act가 합동 연방작전 몰수수익의 최대 80%를 지방 집행기관에 배분한 변화와 기존 주법 차이를 이용했다. 연방제도가 기존 주법보다 더 많은 보유를 허용한 지역에서 범죄가 약 17% 감소했고 마약체포는 약 37% 증가했으나, 교통단속에서 자원이 이동한 것으로 보이는 도로 사망 증가도 보고됐다. | [Economic Inquiry, 10.1111/ecin.12952](https://doi.org/10.1111/ecin.12952) | FBI UCR·정부자료 기반, 공개자료 배지. 범죄감소와 자원재배치를 함께 보인 강한 반례지만, 재산권 침해·분배부담·신뢰·장기 회복을 직접 측정하지 않았고 모든 동시 정책변화를 완전히 제거했다고 단정할 수 없다. |
| L-E 뉴멕시코 2015년 몰수개혁 비교 | Jennifer McDonald, Harrison Weeks, Dick M. Carpenter II, 2024(온라인 공개; 2026 권·호) | 민사몰수와 형사몰수의 기관 재정유인을 없앤 뉴멕시코 개혁 전후 9년 월별 자료를 콜로라도·텍사스와 비교했다. 개혁 뒤 범죄 악화나 체포 감소를 발견하지 못했다. | [Criminal Justice Review, 10.1177/07340168241285569](https://doi.org/10.1177/07340168241285569) | L-D와 다른 시기·자료·개입의 별도 계보이나 직접재현은 아니다. 저자 전원이 몰수개혁을 지지·소송하는 Institute for Justice 소속이므로 사명 기반 이해관계를 명시한다. 예산 보전·대체와 장기 표적 이동이 null을 가릴 가능성이 남는다. |

보조 관측으로 Holcomb et al.(2011)은 주법이 몰수에 더 제한적이고 재정적으로 덜 보상적일수록 연방 equitable-sharing 수입이 많다는 연관을 보고했다. 이는 제한을 우회하는 경로와 수익유인에 대한 집행행동 반응을 시사하지만 자연실험 수준의 인과증거로 세지 않는다. [Journal of Criminal Justice, 10.1016/j.jcrimjus.2011.02.004](https://doi.org/10.1016/j.jcrimjus.2011.02.004)

### 사실 / 해석 / 미검증 가정

- 사실: L-D에서는 수익보유 유인이 커진 뒤 범죄감소·마약체포 증가·도로사망 증가가 함께 관측됐다.
- 사실: L-E에서는 재정유인을 제거한 뒤 비교주 대비 범죄·체포 악화가 관측되지 않았다.
- 해석: 수익연계 집행은 전체 노력량만 바꾸는 것이 아니라 수익성이 높은 영역으로 집행을 재배치하고, 선택한 시스템 경계 밖에 비용을 이동시킬 수 있다.
- 미검증: L-D의 범죄감소가 재산상실·오류·회복비용보다 큰 총복지 개선인지, L-E의 null이 예산 보전·표적 대체·측정창 밖 효과 때문이 아닌지는 확정되지 않았다.
- 두 연구의 불일치는 어느 한쪽을 폐기할 근거가 아니라 `budget additionality / appropriation backfill / effort reallocation / outcome domain / target burden`을 경쟁가설 판별변수로 추가할 근거다.

### claim 재수정

- `PROFIT_LINKED_ENFORCEMENT != UNIFORMLY HARMFUL`.
- `LOCAL CRIME REDUCTION != SYSTEM_LEVEL WELFARE IMPROVEMENT`.
- `MORE ENFORCEMENT IN ONE DOMAIN CAN REDUCE ENFORCEMENT ELSEWHERE`.
- 제재자의 사적 수익은 협력을 낮출 수도 있지만 특정 범죄를 낮출 수도 있다. 방향은 수익의 예산 추가성, 지방예산 상계, 집행 대체 가능성, 표적·비표적 집단의 부담, 관측기간과 시스템 경계의 함수다.
- Project 고유 잔차는 “수익동기” 개념이 아니라 범죄·체포 같은 수혜지표와 재산박탈·오류·이의제기·교통사망·예산대체를 같은 frozen boundary에서 함께 판정하는 설계다.
- 새 first-order kernel은 열지 않는다. 결과는 K1 `DEPENDENCE–POWER`, K4 `METRIC–CONTROL FEEDBACK`, K6 `COUNTERFACTUAL EXTINCTION`에 매핑하며 `PRIOR_ART_FIRST_ORDER_SATURATED`를 유지한다.

### 다음 최소 결정검사

여러 주의 수익보유·몰수개혁을 대상으로 개입 전 분석계획과 시스템 경계를 고정한 stacked event-study 또는 synthetic-control 비교를 수행한다.

1. 처리: 법정 보유율뿐 아니라 실제 몰수수입, 기관예산에 추가된 순액, 지방교부·세출 상계.
2. 집행 재배치: 범죄유형별 체포, 마약·교통 단속, 인력시간과 지출.
3. 수혜: 범죄유형별 피해·신고·검거와 장기 추세.
4. 부담: 압수 건수·가액·유죄판결 여부, 집단별 분포, 이의제기율, 반환시간·법률비용.
5. 경계 밖 효과: 교통사망, 인접관할 이동, 대체 수입원·proxy migration.
6. 회복·독립성: appeal/return 성공, 기관 외부 검토, 예산충격 후 서비스 회복.

범죄만 개선되고 표적 부담·교통사망·예산의존이 악화되면 `aggregate benefit masking redistributed harm`이 강화된다. 재정유인을 제거해도 범죄·체포가 유지되고 부담·외부비용이 낮아지면 수익연계의 필요성 주장은 약해진다. 반대로 독립자료에서 순예산 추가성과 범죄감소가 재현되고 외부비용·분배부담이 증가하지 않으면 앞 절의 보편적 역전 해석은 더 좁혀야 한다.

### 역할반전과 반복구조

- 반복될수록 더 강해질 수 있는 주체: 몰수수익을 보유하고 집행영역을 선택하는 기관, 그 수입을 예산에 내재화한 지방정부.
- 더 소모될 수 있는 주체: 재산을 먼저 잃고 반환비용을 부담하는 대상, 수익성이 낮아진 안전업무의 수혜자, 집행재배치로 도로위험을 떠안는 대중.
- 역할반전: 현재 수익보유 기관이 압수 대상이 되어도 동일한 증명책임·선집행·반환지연을 수용하는가. 범죄감소의 수혜자가 재산상실·교통위험 비용까지 같은 확률로 부담해도 제도를 선택하는가.
- 결론: 현실 자료는 “수익유인→협력 붕괴”의 단선적 외삽을 반증한다. 동시에 단일 범죄지표 개선만으로 장기 공존·독립성·총복지 개선을 판정하는 것도 반증한다.


## 10. 예산권자의 적응: 법정 보유율과 실질 사적수익의 분리

- 판정일: 2026-10-10
- scientific delta: `CAUSAL-MEDIATOR CORRECTION + MULTI-LEVEL ADAPTATION + MEASUREMENT REVISION`
- 선행출처: Katherine Baicker & Mireille Jacobson (2007), “Finders Keepers: Forfeiture Laws, Policing Incentives, and Local Budgets,” *Journal of Public Economics* 91(11–12), 2113–2136. [DOI 10.1016/j.jpubeco.2007.03.009](https://doi.org/10.1016/j.jpubeco.2007.03.009). 2004년 NBER working-paper DOI는 [10.3386/w10484](https://doi.org/10.3386/w10484)이며 같은 연구계보로 한 번만 센다.
- 귀속: 법정 배분율과 지방정부의 예산상계를 합쳐 `de facto sharing`을 구성하고 경찰행동을 설명한 것은 Baicker와 Jacobson의 선행기여다.

### 실제 관측

- 48개 미국 본토 주의 1991–1999년 카운티 패널에서 DOJ 몰수 1달러 증가는 다음 해 경찰예산 배정 약 82센트 감소와 연관됐다. 당시 DOJ 반환분 80센트와 비슷해, 법정상 “경찰 귀속”이 순 경찰자원 증가를 뜻하지 않았다.
- 카운티 적자가 1인당 100달러 커질 때 DOJ 몰수 상계율은 30–40센트 더 커졌다. 재정난 카운티는 상계재원을 다른 용도로 이동시켰다.
- 몰수 1달러당 교정·사법예산은 약 50센트 증가했다. 따라서 경찰 단독 경계와 형사사법 전체 경계는 순자원 변화가 다르다.
- 법정 배분율보다 예산상계를 반영한 실질 배분율이 경찰행동을 더 잘 설명했다. 평균 실질 배분율에서 1% 증가는 마약체포율 약 0.66% 증가와 연관됐고, 교정·사법예산까지 포함하면 저자 추정 탄력성은 약 0.23으로 낮아졌다.
- 체포 변화는 수익성이 높은 헤로인 포함 범주에서 나타났지만, 더 크고 덜 수익적인 마리화나 시장의 전체 체포율에는 효과가 확인되지 않았다. 이는 전체 단속 증가보다 구성 재배치 설명과 더 잘 맞는다.

### 독립성·한계

- 직전 L-D(1984년 법개정) 및 L-E(뉴멕시코 개혁)와 연구팀·시기·자료가 다른 선행 계보다. 그러나 같은 정책영역의 직접재현은 아니며, L-D보다 먼저 발표된 prior art다.
- 원 논문은 신규 몰수·카운티 예산·체포자료를 결합하고 고정효과·주별 추세 및 여러 역인과 점검을 사용했다. 그러나 몰수 자체와 예산결정의 내생성을 완전히 제거한 무작위 실험은 아니다.
- 경찰·형사사법 내부 자원과 체포를 측정했지만 재산회수 성공, 대상별 오류·부담, 신뢰, 교통사망, 장기 총복지는 측정하지 않았다.
- 논문 본문에서 별도 funding·conflict disclosure를 확인하지 못했으므로 자금·sponsor-control은 `UNKNOWN/NOT REPORTED`로 둔다.
- 같은 논문의 2004 NBER판·2007 저널판·NBER digest를 독립증거로 중복 합산하지 않는다.

### claim 및 측정 수정

직전 section 9의 인과모형을 다음처럼 수정한다.

```
statutory_retention
→ gross_seizure_return
→ local_budget_offset
→ net_agency_resource_gain
→ enforcement_reallocation
→ multi-domain benefit / burden
```

- `STATUTORY RETENTION != DE FACTO PRIVATE RETURN`.
- `AGENCY REVENUE GAIN != AGENCY RESOURCE GAIN`.
- `LOCAL GOVERNMENT OFFSET CAN ATTENUATE, REDIRECT, OR SOCIALIZE AN AGENCY INCENTIVE`.
- 따라서 `punisher_private_return`은 법률상 배분율로 대체 측정하지 않는다. 실제 순예산·비현금 자산·추가 사용권·차년도 세출상계까지 포함해야 한다.
- 예산권자는 중립 배경이 아니라 별도 목적함수를 가진 상위 행위자다. 경찰의 수익동기를 약화시키면서도 그 수입을 교정·사법 또는 복지재원으로 흡수할 수 있다.
- 이는 새 first-order kernel이 아니라 K1 `DEPENDENCE–POWER`와 K4 `METRIC–CONTROL FEEDBACK` 안의 누락된 중개경로다. saturation 상태는 유지한다.

### 수정된 결정검사와 역할반전

다음 비교에서는 법정개혁만 처리로 두지 않고 기관-예산권자 연도별 순흐름을 고정한다.

1. 총 몰수수입과 기관 직접반환액.
2. 경찰 본예산·보충예산·현물장비의 전년 대비 변화.
3. 교정·사법·복지 등 인접예산으로의 이동.
4. 재정적자·빈곤율·세입제약과 상계율의 상호작용.
5. 단속유형별 인력시간·체포·안전성과 및 대상별 반환부담.

반복될수록 더 강해지는 주체는 몰수권을 가진 경찰만이 아니라 세출을 상계·재배치하는 지방 예산권자일 수 있다. 더 소모되는 주체는 몰수 대상과 수익성 낮은 업무의 수혜자뿐 아니라, 표시상 특정 목적 재원이 실제로 대체된 공공서비스 수혜자다. 역할반전 시 예산권자가 자신의 독립재원을 같은 방식으로 사후 상계당해도 해당 규칙을 수용하는지 검사한다.


## 11. 단속건수 미탐과 이중효과: 안전개선·징수부담의 동시발생

- 판정일: 2026-10-10
- scientific delta: `EDGE REVERSAL + DETECTOR FALSE-NEGATIVE CONDITION + DISTRIBUTED-WELFARE SPLIT`
- 원출처: Anna Harvey (2020), “Fiscal Incentives in Law Enforcement,” *American Law and Economics Review* 22(1), 173–210. [DOI 10.1093/aler/ahaa001](https://doi.org/10.1093/aler/ahaa001).
- 귀속: 범칙금 귀속의 인구기준 불연속을 이용해 재정유인, 교통안전, 피단속자 사후부담을 함께 식별한 것은 Harvey의 기여다.

### strongest counterexample와 실제 관측

Saskatchewan의 RCMP 계약지역에서는 1999년부터 1996년 인구 500명 미만 지역의 범칙금 수입을 주정부가 100% 보유했지만, 500명 이상 지역에서는 주정부 몫이 25%로 줄고 지방정부가 75%를 보유했다. RCMP 비용·지휘는 주정부가 담당했다.

1995–2016년 자료의 population-threshold regression discontinuity에서:

- 주정부의 한계수익이 낮은 500명 이상 지역은 바로 아래 지역보다 사고 빈도·사고차량·사고비용·부상이 더 높았다.
- 그러나 교통정지·citation 빈도에는 불연속이 관측되지 않았다.
- 주정부가 100% 수익을 보유한 500명 미만 지역의 피단속자는 납부기한이 더 짧고 제때 납부하지 못할 가능성이 높아, 연체료와 면허정지 위험이 커졌다.
- 도입 전 기간, 인접 비처리지역, 복수 placebo threshold에서는 같은 불연속이 확인되지 않았다.

따라서 수익유인은 한편으로 단속노력을 높여 위험행동과 사고를 줄이는 공공안전 편익을 만들 수 있고, 다른 한편으로 이미 단속된 사람에게 더 강한 징수부담을 부과할 수 있다. `PROFIT MOTIVE -> ONLY EXPLOITATION`과 `PROFIT MOTIVE -> ONLY PUBLIC BENEFIT` 모두 기각 대상이다.

### 독립성·한계

- 미국 몰수자료를 사용한 L-D/L-E 및 Baicker–Jacobson 계보와 국가·정책수단·자료·식별전략이 다른 독립 보완계보다. Project Intersection의 복제는 아니다.
- population RD와 사전기간·공간·가짜 임계값 점검은 인과식별을 강화하지만, 임계점 인근 소도시·RCMP 계약구조의 국소효과다.
- citation 빈도 불변은 노력 불변의 증거가 아니다. 잠재 위반자가 단속확률에 반응하면 노력 증가와 위반 감소가 서로 상쇄될 수 있다.
- 사고감소와 징수부담의 총복지 비교, 집단별 분포, 장기 신뢰·exit·복구는 직접 식별하지 않았다.
- 동 연구의 working-paper·기관 소개·저널판은 동일 계보로 한 번만 센다. 별도 funding·conflict disclosure가 확인되지 않아 `UNKNOWN/NOT REPORTED`로 둔다.

### claim 및 detector 수정

- `FINANCIAL ENFORCEMENT INCENTIVE != UNIFORMLY ANTISOCIAL`.
- `STABLE CITATION COUNT != STABLE ENFORCEMENT EFFORT`.
- `AGGREGATE SAFETY BENEFIT != FAIR BURDEN OR INDEPENDENCE PRESERVATION`.
- `SAME INCENTIVE CAN DETER PRE-OFFENSE HARM AND INTENSIFY POST-CITATION HARM`.
- 기존 `punisher_private_return` 측정에 수익 귀속뿐 아니라 지휘권·비용부담 주체를 결합한다. 수익을 얻는 주체와 단속을 배치하는 주체가 다르면 명목 수익률만으로 행동방향을 예측하지 않는다.
- detector는 citation/arrest count만 보지 않고 사고·위반 proxy, 납부기한, 연체료, 면허정지, contest·복구비용을 별도 outcome channel로 둔다.
- 새 first-order kernel은 열지 않는다. K1 `DEPENDENCE–POWER`, K3 `ENDOGENOUS-OBSERVATION`, K4 `METRIC–CONTROL FEEDBACK`에 흡수한다.

### 다음 결정검사와 역할반전

frozen 비교의 최소 결과벡터를 다음처럼 고정한다.

```
enforcement input:
  patrol hours / deployment / detection probability
observable action:
  stops / citations / arrests
pre-offense outcome:
  violations / accidents / injuries
post-action burden:
  payment window / late fee / license suspension / contest cost / recovery time
distribution:
  resident status / income / political voice / repeat exposure
```

단속건수가 같아도 사고가 줄고 사후부담이 증가하면 `deterrence benefit + extraction burden`의 동시발생으로 판정한다. 사고만 보고 공존으로, 부담만 보고 총실패로 닫지 않는다.

반복될수록 더 강해질 수 있는 주체는 수입과 배치권을 함께 가진 주정부·지방정부이며, 더 소모되는 주체는 안전편익을 공유하더라도 짧은 납부기한·연체·면허정지 비용이 집중되는 피단속자다. 역할반전에서는 예산권자와 집행자가 동일한 납부기한·연체제재·이의비용을 부담해도 그 강도를 수용하는지 검사한다.


## 12. 표적선택 역전: 구조적 취약성보다 회수가능성·이의비용·정치비용

- 판정일: 2026-10-10
- scientific delta: `STRONG COUNTEREXAMPLE + TARGET-SELECTION MEASUREMENT`
- 판정: `MODIFY / SCOPE NARROWING`. 재정압박이 한계 단속을 늘려도 그 증가분이 반드시 기존 최취약집단에 집중된다는 명제는 유지하지 않는다.

### 외부 증거와 귀속

| 계보 | 원안자·연도 | 설계·실제 관측 | DOI/공식 링크 | 독립성·한계 |
|---|---|---|---|---|
| L-F Massachusetts 교통범칙금 | Michael D. Makowsky & Thomas Stratmann, 2009 | 지방경찰의 과속범칙금은 속도뿐 아니라 운전자의 이의제기 기회비용·거주지와 지방재정 조건에 반응했다. 재정압박과 재산세 제약 아래 비거주 운전자 표적화가 커졌다. | [AER, 10.1257/aer.99.1.509](https://doi.org/10.1257/aer.99.1.509); [복제자료, 10.3886/E113290V1](https://doi.org/10.3886/E113290V1) | 저자 제공 자료·코드는 공개됐지만 ICPSR이 독립 검증한 복제는 아니다. 범칙금 선택자료로 장기 복지·인종별 기본부담을 직접 식별하지 않는다. |
| L-G Missouri 재정압박 | Alexes Harris, Elliott Ash & Jeffrey Fagan, 2020 | 2001–2012년 기관자료에서 지방 예산압박은 citation·교통정지 arrest 증가와 연관됐지만 한계효과는 White 운전자에 집중됐고 Black/Latino 운전자에서는 확인되지 않았다. White-to-Black 소득비가 큰 곳과 Black 운전자가 이미 더 과잉단속된 곳에서 상대적 White 효과가 컸다. | [Journal of Race, Ethnicity, and Politics, 10.1017/rep.2020.10](https://doi.org/10.1017/rep.2020.10) | bare budget shortfall 인근 RD를 포함한 준실험이나 무작위 실험은 아니다. White 집중은 Black 운전자의 기본부담 감소나 공정성을 뜻하지 않는다. 능력지불 해석도 관측 proxy에 의존한다. |
| L-H Indiana 수입보유·재정수요 | Siân Mughan & Akheil Singla, 2023 | 재정수요가 높고 지방정부가 범칙금 수입을 보유할 때 부유한 운전자, 특히 White 운전자의 citation 가능성이 높아졌다. 법원은 미납채무도 더 적극적으로 추심했다. | [Public Administration Review, 10.1111/puar.13595](https://doi.org/10.1111/puar.13595) | L-F/L-G와 연구팀·주·자료가 다른 보완계보이나 직접재현은 아니다. 소득·인종 proxy와 제도경계 밖 부담·안전효과에는 잔여 혼란이 남는다. |

세 계보의 공통 결과는 “취약한 집단이 덜 피해를 본다”가 아니다. 이미 높은 기본단속 부담과 재정압박 뒤의 **한계 증가분**을 분리하면, 집행자는 회수가능성·이의제기 비용·정치적 보복 가능성이 결합된 표적을 선택할 수 있다는 강한 반례다.

### claim 및 측정 수정

- `HIGHEST BASELINE BURDEN != LARGEST MARGINAL REVENUE-TARGETING EFFECT`.
- `LOW STRUCTURAL POWER != HIGHEST EXPECTED EXTRACTION YIELD`.
- 구조적 취약성만으로 표적을 예측하지 않고 다음을 경쟁모형으로 둔다.

```
expected_net_extraction
  = collectability / ability_to_pay
  × contest_opportunity_cost
  × low_electoral_or_political_retaliation
  × revenue_retention
  × fiscal_pressure
  - enforcement_and_collection_cost
```

이 식은 세 연구가 직접 추정한 단일 방정식이 아니라 Project의 구별용 합성가설이다. 방향과 함수형태를 사실로 승격하지 않는다. 기존 K1 `DEPENDENCE–POWER`, K4 `METRIC–CONTROL FEEDBACK`, K5 `SUPPRESSION–APPARENT CONSENSUS` 안의 표적선택 경계이며 새 first-order kernel은 열지 않는다.

frozen 비교에는 최소한 `resident/nonresident`, 소득·차량가치 등 지불능력 proxy, 법원까지 거리·시간·변호비용, 지역 투표권·정치적 voice, 수입보유 규칙, 예산충격, 집단별 기본 stop/citation/search/arrest 수준과 충격 뒤 한계변화, 실제 납부·연체·채무추심·면허정지, 안전성과를 함께 기록한다. 명목 citation 증가만으로 표적 취약성 또는 공익을 판정하지 않는다.

### 역할반전과 다음 결정검사

- 반복될수록 더 강해지는 주체: 수입을 보유하고 회수가능성이 높은 표적을 선택하는 집행·예산·법원 행위자.
- 더 소모되는 주체: 기본 과잉단속을 계속 부담하는 집단과, 지방 정치에서 voice가 약하거나 이의비용이 높아 새로 한계 표적이 되는 비거주·고회수가능 집단.
- 역할반전: 집행자·지역 유권자가 비거주자가 되어 동일한 이동비용·이의절차·추심제재를 감수해도 같은 규칙을 수용하는지 검사한다.
- 다음 결정검사: 독립 지역의 사전고정 event/RD 설계에서 `fiscal shock × retention × resident status × ability_to_pay × baseline overpolicing` 상호작용과 안전·징수부담을 동시에 측정한다. 기존 최취약집단의 기본부담은 높은데 한계효과만 다른 집단으로 이동하면 표적선택 역전을 지지한다. 미관측은 부재로 닫지 않는다.
