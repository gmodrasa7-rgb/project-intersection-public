const gains=[1,2,4,8],rights=[0,1,3,9],future=[0,1,3];
const choose=(g,r,f)=>r+f>=g?"C":"X";
const data=[];
for(const g of gains)for(const r of rights)for(const f of future)
  data.push({g,r,f,base:choose(g,r,f),noFuture:choose(g,r,0),twiceGain:choose(2*g,r,f)});
const count=k=>data.filter(x=>x[k]==="C").length;
const summary={schema:"C15.synthetic.v1",cases:data.length,parameters:{gains,rights,future},coexistBase:count("base"),coexistNoFuture:count("noFuture"),coexistTwiceGain:count("twiceGain"),collapseWhenFutureLost:data.filter(x=>x.base==="C"&&x.noFuture==="X").length,collapseWhenGainDoubled:data.filter(x=>x.base==="C"&&x.twiceGain==="X").length,unconditionalMaterialOnlyViolations:data.filter(x=>x.r===0&&x.f===0&&x.base==="C").length};
if(summary.cases!==48||summary.unconditionalMaterialOnlyViolations!==0)throw Error("CHECK_FAILED");
if(typeof process!=="undefined")process.stdout.write(JSON.stringify({summary,data},null,2)+"\n");
