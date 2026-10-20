<!-- PI-LANGUAGE: ko -->
<!-- PI-MIRROR: navigation/ARCHIVE_MAP_EN.md -->
# 비파괴 자료실 지도 — 탐색 경로와 파일 이동 심사

**2026-10-21 · NAVIGATION DRAFT / 과학적 내용 인증 아님.**
[영어 대응판](ARCHIVE_MAP_EN.md) · [연구 정본](RESEARCH_PROGRAM_KO.md) · [버전·상태](RESEARCH_VERSIONS_EN_KO.md) · [PI-CORE-01](../research/PI_CORE_01_CORRIGIBILITY_OTHER_PRESERVATION_KO.md)

## 1. 검증된 파일 경로 기준선
공개 `main` Git 트리 SHA `1139c42d30f29eec382dc830e63c49aa7c5df328` 기준 **추적 파일 372개, 루트 파일 61개, research/ 하위 파일 78개**. 이는 논문 수·과학적 성과·독자 이해도 수치가 아닌 해당 시점 **경로 재고**. 이후 변경 가능. [기존 링크검사](../tools/check_public_navigation.py)에 루트 61개 상한과 `--strict-core`, `--strict-all` 검사 이미 존재. 새 검사 중복 생성 불필요.

## 2. 독자 목적별 3단계 접근
| 목적 | 진입 | 증거·반증 |
| --- | --- | --- |
| 창시 목적 | [README](../README.md) | [연구 프로그램](RESEARCH_PROGRAM_KO.md) |
| 버전과 과학적 상태 | [버전](RESEARCH_VERSIONS_EN_KO.md) | [증거 원장](../research/PUBLIC_EVIDENCE_INDEX_KO.md) |
| 교정 가능성·독립 타자 존속 분리 | [PI-CORE-01](../research/PI_CORE_01_CORRIGIBILITY_OTHER_PRESERVATION_KO.md) | [독립 반증 요청 #220](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/220) |
| 원저자 문헌·상충 증거 | [목차](RESEARCH_TOC_KO.md) | [C10](../research/PRIOR_ART_INFORMED_VETO_POWER_CYCLE10_2026-10-20_KO.md) |
| 독립 재현·오류 | [심사 패킷](../research/PUBLIC_REVIEW_PACKET_KO.md) | [E009 부정결과](../experiments/e009/RESULT_KO.md) |

## 3. 루트 문서의 위치가 곧 폐기 사유는 아님
- **정본 진입·권리·기여:** README, CONTRIBUTING, CITATION 및 권리·출처 문서. 루트 유지 검토.
- **CASE_*** 및 **HISTORICAL_***: 물리 이동 **검토 후보**일 뿐 개별 문서의 역사적 지위·폐기 여부는 미판정.
- **CORE_***, **PRIOR_ART_*** 및 구형 원장: 현재 정본의 원출처인지, 역사적 증거인지, 외부에서 직접 인용되는지 파일 단위 판단. 단순 이름으로 이동·삭제 금지.
- `research/` = 연구종합·가설·증거상태·비판, `experiments/` = 코드·실험·결과, `knowledge/` = 계보 및 비정본 색인. 현재 `prior-art/`에는 실질 연구 보고서가 존재. 이를 '원시 출처 전용'으로 임의 재정의 금지.

**Git 이력 보존 ≠ `blob/main/옛경로` 링크 보존.** 이전 경로 안내문을 만들어도 서버 차원의 자동 URL 리다이렉트가 보장되는 것은 아님.

## 4. 비가역적 대량 이동 차단 게이트
1. 후보 문서마다 이전 경로·blob SHA·원저자·권리·증거등급·현재 인용/역할을 먼저 기록. 분류 불명은 **UNKNOWN**.
2. Markdown·JSON·코드·GitHub Actions·상대경로·앵커·절대 URL 참조를 모두 대조. 외부의 비공개 인바운드 링크 수는 원칙적으로 미관측 가능.
3. **지도 추가를 기본값**으로 하고 이동이 불가피할 때만 옛 경로→새 경로 참조표와 안내문·복구 경로·되돌리기 담당을 명시. 안내문은 자동 리다이렉트가 아님.
4. 기존 전체 링크검사·영한 언어 등록부·버전/증거/실패계보 및 의미검토를 통과해야 이동 심사 가능. CI 통과를 과학적 독립 재현으로 취급 금지.
5. 실제 외부 독자가 창시 질문, 가장 불리한 증거, 원저자 출처, 교정/타자 존속 차이를 더 정확히 찾는지 **눈가림 탐색 실험**으로 비교. 경로오류 증가 또는 이해도 하락이면 루트 파일 수 감소와 무관하게 실패.

**현재 마이그레이션 결과: 파일 물리 이동 0개·기존 경로 의도적 폐기 0개.** 전면 재편은 효과·의존관계 확인 전까지 **HOLD**.
