# Project Intersection 모바일 연구 앱 — 한국어 (v0.2.1)

[English edition](README_EN.md) · [공개 연구 저장소](https://github.com/gmodrasa7-rgb/project-intersection-public)

## 목적
일반인이 스마트폰으로 연구 목적을 이해하고, 불리한 증거를 먼저 확인하며, 공개 GitHub Issue로 질문·선행 원저자 문헌·반례·재현 실패를 제보하도록 만드는 **설치형 웹앱(PWA)** 초안.

## 기능
- 다섯 연구축(VC·MER·EI·ECR·IVS-0R)의 한국어·영어 입문 설명.
- 연구 원문·버전·부정결과·미실행 실험으로 연결되는 출처 중심 독서 경로.
- GitHub Issue를 작성하기 전에 제목·설명·출처를 정리하는 로컬 양식. **제출은 GitHub에서 사용자가 직접 승인**하며 GitHub 로그인이 필요함.
- 지원 브라우저에서 홈 화면 설치, 앱 화면 자체의 제한적 오프라인 열람.
- 제3자 트래커·API 토큰·서버 측 개인정보 수집 없음.

## 검증과 한계
- 화면 설명은 2026-10-21의 공개 자료 기반 요약이며 최신 연구·새 커밋 자동 반영 또는 완전한 자료 검색을 보장하지 않음. 링크는 항상 공개 저장소 main 원문을 가리킴.
- E009 부정결과와 E008 본 결과 부재를 최상위 경계로 공개. 자체 합성시험은 현장 인과증명이 아님.
- 오프라인에서는 앱 설명만 확인 가능; 외부 GitHub 문서와 Issue 제출은 네트워크 필요.
- 로그인 없는 직접 제출, 푸시 알림, 고급 검색, 상호 검토·평가 절차는 미구현.
- 원문 저작권은 각 자료의 별도 이용허락 범위에 따름. 앱은 원문을 전체 복제하지 않고 공개 URL로 연결.
- 본 웹앱에는 비공개 P CHRONICLE 및 개인·가족·재무 자료를 연결·노출하지 않음.

## 배포
GitHub Pages를 GitHub Actions 소스로 활성화한 다음, `.github/workflows/pi-mobile-pages.yml`이 main 변경 시 `mobile/`만 게시. 예상 주소: `https://gmodrasa7-rgb.github.io/project-intersection-public/` (실제 페이지 활성·배포 확인 전에는 사용 중이라고 단정 금지).

## 최소 점검
`node --check mobile/app.js` · `node --check mobile/service-worker.js` · `node mobile/check.mjs`.
인간 접근성 검사(스크린리더·모바일 브라우저), PWA 설치 시험, GitHub 로그인 후 제보 흐름 확인은 별도로 필요.

## v0.2 선행 모범사례 응용 (2026-10-21)
- **Zooniverse:** 짧은 검토 과제·선택·튜토리얼. 단, 자원봉사자 다수결은 연구 참값이 아님. https://help.zooniverse.org/getting-started/
- **Mozilla Common Voice:** 수집과 검증을 분리하는 업무 흐름. 현재는 다중독립검증 자동화 미구현. https://www.mozillafoundation.org/en/common-voice/platform-and-dataset/
- **NotebookLM:** 출처 연결·원문 확인 원칙. 실제 LLM 모델은 앱에 설치·호출하지 않음. https://blog.google/innovation-and-ai/technology/ai/notebooklm-google-ai/
- **Consensus:** 지지·반대·미확인을 구분하는 근거 분류. 프로젝트 결과에 가짜 신뢰 점수 부여 금지. https://help.consensus.app/en/articles/17234045-consensus-ai-analysis-citations-and-visuals
- **GitHub Issues:** 공개 전 편집 가능한 제보 초안·최종 직접 제출. https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue
- **W3C WCAG 2.2:** 모바일 터치·입력 접근성 고려, 실기기 인증 아님. https://www.w3.org/TR/WCAG22/

### 추가 기능과 경계
1. 검증 실습은 E007·E008·E009 공개 자료와 고정 커밋 `7913d78024ce98de3a4c3409e92e6d59adcf455a` 참조. 최신 원문 별도 링크. 요약은 역사적 스냅샷이며 새로운 과학적 성과 아님.
2. 사용자의 잠정 판단·메모는 서버로 자동 전송하지 않음. '모름' 선택과 원문 열람 허용. 화면의 일치표시는 연구 타당성 점수 아님.
3. 'AI 독립검증 요청문 복사'는 클립보드 출력뿐이며 실제 AI 호출·자동 전송·검증 결과 생성 없음.
4. 제보는 공개 GitHub Issue 화면으로 이동하며 별도 로그인·수동 제출. 긴 URL은 오류로 처리하고 초안 보존.
5. 모바일 실기기, 접근성, 제보 개인정보 누출, 독립적인 사람의 이해도 테스트는 아직 미검증.

## PI-MOBILE v0.2.1 — 착취 방지 및 기여자 권리 기준

**원칙:** 동의가 있다는 이유만으로 착취 부재를 입증할 수 없고, 무보수라는 이유만으로 모든 자발적 행위를 동일하게 평가하지도 않는다. 누가 편익을 얻는지, 누가 시간·건강·기회비용·자료·수정 비용을 부담하는지, 실질적 거부·이탈·기여 인정을 확인한다.

1. **열람과 학습:** 무료·비가입·무기여 원칙. 앱의 판별 실습 선택·메모는 자동 서버 제출되지 않음. 연구 참여를 위한 회원가입이나 의무 검증 없음.
2. **작은 제보:** 이미 알고 있는 출처 링크, 단순 오류, 질문만 선택적 접수. 새 문헌 탐색·복잡한 반례 입증·재현 노동을 요구하지 않음. 현재 이 앱의 간단한 제보에는 금전 보상 약속이 없음을 게시 전에 알림.
3. **노동집약 과제:** 체계적 선행문헌 조사, 번역, 코딩, 재현 실험, 대량 분류, 심층 감사는 본 앱에서 **모집 중단**. 추후 요청하려면 사전에 실제 예산·작업량·대가·지급 기준·권리·원저자·공개·거절·중단·분쟁 절차를 명시하고 합의해야 함. 모집 재개 또는 보상 약속으로 오해 금지.
4. **기여 귀속:** 초기 창시자·원저자 학자·선행 자료 작성자·새 제보자·재검증자·보조 AI의 역할은 구분. 앱은 새로운 저작권 일괄 양도 동의를 받지 않으나, GitHub 이용약관과 외부 자료 원저작권의 적용은 별도 검토. 감사를 표하거나 이름을 기록하는 일은 금전 보상의 자동 대체가 아님. 기존에 누적된 기여의 정산 쟁점도 별도 유지.
5. **이탈권:** 제보 전 언제든 중단 가능. 공개 GitHub Issue는 계정과 텍스트가 노출된다. 사후 수정·삭제를 요청하더라도 포크·검색엔진·인용·보관본의 완전 제거는 보장되지 않음. 앱에는 익명 접수 수단이 아직 없음.
6. **후속 편익:** 연구비 확보, 공개 데이터의 독점화, 사업화 등 편익 구조가 바뀌면 참여자의 손익·권리·보상 합의를 재검토해야 한다. 보상이 자동 발생하거나 지급이 이미 확보됐다는 뜻은 아님.
7. **적용 범위:** 모바일 앱의 일반인 모집·접수 경로에 대한 차단임. 외부의 기존 GitHub Issue 템플릿·PR·채팅까지 기술적으로 차단한 것은 아님. 따라서 조직 운영 자체의 독립적 감사 필요.

### 원출처·범위
- UNESCO (2021), *Recommendation on Open Science*: 과학 기여 인정·평가와 개방과학에서 발생할 착취·불평등·지식 상실 위험. https://www.unesco.org/en/legal-affairs/recommendation-open-science
- ECSA, *Ten Principles of Citizen Science*: 좋은 시민과학에 필요한 연구자·참여자 권리·기여 인정·피드백 원칙. https://ecsa.citizen-science.net/10-principles/
- Zooniverse, *Acknowledging Volunteers*: 개별 기여 공개 인정과 공동저자 사례. 기여 인정이 적정 보상을 보장한다는 뜻은 아님. https://help.zooniverse.org/transcription-project-guide/project-launch/
- CARE, *Principles for Indigenous Data Governance*: 원래 원주민 데이터 주권의 특수한 역사·권리 맥락에서 만든 원칙. 집단 편익·권한·윤리의 비교 틀로만 참조. 모든 앱 이용자에게 동일한 법적 지위를 자동 부여하는 규정으로 오용 금지. https://doi.org/10.5334/dsj-2020-043

**미검증:** 사용자 체감 착취·권리 보호의 실제 효과, 노동의 시장 보상 적정성, 지역별 저작권 및 철회 가능성. CI PASS는 윤리적 적정성 인증이 아님.

**v0.2.1 추가 차단:** 판별 실습에서 기여 제보 초안을 자동 작성·이동하는 버튼을 제거. 개인 학습 결과를 연구 자료로 수집하도록 유도하지 않음. 복사 가능한 독립검증 프롬프트는 개인 사용을 위한 보조 수단이며 AI 실행/전송은 없음.
