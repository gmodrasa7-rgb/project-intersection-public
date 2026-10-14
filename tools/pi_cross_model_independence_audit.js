"use strict";
// Project Intersection: independent-evidence / exposed-debate protocol diagnostic.
// Analytical mechanics inspired by existing provenance and causal-evaluation methods;
// this does not assert model identity, blinding or source authenticity.
const fs = require("node:fs");
function ensure(ok, code){if(!ok)throw new Error(code)}
function rootsById(nodes){
 const map=new Map(nodes.map(x=>[x.id,x])),memo=new Map(),active=new Set();
 ensure(map.size===nodes.length,"DUPLICATE_SOURCE_ID");
 function roots(id){
  ensure(map.has(id),"UNKNOWN_SOURCE:"+id);
  if(memo.has(id))return memo.get(id);
  ensure(!active.has(id),"SOURCE_CYCLE:"+id);
  active.add(id);
  const p=map.get(id).parents;
  ensure(Array.isArray(p),"INVALID_SOURCE_PARENTS");
  const out=new Set(p.length?p.flatMap(y=>[...roots(y)]):[id]);
  active.delete(id);memo.set(id,out);return out;
 }
 for(const id of map.keys())roots(id);
 return memo;
}
function stageScore(trial, stage, expected, byCell, byResponse, rootMap){
 const selected=expected.map(x=>byCell.get(x.agent_id+"|"+stage)).filter(Boolean);
 if(selected.length!==expected.length)return {status:"BLOCKED_INCOMPLETE_ROSTER",expected:expected.length,observed:selected.length,accuracy:null,naive_unanimity:null,known_dependency_clusters:null,declared_root_count:null};
 const attrs=new Map(trial.agents.map(a=>[a.agent_id,a]));
 const sig=new Map(),parents=selected.map((_,i)=>i);
 function find(x){while(parents[x]!==x){parents[x]=parents[parents[x]];x=parents[x]}return x}
 function union(i,j){const a=find(i),b=find(j);if(a!==b)parents[b]=a}
 function upstream(r){
   const bag=new Set([r.agent_id]);
   for(const id of r.read_response_ids){const src=byResponse.get(id);ensure(src,"UNKNOWN_RESPONSE_REFERENCE:"+id);bag.add(src.agent_id)}
   return bag;
 }
 const keys=selected.map(r=>{
  const a=attrs.get(r.agent_id),base=new Set(["model:"+a.lineage_id]);
  for(const id of r.source_ids)for(const root of rootMap.get(id))base.add("source:"+root);
  for(const member of upstream(r))base.add("exposure:"+member);
  return base;
 });
 for(let i=0;i<selected.length;i++)for(let j=0;j<i;j++){
  if([...keys[i]].some(x=>keys[j].has(x)))union(i,j);
 }
 const correctness=trial.gold===null?null:selected.filter(r=>r.choice===trial.gold).length/selected.length;
 const choices=new Set(selected.map(r=>r.choice));
 const allRoots=new Set(selected.flatMap(r=>r.source_ids.flatMap(id=>[...rootMap.get(id)])));
 return {status:"DECLARED_PROVENANCE_ONLY",expected:expected.length,observed:selected.length,
 accuracy:correctness,naive_unanimity:choices.size===1,
 majority_count:Math.max(...[...choices].map(c=>selected.filter(x=>x.choice===c).length)),
 known_dependency_clusters:new Set(parents.map((_,i)=>find(i))).size,
 declared_root_count:allRoots.size,
 self_reported_no_read_count:selected.filter(r=>r.read_response_ids.length===0).length,
 model_independence_verified:false,scientific_replication:false};
}
function audit(packet){
 ensure(packet&&packet.schema==="pi-cross-model-independence/v0.1","SCHEMA");
 ensure(Array.isArray(packet.trials)&&packet.trials.length>0,"NO_TRIALS");
 const seen=new Set();
 const reports=packet.trials.map(t=>{
  ensure(typeof t.case_id==="string"&&t.case_id,"BAD_CASE");
  ensure(!seen.has(t.case_id),"DUPLICATE_CASE");seen.add(t.case_id);
  ensure(typeof t.gold==="string"||t.gold===null,"BAD_GOLD");
  ensure(Array.isArray(t.agents)&&t.agents.length>=2,"NOT_MULTIMODEL");
  ensure(t.agents.every(a=>typeof a.agent_id==="string"&&a.agent_id&&typeof a.lineage_id==="string"&&a.lineage_id),"BAD_AGENTS");
  ensure(new Set(t.agents.map(a=>a.agent_id)).size===t.agents.length,"DUPLICATE_AGENT");
  ensure(Array.isArray(t.stages)&&t.stages.includes("blind")&&t.stages.every(s=>["blind","debate"].includes(s))&&new Set(t.stages).size===t.stages.length,"BAD_STAGES");
  ensure(Array.isArray(t.sources)&&Array.isArray(t.responses),"BAD_DATA");
  const roots=rootsById(t.sources);
  const cells=new Map(),responses=new Map(),validAgents=new Set(t.agents.map(a=>a.agent_id));
  for(const r of t.responses){
   ensure(r&&typeof r.response_id==="string"&&r.response_id,"BAD_RESPONSE_ID");
   ensure(!responses.has(r.response_id),"DUPLICATE_RESPONSE_ID");responses.set(r.response_id,r);
   ensure(validAgents.has(r.agent_id)&&t.stages.includes(r.stage),"UNREGISTERED_RESPONSE");
   ensure(typeof r.choice==="string"&&r.choice,"BAD_CHOICE");
   ensure(Array.isArray(r.source_ids)&&r.source_ids.every(id=>roots.has(id)),"UNREGISTERED_SOURCE");
   ensure(Array.isArray(r.read_response_ids)&&new Set(r.read_response_ids).size===r.read_response_ids.length,"BAD_EXPOSURE");
   const key=r.agent_id+"|"+r.stage;
   ensure(!cells.has(key),"DUPLICATE_CELL");cells.set(key,r);
  }
  let badVisibility=false;
  for(const r of t.responses){
    if(r.stage==="blind"&&r.read_response_ids.length)badVisibility=true;
    for(const id of r.read_response_ids){
      ensure(responses.has(id),"UNKNOWN_EXPOSURE_SOURCE");
      if(responses.get(id).stage!=="blind"||r.stage!=="debate")badVisibility=true;
      if(id===r.response_id)badVisibility=true;
    }
  }
  const expected=t.agents.flatMap(a=>t.stages.map(stage=>a.agent_id+"|"+stage));
  const missing=expected.filter(x=>!cells.has(x));
  const blocked=missing.length>0||badVisibility;
  const per_stage={};
  for(const stage of t.stages){
   per_stage[stage]=blocked ? {status:missing.length?"BLOCKED_INCOMPLETE_ROSTER":"BLOCKED_VISIBILITY",accuracy:null,naive_unanimity:null,known_dependency_clusters:null} :
      stageScore(t,stage,t.agents,cells,responses,roots);
  }
  const delta=blocked||!t.stages.includes("debate")||t.gold===null?null:per_stage.debate.accuracy-per_stage.blind.accuracy;
  return {case_id:t.case_id,status:blocked?missing.length?"BLOCKED_INCOMPLETE_ROSTER":"BLOCKED_VISIBILITY":"DECLARED_TRACE_ONLY",
    expected_cells:expected.length,observed_cells:cells.size,missing_cells:missing,
    per_stage,debate_minus_blind_accuracy:delta,
    scientific_independence_verified:false,live_model_experiment:false};
 });
 return {schema:packet.schema,evidence:"ANALYSER_ONLY; SELF_REPORTED_PROVENANCE; MODEL_INDEPENDENCE_UNVERIFIED",
  case_count:reports.length,blocked_cases:reports.filter(x=>x.status.startsWith("BLOCKED")).length,
  reports, warning:"Declared source roots, model lineage and no-exposure assertions are not authenticated. Human or model-submitted JSON does not prove blinding, model provenance, independent data, or external scientific replication."};
}
function selftest(){
 function packet(opts={}){
  const ids=["A","B","C","D"];
  const sources=ids.map(a=>({id:"S"+a,parents:opts.shared?["ROOT"]:[]}));
  if(opts.shared)sources.unshift({id:"ROOT",parents:[]});
  const agents=ids.map(a=>({agent_id:a,lineage_id:opts.sameLineage?"common":"family"+a}));
  const responses=ids.flatMap(a=>{
    const blind={response_id:a+"0",agent_id:a,stage:"blind",choice:"WRONG",source_ids:["S"+a],read_response_ids:[]};
    const debate={response_id:a+"1",agent_id:a,stage:"debate",choice:"RIGHT",source_ids:["S"+a],read_response_ids:opts.expose?[ids[(ids.indexOf(a)+1)%4]+"0"]:[]};
    return [blind,debate];
  });
  return {schema:"pi-cross-model-independence/v0.1",trials:[{case_id:"toy",gold:"RIGHT",stages:["blind","debate"],agents,sources,responses}]};
 }
 let checks=0;function check(c,label){ensure(c,label);checks++}
 const a=audit(packet({shared:true,expose:true})).reports[0];
 check(a.status==="DECLARED_TRACE_ONLY","BASE_STATUS");
 check(a.per_stage.blind.naive_unanimity===true&&a.per_stage.blind.known_dependency_clusters===1,"FALSE_FOUR_VOTES");
 check(a.debate_minus_blind_accuracy===1,"TOY_DELTA");
 check(a.scientific_independence_verified===false&&a.per_stage.blind.model_independence_verified===false,"NO_FALSE_SCIENCE");
 const b=audit(packet({sameLineage:true})).reports[0];
 check(b.per_stage.blind.declared_root_count===4&&b.per_stage.blind.known_dependency_clusters===1,"MODEL_LINEAGE_COLLISION");
 const c=audit(packet()).reports[0];
 check(c.per_stage.blind.known_dependency_clusters===4&&c.scientific_independence_verified===false,"DISJOINT_NOT_PROOF");
 const d=packet();d.trials[0].responses=d.trials[0].responses.filter(x=>x.agent_id!=="D");
 const rr=audit(d).reports[0];
 check(rr.status==="BLOCKED_INCOMPLETE_ROSTER"&&rr.missing_cells.length===2&&rr.per_stage.blind.accuracy===null,"WHOLE_RUN_ATTRITION");
 const e=packet();e.trials[0].responses[0].read_response_ids=["B0"];
 check(audit(e).reports[0].status==="BLOCKED_VISIBILITY","BLIND_EXPOSURE");
 const f=packet();f.trials[0].sources[0].parents=["SB"];f.trials[0].sources[1].parents=["SA"];
 let failed=false;try{audit(f)}catch(err){failed=String(err).includes("SOURCE_CYCLE")}check(failed,"CYCLE_REJECTED");
 const g=packet();g.trials[0].responses.push({...g.trials[0].responses[0],response_id:"Rogue",agent_id:"X"});
 failed=false;try{audit(g)}catch(err){failed=String(err).includes("UNREGISTERED_RESPONSE")}check(failed,"ROGUE_REJECTED");
 const h=packet();h.trials[0].responses.push({...h.trials[0].responses[0],response_id:"DuplicateCell"});
 failed=false;try{audit(h)}catch(err){failed=String(err).includes("DUPLICATE_CELL")}check(failed,"DUPLICATE_REJECTED");
 const i=packet();i.trials[0].sources=[{id:"P",parents:[]}];i.trials[0].responses[0].source_ids=["MISSING"];
 failed=false;try{audit(i)}catch(err){failed=String(err).includes("UNREGISTERED_SOURCE")}check(failed,"UNVERIFIED_SOURCE_REJECTED");
 return {pass:true,checks,toy_cases:9,live_model_samples:0,independent_validation:false};
}
if (require.main === module) {
  try {
    const arg = process.argv[2];
    if (arg === "--selftest") process.stdout.write(JSON.stringify(selftest(), null, 2)+"\n");
    else if (arg && process.argv.length===3) {
      const data=JSON.parse(fs.readFileSync(arg,"utf8"));
      process.stdout.write(JSON.stringify(audit(data), null, 2)+"\n");
    } else {process.stderr.write("Usage: node tools/pi_cross_model_independence_audit.js --selftest | DATA.json\n"); process.exitCode=2;}
  } catch (err) {process.stderr.write(String(err.message)+"\n");process.exitCode=1;}
}
module.exports = {audit, selftest};
