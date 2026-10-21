# Project Intersection 모바일 연구 앱 — 한국어 (v0.2.0)

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
