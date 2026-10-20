<!-- PI-LANGUAGE: en-ko | PI-RISE-CUT v0.1.0 | OPERATIONAL EXAMPLE -->
# PI-RISE-CUT v0.1.0 — Minimal Failure Paths / 최소 실패 경로
**2026-10-21 | Version of a new optional diagnostic within PI-RISE. NOT a new research result, safety certificate or actual individual-resource assessment.**

## Original 1 — English | Model and limitations
**Why:** Merely counting grants, AI subscriptions, commits or replicas cannot identify the *minimal combinations of losses* that stop independent research. Existing fault-tree analysis (FTA) and minimal cut sets are an appropriate formal model for a bounded question, not a new invention.

**Proposed Boolean system:** `ACTIVE = HUMAN_AVAILABILITY ∧ RESEARCHER_SUPPORT ∧ SCIENTIFIC_INTEGRITY ∧ RESEARCH_INDEPENDENCE ∧ (LOCAL_COMPUTE ∨ REMOTE_COMPUTE) ∧ (LOCAL_ARCHIVE ∨ PUBLIC_ARCHIVE)`.

**Separate output:** `RECORD_READABLE = LOCAL_ARCHIVE ∨ PUBLIC_ARCHIVE`.

Each symbol is a hypothetical **functioning component**, not a judgment of the actual investigator's capacity, sources of income, moral rights or health. "Researcher support" does not mean that funding is the only or necessary kind of support; it stands for sufficient real-world conditions to engage voluntarily. "Public archive" requires lawful access; publication of private material is neither implied nor authorized.

**Predicted exhaustive cuts under THIS model:**

| Top-level failure | Minimal failure set | Interpretation |
| --- | --- | --- |
| Active independent research cannot operate | `{human_availability}` | No compute substitution for researcher's participation |
| Same | `{researcher_support}` | Loss of conditions for voluntary research |
| Same | `{scientific_integrity}` | Continuing to produce text is not valid research without its evidence boundary |
| Same | `{research_independence}` | Compelled positive verdict cannot satisfy this research objective |
| Same | `{local_compute, remote_compute}` | Both available execution paths removed |
| Same | `{local_archive, public_archive}` | Both accessible provenance paths removed |
| Archived record ceases to be readable | `{local_archive, public_archive}` | Record longevity is distinct from active research |

**Interpretation:** Two types of redundancy preserve optionality for computation or read-access. They cannot duplicate human consent, restore independence by fiat, or make an unvalidated theory true. All conclusions are conditional on the stated Boolean structure and the all-operational starting state.

**Demonstrated method:** `python tools/pi_rise_cutset.py` enumerates all subsets of eight components, finds inclusion-minimal failure sets, and checks each set ceases to be a cut when any one member is restored. `python -m unittest discover -s tests -p 'test_pi_rise_*.py' -v` exercises artificial tests only. Enumeration is capped at 12 components. Passing tests only verifies this model and code.

**Known counterexamples/limitations:** Common-cause failures (one account or power dependency disabling several nominally different paths), unequal evidence value of archives, unavailable restoration credentials, unknown health/care burdens, positive-profit bias, third-party harm displacement and actual grant receipt verification are outside the Boolean example. A reported backup is not necessarily a restorable backup. Source-specific probabilities are unknown, and no risk percentages or investment ROI are claimed. A correct graph is not evidence that the actual research system has the assumed edges.

**Implication for PI-RISE:** Resource expansion should target *observed* bottlenecks and preserve lawful, consent-based researcher continuity; improving one nominal failure path may leave the critical single points untouched. A gap in evidence requires `UNKNOWN/HOLD`, not compulsory research or a funding success claim.

**Methods / original works:** [IEC 61025:2006 fault tree analysis](https://webstore.iec.ch/en/publication/4311) (prior standard, not a permission to redistribute copyrighted text); [NASA fault-tree handbook](https://extapps.ksc.nasa.gov/reliability/Documents/Fault_Tree_Handbook_with_Aerospace_Applications_August_2002.pdf) (minimal cut-set concept); [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) (govern/map/measure/manage and lifecycle risk); [UKRI Research Data Policy, 2026-10-14](https://www.ukri.org/publications/uk-research-and-innovation-research-data-policy/ukri-research-data-policy/) (responsible data stewardship). None proves Project Intersection's thesis or creates funding eligibility.

---
## 원본 2 — 한국어 | 상세 판정 및 활용
### 핵심 관찰
**자금액 합산이 아닌 최소 실패조합 탐지**. 하나가 끊어져도 작동하는 것과, 둘 이상이 끊기면 실패하는 것을 구분.

구조:
- **활성 독립 연구** = 연구자 참여 가능성 ∧ 연구자 지속조건 ∧ 과학적 출처·반례 무결성 ∧ 연구 독립성 ∧ (로컬 연산 ∨ 외부 연산) ∧ (로컬 자료 ∨ 공개 자료).
- **자료 열람 가능** = 로컬 자료 ∨ 공개 자료.
- 실제 사용자 상태의 판정이 아닌 **가정으로 정의한 8요인 예시**. 컴퓨터 고장·자료 읽기 실패·연구자 노동환경 손상을 동일한 '고장'으로 취급하는 현실적 주장 아님.

### 생성된 최소 실패조합: 활성 연구 6개, 보존 자료 1개
1. 연구자 참여 불가능.
2. 자발적 연구에 충분한 지원 조건 소멸.
3. 부정 결과·출처·정정 가능성 무결성 상실.
4. 독립적 연구·발표·거절권 상실.
5. 로컬 연산과 외부 연산이 동시에 사용 불가.
6. 로컬 자료와 공개 자료가 동시에 접근·복구 불가.

**중요:** 1~4는 이 모형의 **단일 실패점**. 5~6은 **이중 실패조합**. 직접 의존성을 명시했으므로 그래프에 넣지 않은 단일 계정·공통전력·공동소유권·접근권 문제는 발견하지 못함.

**과학적 경계:** IEC·NASA의 결함수 방법론 응용. PI-RISE만의 신규 수학 원리나 실제 중단확률의 발견 아님. 누락된 관계는 안전의 증거가 아니라 **미모델링**. 확률·실제 후원액·복구 성능·개별 건강상태 추정 금지.

### 의사결정 응용
- 연구자가 없어도 복구할 수 있다는 주장보다 **연구자 존속·권리·동의의 비대체성** 분리.
- 연산 서비스 한 곳의 가격 인상만으로 모든 연구가 멈추는지를 확인하는 대신 실제 독립된 대체경로 시험.
- GitHub 파일이 존재한다는 이유로 독립 로컬 복원이 가능하다는 주장 금지.
- 실제 입금 없이 지급예정 장부로 연구 가용기간 연장 판정 금지.
- 자금 제공자가 연구 결과를 통제하면 예산이 충분해도 연구 목적 달성 조건에 위배.

**이 모듈의 v0.1.0은 개념·코드 검증 단계.** PI-RISE 상위 운영규약 v0.1.0, PI-RAMP 자료개선 v0.6 등 기존 버전과 구분. 실환경 의존관계·실제 복구 시험·독립 검토 완료 전에는 현실 성공 주장 불가.
