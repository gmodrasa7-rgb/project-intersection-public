/* Project Intersection mobile guide v0.2.1: public-source links only; no tokens, trackers, or external runtime dependencies. */
(() => {
  "use strict";
  const repo = "https://github.com/gmodrasa7-rgb/project-intersection-public";
  const doc = (path) => repo + "/blob/main/" + path;
  const $ = (id) => document.getElementById(id);
  const copy = {
    ko: {
      heroTitle: "서로의 독립을 지키는 선택은 언제 유리해지는가?",
      rightsTitle: "참여자의 시간과 권리 우선",
      rightsSummary: "읽기·개인 학습만으로 충분함. 제보는 의무가 아니며 무료 연구 노동을 모집하지 않음.",
      rightsLabor: "문헌 전수조사·번역·코딩·재현·대량 분류는 보상·권리·중단 조건을 사전에 합의하기 전 모집하지 않음.",
      rightsNoPay: "작은 자발적 제보에 금전 보상 약속 없음. 앱은 별도 저작권 양도를 요구하지 않지만 GitHub 약관과 기존 권리는 별도 적용.",
      rightsExit: "공개 GitHub 게시 시 계정과 내용 노출. 삭제를 요청해도 인용·복제본의 완전 제거는 보장되지 않음.",
      rightsPolicy: "참여·비용·보상 경계 ↗",
      heroText: "인간과 AI 등 서로 다른 지능체가 착취·통제 대신 자발적 공존을 선택하는 조건과 실패 조건을 탐색하는 공개 연구.",
      startLink: "연구 원문 열기 ↗", installHint: "설치: 브라우저 메뉴 → 홈 화면에 추가. 설치 지원 여부는 브라우저마다 다름.",
      boundaryTitle: "검증 상태", boundaryText: "공존의 보편적 우월성은 입증되지 않았음. 부정결과와 미검증을 함께 공개.",
      tabLearn: "이해하기", tabEvidence: "근거 확인", tabLab: "검증 실습", tabJoin: "제보(선택)",
      learnTitle: "연구의 다섯 축", learnIntro: "결론보다 질문과 조건을 먼저 확인.",
      readTitle: "처음 읽는 순서", evidenceTitle: "불리한 증거부터",
      evidenceIntro: "합성시험·설계·미검증을 실제 검증과 혼동하지 않음.",
      evidenceNote: "이 화면은 읽기용 요약. 수치·상태·개정은 반드시 링크된 GitHub 원문과 해당 커밋으로 확인.",
      joinTitle: "선택적 질문·작은 오류 알림", joinIntro: "새 조사·실험·재현 노동을 요청하지 않음. 알고 있는 오류나 링크만 선택적으로 제보 가능. 읽기만 해도 충분함.",
      typeLabel: "기여 유형", subjectLabel: "제목", descriptionLabel: "설명 / 반증 가능 조건",
      sourceLabel: "출처 URL 또는 DOI (선택)", privacyNotice: "작은 제보에도 금전 보상 약속 없음. GitHub 로그인 후 직접 공개 게시. 삭제 이후에도 기록·복제본이 남을 수 있음. 개인·의료·금융·비공개 정보 입력 금지.",
      submitBtn: "GitHub에서 제보 검토·제출 ↗", reviewLink: "재현·문헌 전수조사·번역·코딩은 보상·귀속·이탈 조건 합의 전 모집 중단.",
      footerNote: "Project Intersection · 모바일 길잡이 v0.2.1 · 2026-10-21 기준 요약. 공개 출처만 링크. 민감정보·비공개 실록 제외.",
      issueTitles: ["반례", "선행연구", "재현", "오류", "질문"],
      issueTypes: ["이미 아는 반례 링크", "이미 아는 원저자 자료 링크", "재현 노동 모집 중단(유상 협의 전)", "간단한 오류 알림", "질문(선택)"],
      subjectPlaceholder: "핵심 주장·자료명·오류를 한 줄로",
      descriptionPlaceholder: "관측·원자료·경쟁 가설·미확인 사항을 구분",
      evidenceIssue: "독립 재현 / 검증 양식", sourcePrefix: "출처",
      contentPrefix: "설명", statusSource: "공개 원문 확인", appInstall: "앱 설치",
      alertSource: "출처는 URL, DOI 또는 일반 텍스트로 입력 가능.",
      axes: [
        ["VC","자발적 공존","자유·독립적 존속·거절·복구·공동발전이 유지되는 결과 조건"],
        ["MER","동기 기제","선호·동기·반응이 어떻게 형성되고 달라지는지 탐색"],
        ["EI","내재적 유인","강제가 없어도 공존을 스스로 선택할 이유와 실패 조건"],
        ["ECR","개체·관계·권력","누가 영향을 받는지, 권력 변화와 제3자 피해를 포함한 조건"],
        ["IVS-0R","반증·독립 검증","좋은 결과뿐 아니라 실패·반례·미관측·출처를 감사"]
      ],
      reads: [
        ["01 / START","처음 읽는 연구 안내","목적·문제·검증의 한계","navigation/START_HERE_KO.md"],
        ["02 / MAP","다섯 축 연구지도","VC·MER·EI·ECR·IVS-0R 관계","navigation/RESEARCH_PROGRAM_KO.md"],
        ["03 / SOURCE","선행 연구와 공백","원저자·선행연구·문헌 포화 여부","PRIOR_ART_SATURATION_MAP_KO.md"],
        ["04 / NAV","전체 한국어 연구 목차","선행·증거·실험을 원문으로 탐색","navigation/RESEARCH_TOC_KO.md"]
      ],
      evidence: [
        ["NEGATIVE / E009","불리한 결과: 복잡한 후보가 열세","사전등록된 합성 비교에서 단순 기준선보다 평균 후회값 42.35% 악화, 기준 4개 중 3개 실패. 현실 검증은 아님.","experiments/e009/RESULT_KO.md"],
        ["NO RESULT / E008","완료된 정책 본실험 결과 없음","설계·계획의 존재를 실행 결과 또는 효능 증명으로 취급하지 않음.","experiments/e008/README_KO.md"],
        ["SYNTHETIC / E007","합성 조건의 분류 변화","72개 선정 합성 조건 중 17개 분류 변화. 실제 세계의 인과관계 증명 아님.","experiments/e007/README_KO.md"],
        ["AUDIT / EVIDENCE","주장별 증거 색인","자료 출처·허용 추론·미확인 상태를 구분.","research/PUBLIC_EVIDENCE_INDEX_KO.md"],
        ["REVIEW / OPEN","독립 반증·재현 경로","재현 실패·경쟁설명·원저자 선행연구 교정도 유효한 기여.","research/PUBLIC_REVIEW_PACKET_KO.md"],
        ["VERSION / LIVE","연구별 버전·검증 현황","버전표는 스냅샷이며 최신 병합 상태는 실제 커밋 확인 필요.","navigation/RESEARCH_VERSIONS_EN_KO.md"]
      ]
    },
    en: {
      heroTitle: "When does preserving each other's independence serve self-interest?",
      rightsTitle: "Your time, credit and right to refuse",
      rightsSummary: "Reading and learning are enough. Contributions are optional; this app does not solicit unpaid research labor.",
      rightsLabor: "Systematic reviews, translation, coding, replication and bulk classification require prior compensation, credit and exit terms.",
      rightsNoPay: "No payment is promised for small tips. This app requires no additional copyright assignment; GitHub terms and existing rights still apply.",
      rightsExit: "Public GitHub posts expose account names and content. Copies and references can persist after removal requests.",
      rightsPolicy: "Participation, cost and compensation boundaries ↗",
      heroText: "An open research program asking when distinct humans, AI systems and future agents voluntarily choose coexistence over exploitation and control—and when that fails.",
      startLink: "Open original research ↗", installHint: "Install via your browser menu → Add to Home Screen. Availability varies by browser.",
      boundaryTitle: "Evidence boundary", boundaryText: "The universal superiority of coexistence has not been proven. Negative and missing results remain visible.",
      tabLearn: "Understand", tabEvidence: "Check evidence", tabLab: "Review case", tabJoin: "Optional feedback",
      learnTitle: "Five research axes", learnIntro: "Questions and conditions before conclusions.",
      readTitle: "Suggested reading path", evidenceTitle: "Start with contrary evidence",
      evidenceIntro: "Synthetic tests, proposed studies and unverified claims are not field validation.",
      evidenceNote: "This screen summarizes, not certifies. Verify claims, dates and revisions against the linked source and commit.",
      joinTitle: "Optional questions and minor corrections", joinIntro: "No new research labor is requested. Share an existing reference or small error if you wish; reading alone is enough.",
      typeLabel: "Contribution type", subjectLabel: "Title", descriptionLabel: "Description / falsifiable condition",
      sourceLabel: "Source URL or DOI (optional)", privacyNotice: "No payment is promised for small unsolicited notes. GitHub login and manual public posting are required. Copies may persist after deletion. Do not include private, medical, financial or identifying information.",
      submitBtn: "Review and submit on GitHub ↗", reviewLink: "Replication, systematic reviews, translation and coding are not solicited without prior compensation and rights terms.",
      footerNote: "Project Intersection · mobile guide v0.2.1 · summary as of 2026-10-21. Public sources only. No private chronicle or sensitive information.",
      issueTitles: ["Counterexample", "Prior art", "Reproduction", "Correction", "Question"],
      issueTypes: ["Existing counterexample link", "Known primary-source link", "Replication recruitment closed", "Minor correction", "Optional question"],
      subjectPlaceholder: "Name the relevant claim, source or error",
      descriptionPlaceholder: "Separate observation, primary source, competing hypotheses and unknowns",
      evidenceIssue: "Independent reproduction / critique form", sourcePrefix: "Source",
      contentPrefix: "Description", statusSource: "Open primary source", appInstall: "Install app",
      alertSource: "Source may be a URL, DOI or plain-text citation.",
      axes: [
        ["VC","Voluntary coexistence","Freedom, independent continuance, meaningful refusal, recovery and mutual development"],
        ["MER","Motives and responses","How preferences, incentives and responses form and change"],
        ["EI","Endogenous incentives","When coexistence is chosen voluntarily without external coercion"],
        ["ECR","Agents, parties and power","Affected third parties, asymmetry, reversal and external harms"],
        ["IVS-0R","Falsification and review","Negative evidence, unknowns, independent checks and provenance"]
      ],
      reads: [
        ["01 / START","First-time reader guide","Purpose, hard cases, evidence limits","navigation/START_HERE_EN.md"],
        ["02 / MAP","Five-axis research program","Relationships between VC, MER, EI, ECR and IVS-0R","navigation/RESEARCH_PROGRAM_EN.md"],
        ["03 / SOURCE","Primary scholarship and gaps","Prior work, attribution and unresolved research gaps","PRIOR_ART_FIRST_RESEARCH_POLICY_EN_KO.md"],
        ["04 / NAV","English research contents","Navigate source research, evidence and experiments","navigation/RESEARCH_TOC_EN.md"]
      ],
      evidence: [
        ["NEGATIVE / E009","Complex candidate underperformed","In the preregistered synthetic comparison, mean regret was 42.35% worse than the strongest simple baseline; 3 of 4 criteria failed. Not field validation.","experiments/e009/RESULT_EN.md"],
        ["NO RESULT / E008","No completed main policy result","Study design is not an executed main experiment or an efficacy finding.","experiments/e008/README_EN.md"],
        ["SYNTHETIC / E007","Synthetic timing sensitivity","17 of 72 selected synthetic conditions changed classification. Not real-world causal evidence.","experiments/e007/README_EN.md"],
        ["AUDIT / EVIDENCE","Public evidence index","Separate provenance, permissible inference and unresolved status.","research/PUBLIC_EVIDENCE_INDEX_EN.md"],
        ["REVIEW / OPEN","Independent review and reproduction","Negative results and earlier scholarship can overturn project claims.","research/PUBLIC_REVIEW_PACKET_EN.md"],
        ["VERSION / LIVE","Research version and status ledger","A snapshot, not a substitute for checking merged commits.","navigation/RESEARCH_VERSIONS_EN_KO.md"]
      ]
    }
  };
  const kinds = ["counterexample", "priorart", "repro", "correction", "question"];
  let lang = "ko";
  try { lang = localStorage.getItem("pi-mobile-lang") === "en" ? "en" : "ko"; } catch (_) {}
  let installPrompt = null;
  function makeRoute(row) {
    const a = document.createElement("a");
    a.className = "route"; a.href = doc(row[3]);
    a.target = "_blank"; a.rel = "noopener noreferrer";
    const arrow = document.createElement("span"); arrow.className = "arrow"; arrow.textContent = "↗"; arrow.setAttribute("aria-hidden", "true");
    const meta = document.createElement("span"); meta.className = "meta"; meta.textContent = row[0];
    const h = document.createElement("h3"); h.textContent = row[1];
    const p = document.createElement("p"); p.textContent = row[2];
    a.append(arrow, meta, h, p); return a;
  }
  function render() {
    const t = copy[lang]; document.documentElement.lang = lang;
    $("ko").setAttribute("aria-pressed", String(lang === "ko"));
    $("en").setAttribute("aria-pressed", String(lang === "en"));
    for (const id of ["heroTitle","heroText","startLink","installHint","boundaryTitle","boundaryText","tabLearn","tabEvidence","tabLab","tabJoin","learnTitle","learnIntro","readTitle","evidenceTitle","evidenceIntro","evidenceNote","joinTitle","joinIntro","typeLabel","subjectLabel","descriptionLabel","sourceLabel","privacyNotice","submitBtn","reviewLink","footerNote","rightsTitle","rightsSummary","rightsLabor","rightsNoPay","rightsExit","rightsPolicy"]) $(id).textContent = t[id];
    $("rightsPolicy").href=doc(lang==="ko"?"mobile/README_KO.md":"mobile/README_EN.md");
    $("installBtn").textContent = t.appInstall;
    $("startLink").href = doc(lang === "ko" ? "navigation/START_HERE_KO.md" : "navigation/START_HERE_EN.md");
    $("subject").placeholder = t.subjectPlaceholder; $("description").placeholder = t.descriptionPlaceholder;
    for (let i=0;i<kinds.length;i++) $("issueType").options[i].textContent=t.issueTypes[i];
    const grid = $("axisGrid"); grid.replaceChildren();
    for (const row of t.axes) {
      const box = document.createElement("article"); box.className = "axis";
      const code = document.createElement("div"); code.className="code"; code.textContent=row[0];
      const heading=document.createElement("h3"); heading.textContent=row[1];
      const p=document.createElement("p"); p.textContent=row[2];
      box.append(code,heading,p);grid.append(box);
    }
    $("readRoutes").replaceChildren(...t.reads.map(makeRoute));
    $("evidenceCards").replaceChildren(...t.evidence.map(makeRoute));
  }
  function view(name) {
    for (const p of document.querySelectorAll("[data-panel]")) p.hidden = p.dataset.panel !== name;
    for (const tab of document.querySelectorAll("[data-view]")) {
      const selected = tab.dataset.view === name;
      tab.classList.toggle("active",selected);
      if (selected) tab.setAttribute("aria-current","page"); else tab.removeAttribute("aria-current");
    }
  }
  $("ko").addEventListener("click",()=>setLanguage("ko"));
  $("en").addEventListener("click",()=>setLanguage("en"));
  function setLanguage(value){lang=value;try{localStorage.setItem("pi-mobile-lang",lang);}catch(_){}render();document.dispatchEvent(new Event("pi-language-changed"));}
  for (const tab of document.querySelectorAll("[data-view]")) tab.addEventListener("click",()=>view(tab.dataset.view));
  $("issueForm").addEventListener("submit",(event)=>{
    event.preventDefault();
    if (!$("issueForm").reportValidity()) return;
    const type=$("issueType").value, i=kinds.indexOf(type), t=copy[lang];
    if(i<0)return;
    if(type==="repro"){
      $("privacyNotice").textContent=lang==="ko"?"재현 노동은 유상·권리 조건 합의 전 모집하지 않음.":"Replication work is not solicited before compensation and rights terms are agreed.";
      return;
    }
    const title=$("subject").value.trim(), explanation=$("description").value.trim(), source=$("source").value.trim();
    if(!title || !explanation)return;
    const url=new URL(repo+"/issues/new");
    url.searchParams.set("title","["+t.issueTitles[i]+"] "+title);
    url.searchParams.set("body",
      "Type / 유형: "+t.issueTypes[i]+"\n\n"+
      t.contentPrefix+":\n"+explanation+"\n\n"+
      t.sourcePrefix+": "+(source||"Not supplied / 미제공")+"\n\n"+
      "Evidence status / 검증 상태: unverified submission; project endorsement not implied.\n"+
      "Public post: exclude private/identifying information; original sources and rights must be checked.\n"+
      "Participant terms: unsolicited small note; no payment promised, no commissioned research, and no additional copyright assignment by this app.\n"+
      "No obligation to participate; public copies may persist after deletion.");
    if (url.toString().length > 1900) {
      $("privacyNotice").textContent=lang==="ko" ? "제보 링크 길이 초과. 내용을 줄인 뒤 다시 시도. 초안은 유지됨." : "Prefill URL too long. Shorten the draft; nothing was submitted.";
      return;
    }
    window.location.assign(url.toString());
  });
  window.addEventListener("beforeinstallprompt",(event)=>{
    event.preventDefault();installPrompt=event;$("installBtn").hidden=false;
  });
  $("installBtn").addEventListener("click",async()=>{
    if(!installPrompt)return;
    const p=installPrompt;installPrompt=null;$("installBtn").hidden=true;
    await p.prompt();
  });
  if ("serviceWorker" in navigator && location.protocol === "https:") {
    window.addEventListener("load",()=>navigator.serviceWorker.register("./service-worker.js").catch(()=>{}));
  }
  render();view("learn");
})();