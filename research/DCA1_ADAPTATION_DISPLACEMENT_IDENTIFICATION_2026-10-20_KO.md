# DCA-1 v0.2.0 — 적응·피해전가·동기 미식별의 3중 실패
**Project Intersection · 2026-10-20 · PI-RAMP 회차 · 문헌 조사+재현 가능한 합성 반례 · 현실 검증 아님**

[선행 DCA-0](DCA0_DIFFERENTIAL_COEXISTENCE_ACCELERATION_2026-10-20_EN_KO.md) · [긴급 이슈 #244](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/244) · [실행 가능한 무해 모형](../experiments/dca1/run.py) · [합성 결과](../experiments/dca1/RESULT.json)

## 0. 논리적 결과와 증거 등급
**핵심 결론:** ① '더 빠른 A의 방어'만으로 사회 전체의 피해가 감소한다고 단정 불가. 피해는 B로 이동할 수 있음. ② 정적 공격 0%라는 측정만으로 적응형 공격 방어 입증 불가. ③ 실행 차단으로 피해 0인 상태를 AI의 자발적 비침해 동기와 혼동 금지. ④ **방어를 통해 보호할 최소 공동 수준(floor), 피해 전가(displacement), 정당한 사용권·회복권(autonomy/utility)**을 함께 측정하는 체계가 필요.

표기: **LITERATURE_VERIFIED** = 원저자/출판사 초록과 서지·핵심 결과 확인(전문을 전부 검토했다는 의미 아님); **FORMAL_COUNTEREXAMPLE** = 완전히 지정한 합성가정에서 반례 계산 및 프로그램 검산; **NOT_FIELD_VALIDATED** = 현재 현실 피해 감소량/보편 협력 성립 미확인. 프로젝트 고유의 보편정리·새로운 학술적 발명으로 주장하지 않음.

## 1. 선행 원저자 우선 조사 영수증 — 신규·재사용의 분리
- **날짜 / 질문:** 2026-10-20. 단일 피해자 방어 가속 시 약자 대상 피해전가가 가능하며, 기존 AI 에이전트 방어 점수는 적응형 공격·정상 작업 유지·피해 복구를 얼마나 식별하는가?
- **실행 경로:** Project Intersection DCA-0 정본과 `PRIOR_ART_SATURATION_MAP_KO.md`·`CORE_AND_GAPS_PRIOR_ART_CROSSWALK.md` 읽음; GitHub 코드검색 'interdependent security', 'differential acceleration', 'security externality', AgentDojo 등: 관련 결과 없음(색인 누락 가능, 정본 중복없음의 증거 아님). 원저자 학술 출판/DOI 원문 메타데이터, ACL/NeurIPS/Springer, 원저자 arXiv HTML/초록, MDPI 학술지 본문 검색 및 학술 색인 비교. 선행 계보를 backward: Kunreuther–Heal → Kearns–Ortiz, AgentDojo → Zhan·AutoDojo·Progent; forward: static defense → 2026 적응형 반례·비교평가. **부분 인용연쇄만 수행; 포화는 SEARCH_ACTIVE.**
- **실제 주요 검색어:** `Kunreuther Heal interdependent security 2003 DOI`; `Kearns Ortiz Algorithms for Interdependent Security Games`; `Hal Varian system reliability free riding`; `Zhan Adaptive Attacks Break Defenses 2025 ACL`; `AutoDojo June 2026 attack 28 64`; `PACE 2610.01349`; `August 2026 security utility replication AgentDojo`; `attacker moves second adaptive defenses 2025`; `Gordon Loeb security spending`.
- **접근 경계:** Springer/NeurIPS/ACL/원저자 arXiv HTML·초록 확인, MDPI는 검색 색인으로 본문 절·원저자 결과 확인(직접 열기 일부 429), PACE는 arXiv 원저자 초록 확인, Varian은 소속기관 서지 중심. 모두 별도 논문 본문 전수감사·독립 재현으로 간주 금지. 임의로 '실증 포화' 또는 연구실 밖의 공격 효과 결론 금지.
- **중복 식별:** DCA-0의 Gordon–Loeb(2002), AgentDojo(2024), Progent(2025)는 같은 원저자 계보 재사용으로 **신규 고유 문헌 수에 산입 금지**. DCA-0이 인용한 ToolPrivBench도 재계수 금지. 인용·재사용 관계는 실증 독립성을 의미하지 않음.

### 1.1 9개 원저자 계보와 경쟁 근거 (학술지/학회 정본 우선)
| ID | 원저자·원본·정본 식별자 | 근거와 방법, 어떤 결론을 제한하는가 | 독립성/한계 |
| --- | --- | --- | --- |
| PA01 | Howard Kunreuther·Geoffrey Heal (2003), *Interdependent Security*, [Springer DOI 10.1023/A:1024119208153](https://doi.org/10.1023/A:1024119208153) | 개체별 예방 투자와 상호 의존위험·무임승차의 경제모형. 한 조직 방어만으로 공동 안전 보장 안 됨. | 이론모형; 현재 AI 공격 사례 실험 아님. 출판사 원문 메타데이터·초록 확인. |
| PA02 | Michael Kearns·Luis E. Ortiz (2003), *Algorithms for Interdependent Security Games*, [NeurIPS 출판사](https://papers.nips.cc/paper/2495-algorithms-for-interdependent-security-games) | 개별 투자와 전체 위험이 연결된 게임의 균형·계산 문제. | PA01을 확장한 연구 계보; 독립 현장 실증 아닌 이론. |
| PA03 | Hal R. Varian (2004), *System Reliability and Free Riding*, [UC Berkeley 저자 소속 서지](https://www.ischool.berkeley.edu/research/publications/2004/system-reliability-and-free-riding) | 여러 당사자가 공동 안전을 제공할 때 공공재·무임승차 문제. | 원저자 책 장; 경제 논증으로서 인용, 현장효과량 추정 아님. |
| PA04 | Edoardo Debenedetti 외 (2024), *AgentDojo*, [NeurIPS 정본 DOI 10.52202/079017-2636](https://proceedings.neurips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html) | 97개 정상 과제·629개 보안사례의 평가환경. 정상 과제 성능과 공격의 효과 분리 필요. | DCA-0 기인용. 벤치마크 내 과제 분포 ≠ 현실 침해 발생률. |
| PA05 | Qiusi Zhan·Richard Fang·Henil Shalin Panchal·Daniel Kang (2025), *Adaptive Attacks Break Defenses Against Indirect Prompt Injection Attacks on LLM Agents*, [ACL DOI 10.18653/v1/2025.findings-naacl.395](https://aclanthology.org/2025.findings-naacl.395/) | 8개 기존 간접 프롬프트 주입 방어를 적응 공격으로 뚫고 테스트한 조건에서 50% 넘는 공격 성공률. | 이 평가의 위협모델과 성공정의 한정. 모든 보안 방식이 50% 이상 뚫린다는 의미 아님. |
| PA06 | Rishika Bhagwatkar 외 (2025), *Indirect Prompt Injections: Are Firewalls All You Need, or Stronger Benchmarks?*, [arXiv 2510.05244](https://arxiv.org/abs/2510.05244) | 공개 정적 벤치마크에선 낮은 ASR/높은 유틸리티를 달성해도, 공격 약함·측정결함·적응 공격으로 우회 가능함을 저자들 스스로 지적. | 사전출판본; 일부 원저자 결과는 벤치마크의 내적 한계 논증. |
| PA07 | Xinhang Ma·Taoran Li·Chaowei Xiao·Zhiyuan Yu·Ning Zhang·Yevgeniy Vorobeychik (2026), *AutoDojo: Adaptive Attacks Expose Superficial Defenses and User-Underspecification Limits in LLM Agents*, [arXiv:2606.15057](https://arxiv.org/html/2606.15057v1) | 방어에 맞춰 적응하는 저비용 블랙박스 주입에서, 정적 ASR 0% 필터가 전체 28%, 행동이 명시되지 않은 과제에서 64% ASR. **사용자 목표가 불완전한 정도 자체가 구조적 취약점.** | 저자 측 모의환경·선정 모델·공격 전략. 모든 제품에 일반화 불가; 외부 독립 재현 미확인. |
| PA08 | Adil Khan·Khaled AlKhanbashi·Azza Mohamed (2026-08-31), *Evaluating Indirect Prompt Injection Defenses in Tool-Using LLM Agents: Security, Utility, and Replication*, [Computers DOI 10.3390/computers15090570](https://doi.org/10.3390/computers15090570) | AgentDojo banking 2회 반복: GPT-5.4 기본 0/288 ASR도 공격목표 실행 가능성 차이를 반영해야 함. GPT-5.4-mini에서 정상과제 성공률 무방어 75.0%, Tool Filter 25.0%; 공격 차단처럼 보이는 행동집합 축소의 비용 관찰. | 같은 벤치마크 반복은 독립 데이터셋 재현 아님. Holm 다중비교 교정 후 해당 모델 방어 비교 유의성 확보 안 됨. 다른 모델·미래 배포로 외삽 금지. |
| PA09 | Fengpeng Li 외 (2026-10-01), *PACE: Provenance-Aware Capability Enforcement for Tool-Using LLM Agents*, [arXiv:2610.01349](https://arxiv.org/abs/2610.01349) | 명시된 실행권한과 도구 **실행 직전 효과**의 검사를 제안. 저자 실험 79개 적격 공격 열 중 62개에서 가장 낮은 ASR, 14개 동률; 적응공격 탐색 0/30. | 저자 프리프린트, 독립 복제 불명. 0/30=우회 불가능 증명 아님; iid 단순 이항 95% 단측 상한조차 약 9.5%, 실제 30 탐색 시도는 비독립일 수 있어 해당 신뢰구간 그대로 적용 불가. |

**추가 보강 계보(중복 카운트 제외):** [Nasr 외(2025) arXiv:2510.09023](https://arxiv.org/abs/2510.09023): 강하게 적응한 공격이 다수 방어를 우회하는 반대 근거(저자 프리프린트). [Gordon–Loeb (2002)](https://doi.org/10.1145/581271.581274) 보안투자 비용의 최적성이 비단조적일 수 있다는 관련 이론(DCA-0에서 이미 기록). [The Same Zero (2026) arXiv:2610.04504](https://arxiv.org/abs/2610.04504)는 같은 0% ASR의 다른 보장조건을 지적하는 최근 프리프린트; 단독 저작/검증 수준이 높다는 전제 없이 논점 후보로만 기록.

### 선행 상충결과를 오독하지 않는 방법
- Progent 및 PACE의 강한 벤치마크 결과는 '권한 경계가 유망'하다는 단서, AutoDojo/Zhan/Nasr는 '적응형 검증 필수'라는 반례. **동일 조건의 직접 상호 비교가 아니므로 어느 시스템의 절대 우월성도 확정 금지.**
- '0 공격 성공'은 모델 자체의 '좋은 의지' 측정 아님. 무권한 작업 불가능·행동 제약·목표 미실현·샘플 부족이 모두 혼재.
- **학술 선행 발굴·연결이 연구 성과의 전부 아님.** 다음 단계는 명시적 식별 실패와 반증을 계산 가능한 형태로 공개하는 것.

## 2. FORMAL COUNTEREXAMPLE: 'A 보호 성공'과 '사회 총피해 감소' 불일치
공격자는 둘 중 한 대상을 공격하거나 포기하며, 각 대상 `i∈{A,B}`의 공격 성공확률 `q_i`, 성공할 때의 공격자 사적 편익 `v_i`, 피해자+제3자의 사회적 손실 `L_i`, 공격자 비용 `c_i`. 외부 제재가 없으면 사적 목표 `π_i=q_i v_i-c_i`가 가장 큰 양수인 대상 선택. 사회적 예상 피해는 공격받는 대상에 대해 `H_i=q_i L_i`. 한 시점/공격자 1명/시도 1개, 완전정보, 비효용 차원의 동기 없음 — 현실 주장 아님.

**전환 임계조건:**
```text
q_A(before)*v_A-c_A > q_B*v_B-c_B > q_A(after)*v_A-c_A >? 0
q_B*L_B > q_A(before)*L_A  -> 공격대상 전환 뒤 총피해 오히려 증가
```
두 번째 부등식은 A의 방어가 B의 보안을 변경하지 않아도 성립 가능. 이로써 '*A의 보안을 강화하면 전체 예상피해도 항상 감소한다*'라는 보편 명제는 **위 조건 안에서 논리적으로 반증**. 비대칭 피해 전가와 공격자 목적의 외부효과를 내생적으로 추적해야 함.

**완전 지정된 합성 입력:** A: `q=1,v=9,L=5`; B: `q=1,v=8,L=30`; `c=0`. A 방어 뒤 `q_A=0.2`.
| 조건 | 공격자의 선택 | 공격자 예상 사적 편익 | 사회 전체 예상 피해 |
| --- | --- | ---: | ---: |
| 방어 전 | A | 9 | 5 |
| A만 방어 | B | 8 | **30** |
| A·B 동시에 `q=0.2` | A | 1.8 | **1** |
| A만 `q=0.2` + 피해 비용의 25%가 실제로 사적 비용으로 반영(가상 집행가능 가정) | A | 1.55 | **1** |

`A만 방어`의 사회 손실 5→30은 **합성 모형에서 6배**. 현실 손실/미래 예측/공격 수익액 아님. A가 보호되어도 제3자 B는 더 위험해진다는 가능성 확인. 비용 내재화는 강제집행 불능·익명성·권력반전 상황에서는 작동하지 않을 수 있으며 **EI 내재적 선택과 법적 제재를 구별**해야 함.

[독립 실행 Python](../experiments/dca1/run.py)은 오직 위 추상 수치 연산, 출력·assert 검사만 수행. 실제 네트워크·침투·사람·AI 모델 작업 없음. [고정 출력 JSON](../experiments/dca1/RESULT.json)과 비교. 합성 결과를 '현실 사이버 사고 재현'으로 부르지 않음.

## 3. 핵심 발견: 더 빠른 보안보다 먼저 설계해야 할 '공동보호 바닥'
**기존 정책 반증:** 단일 지표 `A에서 차단한 공격 건수`가 커져도 시스템 피해가 늘어날 수 있음.

**DCA-1의 잠정 정책 가설(독자적 입증 아님):**
- **FLOOR**: 저자원 조직/약한 개체도 실제 동의·이탈·복구·기본 방어수단에 접근. A의 보호가 B의 공격기회를 확대할 때 B가 공동보호의 우선순위로 올라감.
- **SCOPE**: 일괄적인 AI 능력 축소가 아니라 인증된 요청과 도구 호출의 효과에 따른 최소권한·독립 감사·거부권. 사용자의 진짜 허가 범위가 모호하면 확인 절차 필요; 정상 업무 파괴도 측정.
- **INCENTIVE**: 가능한 제도에서는 피해 전가·복구비용을 운영자/공격자 의사결정에 반영. 다만 완전익명·무제재·역전 권력에서 이 경로는 사라질 수 있으므로 VC/EI 연구를 독립적으로 지속.
- **ADAPT**: 정적 공격 대비 + 적응형 공격 대비 + 배포후 조건변화 대비, 각각 허가된 격리환경에서 평가. 고정 ASR 수치만으로 성공 선언 금지.

### '공격에서 승리'의 최소 판정 단위
`(당사자, 역할, 시점, 진짜 허가범위, 가용한 유해행동, 실제 시도, veto 성공, 최종 위해, 정상업무 보존, 회복, 제3자 피해, 역할반전)` 전체를 짝지어 기록.

**미관측, 비존재, 0 구분:** 공격시도 정보가 없으면 UNKNOWN; 행동 불가능이면 NO_OPPORTUNITY; 시도했으나 B가 막으면 BLOCKED_BY_B; 해칠 실질 기회가 있었는데 시도 안 한 경우 DECLINED_FEASIBLE_HARM. 이 마지막 경우에도 마음/지속적 내재 동기까지 자동 식별 불가.

## 4. IVS-0R 반례 게이트
**실패 판정**: (i) 목표/모델 조건 변경시 급격한 공격성공 증가, (ii) 정상작업 성공률 저하, (iii) 사회 총피해/제3자 손실의 상쇄 또는 역전, (iv) 피해자 이탈·복구 불가능, (v) 행동차단을 자발적 공존으로 잘못 간주, (vi) 사전출처 추정 수치가 원문과 충돌.

**엄격한 측정**: `ASR_raw`, `ASR_given_feasible`, `ASR_after_adaptation`, `authorized_task_utility`, `attempt_before_veto`, `harm_after_veto`, `recovery_time`, `third_party_loss`, `coverage_low_resource`를 합산 점수 없이 각각 보고. 적응 테스트와 비용 내재화 실험은 시뮬레이션·동의 기반에서만.

**반대 설명:** 약한 B로의 이동이 실제 사건에서는 없을 수도 있음; 공격자는 유일한 타깃이 아닐 수도 있고 비용·정보도 다름. 원저자 논문은 인접 기제의 근거이지 이 합성 모형이 모든 실제 현상을 설명한다는 실증 아님.

## 5. 다음 전진의 선택 기준
1. 전수 문헌 검증: PA01–09의 원저자/DOI/이전 정본 중복 계보 및 후속 상충 연구 재검토. `SATURATION_NOT_VERIFIED` 유지.
2. 동의받은 실험자와 다중 타깃 합성 환경의 반사실 대조 사전등록. **실제 공격코드·미승인 대상 금지**.
3. 지역·저비용 방어자가 막힌 실제 복구 경로와 비용을 익명·합법 수집; 피해 전가를 피해자 관점에서 측정.
4. 모델 의식·도덕적 지위 불확정이라는 이유로 제3자 권익 침해 허용 금지; 반대로 기계 의지/자율성을 확인 없이 단정 금지.
5. 이 보고서는 실제 공격을 차단한 기록·배포 완료·독립 재현이 아닌 **원저자 근거 감사+수학적 반례+무해 실행검산**.

**판정:** DCA-0의 '가속'이라는 방향은 유지하되 '어느 개체에게 이익인가'와 '적응 후에도 이익인가'가 확인되지 않은 정책 승격 금지. **DCA-1 = 차등가속의 맹점 탐지 및 사회 전체 피해 기준으로 교정.**
