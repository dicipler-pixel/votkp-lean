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
