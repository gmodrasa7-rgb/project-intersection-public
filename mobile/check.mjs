import assert from "node:assert/strict";
import { readFileSync, existsSync } from "node:fs";
const root = new URL("./", import.meta.url);
const at = (name) => new URL(name, root);
const read = (name) => readFileSync(at(name),"utf8");
const html = read("index.html"), js = read("app.js"), manifest=JSON.parse(read("manifest.webmanifest"));
for (const file of ["index.html","app.js","styles.css","service-worker.js","icon.svg","icon-192.png","icon-512.png","manifest.webmanifest","README_KO.md","README_EN.md"]) assert(existsSync(at(file)),"missing "+file);
assert(html.includes('name="viewport"') && html.includes('id="issueForm"') && html.includes('id="axisGrid"'));
assert(manifest.display === "standalone" && manifest.icons.some((i)=>i.sizes==="192x192") && manifest.icons.some((i)=>i.sizes==="512x512"));
assert(js.includes("42.35%") && js.includes("NO RESULT / E008") && js.includes("PUBLIC_REVIEW_PACKET_KO.md"));
assert(!js.includes("github_pat_") && !js.includes("P_CHRONICLE"));
for(const icon of ["icon-192.png","icon-512.png"]){const b=readFileSync(at(icon));assert(b.subarray(0,8).equals(Buffer.from([137,80,78,71,13,10,26,10])),"invalid PNG");}
console.log("PI mobile checks: PASS");