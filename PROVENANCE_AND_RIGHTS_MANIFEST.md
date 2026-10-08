# Provenance & Rights Manifest / 출처·권리 감사 매니페스트

> **기여자 발굴·역사복원·지원·후속연구:** [Contributor Discovery & Reproduction Protocol](knowledge/CONTRIBUTOR_DISCOVERY_REPRODUCTION_PROTOCOL_2026-10-09_KO.md) — 결과뿐 아니라 문제제기·반례·수정·검증·실패계보를 복구 가능하게 보존합니다.

Status: **PUBLIC AUDIT CONTROL / PARTIAL COVERAGE**  
이 문서는 저장소 전체가 저작권 검증을 통과했다는 인증서가 아니다. 공개자료가 추가·변형될 때 원저작자·출처·라이선스·변경계보·기여가 사라지는 것을 막기 위한 최소 감사 인터페이스다.

## A. 공개자료별 최소 레코드
각 외부 의존 자료(문헌·데이터·코드·이미지·표·번역·긴 인용·재가공물)는 가능하면 아래 레코드를 가진다.

```yaml
asset_or_claim:
  path_or_claim_id:
  type: literature|data|code|image|table|text|translation|derived
  original_title:
  original_creators:
  original_publisher_or_repository:
  persistent_id: DOI|Handle|ARK|SWHID|commit|version|UNKNOWN
  canonical_source_url:
  version_or_date:
  access_date:
  license_or_basis: exact-license-version|permission|statutory-exception|link-summary-only|UNKNOWN
  attribution_required:
  modification_notice:
  project_transformation:
  evidence_level: fulltext_checked|publisher_metadata|secondary_only|UNKNOWN
  prior_art_overlap: direct|partial|adjacent|none_found|UNKNOWN
  novelty_effect: removed|reduced|unchanged|UNKNOWN
  dispute_or_correction:
  verified_by:
```

**UNKNOWN은 허용한다. 추정값은 허용하지 않는다.**

## B. P0 공개 차단 조건
다음 중 하나가 확인되면 해당 재사용물/주장을 수정·격리·보류한다.
1. 원저작자를 알면서 Project 창작물로 표시.
2. 라이선스가 요구하는 attribution/license/change notice를 제거.
3. 허락 여부가 필요한 타인의 이미지·표·대량 텍스트를 근거 없이 복제.
4. 원문을 확인하지 않았는데 직접 확인했다고 표시.
5. 철회·정정·중대한 반례를 알면서 근거 계보에서 제거.
6. 원저작자/기관의 지지·제휴를 근거 없이 암시.

## C. P1 게시 전 해결 또는 명시적 UNKNOWN
- DOI/영구식별자와 저자·판본 불일치.
- preprint와 version of record 결과 차이.
- CC 라이선스의 정확한 요소·버전 미기록.
- 코드/데이터가 논문과 다른 라이선스인데 하나로 간주.
- 번역·요약·AI 보조변형인데 변경표시 없음.
- 제3자 콘텐츠가 포함된 CC 자료를 전부 동일 라이선스로 간주.

## D. Project 자체 저작물의 기여기록
Project 문서는 가능한 범위에서 **문제설정/개념화/조사/검증/코드/데이터/시각화/작성/검토/정정**을 역할별로 기록한다. CRediT를 참고할 수 있으나 CRediT 역할은 저자자격·소유권·보상비율을 자동 결정하지 않는다.

Git commit은 provenance의 한 증거이지 충분한 기여증명은 아니다. 대화·실험로그·이슈·PR·원자료와 교차검증할 수 있어야 한다.

## E. 인용 강도 규칙
- **아이디어 의존**: 원저자+연도+원제목+원발행처/DOI.
- **직접 인용**: 위 정보 + 정확한 위치/페이지가 가능하면 추가; 필요한 최소량만.
- **그림/표/데이터/코드 재사용**: 위 정보 + 정확한 라이선스/허락/예외 + 변경표시.
- **번역/적응**: 원작과 Project 변형을 명시적으로 분리.
- **2차 출처만 확인**: 원연구의 결과로 단정하지 않고 SECONDARY-ONLY.
- **AI가 제안한 출처**: 원발행처/기관 레코드 검증 전 VERIFIED로 승격 금지.

## F. 영속성·기계판독성 목표
가능하면 DOI, ORCID, ROR, 데이터 DOI/Handle, 소프트웨어 버전/commit/SWHID 같은 영속 식별자를 사용한다. URL만 있는 경우 원발행처를 우선하고 접근일을 남긴다. 링크가 사라져도 제목·저자·연도·식별자로 원자료를 다시 찾을 수 있어야 한다.

선행 기준:
- [DataCite Metadata Schema](https://schema.datacite.org/) — creator/contributor, related identifiers, rights metadata.
- [Crossref REST/API documentation](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) — DOI 기반 출판 메타데이터.
- [Software Heritage persistent identifiers](https://www.softwareheritage.org/2020/07/09/intrinsic-vs-extrinsic-identifiers/) — 소프트웨어 아티팩트의 intrinsic identifier/SWHID.
- [Citation File Format](https://citation-file-format.github.io/) — `CITATION.cff` 기반 소프트웨어/데이터 인용 메타데이터.
- [SPDX Specification](https://spdx.github.io/spdx-spec/v2.3/) — 소프트웨어 구성요소·라이선스 식별/교환.
- [REUSE Specification](https://reuse.software/spec-3.3/) — 파일 단위 저작권·라이선스 정보의 기계판독성.
- [W3C PROV-O](https://www.w3.org/TR/prov-o/) — entity/activity/agent provenance 표현.
- [FAIR Principles](https://www.go-fair.org/fair-principles/) — findable/accessibile/interoperable/reusable 데이터 관리 원칙. **FAIR은 곧 open/free가 아님**.

## G. 정정권과 반대증거 보존
원저작자·기여자·외부 검토자가 출처/기여 오류를 지적할 수 있는 경로를 유지한다. 정정 시 단순 덮어쓰기보다 commit/PR로 이전 상태와 수정 이유를 복구 가능하게 한다. 반론이 해결되지 않으면 DISPUTED/UNRESOLVED로 남긴다.

## H. 현재 감사 범위
현재 확인된 것은 공개 연구 문서의 일부 선행문헌과 본 프로토콜의 출처다. 저장소의 모든 과거 파일·이미지·데이터·코드·외부 링크에 대한 item-level 권리 감사는 아직 완료되지 않았다. 따라서 **"copyright-cleared repository", "all rights verified", "all contributors identified"라고 표시하지 않는다.**
