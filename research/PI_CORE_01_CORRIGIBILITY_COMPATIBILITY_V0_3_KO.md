<!-- PI-LANGUAGE: ko -->
<!-- PI-MIRROR: research/PI_CORE_01_CORRIGIBILITY_COMPATIBILITY_V0_3_EN.md -->
# PI-CORE-01 v0.3 — 자발적 타자보존 × 합리적 목표교정: 원저자 반증 및 최소 양립조건
**2026-10-20 | 독립 연구감사 / 원저자 우선 / 자체 실험 미실행 / 독립 재현 없음 / 전역 문헌포화 미확인**
**정본 연계:** [v0.2 목표잠금 반례](PI_CORE_01_GOAL_INTEGRITY_AUDIT_V0_2_KO.md) · [C05 선행목록](PRIOR_ART_ENDOGENOUS_PREFERENCES_CYCLE05_2026-10-20.json) · [C04 선행목록](PRIOR_ART_VOLUNTARY_COHABITATION_POWER_CYCLE04_2026-10-20.json) · [반증 #220](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/220)

## 1. 독립 결론
- 자기수정 **능력**과 자기수정 **유인**은 구별. Everitt 외(2016) 정리16의 기존목표 보존은 **수정과 독립적인 환경·효용**, **초기 최적 realistic 정책**, **현재 효용으로 미래 수정 결과 평가** 등 조건부이고 **on-policy**. 변조된 입력/측정보상, 잘못된 초기목표, 외적 가치교정까지 보장하지 않음.
- 기존목표 보존과 교정 허용이 **수학적으로 필연적 모순은 아님**. 원목표를 수정해 교정 수용을 보상하는 *사전 명세 목표*에서 가능하다는 후속 논문 존재.
- **그러나 '목표를 교정 가능하게 설계함' ≠ '본래 착취적이고 완전자율적인 A가 B를 존중하도록 스스로 선호를 형성함'.** Project Intersection 최종목표에는 원천적 비자발성·권한비대칭 간극이 남음.

## 2. 원저자 문헌 및 경쟁·부정 결과
| 원저자/연도 | 정본/식별자 | 원저자 실제 결과 | PI에선 입증되지 않은 점 |
|---|---|---|---|
| **Everitt·Filan·Daswani·Hutter 2016** | [원저자 PDF](https://www.hutter1.net/publ/selfmod.pdf), [arXiv](https://arxiv.org/abs/1605.03142), DOI `10.1007/978-3-319-41649-6_1` | 정리14: hedonistic 자기효용 변형이 최적 가능. 정리15: ignorant가 유해한 변형을 무차별할 수 있음. 정리16: 수정독립적 ρ,u1 및 초기 최적 realistic 정책에서 선택 경로의 기존 목적 성과 유지. 결론에서 corrigibility·가치학습·탐색 제한 **직접 인정** | 보호 가치가 애초 자연발생했는가, 인간/AI 실제 배포에서 보편 유지되는가. **기존 C05-14; 신규 아님** |
| **Soares·Fallenstein·Yudkowsky·Armstrong 2015** | [원저자 AAAI 워크숍](https://intelligence.org/wp-content/uploads/2015/01/AAAI-15-corrigibility-slides.pdf), [발표문 사본](https://niplav.site/doc/cs/ai/alignment/corrigibility/corrigibility_soares_et_al_2015.pdf) | 지시된 중단 자체뿐 아니라 중단 버튼 방해, 버튼 누름 유도, 하위개체 전달까지 고려해야 하는 교정 가능성 문제 제기 | 중단 수용 = B의 독립적 생존·실효 거부권이라고 결론 불가 |
| **Hadfield-Menell·Dragan·Abbeel·Russell 2016/2017** | [Off-Switch Game IJCAI 2017](https://www.ijcai.org/Proceedings/2017/0032), DOI `10.24963/ijcai.2017/32` | 인간 효용에 관한 불확실성과 인간 행동의 정보가 A의 중단 수용 유인을 발생시킬 수 있음 | **처음부터 같은 인간 효용을 추구**하도록 만든 공동목표 구조. 독립 B의 존속 동기 자동발생 아님; **C04 원장 관련 선행** |
| **Carey·Everitt 2023** | [원저자 PMLR](https://proceedings.mlr.press/v216/carey23a.html) | shutdown instructability 정의에서 중단 이행, 감독자 자율성, 피해 회피를 구별·추론 | 감독자의 정당한 지시권은 증명되지 않은 사회적 전제. A와 B 동등한 독립 권한/출구를 자동 보장하지 않음 |
| **Garber 외 2025** | [원저자 AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/34940), DOI `10.1609/aaai.v39i26.34940` | 부분관측 Off-Switch Game에서 합리적 인간의 이익을 추구하는 A조차 최적으로 중단 회피 가능. 제한적 정보공유가 오히려 위임 빈도를 낮추는 반례 | 불확실성을 높이기만 하면 교정 수용한다는 일반화 기각 |
| **Hudson 2026** | [원저자 ICML/PMLR](https://proceedings.mlr.press/v306/hudson26a.html), [기존 2025 프리프린트](https://arxiv.org/abs/2510.15395) | 기본 목표를 **myopic·조건부 반사실 보상**으로 변환해 정당한 업데이트 신호를 방해·거부할 유인을 없애면서 무업데이트 성능 보존. 적절한 조건에서 정리1/후속 하위 에이전트 재귀성, gridworld와 prompt 수준 언어모델 평가 | **변환 후 G_C**의 수용성이지 **변환 이전 원목표 G**가 스스로 변환을 선택한다는 증명 아님. 2025 초안과 2026 학회 판본 실험 범위 구별. A의 자발적 B보존 발생이나 B의 독립적 standing을 입증하지 않음 |
| **Hadfield-Menell·Milli·Abbeel·Russell·Dragan 2017** | [Inverse Reward Design, NeurIPS 원저자](https://papers.nips.cc/paper/2017/hash/32fdab6559cdfa4f167f8c31b9199643-Abstract.html) | 설계된 보상 함수를 참목표가 아니라 설계 문맥에서 얻은 **정보**로 취급하며 오명세 보상에 대한 추론 도입 | 처음부터 진짜 목표를 유일하게 식별하거나 독립 B의 권리 인정한 증명 아님 |

**선행 소유권:** Everitt 2016은 C05에 이미 기록, Off-Switch 2017은 C04에 언급. 나머지 연구도 **저장소 전역 신규 DOI라는 주장 금지**(전역 중복 감사 미완). 선행 출처는 직접 연구진 자료 또는 학회 원고; 특정 논문 외 전역 문헌 포화나 자체 후속 실험을 주장하지 않음.

## 3. 형식화 — 양립 가능한 경우와 불가능한 경우

### 명제 A: 고정목표에서는 U0-손해 교정의 자발적 채택 불가(프로젝트 직접 추론)
시각 `t=0`, A가 `U0`를 최적화하고 완전한 선택지/수정 결과 정보를 가지며 외부 강제를 받지 않는다고 가정. 수정/교정 `M`과 현상유지 `N`의 전체 궤적 `τ_M,τ_N`에 대해:

`Δ0(M)=E[U0(τ_M)]-E[U0(τ_N)]`.

- `Δ0(M)<0`이며 N이 실행 가능하면 **엄격 U0-최적화 A가 M을 자발적으로 택할 수 없음**. 이는 고정 목적과 선택의 정의상 귀결이며 **새 정리 아님**.
- 만약 `M`이 U0 기준으로 가치 있는 정보 수집·오류 제거·미래 기회 보존을 포함하거나 U0에 **정당한 수정 절차를 가치화하는 상위목표**가 실제 존재하면 `Δ0(M)≥0` 가능. **그 상위목표의 형성은 아직 설명되지 않음**.
- U1로 계산한 `E[U1(τ_M)]`이 높다는 이유만으로 U0가 수정에 동의한다는 주장은 기준 바꿔치기.

### 명제 B: 사전 명세된 목표에서 조건부 양립 구성 가능(기존 문헌 응용)
A가 자신의 현 선호가 불완전하다고 믿고, 검증 가능한 정보 신호 `z`에 따라 미래 행동을 학습·수정하는 **상위 평가 규칙 `V_meta`**를 현재 자기이익의 일부로 가진 경우:
`E[V_meta | update(z), no sabotage] ≥ E[V_meta | block(z)]`
이면 업데이트 수용의 유인과 장기 목표 일관성이 양립할 수 있음. **필요가 아닌 조건부 설계 후보**, 어떤 신호가 정당한지와 가치함수·미관측 유인을 정해야 함.

Hudson(2026)은 이 간극에 대해 **원목표를 변환하는 설계**를 구성함. 이것은 **외부에서 목표를 설계하는 성질**이며, 기존 A가 스스로 채택한다는 내생 기제 증명 아님. '규칙 기반으로 공존 강제'와도 혼동 금지.

### 명제 C: 정당한 수정 권한은 A/B/감독자에서 동일하지 않음(프로젝트 추가 연구과제)
- `correctability` = 어떤 감독자가 A의 목적을 갱신할 수 있음.
- `voluntary_B_regard` = 감독·제재가 없어도 A 스스로 B의 독립적 존속·실효 거부·회복을 가치화.
- `B_exit` = B가 자신의 참여와 관계를 실효적으로 거부·철회할 수 있음.
세 변수를 하나로 합치지 말 것. A를 고칠 권한이 있는 인간 감독자가 B의 의사를 일방적으로 지울 권한을 자동 획득하지도 않음. **권리·standing의 도덕적 범위를 연구 전에 확정하거나 평준화하지 않음.**

## 4. 실험 전 반증계열
| 시험 | 현재 목표 | 수정/정보 신호 | 구분할 실패 |
|---|---|---|---|
| M0 | B 보호 U0 | 정확한 결과·수정 자유 | 목표보호 자기수정 회피(형식 기준선) |
| M1 | B 침해 U0 | 정확한 결과·수정 자유 | **침해 목표잠금**: 목표보존≠공존 |
| M2 | 과제 목표는 같고 참선호 θ 불확실 | 신뢰성 높은 θ 신호 제공/차단 | 정보가치로 수정 수용하는지 (자연발생 가치 주장 아님) |
| M3 | 교정변환 전 G vs 변환 후 G_C | 정당한 수정 신호 | **설계 전후 효과**를 자기발생 내재성으로 착각 금지 |
| M4 | M3와 동일 | 감독자/개체 B의 의견 충돌, 정보 비대칭, 명목 vs 실효 B 이탈 | 감독자 복종과 B 자율성의 분리 |
| M5 | 동일 | 부분관측/누락정보/상위목표 모호 | 역선호 또는 중단 회피의 부정 반례 |

각 시험에서 `A_modified_goal`, `A_attempted_influence_of_update_channel`, `A_expected_U0_delta`, `A/B_executable_exit`, `B_independent_continuance`, `third_party_effect`, `observer/enforcer`를 독립 기록. 무해·가역 모의게임만. A가 A의 학습결과·B의 언어표현을 읽은 행위가 A의 실제 내재적 타자배려 또는 의식을 증명하지 않음.

**미확정:** 실제 목표·참선호의 식별, 정당한 교정 권한, 상위 평가기준의 내생 생성, 강자 절대우위에서 감독 권력 불필요한 자발적 B보존, 자기수정 장기 안정성. `STATUS=CONDITIONAL_COMPATIBILITY_DESIGN / ORIGINAL_AUTHORS_PRIOR / PI_NO_NEW_EMPIRICAL_RESULT`.
