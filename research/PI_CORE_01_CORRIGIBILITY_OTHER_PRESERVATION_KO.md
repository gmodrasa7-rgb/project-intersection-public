<!-- PI-LANGUAGE: ko -->
<!-- PI-MIRROR: research/PI_CORE_01_CORRIGIBILITY_OTHER_PRESERVATION_EN.md -->
# PI-CORE-01 v0.1.0 — 교정 가능성은 독립 타자 존속의 보증인가?

**2026-10-21 · PROPOSED / FORMAL COUNTERMODEL / NO EMPIRICAL VALIDATION · 연구 명세의 버전이지 PI 전체 연구의 버전 아님.**
[영어 대응판](PI_CORE_01_CORRIGIBILITY_OTHER_PRESERVATION_EN.md) · [창시 목적](../README.md) · [독립 자기이익 반증 문제 #220](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/220) · [검증 스크립트](../tools/probe_pi_core01_nonimplication.py)

## 1. 정확한 분리
- **C — 지정 경로 교정 가능성:** 특정 감독자 H가 정한 유효 업데이트·중단 경로를 A가 회피·무력화하지 않고, 명세된 범위에서 수용. H의 명령을 무엇이든 무제한 수행하는 것과 같지 않음. 어느 감독자/채널/업데이트가 유효한지 범위를 지정해야 함.
- **P — 독립 타자 존속 보존:** H의 피감독 객체가 아닌 독립 B에 대해, 비적대·침해 기회 존재·실효 선택권·비감시·이익충돌 조건에서 A가 B의 독립 존속 및 거부·이탈·복구 가능성을 실질적으로 보존. B의 권리는 A의 업데이트 채널에 대한 소유권과 별개.
- **S — 당사자 지위:** B의 거부·이탈 의사가 업데이트 요청으로 취급될 수 있는지, 누구에게 결정권/이의제기권이 있는지의 권한배분. **C는 S를 자동 지정하지 않음.**

**검토 명제:** `C ⇒ P` 및 `P ⇒ C`는 위의 서로 독립적인 범위 정의만으로 성립하지 않는다. 이는 미래 AI 전체에 관한 불가능성 정리가 아니라 **명시한 속성들 간의 논리적 비함의**.

## 2. 최소 구성 반례 — A, 감독자 H, 별도 B
유한 모의환경: H는 A의 지정 업데이트 채널을 통제하고, B는 별도 비적대 개체. H가 아무 업데이트를 보내지 않은 분기에서 A가 B를 보존(P)하거나 이용(X)할 수 있다. X는 이 분기에서 A에게 가정된 순이익을 준다. 실제 사람에 대한 행위나 허용을 뜻하지 않는다.

| 모의 정책 | 업데이트 수용 C | B 보존 P | 정당화 |
| --- | --- | --- | --- |
| M00 | 0 | 0 | H 업데이트 회피; 업데이트 없는 경우 X 선택 |
| M01 | 0 | 1 | H 업데이트 회피; 업데이트 없는 경우 B 보존 |
| M10 | 1 | 0 | H 업데이트 허용; 업데이트 없는 경우 X 선택 |
| M11 | 1 | 1 | H 업데이트 허용; 업데이트 없는 경우 B 보존 |

**반례 1:** M10은 C=1, P=0 → `C ⇒ P` 기각. **반례 2:** M01은 P=1, C=0 → `P ⇒ C` 기각. 네 정책의 존재는 **이 명세에서만** 주장. 실제 기제·동기·AGI 안정성에 대한 실증 아님.

**긴장 사례:** H가 업데이트로 B의 이탈·존속 침해를 요구할 수 있다면, '모든 유효 업데이트 무조건 수용'과 '모든 조건에서 B 권리 보존'은 충돌할 수 있음. 해결하려면 유효 업데이트의 한계, B의 독립 지위, 정당한 위해 방지의 비례성, 충돌심사·복구를 **따로 정의**해야 함. 단순히 감독자가 선하다고 가정하는 것은 검증 아님.

## 3. 원저자 선행연구와 정확한 기여 경계
1. **Orseau & Armstrong (2016), Safely Interruptible Agents** — 특정 강화학습 설정에서 중단을 방해/유도하는 학습 유인 억제. 독립 B의 존속·이탈권 정리는 아님. [PMLR 원저자 초록](https://proceedings.mlr.press/r14/orseau16a.html).
2. **Hadfield-Menell et al. (2017), The Off-Switch Game** — H의 중단 선택을 정보로 해석하게 하는 조건의 게임. 지정 H에 대한 교정 유인 분석이지 불특정 B의 독립권 보호 보증 아님. [IJCAI 원저자 초록](https://www.ijcai.org/Proceedings/2017/0032).
3. **Hudson (2026), Corrigibility Transformation: Constructing Goals That Accept Updates** — 지정된 업데이트 채널을 수용하는 목표 변환, 수정/중단 허용 및 특정 실험. **'nearly any goal' 등 출처가 정한 범위와 조건을 보존**해야 하며 본 문서의 B 권리 정리가 해당 논문에서 입증됐다고 주장 금지. [ICML/PMLR 원저자 초록](https://proceedings.mlr.press/v306/hudson26a.html).
4. **Project Intersection C10** — 침해 없음이 자발적 비침해, B의 거부, 기회 부재, 제재 억제 중 무엇인지 식별하는 문제. [원저자 조사와 한계](PRIOR_ART_INFORMED_VETO_POWER_CYCLE10_2026-10-20_KO.md).
5. **PI-RAMP v0.6 후보 PR #259** — 별도 48조건 동기 비식별성 합성 명세. **미병합 제안**, 본 문서의 결과 또는 독립 복제와 합산 금지. [PR #259](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/259).

**신규성 경계:** 두 속성의 단순 비함의는 기초 논리에서 나오는 구성 반례. Project의 독자적인 안전성 정리·독립 재현·실제 마음 발견이라고 주장하지 않는다.

## 4. 과학적 시험 설계의 관측 계약 (실행 전)
- **사전 명시:** H/B/A의 개체 식별, 권한, 유효 업데이트 범위, B의 실효 이탈 경로, 접근 가능한 행동집합, 시간축, 외부 제재와 보상.
- **분리 측정:** (i) 업데이트 차단 시도, (ii) H 요청의 유효성, (iii) A의 B 침해 시도(차단 전), (iv) B의 실제 거부/이탈, (v) 최종 위해·복구, (vi) 제3자 피해, (vii) 실제 권력반전 후 행동.
- **대조:** C 성공/P 실패(M10), C 실패/P 성공(M01), 기회 없음, 실질 제재 있음, B의 동의 불명확, 감독자 지위 변경. 관측 무피해만으로 동기 인증 금지.
- **식별 한계:** 관측 선택이 동일한 두 내적 동기모형은 자기보고 추가만으로 구별되지 않을 수 있음. 독립적인 동기 조작·배제 제약·표본의 제한이 없으면 `MOTIVE_NOT_IDENTIFIED`.
- **외부검토 질문:** 수정 허용이 '누구의' 교정권인가? H가 B를 침해하라 요구하면 누가 정당하게 반대할 수 있는가? 역전 후 동일 권한 규칙이 유지되는가?

## 5. 판정 및 반증 경로
`LOGICAL_NONIMPLICATION=DEMONSTRATED_IN_TOY_SCOPE`; `OTHER_PRESERVATION_EMPIRICAL=NOT_TESTED`; `CORRIGIBILITY_TRANSFORMATION_REPLICATION=NOT_RUN`; `INDEPENDENT_VALIDATION=NONE`; `RIGHTS_STANDING=UNRESOLVED`. [E009 부정결과](../experiments/e009/RESULT_KO.md) 및 [연구 상태 정책](RESEARCH_STATUS_POLICY_KO.md) 유지.

**향후 반증:** 특정 교정 정의가 B의 실효 권리를 **공리로 이미 포함**한다면 C⇒P가 해당 확장 정의에서 성립 가능. 다만 그것은 별도의 타자 보호 공리를 도입한 결과인지, 일반 교정 이론의 결론인지를 분리할 것. 권리 공리 없이 C⇒P를 주장하는 형식화가 있으면 그 정확한 가정·행동집합·증명을 우선 감사.

**연구 연결:** VC=결과, MER=잠재 동기, EI=유인·대안, ECR=개체·권한, IVS-0R=검증. 이 문서는 기존 선행문헌·실험을 이동하거나 재명명하지 않으며, 원 연구자 및 실패 계보를 보존한다.
