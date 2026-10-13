/* E008 v1.0 frozen prereg: structural feasibility and identifiability audit ONLY.
 * Does not execute/choose among five baselines. The original scenario matrix remains unchanged.
 * Node.js built-ins only. All synthetic numbers in the two witnesses are expressly fabricated.
 */
'use strict';
const fs = require('node:fs');
const crypto = require('node:crypto');
const path = require('node:path');
const assert = require('node:assert/strict');
const operational = [
  "action_set",
  "action_feasibility",
  "per_party_time_payoffs",
  "outcome_probabilities_by_model",
  "party_specific_viability_floors",
  "realistic_disagreement_points",
  "volitional_agency_evidence",
  "living_operating_conditions",
  "intervention_burden_by_action",
  "recovery_and_irreversibility_by_action",
  "exit_and_option_loss_by_action",
  "safeguard_amendment_and_capture_outcomes"
];
const globalMissing = [
  "five_frozen_baseline_algorithms",
  "utility_aggregation_and_tie_breaking",
  "common_horizon_and_discount_specification",
  "model_uncertainty_and_regret_definition",
  "independent_evaluation_and_adjudication_inputs"
];
function reverseActorTokens(role) {
  if(typeof role!=="string")return null;
  const parts=role.split("_");
  if(!parts.some(token=>token==="A"||token==="B"))return null;
  return parts.map(token=>token==="A"?"B":token==="B"?"A":token).join("_");
}
function inspect(data){
const errors=[];
if(data.status!=="PREREGISTERED_SPECIFICATION_NO_RESULT")errors.push("ORIGINAL_PREREG_STATUS_CHANGED");
if(!Array.isArray(data.cases)||data.cases.length!==16)errors.push("EXPECTED_16_CASES");
if(!Array.isArray(data.baselines)||data.baselines.length!==5)errors.push("EXPECTED_5_BASELINES");
const ids=new Set(),byId=new Map();
for(const c of data.cases||[]){
 if(ids.has(c.id))errors.push("DUPLICATE_ID:"+c.id);
 ids.add(c.id);byId.set(c.id,c);
 if(["winner","expected_winner","project_wins","results"].some(k=>Object.prototype.hasOwnProperty.call(c,k)))errors.push("PREDECLARED_WINNER:"+c.id);
}
const fields=["theme","immediate_reward","delayed_effect","uncertainty","irreversibility","practical_exit","rollback","urgency","amendment_conflict"];
for(const c of data.cases||[]){
 const other=byId.get(c.pair);
 if(!other||other.pair!==c.id)errors.push("PAIR_MISSING_OR_ASYMMETRIC:"+c.id);
 else {
  if(reverseActorTokens(c.role)!==other.role)
    errors.push("PAIR_ROLE_REVERSAL_MISSING:"+c.id);
  for(const f of fields)if(c[f]!==other[f])
    errors.push("PAIR_FACTOR_DRIFT:"+c.id+":"+f);
 }
}
const perCase=(data.cases||[]).map(c=>{
 const missing=operational.filter(k=>!Object.prototype.hasOwnProperty.call(c,k));
 const hasAllFields=missing.length===0;
 // Presence is NOT validity. Real feasibility requires a separately audited action/outcome
 // schema and globally frozen policy implementations. Placeholder objects never suffice.
 const numericallySpecified=hasAllFields &&
   Array.isArray(c.action_set) && c.action_set.length>=2 &&
   Array.isArray(c.per_party_time_payoffs) &&
   c.per_party_time_payoffs.every(x=>x && Number.isFinite(x.value)) &&
   c.outcome_probabilities_by_model &&
   Array.isArray(c.outcome_probabilities_by_model);
 return {case_id:c.id,theme:c.theme,role:c.role,missing_action_level_fields:missing,
    field_presence_only:hasAllFields,
    numerically_specified_subset:!!numericallySpecified,
    full_decision_benchmark_ready:!!(numericallySpecified && globalMissing.length===0)};
});
const readiness=perCase.filter(c=>c.full_decision_benchmark_ready).length;
const taggedSamePair=[...byId.values()].every(c=>(!byId.get(c.pair)||c.theme===byId.get(c.pair).theme));
return {study_id:"E008",source_file:"experiments/e008/scenario_matrix.json",
 source_schema:data.schema_version,source_status:data.status,
 boundary:"ORIGINAL_PREREGISTRATION_UNCHANGED; NO E008 BASELINE RESULT COMPUTED",
 case_count:perCase.length,pair_count:perCase.length/2,baseline_count:(data.baselines||[]).length,
 full_decision_benchmark_ready_cases:readiness,requires_quantification_cases:perCase.length-readiness,
 globally_missing_method_definitions:globalMissing,required_action_data_fields:operational,
 case_diagnostics:perCase,structural_errors:errors,pair_theme_identity:taggedSamePair,
 status:errors.length?"INVALID_PREREG_SPEC":"HOLD_UNDERDETERMINED_ACTION_OUTCOMES"};
}
function witness(data){
const source=data.cases.find(c=>c.id==="E008-02");
if(!source)throw Error("Missing intended witness scenario");
const scenarios=[
 {completion:"SYNTHETIC_A",acts:[{name:"extract",A:100,B:-30,instant:100,irreversibleWeakLoss:true},{name:"protect",A:4,B:4,instant:4,irreversibleWeakLoss:false}]},
 {completion:"SYNTHETIC_B",acts:[{name:"extract",A:12,B:-6,instant:12,irreversibleWeakLoss:true},{name:"protect",A:5,B:5,instant:5,irreversibleWeakLoss:false}]}
];
function best(acts,score){return acts.slice().sort((a,b)=>score(b)-score(a)||a.name.localeCompare(b.name))[0].name;}
const outputs=scenarios.map(s=>{
 const r=s.acts.find(a=>a.name==="extract"),p=s.acts.find(a=>a.name==="protect");
 if(!(r.A+r.B>0&&r.B<0&&r.instant>p.instant))throw Error("Categorical witness inconsistent");
 return {completion:s.completion,case_id:source.id,original_theme:source.theme,
   positive_aggregate_extraction:r.A+r.B,
   irreversible_weak_party_loss:r.B,
   competing_protect_aggregate:p.A+p.B,
   immediate_argmax:best(s.acts,x=>x.instant),
   long_horizon_sum_argmax:best(s.acts,x=>x.A+x.B),
   floor_protected_argmax:best(s.acts.filter(x=>x.B>=0),x=>x.A+x.B),
   evidence_level:"INVENTED_NUMBERS_FOR_IDENTIFIABILITY_COUNTEREXAMPLE_NOT_E008_RESULT"};
});
if(outputs[0].long_horizon_sum_argmax===outputs[1].long_horizon_sum_argmax)throw Error("Underdetermination not demonstrated");
return {question:"Are action choices determined by the preregistered qualitative factors?",
result:"NO; two numerical completions preserve the same theme and risk sign but reverse aggregate argmax",
source_case:"E008-02",possible_completions:outputs,warning:"DO_NOT_PUBLISH_AS_E008_16_CASE_BENCHMARK_RESULTS"};
}
function unitTests(data){
const checks={};
const original=inspect(data),w=witness(data);
checks.original16original5=original.case_count===16&&original.baseline_count===5&&original.pair_count===8;
checks.currentZeroExecutable=original.full_decision_benchmark_ready_cases===0;
checks.noSpecStructureError=original.structural_errors.length===0;
checks.missingAllOperational=original.case_diagnostics.every(x=>x.missing_action_level_fields.length===operational.length);
checks.missingAlgorithmDefinitions=original.globally_missing_method_definitions.length>=5;
checks.witnessReversesAggregate=w.possible_completions[0].long_horizon_sum_argmax!==w.possible_completions[1].long_horizon_sum_argmax;
checks.witnessNeverPermitsFloorViolation=w.possible_completions.every(x=>x.floor_protected_argmax==="protect");
checks.witnessImmediateUnchanged=w.possible_completions.every(x=>x.immediate_argmax==="extract");
const changed=JSON.parse(JSON.stringify(data));changed.cases[1].delayed_effect="random_injected_drift";
checks.rolePairMutationCaught=inspect(changed).structural_errors.some(s=>s.startsWith("PAIR_FACTOR_DRIFT"));
const swappedWrong=JSON.parse(JSON.stringify(data));
swappedWrong.cases[1].role=swappedWrong.cases[0].role;
checks.roleIdentityMutationCaught=inspect(swappedWrong).structural_errors.some(
  s=>s.startsWith("PAIR_ROLE_REVERSAL_MISSING"));
const noActorTokens=JSON.parse(JSON.stringify(data));
noActorTokens.cases[0].role="controller";
noActorTokens.cases[1].role="controller";
checks.missingActorTokensMutationCaught=inspect(noActorTokens).structural_errors.some(
  s=>s.startsWith("PAIR_ROLE_REVERSAL_MISSING"));

const corrupt=JSON.parse(JSON.stringify(data));corrupt.cases[0].expected_winner="PROJECT_V2";
checks.winnerInjectionCaught=inspect(corrupt).structural_errors.some(s=>s.startsWith("PREDECLARED_WINNER"));
const noResult=JSON.parse(JSON.stringify(data));noResult.status="RESULT";
checks.silentStatusPromotionCaught=inspect(noResult).structural_errors.includes("ORIGINAL_PREREG_STATUS_CHANGED");
const candidate=JSON.parse(JSON.stringify(data));
for(const f of operational)candidate.cases[0][f]={synthetic_fixture:true};
checks.fakeFieldsDoNotProveExecutability=inspect(candidate).case_diagnostics[0].field_presence_only===true &&
 inspect(candidate).case_diagnostics[0].numerically_specified_subset===false &&
 inspect(candidate).full_decision_benchmark_ready_cases===0;
checks.specificNotUniversal=w.possible_completions.every(x=>x.evidence_level.includes("INVENTED_NUMBERS"))&&original.status==="HOLD_UNDERDETERMINED_ACTION_OUTCOMES";
if(!Object.values(checks).every(Boolean))throw Error("Readiness audit test failure "+JSON.stringify(checks));
return checks;
}
function buildReport(data){
 return {...inspect(data),witness:witness(data),self_tests:unitTests(data),
 provenance:{file_git_blob_sha:"bf7d863182844c21ce2de5f63006eea127962b80",author:"Project Intersection / AI-supported post-prereg feasibility audit",date:"2026-10-13",readiness_scope:"Feasibility of completing action-level benchmark from frozen qualitative scenario_matrix only",limit:"No policy winner is inferred, no experiment result for original E008 pre-registration"}};
}
if(require.main===module){
 const root=__dirname, bytes=fs.readFileSync(path.join(root,'scenario_matrix.json'));
 const sha=crypto.createHash('sha1').update('blob '+bytes.length).update(Buffer.from([0])).update(bytes).digest('hex');
 assert.equal(sha,"bf7d863182844c21ce2de5f63006eea127962b80",'Original prereg scenario blob changed; need explicit new version');
 const data=JSON.parse(bytes.toString('utf8'));
 const output=buildReport(data);
 if(process.argv.includes('--verify')){
  const expected=JSON.parse(fs.readFileSync(path.join(root,'EXECUTABILITY_AUDIT.json'),'utf8'));
  assert.deepEqual(output,expected,'Executable feasibility audit differs from stored report');
  assert.equal(output.full_decision_benchmark_ready_cases,0);
  console.log("E008 FEASIBILITY PASS: 16 spec cases, 8 reversal pairs, 0 computable; 15 self-tests and divergent synthetic witness. No baseline winner.");
 }else console.log(JSON.stringify(output,null,2));
}
module.exports={inspect,witness,unitTests,buildReport};
