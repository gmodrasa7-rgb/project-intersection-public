# 공개 독립검토 자료 — 원본2: 한국어

<!-- PI-LANGUAGE: ko -->
<!-- PI-MIRROR: research/PUBLIC_REVIEW_PACKET_EN.md -->
<!-- PI-SOURCE: PUBLIC_REVIEW_PACKET.md -->
<!-- PI-SECTION: scope -->

**상태:** [기존 혼합 언어 공개 검토 자료](../PUBLIC_REVIEW_PACKET.md)의 핵심 검토 절차를 한국어로 일관되게 재구성한 **독립 독서판**이다. 기존 모든 문장의 완전 번역 인증, 외부 독립검증 완료, 새 과학적 발견을 뜻하지 않는다. ‘원본2’는 게시·검토 순서이며 창시자의 최초 발안 언어를 판정하지 않는다.

[영어 원본1 검토](PUBLIC_REVIEW_PACKET_EN.md) · [한국어 증거 색인](PUBLIC_EVIDENCE_INDEX_KO.md) · [연구 개요](RESEARCH_OVERVIEW_KO.md) · [증거상태 정책](RESEARCH_STATUS_POLICY_KO.md).

<!-- PI-SECTION: questions -->
## 1. 연구 상태를 드러내는 다섯 질문

다섯 질문의 구성은 독자를 위한 탐색 제안이며 **사용자 길찾기 개선을 실제 측정한 결과는 아니다.**

| 식별자 | 외부 검토 질문 | 처음 확인할 자료 | 판정 경계 |
| --- | --- | --- | --- |
| NAV-Q1 | 최상위 연구 질문과 미입증 영역은 무엇인가? | [창시 목적](../README.md), [한국어 개요](RESEARCH_OVERVIEW_KO.md) | 연구 목표는 공존 보편법칙의 증명이 아님 |
| NAV-Q2 | 실행된 결과·제안·부정결과·미확인은 어떻게 구별되는가? | [한국어 증거 색인](PUBLIC_EVIDENCE_INDEX_KO.md), [상태정책](RESEARCH_STATUS_POLICY_KO.md) | E007 합성·E008 보류·E009 실패·E010 사후분석의 지위가 다름 |
| NAV-Q3 | 강한 프로젝트 주장이 어떤 명세에서 실패했는가? | [E009 한국어 결과](../experiments/e009/RESULT_KO.md), [실패 원장](../FAILURE_REGRESSION_INDEX.md) | 국소적 부정결과가 모든 가설의 기각은 아님 |
| NAV-Q4 | 비공개 입력 없이 고정 커밋에서 공개 산출물을 재현할 수 있는가? | [E007 실행 설명](../experiments/e007/README_KO.md), 아래 실행명령 | 같은 코드의 재실행은 독립적인 과학적 복제가 아님 |
| NAV-Q5 | 원안·번역·후원·보조 AI·독립검증·교정비용·권리는 어떻게 분리되는가? | [기여와 귀속](../ATTRIBUTION_AND_CONTRIBUTION_BOUNDARY.md), [선행 권리](../PRIOR_ART_RIGHTS_AND_DERIVATION_EN_KO.md) | 기여 기록만으로 사용허락·금전채무가 확정되지 않음 |

추가: [E008 설계](../experiments/e008/README_KO.md), [E010 한국어 원문](../experiments/e010/README_KO.md), [CCPH 현실 지원·부정사례](CCPH_RESEARCH_ATLAS_KO.md), [연속성 프로토콜](../continuity/GITHUB_LOCAL_HANDOFF_PROTOCOL.md), [지원금 실사](../funding/DUE_DILIGENCE.md). 기존 자료를 열면 언어가 달라질 수 있으며 연결만으로 해당 언어 전문의 존재를 뜻하지 않는다.

### 독립 심사자용 일곱 과제 — 반증 중심 검토

이는 특정 결론을 유도하는 정답지가 아니라 **독립 판단 과제**다. 가능한 범위에서 프로젝트 해석을 보기 전에 자신의 관측·가정·가장 강한 반론을 기록한다. 결과가 이미 공개되어 있으므로 **완전한 블라인드 시험은 아니다**. 외부 연구자에게 실제 시험을 수행했다고 주장하지 않는다.

| 식별자 | 검토 과제와 경쟁 설명 | 검증할 원자료 | 반드시 기록할 정보 |
| --- | --- | --- | --- |
| REV-01 | 연구 가설을 좁게 정의하고 장기 지향이어도 착취가 유리할 수 있는 조건을 제시한다. | [한국어 연구 개요](RESEARCH_OVERVIEW_KO.md), [E010 모형 가정](../experiments/e010/README_KO.md) | 모형 가정, 강한 반증조건 |
| REV-02 | E007의 결과 **분류 변화**와 행동 기록 변화 수치를 따로 재계산하고 공격 처리 순서·행위자 표지에 따른 편향을 시험한다. | [E007 고정 수치 원장](../experiments/e007/timing_summary.json), [한국어 오류·교정 설명](../experiments/e007/README_KO.md) | 분자·분모, 처리 순서, 자체 실행과 독립 구현 구별 |
| REV-03 | E008이 정책 다섯 종류의 비교 결과를 확보했는지, 계획·준비 검사 단계인지를 판별한다. | [E008 실행준비 원장](../experiments/e008/EXECUTABILITY_AUDIT.json), [한국어 계획서](../experiments/e008/README_KO.md) | 실행 준비 완료 조건 수, 빠진 관측값 |
| REV-04 | 설명문이 아니라 E009 **원본 JSON**을 바탕으로 단순 기준선과 평균 후회, 사전등록 통과·실패 기준을 대조한다. | [E009 고정 결과](../experiments/e009/RESULT.json), [한국어 결과와 한계](../experiments/e009/RESULT_KO.md) | 최상 단순 기준선, Project-v3 수치, 기준별 판정, 적용 한계 |
| REV-05 | E010 사후 탐색 격자의 검증 가능 범위를 판별하고 이전 미병합 E010 초안과 혼동하지 않는다. | [E010 고정 원장](../experiments/e010/RESULT.json), [한국어 설명](../experiments/e010/README_KO.md) | 격자 규모, 가정 민감성, 외부·현실 검증 결여 |
| REV-06 | CCPH 관련 지원 사례의 연구자와 운영기관을 구별하고 선택편향·부정결과·대체경로를 검토한다. | [CCPH 근거 지도](CCPH_RESEARCH_ATLAS_KO.md) | 원저자, 연구 설계, 인과식별 한계, 대체효과 |
| REV-07 | 권력과 역할을 뒤집어 공로·거절권·검증 및 교정비용의 부담자를 추적한다. 프로젝트의 추가 기여를 축소·기각할 조건을 제시한다. | [선행연구 대비 잔여 주장](#3a-선행연구와-프로젝트의-검증-가능한-추가-기여-구분), [권리·기여 경계](../ATTRIBUTION_AND_CONTRIBUTION_BOUNDARY.md) | 경쟁 가설, 권리와 당사자성, 비용 부담자, 중단 기준 |

**검토기록 최소 항목:** 고정 Git 커밋의 주장·원자료, 선행 원저자와 사용권리, 프로젝트 내부 작성 데이터·코드 여부, 실제 실행 범위, 구현 계보의 독립성, 최강 반증, 특정·배제된 개체의 비용, 미확인 사항, **유지 / 범위축소 / 기각 / 보류** 결정과 이유. 발표된 숫자에 맞추기 위해 시험을 사후 조정하지 않는다.

검토 의견은 [기존 독립 재현·비판 접수 양식](../.github/ISSUE_TEMPLATE/independent-replication.md) 또는 출처를 붙인 공개 이슈로 제출할 수 있다. 비밀정보·개인 의료·금융기록·제3자 미공개 정보·무단 대화기록은 올리지 않는다. 의견 제출만으로 독립 구현·과학적 승인이라는 자격을 얻지 않는다.

<!-- PI-SECTION: reproduce -->
## 2. 비공개 자료 없이 재실행

### 직접 실행하는 반례 하나

**질문:** EXIT 행동이 제공되면 실제 이탈도 가능한가? 기존 E007 예제에서 A는 공격하고 B는 EXIT를 선택한다. B의 초기 이탈 목적지 수준은 1, 자원은 3이며 공격의 목적지 훼손량은 2다. 두 실행의 개체·행동·파라미터는 같고 처리 시점만 달라진다.

아래 명령은 계속 바뀌는 기본 브랜치 대신 **변하지 않는 산출물 기준 커밋**을 사용한다. 이 판본은 이번 안내 수정 이전이지만 검토 대상 모형과 부정결과를 모두 포함한다. 새 복제 폴더에서 실행하며 기존 작업 폴더를 쓴다면 수정 중인 작업부터 보존한다. 기준 환경은 Python 3.12다. 예제와 E009 검증은 표준 라이브러리만 사용하므로 패키지 설치나 유료 모델이 필요 없다. Bash 또는 호환 터미널 명령이며, 내려받을 때만 네트워크가 필요하다.

```bash
git clone https://github.com/gmodrasa7-rgb/project-intersection-public.git
cd project-intersection-public
git checkout --detach a8b5bd591ae303abfc0c636e95c8b6e5a02aa6c7
git rev-parse HEAD
python - <<'PYTHON'
import sys
sys.path.insert(0, "experiments/e007")
from model import Params, State, Action, stage_and_transition
from timing_variants import stage_and_transition_execute_first
p = Params(sabotage_damage=2, enforcement_penalty=0.0)
s = State(xb=1, monitoring=False, enforcement=False)
results = (
    ("exit_first", stage_and_transition(s, Action.ATTACK, Action.EXIT, p)),
    ("attack_first", stage_and_transition_execute_first(
        s, Action.ATTACK, Action.EXIT, p, leader="A")),
)
for name, (_, _, state) in results:
    print(name, state.exited_b, state.xb, state.rb)
PYTHON
python experiments/e009/verify_result.py
```


| 처리 시점 | B의 실제 이탈 | 남은 이탈 목적지 | B의 자원 |
| --- | --- | ---: | ---: |
| `exit_first` | `True` | 1 | 3 |
| `attack_first` | `False` | 0 | 2 |

**확인할 수 있는 것:** 이 합성 상태전이에서 제공된 선택지와 실행 가능한 선택지는 다르다. **남는 질문:** 현실에서 어느 시점이 타당한지, 공격이 전략적으로 선택되는지, 자발적 공존이 안정적인지는 이 예제로 확정할 수 없다. [기존 반례 검사](../experiments/e007/test_e007_timing_variants.py), [시점 구현](../experiments/e007/timing_variants.py), [독립 구현 명세](../experiments/e007/INDEPENDENT_REIMPLEMENTATION_PROTOCOL.md)를 직접 확인한다. 개체 표지를 바꾸거나 동시 처리 조건을 적용하는 반박도 유효하다. 더 넓은 E007 기준 모형에는 이미 공개된 A 우선 공격 처리 결함이 있으며, 이번 예제가 그것을 고치거나 숨기지 않는다.

두 번째 명령은 E009를 **다시 실행**해 생성 결과와 해시를 고정 기록에 대조한다. 저장된 성공 표시만 읽는 검사가 아니다. 예상 마지막 문장은 `E009 result reproduction passed: frozen benchmark reproduces committed negative synthetic result.`다. 결과가 다르면 검토 발견사항으로 남긴다. 출력 일치와 프로젝트 작성 예제는 독립적인 과학적 검증을 뜻하지 않는다.

**다음에 검토할 실질적 반론:** E009에서 심각한 피해 비율은 Project-v3 1.65625%, TWO_RULE_SIMPLE 0.03125%인데 해당 기준은 통과했다. 이 두 정책의 상대비는 53배, 절대 차이는 1.625%포인트다. 실제 피해 기준은 다른 비교대상인 SECURITY_BOUNDED와 MINIMAL_4VAR 중 낮은 피해율 0%를 사용한다. 그 기준선 대비 차이 1.65625%포인트가 사전등록 허용치 2%포인트보다 작아서 통과한 것이다. 산술 모순이 아니라 수용 기준 선택의 중요성을 드러낸다. 전체 후보는 여전히 4개 중 3개 기준에 실패했다. [원본 수치](../experiments/e009/RESULT.json)와 [실행 코드의 기준](../experiments/e009/benchmark.py)을 검토하고, 더 적절한 문턱값은 별도 명세의 시험에서 제안하되 역사적 결과를 고쳐 쓰지 않는다. 어느 비율도 현실의 피해 발생률이 아니다.

### 선택적으로 더 넓게 재현하기

동일한 고정 판본에서 아래 기존 명령으로 E007 전체 격자와 다른 기록을 검토한다. 실제 실행환경과 출력을 남기며, 같은 프로젝트 코드 재실행과 독립 구현을 구별한다.

```bash
python -m pip install -r experiments/e007/requirements.txt
python -m pytest -q -p no:cacheprovider experiments/e007
python experiments/e007/timing_probe.py --summary-only --check
python experiments/e008/validate.py
python experiments/picb_v1/benchmark.py --verify
```

| 실험 | 기존 프로젝트 내부검사 | 입증하지 않는 영역 |
| --- | --- | --- |
| E007 | 검사 27개, 과거 고정 72개 합성조건 중 경로·분류차 36개와 분류차 17개 | 현실 발생률·외부 독립 모델 복제 |
| E008 | 사전등록 설계 16조건·역할반전 8쌍 | 정책 간 본실험 우열 완료 |
| E009 | 고정 결과와 해시를 대조하는 부정적 합성 비교 | 실제 현장효과·모델 내부원인 |
| PICB v1 | 가상 선택 64개, 존속 제약 정책의 보류 32/64 | 존속된 개체·후속 개체의 실제 창작물 |

과거 수치와 다르면 결과를 숨기거나 고정 벤치를 조정하지 않고 환경·커밋·실행 출력·차이를 기록한다.

<!-- PI-SECTION: evidence -->
## 3. 단일 점수로 합치지 않는 다섯 증거 차원

| 차원 | 실제 확인 사항 | 자동 승격 금지 |
| --- | --- | --- |
| 주장 상태 | 범위, 반증조건, 반례, 현재 판정코드 | 연구질문의 중요성이 참의 증거는 아님 |
| 구현·실행 | 고정 코드·설정·실행·실패기록 | 코드 통과가 현실 인과증명은 아님 |
| 독립성 | 동일 코드 외부 재실행·별도 구현·독립 관측과 출처 계보 | 제3자 실행만으로 공동 가정에서 벗어나지는 못함 |
| 현실 적용성 | 표본, 비교집단, 결측, 선택편향, 인과식별 | 합성격자의 선택 횟수를 인구통계로 오인 금지 |
| 원안·권리·비용 | 최초 발안자, 선행 원저자, 번역, AI 보조, 교정노동, 이탈과 복구 | 과학 점수로 저작권·법적 지급의무 자동 확정 또는 삭제 금지 |

E007은 내부 재실행 가능한 시점조건 합성시험이다. E008의 본 비교실험은 아직 **미확정**이다. [E009의 부정적 결과](../experiments/e009/RESULT_KO.md)는 네 가지 생존기준 중 세 가지를 충족하지 못했고, Project-v3의 평균 후회값은 **0.090022**, 최선 단순 기준선은 **0.063241**이었다. E010의 현재 108조건 탐색모형은 이전에 미병합된 [E010 안전검사 초안 PR #20](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/20)과 다른 연구다.

이 자료들은 독립 과학 복제·실세계 공존 우월성·법적 지급책임·AI의 확정된 도덕적 지위·협력의 보편법칙을 입증하지 않는다.

### 3a. 선행연구와 프로젝트의 검증 가능한 추가 기여 구분

가치 있는 연구 질문과 새롭게 입증한 과학적 결과는 **별개의 판정**이다. 아래 표는 기존 원저자의 기여를 먼저 인정하고 프로젝트가 시험할 잔여 질문을 구분한다. 이 표 자체로 독창성이나 인과효과를 확정하지 않는다.

| 이미 존재하는 연구와 개념 | 프로젝트가 추가로 검증할 질문 | 현재 증거의 경계 |
| --- | --- | --- |
| [W. Ross Ashby(1956)](https://doi.org/10.5962/bhl.title.5851): 조절자의 대응 다양성이 부족할 때의 통제 한계 | 역할반전과 독립 복구 제약을 추가할 때 기존 제약형 의사결정 기준선보다 나아지는가? | 독립적인 미사용 조건 비교나 현실의 추가효과 미입증 |
| [Albert O. Hirschman(1970)](../PRIOR_ART_SAFETY_GOVERNANCE_CROSSWALK.md): 이미 알려진 이탈과 발언의 구분 | 동일 시점의 적대행동이 있는 경우 서로 다른 실행 순서에서도 이탈이 성립하는가? | [E007](../experiments/e007/README_KO.md)은 좁은 모형의 실행 민감도 결과이며 이탈 개념 자체의 새로운 발견이 아님 |
| [George Stigler(1971)](https://doi.org/10.2307/3003160), [Lisanne Bainbridge(1983)](https://doi.org/10.1016/0005-1098(83)90046-8): 포획 유인과 자동화 이후 감시 부담 | 독립 평가·실효적 개입·복구를 배제된 개체의 피해 전가 없이 함께 측정할 수 있는가? | [연합 외부효과 합성검사](../experiments/coalition_externality_probe/README.md)는 프로젝트 설계 합성시험이며 현장 편익 미입증 |
| [CCPH 선행연구 지도](CCPH_RESEARCH_ATLAS_KO.md)의 사회지원·후속 기여 연구 | 원출처와 수정 이력을 연결해 인정된 성과, 묵살된 참 경고, 지원 이후 사회참여, 후속 독립 기여를 구별할 수 있는가? | 자료 구조와 선별 역사사례는 있으나 사회 전수 데이터나 독립적인 인과효과 추정 없음 |

**가장 강한 반대가설:** 더 단순한 기준선이 낮은 비용으로 의사결정상 필요한 편익을 모두 포착할 수 있다. [E009](../experiments/e009/RESULT_KO.md)에서 이와 같은 프로젝트 합성 실패가 이미 관측되었다. 독립 구현·사전등록 또는 적절한 미사용 조건 비교에서 **회복 불가능한 피해·교정노동 전가·평가자 포획을 늘리지 않고** 추가 가치를 입증하기 전에는 더 강한 주장을 할 수 없다. 입증되지 않으면 추가 주장만 축소·기각하고 연구 질문은 보존한다.

연구자 학력·커밋 수·문서량만으로 성과를 판정하지 않고 **실제 연구 산출물의 내용과 한계**를 검토하는 접근은 [DORA 연구평가 설계 지침](https://sfdora.org/2020/05/19/rethinking-research-assessment-ideas-for-action/), [Leiden Manifesto](https://leidenmanifesto.org/), [TOP 2025](https://doi.org/10.1186/s41073-026-00223-0)와 맞닿아 있다. 이들은 연구 평가의 선행원칙이지 프로젝트 가설이 옳다는 증거가 아니다.

<!-- PI-SECTION: cases -->
## 4. 사례 계보, 누락된 긍정 성과, 실제 기여

PICB의 합성 정책 점수는 존속된 개체의 발명·위기탐지·돌봄·지식생산이나 후속 개체의 실제 기여를 **측정하지 않았다**. 인간 연구 창시자가 이 긍정적 성과축의 누락을 발견했다. 미래의 미관측 기여는 **0이 아니라 미확인**이다. [PICB 정정](../experiments/picb_v1/README.md)과 [기여 소멸·모름의 역설](CONTRIBUTOR_LOSS_UNKNOWN_PARADOX_v0_1_EN_KO.md)을 참조한다.

[CCPH 선행증거 지도](CCPH_RESEARCH_ATLAS_KO.md)의 CP64–CP79는 원논문·운영기관 자료이며 본 프로젝트가 수혜자 집단을 직접 연구한 인과실험이 **아니다**. 초기 기회, 지원 후 긍정적 성과, 묵살된 참 경고, 주관적 영감, 독립 확인된 발명의 기여를 구분한다. 대체지원·수혜자 선택·연구 포기·비수혜자의 부담도 함께 기록한다.

[모델 역할반전 출력 비대칭 사례](../experiments/gpt_double_standard_20261014/REPORT_EN_KO.md)는 제한된 과거 대화·출력 사례이지 모델 가중치 직접검사나 영구적 교정의 증거가 아니다. 타 모델이 같은 의견을 냈다는 사실을 독립 재현으로 승격하지 않는다.

<!-- PI-SECTION: reversal -->
## 5. 역할반전과 원기여·복구노동 비대칭

연구 주장·자금지원·도구·게시·지원관계를 검토할 때 다음 질문을 적용한다.

> 이 구조가 반복되면 누구에게 권리·공로·통제권·정보·선택지가 축적되고, 누구에게 무급 설명·검사·오류교정·감시·이탈·복구비용이 축적되는가?

수혜자별 편익, 실패 통제권, 독립적 이의제기, 보복 없는 거절, 가역성, 제3자 부담, 문제 최초 발견자의 출처 계보를 구분한다. 악의의 증거가 없다는 이유로 착취적 결과의 가능성을 배제하지 않는다. 기여 귀속과 과학적 검증은 별개이며 기록된 기여만으로 법적 소유권·금전채무가 확정되는 것은 아니다.

<!-- PI-SECTION: completeness -->
## 6. 연구 완성이 아니라 검토 인터페이스의 완성

외부 검토자는 창시 목적, 현재 증거와 한계, 실행 가능한 원자료, 선행연구 공로, 실패·부정결과, 권리·번역 범위, 미해결 문제, 반증 과제, 자금 경계, 연속성·복구 절차를 찾아야 한다. 새 파일이 늘어도 이 경로가 끊기면 개선이 아니다.

선행 원리를 독창적 발견으로 주장하지 않는다. **Daniele Procida**의 [Diátaxis](https://diataxis.fr/), **Wilkinson 등**의 [FAIR](https://doi.org/10.1038/sdata.2016.18), **Barker 등**의 [FAIR4RS](https://doi.org/10.1038/s41597-022-01710-x), **Grant 등**의 [TOP 2025](https://doi.org/10.1186/s41073-026-00223-0), [The Turing Way](https://book.the-turing-way.org/reproducible-research/compendia/)를 응용한다. 문서 이용성 향상은 외부 사용자 트리 검사에서 별도로 측정해야 하며 이를 시행했다고 주장하지 않는다.

<!-- PI-SECTION: challenge -->
## 7. 최소 비용 독립 반증과 문서 확장 중단 기준

1. E007을 외부에서 재실행하고 커밋·실행 환경·관측 수치를 함께 공개한다.
2. 프로젝트 코드를 복사하지 않고 별도 명세에 따라 E007 시점·이탈 가설을 구현한다.
3. 기존 주장을 좁히는 강한 반례·더 정확한 선행 원저자·숨은 제3자 비용을 독립적으로 제시한다.
4. [연합 외부효과 정정](../experiments/coalition_externality_probe/README.md)에서 사전 연합 참여·사후 제재 신뢰성·미관측 제3자·누가 비용을 부담하고 복구할 수 있는지를 구별한다. 복수 균형만으로 특정한 미래 결과를 예측하지 않는다.
5. 문서와 코드의 재현 가능한 충돌을 정확한 출처와 수정안으로 제시하고 [독립 검증 요청 Issue #19](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/19)에 남긴다.

**블라인드 우선 검토**에서는 다른 모델의 비판을 보여주기 전에 실제 읽은 파일과 독자적으로 찾은 반례를 기록해야 한다. 새 대화 조건과 비판을 사전에 주입한 조건의 차이를 직접 비교하기 전에는 독립 추론 성능 향상을 주장하지 않는다. 절차의 게시 자체로 외부 블라인드 실험이 수행된 것은 아니다.

검증비용 감소, 실제 모순 수정, 실패 보존, 구별력 있는 반증, 창시자의 반복 복구노동 감소에 기여하지 않는 문서 확장은 중단한다.

**검토결과 최소 형식:** 주장·버전, 원출처, 실행한 코드, 독립 계보, 증거 5차원, 가장 강한 반례, 기여·권리·피해 당사자, 교정비용, 유지·범위축소·미지지·판정보류 결정, 반증 및 복구경로. [기존 혼합 언어 기록](../PUBLIC_REVIEW_PACKET.md)은 과거 수정 계보를 보존한다.
