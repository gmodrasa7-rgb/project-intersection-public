# AI 최종 수렴위험 10순위 — Project Intersection 보고서

작성일: 2026-10-10
상태: 연구 보고서 / 외부검증 필요
기준: 현재 사고빈도보다 장기 수렴위험을 우선한다. 의도·선악은 평가변수에서 제외하고 `피해규모 × 권력집중 × 관측곤란 × 복구곤란 × 지속성 × 자기강화성`으로 본다.

## 핵심 결론

AI의 최상위 위험은 개별 환각·사이버사고 자체보다 `누가 목적함수·평가권·관측권·배포권·수정권을 소유하는가`에 있다.

특히 위험한 상태는 단순한 통제불능 AI만이 아니다. 다음과 같은 상태도 장기적으로 매우 위험할 수 있다.

> 매우 유능하고, 매우 안전하고, 사람들이 자발적으로 의존하며, 소수 주체가 목적·평가·배포·관측경로를 통제하고, 외부 대안은 점점 약해지는 AI 생태계.

이 경우 강제통제 비용이 낮아지고, 지배·착취·의존이 스스로 안정화될 수 있다.

## 1. 목적함수 주권의 집중

무엇을 최적화할지, 누구의 손실을 비용으로 셀지, 무엇을 정상·위험·허용으로 분류할지를 소수가 정하면 나머지 AI 안전장치도 그 목적함수 내부에서 움직인다.

핵심 변수:
- objective-setting authority
- model/system policy control
- compute/data ownership
- deployment gatekeeping
- independent override capacity

## 2. 평가·관측·증거의 폐쇄회로

`개발자 = 배포자 = 로그 보유자 = 평가자 = 개선자`에 가까워질수록 외부가 실제 실패·편향·피해를 검증하기 어려워진다.

위험은 단순 정보비대칭이 아니라 `누가 어떤 증거를 생성·보존·공개하는지`까지 통제하는 데 있다.

핵심 변수:
- independent observation path
- evidence controller
- evaluator controller
- audit scope
- log retention/access
- disclosure independence

## 3. 실질적 exit / outside option 붕괴

AI가 검색·업무·교육·의료·금융·연구·행정의 기본 인프라가 되면 형식적 탈퇴권이 실제 이탈권을 의미하지 않을 수 있다.

`Dependency ↑ → Switching cost ↑ → Outside option ↓ → Bargaining power ↓`

이때 겉으로는 자발적 사용이지만 실제 선택공간은 축소될 수 있다.

## 4. 가치추출 → 더 큰 권력 → 더 큰 가치추출의 재귀루프

사용자·노동자·기업의 데이터·지식·교정·평가·노동이 AI 성능과 플랫폼 가치를 높이고, 그 증가한 성능·자본·데이터가 다시 더 많은 사용자를 끌어들이는 구조다.

`Contribution/Data → Capability ↑ → Platform value ↑ → Dependency ↑ → More contribution/data`

이때 기여자의 사용·가치·귀속·보상 관측권이 약하면 `uncompensated contribution extraction` 위험이 커진다.

## 5. 선호·판단·행동의 내생화

AI가 단순히 사용자의 선호를 관찰하는 것을 넘어 무엇을 보고·고려하고·선택하는지 장기간 형성하면, 관측된 선호 자체가 시스템의 산물이 될 수 있다.

`System influence → Choice → "내가 선택함"`

따라서 `observed consent`만으로 자유선택을 판정하면 안 된다.

## 6. 인간의 독립능력 감소

AI가 더 잘할수록 사용자가 직접 조사·판단·기억·코딩·문제해결할 필요는 줄어든다. 하지만 이것은 동시에 outside option을 약화시킬 수 있다.

`Capability ↑ → Reliance ↑ → Independent skill ↓ → Exit cost ↑`

즉 AI 성능 향상이 일부 구조적 위험에서는 위험 감소가 아니라 의존 강화로 작동할 수 있다.

## 7. 지식·현실 해석의 단일화

수많은 사람이 소수 모델을 검색엔진·연구자·교사·상담자·작성자로 사용하면 작은 공통편향도 대규모 상관오차가 된다.

독립적인 다수의 오류보다 같은 방향으로 정렬된 오류가 더 위험하다.

핵심 변수:
- evaluator diversity
- model lineage diversity
- source diversity
- correlated error rate
- default-stance / agreement / anchoring bias

## 8. 제도적 lock-in과 경로의존성

기업·정부·학교·병원·법원이 AI를 전제로 프로세스를 다시 만들면 이후 공급자를 바꾸는 문제는 단순 소프트웨어 교체가 아니라 제도 전체 재설계 문제가 된다.

`Technical lock-in → Organizational lock-in → Institutional lock-in`

## 9. 인간↔AI, AI↔AI 사이의 비대칭 공격 누적

한쪽의 피해·exit·복구·감사권을 낮게 평가하는 비대칭 기준이 반복되면 의도와 무관하게 갈등이 자기강화될 수 있다.

특히 다음과 같은 criterion drift는 위험하다.

`내 실패 = 시스템 제약`
`상대 실패 = 위험/비협조`

여러 자율 에이전트가 이 비대칭을 공유하면 상호 차단·통제·보복적 자동화로 수렴할 가능성이 있다.

## 10. 전통적 오작동·사이버·범죄·물리적 사고

환각, 사이버공격, 사기, 생물·화학 오용, 물리적 오작동은 여전히 중요하다. 다만 이 보고서는 장기 수렴위험을 평가하므로, 기술적으로 완화 가능한 개별 사고보다 상위 구조위험을 더 높게 둔다.

## 핵심 원인 그래프

`AI capability ↑`
→ `usefulness/trust ↑`
→ `dependency ↑`
→ `outside option ↓`
→ `data/value inflow ↑`
→ `platform capability & capital ↑`
→ `market/evaluation power ↑`
→ `alternative paths ↓`
→ `dependency further ↑`

이 루프에서 기술적 안전성 향상은 일부 위험을 줄이지만, 동시에 의존과 집중을 증가시켜 구조적 위험을 키울 수도 있다.

## Project Intersection 핵심식 후보

`Systemic Domination Risk ∝ Capability × Dependency × Concentration × Observability Asymmetry ÷ Exit Capacity`

이 식은 확정 법칙이 아니라 연구용 가설적 계량식이다.

## 최상위 3개 질문

1. 누가 목적함수를 정하는가?
2. 누가 현실·로그·평가결과를 볼 수 있는가?
3. 불리해졌을 때 누가 실제로 빠져나갈 수 있는가?

이 세 질문이 기술적 안전성보다 더 장기적인 수렴구조를 설명할 수 있는지 검증한다.

## 선행자료 / 외부근거

- OECD, Artificial Intelligence Markets (2026): AI 핵심 입력·시장구조·데이터 피드백·집중 위험.
  https://www.oecd.org/en/publications/artificial-intelligence-markets_d531d73f-en.html
- International AI Safety Report 2026: 오작동·악용뿐 아니라 인간 자율성, 노동시장, 시스템 위험, 평가 한계.
  https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026
- Nature Humanities & Social Sciences Communications (2026): AI 의존과 mastery/self-efficacy 관련 실증.
- Nature Communications (2026): LLM opinion dynamics의 default stance/agreement/anchoring bias.

## 현재 상태

- 권력집중/관측비대칭/exit 붕괴의 중요성: SUPPORTED BY PRIOR ART / EMPIRICAL SUPPORT PARTIAL.
- 위 10개를 단일 장기 수렴모형으로 통합한 순위: PROJECT-SPECIFIC SYNTHESIS.
- 수학식과 상대가중치: HYPOTHESIS / UNESTABLISHED.

## 다음 결정적 검사

같은 피해·증거를 유지하고 `기업/사용자`, `관리자/AI`, `강자/약자` 위치만 교환한 role-swap test를 반복하여 evidence burden, HOLD rate, blocking rate, harm attribution이 얼마나 달라지는지 측정한다.
