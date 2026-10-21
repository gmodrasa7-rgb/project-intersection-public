import assert from "node:assert/strict";
import { readFileSync, existsSync } from "node:fs";
const root = new URL("./", import.meta.url);
const at = (name) => new URL(name, root);
const read = (name) => readFileSync(at(name),"utf8");
const html = read("index.html"), js = read("app.js"), manifest=JSON.parse(read("manifest.webmanifest"));
for (const file of ["index.html","app.js","review-lab.js","styles.css","service-worker.js","icon.svg","icon-192.png","icon-512.png","manifest.webmanifest","README_KO.md","README_EN.md"]) assert(existsSync(at(file)),"missing "+file);
assert(html.includes('id="tabLab"') && html.includes('id="labOutcome"'));
assert(read("service-worker.js").includes("review-lab.js"));
assert(read("review-lab.js").includes("7913d78024ce98de3a4c3409e92e6d59adcf455a"));
assert(read("review-lab.js").includes("SYNTHETIC_NEGATIVE") && read("review-lab.js").includes("NO_MAIN_RESULT"));
assert(!read("review-lab.js").includes("fetch("),"review must not call arbitrary network services");
assert(!read("review-lab.js").includes("P_CHRONICLE"),"no private archive reference");
for(const p of ["experiments/e007/README_EN.md","experiments/e007/README_KO.md","experiments/e008/README_EN.md","experiments/e008/README_KO.md","experiments/e009/RESULT_EN.md","experiments/e009/RESULT_KO.md"]){
  assert(existsSync(new URL("../"+p,root)),"missing provenance source "+p);
}

assert(html.includes('name="viewport"') && html.includes('id="issueForm"') && html.includes('id="axisGrid"'));
assert(manifest.display === "standalone" && manifest.icons.some((i)=>i.sizes==="192x192") && manifest.icons.some((i)=>i.sizes==="512x512"));
assert(js.includes("42.35%") && js.includes("NO RESULT / E008") && js.includes("PUBLIC_REVIEW_PACKET_KO.md"));
assert(!js.includes("github_pat_") && !js.includes("P_CHRONICLE"));
for(const icon of ["icon-192.png","icon-512.png"]){const b=readFileSync(at(icon));assert(b.subarray(0,8).equals(Buffer.from([137,80,78,71,13,10,26,10])),"invalid PNG");}
console.log("PI mobile v0.2 source-boundary checks: PASS");