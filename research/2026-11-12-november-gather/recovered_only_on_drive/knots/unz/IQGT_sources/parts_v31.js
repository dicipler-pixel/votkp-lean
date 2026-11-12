/* SCRIPT: mixer3d_parts_v3
   3D Mixer Parts v3 — Jeromie Beasley — 28 Oct 2026
   Shared 3D parts and the Atlas Memoriae layout. Two views of the same eyes:
   the Explainer (one scrolling page of panels, each with its own live 3D window, a sticky control strip,
   a grade legend and a self-test that checks every eye against the paper's numbers) and the Stage
   (one eye full screen for the video: film order, overlay for screen blending, record, clean view, PNG).
   Each eye has its own scene, camera and parameters. This is NOT a mixer: each paper's mixer writes
   its own eyes from its own physics on these parts. ES module, three r158 from the import map. */
import * as THREE from 'three';
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';
import { OutputPass } from 'three/addons/postprocessing/OutputPass.js';
const T = THREE;

/* ---------- palette (one meaning per colour, shared by every eye) ---------- */
const PAL = { metric:0x5ab0ff, twist:0xb18cff, gap:0xffb547, tail:0x4fe3c1, tip:0xff6f91, ink:0xe8eefb, dim:0x93a3c0, faint:0x3b4a66 };
const hex = c => '#' + c.toString(16).padStart(6, '0');
const rgb = c => [((c>>16)&255)/255, ((c>>8)&255)/255, (c&255)/255];

/* ---------- glow parts ---------- */
const sprite = (() => { const c = document.createElement('canvas'); c.width = c.height = 64; const x = c.getContext('2d');
  const g = x.createRadialGradient(32,32,0,32,32,32); g.addColorStop(0,'rgba(255,255,255,1)'); g.addColorStop(0.22,'rgba(255,255,255,.7)'); g.addColorStop(1,'rgba(255,255,255,0)');
  x.fillStyle = g; x.fillRect(0,0,64,64); const t = new T.CanvasTexture(c); return t; })();
const glowMat = size => new T.PointsMaterial({size, map:sprite, transparent:true, depthWrite:false, blending:T.AdditiveBlending, vertexColors:true, sizeAttenuation:true});
function points(n, size){ const geo = new T.BufferGeometry(); geo.setAttribute('position', new T.BufferAttribute(new Float32Array(n*3),3)); geo.setAttribute('color', new T.BufferAttribute(new Float32Array(n*3),3)); const p = new T.Points(geo, glowMat(size)); p.frustumCulled = false; return p; }
function setPt(p, i, P, c){ const a = p.geometry.attributes; a.position.setXYZ(i, P.x, P.y, P.z); if(c) a.color.setXYZ(i, c[0], c[1], c[2]); }
function flush(p){ const a = p.geometry.attributes; a.position.needsUpdate = true; a.color.needsUpdate = true; }
function line(pts, color, opacity){ const geo = new T.BufferGeometry().setFromPoints(pts.length ? pts : [new T.Vector3(), new T.Vector3()]); const l = new T.Line(geo, new T.LineBasicMaterial({color, transparent:true, opacity:opacity==null?1:opacity, depthWrite:false})); l.frustumCulled = false; return l; }
function setLine(l, pts){ l.geometry.dispose(); l.geometry = new T.BufferGeometry().setFromPoints(pts.length ? pts : [new T.Vector3(), new T.Vector3()]); }
function dashed(pts, color, opacity){ const l = new T.Line(new T.BufferGeometry().setFromPoints(pts), new T.LineDashedMaterial({color, dashSize:0.06, gapSize:0.05, transparent:true, opacity:opacity==null?0.7:opacity, depthWrite:false})); l.computeLineDistances(); l.frustumCulled = false; return l; }
function setDashed(l, pts){ l.geometry.dispose(); l.geometry = new T.BufferGeometry().setFromPoints(pts); l.computeLineDistances(); }
/* glowing tube along a polyline (for the curves that carry the argument) */
function tube(pts, r, color, opacity){ const m = new T.Mesh(tubeGeo(pts, r), new T.MeshBasicMaterial({color, transparent:true, opacity:opacity==null?1:opacity, depthWrite:false, blending:T.AdditiveBlending})); m.userData.r = r; m.frustumCulled = false; return m; }
function tubeGeo(pts, r){ if(pts.length < 2) pts = [new T.Vector3(), new T.Vector3(0,1e-4,0)]; const c = new T.CatmullRomCurve3(pts, false, 'centripetal'); return new T.TubeGeometry(c, Math.min(600, pts.length*2), r, 8, false); }
function setTube(m, pts){ m.geometry.dispose(); m.geometry = tubeGeo(pts, m.userData.r); }
function orb(r, color, glow){ const g = new T.Group(); const core = new T.Mesh(new T.SphereGeometry(r, 24, 16), new T.MeshBasicMaterial({color}));
  const halo = new T.Sprite(new T.SpriteMaterial({map:sprite, color, transparent:true, depthWrite:false, blending:T.AdditiveBlending, opacity:0.9}));
  halo.scale.setScalar(r*(glow||7)); g.add(core); g.add(halo); g.userData = {core, halo}; return g; }
function paintOrb(o, color){ o.userData.core.material.color.set(color); o.userData.halo.material.color.set(color); }
/* rim-lit glass sphere: bright at the silhouette, clear in the middle */
function glass(r, color, power, opacity){ const mat = new T.ShaderMaterial({ transparent:true, depthWrite:false, blending:T.AdditiveBlending, side:T.FrontSide,
  uniforms:{ c:{value:new T.Color(color)}, p:{value:power||2.6}, o:{value:opacity==null?0.55:opacity} },
  vertexShader:'varying vec3 vN; varying vec3 vV; void main(){ vec4 mv = modelViewMatrix*vec4(position,1.0); vN = normalize(normalMatrix*normal); vV = normalize(-mv.xyz); gl_Position = projectionMatrix*mv; }',
  fragmentShader:'uniform vec3 c; uniform float p; uniform float o; varying vec3 vN; varying vec3 vV; void main(){ float f = pow(1.0-abs(dot(vN,vV)), p); gl_FragColor = vec4(c*f*o, f*o); }' });
  return new T.Mesh(new T.SphereGeometry(r, 64, 48), mat); }
function ring(r, color, w, opacity){ const m = new T.Mesh(new T.TorusGeometry(r, w||0.006, 8, 160), new T.MeshBasicMaterial({color, transparent:true, opacity:opacity==null?0.8:opacity, depthWrite:false, blending:T.AdditiveBlending})); return m; }
function arrow(color, len, head){ const g = new T.Group(); const mat = new T.MeshBasicMaterial({color, transparent:true, opacity:0.95, depthWrite:false});
  const shaft = new T.Mesh(new T.CylinderGeometry(0.012, 0.012, 1, 10), mat); const tip = new T.Mesh(new T.ConeGeometry(0.045, head||0.14, 16), mat);
  g.add(shaft); g.add(tip); g.userData = {shaft, tip, head:head||0.14}; setArrow(g, new T.Vector3(), new T.Vector3(0,len||1,0)); return g; }
function setArrow(a, from, vec){ const L = vec.length(), u = a.userData, h = Math.min(u.head, L*0.45); const dir = L > 1e-9 ? vec.clone().divideScalar(L) : new T.Vector3(0,1,0);
  a.position.copy(from); a.quaternion.setFromUnitVectors(new T.Vector3(0,1,0), dir);
  u.shaft.scale.set(1, Math.max(1e-4, L-h), 1); u.shaft.position.set(0, (L-h)/2, 0); u.tip.position.set(0, L-h/2, 0); u.tip.scale.setScalar(L > 1e-6 ? 1 : 1e-4); a.visible = L > 1e-6; }
function bar(w, d, color){ const m = new T.Mesh(new T.BoxGeometry(w, 1, d), new T.MeshStandardMaterial({color, emissive:color, emissiveIntensity:0.3, roughness:0.45, metalness:0.1, transparent:true, opacity:0.9}));
  m.geometry.translate(0, 0.5, 0); return m; }
function setBar(m, h){ m.scale.y = Math.max(1e-3, h); }
function slab(w, h, d, color, opacity){ return new T.Mesh(new T.BoxGeometry(w, h, d), new T.MeshBasicMaterial({color, transparent:true, opacity:opacity==null?0.12:opacity, depthWrite:false, blending:T.AdditiveBlending})); }
function grid(size, n, color, opacity){ const pts = []; const h = size/2; for(let i=0;i<=n;i++){ const t = -h + size*i/n; pts.push(new T.Vector3(t,0,-h), new T.Vector3(t,0,h), new T.Vector3(-h,0,t), new T.Vector3(h,0,t)); }
  return new T.LineSegments(new T.BufferGeometry().setFromPoints(pts), new T.LineBasicMaterial({color, transparent:true, opacity, depthWrite:false})); }
function trail(n, size){ const p = points(n, size); p.userData = {n, i:0, filled:0}; return p; }
function pushTrail(p, P, c){ const u = p.userData, a = p.geometry.attributes;
  a.position.setXYZ(u.i, P.x, P.y, P.z); u.i = (u.i+1) % u.n; u.filled = Math.min(u.n, u.filled+1);
  for(let k=0;k<u.n;k++){ const age = ((u.i - 1 - k) % u.n + u.n) % u.n; const f = k < u.filled ? Math.pow(1 - age/u.n, 1.6)*0.9 : 0; a.color.setXYZ(k, c[0]*f, c[1]*f, c[2]*f); }
  a.position.needsUpdate = a.color.needsUpdate = true; }
function clearTrail(p){ p.userData.i = 0; p.userData.filled = 0; const a = p.geometry.attributes; a.color.array.fill(0); a.color.needsUpdate = true; }
/* terrain: height H(a,b) and colour C(a,b) over an N x M grid spanning x in [x0,x1], z in [z0,z1] */
function surface(N, M, x0, x1, z0, z1, opacity){ const geo = new T.PlaneGeometry(1, 1, N-1, M-1); geo.rotateX(-Math.PI/2);
  geo.setAttribute('color', new T.BufferAttribute(new Float32Array(N*M*3),3));
  const mesh = new T.Mesh(geo, new T.MeshStandardMaterial({vertexColors:true, roughness:0.6, metalness:0.0, side:T.DoubleSide, transparent:true, opacity:opacity==null?0.78:opacity, depthWrite:false}));
  const wire = new T.LineSegments(new T.WireframeGeometry(geo), new T.LineBasicMaterial({color:0x5ab0ff, transparent:true, opacity:0.07, depthWrite:false}));
  const grp = new T.Group(); grp.add(mesh); grp.add(wire); grp.userData = {N, M, x0, x1, z0, z1, geo, wire}; return grp; }
function setSurface(s, H, C){ const u = s.userData, pos = u.geo.attributes.position, col = u.geo.attributes.color;
  for(let b=0;b<u.M;b++) for(let a=0;a<u.N;a++){ const i = b*u.N + a; const x = u.x0 + (u.x1-u.x0)*a/(u.N-1), z = u.z0 + (u.z1-u.z0)*b/(u.M-1);
    pos.setXYZ(i, x, H(a,b), z); const c = C(a,b); col.setXYZ(i, c[0], c[1], c[2]); }
  pos.needsUpdate = col.needsUpdate = true; u.geo.computeVertexNormals(); u.geo.computeBoundingSphere();
  u.wire.geometry.dispose(); u.wire.geometry = new T.WireframeGeometry(u.geo); }
/* floating label, always facing the camera */
function label(text, color, scale){ const c = document.createElement('canvas'), x = c.getContext('2d'), f = 46;
  const font = `500 ${f}px "Instrument Sans",system-ui,sans-serif`; x.font = font; const w = Math.ceil(x.measureText(text).width) + 28; c.width = w; c.height = f + 22;
  x.font = font; x.fillStyle = color || '#c9d6ec'; x.textBaseline = 'middle'; x.fillText(text, 14, c.height/2);
  const tex = new T.CanvasTexture(c); tex.colorSpace = T.SRGBColorSpace; tex.anisotropy = 4;
  const s = new T.Sprite(new T.SpriteMaterial({map:tex, transparent:true, depthWrite:false, depthTest:false}));
  const k = 0.8*(scale || 0.3) / f; s.scale.set(w*k, c.height*k, 1); s.renderOrder = 10; s.userData.text = text; s.userData.scale = scale; return s; }
/* a faint shell of glowing dust around a sphere (the sky the state lives on) */
function dust(n, r0, r1, color, size, seed){ const p = points(n, size || 0.05), c = rgb(color == null ? 0x5ab0ff : color); let a = (seed || 7) >>> 0; const rnd = () => { a = (a*1664525 + 1013904223) >>> 0; return a/4294967296; };
  for(let i=0;i<n;i++){ const u = rnd()*2-1, ph = rnd()*Math.PI*2, R = r0 + (r1-r0)*rnd()**2, s = Math.sqrt(1-u*u), b = 0.25 + 0.75*rnd()**3;
    setPt(p, i, new T.Vector3(R*s*Math.cos(ph), R*u, R*s*Math.sin(ph)), [c[0]*b, c[1]*b, c[2]*b]); } flush(p); return p; }
function relabel(s, text, color){ if(s.userData.text === text) return; const n = label(text, color, s.userData.scale); s.material.map.dispose(); s.material.map = n.material.map; s.scale.copy(n.scale); s.userData.text = text; }

/* ---------- engine: one renderer, one scene per eye ----------
   Stage view: the current eye fills the screen, with bloom (for the video).
   Explainer view: every eye is a panel in one scrolling page; the canvas sits over the page,
   ignores the pointer, and each visible panel's scene is drawn into that panel's window. */
function engine(canvas){
  const renderer = new T.WebGLRenderer({canvas, antialias:true, alpha:true, preserveDrawingBuffer:true, powerPreference:'high-performance'});
  renderer.setPixelRatio(Math.min(2, window.devicePixelRatio||1)); renderer.toneMapping = T.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.05;
  renderer.setClearColor(0x000000, 0);
  const stars = points(1800, 0.22); { const a = stars.geometry.attributes; for(let i=0;i<1800;i++){ const u = Math.random()*2-1, ph = Math.random()*Math.PI*2, R = 70+Math.random()*60, s = Math.sqrt(1-u*u);
    a.position.setXYZ(i, R*s*Math.cos(ph), R*u, R*s*Math.sin(ph)); const b = 0.25+0.55*Math.random()**3, t = Math.random(); a.color.setXYZ(i, b*(0.75+0.25*t), b*0.85, b); } flush(stars); }
  stars.material.fog = false;
  const composer = new EffectComposer(renderer); const rp = new RenderPass(new T.Scene(), new T.PerspectiveCamera()); composer.addPass(rp);
  const bloom = new UnrealBloomPass(new T.Vector2(512, 512), 0.6, 0.45, 0.3); composer.addPass(bloom); composer.addPass(new OutputPass());
  function sceneFor(){ const s = new T.Scene(); s.background = new T.Color(0x03060c); s.fog = new T.FogExp2(0x03060c, 0.018);
    s.add(new T.AmbientLight(0x9fb4d8, 0.55)); const key = new T.DirectionalLight(0xffffff, 1.1); key.position.set(3,6,4); s.add(key);
    const rim = new T.DirectionalLight(0x6f8cff, 0.6); rim.position.set(-5,-2,-4); s.add(rim); return s; }
  function place(cam, V, aspect, mobile){ const D = V.dist*(mobile ? 1.3 : 1);
    cam.position.set(D*Math.cos(V.pitch)*Math.sin(V.yaw), V.ty + D*Math.sin(V.pitch), D*Math.cos(V.pitch)*Math.cos(V.yaw)); cam.lookAt(0, V.ty, 0);
    if(Math.abs(cam.aspect - aspect) > 1e-4){ cam.aspect = aspect; cam.updateProjectionMatrix(); } }
  return { renderer, stars, composer, rp, bloom, sceneFor, place };
}
/* orbit control on any element, writing into a view state V = {yaw, pitch, dist, ty, auto} */
function orbit(el, getV, wheelNeedsKey){
  const ptrs = new Map(); let pinch0 = 0, dist0 = 0;
  el.addEventListener('pointerdown', e => { if(e.button > 0) return; el.setPointerCapture(e.pointerId); ptrs.set(e.pointerId, {x:e.clientX, y:e.clientY}); const V = getV(); if(V) V.auto = false;
    if(ptrs.size === 2){ const [a,b] = [...ptrs.values()]; pinch0 = Math.hypot(a.x-b.x, a.y-b.y); dist0 = V ? V.dist : 0; } });
  el.addEventListener('pointermove', e => { if(!ptrs.has(e.pointerId)) return; const p = ptrs.get(e.pointerId), V = getV(); if(!V) return;
    if(ptrs.size === 1){ V.yaw -= (e.clientX - p.x)*0.006; V.pitch = Math.max(-1.35, Math.min(1.35, V.pitch + (e.clientY - p.y)*0.006)); }
    p.x = e.clientX; p.y = e.clientY;
    if(ptrs.size === 2){ const [a,b] = [...ptrs.values()]; const d = Math.hypot(a.x-b.x, a.y-b.y); if(pinch0) V.dist = Math.max(2.2, Math.min(30, dist0*pinch0/d)); } });
  ['pointerup','pointercancel'].forEach(t => el.addEventListener(t, e => { ptrs.delete(e.pointerId); if(ptrs.size < 2) pinch0 = 0; }));
  el.addEventListener('wheel', e => { if(wheelNeedsKey && !(e.ctrlKey || e.metaKey || e.altKey)) return; e.preventDefault(); const V = getV(); if(V) V.dist = Math.max(2.2, Math.min(30, V.dist*Math.exp(e.deltaY*0.001))); }, {passive:false});
}

/* ---------- the Atlas Memoriae layout ---------- */
const CSS = `
:root{--void:#03060c;--page:#050a14;--panel:rgba(12,19,35,.72);--panel2:#08101f;--glass:rgba(9,14,27,.7);--edge:rgba(150,185,255,.12);--edge2:rgba(150,185,255,.24);
--ink:#e8eefb;--dim:#97a6c2;--faint:#5b6a86;--metric:#5ab0ff;--twist:#b18cff;--gap:#ffb547;--tail:#4fe3c1;--tip:#ff6f91;
--ui:"Instrument Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--math:"STIX Two Text","Cambria Math","Times New Roman",serif;
--rail:236px;--card:372px;--bar:64px;color-scheme:dark}
*{box-sizing:border-box}html,body{height:100%}
body{margin:0;background:var(--page);color:var(--ink);font-family:var(--ui);font-size:14px;line-height:1.5;overflow:hidden;-webkit-font-smoothing:antialiased;font-variant-numeric:tabular-nums}
#gl{position:fixed;inset:0;width:100%;height:100%;display:block;z-index:6;pointer-events:none}
body.stage #gl{z-index:0;pointer-events:auto;touch-action:none;cursor:grab}body.stage #gl:active{cursor:grabbing}
button{font:inherit;color:inherit;background:none;border:0;cursor:pointer;padding:0}
a{color:inherit}
:focus-visible{outline:2px solid var(--metric);outline-offset:2px;border-radius:6px}
.glass{background:var(--glass);border:1px solid var(--edge);backdrop-filter:blur(18px) saturate(1.2);-webkit-backdrop-filter:blur(18px) saturate(1.2);border-radius:14px}
/* the navigation pill, shared by both views */
.pill{position:fixed;top:12px;left:50%;transform:translateX(-50%);z-index:20;display:flex;align-items:center;gap:4px;padding:5px;border-radius:99px;white-space:nowrap;background:#070c18}
.pill .brand{font-family:var(--math);font-size:15px;padding:4px 12px 4px 10px;text-decoration:none;color:var(--ink)}
.pill .sep{width:1px;height:20px;background:var(--edge2);margin:0 4px}
.pill button,.pill a.b{padding:6px 12px;border-radius:99px;font-size:13px;color:var(--dim);text-decoration:none}
.pill button:hover,.pill a.b:hover{color:var(--ink);background:rgba(150,185,255,.08)}
.pill button[aria-pressed=true]{color:var(--ink);background:rgba(90,176,255,.18)}
/* ===== Explainer view ===== */
#ex{position:fixed;inset:0;overflow-y:auto;overflow-x:hidden;z-index:1;scroll-behavior:smooth;scrollbar-width:thin}
body.stage #ex{display:none}
.ex-in{max-width:1240px;margin:0 auto;padding:88px 24px 120px}
.hero h1{font-family:var(--math);font-weight:400;font-size:clamp(34px,5vw,58px);line-height:1.02;letter-spacing:-.01em;margin:0}
.hero .sub{font-size:16px;color:var(--dim);margin:12px 0 0;max-width:68ch}
.hero .by{font-size:13px;color:var(--faint);margin-top:8px}
.legend{display:flex;flex-wrap:wrap;gap:6px;margin-top:18px}
.chip{display:inline-flex;align-items:center;gap:6px;padding:2px 9px;border-radius:99px;border:1px solid var(--edge2);font-size:12px;color:var(--ink);white-space:nowrap}
.chip[data-g=proved]{border-color:rgba(79,227,193,.5);color:var(--tail)}.chip[data-g=data]{border-color:rgba(255,181,71,.5);color:var(--gap)}
.chip[data-g=structural]{border-color:rgba(255,111,145,.5);color:var(--tip)}.chip[data-g=computed]{border-color:rgba(90,176,255,.5);color:var(--metric)}
.chip[data-g=known]{border-color:rgba(177,140,255,.5);color:var(--twist)}.chip[data-g=open]{border-color:rgba(150,170,200,.45);color:var(--dim);border-style:dashed}
.strip{position:sticky;top:64px;z-index:5;background:#070c18;margin:26px 0 8px;display:flex;flex-wrap:wrap;align-items:center;gap:10px 16px;padding:10px 14px}
.strip label{display:flex;align-items:center;gap:10px;font-size:13px;color:var(--dim)}.strip label output{color:var(--ink);min-width:3.5ch}
.strip input[type=range]{width:120px}
.strip .grow{flex:1}
.act-h{display:flex;align-items:baseline;gap:14px;margin:46px 0 14px}
.act-h h2{font-family:var(--math);font-style:italic;font-weight:400;font-size:26px;margin:0;color:var(--ink)}
.act-h .gapmark{flex:1;height:1px;background:linear-gradient(90deg,var(--gap),transparent);opacity:.45}
.panels{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}
.pn{background:var(--panel);border:1px solid var(--edge);border-radius:16px;padding:16px;display:grid;gap:10px;align-content:start;min-width:0}
.pn.wide{grid-column:1/-1}.pn.wide .vp{aspect-ratio:21/9}@media (max-width:860px){.pn.wide .vp{aspect-ratio:16/10}}
.pn-h{display:flex;align-items:baseline;justify-content:space-between;gap:10px}
.pn-h h3{margin:0;font-size:17.5px;font-weight:600;letter-spacing:-.005em}.pn-h h3 b{font-weight:500;color:var(--faint);margin-right:8px;font-size:14px}
.pn .eq{font-family:var(--math);font-size:17px;line-height:1.45;color:#f4f7ff;white-space:pre-wrap}
.pn p{margin:0;color:var(--dim);font-size:13.5px;line-height:1.55}
.vp{position:relative;aspect-ratio:16/10;border-radius:12px;overflow:hidden;background:#060b16;border:1px solid var(--edge);touch-action:pan-y;cursor:grab}
.vp:active{cursor:grabbing}
.vrow{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-top:-2px;font-size:12px;color:var(--faint)}
.vrow .open{white-space:nowrap;flex:none;padding:4px 11px;border-radius:99px;font-size:12px;color:var(--dim);border:1px solid var(--edge)}
.vrow .open:hover{color:var(--ink);border-color:var(--edge2)}
/* shared control and readout styles */
.ctl{display:grid;gap:10px}
.ctl label{display:grid;grid-template-columns:1fr auto;gap:4px 8px;font-size:12.5px;color:var(--dim)}
.ctl output{color:var(--ink)}
input[type=range]{grid-column:1/-1;width:100%;height:18px;margin:0;background:none;-webkit-appearance:none;appearance:none}
input[type=range]::-webkit-slider-runnable-track{height:3px;border-radius:3px;background:linear-gradient(90deg,var(--metric) var(--f,50%),rgba(150,185,255,.18) var(--f,50%))}
input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:14px;height:14px;border-radius:50%;background:#fff;margin-top:-5.5px;box-shadow:0 0 0 4px rgba(90,176,255,.25)}
input[type=range]::-moz-range-track{height:3px;border-radius:3px;background:rgba(150,185,255,.18)}input[type=range]::-moz-range-progress{height:3px;background:var(--metric);border-radius:3px}
input[type=range]::-moz-range-thumb{width:14px;height:14px;border:0;border-radius:50%;background:#fff}
.seg{display:flex;flex-wrap:wrap;gap:4px;padding:3px;border-radius:10px;background:rgba(150,185,255,.06);border:1px solid var(--edge)}
.seg button{flex:1 1 auto;padding:5px 10px;border-radius:7px;font-size:12.5px;color:var(--dim)}
.seg button[aria-pressed=true]{background:rgba(90,176,255,.16);color:var(--ink)}
.read{display:grid;gap:6px;border-top:1px solid var(--edge);padding-top:10px}
.read div{display:flex;justify-content:space-between;align-items:baseline;gap:12px;font-size:12.5px;color:var(--dim)}
.read b{font-weight:500;color:var(--ink);font-size:13.5px;text-align:right;overflow-wrap:anywhere;min-width:0}.read span{min-width:0}
.read b[data-t=metric]{color:var(--metric)}.read b[data-t=twist]{color:var(--twist)}.read b[data-t=gap]{color:var(--gap)}.read b[data-t=tail]{color:var(--tail)}.read b[data-t=tip]{color:var(--tip)}
.keys{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:12px;color:var(--dim)}.keys span::before{content:"";display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:6px;background:var(--c);box-shadow:0 0 8px var(--c);vertical-align:-1px}
.tb{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:36px;min-width:36px;padding:0 12px;border-radius:10px;color:var(--ink);font-size:13px;border:1px solid var(--edge)}
.tb:hover{border-color:var(--edge2);background:rgba(150,185,255,.06)}.tb[aria-pressed=true]{border-color:var(--metric);background:rgba(90,176,255,.14)}
.tb svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.tb.rec[aria-pressed=true]{border-color:var(--tip);background:rgba(255,111,145,.14);color:#ffd2dc}
.foot{margin-top:56px;color:var(--faint);font-size:12.5px;max-width:80ch}
/* ===== Stage view ===== */
.st{display:none}body.stage .st{display:block}body.stage .st.flex{display:flex}body.stage .st.grid{display:grid}
.mast{position:fixed;top:18px;left:22px;max-width:calc(50% - 200px);pointer-events:none;z-index:4}
.mast h1{font-family:var(--math);font-weight:400;font-size:26px;line-height:1.05;margin:0}
.rail{position:fixed;left:14px;top:84px;bottom:calc(var(--bar) + 26px);width:var(--rail);padding:12px 10px 12px 12px;overflow:auto;scrollbar-width:thin;z-index:4}
.act{position:relative;padding-left:18px}.act+.act{margin-top:22px}
.act::before{content:"";position:absolute;left:5px;top:4px;bottom:4px;width:2px;border-radius:2px;background:linear-gradient(var(--tail),rgba(79,227,193,.15))}
.act h4{font-family:var(--math);font-style:italic;font-weight:400;font-size:14.5px;color:var(--dim);margin:0 0 4px}
.lv{display:flex;align-items:center;gap:10px;width:100%;text-align:left;padding:5px 6px 5px 0;color:var(--dim);font-size:13px;border-radius:6px}
.lv i{flex:none;width:18px;height:2px;border-radius:2px;background:var(--faint);transition:width .25s,background .25s,box-shadow .25s;margin-left:-14px}
.lv:hover{color:var(--ink)}.lv[aria-current=true]{color:var(--ink)}.lv[aria-current=true] i{width:26px;background:var(--metric);box-shadow:0 0 10px var(--metric)}
.lv b{font-weight:400;color:var(--faint);font-size:11.5px;min-width:16px}
.card{position:fixed;top:64px;right:18px;width:var(--card);max-height:calc(100% - var(--bar) - 92px);overflow:auto;padding:18px 18px 16px;gap:12px;scrollbar-width:thin;z-index:4}
.card .sec{display:flex;justify-content:space-between;gap:12px;font-size:12.5px;color:var(--dim)}
.card h3{font-size:21px;font-weight:600;letter-spacing:-.01em;margin:0;line-height:1.2}
.card .eq{font-family:var(--math);font-size:19px;line-height:1.45;color:#f4f7ff;white-space:pre-wrap}
.card p{color:var(--dim);margin:0;font-size:13.5px;line-height:1.55}
.bar{position:fixed;left:14px;right:14px;bottom:14px;height:var(--bar);align-items:center;gap:12px;padding:0 14px;z-index:4}
.line{flex:1;display:flex;align-items:center;gap:3px;height:36px;min-width:0}
.line .grp{display:flex;gap:3px;flex:var(--n) 1 0;min-width:0}.line .grp+.grp{margin-left:9px}
.line button{flex:1;height:22px;border-radius:5px;position:relative;overflow:hidden;background:rgba(150,185,255,.07)}
.line button:hover{background:rgba(150,185,255,.16)}.line button[aria-current=true]{background:rgba(90,176,255,.22)}
.line button i{position:absolute;left:0;top:0;bottom:0;width:0;background:linear-gradient(90deg,rgba(90,176,255,.5),rgba(79,227,193,.65))}.line button em{position:relative;font-style:normal;font-size:10.5px;color:var(--dim)}.line button[aria-current=true] em{color:var(--ink)}
.sel{height:36px;border-radius:10px;border:1px solid var(--edge);background:transparent;color:var(--ink);font:inherit;font-size:13px;padding:0 8px}.sel option{background:#0b1222}
.cleanexit{position:fixed;right:16px;bottom:16px;display:none;opacity:.35;font-size:12px;color:var(--dim);z-index:4}
body.clean .rail,body.clean .card,body.clean .bar,body.clean .mast,body.clean .pill{display:none!important}body.clean .cleanexit{display:block}
/* callouts pinned to points in 3D */
#co{position:fixed;inset:0;pointer-events:none;z-index:8;overflow:hidden}
body.stage #co{z-index:3}
.callout{position:absolute;left:0;top:0;display:none;will-change:transform}
.callout .ret{position:absolute;left:-7px;top:-7px;width:14px;height:14px;border-radius:50%;border:1.5px solid var(--c);box-shadow:0 0 8px var(--c)}
.callout .ret::after{content:"";position:absolute;left:4px;top:4px;width:3px;height:3px;border-radius:50%;background:var(--c)}
.callout .lead{position:absolute;left:0;top:0;height:1px;background:linear-gradient(90deg,var(--c),rgba(255,255,255,.25));transform-origin:0 0}
.callout .box{position:absolute;padding:5px 9px 6px;border-radius:8px;background:rgba(6,11,22,.82);border:1px solid var(--edge2);border-left:2px solid var(--c);white-space:nowrap;backdrop-filter:blur(6px)}
.callout .box b{display:block;font-size:12px;font-weight:600;color:var(--ink);letter-spacing:.01em}
.callout .box span{display:block;font-size:11px;color:var(--dim)}
.pn.small .callout .box span{display:none}
/* self-test sheet */
.sheet{position:fixed;inset:0;z-index:30;display:none;align-items:center;justify-content:center;background:rgba(2,4,9,.6);padding:16px}
.sheet.on{display:flex}
.sheet .box{width:min(900px,100%);max-height:86vh;overflow:auto;padding:20px 22px;border-radius:16px;background:#0a1222;border:1px solid var(--edge2)}
.sheet h2{font-family:var(--math);font-weight:400;font-size:26px;margin:0 0 4px}.sheet .sum{color:var(--dim);margin:0 0 14px}
.sheet table{width:100%;border-collapse:collapse;font-size:13px;table-layout:fixed}.sheet col.c1{width:22%}.sheet col.c2{width:34%}.sheet col.c3{width:17%}.sheet col.c4{width:17%}.sheet col.c5{width:10%}.sheet td{overflow-wrap:anywhere}.sheet td,.sheet th{text-align:left;padding:7px 8px;border-top:1px solid var(--edge);vertical-align:top}
.sheet th{color:var(--faint);font-weight:500;position:sticky;top:-20px;background:#0a1222}.sheet td.ok{color:var(--tail)}.sheet td.no{color:var(--tip)}
.sheet .x{float:right}
.toast{position:fixed;left:50%;bottom:96px;transform:translateX(-50%);padding:8px 14px;border-radius:10px;font-size:13px;opacity:0;transition:opacity .3s;pointer-events:none;z-index:31}
.toast.on{opacity:1}
@media (max-width:1100px){:root{--rail:200px;--card:330px}}
@media (max-width:860px){.panels{grid-template-columns:minmax(0,1fr)}.ex-in{padding:76px 14px 100px}.strip{top:58px}}
@media (max-width:720px){.strip{position:static;padding:8px 10px;gap:8px}.strip label,.strip #x_test,.strip .grow{display:none}}
@media (max-width:720px){
 :root{--bar:56px}
 .pill{top:8px;max-width:calc(100% - 16px);overflow-x:auto}.pill .brand{display:none}
 .mast{display:none}
 .rail{top:56px;left:8px;right:8px;bottom:auto;width:auto;height:46px;display:flex!important;gap:16px;overflow-x:auto;overflow-y:hidden;padding:6px 10px;align-items:center;white-space:nowrap}
 body:not(.stage) .rail{display:none!important}
 .act{display:flex;align-items:center;gap:4px;padding-left:0}.act+.act{margin-top:0}.act::before,.act+.act::after,.act h4{display:none}
 .lv{padding:4px 8px;width:auto;border:1px solid var(--edge);border-radius:99px;font-size:12px}.lv i{display:none}.lv[aria-current=true]{border-color:var(--metric)}
 .card{top:auto;right:8px;left:8px;bottom:calc(var(--bar) + 16px);width:auto;max-height:42%;padding:14px}
 .card>*{order:10}.card .sec{order:0}.card h3{order:1}.card .read{order:2;border-top:0;padding-top:0}.card .ctl{order:3}.card .eq{order:4;font-size:17px}.card p{order:5}.card .keys{order:6}
 .bar{left:8px;right:8px;bottom:8px;gap:6px;padding:0 8px}.bar .wide{display:none}.line{display:none}.count{display:block!important;flex:1;text-align:center;color:var(--dim);font-size:13px}
 body.stage .mast.st{display:none!important}
 .vp{aspect-ratio:4/3}
}`;
const ICON = {
  prev:'<svg viewBox="0 0 24 24"><path d="M15 6l-6 6 6 6"/></svg>', next:'<svg viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"/></svg>',
  play:'<svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z"/></svg>', pause:'<svg viewBox="0 0 24 24"><path d="M8 5v14M16 5v14"/></svg>',
  clean:'<svg viewBox="0 0 24 24"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/></svg>', png:'<svg viewBox="0 0 24 24"><rect x="3.5" y="5.5" width="17" height="13" rx="2"/><circle cx="9" cy="10.5" r="1.6"/><path d="M20 16l-5-5-8 8"/></svg>',
  rec:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="5.5"/></svg>', layer:'<svg viewBox="0 0 24 24"><path d="M12 4l8.5 4.5L12 13 3.5 8.5z"/><path d="M3.5 13L12 17.5 20.5 13"/></svg>'
};
const GRADES = [['proved','Proved'],['computed','Computed here'],['data','Measured data'],['known','Known result'],['structural','Structural comparison'],['open','Open']];

function run(MIX){
  const st = document.createElement('style'); st.textContent = CSS; document.head.append(st);
  const eyes = MIX.eyes, byId = {}; eyes.forEach(e => byId[e.id] = e);
  const order = MIX.acts.flatMap(a => a.eyes), num = id => order.indexOf(id) + 1;
  const chip = e => `<span class="chip" data-g="${e.grade}">${e.gradeLabel || GRADES.find(g => g[0] === e.grade)[1]}</span>`;
  document.body.insertAdjacentHTML('beforeend', `
<canvas id="gl" aria-label="3D views of the eyes"></canvas>
<nav class="pill glass" aria-label="Site and view">
  <a class="brand" href="${MIX.home || '#'}">Atlas Memoriae</a><span class="sep"></span>
  <button id="v_ex" aria-pressed="true">Explainer</button><button id="v_st" aria-pressed="false">Stage</button>
  <span class="sep"></span><button id="v_test">Run self-test</button>${MIX.paper ? `<a class="b" href="${MIX.paper.href}" target="_blank" rel="noopener">${MIX.paper.label}</a>` : ''}
</nav>
<main id="ex"><div class="ex-in">
  <header class="hero"><h1>${MIX.title}</h1><p class="sub">${MIX.subtitle || ''}</p><div class="by">${MIX.byline || ''}</div>
    <div class="legend">${GRADES.map(g => `<span class="chip" data-g="${g[0]}">${g[1]}</span>`).join('')}</div></header>
  <div class="strip glass" role="toolbar" aria-label="All eyes">
    <button class="tb" id="x_play" aria-pressed="true">${ICON.pause}<span>Pause all</span></button>
    <label>Speed <input id="x_speed" type="range" min="0.25" max="2" step="0.05" value="1"><output id="x_speed_o">1.00×</output></label>
    <button class="tb" id="x_turn" aria-pressed="true">Slow turn</button>
    <span class="grow"></span><button class="tb" id="x_test">Run self-test</button>
  </div>
  ${MIX.acts.map(a => `<section aria-label="${a.name}"><div class="act-h"><h2>${a.name}</h2><span class="gapmark"></span></div><div class="panels">${a.eyes.map((id, ix) => { const e = byId[id], wide = e.wide || (a.eyes.length % 2 === 1 && ix === a.eyes.length - 1);
    return `<article class="pn${wide ? ' wide' : ''}" id="pn-${id}"><div class="pn-h"><h3><b>${num(id)}</b>${e.title}</h3>${chip(e)}</div>
      <div class="vp" id="vp-${id}" role="img" aria-label="${e.title}: drag to turn"></div>
      <div class="vrow"><span>${e.section}</span><button class="open" data-open="${id}">Open on the stage</button></div>
      <div class="eq">${e.eq}</div><p>${e.text}</p><div class="keys">${(e.legend||[]).map(l => `<span style="--c:${l[0]}">${l[1]}</span>`).join('')}</div>
      <div class="ctl" id="xc-${id}"></div><div class="read" id="xr-${id}"></div></article>`; }).join('')}</div></section>`).join('')}
  <p class="foot">${MIX.foot || ''}</p>
</div></main>
<header class="mast st"><h1>${MIX.title}</h1></header>
<nav class="rail glass st" id="rail" aria-label="Eyes"></nav>
<section class="card glass st grid" id="card" aria-live="polite">
  <div class="sec"><span id="c_sec"></span><span id="c_grade"></span></div>
  <h3 id="c_title"></h3><div class="eq" id="c_eq"></div><p id="c_what"></p><div class="keys" id="c_leg"></div><div class="ctl" id="c_ctl"></div><div class="read" id="c_read"></div>
</section>
<footer class="bar glass st flex">
  <button class="tb" id="b_prev" aria-label="Previous eye">${ICON.prev}</button>
  <button class="tb" id="b_play" aria-pressed="false" aria-label="Play the film">${ICON.play}<span class="wide">Film</span></button>
  <button class="tb" id="b_next" aria-label="Next eye">${ICON.next}</button>
  <div class="line" id="line"></div><span class="count" id="b_count" style="display:none"></span>
  <select class="sel wide" id="b_sec" aria-label="Seconds per eye"><option value="6">6 s</option><option value="8">8 s</option><option value="10" selected>10 s</option><option value="15">15 s</option><option value="20">20 s</option><option value="30">30 s</option></select>
  <button class="tb wide" id="b_over" aria-pressed="false" title="Black background for screen blending over footage">${ICON.layer}<span>Overlay</span></button>
  <button class="tb" id="b_clean" aria-label="Clean view">${ICON.clean}</button>
  <button class="tb wide" id="b_png" aria-label="Save frame as PNG">${ICON.png}</button>
  <button class="tb rec wide" id="b_rec" aria-pressed="false" aria-label="Record the stage as video">${ICON.rec}<span>Record</span></button>
</footer>
<button class="cleanexit" id="b_back">Show controls</button>
<div class="sheet" id="sheet" role="dialog" aria-modal="true" aria-labelledby="sheet_h"><div class="box"><button class="tb x" id="sheet_x">Close</button><h2 id="sheet_h">Self-test</h2><p class="sum" id="sheet_sum"></p><div id="sheet_body"></div></div></div>
<div class="toast glass" id="toast" role="status"></div><div id="co" aria-hidden="true"></div>`);
  const $ = id => document.getElementById(id);
  const E = engine($('gl')), R = E.renderer;
  const isMobile = () => window.innerWidth <= 720;
  let mode = 'explain', cur = null, film = false, fi = 0, t0 = 0, tEye = 0, paused = false, speed = 1, slowTurn = true, overlay = false;
  /* eyes: own scene, own camera, own view, own parameters */
  eyes.forEach(e => { e.p = {}; (e.controls||[]).forEach(c => e.p[c.id] = c.value); (e.choices||[]).forEach(c => e.p[c.id] = c.value);
    e.scene = E.sceneFor(); e.cam = new T.PerspectiveCamera(42, 1.6, 0.05, 400); const v = e.view || [0.7,0.38,7.2,0.3];
    e.V = {yaw:v[0], pitch:v[1], dist:v[2], ty:v[3] == null ? 0.3 : v[3], auto:true}; e.V0 = Object.assign({}, e.V);
    const sv = e.stageView || v; e.Vs = {yaw:sv[0], pitch:sv[1], dist:sv[2], ty:sv[3] == null ? 0.3 : sv[3], auto:true}; e.Vs0 = Object.assign({}, e.Vs);
    e.group = new T.Group(); e.scene.add(e.group); e.ctx = {T, p:e.p, eye:e, M:API, scene:e.scene}; e.t = 0; e.readT = 0; e.callouts = [];
    e.ctx.callout = (where, title, sub, color, dx, dy) => { const el = document.createElement('div'); el.className = 'callout'; el.style.setProperty('--c', color || '#5ab0ff');
      el.innerHTML = `<i class="ret"></i><i class="lead"></i><div class="box"><b>${title}</b>${sub ? `<span>${sub}</span>` : ''}</div>`; document.getElementById('co').append(el);
      const c = {el, where: typeof where === 'function' ? where : () => where, dx: dx == null ? 46 : dx, dy: dy == null ? -40 : dy, set(t, s2){ el.querySelector('b').textContent = t; if(s2 != null){ const sp = el.querySelector('span'); if(sp) sp.textContent = s2; } }};
      e.callouts.push(c); return c; };
    e.make(e.group, e.ctx); });
  /* controls (built into the stage card or a panel; both write the same parameters) */
  const fmt = (c, v) => c.fmt ? c.fmt(v) : (+v).toFixed(c.dp == null ? 2 : c.dp);
  const fill = el => el.style.setProperty('--f', (100*(el.value - el.min)/(el.max - el.min)) + '%');
  function controlsInto(box, e, pre){
    const C = e.controls || [], H = e.choices || [];
    box.innerHTML = H.map(h => `<div class="seg" role="group" aria-label="${h.label}">${h.options.map(o => `<button data-h="${h.id}" data-v="${o[0]}" aria-pressed="${String(e.p[h.id])===String(o[0])}">${o[1]}</button>`).join('')}</div>`).join('')
      + C.map(c => `<label>${c.label} <output id="${pre}o_${c.id}">${fmt(c, e.p[c.id])}</output><input id="${pre}p_${c.id}" type="range" min="${c.min}" max="${c.max}" step="${c.step}" value="${e.p[c.id]}" aria-label="${c.label}"></label>`).join('');
    C.forEach(c => { const el = $(pre+'p_'+c.id); fill(el); el.addEventListener('input', ev => { e.p[c.id] = +ev.target.value; $(pre+'o_'+c.id).textContent = fmt(c, e.p[c.id]); fill(el); if(e.change) e.change(e.ctx, c.id); }); });
    box.querySelectorAll('.seg button').forEach(b => b.addEventListener('click', () => { const h = H.find(x => x.id === b.dataset.h); const v = typeof h.value === 'number' ? +b.dataset.v : b.dataset.v;
      e.p[h.id] = v; b.parentElement.querySelectorAll('button').forEach(x => x.setAttribute('aria-pressed', x === b)); if(e.change) e.change(e.ctx, h.id); }));
  }
  eyes.forEach(e => { controlsInto($('xc-'+e.id), e, 'x'+e.id+'_'); orbit($('vp-'+e.id), () => e.V, true); });
  orbit($('gl'), () => mode === 'stage' && cur ? cur.Vs : null, false);
  /* stage rail and timeline */
  MIX.acts.forEach(a => {
    const div = document.createElement('div'); div.className = 'act'; div.innerHTML = `<h4>${a.name}</h4>`;
    const grp = document.createElement('div'); grp.className = 'grp'; grp.style.setProperty('--n', a.eyes.length);
    a.eyes.forEach(id => { const b = document.createElement('button'); b.className = 'lv'; b.dataset.id = id; b.innerHTML = `<i></i><b>${num(id)}</b><span>${byId[id].title}</span>`; b.addEventListener('click', () => { stopFilm(); show(id); }); div.append(b);
      const s = document.createElement('button'); s.dataset.id = id; s.setAttribute('aria-label', `${num(id)}. ${byId[id].title}`); s.title = `${num(id)}. ${byId[id].title}`; s.innerHTML = `<i></i><em>${num(id)}</em>`;
      s.addEventListener('click', () => { if(film){ fi = order.indexOf(id); t0 = performance.now()/1000; } show(id); }); grp.append(s); });
    $('rail').append(div); $('line').append(grp); });
  function show(id){
    if(!byId[id]) id = order[0];
    if(cur && cur.leave) cur.leave(cur.ctx);
    cur = byId[id]; tEye = 0;
    document.querySelectorAll('.lv[data-id],.line button[data-id]').forEach(b => b.setAttribute('aria-current', b.dataset.id === id));
    $('c_sec').textContent = `Eye ${num(id)} of ${order.length}, ${cur.section}`; $('b_count').textContent = `${num(id)} / ${order.length}`; $('c_grade').innerHTML = chip(cur);
    $('c_title').textContent = cur.title; $('c_eq').textContent = cur.eq; $('c_what').textContent = cur.text;
    $('c_leg').innerHTML = (cur.legend||[]).map(l => `<span style="--c:${l[0]}">${l[1]}</span>`).join('');
    controlsInto($('c_ctl'), cur, 's_'); Object.assign(cur.Vs, cur.Vs0);
    if(cur.enter) cur.enter(cur.ctx);
    try { history.replaceState(null, '', '#stage-' + id); } catch(err) {}
    const lv = document.querySelector(`.lv[data-id="${id}"]`); if(lv && lv.scrollIntoView) try { lv.scrollIntoView({block:'nearest', inline:'nearest'}); } catch(err) {}
  }
  function setMode(m, id){
    mode = m; document.body.classList.toggle('stage', m === 'stage'); $('v_ex').setAttribute('aria-pressed', m !== 'stage'); $('v_st').setAttribute('aria-pressed', m === 'stage');
    if(m === 'stage'){ show(id || (cur ? cur.id : order[0])); }
    else { stopFilm(); clean(false); eyes.forEach(e => controlsInto($('xc-'+e.id), e, 'x'+e.id+'_'));
      if(id){ const el = $('pn-'+id); if(el) el.scrollIntoView({block:'start'}); } try { history.replaceState(null, '', '#' + (id || '')); } catch(err) {} }
    resize();
  }
  function step(d){ const i = (order.indexOf(cur.id) + d + order.length) % order.length; if(film){ fi = i; t0 = performance.now()/1000; } show(order[i]); }
  function startFilm(){ film = true; fi = order.indexOf(cur.id); t0 = performance.now()/1000; $('b_play').setAttribute('aria-pressed', true); $('b_play').innerHTML = ICON.pause + '<span class="wide">Film</span>'; }
  function stopFilm(){ film = false; $('b_play').setAttribute('aria-pressed', false); $('b_play').innerHTML = ICON.play + '<span class="wide">Film</span>'; document.querySelectorAll('.line button i').forEach(i => i.style.width = '0'); }
  const toast = m => { const t = $('toast'); t.textContent = m; t.classList.add('on'); clearTimeout(toast.h); toast.h = setTimeout(() => t.classList.remove('on'), 2200); };
  const clean = on => { document.body.classList.toggle('clean', on); resize(); };
  /* wiring */
  $('v_ex').addEventListener('click', () => setMode('explain', cur && mode === 'stage' ? cur.id : null));
  $('v_st').addEventListener('click', () => setMode('stage'));
  document.querySelectorAll('[data-open]').forEach(b => b.addEventListener('click', () => setMode('stage', b.dataset.open)));
  $('x_play').addEventListener('click', e => { paused = !paused; e.currentTarget.setAttribute('aria-pressed', !paused); e.currentTarget.innerHTML = (paused ? ICON.play + '<span>Play all</span>' : ICON.pause + '<span>Pause all</span>'); });
  $('x_speed').addEventListener('input', e => { speed = +e.target.value; $('x_speed_o').textContent = speed.toFixed(2) + '×'; fill(e.target); }); fill($('x_speed'));
  $('x_turn').addEventListener('click', e => { slowTurn = !slowTurn; e.currentTarget.setAttribute('aria-pressed', slowTurn); });
  $('b_prev').addEventListener('click', () => step(-1)); $('b_next').addEventListener('click', () => step(1));
  $('b_play').addEventListener('click', () => film ? stopFilm() : startFilm());
  $('b_clean').addEventListener('click', () => clean(true)); $('b_back').addEventListener('click', () => clean(false));
  $('b_over').addEventListener('click', e => { overlay = e.currentTarget.getAttribute('aria-pressed') !== 'true'; e.currentTarget.setAttribute('aria-pressed', overlay); toast(overlay ? 'Overlay on: black background for screen blending' : 'Overlay off'); });
  const fname = ext => (MIX.short || 'mixer').replace(/[^A-Za-z0-9]+/g,'_') + '_' + num(cur.id) + '_' + cur.id + '.' + ext;
  $('b_png').addEventListener('click', () => { drawStage(); const a = document.createElement('a'); a.href = $('gl').toDataURL('image/png'); a.download = fname('png'); a.click(); toast('Frame saved'); });
  let rec = null, chunks = [];
  $('b_rec').addEventListener('click', e => { const b = e.currentTarget;
    if(rec){ rec.stop(); return; }
    if(!window.MediaRecorder || !$('gl').captureStream){ toast('This browser cannot record the stage'); return; }
    const types = ['video/webm;codecs=vp9','video/webm;codecs=vp8','video/webm','video/mp4']; const type = types.find(t => MediaRecorder.isTypeSupported(t)) || '';
    chunks = []; rec = new MediaRecorder($('gl').captureStream(60), type ? {mimeType:type, videoBitsPerSecond:16e6} : {});
    rec.ondataavailable = ev => ev.data.size && chunks.push(ev.data);
    rec.onstop = () => { const blob = new Blob(chunks, {type: rec.mimeType}); const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = fname(rec.mimeType.includes('mp4') ? 'mp4' : 'webm'); a.click(); rec = null; b.setAttribute('aria-pressed', false); b.querySelector('span').textContent = 'Record'; toast('Recording saved'); };
    rec.start(250); b.setAttribute('aria-pressed', true); b.querySelector('span').textContent = 'Stop'; toast('Recording the stage'); });
  document.addEventListener('keydown', e => { if(e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;
    if(e.key === 'Escape'){ $('sheet').classList.remove('on'); clean(false); return; }
    if(mode !== 'stage') return;
    if(e.key === 'ArrowRight') step(1); else if(e.key === 'ArrowLeft') step(-1); else if(e.key === ' '){ e.preventDefault(); film ? stopFilm() : startFilm(); }
    else if(e.key === 'c' || e.key === 'C') clean(!document.body.classList.contains('clean')); });
  /* self-test: every eye checks its own readouts against the paper's numbers; it tests the mixer, never the paper */
  function selfTest(){ $('sheet_body').innerHTML = '<p class="sum">Running…</p>'; $('sheet').classList.add('on');
    setTimeout(() => { let n = 0, ok = 0; const rows = [];
      eyes.forEach(e => { if(!e.test) return; let res; try { res = e.test(e.ctx); } catch(err) { res = [{label:'test failed to run: ' + err.message, mixer:'', paper:'', ok:false}]; }
        res.forEach(r => { n++; if(r.ok) ok++; rows.push(`<tr><td>${num(e.id)}. ${e.title}</td><td>${r.label}</td><td>${r.mixer}</td><td>${r.paper}</td><td class="${r.ok ? 'ok' : 'no'}">${r.ok ? 'Matches' : 'Miss'}</td></tr>`); }); });
      $('sheet_sum').textContent = `${ok} of ${n} checks match the paper. This checks the mixer against the paper's numbers; it does not grade the paper.`;
      $('sheet_body').innerHTML = `<table><colgroup><col class="c1"><col class="c2"><col class="c3"><col class="c4"><col class="c5"></colgroup><thead><tr><th>Eye</th><th>Check</th><th>Mixer</th><th>Paper</th><th>Result</th></tr></thead><tbody>${rows.join('')}</tbody></table>`; }, 30); }
  $('v_test').addEventListener('click', selfTest); $('x_test').addEventListener('click', selfTest); $('sheet_x').addEventListener('click', () => $('sheet').classList.remove('on'));
  $('sheet').addEventListener('click', e => { if(e.target === $('sheet')) $('sheet').classList.remove('on'); });
  /* drawing */
  function resize(){ const w = Math.max(1, window.innerWidth), h = Math.max(1, window.innerHeight); R.setSize(w, h, false); E.composer.setSize(w, h); E.bloom.setSize(Math.round(w/2), Math.round(h/2)); }
  window.addEventListener('resize', resize);
  const stageShift = () => { if(document.body.classList.contains('clean')) return [0,0]; if(isMobile()) return [0, -window.innerHeight*0.17];
    const cs = getComputedStyle(document.documentElement); return [(parseFloat(cs.getPropertyValue('--rail'))+14 - parseFloat(cs.getPropertyValue('--card'))-18)/2, -36]; };
  function drawStage(){ const w = Math.max(1, window.innerWidth), h = Math.max(1, window.innerHeight), s = cur.scene;
    s.background = new T.Color(overlay ? 0x000000 : 0x03060c); s.fog.color.set(overlay ? 0x000000 : 0x03060c); E.stars.visible = !overlay; s.add(E.stars);
    E.place(cur.cam, cur.Vs, w/h, isMobile()); const [sx, sy] = stageShift(); if(sx || sy) cur.cam.setViewOffset(w, h, -sx, -sy, w, h); else cur.cam.clearViewOffset();
    R.setScissorTest(false); R.setViewport(0, 0, w, h); E.rp.scene = s; E.rp.camera = cur.cam; E.composer.render();
    eyes.forEach(e => { if(e !== cur) hideCallouts(e); }); if(document.body.classList.contains('clean') && !overlay) hideCallouts(cur); else { let b0 = 0, b1 = w, t0 = 0, hh = h; if(!document.body.classList.contains('clean') && !isMobile()){ const rr = document.getElementById('rail').getBoundingClientRect(), cr = document.getElementById('card').getBoundingClientRect(); b0 = rr.right; b1 = cr.left; hh = document.querySelector('.bar').getBoundingClientRect().top; t0 = 56; }
      if(isMobile() && !document.body.classList.contains('clean')){ t0 = document.getElementById('rail').getBoundingClientRect().bottom; hh = document.getElementById('card').getBoundingClientRect().top; }
      placeCallouts(cur, cur.cam, 0, 0, w, hh, t0, b0, b1); } }
  function drawPanels(dt){ const H = Math.max(1, window.innerHeight), W = Math.max(1, window.innerWidth), clipTop = $('ex').querySelector('.strip').getBoundingClientRect().bottom;
    R.setScissorTest(false); R.setViewport(0, 0, W, H); R.setClearColor(0x000000, 0); R.clear(); R.setScissorTest(true);
    eyes.forEach(e => { const el = $('vp-'+e.id); const r = el.getBoundingClientRect();
      const top = Math.max(r.top, clipTop); if(r.bottom <= top || r.top > H || r.width < 2){ hideCallouts(e); return; }
      const y = H - r.bottom, vb = Math.min(r.bottom, H); R.setViewport(r.left, y, r.width, r.height); R.setScissor(Math.max(0, r.left), H - vb, r.width, vb - top);
      const s = e.scene; s.background = PANEL_BG; s.fog.color.set(0x060b16); E.stars.visible = true; s.add(E.stars);
      e.cam.clearViewOffset(); E.place(e.cam, e.V, r.width/r.height, false);
      if(!paused){ e.t += dt*speed; if(slowTurn && e.V.auto) e.V.yaw += dt*0.05; }
      let rows = null; try { rows = e.step ? e.step(paused ? 0 : dt*speed, e.t, e.ctx) : null; } catch(err) { if(!e.warned){ e.warned = true; console.error('eye ' + e.id + ': ' + err.message); } }
      e.readT += dt; if(rows && e.readT > 0.2){ e.readT = 0; $('xr-'+e.id).innerHTML = rows.map(q => `<div><span>${q[0]}</span><b${q[2] ? ` data-t="${q[2]}"` : ''}>${q[1]}</b></div>`).join(''); }
      R.render(s, e.cam); placeCallouts(e, e.cam, r.left, r.top, r.width, r.height, clipTop); });
    R.setScissorTest(false); }
  const PANEL_BG = new T.Color(0x060b16), _v = new T.Vector3();
  function placeCallouts(e, cam, left, top, w, h, minY, bx0, bx1){ bx0 = bx0 == null ? left : bx0; bx1 = bx1 == null ? left + w : bx1; const ty0 = Math.max(top, minY);
    e.callouts.forEach(c => { const P = c.where(); if(!P){ c.el.style.display = 'none'; return; }
      _v.copy(P).applyMatrix4(e.group.matrixWorld).project(cam); const x = left + (_v.x + 1)/2*w, y = top + (1 - _v.y)/2*h;
      if(_v.z > 1 || x < bx0 + 4 || x > bx1 - 4 || y < ty0 + 4 || y > top + h - 4){ c.el.style.display = 'none'; return; }
      c.el.style.display = 'block'; const box = c.el.querySelector('.box'), lead = c.el.querySelector('.lead'), bw = box.offsetWidth || 120, bh = box.offsetHeight || 34;
      let bxl = c.dx >= 0 ? x + c.dx : x + c.dx - bw, byt = y + c.dy - bh/2;
      if(bxl + bw > bx1 - 6) bxl = x - Math.abs(c.dx) - bw; if(bxl < bx0 + 6) bxl = x + Math.abs(c.dx);
      bxl = Math.max(bx0 + 6, Math.min(bx1 - 6 - bw, bxl)); byt = Math.max(ty0 + 6, Math.min(top + h - 6 - bh, byt));
      const ex = Math.max(bxl, Math.min(bxl + bw, x)), ey = Math.max(byt, Math.min(byt + bh, y)), dx = ex - x, dy = ey - y, L = Math.hypot(dx, dy);
      c.el.style.transform = `translate(${x}px,${y}px)`; lead.style.width = L + 'px'; lead.style.transform = `rotate(${Math.atan2(dy, dx)}rad)`;
      box.style.left = (bxl - x) + 'px'; box.style.top = (byt - y) + 'px'; }); }
  const hideCallouts = e => e.callouts.forEach(c => c.el.style.display = 'none');
  let last = performance.now(), readT = 0;
  const still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function frame(now){
    const dt = still ? 0 : Math.min(0.05, (now - last)/1000); last = now;
    if(mode === 'stage' && cur){
      tEye += dt; if(cur.Vs.auto && !still) cur.Vs.yaw += dt*0.06;
      if(film){ const sec = +$('b_sec').value, t = now/1000 - t0; if(t > sec){ fi = (fi+1) % order.length; t0 = now/1000; show(order[fi]); }
        document.querySelectorAll('.line button').forEach(b => { const k = order.indexOf(b.dataset.id); b.querySelector('i').style.width = k < fi ? '100%' : k === fi ? (100*Math.min(1,(now/1000-t0)/sec)) + '%' : '0'; }); }
      let rows = null; try { rows = cur.step ? cur.step(dt, tEye, cur.ctx) : null; } catch(err) { if(!cur.warned){ cur.warned = true; console.error('eye ' + cur.id + ': ' + err.message); } }
      readT += dt; if(rows && readT > 0.15){ readT = 0; $('c_read').innerHTML = rows.map(q => `<div><span>${q[0]}</span><b${q[2] ? ` data-t="${q[2]}"` : ''}>${q[1]}</b></div>`).join(''); }
      drawStage();
    } else drawPanels(dt);
    requestAnimationFrame(frame);
  }
  resize(); requestAnimationFrame(frame);
  let start = '', startStage = false; try { const h = decodeURIComponent(location.hash.slice(1)); if(h.startsWith('stage-')){ startStage = true; start = h.slice(6); } else start = h; } catch(err) {}
  cur = byId[start] || byId[order[0]];
  setMode(startStage || MIX.view === 'stage' ? 'stage' : 'explain', byId[start] ? start : null);
  window.MIXER_API = { show, step, setMode, startFilm, stopFilm, clean, selfTest, eyes:byId, get cur(){ return cur; }, get mode(){ return mode; } };
}

const API = { T, PAL, hex, rgb, sprite, dust, points, setPt, flush, line, setLine, dashed, setDashed, tube, setTube, orb, paintOrb, glass, ring, arrow, setArrow, bar, setBar, slab, grid, trail, pushTrail, clearTrail, surface, setSurface, label, relabel, engine, orbit, run };
window.Mixer3D3 = API;
