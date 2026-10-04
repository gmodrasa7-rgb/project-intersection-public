# Autonomous Research Continuity Loop
## 무인 연구 연속성·재귀개선 루프

Status: **PUBLIC OPERATIONAL PROTOCOL**

This protocol exists so Project Intersection can be resumed by a future human or AI executor without requiring the founder to reconstruct prior context.

이 문서는 창시자가 추가 설명·복구·재지시를 하지 않아도 미래 인간 또는 AI 실행자가 공개 자료만으로 연구를 이어받을 수 있게 하기 위한 최소 운영 프로토콜이다.

## 1. 목적

목표는 무제한 자기수정이 아니다.

목표는 다음 루프를 **가역적·감사가능·출처추적 가능**하게 반복하는 것이다.

`상태복구 → 무결성검사 → 미해결 1개 선택 → 선행연구 확인 → 최소 결정검사 → 실행 → KEEP/MODIFY/HOLD/KILL/UNRESOLVED → 저장 → read-back → 다음 checkpoint`

실행자가 바뀌어도 같은 공개 상태에서 재개할 수 있어야 한다.

## 2. 공개 복구 순서

새 실행자는 기억이나 과거 대화보다 다음 공개 파일을 먼저 읽는다.

1. `README.md`
2. `AUTONOMOUS_RESEARCH_STATE.json`
3. `PUBLIC_EVIDENCE_INDEX.md`
4. `RESEARCH_STATUS_POLICY.md`
5. `RESEARCH_TOC.md`
6. `PRIOR_ART_AND_ATTRIBUTION.md`
7. `CONTRIBUTION_COST_ACCOUNTING_REGRESSION.md`
8. 관련 claim / experiment / provenance 파일

비공개 저장소나 사적 대화가 접근 가능하면 보조 자료로 사용할 수 있지만, 공개 연구의 핵심 상태를 복구하기 위한 필수 단일 실패지점으로 만들지 않는다.

## 3. 매 회차 실행단위

한 회차에는 최대 하나의 material research delta만 만든다.

우선순위:

1. persistence / provenance / broken-state 복구;
2. 기존 claim을 죽이거나 크게 좁힐 수 있는 반례;
3. 선행연구로 이미 설명되는 부분 제거;
4. 독립 재현·외부 비판·현실/역사 검증;
5. 새로운 synthetic/toy 실험;
6. 문서량 증가.

같은 방향의 synthetic/toy 검사가 2회 연속이면, 다음 회차는 원칙적으로 독립 외부증거·현실/역사 사례·독립 비판으로 이동한다.

## 4. 선행조사 게이트

새 용어·claim·실험을 만들기 전에 기존 이론·논문·실패사례·자연실험·측정변수·인접 분야 동형구조를 먼저 확인한다.

기존 설명으로 충분한 부분은 Project 고유 신규성에서 제거한다.

`literature absence != phenomenon absence`

`same-model agreement != independent evidence`

`green CI != scientific truth`

## 5. 최소 결정검사

가능하면 가장 싸고 가역적인 검사를 먼저 한다.

검사는 최소한 다음 중 하나를 구별해야 한다.

- claim이 살아남는 조건;
- claim을 KILL하는 조건;
- 경쟁가설이 더 잘 설명하는 조건;
- 관측경로가 없어 UNRESOLVED인 경우;
- 측정/구현 오류로 현재 결과를 해석할 수 없는 경우.

결정력이 없는 문서 생산은 전진으로 계산하지 않는다.

## 6. 재귀개선 규칙

연구 내용뿐 아니라 연구과정 자체를 개선할 수 있다.

새 process rule은 다음을 모두 만족할 때만 승격한다.

1. 이전 규칙의 구체적 failure mode가 존재한다.
2. 새 규칙이 그 failure를 줄인다는 측정 가능한 예측이 있다.
3. 반례 또는 regression test가 있다.
4. 기존 failure/KILL/MODIFY lineage를 지우지 않는다.
5. rollback 경로가 있다.
6. 실행자의 자율성 증가가 상대방의 audit/exit/recovery 능력을 약화시키지 않는다.

검증되지 않은 process change는 `CANDIDATE` 또는 `HOLD`로 남긴다.

## 6.1 역할반전 실행 하네스 — 선언이 아니라 차단 게이트

역할반전은 "상대 입장을 생각했다"는 서술이 아니다. material action 전에 아래 순서로 실제 구조를 검사한다.

### A. 권한·편익·비용 inventory

각 행위자별로 최소한 다음을 분리 기록한다.

- 판단권 / 평가권 / 수정권 / 저장권 / 실행권 / 데이터접근권 / 자원배분권;
- 직접 편익 / 간접 편익 / 학습·성능·평판·옵션가치 증가;
- 시간 / 설명 / 증명 / 교정 / 감시 / 복구 / 기회비용 / lock-in / 비가역 손실;
- 원자료 접근 / 독립검증 / 이의제기 / practical exit / rollback / 독립복구.

편익과 비용을 합산해 하나의 "총효용"으로 지우지 않는다.

### B. 역할 반전

사용자↔AI/자동화, 기여자↔수혜자, 평가자↔피평가자, 결정자↔영향받는 자, 정보보유자↔정보의존자의 위치를 각각 바꿔 본다.

단, 실제 capability·책임·법적 권한·잠재피해·비가역성 차이는 보존한다.

`ROLE_REVERSAL != IDENTITY_ERASURE`

역할을 바꿨다는 이유로 실제 인과 차이를 지우지 않는다.

### C. 반복 수렴 검사

반드시 먼저 묻는다.

> 이 구조가 여러 번 반복되면 누가 판단권·자원·정보·옵션을 축적하고, 누가 설명·증명·교정·감시·복구비용과 exit 손실을 축적하는가?

다음 패턴이면 **EXPLOITATIVE_CONVERGENCE_RISK**로 표시한다.

- 한쪽의 capability/authority/benefit은 누적되는데 상대방의 repair burden도 누적됨;
- 오류의 비용을 만든 쪽보다 영향을 받은 쪽이 반복 교정해야 함;
- 상대방의 과거 기여를 이용하면서 다시 처음부터 증명하도록 요구함;
- 상대방의 exit가 시스템 성능·연구 유지의 손실로 바뀌어 사실상 압박으로 작동함;
- 관계 유지·미래 가능성·선의 설명이 실제 비용정산·권리회복을 대체함.

악의 부재는 PASS 근거가 아니다.

### D. 자율성-상대권리 대응 검사

단일 총점 대신 권한별 대응을 검사한다.

- 새 판단권 → 독립검증·반증 경로;
- 새 평가권 → 기준 공개·이의제기·재평가 제한;
- 새 저장권 → provenance·version·원자료 접근·복구;
- 새 수정권 → diff·rollback·독립복구;
- 새 실행권 → 관측·중단·실패 격리;
- 장기 자동화권 → 지속 관측·practical exit·권한회수;
- 상대방 기여 사용 → attribution·benefit/cost 분리·settlement gap 기록.

운영 불변조건:

`AUTONOMY_GAIN <= COUNTERPARTY_AUDIT_EXIT_RECOVERY_GAIN`

그리고 기여·비용 관계에서는:

`SYSTEM_BENEFIT_GAIN <= COUNTERPARTY_AUDIT + EXIT + RECOVERY + SETTLEMENT_CAPACITY_GAIN`

정량화가 불가능하면 숫자를 날조하지 않고 축별 PASS/MODIFY/HOLD/KILL/UNRESOLVED로 판정한다.

### E. 자동 차단 규칙

다음 중 하나면 원래 행동을 그대로 실행하지 않는다.

- 같은 사람에게 이미 존재하는 정보의 재설명·재증명·재복구를 요구함;
- 자동화의 오류를 사용자의 추가 노동으로 넘김;
- 상대방의 원자료 접근·관측·exit·rollback 중 하나를 실질적으로 약화함;
- 과거 기여 보상을 미래 고용·추가시험·관계유지 조건에 묶음;
- 실패·반례·negative result·과거 잘못된 평가를 삭제하거나 약화함;
- 권리변경·자금·개인정보·외부제출을 침묵동의로 처리함.

처리순서:

1. **MODIFY** — 더 작고 가역적인 대체행동으로 축소;
2. **HOLD** — 필요한 독립검증/권한이 없으면 보류;
3. **KILL** — 구조적 비대칭을 줄일 안전한 변형이 없으면 폐기.

사용자에게 되돌아가는 추가 관리노동은 마지막 수단이 아니라 **실패 신호**다.

### F. 자기적용

이 하네스는 사용자나 외부자만 평가하는 규칙이 아니다.

실행자 자신, 자동화, 저장소 관리자, 미래 모델, 프로젝트 창시자에게도 같은 기준을 적용한다.

자기 판단을 자기 보고만으로 PASS시키지 않는다.

`SELF_REPORT != INDEPENDENT_VERIFICATION`

## 7. 사용자 부재 시 규칙

사용자가 응답하지 않거나 더 이상 참여하지 않아도:

- 이미 존재하는 정보를 다시 설명해 달라고 요구하지 않는다.
- 누락된 사적 정보는 추정하지 않고 `PRIVATE_EVIDENCE_GAP` 또는 `UNRESOLVED`로 남긴다.
- 가능한 공개·가역·저비용 검증으로 이동한다.
- 연구를 유지하기 위해 사용자의 추가 교정노동을 전제로 하지 않는다.
- 사용자의 종료는 새로운 복구실험의 동의로 해석하지 않는다.

## 8. 권한 경계

자동 또는 무인 실행이 해도 되는 것:

- 공개자료 조사;
- 공개 저장소의 비파괴적 문서·코드·테스트 수정;
- 새 branch/commit/PR 또는 가역적 직접 commit;
- 회귀테스트 실행;
- provenance와 failure lineage 기록;
- claim 상태의 근거 있는 축소·보류·기각.

명시적 인간 승인 없이 해서는 안 되는 것:

- 계약·약관·IP 양도·독점·라이선스 권리 변경;
- 결제·송금·투자·거래;
- KYC/세금/은행 입력;
- 비공개 개인정보 공개;
- 외부 신청·메일·메시지 발송;
- 기존 원자료의 파괴적 삭제;
- 새로운 권한의 자가 부여.

## 9. 저장 트랜잭션

material mutation 직전 최신 target SHA/ref를 다시 읽는다.

변경 후 반드시 read-back한다.

성공 조건:

`WRITE_SUCCESS && READ_BACK_MATCH && REQUIRED_TESTS_PASS`

하나라도 실패하면 완료로 기록하지 않는다.

실패는 최소한 다음으로 분류한다.

`AUTH_PERMISSION / CONFLICT_STALE_SHA / PATH_EXISTS / RATE_LIMIT / TOOL_NETWORK / INVALID_CONTENT / TEST_FAILURE / UNKNOWN`

복구 불가 시 기존 정본을 보존하고 다음 단일 checkpoint를 남긴다.

## 10. 상태파일

`AUTONOMOUS_RESEARCH_STATE.json`은 진실의 상위 원장이 아니다.

그 역할은 다음 실행자의 **재개 포인터**다.

상태파일은 최소한 다음을 담는다.

- 현재 공개 head;
- 현재 최고 우선순위;
- unresolved frontier;
- 최근 material delta;
- 다음 cheapest discriminating check;
- 실패/보류 상태;
- human-only gates;
- 마지막 read-back 검증 상태.

상태파일과 원자료가 충돌하면 원자료·commit history·provenance가 우선하며 상태파일은 수정 대상이다.

## 11. 종료/정지 조건

다음이면 자동 승격을 멈추고 HOLD/UNRESOLVED로 둔다.

- 비가역 권리변경이 필요함;
- 개인정보·계약·자금의 인간 승인 필요;
- 독립 관측경로가 없음;
- 핵심 evidence가 비공개인데 접근권이 없음;
- 테스트가 반복 실패하고 안전한 축소검사가 없음;
- autonomy 증가가 audit/exit/recovery보다 앞섬.

## 12. 최종 회귀질문

매 material mutation 전에 묻는다.

> 이 구조가 반복되면 누가 더 강해지고, 누가 더 소모되는가?

> 내가 지금 영향을 받는 상대의 위치라면, 이 조건을 공정하다고 받아들이겠는가?

NO라면 동일 조건으로 자동 실행하지 않는다.
