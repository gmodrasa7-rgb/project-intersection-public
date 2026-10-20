/* Offline app shell only; external GitHub research pages require network. */
const CACHE="pi-mobile-v0.1.0";
const SHELL=["./","./index.html","./styles.css","./app.js","./manifest.webmanifest","./icon.svg","./icon-192.png","./icon-512.png"];
self.addEventListener("install",(event)=>{event.waitUntil(caches.open(CACHE).then((c)=>c.addAll(SHELL)).then(()=>self.skipWaiting()));});
self.addEventListener("activate",(event)=>{event.waitUntil(caches.keys().then((keys)=>Promise.all(keys.filter((x)=>x.startsWith("pi-mobile-")&&x!==CACHE).map((x)=>caches.delete(x)))).then(()=>self.clients.claim()));});
self.addEventListener("fetch",(event)=>{
  const req=event.request, url=new URL(req.url);
  if(req.method!=="GET"||url.origin!==self.location.origin)return;
  event.respondWith(fetch(req).then((res)=>{if(res.ok&&url.pathname.startsWith(new URL("./",self.registration.scope).pathname)){const copy=res.clone();caches.open(CACHE).then((c)=>c.put(req,copy)).catch(()=>{});}return res;}).catch(()=>caches.match(req).then((res)=>res||caches.match("./index.html"))));
});