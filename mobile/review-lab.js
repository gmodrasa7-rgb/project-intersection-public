/* PI Mobile v0.2 source-first review. No network, AI call or telemetry. */
(() => {
"use strict";
const $ = id => document.getElementById(id);
const base = "https://github.com/gmodrasa7-rgb/project-intersection-public/blob/";
const snapshot = "7913d78024ce98de3a4c3409e92e6d59adcf455a";
const records = [
{id:"E009",state:"SYNTHETIC_NEGATIVE",source:"experiments/e009/RESULT",
 ko:["복잡한 후보가 단순 기준선보다 열세","사전등록 합성 비교: 평균 후회값 42.35% 악화, 4개 기준 중 3개 실패.","현실 AI·인간의 공존이 불가능하다는 증명이 아님.","외부 환경·독립 재현 결과 미확인."],
 en:["Complex candidate worse than simple baseline","Preregistered synthetic comparison: 42.35% worse mean regret; 3 of 4 criteria failed.","Not proof that real humans or AI cannot coexist.","Independent replication and transfer to external conditions remain unknown."]},
{id:"E008",state:"NO_MAIN_RESULT",source:"experiments/e008/README",
 ko:["정책 비교 본실험 미실행","연구 설계·사전등록 자료는 존재.","실행된 정책 비교의 효과가 입증된 것이 아님.","실제 시행 결과와 독립 재현 미확인."],
 en:["No completed policy comparison main result","Design and preregistration exist.","Not proof of an executed policy comparison or efficacy.","Results of execution and independent replication remain unknown."]},
{id:"E007",state:"SYNTHETIC_LIMITED",source:"experiments/e007/README",
 ko:["합성 조건 분류 변화","선정한 합성 72개 조건에서 17개 분류 변화.","현실의 인과관계나 동기를 확인한 것이 아님.","다른 조건·현장 자료에 대한 일반화 미확인."],
 en:["Selected synthetic classification changes","17 changes among 72 selected synthetic timing conditions.","Not evidence of real-world causation or motivation.","Generalization to other settings and field data is unknown."]}
];
const tr={
ko:{title:"원문 판별 실습",intro:"선행 시민과학 방식 응용: 원문 먼저 확인 → 독립 잠정 판단 → 한계와 반례 검토. 응답을 점수·학술 실증으로 환산하지 않음.",choose:"사례 선택",frozen:"원문 고정판 ↗",live:"현재 원문 ↗",judgment:"내 잠정 판단",options:["판단 유보·모름","현실 인과관계 입증","합성시험의 제한된 결과","본실험 결과 없음"],reveal:"근거 범위 확인",supported:"원문에서 확인된 것",unsupported:"확인되지 않은 것",unknown:"미확인",note:"추가 반례·경쟁설명 (선택)",send:"제보 초안으로 옮기기",prompt:"AI 독립검증 요청문 복사",privacy:"판단·메모는 페이지 안에서만 유지. 자동 제출·AI 호출 없음.",copied:"복사 완료. 외부 AI에는 직접 붙여넣어야 함.",failed:"클립보드 복사 불가. 브라우저 권한 확인.",ready:"제보 초안으로 이동. 공개 전 검토 필요.",noChoice:"모름도 허용. 판단을 선택해 근거 범위를 확인할 수 있음.",choice:"선택한 잠정 판단",aligned:"원문 분류와 일치. 과학적 검증 점수 아님.",notAligned:"선택한 결론이 원문 범위를 벗어나거나 결과 상태와 다름.",unknownChoice:"모름은 유효한 보류. 원문 확인 필요.",promptText:"Project Intersection 외부 검토. 옹호하지 말고 원문부터 확인하라. URL에 접근할 수 없으면 불가능하다고 명시. 관측·가설·합성결과·현실실증·미관측을 분리하고, 반례/경쟁설명/원저자 선행연구를 찾으라. 데이터·출처·독립성·검증 불가능성을 구분하라. 확인하지 않은 원문을 읽은 척하지 말 것."},
en:{title:"Primary-source review exercise",intro:"Inspired by citizen science: inspect the original → record a provisional judgment → examine limitations and contrary explanations. No scientific scores or telemetry.",choose:"Choose case",frozen:"Frozen source ↗",live:"Current source ↗",judgment:"My provisional judgment",options:["Hold / unknown","Real-world causation proven","Limited synthetic finding","No completed main result"],reveal:"Inspect evidence boundary",supported:"What the source supports",unsupported:"What it does not establish",unknown:"Still unknown",note:"Counterexample or alternative (optional)",send:"Transfer to draft report",prompt:"Copy independent AI-audit prompt",privacy:"Judgment and notes remain on this page. No automatic publication or AI call.",copied:"Copied. Paste into an external AI yourself.",failed:"Clipboard unavailable; check browser permissions.",ready:"Report draft prepared. Review before public posting.",noChoice:"Unknown is an acceptable response. Choose a provisional judgment to inspect the boundary.",choice:"Provisional judgment",aligned:"Matches the recorded boundary; not a scientific validation score.",notAligned:"The choice overstates or conflicts with the limited record.",unknownChoice:"Holding judgment is valid. Inspect the original source.",promptText:"Independently review Project Intersection without advocacy. Inspect the primary source first. If you cannot access it, say so. Separate observations, hypotheses, synthetic findings, field validation, missing observations, counterexamples and prior art. Check attribution and independence. Do not invent citations or imply that an unread source was examined."}
};
let selected="E009",revealed=false;
function language(){return document.documentElement.lang==="en"?"en":"ko";}
function text(id,v){$(id).textContent=v;}
function link(record,l,sha){return base+sha+"/"+record.source+"_"+l.toUpperCase()+".md";}
function render(){
 const l=language(),t=tr[l],r=records.find(v=>v.id===selected);
 for(const [id,key] of [["labTitle","title"],["labIntro","intro"],["caseLabel","choose"],["judgmentLabel","judgment"],["showExplanation","reveal"],["notesLabel","note"],["issueTransfer","send"],["copyAIPrompt","prompt"],["labPrivacy","privacy"]])text(id,t[key]);
 $("caseSelector").replaceChildren(...records.map(c=>{const o=document.createElement("option");o.value=c.id;o.textContent=c.id+" · "+c[l][0];return o;}));
 $("caseSelector").value=selected;
 const choices=$("judgment");const prior=choices.value;
 choices.replaceChildren(...t.options.map((x,i)=>{const o=document.createElement("option");o.value=["UNKNOWN","REAL_WORLD","SYNTHETIC","NO_MAIN"][i];o.textContent=x;return o;}));if(prior)choices.value=prior;
 text("labCaseTitle",r[l][0]);text("labStatus",r.id+" · "+r.state+" · source snapshot: "+snapshot.slice(0,12));
 $("frozenSource").href=link(r,l,snapshot);text("frozenSource",t.frozen);
 $("liveSource").href=link(r,l,"main");text("liveSource",t.live);
 if(revealed)show();
}
function show(){
 const l=language(),t=tr[l],r=records.find(v=>v.id===selected),guess=$("judgment").value;
 text("sourceSupport",r[l][1]);text("sourceLimit",r[l][2]);text("sourceUnknown",r[l][3]);
 for(const [id,key] of [["supportHead","supported"],["limitHead","unsupported"],["unknownHead","unknown"]])text(id,t[key]);
 const expected=r.state==="NO_MAIN_RESULT"?"NO_MAIN":"SYNTHETIC";
 const verdict=guess==="UNKNOWN"?t.unknownChoice:guess===expected?t.aligned:t.notAligned;
 text("labFeedback",t.choice+": "+t.options[["UNKNOWN","REAL_WORLD","SYNTHETIC","NO_MAIN"].indexOf(guess)]+" — "+verdict);
 $("labOutcome").hidden=false;revealed=true;
}
$("caseSelector").addEventListener("change",()=>{selected=$("caseSelector").value;revealed=false;$("labOutcome").hidden=true;$("labNotes").value="";$("judgment").value="UNKNOWN";text("labFeedback",tr[language()].noChoice);render();});
$("showExplanation").addEventListener("click",show);
$("issueTransfer").addEventListener("click",()=>{
 const r=records.find(v=>v.id===selected),l=language(),t=tr[l],n=$("labNotes").value.trim();
 $("issueType").value="counterexample";
 $("subject").value=(r.id+" · "+r[l][0]).slice(0,90);
 $("description").value=(t.choice+": "+$("judgment").selectedOptions[0].textContent+"\n"+(n||r[l][3])).slice(0,800);
 $("source").value=link(r,l,snapshot);
 document.querySelector('[data-view="join"]').click();
 text("privacyNotice",t.ready+" "+(l==="ko"?"개인정보 배제 확인.":"Check for private information."));
 $("subject").focus();
});
$("copyAIPrompt").addEventListener("click",async()=>{
 const r=records.find(v=>v.id===selected),l=language(),t=tr[l];
 const prompt=t.promptText+"\nSource: "+link(r,l,snapshot)+"\nClaim: "+r[l][1]+"\nUncertainty: "+r[l][3];
 try{if(!navigator.clipboard?.writeText)throw Error("No clipboard");await navigator.clipboard.writeText(prompt);text("copyStatus",t.copied);}
 catch(_){text("copyStatus",t.failed);}
});
document.addEventListener("pi-language-changed",render);
render();text("labFeedback",tr[language()].noChoice);
})();