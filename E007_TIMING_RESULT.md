# E007 — Timing sensitivity / 시점 민감도
## Original 1 — English
Status: computationally reproduced synthetic result; public summary. Executable sample: [E007](experiments/e007/README.md).

A finite two-agent game compares exit-priority with execute-first timing on the same 72 selected synthetic cases. A fresh isolated run reproduced:
| Measure | Count |
|---|---:|
| History and/or classification changed | 36 / 72 |
| Classification changed | 17 / 72 |
| A-leading classification changes | 8 / 36 |
| B-leading classification changes | 9 / 36 |
| Regression tests passed | 27 |

These are counts in a hand-selected model grid, not real-world probabilities. The result supports only that classifications in this implementation depend on timing semantics. It does not establish coexistence, independence, or an audit architecture as universally superior.

Failure lineage: the original role-reversal sweep varied the wrong target coordinate for one role order; the corrected sweep uses the actual target in both orders. Earlier test-count documentation was stale; the current package has 27 passing tests. A later history-encoding audit found that execute-first logging used the follower's pre-strike activity state; after recording the realized post-strike response instead, history/timing-sensitive cases changed 31/72 -> 36/72 while classification-sensitive cases remained 17/72. Added checks expose limitations of scalar enforcement and unrepresented substitute identity.

Open limits: stochastic enforcement, wider timing/equilibrium regimes, off-path participation, cheap substitution and empirical validation. This run reused project code, tests and grid: it is not independent implementation or independent scientific replication. Public readers can now execute the supplied code and grid in experiments/e007.

Reproduction record: source snapshot 4830a7456989ecf94a1ccf0bc333110915b00912; Python 3.12; pytest 9.1.1. Commands in the isolated candidate: `python -m pytest -q -p no:cacheprovider`; `python timing_probe.py --summary-only --check`. Headline counts were fixed before this rerun, not before the original experiment.

Next falsification: rerun the released package; challenge timing and equilibrium-selection assumptions. A mismatch weakens this computational claim; successful rerunning still does not validate real-world behavior.

## 원문2 — 한국어 대응본
상태: 계산 재현한 합성 결과의 공개 요약. [실행 코드 공개](experiments/e007/README.md).

유한한 두 행위자 게임에서 같은 72개 선택된 합성 조건에 이탈 우선과 선행행동 우선 규칙을 비교했다. 이번 격리 실행에서 행동 경로 또는 분류 변화 36/72, 분류 변화 17/72를 재현했다. A 선행은 8/36, B 선행은 9/36에서 분류가 변했고 회귀 테스트 27개가 통과했다.

이 수치는 선택된 모형 조건의 개수이며 현실 확률이 아니다. 지지되는 주장은 이 구현의 결과 분류가 시점 규칙에 의존한다는 것뿐이다. 공존·독립성·특정 감사 구조의 보편적 우월성을 입증하지 않는다.

실패계보: 최초 역할반전 탐색은 한 역할에서 잘못된 대상 좌표를 변경했다. 수정 탐색은 양쪽 모두 실제 대상 좌표를 변경한다. 과거 테스트 개수 표기는 오래됐으며 현재 묶음은 27개가 통과한다. 추가 history-encoding 감사에서 execute-first가 상대의 공격 전 활성상태를 기준으로 행동을 기록하던 오류를 수정했고, 경로/시점 민감도는 31/72에서 36/72로 바뀌었지만 분류 민감도 17/72는 유지됐다. 추가 검사는 단일 제재값과 표현되지 않은 대체물 정체성의 한계를 드러낸다.

확률적 집행, 더 넓은 시점·균형 조건, 균형경로 밖 참여조건, 저렴한 대체 가능성, 현실 검증은 미해결이다. 프로젝트 코드·테스트·조건을 재사용한 실행이므로 독립 구현이나 독립 과학 재현이 아니다. 공개 저장소 experiments/e007에서 제공된 코드와 조건을 실행할 수 있다.

재현 기록: 원천 스냅샷 d7242191f284d713781129c1720e233c7bd4708d, Python 3.12, pytest 9.1.1. 격리 후보에서 위 두 명령을 실행했다. 기대 수치는 이번 재실행 전에 고정되어 있었지만 원 실험의 사전등록을 뜻하지 않는다.

다음 반증은 공개 묶음 재실행과 시점·균형선택 가정에 대한 공격이다. 수치 불일치는 계산 주장을 약화하며, 일치해도 현실 행동 검증이 되지는 않는다.
