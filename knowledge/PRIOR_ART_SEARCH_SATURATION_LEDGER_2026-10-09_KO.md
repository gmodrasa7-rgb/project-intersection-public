# PRIOR-ART 검색포화 원장

**목적:** ZERO GATE의 검색포화 판정을 말이 아니라 재검사 가능한 증거로 남긴다.  
**현재:** OPEN / SATURATION COUNT = 0 / 3

## 상태 정의
- `OPEN`: 신규 DIRECT/PARTIAL 원출처가 계속 발견되거나 필수 검색경로 미완료.
- `CANDIDATE-1/2`: 유효한 독립 검색파동에서 신규 DIRECT/PARTIAL 원출처 0건이 각각 1/2회 연속.
- `SATURATION-CANDIDATE`: 서로 다른 유효 파동 3회 연속 0건.
- `REOPENED`: 포화 후보 뒤 새로운 DIRECT/PARTIAL 원출처 발견.
- `INVALID-WAVE`: 검색/API 실패, 동일 검색 반복, 범위 임의축소, 출처검증 불가.

## 파동 원장
| Wave | 날짜 | 독립 경로 | 신규 DIRECT/PARTIAL | 반례/정정 | 상태 |
|---|---|---|---:|---:|---|
| W0 | 2026-10-09 | 기존 prior-art/정량 원문 감사 | 다수 | 다수 | OPEN |
| W1 | 2026-10-09 | governance×credit×exit 역방향 탐색 | 다수 | 있음 | RESET→0 |
| W2 | 2026-10-09 | 저자권 분쟁·acknowledgement·exit/voice 서지복구 | 다수 | 있음 | RESET→0 |

현재 연속 0건: **0**.

## 유효 파동 필수필드
각 파동은 다음을 남긴다.
1. 날짜/검색경로/DB 또는 인용계보
2. 검색식과 핵심 동의어
3. 포함·제외 기준
4. 접근 실패/검색 실패
5. 새 DIRECT/PARTIAL/ADJACENT/BACKGROUND 수
6. 새 반례/null/정정/철회
7. 원저자·원제목·연도·DOI/영구식별자
8. Project claim에 미친 novelty effect
9. verifier와 novelty auditor가 동일인인지 여부
10. 다음 파동에서 의도적으로 달라질 검색축

## 자동 리셋
다음 중 하나면 연속 0건 카운터를 0으로:
- 새 DIRECT/PARTIAL prior art
- 더 이른 독립발견
- 기존 핵심 출처의 정정/철회가 claim을 변경
- 기존 분류가 BACKGROUND→PARTIAL/DIRECT로 상향
- 포함기준이 잘못되어 재검색 필요

## 포화 후보도 종료가 아님
SATURATION-CANDIDATE는 '문헌이 없다'가 아니다. 이후 새 원출처가 나오면 즉시 REOPENED. Project residual은 항상 선행성 재검토 가능.

## 현재 다음 파동
W3: **authorship dispute → career/funding/collaboration/exit outcomes** 직접 인과/종단연구.
W4: **non-author technical/data/software contributors → career recognition/retention**.
W5: **비영어권·학위논문·기술보고서·조직연구에서 provenance/correction/exit 결합**.


> [선택 인과축 분리 프로토콜](CHOICE_CAUSAL_AXES_PROTOCOL_2026-10-09_KO.md): 자율성·강제성·유도/영향·편향·조종을 독립축으로 판정하며 선택결과에서 원인을 역추론하지 않는다. PRIOR-ART GATE OPEN.


| W-CHOICE-1 | 2026-10-09 | 선택 인과축: 학술 색인/출판사/학위논문/철학/실험심리 | 17건 이상 확인(기존 레지스트리와 중복 대조 미완료) | 조종·자율성 판단의 반례 포함 | RESET→0 |

**주의:** W-CHOICE-1의 17건은 이 파동에서 확인한 직접/부분 관련 문헌 수이지 Project 전체에 대해 17건이 모두 처음 발견되었다는 뜻이 아니다. 기존 파일과 중복대조가 끝날 때까지 '신규 순증'은 UNKNOWN. 최소 한 건 이상 새 직접 실증 문헌을 확인했으므로 포화 카운트는 0/3이다.


| W-CHOICE-2 | 2026-10-09 | 원전: 동의/조종 역사, 적응적 선호, 심리적 반발, 설득 기술·다크패턴 | 다수(신규 직접/부분 원전 존재, 전체 중복제거 미완료) | Mathur 2019 분류 정정 확인 | RESET→0 |

W-CHOICE-2 원장: [원저작자·역사·출처·기여](CHOICE_CAUSAL_AXES_PRIOR_ART_WAVE_2_2026-10-09_KO.md). 기존 W-CHOICE-1과 별개 검색축. 검색포화 0/3.

| W-CHOICE-3 | 2026-10-09 | 강제의 기준선·choice blindness·실험 다크패턴 | 새 DIRECT/PARTIAL 원전 있음 | 강한 패턴의 반발; 자기보고 불일치 | RESET→0 |

[W3 원저자·원출처·기여](CHOICE_CAUSAL_AXES_PRIOR_ART_WAVE_3_2026-10-09_KO.md).
| W-CHOICE-4 | 2026-10-09 | 선택맹 정치/도덕 실험·선호형성 방법론·후속 인용 | 신규 DIRECT/PARTIAL 있음 | 스웨덴 2013 vs 아르헨티나 2017 정치 결과 차이 | RESET→0 |

[W4 원저자·원전·반례](CHOICE_CAUSAL_AXES_PRIOR_ART_WAVE_4_2026-10-09_KO.md).
