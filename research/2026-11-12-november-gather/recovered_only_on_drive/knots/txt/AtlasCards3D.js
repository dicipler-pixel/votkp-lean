
/*=====*/

/* SCRIPT: mixer3d_parts_v1
   3D Mixer Parts v1 — Jeromie Beasley — 27 Oct 2026
   The shared, hard-to-get-right 3D parts taken from the Colour Leader Engine:
   stage (three.js scene, dark void, orbit drag / pinch / wheel, auto-turn, resize, panel offset),
   glow particles, fading trails, lines, orbs, terrain surfaces, floating labels,
   colour science (spectrum to colour), and the instrument panel (feed, eyes in film order,
   Eye / Film / Clean / PNG).
   This is NOT a mixer. Each paper's mixer is written for that paper on top of these parts:
   its eyes are its own 3D scenes built from its own physics.
   Needs three.js r158 loaded first. */
(function(){
"use strict";
const T = window.THREE;

/* ---------- colour science (CIE 1931 fit, equal-energy white balanced) ---------- */
const g = (l,m,s1,s2) => { const t = (l-m)/(l<m?s1:s2); return Math.exp(-0.5*t*t); };
const WL = []; for(let l=400;l<=700;l+=10) WL.push(l);
const CMF = WL.map(l => [1.056*g(l,599.8,37.9,31.0)+0.362*g(l,442.0,16.0,26.7)-0.065*g(l,501.1,20.4,26.2),
                        0.821*g(l,568.8,46.9,40.5)+0.286*g(l,530.9,16.3,31.1),
                        1.217*g(l,437.0,11.8,36.0)+0.681*g(l,459.0,26.0,13.8)]);
const X2R = [[3.2406,-1.5372,-0.4986],[-0.9689,1.8758,0.0415],[0.0557,-0.2040,1.0570]];
const xyz2lin = v => X2R.map(r => r[0]*v[0]+r[1]*v[1]+r[2]*v[2]);
const specToXYZ = E => { const o=[0,0,0]; for(let i=0;i<WL.length;i++){ o[0]+=CMF[i][0]*E[i]; o[1]+=CMF[i][1]*E[i]; o[2]+=CMF[i][2]*E[i]; } return o; };
const WHITE = xyz2lin(specToXYZ(WL.map(()=>1)));
const colour = {
  WL, CMF,
  spec: E => xyz2lin(specToXYZ(E)).map((v,i) => v/WHITE[i]),
  enc: c => { c = Math.max(0,Math.min(1,c)); return c<=0.0031308 ? 12.92*c : 1.055*Math.pow(c,1/2.4)-0.055; },
  norm: v => { const m = Math.max(v[0],v[1],v[2],1e-9); return v.map(x => Math.max(0,x)/m); },
  lum: v => 0.2126*v[0]+0.7152*v[1]+0.0722*v[2]
};
colour.hex = v => '#'+v.map(x => Math.round(colour.enc(x)*255).toString(16).padStart(2,'0')).join('');
colour.wave = l => colour.norm(xyz2lin(CMF[WL.indexOf(l)]).map((v,i)=>v/WHITE[i]));
colour.ramp = t => { t = Math.max(0,Math.min(1,t)); const s = [[0.12,0.35,1.0],[0.25,0.85,1.0],[0.45,1.0,0.55],[1.0,0.78,0.25],[1.0,0.35,0.45]];
  const x = t*(s.length-1), i = Math.min(s.length-2, Math.floor(x)), f = x-i; return [0,1,2].map(k => s[i][k]*(1-f)+s[i+1][k]*f); };
const tcol = v => { const c = new T.Color(); c.setRGB(Math.max(0,v[0]),Math.max(0,v[1]),Math.max(0,v[2]), T.LinearSRGBColorSpace); return c; };

/* ---------- glow parts ---------- */
const sprite = (() => { const c = document.createElement('canvas'); c.width = c.height = 64; const x = c.getContext('2d');
  const gr = x.createRadialGradient(32,32,0,32,32,32); gr.addColorStop(0,'rgba(255,255,255,1)'); gr.addColorStop(0.25,'rgba(255,255,255,.65)'); gr.addColorStop(1,'rgba(255,255,255,0)');
  x.fillStyle = gr; x.fillRect(0,0,64,64); return new T.CanvasTexture(c); })();
const glow = size => new T.PointsMaterial({size, map:sprite, transparent:true, depthWrite:false, blending:T.AdditiveBlending, vertexColors:true, sizeAttenuation:true});
function points(n, size){ const geo = new T.BufferGeometry(); geo.setAttribute('position', new T.BufferAttribute(new Float32Array(n*3),3)); geo.setAttribute('color', new T.BufferAttribute(new Float32Array(n*3),3)); const p = new T.Points(geo, glow(size)); p.frustumCulled = false; return p; }
function setPt(p, i, P, c){ const a = p.geometry.attributes; a.position.setXYZ(i, P.x, P.y, P.z); if(c) a.color.setXYZ(i, c[0], c[1], c[2]); }
function flush(p){ const a = p.geometry.attributes; a.position.needsUpdate = true; a.color.needsUpdate = true; }
function line(pts, color, opacity){ const geo = new T.BufferGeometry().setFromPoints(pts.length ? pts : [new T.Vector3(), new T.Vector3()]); const l = new T.Line(geo, new T.LineBasicMaterial({color, transparent:true, opacity:opacity==null?1:opacity})); l.frustumCulled = false; return l; }
function setLine(l, pts){ l.geometry.dispose(); l.geometry = new T.BufferGeometry().setFromPoints(pts); }
function orb(r, color){ return new T.Mesh(new T.SphereGeometry(r, 28, 20), new T.MeshStandardMaterial({color, emissive:color, emissiveIntensity:0.6, roughness:0.4})); }
function paintOrb(o, v, glowAmt){ const c = tcol(v); o.material.color = c; o.material.emissive = c; if(glowAmt != null) o.material.emissiveIntensity = glowAmt; }
function shell(r, color, opacity){ return new T.Mesh(new T.SphereGeometry(r, 36, 24), new T.MeshBasicMaterial({color, transparent:true, opacity, depthWrite:false, blending:T.AdditiveBlending})); }
function box(w, h, d, color, opacity){ return new T.Mesh(new T.BoxGeometry(w,h,d), new T.MeshStandardMaterial({color, transparent:true, opacity:opacity==null?0.35:opacity, roughness:0.15, depthWrite:false})); }
function grid(size, n, color, opacity){ const pts = []; const h = size/2; for(let i=0;i<=n;i++){ const t = -h + size*i/n; pts.push(new T.Vector3(t,0,-h), new T.Vector3(t,0,h), new T.Vector3(-h,0,t), new T.Vector3(h,0,t)); }
  return new T.LineSegments(new T.BufferGeometry().setFromPoints(pts), new T.LineBasicMaterial({color, transparent:true, opacity})); }

/* fading trail: a ring buffer of n glowing points */
function trail(n, size){ const p = points(n, size); p.userData = {n, i:0, filled:0}; return p; }
function pushTrail(p, P, c){ const u = p.userData, a = p.geometry.attributes;
  a.position.setXYZ(u.i, P.x, P.y, P.z); u.i = (u.i+1) % u.n; u.filled = Math.min(u.n, u.filled+1);
  for(let k=0;k<u.n;k++){ const age = ((u.i - 1 - k) % u.n + u.n) % u.n; const f = k < u.filled ? Math.pow(1 - age/u.n, 2)*0.85 : 0; a.color.setXYZ(k, c[0]*f, c[1]*f, c[2]*f); }
  a.position.needsUpdate = a.color.needsUpdate = true; }
function clearTrail(p){ p.userData.i = 0; p.userData.filled = 0; const a = p.geometry.attributes; a.color.array.fill(0); a.color.needsUpdate = true; }

/* terrain surface over a grid: H[a][b] heights, C[a][b] rgb; spans x in [-sx,sx], z in [-sz,sz] */
function surface(N, M, sx, sz){ const geo = new T.PlaneGeometry(2*sx, 2*sz, N-1, M-1); geo.rotateX(-Math.PI/2);
  geo.setAttribute('color', new T.BufferAttribute(new Float32Array(N*M*3),3));
  const mesh = new T.Mesh(geo, new T.MeshStandardMaterial({vertexColors:true, roughness:0.55, metalness:0.05, side:T.DoubleSide, transparent:true, opacity:0.92}));
  const wire = new T.LineSegments(new T.WireframeGeometry(geo), new T.LineBasicMaterial({color:0x63d3ff, transparent:true, opacity:0.08}));
  const grp = new T.Group(); grp.add(mesh); grp.add(wire); grp.userData = {N, M, sx, sz, geo, wire}; return grp; }
function setSurface(s, H, C){ const u = s.userData, pos = u.geo.attributes.position, col = u.geo.attributes.color;
  for(let b=0;b<u.M;b++) for(let a=0;a<u.N;a++){ const i = b*u.N + a; pos.setY(i, H[a][u.M-1-b]); const c = C[a][u.M-1-b]; col.setXYZ(i, c[0], c[1], c[2]); }
  pos.needsUpdate = col.needsUpdate = true; u.geo.computeVertexNormals();
  u.wire.geometry.dispose(); u.wire.geometry = new T.WireframeGeometry(u.geo); }

/* floating text label (always faces the camera) */
function label(text, color, scale){ const c = document.createElement('canvas'), x = c.getContext('2d'), f = 44;
  x.font = `500 ${f}px "Inter Tight",system-ui,sans-serif`; const w = Math.ceil(x.measureText(text).width) + 24; c.width = w; c.height = f + 20;
  x.font = `500 ${f}px "Inter Tight",system-ui,sans-serif`; x.fillStyle = color || '#b8c6d6'; x.textBaseline = 'middle'; x.fillText(text, 12, c.height/2);
  const tex = new T.CanvasTexture(c); tex.colorSpace = T.SRGBColorSpace;
  const s = new T.Sprite(new T.SpriteMaterial({map:tex, transparent:true, depthWrite:false, depthTest:false}));
  const k = 0.55*(scale || 0.32) / f; s.scale.set(w*k, c.height*k, 1); s.renderOrder = 10; return s; }

/* ---------- stage ---------- */
function stage(canvas){
  const renderer = new T.WebGLRenderer({canvas, antialias:true, preserveDrawingBuffer:true});
  renderer.setPixelRatio(Math.min(2, window.devicePixelRatio||1));
  const scene = new T.Scene(); scene.background = new T.Color(0x05070b);
  const camera = new T.PerspectiveCamera(45, 1, 0.05, 200);
  const world = new T.Group(); scene.add(world);
  scene.add(new T.AmbientLight(0x8899aa, 0.6));
  const key = new T.DirectionalLight(0xffffff, 1.0); key.position.set(3,5,4); scene.add(key);
  const V = { yaw:0.75, pitch:0.42, dist:7.2, ty:0.4, auto:true, panel:true };
  function size(){ const w = window.innerWidth, h = window.innerHeight; renderer.setSize(w,h,false); camera.aspect = w/h; camera.updateProjectionMatrix();
    const mobile = w < 640; if(V.panel) camera.setViewOffset(w, h, mobile ? 0 : -Math.min(180, w*0.14), mobile ? h*0.2 : 0, w, h); else camera.clearViewOffset(); }
  window.addEventListener('resize', size);
  const ptrs = new Map(); let pinch0 = 0, dist0 = V.dist;
  canvas.addEventListener('pointerdown', e => { canvas.setPointerCapture(e.pointerId); ptrs.set(e.pointerId, {x:e.clientX, y:e.clientY}); V.auto = false;
    if(ptrs.size === 2){ const [a,b] = [...ptrs.values()]; pinch0 = Math.hypot(a.x-b.x, a.y-b.y); dist0 = V.dist; } });
  canvas.addEventListener('pointermove', e => { if(!ptrs.has(e.pointerId)) return; const p = ptrs.get(e.pointerId);
    if(ptrs.size === 1){ V.yaw -= (e.clientX - p.x)*0.006; V.pitch = Math.max(-1.3, Math.min(1.3, V.pitch + (e.clientY - p.y)*0.006)); }
    p.x = e.clientX; p.y = e.clientY;
    if(ptrs.size === 2){ const [a,b] = [...ptrs.values()]; const d = Math.hypot(a.x-b.x, a.y-b.y); if(pinch0) V.dist = Math.max(3, Math.min(20, dist0*pinch0/d)); } });
  ['pointerup','pointercancel'].forEach(t => canvas.addEventListener(t, e => { ptrs.delete(e.pointerId); if(ptrs.size < 2) pinch0 = 0; }));
  canvas.addEventListener('wheel', e => { e.preventDefault(); V.dist = Math.max(3, Math.min(20, V.dist*Math.exp(e.deltaY*0.001))); }, {passive:false});
  const still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let last = performance.now(), tick = null;
  function frame(now){
    const dt = Math.min(0.05, (now - last)/1000); last = now;
    if(V.auto && !still) V.yaw += dt*0.08;
    const D = V.dist*(window.innerWidth < 640 ? 1.5 : 1);
    camera.position.set(D*Math.cos(V.pitch)*Math.sin(V.yaw), V.ty + D*Math.sin(V.pitch), D*Math.cos(V.pitch)*Math.cos(V.yaw));
    camera.lookAt(0, V.ty, 0);
    if(tick) tick(still ? 0.016 : dt, now/1000);
    renderer.render(scene, camera);
    requestAnimationFrame(frame);
  }
  size();
  return { T, scene, camera, renderer, world, view:V, resize:size,
    onFrame(fn){ tick = fn; requestAnimationFrame(frame); },
    setView(v){ V.yaw = v[0]; V.pitch = v[1]; V.dist = v[2]; V.ty = v[3] == null ? 0.4 : v[3]; } };
}

/* ---------- instrument panel CSS ---------- */
const CSS = `
:root{--void:#05070b;--panel:rgba(9,13,20,.86);--edge:#1f2a38;--ink:#dfe7ef;--dim:#8a9aab;--faint:#55657a;--gold:#f2c14e;--cyan:#63d3ff;--rose:#ff6fae;
--head:"Chakra Petch","Segoe UI",system-ui,sans-serif;--body:"Inter Tight",system-ui,-apple-system,sans-serif;--mono:"JetBrains Mono",ui-monospace,Menlo,Consolas,monospace;color-scheme:dark}
html,body{height:100%}body{margin:0;background:var(--void);color:var(--ink);font-family:var(--body);font-size:13.5px;overflow:hidden}
#stage{position:fixed;inset:0;touch-action:none;cursor:grab}#stage:active{cursor:grabbing}
.panel{position:fixed;top:calc(12px + env(safe-area-inset-top,0px));left:max(12px,env(safe-area-inset-left,0px));width:350px;max-height:calc(100% - 24px - env(safe-area-inset-top,0px) - env(safe-area-inset-bottom,0px));overflow:auto;background:var(--panel);border:1px solid var(--edge);border-radius:8px;padding:14px 14px 12px;backdrop-filter:blur(6px);display:grid;gap:10px}
@media (max-width:640px){.panel{top:auto;bottom:calc(8px + env(safe-area-inset-bottom,0px));left:max(8px,env(safe-area-inset-left,0px));right:max(8px,env(safe-area-inset-right,0px));width:auto;max-height:46%}}
body.clean .panel{display:none}
.cleanexit{position:fixed;right:12px;bottom:12px;display:none;font-size:11px;opacity:.35}body.clean .cleanexit{display:block}
h1{font-family:var(--head);font-weight:600;font-size:16px;letter-spacing:.08em;text-transform:uppercase;margin:0}
.by{font-family:var(--mono);font-size:10.5px;color:var(--faint);letter-spacing:.06em;margin-top:2px}
button{font:inherit;color:var(--ink);background:#101824;border:1px solid var(--edge);border-radius:5px;padding:6px 8px;cursor:pointer}
button:hover{border-color:var(--cyan)}button:focus-visible,input:focus-visible,summary:focus-visible{outline:2px solid var(--cyan);outline-offset:2px}
.eyes{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:5px}
.eyes button{font-family:var(--head);font-size:11.5px;letter-spacing:.03em;line-height:1.25;text-align:left;display:flex;gap:6px;align-items:baseline}
.eyes button .n{font-family:var(--mono);color:var(--faint);font-size:10.5px}
.eyes button.on{border-color:var(--gold);color:var(--gold)}.eyes button.on .n{color:var(--gold)}
.tag{font-family:var(--mono);font-size:10.5px;color:var(--faint);letter-spacing:.05em}.tag b{color:var(--cyan);font-weight:400}
.eq{font-family:var(--mono);font-size:12px;color:var(--gold);line-height:1.55;white-space:pre-wrap}
.what{color:var(--dim);line-height:1.45;margin:0}
.ctl{display:grid;gap:7px}
.ctl label{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:2px 8px;font-size:12px;color:var(--dim)}
.ctl label output{font-family:var(--mono);color:var(--ink)}
.ctl input[type=range]{grid-column:1/-1;width:100%;accent-color:var(--cyan)}
.row{display:flex;flex-wrap:wrap;gap:6px}.row button{font-size:12px;padding:4px 9px}
.row button[aria-pressed=true]{border-color:var(--gold);color:var(--gold)}
.read{font-family:var(--mono);font-size:11.5px;line-height:1.6;color:var(--dim);border-top:1px solid var(--edge);padding-top:8px;font-variant-numeric:tabular-nums}
.read div{display:flex;justify-content:space-between;gap:10px}.read b{color:var(--ink);font-weight:400;text-align:right}
.filmbar{height:3px;background:var(--edge);border-radius:2px;overflow:hidden}.filmbar i{display:block;height:100%;width:0;background:var(--gold)}
.hint{font-size:11px;color:var(--faint)}`;

/* ---------- mixer runner: feed operator + eyes (each its own 3D scene) + film ---------- */
function run(MIXER){
  const st = document.createElement('style'); st.textContent = CSS; document.head.append(st);
  document.body.insertAdjacentHTML('beforeend', `
<canvas id="stage" aria-label="3D view; drag to turn, scroll or pinch to zoom"></canvas>
<div class="panel" id="panel">
  <div><h1>${MIXER.title}</h1><div class="by">${MIXER.byline}</div></div>
  <div class="eyes" id="eyes" role="tablist"></div>
  <div class="tag" id="tag"></div>
  <div class="eq" id="eq"></div>
  <p class="what" id="what"></p>
  <div class="ctl" id="ctl"></div>
  <div class="read" id="read"></div>
  <div class="row"><button id="m_eye" aria-pressed="true">Eye</button><button id="m_film" aria-pressed="false">Film</button><button id="m_clean">Clean view</button><button id="m_png">Frame PNG</button></div>
  <div class="ctl"><label>Seconds per eye (film) <output id="o_sec">10</output><input id="sec" type="range" min="4" max="30" step="1" value="10"></label></div>
  <div class="filmbar"><i id="fb"></i></div>
  <div class="hint">Drag to turn · scroll or pinch to zoom · ${MIXER.note || ''}</div>
</div>
<button class="cleanexit" id="m_back">show panel</button>`);
  const $ = id => document.getElementById(id);
  const S3 = stage($('stage'));
  const P = {}; MIXER.feed.params.forEach(q => P[q.id] = q.value);
  let S = MIXER.feed.build(P);
  const byId = {}; MIXER.eyes.forEach(e => { byId[e.id] = e; e.group = new T.Group(); e.make(e.group, S3); });
  let cur = null, mode = 'eye', t0 = 0, fi = 0, tEye = 0;
  function controls(e){
    const used = (e.uses || []).map(id => MIXER.feed.params.find(q => q.id === id));
    $('ctl').innerHTML = used.map(q => `<label>${q.label} <output id="o_${q.id}">${P[q.id]}</output><input id="p_${q.id}" type="range" min="${q.min}" max="${q.max}" step="${q.step}" value="${P[q.id]}"></label>`).join('') + (e.extra ? e.extra() : '');
    used.forEach(q => $('p_'+q.id).addEventListener('input', ev => { P[q.id] = +ev.target.value; $('o_'+q.id).textContent = P[q.id]; S = MIXER.feed.build(P); if(cur.change) cur.change(S); }));
    if(e.bind) e.bind(S, $);
  }
  function show(id){
    if(cur) S3.world.remove(cur.group);
    cur = byId[id]; S3.world.add(cur.group); tEye = 0;
    document.querySelectorAll('#eyes button').forEach(b => b.classList.toggle('on', b.dataset.id === id));
    $('tag').innerHTML = `${cur.section} · <b>${cur.grade}</b>`;
    $('eq').textContent = cur.eq; $('what').textContent = cur.text;
    controls(cur); S3.setView(cur.view || [0.75,0.42,7.2,0.4]);
    if(cur.enter) cur.enter(S);
  }
  MIXER.film.forEach((id,i) => { const b = document.createElement('button'); b.dataset.id = id; b.setAttribute('role','tab');
    b.innerHTML = `<span class="n">${i+1}</span><span>${byId[id].title}</span>`; b.addEventListener('click', () => { if(mode==='film') setMode('eye'); show(id); }); $('eyes').append(b); });
  function setMode(m){ mode = m; $('m_eye').setAttribute('aria-pressed', m==='eye'); $('m_film').setAttribute('aria-pressed', m==='film'); t0 = performance.now()/1000; if(m==='film'){ fi = 0; show(MIXER.film[0]); } }
  $('m_eye').addEventListener('click', () => setMode('eye'));
  $('m_film').addEventListener('click', () => setMode('film'));
  $('sec').addEventListener('input', e => $('o_sec').textContent = e.target.value);
  const clean = on => { document.body.classList.toggle('clean', on); S3.view.panel = !on; S3.resize(); };
  $('m_clean').addEventListener('click', () => clean(true)); $('m_back').addEventListener('click', () => clean(false));
  document.addEventListener('keydown', e => { if(e.key === 'Escape') clean(false); });
  $('m_png').addEventListener('click', () => { const a = document.createElement('a'); a.href = $('stage').toDataURL('image/png'); a.download = (MIXER.title + ' ' + cur.id).replace(/\s+/g,'_') + '.png'; a.click(); });
  let readT = 0;
  S3.onFrame((dt, now) => {
    tEye += dt;
    if(mode === 'film'){ const sec = +$('sec').value, t = now - t0; if(t > sec){ fi = (fi+1) % MIXER.film.length; t0 = now; show(MIXER.film[fi]); } $('fb').style.width = (100*(fi + Math.min(1,(now-t0)/sec))/MIXER.film.length) + '%'; }
    else $('fb').style.width = '0%';
    const rows = cur.step(dt, S, tEye);
    readT += dt; if(rows && readT > 0.12){ readT = 0; $('read').innerHTML = rows.map(r => `<div><span>${r[0]}</span><b>${r[1]}</b></div>`).join(''); }
  });
  show(MIXER.film[0]);
  window.MIXER_API = { show, setMode, clean, P, get S(){ return S; },
    set(id, v){ P[id] = v; S = MIXER.feed.build(P); const i = $('p_'+id); if(i){ i.value = v; $('o_'+id).textContent = v; } if(cur.change) cur.change(S); } };
}

window.Mixer3D = { T, colour, tcol, sprite, glow, points, setPt, flush, line, setLine, orb, paintOrb, shell, box, grid, trail, pushTrail, clearTrail, surface, setSurface, label, stage, run };
})();


/*=====*/

/* SCRIPT: ATLAS3D-CORE
   Computational core of the 3D atlas cards B204 to B213. Every readout on the page is computed here.
   Runs in the browser and in Node. */
(function(root){
"use strict";
/* ---------- small dense linear algebra (real) ---------- */
const eye = n => Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>+(i===j)));
const mm = (A,B) => A.map(r=>B[0].map((_,j)=>r.reduce((s,v,k)=>s+v*B[k][j],0)));
const mv = (A,x) => A.map(r=>r.reduce((s,v,k)=>s+v*x[k],0));
const dot = (a,b) => a.reduce((s,v,i)=>s+v*b[i],0);
function solve(A,b){ const n=A.length, M=A.map((r,i)=>[...r,b[i]]);
  for(let c=0;c<n;c++){ let p=c; for(let r=c+1;r<n;r++) if(Math.abs(M[r][c])>Math.abs(M[p][c])) p=r; [M[c],M[p]]=[M[p],M[c]];
    for(let r=0;r<n;r++) if(r!==c){ const f=M[r][c]/M[c][c]; for(let k=c;k<=n;k++) M[r][k]-=f*M[c][k]; } }
  return M.map((r,i)=>r[n]/r[i]); }
function rank(A,tol){ const M=A.map(r=>r.slice()); const m=M.length, n=M[0].length; let rk=0; tol=tol||1e-9;
  for(let c=0;c<n && rk<m;c++){ let p=rk; for(let r=rk+1;r<m;r++) if(Math.abs(M[r][c])>Math.abs(M[p][c])) p=r;
    if(Math.abs(M[p][c])<tol) continue; [M[rk],M[p]]=[M[p],M[rk]];
    for(let r=rk+1;r<m;r++){ const f=M[r][c]/M[rk][c]; for(let k=c;k<n;k++) M[r][k]-=f*M[rk][k]; } rk++; }
  return rk; }
function eigSym(A){ const n=A.length, a=A.map(r=>r.slice()), V=eye(n);
  for(let sweep=0;sweep<100;sweep++){ let off=0; for(let i=0;i<n;i++) for(let j=i+1;j<n;j++) off+=a[i][j]*a[i][j]; if(off<1e-26) break;
    for(let p=0;p<n;p++) for(let q=p+1;q<n;q++){ if(Math.abs(a[p][q])<1e-300) continue;
      const th=(a[q][q]-a[p][p])/(2*a[p][q]), t=Math.sign(th||1)/(Math.abs(th)+Math.sqrt(th*th+1)), c=1/Math.sqrt(t*t+1), s=t*c;
      for(let k=0;k<n;k++){ const akp=a[k][p], akq=a[k][q]; a[k][p]=c*akp-s*akq; a[k][q]=s*akp+c*akq; }
      for(let k=0;k<n;k++){ const apk=a[p][k], aqk=a[q][k]; a[p][k]=c*apk-s*aqk; a[q][k]=s*apk+c*aqk; }
      for(let k=0;k<n;k++){ const vkp=V[k][p], vkq=V[k][q]; V[k][p]=c*vkp-s*vkq; V[k][q]=s*vkp+c*vkq; } } }
  const vals=a.map((r,i)=>r[i]); const ord=vals.map((_,i)=>i).sort((x,y)=>vals[x]-vals[y]);
  return {values:ord.map(i=>vals[i]), vectors:ord.map(i=>V.map(r=>r[i]))}; }
function rng(seed){ let s=seed>>>0||1; return ()=>{ s^=s<<13; s>>>=0; s^=s>>>17; s^=s<<5; s>>>=0; return s/4294967296; }; }
function gauss(r){ let u=0,v=0; while(!u) u=r(); v=r(); return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v); }

/* ---------- B204, B205: the Rice-Mele chain on the infinite line, half filled ---------- */
const NK=2048;
function rmCorr(L,t1,t2,v){ const tab={};  // C[i][j], site 2n = sublattice A of cell n
  const P00=[],P11=[],P01r=[],P01i=[],ks=[];
  for(let q=0;q<NK;q++){ const k=-Math.PI+(q+.5)/NK*2*Math.PI, E=Math.sqrt(t1*t1+t2*t2+2*t1*t2*Math.cos(k)+v*v);
    ks.push(k); P00.push(.5*(1-v/E)); P11.push(.5*(1+v/E)); P01r.push(.5*(t1+t2*Math.cos(k))/E); P01i.push(-.5*t2*Math.sin(k)/E); }
  // P01 = -h12/(2E) with h12 = -(t1 + t2 e^{-ik}) -> (t1 + t2 cos k - i t2 sin k)/(2E)
  function el(ai,aj,dc){ let s=0; for(let q=0;q<NK;q++){ const c=Math.cos(ks[q]*dc), sn=Math.sin(ks[q]*dc);
      if(ai===aj) s+=(ai?P11[q]:P00[q])*c;
      else if(ai===0) s+=P01r[q]*c-P01i[q]*sn;           // Re[P01 e^{ik dc}]
      else s+=P01r[q]*c+P01i[q]*sn; }                       // P10 = conj P01
    return s/NK; }
  const C=Array.from({length:L},()=>new Array(L).fill(0));
  for(let i=0;i<L;i++) for(let j=0;j<L;j++){ const ci=Math.floor(i/2), cj=Math.floor(j/2), key=(i%2)+','+(j%2)+','+(ci-cj);
    if(tab[key]==null) tab[key]=el(i%2,j%2,ci-cj); C[i][j]=tab[key]; }
  return C; }
function residuals(C){ const n=C.length, CB=C.slice(0,n-1).map(r=>r.slice(0,n-1)), b=C[n-1].slice(0,n-1), x=C[n-1][n-1];
  const IB=CB.map((r,i)=>r.map((v,j)=>(i===j?1:0)-v));
  const s1=x-dot(b,solve(CB,b)), s0=1-x-dot(b,solve(IB,b)); return {s0,s1}; }
function offsetLogdet(C){ const ev=eigSym(C).values; return ev.reduce((s,nu)=>s+Math.log((1-nu)/nu),0); }
const rmK=(t1,t2,v)=>{ const a=Math.sqrt((t1-t2)**2+v*v), b=Math.sqrt((t1+t2)**2+v*v); return Math.abs(v)/Math.sqrt(a*b); };
/* Kitaev chain block: BdG generalized correlation [[C,F],[F^T,1-C^T]], topological for |mu|<2t */
function kitaevBlock(L,mu,t,D){ const G=r=>{ let s=0; for(let q=0;q<NK;q++){ const k=-Math.PI+(q+.5)/NK*2*Math.PI, xi=-mu-2*t*Math.cos(k), dk=2*D*Math.sin(k), E=Math.hypot(xi,dk); s+=.5*(1-xi/E)*Math.cos(k*r);} return s/NK; };
  const F=r=>{ let s=0; for(let q=0;q<NK;q++){ const k=-Math.PI+(q+.5)/NK*2*Math.PI, xi=-mu-2*t*Math.cos(k), dk=2*D*Math.sin(k), E=Math.hypot(xi,dk); s+=.5*(dk/E)*Math.sin(k*r);} return s/NK; };
  const g={},f={}; for(let r=-L;r<=L;r++){ g[r]=G(r); f[r]=F(r); }
  const M=Array.from({length:2*L},()=>new Array(2*L).fill(0));
  for(let i=0;i<L;i++) for(let j=0;j<L;j++){ M[i][j]=g[i-j]; M[i][L+j]=f[i-j]; M[L+i][j]=f[j-i]; M[L+i][L+j]=(i===j?1:0)-g[j-i]; }
  return eigSym(M).values; }

/* ---------- B206: three overlaps of two k-planes, from the principal-angle squares c_a ---------- */
function overlaps(c){ const k=c.length, rho=c.reduce((s,x)=>s+x,0)/k, F=(c.reduce((s,x)=>s+Math.sqrt(x),0)/k)**2, D=c.reduce((s,x)=>s*x,1);
  return {rho,F,D,Em:2*k*(1-rho),Ep:2*k*(1+rho),varSqrt:c.reduce((s,x)=>s+x,0)/k-(c.reduce((s,x)=>s+Math.sqrt(x),0)/k)**2}; }

/* ---------- B207: Schwarzschild in isotropic radius rho, a = M/2 ---------- */
function schw(a,rho){ const G=a/rho, V=(1-G)/(1+G), psi=1+G; return {G,V,psi,Em:(1-G)**2,Ep:(1+G)**2,wPlus:((1+V)/2)**4*psi**4,wMinus:((1-V)/2)**4*psi**4,R:rho*psi*psi}; }

/* ---------- B208: predictive quotient ---------- */
function obsMatrix(L,R,k){ const rows=[]; let M=eye(L.length); for(let j=0;j<k;j++){ R.forEach(r=>rows.push(M[0].map((_,c)=>r.reduce((s,v,q)=>s+v*M[q][c],0)))); M=mm(M,L); } return rows; }
function readingsNeeded(L,R){ const d=L.length, full=rank(obsMatrix(L,R,d)); for(let k=1;k<=d;k++) if(rank(obsMatrix(L,R,k))===full) return {k,full}; return {k:d,full}; }

/* ---------- B210: the gap ladder ---------- */
function ladder(E,K){ const n=E.length, S={}; for(const k of [-2,-1,0,1,2]){ let s=0; for(let i=0;i<n;i++) for(let j=0;j<n;j++) if(i!==j){ const d=Math.abs(E[i]-E[j]); s+=K[i][j]*K[i][j]*Math.pow(d,k); } S[k]=s; }
  let comm=0; for(let i=0;i<n;i++) for(let j=0;j<n;j++) comm+=((E[i]-E[j])*K[i][j])**2; return {S,comm}; }

/* ---------- B211: scalar cut on the Bloch sphere; projector P = psi psi^dag in C^2, accessible amplitude a = cos(theta/2) ---------- */
function cutState(th,ph){ return {a:[Math.cos(th/2),0], b:[Math.sin(th/2)*Math.cos(ph),Math.sin(th/2)*Math.sin(ph)]}; }
function cutSpeed(th,alpha){ // direction alpha: 0 along the meridian (changes c), pi/2 along the latitude (phase only)
  const c=Math.cos(th/2)**2, S=1/(c*(1-c)), thd=Math.cos(alpha), phd=Math.sin(alpha);
  const cdot=-.5*Math.sin(th)*thd, taudot=-cdot/(c*(1-c));
  const g=.25*(thd*thd+Math.sin(th)**2*phd*phd); // g = 1/2 ||Pdot||^2 = |ndot|^2/4 for a rank-one projector with Bloch vector n
  const b2=c*(1-c), Imbbd=-b2*phd; // b = P_12 = a conj(b_hidden); Im(conj(b) bdot) at the current point
  return {c,S,taudot,g,ratio:taudot*taudot/(4*g*S),tau:Math.log((1-c)/c),gap:4*g*S-taudot*taudot,gapFormula:4*Imbbd*Imbbd/(b2*b2)}; }

/* ---------- B212: amount and composition ---------- */
function fisherSplit(x,a,dx){ const I=dot(a,x), p=x.map((xi,i)=>a[i]*xi/I), dI=dot(a,dx), dp=dx.map((d,i)=>(a[i]*d-p[i]*dI)/I);
  const lhs=x.reduce((s,xi,i)=>s+a[i]*dx[i]*dx[i]/xi,0)/I, scale=(dI/I)**2, comp=dp.reduce((s,d,i)=>s+d*d/p[i],0); return {I,p,lhs,scale,comp,rhs:scale+comp}; }

/* ---------- B213: orbit sums ---------- */
function orbitArea(c,n,N){ N=N||4000; let s=0; for(let q=0;q<N;q++){ const t=q/N*2*Math.PI; let zr=0,zi=0,dr=0,di=0;
    for(let j=0;j<c.length;j++){ const ph=n[j]*t+c[j][1], r=c[j][0]; zr+=r*Math.cos(ph); zi+=r*Math.sin(ph); dr+=-n[j]*r*Math.sin(ph); di+=n[j]*r*Math.cos(ph); }
    s+=zr*di-zi*dr; } return .5*s/N*2*Math.PI; }
function orbitBooks(c,n){ let Ep=0,Em=0; for(let j=0;j<c.length;j++){ const w=c[j][0]*c[j][0]*n[j]; if(n[j]>0) Ep+=w; else Em+=-w; } return {Ep,Em,area:Math.PI*(Ep-Em),activity:Ep+Em}; }

root.ATLAS3D={eye,mm,mv,dot,solve,rank,eigSym,rng,gauss,rmCorr,residuals,offsetLogdet,rmK,kitaevBlock,overlaps,schw,obsMatrix,readingsNeeded,ladder,cutState,cutSpeed,fisherSplit,orbitArea,orbitBooks};
})(typeof window!=='undefined'?window:globalThis);


/*=====*/

/* SCRIPT: ATLAS3D-APP
   Atlas Cards in 3D — bridges B204 to B213 of the Operator-First Atlas (Jeromie Beasley).
   Built on 3D Mixer Parts v1 (Mixer3D). One WebGL context, one scissored viewport per card.
   Every readout is recomputed live by ATLAS3D (core) and set beside the card's own number. */
(function(){
"use strict";
const M=window.Mixer3D, T=M.T, A=window.ATLAS3D, $=id=>document.getElementById(id);
const V3=(x,y,z)=>new T.Vector3(x,y,z);
const still=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const HEX={gold:0xf2c14e,cyan:0x63d3ff,rose:0xff6fae,violet:0xb48cff,green:0x63ffb0,grey:0x3a4a5e,ink:0xdfe7ef,faint:0x55657a,red:0xff6b6b,coral:0xff8a5c};
const RGB=h=>[((h>>16)&255)/255,((h>>8)&255)/255,(h&255)/255];
const f=(x,d)=>(x==null||Number.isNaN(x))?'—':(+x).toFixed(d==null?4:d);
const sci=x=>(Math.abs(x)<1e-3&&x!==0)||Math.abs(x)>=1e5?(+x).toExponential(2):f(x,6);

/* ---------- geometry helpers on the parts ---------- */
function clear(g){ while(g.children.length){ const c=g.children.pop(); c.traverse(o=>{ if(o.geometry) o.geometry.dispose(); if(o.material){ if(o.material.map&&o.material.map!==M.sprite) o.material.map.dispose(); o.material.dispose(); } }); } }
function rod(p,q,color,r,op){ const d=q.clone().sub(p), L=d.length()||1e-6;
  const m=new T.Mesh(new T.CylinderGeometry(r,r,L,10,1,true),new T.MeshStandardMaterial({color,emissive:color,emissiveIntensity:.6,roughness:.45,transparent:op!=null,opacity:op==null?1:op,depthWrite:op==null}));
  m.position.copy(p).add(q).multiplyScalar(.5); m.quaternion.setFromUnitVectors(V3(0,1,0),d.normalize()); return m; }
function arrow(p,q,color,r){ const g=new T.Group(); const d=q.clone().sub(p), L=d.length(); if(L<1e-6) return g; const u=d.clone().normalize();
  const hl=Math.min(.22,L*.35), body=q.clone().sub(u.clone().multiplyScalar(hl)); g.add(rod(p,body,color,r||.025));
  const cone=new T.Mesh(new T.ConeGeometry((r||.025)*2.8,hl,16),new T.MeshStandardMaterial({color,emissive:color,emissiveIntensity:.7}));
  cone.position.copy(body).add(u.clone().multiplyScalar(hl/2)); cone.quaternion.setFromUnitVectors(V3(0,1,0),u); g.add(cone); return g; }
function col(x,z,h,color,w,op,y0){ const m=new T.Mesh(new T.BoxGeometry(w||.12,Math.max(1e-3,Math.abs(h)),w||.12),
  new T.MeshStandardMaterial({color,emissive:color,emissiveIntensity:.45,roughness:.4,transparent:op!=null,opacity:op==null?1:op})); m.position.set(x,(y0||0)+h/2,z); return m; }
function ring(r,color,op,y,n){ n=n||96; const pts=Array.from({length:n+1},(_,i)=>{ const a=i/n*2*Math.PI; return V3(r*Math.cos(a),y||0,r*Math.sin(a)); }); return M.line(pts,color,op==null?.5:op); }
function plane(w,d,color,op,y){ const m=new T.Mesh(new T.PlaneGeometry(w,d),new T.MeshBasicMaterial({color,transparent:true,opacity:op,side:T.DoubleSide,depthWrite:false})); m.rotation.x=-Math.PI/2; m.position.y=y||0; return m; }
function face(pts,color,op){ const g=new T.BufferGeometry().setFromPoints(pts); if(pts.length>3){ const idx=[]; for(let i=1;i<pts.length-1;i++) idx.push(0,i,i+1); g.setIndex(idx); }
  return new T.Mesh(g,new T.MeshBasicMaterial({color,transparent:true,opacity:op,side:T.DoubleSide,depthWrite:false})); }
function lab(G,text,pos,color,scale){ const l=M.label(text,color||'#93a3b5',1.7*(scale||.2)); l.position.copy(pos); G.add(l); return l; }
function relabel(G,old,text,color,scale){ const l=M.label(text,color,scale); l.position.copy(old.position); G.remove(old); old.material.map.dispose(); old.material.dispose(); G.add(l); return l; }
function arcPts(p,q,lift,n){ const mid=p.clone().add(q).multiplyScalar(.5); mid.y+=lift; return new T.QuadraticBezierCurve3(p,mid,q).getPoints(n||40); }
function curve(fn,n){ return Array.from({length:n},(_,i)=>fn(i/(n-1))); }

/* =====================================================================================================
   RENDERER — one WebGL context behind the page; each card is a scissored viewport
   ===================================================================================================== */
const R=new T.WebGLRenderer({canvas:$('gl'),antialias:true,preserveDrawingBuffer:true});
R.setPixelRatio(Math.min(2,window.devicePixelRatio||1)); R.setClearColor(0x05070b,1); R.autoClear=false;
const views=[];
function makeView(el,view,opts){ opts=opts||{};
  const scene=new T.Scene(); scene.background=new T.Color(0x05070b);
  scene.add(new T.AmbientLight(0x8899aa,.65)); const key=new T.DirectionalLight(0xffffff,1); key.position.set(3,5,4); scene.add(key);
  const cam=new T.PerspectiveCamera(opts.fov||40,1,.05,400); const G=new T.Group(); scene.add(G);
  const v={el,scene,cam,G,V:{yaw:view[0],pitch:view[1],dist:view[2],ty:view[3]||0,auto:true},home:view.slice(),spin:opts.spin==null?1:opts.spin,active:false};
  const ptrs=new Map(); let pinch0=0,dist0=v.V.dist;
  el.addEventListener('pointerdown',e=>{ if(e.target.closest('button')) return; el.setPointerCapture(e.pointerId); ptrs.set(e.pointerId,{x:e.clientX,y:e.clientY}); v.V.auto=false; v.active=true;
    if(ptrs.size===2){ const [a,b]=[...ptrs.values()]; pinch0=Math.hypot(a.x-b.x,a.y-b.y); dist0=v.V.dist; } });
  el.addEventListener('pointermove',e=>{ if(!ptrs.has(e.pointerId)) return; const p=ptrs.get(e.pointerId);
    if(ptrs.size===1){ v.V.yaw-=(e.clientX-p.x)*.007; v.V.pitch=Math.max(-1.35,Math.min(1.35,v.V.pitch+(e.clientY-p.y)*.007)); }
    p.x=e.clientX; p.y=e.clientY;
    if(ptrs.size===2){ const [a,b]=[...ptrs.values()]; const d=Math.hypot(a.x-b.x,a.y-b.y); if(pinch0) v.V.dist=Math.max(1.5,Math.min(60,dist0*pinch0/d)); } });
  ['pointerup','pointercancel'].forEach(t=>el.addEventListener(t,e=>{ ptrs.delete(e.pointerId); if(ptrs.size<2) pinch0=0; }));
  el.addEventListener('pointerleave',()=>{ v.active=false; });
  el.addEventListener('wheel',e=>{ if(!v.active) return; e.preventDefault(); v.V.dist=Math.max(1.5,Math.min(60,v.V.dist*Math.exp(e.deltaY*.001))); },{passive:false});
  el.addEventListener('dblclick',()=>{ v.V.yaw=v.home[0]; v.V.pitch=v.home[1]; v.V.dist=v.home[2]; v.V.ty=v.home[3]||0; });
  views.push(v); return v; }

/* =====================================================================================================
   THE ATLAS — strata and the ten bridges
   ===================================================================================================== */
const STRATA=['L0 Calibration','L1 Subspace','L2 Spectrum','L3 Wall','L4 Census','L5 Memory','L6 Volume','L7 Realizations'];
const GRADE={T:'theorem',V:'measured',H:'reading'};
const P={speed:1,playing:!still};
const CARDS=[];
const card=c=>{ CARDS.push(c); return c; };

/* ---------------------------------- B204 ---------------------------------- */
card({ id:'B204', route:[4,5], grade:'T',
  hero:'The boundary sets the sign of the offset: it flips when the two residuals trade places.',
  eq:'odd block A = B ∪ {x}\ne^Ω_A = s₀ / s₁,   Ω_A = 2 artanh ξ,   ξ = (s₀ − s₁)/(s₀ + s₁)\ns₁ = C_xx − b† C_B⁻¹ b          (x filled, block full)\ns₀ = 1 − C_xx − b† (1 − C_B)⁻¹ b    (x empty, block empty)\neven block:  det C_B = det(1 − C_B),  Ω_B = 0\nv → −v:  s₀ ↔ s₁,  Ω → −Ω',
  prose:'The offset of a block is the log-odds of finding it empty against finding it full. On the Rice–Mele chain an even block is protected and its offset is zero, so everything an odd block carries comes from the one site added at its edge: two Schur residuals, the chance that site is filled given a full block and the chance it is empty given an empty one. Their ratio is the offset. Reverse the staggered potential and the two residuals trade places, and the sign flips.',
  carry:'A half-filled Rice–Mele chain (t₁, t₂, v), its correlation matrix C, and an odd block of 2m + 1 sites written as an even block plus one edge site x.',
  chk:'det C_B = det(1 − C_B) on the even block; then compute s₀ and s₁ by Schur complement and compare log(s₀/s₁) with log det(1 − C_A) − log det C_A.',
  arrive:'The odd block’s offset equals log(s₀/s₁) exactly; its size tends to 2 artanh κ with κ = |v|/√(E_min E_max), and its sign is set by which residual is larger.',
  closed:'v = 0 (s₀ = s₁, the chiral chain: Ω = 0 for every block) or an even block.',
  links:{builds:'B151 (offset = log-odds of empty against full) · B152 (a particle–hole symmetry pins the offset at zero)',pairs:'B153 (the offset is a rapidity, τ = 2 artanh a) · B205',feeds:'B211 (how fast an offset can move)'},
  why:'Block determinants factor through the Schur complement: det C_A = det C_B · s₁ and det(1 − C_A) = det(1 − C_B) · s₀. The even block is protected, so the two even factors cancel and only the ratio of residuals survives. The sublattice map sends v to −v and exchanges full with empty, which is s₀(v) = s₁(−v).',
  view:[0.35,0.55,8.6,0.5],
  controls:()=>`<label>odd block 2m+1 <input data-l type="range" min="1" max="5" step="1" value="4"><output>9</output></label><label>v <input data-v type="range" min="-0.8" max="0.8" step="0.02" value="0.4"><output>0.40</output></label><button data-sweep aria-pressed="true">Sweep v</button>`,
  bind(el){ const l=el.querySelector('[data-l]'), v=el.querySelector('[data-v]'), sw=el.querySelector('[data-sweep]');
    l.oninput=()=>{ this.m=+l.value; l.nextElementSibling.textContent=2*this.m+1; this.recompute(); this.draw(); };
    v.oninput=()=>{ this.sweep=false; sw.setAttribute('aria-pressed',false); this.v=+v.value; v.nextElementSibling.textContent=f(this.v,2); this.recompute(); this.draw(); };
    sw.onclick=()=>{ this.sweep=!this.sweep; sw.setAttribute('aria-pressed',this.sweep); }; this.vInput=v; },
  make(G){ this.G=G; this.m=4; this.v=.4; this.t1=.6; this.t2=1; this.sweep=true; this.ph=0; this.dyn=new T.Group(); G.add(this.dyn); this.cache={}; this.recompute(); this.draw(); },
  recompute(){ const key=this.m+','+this.v.toFixed(2); if(!this.cache[key]){ const L=2*this.m+1, C=A.rmCorr(L,this.t1,this.t2,this.v), r=A.residuals(C), CB=C.slice(0,L-1).map(q=>q.slice(0,L-1));
      this.cache[key]={L,s0:r.s0,s1:r.s1,Om:A.offsetLogdet(C),OmB:A.offsetLogdet(CB),occ:C.map((q,i)=>q[i])}; } this.s=this.cache[key]; },
  draw(){ clear(this.dyn); const s=this.s, L=s.L, dx=7.2/(L+1), x0=-3.6+dx;
    for(let i=0;i<L;i++){ const x=x0+i*dx, isx=i===L-1, h=s.occ[i]*1.6;
      this.dyn.add(col(x,0,h,isx?HEX.gold:(i%2?HEX.cyan:HEX.violet),.22,isx?null:.85));
      if(i<L-1) this.dyn.add(rod(V3(x,0,0),V3(x+dx,0,0),HEX.grey,i%2?.035:.018,.8)); }
    const xs=x0+(L-1)*dx; this.dyn.add(M.line([V3(-3.7,0,-.6),V3(xs-dx/2,0,-.6)],HEX.faint,.5)); lab(this.dyn,'even block B, Ω_B = 0',V3((x0+xs-dx)/2,-.35,-.6),'#93a3b5',.17);
    lab(this.dyn,'x',V3(xs,-.32,0),'#f2c14e',.2);
    // residual towers on log scale
    const lg=t=>Math.max(.05,(Math.log10(t)+9)*.32);
    this.dyn.add(col(xs+.9,.8,lg(s.s0),HEX.green,.28,.9)); this.dyn.add(col(xs+.9,-.8,lg(s.s1),HEX.rose,.28,.9));
    lab(this.dyn,'s₀',V3(xs+.9,lg(s.s0)+.25,.8),'#63ffb0',.2); lab(this.dyn,'s₁',V3(xs+.9,lg(s.s1)+.25,-.8),'#ff6fae',.2);
    // offset arrow above the chain
    const y=2.2, len=Math.max(-3,Math.min(3,s.Om*2.5)); this.dyn.add(M.line([V3(-3.2,y,0),V3(3.2,y,0)],HEX.faint,.6));
    if(Math.abs(len)>.02) this.dyn.add(arrow(V3(0,y,0),V3(len,y,0),s.Om>0?HEX.green:HEX.rose,.035));
    lab(this.dyn,'Ω = log(s₀/s₁)',V3(0,y+.4,0),'#f2c14e',.2);
    const lim=2*Math.atanh(A.rmK(this.t1,this.t2,this.v))*2.5; [lim,-lim].forEach(xx=>this.dyn.add(rod(V3(xx,y-.18,0),V3(xx,y+.18,0),HEX.gold,.012,.8))); },
  step(dt){ if(this.sweep&&P.playing){ this.ph+=dt*.35; const nv=Math.round(.7*Math.sin(this.ph)*50)/50; if(nv!==this.v){ this.v=nv; if(this.vInput){ this.vInput.value=nv; this.vInput.nextElementSibling.textContent=f(nv,2);} this.recompute(); this.draw(); } }
    const s=this.s, n=(s.L-1)/2, lim=2*Math.atanh(A.rmK(this.t1,this.t2,this.v)), ok=Math.abs(Math.log(s.s0/s.s1)-s.Om)<1e-6;
    return [['block, v',`${s.L} sites, v = ${f(this.v,2)}`,''],['s₀, s₁',`${s.s0.toExponential(3)}, ${s.s1.toExponential(3)}`,''],
      ['log(s₀/s₁)',f(Math.log(s.s0/s.s1),9),'= Ω_A'],['Ω_A = log det(1−C) − log det C',f(s.Om,9),'log(s₀/s₁)',ok],
      ['even block Ω_B',sci(s.OmB),'0',Math.abs(s.OmB)<1e-6],['|Ω_A| against 2 artanh κ',`${f(Math.abs(s.Om),6)} vs ${f(lim,6)}`,'→ 2 artanh κ'],
      ['sign',this.v===0?'0':(s.Om>0?'+ (s₀ > s₁)':'− (s₁ > s₀)'),'(−1)^m sgn v',this.v===0?Math.abs(s.Om)<1e-9:Math.sign(s.Om)===((n%2?-1:1)*Math.sign(this.v))]]; },
  check(){ const r=[]; for(const L of [5,9]){ const C=A.rmCorr(L,.6,1,.4), q=A.residuals(C), Om=A.offsetLogdet(C); r.push([`L=${L}: log(s₀/s₁) vs log-det offset`,`${f(Math.log(q.s0/q.s1),8)} / ${f(Om,8)}`,'equal',Math.abs(Math.log(q.s0/q.s1)-Om)<1e-6]); }
    const a=A.residuals(A.rmCorr(9,.6,1,.4)), b=A.residuals(A.rmCorr(9,.6,1,-.4)); r.push(['v → −v swaps s₀ and s₁',sci(Math.abs(a.s0-b.s1)+Math.abs(a.s1-b.s0)),'0',Math.abs(a.s0-b.s1)+Math.abs(a.s1-b.s0)<1e-10]);
    r.push(['2 artanh κ at (0.6, 1, 0.4)',f(2*Math.atanh(A.rmK(.6,1,.4)),12),'0.881157076037',Math.abs(2*Math.atanh(A.rmK(.6,1,.4))-0.881157076037)<1e-11]); return r; } });

/* ---------------------------------- B205 ---------------------------------- */
card({ id:'B205', route:[5,7], grade:'V',
  hero:'Rice–Mele and Kitaev are opposite chains for the self-dual mode.',
  eq:'self-dual mode:  ν = ½,   2 artanh(1 − 2ν) = 0\nRice–Mele, v = 0:  odd block → exactly one ν = ½\n                   even block → none\nRice–Mele, v ≠ 0:  the mode moves,  |Ω_odd| → 2 artanh κ\nKitaev, |μ| < 2t:  ν → ½ at every block length\n                   ν ↔ 1 − ν symmetric,  Ω = 0',
  prose:'Each block spectrum is a list of occupations ν, and the self-dual mode is the one at ν = ½, where empty and full are equally likely. In the Rice–Mele chain the mode is a matter of parity: at the chiral point every odd block carries exactly one and every even block none, and the staggered potential pushes it off ½, which is where the offset comes from. In the Kitaev chain the mode sits at ½ for every block length, and the spectrum is mirrored so the offset is hidden by construction. One chain lets the self-dual mode move and shows the constant; the other pins the mode and hides it.',
  carry:'Two half-filled chains: Rice–Mele (t₁ = 0.6, t₂ = 1, v) and the Kitaev chain (t = Δ = 1, μ). Block correlation spectra for lengths 4 to 9.',
  chk:'The distance of the nearest occupation to ½ for even and odd blocks of each chain, and the symmetry of each spectrum under ν ↔ 1 − ν.',
  arrive:'Rice–Mele: parity-locked half-mode at v = 0 and a nonzero offset for v ≠ 0. Kitaev, topological phase: a half-mode at every length and zero offset; trivial phase (|μ| > 2t): no half-mode.',
  closed:'μ crosses 2t (the Kitaev half-modes disappear) or v = 0 (the Rice–Mele offset closes).',
  links:{builds:'B152 (particle–hole symmetry pins the offset at zero) · B153 (offset as rapidity)',pairs:'B204 (the boundary sets the sign)',feeds:'B191 (a constant is invisible to one book, recorded by the other)'},
  why:'At the chiral point the Rice–Mele spectrum is symmetric about ½, so an odd number of occupations forces one onto ½; a staggered potential breaks that symmetry. The Kitaev block is a Bogoliubov–de Gennes spectrum, mirrored about ½ by construction, and in the topological phase each cut of the block hosts a Majorana edge, which appears as an occupation pinned at ½.',
  view:[0.1,0.42,9.2,0.7],
  controls:()=>`<label>Rice–Mele v <input data-v type="range" min="0" max="0.8" step="0.05" value="0"><output>0.00</output></label><label>Kitaev μ <input data-mu type="range" min="0" max="3" step="0.25" value="0.5"><output>0.50</output></label>`,
  bind(el){ const v=el.querySelector('[data-v]'), mu=el.querySelector('[data-mu]');
    v.oninput=()=>{ this.v=+v.value; v.nextElementSibling.textContent=f(this.v,2); this.build(); };
    mu.oninput=()=>{ this.mu=+mu.value; mu.nextElementSibling.textContent=f(this.mu,2); this.build(); }; },
  make(G){ this.G=G; this.v=0; this.mu=.5; this.dyn=new T.Group(); G.add(this.dyn); this.cache={}; this.build(); },
  spectra(){ const k1='rm'+this.v, k2='k'+this.mu;
    if(!this.cache[k1]) this.cache[k1]=[4,5,6,7,8,9].map(L=>A.eigSym(A.rmCorr(L,.6,1,this.v)).values);
    if(!this.cache[k2]) this.cache[k2]=[4,5,6,7,8,9].map(L=>A.kitaevBlock(L,this.mu,1,1));
    return {rm:this.cache[k1],kt:this.cache[k2]}; },
  build(){ clear(this.dyn); const s=this.spectra(); this.s=s; const Ls=[4,5,6,7,8,9]; const k9='o9'+this.v; if(this.cache[k9]==null) this.cache[k9]=A.offsetLogdet(A.rmCorr(9,.6,1,this.v)); this.om9=this.cache[k9];
    const draw=(spec,z,name,color)=>{ lab(this.dyn,name,V3(-4.1,1.95,z),'#dfe7ef',.22);
      this.dyn.add(face([V3(-3.4,1,z-.55),V3(3.4,1,z-.55),V3(3.4,1,z+.55),V3(-3.4,1,z+.55)],HEX.gold,.07)); this.dyn.add(M.line([V3(-3.4,1,z-.55),V3(3.4,1,z-.55)],HEX.gold,.4));
      Ls.forEach((L,i)=>{ const x=-2.9+i*1.16; lab(this.dyn,`${L}`,V3(x,-.25,z+.7),'#93a3b5',.16);
        spec[i].forEach(nu=>{ const near=Math.abs(nu-.5)<1e-3; const o=M.orb(near?.075:.045,near?HEX.gold:color); o.position.set(x,nu*2,z+(near?0:(nu-.5)*.4)); this.dyn.add(o); });
        this.dyn.add(M.line([V3(x,0,z),V3(x,2,z)],HEX.grey,.4)); }); };
    draw(s.rm,1.4,'Rice–Mele',HEX.cyan); draw(s.kt,-1.4,'Kitaev',HEX.violet);
    lab(this.dyn,'ν = ½',V3(3.9,1,0),'#f2c14e',.18); lab(this.dyn,'block length',V3(0,-.6,2.4),'#93a3b5',.16); },
  step(){ const s=this.s, d=sp=>Math.min(...sp.map(x=>Math.abs(x-.5))), sym=sp=>{ const a=sp.slice().sort((x,y)=>x-y), b=sp.map(x=>1-x).sort((x,y)=>x-y); return Math.max(...a.map((x,i)=>Math.abs(x-b[i]))); };
    const rmOdd=Math.max(d(s.rm[1]),d(s.rm[3]),d(s.rm[5])), rmEven=Math.min(d(s.rm[0]),d(s.rm[2]),d(s.rm[4])), kt=Math.max(...s.kt.map(d)), ktSym=Math.max(...s.kt.map(sym));
    const om=this.om9;
    return [['Rice–Mele odd blocks: nearest |ν − ½|',sci(rmOdd),this.v===0?'0':'moves off ½',this.v===0?rmOdd<1e-9:null],['Rice–Mele even blocks: nearest |ν − ½|',f(rmEven,4),'> 0',rmEven>1e-3],
      ['Rice–Mele offset, 9 sites',f(om,6),this.v===0?'0':`→ ±${f(2*Math.atanh(A.rmK(.6,1,this.v)),6)}`,this.v===0?Math.abs(om)<1e-6:null],
      ['Kitaev, every length: nearest |ν − ½|',sci(kt),this.mu<2?'→ 0':'none near ½',this.mu<2?kt<1e-3:kt>.1],['Kitaev spectrum ν ↔ 1 − ν',sci(ktSym),'symmetric, Ω = 0',ktSym<1e-9]]; },
  check(){ const d=sp=>Math.min(...sp.map(x=>Math.abs(x-.5)));
    const odd=[5,9].map(L=>d(A.eigSym(A.rmCorr(L,.6,1,0)).values)), even=[4,8].map(L=>d(A.eigSym(A.rmCorr(L,.6,1,0)).values));
    const kt=[4,5,8,9].map(L=>d(A.kitaevBlock(L,.5,1,1))), tr=[4,9].map(L=>d(A.kitaevBlock(L,3,1,1)));
    return [['Rice–Mele v = 0, odd 5, 9: |ν − ½|',odd.map(sci).join(', '),'0',odd.every(x=>x<1e-9)],['Rice–Mele v = 0, even 4, 8',even.map(x=>f(x,4)).join(', '),'none at ½',even.every(x=>x>1e-3)],
      ['Kitaev μ = 0.5, lengths 4, 5, 8, 9',kt.map(sci).join(', '),'→ 0',kt.every(x=>x<1e-3)],['Kitaev μ = 3 (trivial)',tr.map(x=>f(x,3)).join(', '),'none at ½',tr.every(x=>x>.1)]]; } });

/* ---------------------------------- B206 ---------------------------------- */
card({ id:'B206', route:[1,4], grade:'T',
  hero:'Three overlaps of two subspaces, and the books see only the first.',
  eq:'principal-angle squares  c_a = cos²θ_a,  a = 1 … k\nρ = (1/k) Σ c_a      F = ((1/k) Σ √c_a)²      D = Π c_a\nD^{1/k} ≤ F ≤ ρ,     ρ − F = Var(√c_a)\nbooks:  E∓ = ‖P ∓ R‖² = 2k(1 ∓ ρ)',
  prose:'Two k-dimensional subspaces meet at k principal angles, and there are three honest ways to fold those angles into one overlap: the Born average ρ, the fidelity F, and the determinant D that a Slater overlap measures. They are ordered, and they come apart as the angles spread. The two books on an edge carrying these subspaces are 2k(1 ∓ ρ), so they read the Born average and nothing else: the lists (1, 0) and (½, ½) give identical books while F and D move.',
  carry:'Two rank-k orthogonal projectors P and R and their principal angles θ₁ … θ_k.',
  chk:'Compute ρ, F and D from the c_a, and ‖P − R‖², ‖P + R‖² from the matrices.',
  arrive:'D^{1/k} ≤ F ≤ ρ with ρ − F = Var(√c_a); both books are functions of ρ alone.',
  closed:'All principal angles equal (then the three overlaps agree: D^{1/k} = F = ρ).',
  links:{builds:'B185 (both books are Born sums; on rank-k fields E∓ = 2k(1 ∓ p))',pairs:'B190 (P² + V² + L² = 1, with V = p on projector edges)',feeds:'B210 (the coupling weight read at each gap power)'},
  why:'ρ is the mean of the c_a, F the square of the mean of their square roots, and D their product. Jensen gives F ≤ ρ with the gap Var(√c_a); the arithmetic–geometric mean gives D^{1/k} ≤ F. For projectors ‖P ∓ R‖² = Tr P + Tr R ∓ 2 Tr PR = 2k ∓ 2kρ.',
  view:[0.55,0.45,7.4,0.6],
  controls:()=>`<label>spread <input data-s type="range" min="0" max="1" step="0.01" value="0"><output>0.00</output></label><button data-auto aria-pressed="true">Morph</button>`,
  bind(el){ const s=el.querySelector('[data-s]'), a=el.querySelector('[data-auto]'); this.sIn=s;
    s.oninput=()=>{ this.auto=false; a.setAttribute('aria-pressed',false); this.sp=+s.value; s.nextElementSibling.textContent=f(this.sp,2); };
    a.onclick=()=>{ this.auto=!this.auto; a.setAttribute('aria-pressed',this.auto); }; },
  make(G){ this.G=G; this.sp=0; this.auto=true; this.ph=0; this.dyn=new T.Group(); G.add(this.dyn);
    G.add(M.line([V3(1.6,0,-1.3),V3(4,0,-1.3)],HEX.faint,.6)); lab(G,'ρ',V3(2,-.3,-1.3),'#63d3ff',.2); lab(G,'F',V3(2.8,-.3,-1.3),'#b48cff',.2); lab(G,'D^{1/k}',V3(3.6,-.3,-1.3),'#ff6fae',.18);
    lab(G,'books 2k(1∓ρ)',V3(2.8,-.3,1.5),'#f2c14e',.18); },
  cvec(){ return [.5+.5*this.sp,.5-.5*this.sp]; },
  step(dt){ if(this.auto&&P.playing){ this.ph+=dt*.5; this.sp=.5-.5*Math.cos(this.ph); if(this.sIn){ this.sIn.value=this.sp; this.sIn.nextElementSibling.textContent=f(this.sp,2); } }
    clear(this.dyn); const c=this.cvec(), o=A.overlaps(c);
    // two planes in R^4 drawn as two principal-angle wedges
    c.forEach((ci,a)=>{ const th=Math.acos(Math.sqrt(Math.max(0,Math.min(1,ci)))), base=V3(-2.4+a*1.9,0,0), L=1.5;
      const u=V3(0,L,0), w=V3(L*Math.sin(th),L*Math.cos(th),0);
      this.dyn.add(arrow(base,base.clone().add(u),HEX.cyan,.025)); this.dyn.add(arrow(base,base.clone().add(w),HEX.gold,.025));
      this.dyn.add(face([base,...curve(t=>base.clone().add(V3(.6*Math.sin(th*t),.6*Math.cos(th*t),0)),12)],HEX.rose,.25));
      lab(this.dyn,`θ${a+1} = ${f(th*180/Math.PI,0)}°`,base.clone().add(V3(0,-.35,0)),'#93a3b5',.16); });
    const sc=1.8; this.dyn.add(col(2,-1.3,o.rho*sc,HEX.cyan,.3)); this.dyn.add(col(2.8,-1.3,o.F*sc,HEX.violet,.3)); this.dyn.add(col(3.6,-1.3,Math.sqrt(o.D)*sc,HEX.rose,.3));
    this.dyn.add(col(2.5,1.5,o.Em*.25,HEX.gold,.26,.9)); this.dyn.add(col(3.1,1.5,o.Ep*.25,HEX.gold,.26,.9));
    this.o=o; this.c=c;
    return [['c₁, c₂',`${f(c[0],3)}, ${f(c[1],3)}`,''],['ρ (Born)',f(o.rho,6),'½ throughout',Math.abs(o.rho-.5)<1e-12],['F (fidelity)',f(o.F,6),'between ¼ and ½'],['D (Slater)',f(o.D,6),'between 0 and ¼'],
      ['D^{1/k} ≤ F ≤ ρ',`${f(Math.sqrt(o.D),4)} ≤ ${f(o.F,4)} ≤ ${f(o.rho,4)}`,'ordered',Math.sqrt(o.D)<=o.F+1e-12&&o.F<=o.rho+1e-12],['ρ − F vs Var(√c)',`${sci(o.rho-o.F)} / ${sci(o.varSqrt)}`,'equal',Math.abs(o.rho-o.F-o.varSqrt)<1e-12],
      ['books E−, E+',`${f(o.Em,4)}, ${f(o.Ep,4)}`,'2, 6 (fixed)',Math.abs(o.Em-2)<1e-12&&Math.abs(o.Ep-6)<1e-12]]; },
  check(){ const r=A.rng(206); let bad=0, worst=0; for(let i=0;i<2000;i++){ const k=1+Math.floor(r()*4), c=Array.from({length:k},()=>r()); const o=A.overlaps(c);
      if(Math.pow(o.D,1/k)>o.F+1e-12||o.F>o.rho+1e-12) bad++; worst=Math.max(worst,Math.abs(o.rho-o.F-o.varSqrt)); }
    const a=A.overlaps([1,0]), b=A.overlaps([.5,.5]);
    return [['2000 random angle lists: order D^{1/k} ≤ F ≤ ρ',`${bad} failures`,'0',bad===0],['ρ − F = Var(√c), worst',sci(worst),'0',worst<1e-12],
      ['(1,0) vs (½,½): ρ, F, D',`${a.rho},${a.F},${a.D} | ${b.rho},${f(b.F,2)},${b.D}`,'½,¼,0 | ½,½,¼',a.rho===.5&&a.F===.25&&a.D===0&&Math.abs(b.F-.5)<1e-12&&b.D===.25],['books identical',`${a.Em},${a.Ep} | ${b.Em},${b.Ep}`,'2, 6 both',a.Em===b.Em&&a.Ep===b.Ep]]; } });

/* ---------------------------------- B207 ---------------------------------- */
card({ id:'B207', route:[3,7], grade:'H',
  hero:'The doubled Schwarzschild slice reads as the two books of one scalar edge.',
  eq:'isotropic slice:  g = ψ⁴ δ,  ψ = 1 + Γ,  Γ = a/ρ,  a = M/2\nlapse  V = (1 − Γ)/(1 + Γ)\nscalar edge (1, Γ):  E− = (1 − Γ)²,  E+ = (1 + Γ)²\nr = (1 − Γ)/(1 + Γ) = tanh(½ log(ρ/a)) = V\ndoubling ((1 ± V)/2)⁴ g:  sheet + flat,  sheet − = (a/ρ)⁴ δ\nρ → a²/ρ:  Γ → 1/Γ,  V → −V',
  prose:'Bunting and Masood-ul-Alam proved uniqueness of static black holes by doubling the time-symmetric slice with the two conformal factors ((1 ± V)/2)⁴. On Schwarzschild the lapse is exactly the reflection coefficient of one scalar edge whose ends carry 1 and Γ = a/ρ, so the two sheets are the two books of that edge: the parallel book closes at the horizon, where Γ = 1 and V = 0, and the inversion that swaps the sheets is the sector flip that swaps the books. The identities are exact; reading the doubling as a ledger is the interpretation.',
  carry:'The Schwarzschild time-symmetric slice in isotropic radius ρ, mass M = 2a, and its lapse V.',
  chk:'Compare V with the scalar-edge reflection (1 − Γ)/(1 + Γ); compute both doubled conformal factors; apply ρ → a²/ρ.',
  arrive:'V = r exactly; sheet + is flat and sheet − is the inverted flat metric; the inversion sends V to −V and exchanges the books.',
  closed:'At the horizon ρ = a: Γ = 1, V = 0, E− = 0 (a parallel edge) and the two sheets meet.',
  links:{builds:'B189 (one scalar edge is one reflecting step) · B186 (the sector flip swaps the two halves)',pairs:'B199 (one wall where the trace form vanishes, ISCO among them)',feeds:'B176 (the outside half is thermal)'},
  why:'With ψ = 1 + Γ and V = (1 − Γ)/(1 + Γ), (1 + V)/2 = 1/ψ and (1 − V)/2 = Γ/ψ, so ((1 + V)/2)⁴ψ⁴ = 1 and ((1 − V)/2)⁴ψ⁴ = Γ⁴. A scalar edge with ends 1 and Γ has E−/E+ = ((1 − Γ)/(1 + Γ))² = V². Inversion sends Γ to 1/Γ, which reverses the sign of r.',
  view:[0.65,0.48,9.5,0.0],
  controls:()=>`<label>ρ / a <input data-r type="range" min="0.2" max="5" step="0.01" value="2"><output>2.00</output></label><button data-flip>Inversion ρ → a²/ρ</button><button data-auto aria-pressed="true">Travel</button>`,
  bind(el){ const r=el.querySelector('[data-r]'), a=el.querySelector('[data-auto]'); this.rIn=r;
    r.oninput=()=>{ this.auto=false; a.setAttribute('aria-pressed',false); this.rho=+r.value; r.nextElementSibling.textContent=f(this.rho,2); };
    el.querySelector('[data-flip]').onclick=()=>{ this.rho=1/this.rho; r.value=this.rho; r.nextElementSibling.textContent=f(this.rho,2); };
    a.onclick=()=>{ this.auto=!this.auto; a.setAttribute('aria-pressed',this.auto); }; },
  make(G){ this.G=G; this.a=1; this.rho=2; this.auto=true; this.ph=0;
    // the doubled slice embedded as Flamm's surface, coloured by the lapse; rho > a upper sheet, rho < a lower sheet
    const N=80, Mr=40, geo=new T.BufferGeometry(), pos=[], colr=[], idx=[];
    for(let i=0;i<N;i++){ const rho=Math.exp(-1.6+3.2*i/(N-1)); const s=A.schw(1,rho), Rr=s.R, z=Math.sign(Math.log(rho))*Math.sqrt(Math.max(0,16*(Rr-4)))*.32;
      const c=M.colour.ramp((s.V+1)/2);
      for(let j=0;j<Mr;j++){ const t=j/Mr*2*Math.PI, rr=Rr*.32; pos.push(rr*Math.cos(t),z,rr*Math.sin(t)); colr.push(...c); } }
    for(let i=0;i<N-1;i++) for(let j=0;j<Mr;j++){ const a=i*Mr+j, b=i*Mr+(j+1)%Mr, c=(i+1)*Mr+j, d=(i+1)*Mr+(j+1)%Mr; idx.push(a,b,c,b,d,c); }
    geo.setAttribute('position',new T.Float32BufferAttribute(pos,3)); geo.setAttribute('color',new T.Float32BufferAttribute(colr,3)); geo.setIndex(idx); geo.computeVertexNormals();
    G.add(new T.Mesh(geo,new T.MeshStandardMaterial({vertexColors:true,side:T.DoubleSide,transparent:true,opacity:.55,roughness:.6,depthWrite:false})));
    G.add(new T.LineSegments(new T.WireframeGeometry(geo),new T.LineBasicMaterial({color:0x63d3ff,transparent:true,opacity:.05})));
    G.add(ring(4*.32,HEX.gold,.9,0)); lab(G,'horizon ρ = a,  V = 0,  E− = 0',V3(1.9,.15,0),'#f2c14e',.17);
    lab(G,'sheet + (flat)',V3(-2.3,1.9,0),'#93a3b5',.16); lab(G,'sheet − (inverted flat)',V3(-2.3,-1.9,0),'#93a3b5',.16);
    this.dyn=new T.Group(); G.add(this.dyn); this.tr=M.trail(160,.09); G.add(this.tr); },
  step(dt){ if(this.auto&&P.playing){ this.ph+=dt*.25; this.rho=Math.exp(1.4*Math.sin(this.ph)); if(this.rIn){ this.rIn.value=this.rho; this.rIn.nextElementSibling.textContent=f(this.rho,2); } }
    clear(this.dyn); const s=A.schw(this.a,this.rho), si=A.schw(this.a,this.a*this.a/this.rho);
    const z=Math.sign(Math.log(this.rho))*Math.sqrt(Math.max(0,16*(s.R-4)))*.32, P0=V3(s.R*.32,z,0);
    const o=M.orb(.09,0xffffff); o.position.copy(P0); this.dyn.add(o); M.pushTrail(this.tr,P0,M.colour.ramp((s.V+1)/2));
    // the scalar edge beside the surface: two ends 1 and Gamma, books as columns
    const bx=3.2; this.dyn.add(col(bx,-.4,1*.8,HEX.cyan,.22)); this.dyn.add(col(bx,.4,Math.min(4,s.G)*.8,HEX.violet,.22));
    this.dyn.add(col(bx+.9,-.4,s.Em*.5,HEX.rose,.22,.9)); this.dyn.add(col(bx+.9,.4,Math.min(8,s.Ep)*.5,HEX.green,.22,.9));
    return [['ρ/a, Γ',`${f(this.rho/this.a,4)}, ${f(s.G,4)}`,''],['lapse V',f(s.V,8),'= r of the edge',true],['edge r = (1−Γ)/(1+Γ)',f((1-s.G)/(1+s.G),8),'V',Math.abs((1-s.G)/(1+s.G)-s.V)<1e-14],
      ['E−/E+ against V²',`${f(s.Em/s.Ep,8)} / ${f(s.V*s.V,8)}`,'equal',Math.abs(s.Em/s.Ep-s.V*s.V)<1e-14],['sheet + factor ((1+V)/2)⁴ψ⁴',f(s.wPlus,10),'1 (flat)',Math.abs(s.wPlus-1)<1e-12],
      ['sheet − factor vs (a/ρ)⁴',`${sci(s.wMinus)} / ${sci(s.G**4)}`,'equal',Math.abs(s.wMinus-s.G**4)<1e-12*Math.max(1,s.G**4)],['inversion: V(a²/ρ)',f(si.V,8),'−V',Math.abs(si.V+s.V)<1e-14]]; },
  check(){ let w=0; for(let i=1;i<200;i++){ const rho=.05+i*.04, s=A.schw(.5,rho), si=A.schw(.5,.25/rho); w=Math.max(w,Math.abs((1-s.G)/(1+s.G)-s.V),Math.abs(s.wPlus-1),Math.abs(si.V+s.V)); }
    const h=A.schw(1,1); return [['200 radii: V = r, sheet + flat, inversion flips V',sci(w),'0',w<1e-12],['horizon ρ = a: V, E−',`${h.V}, ${h.Em}`,'0, 0',h.V===0&&h.Em===0]]; } });

/* ---------------------------------- B208 ---------------------------------- */
const L8=[[Math.cos(.5),-Math.sin(.5),0],[Math.sin(.5),Math.cos(.5),0],[0,0,.9]], R8=[[1,0,0]];
card({ id:'B208', route:[5,0], grade:'T',
  hero:'A present reading predicts its own future exactly when what it cannot see stays unseen, and the quotient by that invisible part is the smallest predictor.',
  eq:'x_{t+1} = L x_t,   y_t = R x_t\nN = ∩_{j<d} ker(R L^j) = largest L-invariant subspace in ker R\nfutures agree ∀n  ⇔  they agree for n < d − rank R + 1\nsufficient F:  ker F ⊆ N,  rank F ≥ dim V/N\nthe present closes  ⇔  L ker R ⊆ ker R  ⇔  N = ker R',
  prose:'Two states that differ only by a vector in N give the same readings forever, so nothing about them is ever worth keeping; two states that differ by anything else are told apart within d − rank R + 1 readings, which is the most any system needs. The quotient V/N is therefore the smallest thing the present can carry and still predict every future reading. The present reading alone is enough exactly when the unseen part is never fed back into the seen part.',
  carry:'A linear system x ↦ L x on V of dimension d, with a reading y = R x.',
  chk:'Stack R, RL, RL², … until the rank stops growing; its kernel is N. Compare with the bound d − rank R + 1 and with L ker R ⊆ ker R.',
  arrive:'N, the minimal predictor V/N, and the number of readings that decide.',
  closed:'R injective on the orbit (N = 0, the reading sees everything) or L ker R ⊆ ker R (the present closes and N = ker R).',
  links:{builds:'B104 (silence is certified by finitely many moments)',pairs:'B209 (what is eliminated returns as memory)',feeds:'B211 (how fast a kept record can move)'},
  why:'The kernels of the stacked readings decrease; once one step adds nothing, no later step can (Cayley–Hamilton), and each useful step raises the rank by at least one, starting from rank R, so at most d − rank R + 1 readings are needed. Any F that decides the future must vanish on states with identical futures, so ker F ⊆ N. A linear map that is not one-to-one on V/N loses a difference some reading will show. Kalman’s observability is the classical form.',
  view:[0.75,0.5,7.0,0.2],
  controls:()=>`<label>difference along N <input data-n type="range" min="0" max="1.5" step="0.05" value="1"><output>1.00</output></label><button data-mode aria-pressed="false">Leak N into the reading</button>`,
  bind(el){ const n=el.querySelector('[data-n]'), m=el.querySelector('[data-mode]');
    n.oninput=()=>{ this.dn=+n.value; n.nextElementSibling.textContent=f(this.dn,2); this.reset(); };
    m.onclick=()=>{ this.leak=!this.leak; m.setAttribute('aria-pressed',this.leak); this.reset(); }; },
  make(G){ this.G=G; this.dn=1; this.leak=false;
    G.add(plane(4.4,4.4,HEX.cyan,.05,0)); G.add(M.grid(4.4,8,0x1c2735,.6)); lab(G,'V/N (what must be kept)',V3(1.6,.05,2.4),'#63d3ff',.17);
    G.add(rod(V3(0,-1.8,0),V3(0,1.8,0),HEX.rose,.012,.8)); lab(G,'N (never seen)',V3(.25,1.95,0),'#ff6fae',.17);
    G.add(rod(V3(-2.4,0,0),V3(2.4,0,0),HEX.gold,.012,.8)); lab(G,'reading axis R',V3(2.6,.15,0),'#f2c14e',.16);
    this.trA=M.trail(160,.09); this.trB=M.trail(160,.09); G.add(this.trA); G.add(this.trB); this.dyn=new T.Group(); G.add(this.dyn); this.reset(); },
  mat(){ return this.leak?[[Math.cos(.5),-Math.sin(.5),.35],[Math.sin(.5),Math.cos(.5),0],[0,0,.9]]:L8; },
  reset(){ this.xa=[1.4,0,.3]; this.xb=[1.4,0,.3+this.dn]; this.t=0; this.acc=0; this.ya=[]; this.yb=[]; M.clearTrail(this.trA); M.clearTrail(this.trB); },
  step(dt){ if(P.playing) this.acc+=dt; if(this.acc>.55){ this.acc=0; const L=this.mat(); this.xa=A.mv(L,this.xa); this.xb=A.mv(L,this.xb); this.t++;
      if(this.t>40||Math.hypot(...this.xa)<.05) this.reset(); }
    const pa=V3(this.xa[0],this.xa[2],this.xa[1]), pb=V3(this.xb[0],this.xb[2],this.xb[1]);
    clear(this.dyn); const oa=M.orb(.12,HEX.cyan), ob=M.orb(.12,HEX.violet); oa.position.copy(pa); ob.position.copy(pb); this.dyn.add(oa); this.dyn.add(ob);
    this.dyn.add(M.line([pa,pb],HEX.rose,.6)); this.dyn.add(M.line([pa,V3(this.xa[0],0,0)],HEX.gold,.35));
    const sh=M.orb(.06,HEX.gold); sh.position.set(this.xa[0],0,0); this.dyn.add(sh);
    M.pushTrail(this.trA,pa,RGB(HEX.cyan)); M.pushTrail(this.trB,pb,RGB(HEX.violet));
    const L=this.mat(), rn=A.readingsNeeded(L,R8), dimN=3-rn.full, ya=this.xa[0], yb=this.xb[0];
    const closes=(()=>{ const kr=[[0,1,0],[0,0,1]]; return kr.every(v=>Math.abs(A.mv(L,v)[0])<1e-12); })();
    return [['readings y(A), y(B)',`${f(ya,5)}, ${f(yb,5)}`,this.leak?'differ':'identical',this.leak?null:Math.abs(ya-yb)<1e-12],['dim N',`${dimN}`,this.leak?'0':'1',dimN===(this.leak?0:1)],
      ['minimal predictor dim V/N',`${rn.full}`,this.leak?'3':'2',rn.full===(this.leak?3:2)],['readings that decide',`${rn.k}`,`≤ d − rank R + 1 = 3`,rn.k<=3],['present closes (L ker R ⊆ ker R)',closes?'yes':'no','no (rotation feeds the plane)',!closes]]; },
  check(){ const r=A.rng(208); let worst=0; for(let i=0;i<181;i++){ const d=3+Math.floor(r()*4), q=1+Math.floor(r()*(d-1)); const L=Array.from({length:d},()=>Array.from({length:d},()=>A.gauss(r))), Rm=Array.from({length:q},()=>Array.from({length:d},()=>A.gauss(r)));
      const rn=A.readingsNeeded(L,Rm); worst=Math.max(worst,rn.k-(d-A.rank(Rm)+1)); }
    const S=[[0,0,0,0,1],[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0]], sh=A.readingsNeeded(S,[[1,0,0,0,0]]);
    return [['181 random systems: readings beyond d − rank R + 1',`${worst}`,'≤ 0',worst<=0],['five-site shift, one reading',`${sh.k}`,'5 (bound attained)',sh.k===5]]; } });

/* ---------------------------------- B209 ---------------------------------- */
const D9={gam:.35,om:1.6};
card({ id:'B209', route:[1,5], grade:'T',
  hero:'Eliminating a hidden block leaves a memory kernel and a separate hidden-preparation source, and both vanish exactly when the cut commutes with the Hamiltonian.',
  eq:'ẋ = A x + B y,    ẏ = C x + D y\nẋ(t) = A x(t) + ∫₀ᵗ K(t − s) x(s) ds + S(t)\nK(τ) = B e^{Dτ} C,      S(t) = B e^{Dt} y(0)\nL = −iH:  K(τ) = −B e^{−iH₂₂τ} B†\n          S(t) = −i B e^{−iH₂₂t} y(0)\nB = 0  ⇔  [H, Π] = 0',
  prose:'Remove the part of the system you do not watch and its influence does not disappear; it comes back twice. Once as memory, a kernel that weights the kept variable’s own past by how long the hidden block takes to answer, and once as a source, the hidden block’s own starting state leaking in. For a Hamiltonian both pass through the same coupling B, so both vanish together exactly when the cut commutes with the Hamiltonian. For a general generator they are separate books: with C = 0 the kernel dies and the source does not.',
  carry:'A linear flow on kept ⊕ hidden with blocks A, B, C, D, and a starting hidden state y(0).',
  chk:'Integrate the full flow exactly and evaluate the memory equation on its solution.',
  arrive:'The kept variable obeys the closed equation with kernel B e^{Dτ}C and source B e^{Dt}y(0); for L = −iH the signs are −B e^{−iH₂₂τ}B† and −iB e^{−iH₂₂t}y(0).',
  closed:'B = 0 (no influence reaches the kept block); for a Hamiltonian this is [H, Π] = 0 for the cut projector Π.',
  links:{builds:'B48 (the Schur seam) · B161',pairs:'B208 (what the present must keep)',feeds:'B210 (the zero-lag memory is the coupling weight)'},
  why:'Solve the hidden equation by variation of constants, y(t) = e^{Dt}y(0) + ∫₀ᵗ e^{D(t−s)} C x(s) ds, and substitute into ẋ = Ax + By. For L = −iH the blocks are −iH₁₁, −iB, −iB† and −iH₂₂, and the two factors of −i give the minus sign in front of the kernel.',
  view:[0.6,0.6,8.0,0.6],
  controls:()=>`<label>hidden damping γ <input data-g type="range" min="0" max="1.2" step="0.05" value="0.35"><output>0.35</output></label><label>coupling B <input data-b type="range" min="0" max="1.5" step="0.05" value="1"><output>1.00</output></label>`,
  bind(el){ const g=el.querySelector('[data-g]'), b=el.querySelector('[data-b]');
    g.oninput=()=>{ this.gam=+g.value; g.nextElementSibling.textContent=f(this.gam,2); this.build(); };
    b.oninput=()=>{ this.b=+b.value; b.nextElementSibling.textContent=f(this.b,2); this.build(); }; },
  make(G){ this.G=G; this.gam=D9.gam; this.b=1; this.dyn=new T.Group(); G.add(this.dyn); this.cur=M.points(1,.2); G.add(this.cur); this.t=0; this.build(); },
  kern(tau){ const e=Math.exp(-this.gam*tau); return this.b*this.b*e*Math.cos(D9.om*tau); },   // B = (b,0), C = (b,0)^T, D = [[-g, w],[-w,-g]]
  build(){ clear(this.dyn); const N=48, H=[], Cc=[]; let mx=0;
    for(let i=0;i<N;i++){ H.push([]); Cc.push([]); for(let j=0;j<N;j++){ const t=i/(N-1)*6, s=j/(N-1)*6; const v=s<=t?this.kern(t-s):0; H[i].push(v); mx=Math.max(mx,Math.abs(v)); } }
    const surf=M.surface(N,N,2.4,2.4); for(let i=0;i<N;i++) for(let j=0;j<N;j++){ const v=H[i][j]; Cc[i][j]=v>=0?M.colour.ramp(.55+.45*v/(mx||1)):M.colour.ramp(.45+.45*v/(mx||1)); H[i][j]=1.4*v/(mx||1); }
    M.setSurface(surf,H,Cc); this.dyn.add(surf);
    lab(this.dyn,'present time t',V3(0,-.2,2.75),'#93a3b5',.17); lab(this.dyn,'past time s',V3(-2.9,-.2,0),'#93a3b5',.17); lab(this.dyn,'kernel K(t − s), s ≤ t',V3(0,1.9,-2.4),'#f2c14e',.17);
    // source term along the far edge
    const src=curve(u=>V3(-2.4+4.8*u,1.4*this.b*Math.exp(-this.gam*u*6)*Math.cos(D9.om*u*6)/(Math.max(this.b,1e-9)),2.65),80); this.dyn.add(M.line(src,HEX.rose,.9)); lab(this.dyn,'source S(t) = B e^{Dt} y(0)',V3(2.4,1.6,2.7),'#ff6fae',.15); },
  step(dt){ if(P.playing) this.t=(this.t+dt*.8)%6; const u=this.t/6; M.setPt(this.cur,0,V3(-2.4+4.8*u,.1,-2.4+4.8*u),[1,1,1]); M.flush(this.cur);
    const tau=this.t, k=this.kern(tau);
    return [['lag τ',f(tau,3),''],['kernel K(τ) = b² e^{−γτ} cos ωτ',f(k,6),''],['memory at zero lag K(0)',f(this.kern(0),4),'= ‖B‖² = coupling weight',Math.abs(this.kern(0)-this.b*this.b)<1e-15],['B = 0: kernel and source',this.b===0?'both 0':'nonzero','vanish together',this.b===0?true:null]]; },
  check(){ // exact flow vs memory equation on its solution, Schrodinger case, 3x3 complex by series exponential
    const n=3; const H=[[.4,.7,-.3],[.7,-.2,.5],[-.3,.5,.9]];
    const expmi=(Hm,t)=>{ const ev=A.eigSym(Hm); return {apply:v=>{ const out=[[0,0],[0,0],[0,0]].slice(0,Hm.length).map(()=>[0,0]); ev.vectors.forEach((vec,k)=>{ const c=vec.reduce((s,x,i)=>[s[0]+x*v[i][0],s[1]+x*v[i][1]],[0,0]); const ph=-ev.values[k]*t, cr=Math.cos(ph), ci=Math.sin(ph); const z=[c[0]*cr-c[1]*ci,c[0]*ci+c[1]*cr]; vec.forEach((x,i)=>{ out[i][0]+=x*z[0]; out[i][1]+=x*z[1]; }); }); return out; }}; };
    const z0=[[1,0],[0,0],[0,0]], x=t=>expmi(H,t).apply(z0); const H22=[[H[1][1],H[1][2]],[H[2][1],H[2][2]]], Bv=[H[0][1],H[0][2]];
    const t=1.3, h=1e-5, xp=x(t+h)[0], xm=x(t-h)[0], xd=[(xp[0]-xm[0])/(2*h),(xp[1]-xm[1])/(2*h)];
    // memory integral with kernel -B e^{-iH22 tau} B^dag (Simpson, 2000 panels)
    const NS=2000; let mem=[0,0]; for(let q=0;q<=NS;q++){ const s=t*q/NS, w=(q===0||q===NS)?1:(q%2?4:2); const xs=x(s)[0];
      const e=expmi(H22,t-s).apply([[Bv[0],0],[Bv[1],0]]); const kr=-(Bv[0]*e[0][0]+Bv[1]*e[1][0]), ki=-(Bv[0]*e[0][1]+Bv[1]*e[1][1]);
      mem[0]+=w*(kr*xs[0]-ki*xs[1]); mem[1]+=w*(kr*xs[1]+ki*xs[0]); } mem=mem.map(m=>m*t/NS/3);
    const xt=x(t)[0], ax=[H[0][0]*xt[1],-H[0][0]*xt[0]];   // -i H11 x
    const rhs=[ax[0]+mem[0],ax[1]+mem[1]], res=Math.hypot(xd[0]-rhs[0],xd[1]-rhs[1])/Math.hypot(...xd);
    return [['Schrödinger case, y(0) = 0: ẋ vs memory equation',sci(res),'0 (to quadrature)',res<1e-6]]; } });

/* ---------------------------------- B210 ---------------------------------- */
card({ id:'B210', route:[2,4], grade:'T',
  hero:'One coupling weight read at gap power k is a log-convex ladder, and the coupling energy sits between the eigenprojector metric below and the squared commutator above.',
  eq:'S_k = Σ_{i≠j} |K_ij|² Δ_ij^k,    Δ_ij = |E_i − E_j|\nlog S_k convex in k:   S_k² ≤ S_{k−1} S_{k+1}\nk = −2 metric · −1 static response · 0 coupling energy\nk = +2:  S₂ = ‖[D, K]‖²_F\nS₀² ≤ S₋₂ S₂\nopen rung:   S₀²/S₋₁ ≤ S₁ ≤ √(S₀ S₂)',
  prose:'Take one coupling K between levels E_i and read its weight |K_ij|² against powers of the gaps. Every rung is the same weights seen through a different lens: inverse-square gaps give the metric of the eigenprojectors, inverse gaps the static response, no gaps the plain coupling energy, squared gaps the squared commutator with the unperturbed Hamiltonian. Because the rungs are moments of one positive measure, their logarithms lie on a convex curve, so the middle rung is pinned between its neighbours and the one rung without a name is bracketed.',
  carry:'Levels E₁ … E_n and a Hermitian coupling K (the off-diagonal weights).',
  chk:'Compute S₋₂ … S₂ and test convexity; compare S₂ with ‖[D, K]‖² and with ¼‖[H, H†]‖² for H = D + iK.',
  arrive:'A convex ladder; S₂ = ‖[D, K]‖² = ¼‖[H, H†]‖² only for the non-Hermitian companion H = D + iK.',
  closed:'K diagonal (every rung zero) or all gaps equal (every rung proportional, the ladder is a straight line).',
  links:{builds:'B25 (susceptibility and inverse-square gaps) · B130, B131 (optical response and the metric) · B109 (speed of change is the weight between)',pairs:'B206',feeds:'B211'},
  why:'S_k = Σ w_ij Δ_ij^k with w ≥ 0 is a moment sequence, and Cauchy–Schwarz on (w Δ^{(k−1)/2}, w Δ^{(k+1)/2}) gives S_k² ≤ S_{k−1}S_{k+1}. [D, K]_ij = (E_i − E_j)K_ij, so ‖[D, K]‖² = S₂. For H = D + iK, [H, H†] = −2i[D, K]. For a Hermitian H the self-commutator is zero, which is why the top rung is the commutator with D, not non-normality of H.',
  view:[0.4,0.35,8.4,1.0],
  controls:()=>`<label>top level E₃ <input data-e type="range" min="1.2" max="4" step="0.05" value="2.5"><output>2.50</output></label>`,
  bind(el){ const e=el.querySelector('[data-e]'); e.oninput=()=>{ this.E3=+e.value; e.nextElementSibling.textContent=f(this.E3,2); this.build(); }; },
  make(G){ this.G=G; this.E3=2.5; this.K=[[0,.6,.3],[.6,0,.5],[.3,.5,0]]; this.dyn=new T.Group(); G.add(this.dyn); this.fl=M.points(60,.1); G.add(this.fl); this.ph=0; this.build(); },
  build(){ clear(this.dyn); const E=[0,1,this.E3], L=A.ladder(E,this.K); this.L=L; const ks=[-2,-1,0,1,2];
    // rungs as rings of pair-columns
    ks.forEach((k,r)=>{ const y=r*.8; this.dyn.add(ring(1.3,HEX.faint,.35,y,64)); lab(this.dyn,`k = ${k>0?'+':''}${k}`,V3(-2.2,y,0),'#93a3b5',.17);
      const pairs=[[0,1],[0,2],[1,2]]; pairs.forEach(([i,j],q)=>{ const a=q/3*2*Math.PI, d=Math.abs(E[i]-E[j]), w=this.K[i][j]**2*Math.pow(d,k);
        this.dyn.add(col(1.3*Math.cos(a),1.3*Math.sin(a),Math.min(1.5,w*.6),[HEX.violet,HEX.cyan,HEX.gold,HEX.coral,HEX.rose][r],.13,.9,y)); }); });
    // log S_k curve beside, with the k = +1 bracket
    const lx=k=>2.4+.45*(k+2), ly=k=>1.6+Math.log(L.S[k])*1.2;
    this.dyn.add(M.line(ks.map(k=>V3(lx(k),ly(k),0)),HEX.gold,1)); ks.forEach(k=>{ const o=M.orb(.06,k===1?HEX.rose:HEX.gold); o.position.set(lx(k),ly(k),0); this.dyn.add(o); });
    const lo=L.S[0]**2/L.S[-1], hi=Math.sqrt(L.S[0]*L.S[2]); this.dyn.add(rod(V3(lx(1),1.6+Math.log(lo)*1.2,.05),V3(lx(1),1.6+Math.log(hi)*1.2,.05),HEX.rose,.02,.8));
    lab(this.dyn,'log S_k',V3(lx(0),ly(2)+.5,0),'#f2c14e',.17); },
  step(dt){ if(P.playing) this.ph+=dt*.6; for(let q=0;q<60;q++){ const u=((this.ph*.3+q/60)%1), r=Math.floor(u*5), a=u*5%1*2*Math.PI; M.setPt(this.fl,q,V3(1.3*Math.cos(a),r*.8+.02,1.3*Math.sin(a)),[.9,.8,.4]); } M.flush(this.fl);
    const S=this.L.S, conv=[-1,0,1].every(k=>S[k]**2<=S[k-1]*S[k+1]*(1+1e-12));
    const E=[0,1,this.E3]; let sc=0; for(let i=0;i<3;i++) for(let j=0;j<3;j++){ const c=(E[i]-E[j])*this.K[i][j]; sc+=c*c; } // 1/4||[H,H^dag]||^2 for H = D + iK equals ||[D,K]||^2
    return [['S₋₂ (metric)',f(S[-2],5),this.E3===2.5?'0.97102':''],['S₋₁ (static response)',f(S[-1],5),this.E3===2.5?'1.12533':''],['S₀ (coupling energy)',f(S[0],5),'1.40000',Math.abs(S[0]-1.4)<1e-12],
      ['S₂ vs ‖[D, K]‖²',`${f(S[2],5)} / ${f(this.L.comm,5)}`,'equal',Math.abs(S[2]-this.L.comm)<1e-12],['log-convex at k = −1, 0, +1',conv?'yes':'no','yes',conv],
      ['S₀² ≤ S₋₂ S₂',`${f(S[0]**2,4)} ≤ ${f(S[-2]*S[2],4)}`,'holds',S[0]**2<=S[-2]*S[2]],['open rung S₁ in [S₀²/S₋₁, √(S₀S₂)]',`${f(S[0]**2/S[-1],4)} ≤ ${f(S[1],4)} ≤ ${f(Math.sqrt(S[0]*S[2]),4)}`,'bracketed',S[0]**2/S[-1]<=S[1]&&S[1]<=Math.sqrt(S[0]*S[2])]]; },
  check(){ const r=A.rng(210); let bad=0; for(let i=0;i<400;i++){ const n=3+Math.floor(r()*5), E=Array.from({length:n},()=>2*A.gauss(r)), K=Array.from({length:n},()=>new Array(n).fill(0));
      for(let a=0;a<n;a++) for(let b=a+1;b<n;b++){ K[a][b]=K[b][a]=A.gauss(r); } const L=A.ladder(E,K), S=L.S;
      if(![-1,0,1].every(k=>S[k]**2<=S[k-1]*S[k+1]*(1+1e-12))||Math.abs(S[2]-L.comm)>1e-9*L.comm||!(S[0]**2/S[-1]<=S[1]*(1+1e-12)&&S[1]<=Math.sqrt(S[0]*S[2])*(1+1e-12))) bad++; }
    const L=A.ladder([0,1,2.5],[[0,.6,.3],[.6,0,.5],[.3,.5,0]]);
    return [['400 random systems: convexity, S₂ = ‖[D,K]‖², bracket',`${bad} failures`,'0',bad===0],['worked example S₋₂ … S₂',[-2,-1,0,1,2].map(k=>f(L.S[k],4)).join(', '),'0.9710, 1.1253, 1.4000, 1.9200, 2.9700',Math.abs(L.S[-2]-0.9710222)<1e-6&&Math.abs(L.S[2]-2.97)<1e-12]]; } });

/* ---------------------------------- B211 ---------------------------------- */
card({ id:'B211', route:[1,5], grade:'T',
  hero:'A record moves only as fast as the weight between and the sharpness of the cut allow, and one trajectory attains that speed at every instant.',
  eq:'P = [[C, B],[B†, D]],   P² = P,   0 < C < I\nτ = Tr[log(I − C) − log C]    g = ½‖Ṗ‖²    S = Tr[(C(I − C))⁻¹]\nτ̇² ≤ 4 g S\nequality ⇔ Ṗ = λ[P, [P, F]],  F = diag(W, 0),  W = −(C(I − C))⁻¹\nscalar cut:  4gS − τ̇² = 4(Im b̄ḃ)²/(c(1 − c))²,  b = P₁₂\nṖ = −i[H, P]:  g = E_B = ‖P H (1 − P)‖²,   |τ̇| ≤ 2√(E_B) S',
  prose:'The offset of the part of a state you can reach, τ, is a record, and it cannot change faster than the state itself moves. The bound has two factors: the geometric speed g, which for a Hamiltonian is exactly the coupling energy across the kept sector, and S, which grows as the cut sharpens toward an occupation of 0 or 1. Moving straight along the meridian of the Bloch sphere attains it at every instant; moving around a latitude changes only a phase and leaves the record still. The census C(I − C) alone cannot see the record: diag(0.2, 0.8) and diag(0.2, 0.2) share the census 0.16 I with offsets 0 and log 16.',
  carry:'A moving orthogonal projector P with a fixed accessible cut and its block C, 0 < C < I.',
  chk:'Differentiate τ along random tangent directions and along T = [P, [P, F]]; compare τ̇² with 4gS.',
  arrive:'τ̇² ≤ 4gS everywhere, with equality exactly along T; the scalar-cut gap is 4(Im b̄ḃ)²/(c(1 − c))².',
  closed:'C reaches 0 or I (S diverges, the offset is unbounded) or Ṗ = 0.',
  links:{builds:'B109 (g = ½ Tr Ṗ²) · B151 (offset as log-odds) · B160',pairs:'B204',feeds:'B210 (g = E_B is the k = 0 rung of the coupling seen by P)'},
  why:'τ̇ = Tr(W Ċ) = Tr(T Ṗ) because Ṗ is tangent and T is the tangent projection of F. Cauchy–Schwarz gives τ̇² ≤ ‖T‖²‖Ṗ‖² = ‖T‖² · 2g, and ‖T‖² = 2 Tr(CW² − CWCW) = 2S using [W, C] = 0. Equality is Ṗ parallel to T.',
  view:[0.9,0.35,6.6,0],
  controls:()=>`<label>direction α <input data-a type="range" min="0" max="90" step="1" value="35"><output>35°</output></label><label>polar angle θ <input data-t type="range" min="15" max="165" step="1" value="70"><output>70°</output></label>`,
  bind(el){ const a=el.querySelector('[data-a]'), t=el.querySelector('[data-t]');
    a.oninput=()=>{ this.al=+a.value*Math.PI/180; a.nextElementSibling.textContent=a.value+'°'; };
    t.oninput=()=>{ this.th=+t.value*Math.PI/180; t.nextElementSibling.textContent=t.value+'°'; }; },
  make(G){ this.G=G; this.al=35*Math.PI/180; this.th=70*Math.PI/180; this.ph=0;
    G.add(M.shell(1.6,0x63d3ff,.06)); for(let i=1;i<6;i++){ const y=1.6*Math.cos(i*Math.PI/6), r=1.6*Math.sin(i*Math.PI/6); G.add(ring(r,HEX.faint,.25,y,72)); }
    for(let i=0;i<6;i++){ const a=i*Math.PI/6; G.add(M.line(curve(u=>{ const t=u*Math.PI; return V3(1.6*Math.sin(t)*Math.cos(a),1.6*Math.cos(t),1.6*Math.sin(t)*Math.sin(a)); },60),HEX.faint,.2)); }
    lab(G,'accessible full (c = 1)',V3(0,1.95,0),'#93a3b5',.15); lab(G,'hidden full (c = 0)',V3(0,-1.95,0),'#93a3b5',.15);
    this.dyn=new T.Group(); G.add(this.dyn); this.tr=M.trail(200,.08); G.add(this.tr);
    // the saturating ratio curve outside the sphere
    this.side=new T.Group(); G.add(this.side); },
  pt(th,ph){ return V3(1.6*Math.sin(th)*Math.cos(ph),1.6*Math.cos(th),1.6*Math.sin(th)*Math.sin(ph)); },
  step(dt){ if(P.playing) this.ph+=dt*.6; clear(this.dyn); const th=this.th+.35*Math.sin(this.ph)*Math.cos(this.al), ph=.8*Math.sin(this.ph)*Math.sin(this.al)/Math.max(.2,Math.sin(this.th));
    const p=this.pt(th,ph), o=M.orb(.09,0xffffff); o.position.copy(p); this.dyn.add(o); M.pushTrail(this.tr,p,[.95,.8,.35]);
    // tangent arrows: meridian (saturating) and actual direction
    const e1=V3(Math.cos(th)*Math.cos(ph),-Math.sin(th),Math.cos(th)*Math.sin(ph)), e2=V3(-Math.sin(ph),0,Math.cos(ph));
    this.dyn.add(arrow(p,p.clone().add(e1.clone().multiplyScalar(.7)),HEX.green,.02)); const d=e1.clone().multiplyScalar(Math.cos(this.al)).add(e2.clone().multiplyScalar(Math.sin(this.al)));
    this.dyn.add(arrow(p,p.clone().add(d.multiplyScalar(.7)),HEX.gold,.02));
    const s=A.cutSpeed(this.th,this.al);
    clear(this.side); const bx=2.4; this.side.add(col(bx,0,Math.min(3,s.taudot*s.taudot*.15),HEX.gold,.25)); this.side.add(col(bx+.55,0,Math.min(3,4*s.g*s.S*.15),HEX.green,.25,.6));
    return [['c = accessible occupation',f(s.c,4),''],['offset τ = log((1 − c)/c)',f(s.tau,5),''],['τ̇² / (4gS)',f(s.ratio,6),this.al===0?'1 (meridian)':'≤ 1',this.al===0?Math.abs(s.ratio-1)<1e-12:s.ratio<=1+1e-12],
      ['gap 4gS − τ̇²',f(s.gap,6),`4(Im b̄ḃ)²/(c(1−c))² = ${f(s.gapFormula,6)}`,Math.abs(s.gap-s.gapFormula)<1e-9],['census vs offset: diag(.2,.8), diag(.2,.2)','0.16 I both','offsets 0, log 16 = 2.772589',true]]; },
  check(){ let worst=0; for(let i=0;i<500;i++){ const th=.2+i/500*2.7, al=(i*0.6180339)%1*Math.PI/2, s=A.cutSpeed(th,al); worst=Math.max(worst,s.ratio, Math.abs(s.gap-s.gapFormula)>1e-8?99:0); }
    const m=A.cutSpeed(1.1,0); const o1=Math.log(.8/.2)+Math.log(.2/.8), o2=2*Math.log(.8/.2);
    return [['500 directions: largest τ̇²/(4gS)',f(worst,6),'≤ 1',worst<=1+1e-12],['meridian (equality case)',f(m.ratio,12),'1',Math.abs(m.ratio-1)<1e-12],['offsets at census 0.16 I',`${f(o1,6)}, ${f(o2,6)}`,'0, log 16 = 2.772589',Math.abs(o1)<1e-15&&Math.abs(o2-Math.log(16))<1e-12]]; } });

/* ---------------------------------- B212 ---------------------------------- */
card({ id:'B212', route:[0,1], grade:'T',
  hero:'Amount and composition separate exactly: the Fisher metric of positive amounts is the squared change of log scale plus the Fisher metric of the proportions, with no cross term.',
  eq:'x_i > 0,  a_i > 0,   I = Σ a_i x_i,   p_i = a_i x_i / I\n(1/I) Σ a_i dx_i²/x_i  =  (d log I)²  +  Σ dp_i²/p_i\nz = √I ψ:   4‖dz_hor‖²/I = (d log I)² + 4 ds²_FS\nds²_FS = ¼ Σ dp_i²/p_i + Var_p(dφ_i)\ncoarse q = K p:   Σ q̇_j²/q_j ≤ Σ ṗ_i²/p_i',
  prose:'Any change in a collection of positive amounts splits into how much there is and what it is made of, and the two pieces add with no interference: the change of log total, and the Fisher speed of the proportions. For complex amplitudes a third piece appears, the spread of relative phases, still with no cross term. A coarse reading that merges components can only lose composition speed, never gain it: a mixture can change inside while a sensor shows nothing.',
  carry:'Positive amounts x with fixed weights a, and a small change dx (or a complex amplitude vector z).',
  chk:'Compute both sides for random amounts and changes; for the coarse reading, compare the merged and unmerged Fisher speeds.',
  arrive:'The split is an identity; equality in the contraction needs ṗ_i/p_i constant within each merged group.',
  closed:'I = 0 (composition undefined) or a component reaches zero (square-root coordinates needed).',
  links:{builds:'B109 (Bures speed and Fisher information from the same metric)',pairs:'B213 (two books of an orbit)',feeds:'B206 (overlaps of what is kept)'},
  why:'Substitute a_i dx_i = p_i dI + I dp_i into (1/I) Σ a_i dx_i²/x_i = Σ (a_i dx_i)²/(I a_i x_i) = Σ (p_i dI + I dp_i)²/(I² p_i). Expanding gives (dI/I)² Σ p_i + 2 (dI/I) Σ dp_i + Σ dp_i²/p_i, and Σ p_i = 1, Σ dp_i = 0. The contraction is Cauchy–Schwarz within each output.',
  view:[0.78,0.45,6.4,0.8],
  controls:()=>`<button data-new>New motion</button><label>scale share <input data-s type="range" min="0" max="1" step="0.05" value="0.5"><output>0.50</output></label>`,
  bind(el){ el.querySelector('[data-new]').onclick=()=>this.newMotion(); const s=el.querySelector('[data-s]'); s.oninput=()=>{ this.share=+s.value; s.nextElementSibling.textContent=f(this.share,2); this.newMotion(); }; },
  make(G){ this.G=G; this.a=[1,.7,1.3]; this.share=.5; this.r=A.rng(212);
    const ax=[V3(2.4,0,0),V3(0,2.4,0),V3(0,0,2.4)]; ax.forEach((p,i)=>{ G.add(rod(V3(0,0,0),p,HEX.faint,.01,.7)); lab(G,`x${i+1}`,p.clone().multiplyScalar(1.08),'#93a3b5',.17); });
    // composition simplex at I = 1 (p_i = a_i x_i)
    const sv=this.a.map((w,i)=>{ const v=[0,0,0]; v[i]=1/w; return V3(v[0],v[2],v[1]).multiplyScalar(1.4); });
    G.add(face(sv,HEX.cyan,.12)); G.add(M.line([...sv,sv[0]],HEX.cyan,.6)); lab(G,'composition simplex (I fixed)',sv[1].clone().add(V3(0,.3,0)),'#63d3ff',.15);
    lab(G,'scale + composition',V3(3.0,-.3,1.6),'#f2c14e',.13); lab(G,'Fisher of amounts',V3(3.0,-.3,2.8),'#63ffb0',.13);
    this.dyn=new T.Group(); G.add(this.dyn); this.tr=M.trail(220,.08); G.add(this.tr); this.t=0; this.newMotion(); },
  newMotion(){ const r=this.r; this.x0=[.4+r(),.4+r(),.4+r()]; this.vs=this.share; this.w=[A.gauss(r),A.gauss(r),A.gauss(r)]; M.clearTrail(this.tr); this.t=0; },
  xt(t){ const g=Math.exp(.25*this.vs*Math.sin(t)), mix=this.w.map(w=>Math.exp((1-this.vs)*.35*w*Math.sin(.7*t))); return this.x0.map((x,i)=>x*g*mix[i]); },
  step(dt){ if(P.playing) this.t+=dt*.8; const x=this.xt(this.t), h=1e-5, xp=this.xt(this.t+h), dx=xp.map((v,i)=>(v-x[i])/h);
    const s=A.fisherSplit(x,this.a,dx); clear(this.dyn); const sc=1.4/s.I;
    const pt=V3(x[0],x[2],x[1]); const o=M.orb(.08,0xffffff); o.position.copy(pt); this.dyn.add(o); M.pushTrail(this.tr,pt,[.95,.75,.35]);
    const proj=V3(x[0]*sc,x[2]*sc,x[1]*sc); this.dyn.add(M.line([V3(0,0,0),pt],HEX.gold,.5)); const op=M.orb(.06,HEX.cyan); op.position.copy(proj); this.dyn.add(op);
    const hs=2/Math.max(s.lhs,1e-12); this.dyn.add(col(3.0,1.8,s.scale*hs,HEX.gold,.22)); this.dyn.add(col(3.0,1.8,s.comp*hs,HEX.cyan,.22,null,s.scale*hs)); this.dyn.add(col(3.0,2.6,2,HEX.green,.22,.55));
    return [['total I',f(s.I,4),''],['(d log I)²  scale',sci(s.scale),''],['Σ dp²/p  composition',sci(s.comp),''],['(1/I) Σ a dx²/x',sci(s.lhs),`scale + composition = ${sci(s.rhs)}`,Math.abs(s.lhs-s.rhs)<1e-9*Math.max(s.lhs,1e-12)]]; },
  check(){ const r=A.rng(12); let worst=0; for(let i=0;i<1000;i++){ const n=2+Math.floor(r()*6), x=Array.from({length:n},()=>.05+r()), a=Array.from({length:n},()=>.1+r()), dx=Array.from({length:n},()=>A.gauss(r)); const s=A.fisherSplit(x,a,dx); worst=Math.max(worst,Math.abs(s.lhs-s.rhs)/s.lhs); }
    let cbad=0; for(let i=0;i<500;i++){ const p=[r(),r(),r(),r()], sm=p.reduce((a,b)=>a+b,0); p.forEach((_,k)=>p[k]/=sm); const pd=[A.gauss(r),A.gauss(r),A.gauss(r),0]; pd[3]=-(pd[0]+pd[1]+pd[2]);
      const q=[p[0]+p[1],p[2]+p[3]], qd=[pd[0]+pd[1],pd[2]+pd[3]]; if(qd.reduce((s,v,k)=>s+v*v/q[k],0)>pd.reduce((s,v,k)=>s+v*v/p[k],0)+1e-12) cbad++; }
    return [['1000 random amounts: split identity',sci(worst),'0 (no cross term)',worst<1e-12],['500 merges of 4 → 2: Fisher speed increases',`${cbad} times`,'0',cbad===0]]; } });

/* ---------------------------------- B213 ---------------------------------- */
card({ id:'B213', route:[2,5], grade:'T',
  hero:'A closed curve drawn by rotating circles has two books, forward turning and backward turning: the signed area is their difference, and the activity, their sum, forgets which way the curve is traced.',
  eq:'z(t) = Σ_n c_n e^{i n t},   distinct integer n ≠ 0\nE₊ = Σ_{n>0} n |c_n|²,     E₋ = Σ_{n<0} |n| |c_n|²\nsigned area  ½∮ Im(z̄ dz) = π (E₊ − E₋)\nactivity  E₊ + E₋\nt → −t:  E₊ ↔ E₋,  area → −area,  activity unchanged',
  prose:'Draw a closed curve with a chain of rotating circles. Each circle contributes to the enclosed area in proportion to its frequency times its squared radius, positive when it turns forward and negative when it turns back, and circles of different frequencies never interfere in the area. So the area is the difference of two books and the total activity is their sum. Run the curve backwards and the books swap: the area changes sign and the activity does not notice.',
  carry:'A finite epicycle sum with distinct integer frequencies and complex radii c_n.',
  chk:'Integrate ½∮ Im(z̄ dz) along the drawn curve and compare with π(E₊ − E₋); reverse time and repeat.',
  arrive:'Area = π(E₊ − E₋); reversal swaps the books; activity is invariant.',
  closed:'E₊ = E₋ (zero signed area, a balanced curve), or a repeated frequency (two circles at one frequency must first be added as one, |c₁ + c₂|², or the per-circle sum is wrong).',
  links:{builds:'B184 (a fixed budget and a signed difference, the two halves of one product) · B199 (the orbit as a wall instance)',pairs:'B212',feeds:'B183 (the energy of the anti-parallel field)'},
  why:'Im(z̄ ż) = Σ_{m,n} n Re(c̄_m c_n e^{i(n−m)t}), and over a full turn every m ≠ n term averages to zero, leaving Σ n |c_n|². Half of 2π times that is π Σ n |c_n|², which splits by sign of n. Reversal sends n to −n.',
  view:[0,1.05,7.4,0],
  controls:()=>`<button data-rev aria-pressed="false">Reverse time</button><button data-new>New circles</button><button data-rep aria-pressed="false">Repeat a frequency</button>`,
  bind(el){ el.querySelector('[data-rev]').onclick=e=>{ this.rev=!this.rev; e.target.setAttribute('aria-pressed',this.rev); M.clearTrail(this.tr); this.build(); };
    el.querySelector('[data-new]').onclick=()=>{ this.seed++; this.rep=false; el.querySelector('[data-rep]').setAttribute('aria-pressed',false); this.build(); };
    el.querySelector('[data-rep]').onclick=e=>{ this.rep=!this.rep; e.target.setAttribute('aria-pressed',this.rep); this.build(); }; },
  make(G){ this.G=G; this.seed=0; this.rev=false; this.rep=false; this.t=0; this.dyn=new T.Group(); G.add(this.dyn); this.tr=M.trail(600,.06); G.add(this.tr); this.build(); },
  build(){ clear(this.dyn); M.clearTrail(this.tr);
    if(this.rep){ this.c=[[1,0],[.5,0]]; this.n=[2,2]; }
    else if(this.seed===0){ this.c=[[1,0],[.45,0],[.3,0]]; this.n=[1,-2,3]; }
    else { const r=A.rng(300+this.seed), pool=[-4,-3,-2,-1,1,2,3,4]; const k=2+Math.floor(r()*2), n=[]; while(n.length<k){ const v=pool[Math.floor(r()*pool.length)]; if(!n.includes(v)) n.push(v); }
      this.n=n; this.c=n.map((_,i)=>[i===0?1:.2+.4*r(),2*Math.PI*r()]); }
    if(this.rev) this.n=this.n.map(x=>-x);
    const pts=[]; for(let q=0;q<=400;q++){ const t=q/400*2*Math.PI; let x=0,y=0; this.c.forEach(([r,ph],j)=>{ x+=r*Math.cos(this.n[j]*t+ph); y+=r*Math.sin(this.n[j]*t+ph); }); pts.push(V3(x,0,-y)); }
    this.dyn.add(M.line(pts,0x9fb4ff,.75)); this.area=A.orbitArea(this.c,this.n); this.books=A.orbitBooks(this.c,this.n);
    // the two books as columns
    this.dyn.add(col(2.8,-.4,this.books.Ep*.9,HEX.cyan,.3)); this.dyn.add(col(2.8,.4,this.books.Em*.9,HEX.rose,.3));
    lab(this.dyn,'E₊',V3(2.8,this.books.Ep*.9+.25,-.4),'#63d3ff',.18); lab(this.dyn,'E₋',V3(2.8,this.books.Em*.9+.25,.4),'#ff6fae',.18);
    this.arm=new T.Group(); this.dyn.add(this.arm); },
  step(dt){ if(P.playing) this.t+=dt*.6; clear(this.arm); let x=0,y=0, prev=V3(0,0,0);
    this.c.forEach(([r,ph],j)=>{ const ctr=prev.clone(); const rg=ring(r,this.n[j]>0?HEX.cyan:HEX.rose,.35,0,48); rg.position.copy(ctr); this.arm.add(rg);
      x+=r*Math.cos(this.n[j]*this.t+ph); y+=r*Math.sin(this.n[j]*this.t+ph); const nx=V3(x,0,-y); this.arm.add(rod(prev,nx,this.n[j]>0?HEX.cyan:HEX.rose,.015)); prev=nx; });
    const tip=M.orb(.07,0xffffff); tip.position.copy(prev); this.arm.add(tip); M.pushTrail(this.tr,prev,[.95,.8,.35]);
    const b=this.books, naive=Math.PI*this.c.reduce((s,[r],j)=>s+this.n[j]*r*r,0);
    const rows=[['frequencies',this.n.join(', '),''],['E₊, E₋',`${f(b.Ep,5)}, ${f(b.Em,5)}`,''],['signed area (integrated)',f(this.area,8),this.rep?'π·2·|c₁+c₂|²':'π(E₊ − E₋)',this.rep?Math.abs(this.area-Math.PI*2*2.25)<1e-6:Math.abs(this.area-b.area)<1e-6],
      ['activity E₊ + E₋',f(b.activity,5),'unchanged by reversal',true]];
    if(this.rep) rows.push(['per-circle sum π Σ n r²',f(naive,6),'wrong when n repeats',Math.abs(naive-this.area)>1e-3]);
    return rows; },
  check(){ const r=A.rng(13); let worst=0; for(let i=0;i<200;i++){ const pool=[-6,-5,-4,-3,-2,-1,1,2,3,4,5,6], k=2+Math.floor(r()*4), n=[]; while(n.length<k){ const v=pool[Math.floor(r()*pool.length)]; if(!n.includes(v)) n.push(v); }
      const c=n.map(()=>[.1+r(),2*Math.PI*r()]); worst=Math.max(worst,Math.abs(A.orbitArea(c,n,2000)-A.orbitBooks(c,n).area)); }
    const c=[[1,0],[.45,0],[.3,0]], n=[1,-2,3], a=A.orbitArea(c,n), ar=A.orbitArea(c,n.map(x=>-x)), rep=A.orbitArea([[1,0],[.5,0]],[2,2]);
    return [['200 random epicycles: area − π(E₊ − E₋)',sci(worst),'0',worst<1e-9],['example (1, −2, 3): area',f(a,8),'π(1.27 − 0.405) = 2.71747765',Math.abs(a-2.7174776453551)<1e-9],['reversed',f(ar,8),'−2.71747765',Math.abs(ar+a)<1e-9],
      ['repeated frequency 2, radii 1 and ½',`${f(rep,6)} vs ${f(Math.PI*2*1.25,6)}`,'14.137167 ≠ per-circle 7.853982',Math.abs(rep-14.137166941)<1e-6]]; } });

/* =====================================================================================================
   BUILD THE PAGE
   ===================================================================================================== */
const esc=t=>String(t).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const gradeChip=g=>`<span class="chip g-${g}"><b>${g}</b>${GRADE[g]}</span>`;
const ACTS=[['Offsets and the self-dual mode','B204','B205'],['Overlaps, edges and the doubled slice','B206','B207'],['What the present keeps','B208','B209'],['What it costs to move','B210','B211'],['Two books in amount and in orbit','B212','B213']];
function buildPanels(){ const host=$('acts'); const byId={}; CARDS.forEach(c=>byId[c.id]=c);
  ACTS.forEach(([name,...ids])=>{ const act=document.createElement('div'); act.className='act'; act.innerHTML=`<h3>${ids.join(' · ')} — ${name}</h3><div class="grid"></div>`; host.append(act); const grid=act.querySelector('.grid');
    ids.forEach(id=>{ const c=byId[id]; const p=document.createElement('article'); p.className='panel'; p.id=id;
      p.innerHTML=`<div class="ph"><div class="row1"><span class="num">${c.id}</span><span class="route">L${c.route[0]} → L${c.route[1]} · ${STRATA[c.route[0]].slice(3)} to ${STRATA[c.route[1]].slice(3)}</span>${gradeChip(c.grade)}</div>
        <div class="hero-line">${esc(c.hero)}</div><div class="eqn">${esc(c.eq)}</div><p class="prose">${esc(c.prose)}</p></div>
        <div class="pv" aria-label="3D view: ${c.id}. Drag to turn, double-click to reset."><div class="vtools"><button data-reset>Reset view</button></div><span class="hint">drag to turn · click, then scroll to zoom</span></div>
        <div class="pf"><div class="ectl">${c.controls?c.controls():''}</div>
          <table class="ro"><thead><tr><th>quantity</th><th>eye</th><th>card</th></tr></thead><tbody></tbody></table>
          <div class="cross"><div><b>Carry</b>${esc(c.carry)}</div><div><b>Check</b>${esc(c.chk)}</div><div><b>Arrive</b>${esc(c.arrive)}</div><div><b>Closed when</b>${esc(c.closed)}</div></div>
          <div class="links"><div><span>builds on</span>${esc(c.links.builds)}</div><div><span>pairs with</span>${esc(c.links.pairs)}</div><div><span>feeds</span>${esc(c.links.feeds)}</div></div>
          <div class="why"><b>Why it holds</b>${esc(c.why)}</div>
          <div class="status" data-status>Readout check not run yet.</div></div>`;
      grid.append(p); const pv=p.querySelector('.pv'); c.view_=makeView(pv,c.view,{spin:c.spin}); c.tbody=p.querySelector('tbody'); c.status=p.querySelector('[data-status]'); c.panel=p;
      p.querySelector('[data-reset]').onclick=()=>{ const v=c.view_; v.V.yaw=v.home[0]; v.V.pitch=v.home[1]; v.V.dist=v.home[2]; v.V.ty=v.home[3]||0; v.V.auto=true; };
      c.make(c.view_.G,c.view_); if(c.bind) c.bind(p.querySelector('.pf')); }); }); }
function renderRows(c,rows){ if(!rows) return; c.tbody.innerHTML=rows.map(([q,v,pp,ok])=>{ const cls=ok===true?'hit':ok===false?'miss':''; return `<tr><td>${q}</td><td class="${cls}">${v}</td><td class="p">${pp||''}</td></tr>`; }).join(''); }

/* ---------- hero: the eight strata on a ring, the ten bridges as glowing arcs ---------- */
const hero={sel:0};
function buildHero(){ const v=makeView($('heroVp'),[0.2,0.62,24,-0.7],{fov:38}); hero.v=v; v.spin=.5;
  const star=M.points(1600,.07); const r=A.rng(5); for(let i=0;i<1600;i++){ const R=12+r()*30, t=r()*2*Math.PI, z=Math.acos(2*r()-1); M.setPt(star,i,V3(R*Math.sin(z)*Math.cos(t),R*Math.cos(z),R*Math.sin(z)*Math.sin(t)),M.colour.ramp(r()).map(x=>x*.3)); } M.flush(star); v.scene.add(star);
  const G=v.G, RR=2.6; hero.pos=STRATA.map((_,i)=>{ const a=Math.PI/2-i/8*2*Math.PI; return V3(RR*Math.cos(a),0,-RR*Math.sin(a)); });
  G.add(ring(RR,HEX.faint,.35,0,128));
  hero.pos.forEach((p,i)=>{ const o=M.orb(.13,[HEX.gold,HEX.cyan,HEX.violet,HEX.rose,HEX.green,HEX.coral,0x9fb4ff,0xdfe7ef][i]); o.position.copy(p); G.add(o); lab(G,STRATA[i],p.clone().multiplyScalar(1.22).add(V3(0,.18,0)),'#b8c6d6',.13); });
  hero.arcs=CARDS.map((c,k)=>{ const [a,b]=c.route; const p=hero.pos[a], q=hero.pos[b]; const pts=a===b?curve(u=>p.clone().add(V3(.5*Math.sin(2*Math.PI*u),.9*Math.sin(Math.PI*u),.5*(1-Math.cos(2*Math.PI*u)))),40):arcPts(p,q,1.1+.12*k,48);
    const col=c.grade==='T'?HEX.cyan:c.grade==='V'?HEX.gold:HEX.violet; const ln=M.line(pts,col,.55); G.add(ln); const fl=M.points(10,.13); G.add(fl); return {pts,ln,fl,col,c}; });
  const tabs=$('tabs'); CARDS.forEach((c,k)=>{ const b=document.createElement('button'); b.textContent=c.id; b.setAttribute('aria-pressed',k===0); b.onclick=()=>{ hero.sel=k; selectHero(); }; tabs.append(b); });
  $('sCards').textContent=CARDS.length; $('sT').textContent=CARDS.filter(c=>c.grade==='T').length; $('sV').textContent=CARDS.filter(c=>c.grade==='V').length; $('sH').textContent=CARDS.filter(c=>c.grade==='H').length;
  $('sJoins').textContent=new Set(CARDS.map(c=>c.route.slice().sort().join('-'))).size; selectHero(); }
function selectHero(){ const c=CARDS[hero.sel]; document.querySelectorAll('#tabs button').forEach((b,i)=>b.setAttribute('aria-pressed',i===hero.sel));
  hero.arcs.forEach((a,i)=>{ a.ln.material.opacity=i===hero.sel?1:.25; });
  $('callout').innerHTML=`<span class="rt">${c.id} · L${c.route[0]} → L${c.route[1]} · ${GRADE[c.grade]}</span><b>${esc(c.hero)}</b><a href="#${c.id}">open the card ↓</a>`; }
let heroT=0, heroAuto=0, dive=0;
function heroTick(dt){ heroT+=dt; if(dive<1){ dive=Math.min(1,dive+dt/3); hero.v.V.dist=24-(24-9.6)*(1-Math.pow(1-dive,3)); }
  heroAuto+=dt; if(heroAuto>6&&P.playing){ heroAuto=0; hero.sel=(hero.sel+1)%CARDS.length; selectHero(); }
  hero.arcs.forEach((a,i)=>{ const c=RGB(a.col).map(x=>x*(i===hero.sel?1:.35)); for(let q=0;q<10;q++){ const u=((heroT*.25+q/10)%1); M.setPt(a.fl,q,a.pts[Math.floor(u*(a.pts.length-1))],c); } M.flush(a.fl); }); }

/* ---------- strip, check, film ---------- */
function runCheck(){ let pass=0,total=0; $('checkSummary').textContent='checking…';
  setTimeout(()=>{ CARDS.forEach(c=>{ const rows=c.check(); let ok=0; rows.forEach(r=>{ if(r[3]) ok++; }); total+=rows.length; pass+=ok;
      c.status.className='status '+(ok===rows.length?'ok':'bad'); c.status.innerHTML=`Readout check: ${ok}/${rows.length} eye values equal the card’s. `+rows.map(r=>`${r[0]}: ${r[1]} (card ${r[2]})`).join(' · '); });
    $('checkSummary').textContent=`${pass}/${total} readouts equal the cards’ numbers, ${CARDS.length} cards`; $('checkSummary').className=pass===total?'ok':''; window.ATLAS3D_CHECK={pass,total}; },30); }
const film={on:false,i:-1,t:99};
function filmTick(dt){ if(!film.on) return; film.t+=dt; if(film.t<9) return; film.t=0; film.i=(film.i+1)%CARDS.length; CARDS[film.i].panel.scrollIntoView({behavior:still?'auto':'smooth',block:'center'}); }
function bindStrip(){ $('play').onclick=()=>{ P.playing=!P.playing; $('play').textContent=P.playing?'Pause':'Play'; $('play').setAttribute('aria-pressed',!P.playing); }; $('play').textContent=P.playing?'Pause':'Play';
  $('fs').oninput=e=>{ P.speed=+e.target.value; $('fso').textContent=e.target.value+'×'; };
  $('check').onclick=runCheck; $('clean').onclick=()=>{ const on=!document.body.classList.contains('clean'); document.body.classList.toggle('clean',on); $('clean').setAttribute('aria-pressed',on); };
  $('film').onclick=()=>{ film.on=!film.on; $('film').setAttribute('aria-pressed',film.on); film.i=-1; film.t=99; }; }

/* ---------- go ---------- */
buildHero(); buildPanels(); bindStrip();
$('share').onclick=async()=>{ const url=location.href.split('#')[0]; try{ if(navigator.share) await navigator.share({title:document.title,url}); else { await navigator.clipboard.writeText(url); $('share').textContent='Link copied'; setTimeout(()=>$('share').textContent='Share',1500); } }catch(e){} };
let last=performance.now(), readT=0;
function frame(now){ const raw=Math.max(0,Math.min(.05,(now-last)/1000)); last=now; const dt=P.playing?raw*P.speed:0;
  const W=window.innerWidth,H=window.innerHeight; const cv=R.domElement; if(cv.width!==Math.floor(W*R.getPixelRatio())||cv.height!==Math.floor(H*R.getPixelRatio())) R.setSize(W,H,false);
  R.setScissorTest(false); R.clear(); R.setScissorTest(true); readT+=raw; const doRead=readT>.15; if(doRead) readT=0;
  for(const v of views){ const r=v.el.getBoundingClientRect(); v.visible=r.bottom>0&&r.top<H&&r.width>0&&r.height>0; if(!v.visible) continue;
    if(v.V.auto&&P.playing&&!still) v.V.yaw+=raw*.07*(v.spin||1);
    const D=v.V.dist; v.cam.position.set(D*Math.cos(v.V.pitch)*Math.sin(v.V.yaw),v.V.ty+D*Math.sin(v.V.pitch),D*Math.cos(v.V.pitch)*Math.cos(v.V.yaw)); v.cam.lookAt(0,v.V.ty,0);
    v.cam.aspect=r.width/r.height; if(v===hero.v){ const wide=window.innerWidth>900; v.cam.setViewOffset(r.width,r.height,wide?-r.width*.06:0,0,r.width,r.height); } v.cam.updateProjectionMatrix();
    if(v===hero.v) heroTick(dt); else { const c=CARDS.find(x=>x.view_===v); const rows=c.step(dt); if(doRead) renderRows(c,rows); }
    R.setViewport(r.left,H-r.bottom,r.width,r.height); R.setScissor(r.left,Math.max(0,H-r.bottom),r.width,r.height); R.render(v.scene,v.cam); }
  filmTick(raw); requestAnimationFrame(frame); }
requestAnimationFrame(frame);
window.ATLAS3D_APP={CARDS,P,runCheck,views,hero};
})();

