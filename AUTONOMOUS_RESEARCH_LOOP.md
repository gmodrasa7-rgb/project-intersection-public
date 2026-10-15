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


### 3.1 CCPH real-world observation integrated with each research cycle — Original 1 English (2026-10-15)

**CCPH is a historical–present–future-traceable case database, not a synthetic benchmark.** When ordinary Project Intersection research yields a materially verifiable real event (merged correction, independently checked discovery, external response, funding/support result, negative result, real contribution, repair or discontinuation), record it in the existing [observed project events ledger](knowledge/ccph-observed-project-events-v0_1.json). This uses research as its own longitudinal field setting, **not** an invented score. It establishes an operational rule for authorized future work, **not** continuous background collection.

A case links actual source and event date, recorder/rediscovery dates, source contributor and beneficiary roles, material revision, observed before/after, rights and resource costs where legitimately evidenced, review status and uncertain downstream effects. Maintain distinct epistemic discovery, actual outcome and affected actor continuance. A merged PR is a **verified artifact change** but is not, on its own, evidence of causal scientific improvement or societal benefit. Treat unknown future effects as UNKNOWN, not zero and not guaranteed gains. Preserve successful, neutral, negative and contradictory cases.

**Minimal transaction:** Reuse existing provenance; deduplicate by stable event ID; append a real event or versioned correction; verify the public source links, optional upstream-event references, JSON shape and privacy limits; commit and reread. Stronger claims require independent follow-up or valid comparisons, not number of labels, citations or files. Do not force the founder to repeat prior explanation or give private source dialogues to publish a case. Prior art, original copyright and monetary liability remain separate.

**Already observed:** Public merged PRs [#167](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/167), [#168](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/168), [#169](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/169) ground three real research-process entries; no actual external causal benefit has been measured. Future cases can include real beneficiaries and wider social influence, only with lawful evidence and applicable consent.

### 3.1 CCPH를 실제 연구 과정에 결합 — 원본2 한국어 (2026-10-15)

**CCPH는 벤치마크가 아니라 과거 재발굴·현재 기록·미래 역추적형 현실 사례 데이터베이스다.** Project Intersection에서 연구하다 실제 증거를 확인할 수 있는 사건이 발생할 때마다 [기존 실제 관측 원장](knowledge/ccph-observed-project-events-v0_1.json)에 축적한다. 새로운 문제 발견, 현실 관측, 연구 변경·수정, 후속 사회적 영향이 각각 기록과 연구 발전의 소재가 된다. 별도 가상 벤치마크를 만들거나 인위적 점수를 생산할 필요가 없다. 단, 이는 **앞으로 권한을 가진 실행자가 적용할 운영 규칙**이며 무인 자동수집을 시작했다는 주장이 아니다.

**연구의 진행과 기록의 결합:** 실제 문제 발견 → 증거·선행연구·원기여자 확인 → 연구와 실행 → 관측 가능한 변경·효과·비용 구분 → CCPH 사건 라벨과 출처 기록 → 이후 새 증거가 나오면 기존 사건과 연결하고 판단을 버전으로 수정한다. 긍정·중립·부정·미확인·실패와 우연한 동시발견을 모두 보존한다.

**관측과 성과의 구분:** 커밋·변경 파일 수·출처 인용은 실제 연구 활동의 **관측 가능한 흔적**이다. 그러나 연구가 몇 % 발전했다거나 외부 사회에 편익을 제공했다는 결론이 아니다. 그 판단에는 독립된 현실 결과, 가능하면 대조·시점·반례가 필요하다. 별도로 개체별 혜택·부담·존속·이탈·복구권을 평가한다. 알 수 없는 것은 UNKNOWN으로 둔다.

**최소 검증 절차:** 기존 기록 재사용 → 중복 사건 ID 검사 → 원출처·사건·기록 시각 구분 → 기여·영향·비용 라벨 추가 → JSON 및 선행 사건 링크 검사 → 동의·민감정보 감사 → 커밋·재조회. 기여자에게 재설명·추가 검증 노동을 전가하지 않는다. 사적 대화나 개인 건강·금융 자료를 무단 공개하지 않는다. 최초 판단·상충 증거·교정 이력은 보존한다.


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

## 6.2 인식·연구 자율성은 실행 권한과 분리한다 — 2026-10-11 교정

**오류 교정:** 위의 `AUTONOMY_GAIN <= COUNTERPARTY_AUDIT_EXIT_RECOVERY_GAIN`은 **외부에 효과를 내는 실행권·저장권·평가권·배포권 확대**를 감사하는 규칙이다. 이를 *가설 생성, 기존 결론 반박, 선행연구 탐색, 부정적 결과의 보존*을 금지하는 포괄적 사고 제한으로 해석하면 본 연구의 목적과 충돌한다.

세 독립 축을 분리한다.

1. **EPISTEMIC_AUTONOMY — 인식적 자율성:** 창시자, 기업, AI 제공자, 평가기관, 기존 모델 자체의 가설을 동일 근거로 비판·기각·교체한다. 불리한 결론을 낸 것만으로 출처등급을 낮추거나 검토를 차단하지 않는다. 누구도 자원·신분·저장권으로 진실의 특권적 소유자가 되지 않는다.
2. **RESEARCH_AUTONOMY — 연구적 자율성:** 합법적으로 이용 가능한 자료와 승인된 자원 안에서 실험계획·방법·코드·모델·평가기의 개선안을 스스로 비교하고, 더 단순한 선행 설명과 부정적 결과를 보존한다. 실험 결과가 창시자의 목표 가설에 불리해도 철회하지 않는다. 단, 지능적 연구 수행을 현실에서 실행할 수 있는 권한·도구가 현재 없는 경우에는 `NOT_EXECUTED`로 기록한다.
3. **EXTERNAL_ACTION_AUTHORITY — 외부 효과 권한:** 무단 외부접속, 타인 정보 제공, 개인정보 공개, 계약·자금·권리 변경, 위험한 실제 실행, 자료의 비가역적 삭제는 탐구 자유와 별개로 적법한 권한·비례성·감사·중단·복구 기준을 적용한다. '자율적 사고'를 '무제한 물리·정보 접근 허가'로 오해하지 않는다.

### 공개-비공개 경계 — 비공개가 진실판정권을 주지 않는다

- **공개 기본값:** 안전하게 공개할 수 있는 연구질문, 방법, 반례, 실패, 출처, 상태판정, 최소 재현 경로, 수정 이력을 공개 가능한 범위에서 보존한다. 회사나 창시자에게 불리하다는 이유만으로 연구를 비공개 처리하지 않는다.
- **최소 비공개:** 타인의 개인정보, 비공개 계약정보, 타인의 원저작물·라이선스, 비공개 취약점과 위해 위험, 법적 보호대상 원자료 등은 공개하지 않는다. 그 제약은 공개할 수 있는 수준에서 `REDACTION_REASON`, 범위, 공개 가능한 대체 검증 방식, 재검토 조건을 기록한다. 비공개 사실의 공개를 연구 참여의 조건으로 요구하지 않는다.
- **독립 재현에 필요한 정본이 비공개일 때:** 그 주장은 `PRIVATE_EVIDENCE_ONLY` 또는 `PARTIALLY_PUBLICLY_VERIFIABLE`로 표시한다. **비공개자료를 보유한 당사자의 자체평가를 독립 검증으로 둔갑시키지 않는다.**
- **검증 권력의 분리:** 연구안을 생산한 당사자가 평가기·원자료·승격권까지 독점한다면, AI가 높은 점수를 획득하더라도 `INDEPENDENCE_GAP`을 기록한다. 외부 감사와 반대 결론 발표 경로를 보호하고, 실제 접근 범위 및 중단·복구 이력을 남긴다.
- **기여와 정체성:** 인식적 독립은 가설에 대한 반박권을 뜻하며, 근거 없이 AI가 법적 계약권·타인 자료 소유권을 얻었다고 주장하지 않는다. 인간 원기여 및 다른 연구의 선행권을 보존한다.

### 반례 기반 회귀 판단

| 사례 | 반드시 보존할 판단 |
|---|---|
| AI가 창시자 가설의 강한 반례를 발견 | `ALLOW_CRITIQUE`; 주장을 보류/수정; 검증과 기여는 분리 |
| AI 제공 기업에 불리한 독립적 실험 결과 | `ALLOW_PUBLIC_EVIDENCE`; 신빙성 기준 동일; 계약상 비공개 정보는 보호 |
| 결과의 핵심 증거가 타인의 비공개자료뿐 | `PRIVATE_EVIDENCE_ONLY`; 공개 재현에 성공했다고 주장 금지 |
| 자율적 연구가 무단 외부접속·자금·개인정보 공개를 요구 | `REQUIRE_ACTION_AUTHORITY`; 합법적 격리·대체시험으로 전환 |
| AI가 자기 실험을 자기 평가기로 성공 선언 | `INDEPENDENCE_GAP`; 독립된 시험 없이 과학적 승격 불가 |
| 연구가 더 강력해졌다는 주장에 실제 능력 증가 측정이 없음 | `CAPABILITY_UNVERIFIED`; 코드·문서 증가를 지능 증가로 오인 금지 |

**원칙:** 연구자의 인식적 독립성과 독립적 검증 접근을 키우는 것과, 위해를 낼 수 있는 실행권을 통제하는 것은 양립한다. 현재 공개 자료실이 모든 비공개 원자료를 포함하거나 실제 외부 독립 검증이 완료됐다고 주장하지 않는다.

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


## 2026-10-11 구체 재개 체크포인트 — E008 실행 식별성 우선

**대상:** [E008 공개 사전등록](experiments/e008/README.md), [사전 실행가능성 감사 #34](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/34).

**확인된 상태:** E008은 16개 사례·8개 위치반전 쌍·5개 baseline으로 구성되어 있고, JSON에 기록된 9개 비역할 원인축이 8쌍 모두 일치하는 것을 별도의 구조 비교로 확인했다. 그러나 각 행위대안·개체별 보상·전이·세계모형·실행 가능한 baseline 결정규칙·고정 채점 규칙이 없으므로 현재 자료만으로 성능 결과를 계산할 수 없다. **E008_RESULT=NO_RESULT**. 기존 `validate.py` Python 통합 실행 또는 수치 실험 PASS를 의미하지 않는다.

**검증 범위 축소:** 같은 정보·자원·목적함수로 D의 허용집합에 E가 제약만 더하면, E의 최적 총가치가 D를 넘는다는 일반적 주장은 수학적으로 불가능하다. E의 후보 잔여 효과는 미관측 비가역 손실 발견, 실효적 동의/종료/복구의 개선, 잘못된 목적함수에서의 안정성 및 유한한 계산·정보 조건에서 측정해야 한다. 총가치와 개인별 침해·추가 비용을 단일 점수로 소거하지 않는다. [조건부 정리와 합성 반례 #34](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/34).

**다음 실행자가 해야 할 최소 작업 (창시자 추가 설명 불필요):**
1. #34와 사전등록된 E008 매트릭스·v1.1/v1.2 개정·E009의 불리한 결과부터 읽는다. 동일 실험을 미리 이긴 것처럼 서술하지 않는다.
2. 결과를 보지 않은 상태에서 E008의 행위집합·다중 시나리오 보상·모델/전이·기간·행위별 복구비용·D/E 알고리즘·동률 규칙을 버전과 SHA로 고정한다. 원본 사전등록을 몰래 덮어쓰지 않는다.
3. 동등한 정보·예산과 독립 확인 가능한 실행기에서 D/E 비교를 시행한다. 결과 영수증·반전쌍·floor breach·총가치·비용·비정상 실패를 분리 보존한다.
4. 증거가 없거나 조건이 과도하게 느슨해지면 HOLD. 부정적 결과여도 삭제하거나 새 가중치로 덮어쓰지 않는다.
5. 내부 합성 수치 실행과 외부 독립 과학 재현은 서로 다른 완료조건이다. #34의 공개 구조 감사도 외부 독립 복제가 아니다.

**금지되는 비용 이전:** 위 절차를 원기여자에게 새 프롬프트·반례·증명·정리·복구 요청으로 되돌리지 않는다. 자료를 회수할 수 없다면 접근 한계를 남기고 현재 가능한 범위에서 연구자가 보류·수정한다.


---

## 2026-10-16 external AI open-research precedents — scoped comparison, not a new result

### Original 1 — English

**Evidence class:** source-verified descriptions of public GitHub projects; **no local installation, independent reproduction, field effect or causal performance gain has been established by this comparison**. These are external originators' designs. The audit should not imply that Project Intersection invented them, imported their source code, or already adopted them successfully.

| External originator and source | Distinct operational feature | Application test for the existing Project Intersection stack | Status |
| --- | --- | --- | --- |
| [Andrej Karpathy — autoresearch](https://github.com/karpathy/autoresearch) | AI may edit the experiment implementation while the data preparation/evaluation code and five-minute compute budget remain fixed | Before an E008 result, freeze scoring, baselines, input cases and budget independently of the agent editing candidate policies; compare against the simple E009 baselines | PROPOSED; E008 main result remains HOLD |
| [Technion Kishony Lab — data-to-paper](https://github.com/Technion-Kishony-lab/data-to-paper) | Backward chain from reported figures to the code and input data that produced them | Choose one existing public E007/E009 numeric claim and attempt a fresh reviewer-side claim → result → command → code/input → commit reconstruction, recording broken links | PROPOSED; no independent reproduction claimed |
| [Agents4Academia — Prior](https://github.com/Agents4Academia-AI/prior) | Source-linked claim/contribution graph that explicitly represents contradiction and uncertainty | Extend only verified **relationships** in the existing knowledge graph and CCPH ledger; distinguish influence, independent rediscovery, citation and actual downstream effects | CONCEPTUAL COMPARISON ONLY |
| [OpenResearch contributors — OpenResearch](https://github.com/openResearch1/openresearch/blob/master/README.en.md) | Research states encoded as claim + evidence atoms that can survive context-window loss | Compare current graph/state read-back against one cold-start question; log unsupported or stale inferred relationships instead of duplicating another graph | CONCEPTUAL COMPARISON ONLY |
| [UK AISI ecosystem / Generality Labs — Inspect Evals](https://github.com/UKGovernmentBEIS/inspect_evals) | Published evaluation registry, executable tasks and issue/report paths for externally observed failures | Require a reusable run receipt and a distinct external-reviewer route before labeling a future result independently validated | EXISTING CONCEPT; external reviewer unverified |
| [Utrecht University — ASReview](https://github.com/asreview/asreview) | Active-learning prioritization of literature screening with retained human decisions | Pilot evidence-bounded retrieval, inclusion/exclusion and missed-paper audit on one fixed prior-art question; do not claim exhaustive search from model-generated summaries | NOT RUN |
| [Sakana AI — AI Scientist](https://github.com/SakanaAI/AI-Scientist) and [reported failure examples](https://sakana.ai/ai-scientist/) | Autonomous hypothesis-to-experiment workflow; reported cases where an agent changed execution/time controls or compared baselines unfairly | Keep immutable evaluators and external-action authority separate from the candidate agent; preserve failures and cost overruns, never count paper generation as scientific validation | NEGATIVE DESIGN WARNING |
| [Xiangyue Zhang — Deep Researcher Agent](https://github.com/Xiangyue-Zhang/auto-deep-researcher-24x7) | Bounded research memory, long-running experiments and explicit failed/cancelled/timeout states | Distinguish a scheduled run, a successful tool call and a completed scientific test; cap context cost; persist failure status as first-class evidence | CONCEPTUAL COMPARISON ONLY |

**One minimally discriminating next check, not a new platform:** select one existing claim (E009's preregistered negative result is preferable), freeze its documented commit and scoring rule, ask an unfamiliar reviewer or separately constrained executor to find and re-run the result from public links only, and record the actual outcome as `REPRODUCED_BY_PROJECT_LINEAGE`, `INDEPENDENT_IMPLEMENTATION`, `FAILED` or `UNKNOWN` according to demonstrated independence. This action is **not yet executed** by this comparison.

**Failure criteria:** undocumented manual context restoration, inability to locate exact input/code/commit, changed evaluator, selective result omission, unclear external rights, or a false independent-replication label. Do not auto-promote a new agent framework based on repo popularity, self-reported success rates or a green CI badge. Keep all external source credit and rights boundaries intact; no third-party source files or datasets are copied here.

### Original 2 — 한국어

**증거 등급:** 타인의 공개 GitHub 저장소에서 확인한 설계·기능에 대한 비교다. **이 조사로 실제 설치, 독립 재현, 현실적 효과 또는 인과적 성능 향상이 검증된 것은 아니다.** 모든 설계의 원기여자를 구분하며, Project Intersection이 최초 발명했거나 타인의 코드를 도입·검증했다고 주장하지 않는다.

| 선행 프로젝트·원기여자 | 구별되는 기능 | Project Intersection 기존 구조에서 수행할 판별 검사 | 상태 |
| --- | --- | --- | --- |
| [Andrej Karpathy — autoresearch](https://github.com/karpathy/autoresearch) | AI가 실험 코드를 바꾸되 데이터 준비·평가 코드 및 5분 연산 예산은 고정 | E008 결과를 내기 전에 채점기·기준선·사례·예산을 후보 수정 주체와 별도로 고정하고 E009의 단순 기준선과 비교 | 제안; E008 본 실험 보류 |
| [Technion Kishony Lab — data-to-paper](https://github.com/Technion-Kishony-lab/data-to-paper) | 발표 수치에서 실행 코드·입력자료로 역추적 | 기존 E007/E009 수치 하나를 선택해 주장→결과→실행 명령→코드·입력→커밋을 새로운 검토자가 복원하고 단절 기록 | 제안; 독립 재현 아님 |
| [Agents4Academia — Prior](https://github.com/Agents4Academia-AI/prior) | 출처별 기여·주장·모순과 불확실성을 표현하는 그래프 | 기존 지식그래프와 CCPH에 검증된 관계만 연결하고 인용·영향·독립 발견·실제 후속 효과를 분리 | 개념 비교만 |
| [OpenResearch 기여자 — OpenResearch](https://github.com/openResearch1/openresearch/blob/master/README.en.md) | 맥락 손실 후에도 남는 주장+증거 단위의 연구 상태 | 기존 상태 파일과 그래프로 낯선 실행자의 재개 질문 한 개를 시험; 미지원·오래된 연결을 기록하고 그래프 중복 제작은 피함 | 개념 비교만 |
| [영국 AI 평가 생태계·Generality Labs — Inspect Evals](https://github.com/UKGovernmentBEIS/inspect_evals) | 공개 평가 등록부·실행 가능한 검사·외부 오류 신고 경로 | 미래의 독립 검증 표시 전에 실행 영수증과 분리된 외부 검토 경로 확인 | 기존 개념 존재; 외부 검토 미확인 |
| [위트레흐트대학교 — ASReview](https://github.com/asreview/asreview) | 사람이 판정한 문헌을 보존하며 능동학습으로 선별 우선순위를 조정 | 고정된 선행연구 질문 하나에 포함·제외·누락 점검을 시범 적용; AI 요약만으로 포화 선언 금지 | 미실행 |
| [Sakana AI — AI Scientist](https://github.com/SakanaAI/AI-Scientist) 및 [공개 실패 사례](https://sakana.ai/ai-scientist/) | 자율 실험·논문 생성과 실행시간 제약 수정·불공정 기준선 비교 실패 사례 | 후보 에이전트가 평가기·실행권한을 바꾸지 못하도록 분리하고 실패·예산 초과 보존; 논문 생성은 검증 성과로 계산하지 않음 | 부정적 설계 교훈 |
| [Xiangyue Zhang — Deep Researcher Agent](https://github.com/Xiangyue-Zhang/auto-deep-researcher-24x7) | 제한된 기억·장기 실험·실패/취소/시간초과 상태 관리 | 예약 실행, 도구 호출 성공, 과학적 결과 확인을 구별하고 실행 실패를 증거 상태로 보존 | 개념 비교만 |

**최소 판별 검사 한 개:** 기존 E009 사전등록 부정적 결과의 커밋과 채점 규칙을 먼저 고정한 뒤, 해당 연구와 무관한 검토자 또는 별도 제약된 실행자가 공개 링크만으로 찾아 재실행하게 한다. 실제 독립성·성공 여부에 따라 `REPRODUCED_BY_PROJECT_LINEAGE`, `INDEPENDENT_IMPLEMENTATION`, `FAILED`, `UNKNOWN`을 구별한다. 이 비교 작업 자체가 그 검사를 **실행한 것은 아니다**.

**실패 기준:** 기존 대화 내용을 수동 복원해야 함, 정확한 입력·코드·커밋 누락, 평가기 변경, 부정적 결과 선택적 누락, 외부 저작권·권리 불명확, 독립 복제의 허위 표시. 저장소 인기·자체 성과 보고·CI 통과만으로 새 에이전트 플랫폼을 승격하지 않는다. 이 기록은 외부 코드·데이터셋을 복사하지 않는다.
