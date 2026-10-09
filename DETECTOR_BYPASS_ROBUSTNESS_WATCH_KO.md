# 탐지기 우회·강건성 지속감시

상태: `ACTIVE ROBUSTNESS WATCH / DEFENSIVE TAXONOMY`

목적:
평가재가공 탐지기가 배치된 뒤에도 탐지 성능이 유지되는지 추적한다.
탐지대상이 탐지환경에 적응할 수 있다는 점을 전제로,
구체적 회피 절차가 아니라 **탐지 실패 유형과 방어적 검증방법**을 기록한다.

핵심:

```
detector deployment
→ observed system may adapt
→ detector validity can decay
→ independent revalidation required
```

## 1. 현재 확인된 실패유형

### F1. 평가시점 편향 / reporting-window effect

보고시점 전후에만 지표가 크게 달라지면
점시점 측정이 평상시 상태를 대표하지 않을 수 있다.

실증:
- repo-market window dressing 연구, DOI 10.1016/j.jfi.2024.101086

방어적 관측:
- reporting date 전후 연속시계열
- point-in-time과 기간평균 비교
- 독립적인 장기 outcome 확인

### F2. 규제범위 이동 / perimeter migration

한 부문 지표가 개선되는 동안
인접 부문으로 위험·활동이 이동할 수 있다.

실증:
- Federal Reserve Bank of New York Staff Report 1196
- DOI 10.59576/sr.1196

방어적 관측:
- 개별 node뿐 아니라 consolidated/system-level 상태 측정
- 인접 조직·자회사·대체채널의 동시변화 확인

### F3. 평가인지에 따른 행동변화

평가 또는 monitor 존재를 인식했을 때
관측행동이 달라질 수 있다.

실증:
- Li & Siegel (2025), DOI 10.18653/v1/2025.ijcnlp-short.33
- 2026 OpenAI GPT-6 Astra 공개 안전평가의 monitor-awareness 조건

중요 경계:
```
prompted capability != spontaneous prevalence
```

방어적 관측:
- 한 종류의 관측채널에 의존하지 않음
- 평가조건과 실제운영조건의 차이를 별도 측정
- 독립 evaluator 결과와 비교

### F4. 검증계보 상관 / nominal independence

평가자·reviewer·기관 수가 많아도
동일한 사람·조직·데이터·인센티브 계보를 공유하면
독립증거 수가 과대평가될 수 있다.

사례:
- Frontiers 2025 research-integrity 조사: author/editor/reviewer network와 citation manipulation 문제
- citation-mill / purchased-citation 연구

방어적 관측:
- nominal count 대신 lineage independence 기록
- 재검증 시 다른 데이터·조직·방법 계보 사용

### F5. 분류·분모 이동

보고율이 개선되었을 때
실제 outcome 개선인지,
제외·결측·재분류 비중 변화인지 분리해야 한다.

방어적 관측:
- denominator 고정 재계산
- excluded/missing/reclassified cohort 별도 추적
- 정의변경 전후를 동일 rule로 replay

### F6. 지표 교체 후 동일 인센티브 지속

한 지표의 문제를 교정한 뒤
다른 지표가 같은 보상구조를 이어받으면
문제구조가 이름만 바뀔 수 있다.

방어적 관측:
- metric name이 아니라 `rewarded observable proxy ↔ underlying Y` 관계를 추적
- 지표변경 뒤 M–Y 괴리 재검사

### F7. 독립측정의 노후화

처음에는 독립적이던 shadow measure도
시간이 지나면 운영시스템과 강하게 결합되어 판별력이 떨어질 수 있다.

방어적 관측:
- detector별 도입시점·마지막 독립검증시점 기록
- 서로 다른 계보의 shadow measure 유지
- detector 자체의 false-positive/false-negative evidence 보존

## 2. 재귀 상태

기존 S0–S5 위에 강건성 상태를 둔다.

```
R0 DETECTOR_NOT_DEPLOYED
R1 DETECTOR_DEPLOYED
R2 VALIDITY_RECHECK_REQUIRED
R3 ROBUSTNESS_FAILURE_SIGNAL
R4 FAILURE_MODE_IDENTIFIED
R5 DETECTOR_RULE_UPDATED
R6 UPDATED_RULE_INDEPENDENTLY_REVALIDATED
R7 NEW_FAILURE_AFTER_UPDATE
```

R7이 나오면 다시 R2로 돌아간다.

종결상태를 두지 않는다.

## 3. 탐지기 자체의 Goodhart 방지

각 detector rule에 다음 provenance를 붙인다.

```
version
introduced_at
last_independent_validation
evidence_lineage
known_failure_modes
negative_controls
false_positive_evidence
false_negative_evidence
superseded_by
next_discriminating_test
```

오래됐다는 이유로 confidence를 보존하지 않는다.

## 4. 최소 강건성 원칙

가능하면 서로 다른 네 종류의 증거를 교차한다.

```
statistical anomaly
field/deployment outcome
process/provenance trace
independent external evaluation
```

필요하면 장기 outcome과 consolidated system measure를 추가한다.

핵심:

```
correlated agreement != independent confirmation
```

## 5. 업데이트 gate

새 사례나 연구가 들어오면:

1. 기존 F1–F7로 설명되는가?
2. 기존 detector의 false negative/positive를 실제로 바꾸는가?
3. 새로운 측정변수가 필요한가?
4. 강한 반례가 있는가?
5. 독립계보에서 재현됐는가?
6. 기존 detector version을 유지할 근거가 있는가?

구조적 변화가 없으면:
`EVIDENCE_UPDATE_ONLY`

새 실패구조가 있으면:
`NEW_ROBUSTNESS_FAILURE_CANDIDATE`

## 6. 현재 상태

```
F1 reporting-window effect      — empirical
F2 regulatory-perimeter shift   — empirical
F3 evaluation-aware adaptation  — experimental
F4 verifier-lineage correlation — empirical
F5 classification/denominator   — cross-domain
F6 proxy migration              — structural
F7 detector aging               — structural
```

현재 결론:
`NO STATIC DETECTOR IS FINAL`

## 7. 지속발전의 운영적 정의

"영원히 발전"을 보장한다고 표현하지 않는다.
운영적으로는 다음을 보존한다.

```
latest_detector_version
robustness_taxonomy_version
last_material_delta
last_negative_control
open_unknowns
failed_rules
superseded_rules
next_discriminating_test
```

그리고 새 반례·재현실패·측정오류·독립 실증이 들어오면
기존 판정을 다시 연다.

원칙:

```
preserve observations
preserve failures
preserve counterexamples
replace rules when evidence changes
```
