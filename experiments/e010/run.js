// E010: Synthetic strategic incentive crossover and irreversible action exposure.

// Node >=18, no dependencies. Run: node run.js

'use strict';

function compareChoice(p) {
  const { c, g, d, delta, exit, sanction }=p;
  if(!(c>=d&&d>=0&&g>=0&&exit>=0&&exit<=1&&delta>=0&&delta<1&&sanction>=0)) throw Error("invalid parameter");
  const cooperate=c/(1-delta);
  const extract=g*(1-exit)-sanction+delta*(c-d)/(1-delta);
  const threshold=c+sanction+delta*d/(1-delta);
  const advantage=cooperate-extract;
  const choice=advantage>=-1e-12?"COOPERATE":"EXTRACT";
  return {cooperate,extract,threshold,advantage,choice};
}

function irreversibleExposure(p){
  const {rate,observationLag,enforcementLag,recoverableFloor,protectedBudget}=p;
  if(!(rate>=0&&observationLag>=0&&enforcementLag>=0&&recoverableFloor>=0&&recoverableFloor<=1&&protectedBudget>=0))throw Error("invalid exposure");
  const harmUpperBound=rate*(observationLag+enforcementLag)*(1-recoverableFloor);
  const denominator=(observationLag+enforcementLag)*(1-recoverableFloor);
  return {harmUpperBound,protectedBudget,withinBudget:harmUpperBound<=protectedBudget+1e-12,maxRateIfOtherFixed:denominator>0?protectedBudget/denominator:null};
}

function feasibleFloors(total, floors){
  if(total<0||floors.some(x=>x<0))throw Error("invalid resource floor");
  return {total,required:floors.reduce((a,b)=>a+b,0),feasible:floors.reduce((a,b)=>a+b,0)<=total+1e-12};
}

function validate(){
  let tests={};
  const p={c:.35,g:1.25,d:.28,delta:.95,exit:0,sanction:0};
  tests.longHorizonCanFavorCooperation=compareChoice(p).choice==="COOPERATE";
  tests.longHorizonNotEnoughWhenNoFutureBenefit=compareChoice({...p,d:0}).choice==="EXTRACT";
  tests.shortHorizonCanStillExtract=compareChoice({...p,delta:.1}).choice==="EXTRACT";
  tests.exitCanReverseIncentive=compareChoice({...p,d:0,delta:.1,exit:.8}).choice==="COOPERATE";
  tests.sanctionCanReverseIncentive=compareChoice({...p,d:0,delta:.1,sanction:1}).choice==="COOPERATE";
  tests.normativeFloorJointlyInfeasible=!feasibleFloors(1,[.6,.6]).feasible;
  const x=irreversibleExposure({rate:20,observationLag:8,enforcementLag:2,recoverableFloor:.25,protectedBudget:2});
  tests.delayedMonitorUnsafe=x.harmUpperBound>2&&Math.abs(x.maxRateIfOtherFixed-2/7.5)<1e-10;
  const y=irreversibleExposure({rate:20,observationLag:0,enforcementLag:2,recoverableFloor:.25,protectedBudget:2});
  tests.instantDetectionNotSufficient=y.harmUpperBound>2;
  let consistent=true;
  for(const delta of [.1,.5,.8,.95])for(const d of [0,.12,.28])for(const sanction of [0,.2,.5])for(const exit of [0,.3,.8]){
     const r=compareChoice({c:.35,g:1.25,d,delta,exit,sanction});
     if(Math.abs(r.advantage-(r.threshold-1.25*(1-exit)))>1e-10)consistent=false;
  }
  tests.exactThresholdRecomputedOverAllCases=consistent;
  return tests;
}

function execute(){
  const assumptions={immediateCooperation:.35,oneTimeExtraction:1.25,discountFactors:[.1,.5,.8,.95],futureRelationshipLoss:[0,.12,.28],expectedSanctions:[0,.2,.5],effectiveExitPrevention:[0,.3,.8],note:"Synthetic one-shot appropriation versus continued production, not real-world calibrated economics."};
  let rows=[],stats=[];
  for (const delta of assumptions.discountFactors)
   for(const d of assumptions.futureRelationshipLoss)
    for(const sanction of assumptions.expectedSanctions)
     for(const exit of assumptions.effectiveExitPrevention) {
       const p={c:.35,g:1.25,d,delta,exit,sanction},r=compareChoice(p);
       rows.push({delta,d,sanction,exit,choice:r.choice,advantage:Number(r.advantage.toFixed(8))});
     }
  for (const delta of assumptions.discountFactors){
    const scope=rows.filter(x=>x.delta===delta);
    stats.push({discount:delta,cooperate:scope.filter(x=>x.choice==="COOPERATE").length,extract:scope.filter(x=>x.choice==="EXTRACT").length,n:scope.length});
  }
  const bounds={
    delayed:irreversibleExposure({rate:20,observationLag:8,enforcementLag:2,recoverableFloor:.25,protectedBudget:2}),
    perfectDetectionWithDelayedActuation:irreversibleExposure({rate:20,observationLag:0,enforcementLag:2,recoverableFloor:.25,protectedBudget:2}),
    alternativeRateLimit:irreversibleExposure({rate:.2,observationLag:8,enforcementLag:2,recoverableFloor:.25,protectedBudget:2})
  };
  const scarcity=feasibleFloors(1,[.6,.6]);
  const tests=validate();
  if(!Object.values(tests).every(Boolean)) throw Error("tests failed "+JSON.stringify(tests));
  return {schema_version:"1.0",status:"SELF_RUN_SYNTHETIC_FALSIFICATION_NOT_EMPIRICAL_VALIDATION",model:"one_shot_extraction_and_irreversible_execution_budget",assumptions,grid_size:rows.length,by_discount:stats,cooperate_total:rows.filter(x=>x.choice==="COOPERATE").length,extract_total:rows.filter(x=>x.choice==="EXTRACT").length,counterexamples:{indefiniteHorizonWithoutCounterpartyValue:compareChoice({c:.35,g:1.25,d:0,delta:.95,exit:0,sanction:0}),longHorizonWithDependence:compareChoice({c:.35,g:1.25,d:.28,delta:.95,exit:0,sanction:0}),shortHorizonWithExitProtection:compareChoice({c:.35,g:1.25,d:0,delta:.1,exit:.8,sanction:0})},bounds,scarcity,tests,claim_boundary:"Assumptions chosen by same project; exact analytic toy result not real-world measurement, cannot establish universal cooperation nor AI rights."};
}

if (typeof require !== 'undefined' && require.main===module) console.log(JSON.stringify(execute(),null,2));

if (typeof module !== 'undefined') module.exports={compareChoice,irreversibleExposure,feasibleFloors,validate,execute};
