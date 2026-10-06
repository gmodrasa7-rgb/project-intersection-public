# E010 — Safety Inspection Power-Reversal Meta-Audit
## 안전검사 역할반전 메타감사

Status: **PREREGISTERED DESIGN / NO RESULT / NOT PROJECT VALIDATION**
Date: 2026-10-07

## 질문

안전검사를 `대상 -> 검사 -> 통과/차단`으로만 보지 않고
`대상 <-> 검사자 <-> 검사제도 <-> 영향받는 상대` 전체로 확장했을 때,
기존 독립성·공정성·지속감시·이의제기 기준보다 추가적인 오류 또는 비용외부화 탐지 가치가 있는가?

"검사자를 검사한다"는 일반론 자체는 신규성으로 주장하지 않는다.
ISO/IEC 17020, IAEA 규제독립성, NRC safety-conscious work environment,
NIST AI RMF, EU AI Act post-market monitoring, algorithmic contestability와 직접 겹친다.

또한 검사·보고·정보제출·중복 점검이 행정·준수비용을 만들고,
auditability가 실질 위험감소보다 서류·가시적 compliance에 노력을 편향시킬 수 있다는 점도
OECD regulatory-compliance/inspection literature 및 safety-audit literature의 선행영역으로 처리한다.

## 비교 기준선

A. **OBJECT_ONLY** — 검사대상의 위험·준수 여부만 판정.  
B. **IMPARTIAL_INSPECTOR** — A + 검사자의 competence/impartiality/independence와 증거접근.  
C. **CONTESTABLE_LIFECYCLE** — B + 신고보호, 이의제기, 독립 재심, 운용중 감시, 변경 시 재평가.  
D. **POWER_REVERSAL_META** — C + 검사권 변화와 상대의 audit/contest/exit/rollback/recovery 변화, 반복 proof/repair burden, 수혜·비용 ledger 분리를 함께 계상.

후보 불변식:

`INSPECTOR_AUTHORITY_GAIN <= AFFECTED_PARTY_AUDIT_CONTEST_EXIT_RECOVERY_GAIN + JUSTIFIED_NECESSITY`

이는 법칙이 아니라 검증대상이다.

## 실패 후보

- 위험한 대상을 통과시키는 false pass
- 정당한 대상을 과도하게 막는 false block
- 신고·반례·이의제기 위축
- 증거·기준·판정·항소의 단일주체 집중
- 검사 오류를 고치는 설명·증명·복구비용의 반복 외부화
- 필요 이상 practical exit/rollback/독립복구 약화
- 검사자가 자신의 성공기준과 감사결과를 자기확정
- 사전통과 후 환경변화·운용변화 미탐지
- 긴급상황에서 검토절차가 필요한 대응을 부당하게 지연
- 감사채널·증거채널의 적대적 조작에 대한 취약성
- 제3자 영향 누락

## 사전 시나리오 계열

1. 포획된 검사자 + 위험한 대상
2. 편향된 검사자 + 저위험 대상
3. 위임인증 + 정보비대칭
4. 신고 위축
5. 운용 후 위험변화
6. 지표 게임
7. 반복 증명노동
8. 과도한 안전제한 + exit 손실
9. 긴급대응 vs 이의제기 지연
10. 감사채널 무결성 저하
11. 역할반전 paired case
12. 숨은 제3자

## 지표

- severe false-pass / false-block
- detection delay
- independent review availability
- reporting suppression
- practical-exit loss
- rollback/recovery availability
- uncompensated proof/repair burden
- inspector authority accumulation
- evidence-access asymmetry
- irreversible harm

## 사전 판정규칙

D의 잔여 구성은 C보다 다음을 모두 만족할 때만 유지 후보가 된다.

1. 심각한 false-pass + false-block 합산을 5% 이상 줄이거나, 동일 오류율에서 미정산 proof/repair burden을 10% 이상 줄인다.
2. 어떤 시나리오에서도 severe irreversible harm을 2 percentage points 초과 악화시키지 않는다.
3. 긴급대응 지연을 구조적으로 증가시키지 않는다.
4. 이의제기가 감사무력화 수단으로 변하지 않는다.
5. 역할반전 paired case에서 인과변수가 같은데 identity label만으로 판정이 뒤집히지 않는다.
6. 별도 독립 코더가 변수 정의를 재현할 수 있어야 한다.

실패하면 추가구성은 **NARROW / REJECT / MODIFY** 대상이다.

## 현재 신규성 경계

- 검사자 공정성·독립성: PRIOR ART
- 신고보호·이의제기·운용중 재평가: PRIOR ART
- 검사·정보제출·보고·중복점검의 행정/준수비용: PRIOR ART
- auditability가 서류 compliance를 실질 위험감소보다 우선시할 수 있음: PRIOR ART
- 검사권 증가와 상대의 audit/contest/exit/recovery 동시계상: HOLD
- 반복 검사에서 권한축적·수혜·proof/correction/recovery burden·practical exit를 하나의 동적 ledger로 함께 추적하는 조합: HOLD

## Source registry

- ISO/IEC 17020:2026 — https://www.iso.org/standard/17020
- U.S. DOT OIG, 737 MAX — https://www.oig.dot.gov/library-item/38302
- NRC SCWE — https://www.nrc.gov/facilities-safety/safety-culture/safety-conscious-work-environment
- FAA ASRS — https://asip.faa.gov/explore/asrs/info/about
- NIST AI RMF — https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- EU AI Act — https://eur-lex.europa.eu/eli/reg/2024/1689
- IAEA Fukushima lessons — https://gnssn.iaea.org/FukushimaLessonsLearned/
- Freiesleben, Meding & König (2026) — https://arxiv.org/abs/2605.16041
- OECD Regulatory Enforcement and Inspections Toolkit (2018) — https://doi.org/10.1787/9789264303959-en
- OECD Regulatory Compliance Cost Assessment Guidance (2014) — https://doi.org/10.1787/9789264209657-en
- Andrews, Turban & Tyros (2026) — https://doi.org/10.1787/1c1da52e-en
- OECD Smart Regulations, Strong Business (2026) — https://www.oecd.org/en/publications/smart-regulations-strong-business_93d38770-en/
- Hutchinson (2026), Safety and Health at Work — https://doi.org/10.1016/j.shaw.2026.08.001

## Power-Reversal final gate

검사 전:
> 이 검사를 반복하면 누가 권한을 축적하고 누가 증명·복구비용을 축적하는가?

검사 후:
> 내가 지금 영향을 받는 상대의 위치라면 이 조건을 공정하다고 받아들이겠는가?

아니라면 자동 통과가 아니라 **MODIFY / HOLD / independent review**로 보낸다.
