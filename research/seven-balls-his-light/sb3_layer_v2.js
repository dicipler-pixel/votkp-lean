/* SCRIPT: SB3-LAYER-V2 — the seven balls drawn as his balls, a flock of clocks, with his light moving in them. Jeromie Beasley. 18 Nov 2026. AI-assisted.
   Every ball is his whole Light at the Hypersurface ball (createOriginalMixerBall), the same size, placed each frame where SB3 puts it — one peel step
   out along its arm, as FL-LAYER-V1 layout() places them — with its one tree, its arms and orbs, its stack streams and pushes, its loop, rim field and
   hypothesis layer. Off, because the real balls are the walls now: the six caps, the deeper caps, the cap crossings, the 45° cap circles and the cap shadows;
   and his own ray fan, because the light is SB3's. Above each ball its own clock (FL-LAYER-V1): C at rate 1, a neighbour at 1/z of its arm (HYPOTHESIS, the
   Flock's clock ratio); the hand turns once per 2 units of the ball's own time. The ball's core glows with the light in it. */
(()=>{
'use strict';
const $ = s => document.getElementById(s), T = THREE, M3 = window.Mixer3D, canvas = $('scene'), stage = $('stage'), RB = 2.6, TAU = 2*Math.PI;
const WALL = 3 + 2*Math.SQRT2;
const O = { mode:'his', source:0, shine:true, breathe:true, A:0.35, z:[3,5,7], speed:1, zoom:120, panx:0, pany:0, playing:true,
  show:{ rims:true, field:true, trails:true, hits:true, ground:true, clocks:true, names:true } };
let W = null, clockTau = new Float64Array(7), clockLine = null, cores = null, acc = 0, last = 0, az = 0.55, el = 0.35, group = new T.Group(), BALLS = [], pk, trails, hits, deps, labels = [];
const scene = new T.Scene(), camera = new T.PerspectiveCamera(40, 1, 0.05, 400), renderer = new T.WebGLRenderer({ canvas, antialias:true, alpha:true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 1.6)); scene.add(group); scene.add(new T.AmbientLight(0xb6dfff, 1.2));
const NTR = 16, MAXP = 5000, MAXH = 1200, MAXD = 3000, FAR = new T.Vector3(1e4, 1e4, 1e4), Z3 = [0,0,0];
const seg = (n, op) => { const g = new T.BufferGeometry(); g.setAttribute('position', new T.BufferAttribute(new Float32Array(n*6), 3)); g.setAttribute('color', new T.BufferAttribute(new Float32Array(n*6), 3));
  const m = new T.LineSegments(g, new T.LineBasicMaterial({ vertexColors:true, transparent:true, opacity:op, depthWrite:false, depthTest:false, blending:T.AdditiveBlending })); m.frustumCulled = false; m.renderOrder = 6; group.add(m); let i = 0;
  return { reset(){ i = 0; }, add(a, b, c){ if(i >= n) return; const p = g.attributes.position, q = g.attributes.color; p.setXYZ(2*i, a[0], a[1], a[2]); p.setXYZ(2*i+1, b[0], b[1], b[2]); q.setXYZ(2*i, c[0], c[1], c[2]); q.setXYZ(2*i+1, c[0], c[1], c[2]); i++; }, done(){ g.setDrawRange(0, 2*i); g.attributes.position.needsUpdate = g.attributes.color.needsUpdate = true; } }; };
const pts = (n, size) => { const p = M3.points(n, size); p.material.depthTest = false; p.renderOrder = 7; p.frustumCulled = false; group.add(p); return p; };
function resize(){ const w = stage.clientWidth, h = stage.clientHeight; renderer.setSize(w, h, false); camera.aspect = w/h; camera.updateProjectionMatrix(); }
function orbit(){ const base = 9.5, radius = base*100/O.zoom, look = new T.Vector3(O.panx/100*base*0.5, O.pany/100*base*0.5, 0);
  camera.position.set(radius*Math.sin(az)*Math.cos(el), radius*Math.sin(el), radius*Math.cos(az)*Math.cos(el)).add(look); camera.lookAt(look); camera.updateMatrixWorld(); }
function dispose(){ group.traverse(o => { if(o.geometry) o.geometry.dispose(); if(o.material) (Array.isArray(o.material) ? o.material : [o.material]).forEach(m => m.dispose()); }); while(group.children.length) group.remove(group.children[0]); BALLS = []; $('labels').innerHTML = ''; labels = []; }
const P = () => ({ zI:O.z[0], zJ:O.z[1], zK:O.z[2], A:O.A, drive:O.breathe ? 'breathe' : 'hold' });
function build(){ dispose(); W = SB3.makeWorld({ mode:O.mode, zI:O.z[0], zJ:O.z[1], zK:O.z[2], A:O.A, breathe:O.breathe, source:O.source, emitEvery:O.shine ? 2 : 0 }); SB3.emit(W); acc = 0;
  W.B.forEach((b, i) => { const orig = window.createOriginalMixerBall(Object.assign({}, P(), { drive:O.breathe ? 'breathe' : 'hold' }));
    orig.layers({ rim:1, tree:0.7, balls:1, faces:0, cross:0, rays:0, stack:0.8, press:0.25, loop:0.3, rimf:0.5, hyp:0.35 });
    orig.world.traverse(o => { if(o.isPoints && o.material && o.material.size != null) o.userData.size0 = o.material.size; });   /* his dot sizes are in his ball's units; they are scaled with the ball below */
    orig.world.rotation.x = Math.PI/2;   /* his ball draws J along −z; turned so I, J, K are x, y, z, the axes the neighbours sit on */
    const G = orig.groups; G.rim.children.forEach(o => { if(o.isSprite) o.visible = false; });
    const rf = G.rimf.children; for(let q=1;q<=12;q++) if(rf[q]) rf[q].visible = false;             /* the 45° circles and the shadows of his caps */
    G.stack.children.forEach(o => { if(o.isGroup) o.visible = false; });                         /* the deeper caps; the streams and points on the arms stay */
    group.add(orig.world); BALLS.push({ i, orig, rimp:rf[0] });
    const lab = document.createElement('div'); lab.className = 'lab'; lab.textContent = 'ball ' + b.name; $('labels').appendChild(lab); labels.push({ i, lab }); });
  trails = seg(MAXP*(NTR - 1), 0.9); clockLine = seg(7*40, 1); cores = pts(7, 0.5); clockTau = new Float64Array(7); pk = pts(MAXP, 0.13); hits = pts(MAXH, 0.16); deps = pts(MAXD, 0.08); W.trail = new Map(); placeBalls(); ui(); }
function placeBalls(){ BALLS.forEach(x => { const b = W.B[x.i]; x.orig.world.position.set(b.c[0], b.c[1], b.c[2]); x.orig.world.scale.setScalar(b.R/RB); x.orig.world.traverse(o => { if(o.userData.size0 != null) o.material.size = o.userData.size0*b.R/RB; }); x.orig.world.visible = O.show.rims || O.show.field; x.orig.at(W.t);
    x.orig.groups.rim.visible = O.show.rims; x.orig.groups.rimf.visible = O.show.field; x.orig.world.traverse(o => { if(o.isSprite) o.visible = false; }); });   /* his ball's own text sprites, seven times over, are replaced by one name per ball */
  /* C's rim field: where a neighbour has come into C, that part of C's rim is inside the neighbour; it is not drawn there (the neighbour is the wall) */
  const C = BALLS[0]; if(C && C.rimp && O.show.field){ const a = C.rimp.geometry.attributes, n = a.position.count, s = 1/RB;
    for(let q=0;q<n;q++){ const x = a.position.getX(q)*s, y = -a.position.getZ(q)*s, z = a.position.getY(q)*s; let inN = false;
      for(let j=1;j<7;j++){ const b = W.B[j], dx = x - b.c[0], dy = y - b.c[1], dz = z - b.c[2]; if(dx*dx + dy*dy + dz*dz < b.R*b.R){ inN = true; break; } }
      if(inN) a.color.setXYZ(q, 0, 0, 0); } a.color.needsUpdate = true; } }
const ramp = x => M3.colour.ramp(x);
function draw(){ trails.reset(); const nray = W.o.nray;
  /* the packets: his ray colour by how many balls deep (word length), brightness by the light carried */
  let np = 0; const live = new Set();
  for(const k of W.pk){ if(np >= MAXP) break; const q = SB3.posOf(W, k); live.add(k);
    let tr = W.trail.get(k); if(!tr){ tr = k.trail && k.trail.length ? k.trail.slice() : []; } tr.push(q.slice()); if(tr.length > NTR) tr.shift(); k.trail = tr; W.trail.set(k, tr);
    const lv = Math.min(1, k.word.filter(j => j !== 0).length/4), c = ramp(0.15 + 0.7*lv), f = Math.min(1, 1.6*Math.sqrt(k.flux*nray));
    M3.setPt(pk, np++, new T.Vector3(q[0], q[1], q[2]), c.map(v => v*f));
    if(O.show.trails) for(let m=1;m<tr.length;m++){ const g = f*Math.pow(m/tr.length, 1.3); trails.add(tr[m-1], tr[m], c.map(v => v*g)); } }
  for(let q=np;q<MAXP;q++) M3.setPt(pk, q, FAR, Z3);
  for(const k of W.trail.keys()) if(!live.has(k)) W.trail.delete(k);
  trails.done();
  /* where light met a ball's sphere: white by what it returned, rose where it returned all */
  W.hits = W.hits.filter(h => (h.age += frameDt) < 0.6).slice(-MAXH); let nh = 0;
  for(const h of W.hits){ const g = O.show.hits ? Math.min(1, 2.5*Math.sqrt(h.f*nray))*(1 - h.age/0.6) : 0; M3.setPt(hits, nh++, new T.Vector3(h.q[0], h.q[1], h.q[2]), h.total ? [g, 0.45*g, 0.7*g] : [g, g, g]); }
  for(let q=nh;q<MAXH;q++) M3.setPt(hits, q, FAR, Z3);
  /* the ground keeps the record: where light reached the rim, a gold mark that fades slowly */
  W.deposits = W.deposits.filter(d => (d.age += frameDt) < 10).slice(-MAXD); let nd = 0;
  for(const d of W.deposits){ const g = O.show.ground ? Math.min(1, 3*Math.sqrt(d.f*nray))*(1 - d.age/10) : 0; M3.setPt(deps, nd++, new T.Vector3(d.q[0], d.q[1], d.q[2]), [g, 0.78*g, 0.3*g]); }
  for(let q=nd;q<MAXD;q++) M3.setPt(deps, q, FAR, Z3);
  /* the flock of clocks: each ball's own dial above it, facing the viewer; the core glows with the light in the ball */
  clockLine.reset(); const _r = new T.Vector3().setFromMatrixColumn(camera.matrixWorld, 0), _u = new T.Vector3().setFromMatrixColumn(camera.matrixWorld, 1), bk = SB3.books(W), CC = [[1,0.95,0.8],[1,0.55,0.49],[1,0.55,0.49],[0.39,0.83,1],[0.39,0.83,1],[0.95,0.76,0.31],[0.95,0.76,0.31]];
  W.B.forEach((b, i) => { const p = new T.Vector3(b.c[0], b.c[1], b.c[2]), s = Math.min(1, 1.3*Math.pow(bk.inBall[i]/Math.max(1, bk.emitted), 0.35)), cc = CC[i]; M3.setPt(cores, i, p, cc.map(v => v*s));
    if(O.show.clocks){ const ax = i ? new T.Vector3(...SB3.AXW[i - 1]) : _u, c = p.clone().addScaledVector(ax, 1.22), rc = 0.16; let prev = null; for(let q=0;q<=32;q++){ const t = TAU*q/32, pt = c.clone().addScaledVector(_r, rc*Math.sin(t)).addScaledVector(_u, rc*Math.cos(t)); if(prev) clockLine.add([prev.x, prev.y, prev.z], [pt.x, pt.y, pt.z], cc.map(v => 0.5*v)); prev = pt; }
      const ang = Math.PI*clockTau[i], tip = c.clone().addScaledVector(_r, 0.9*rc*Math.sin(ang)).addScaledVector(_u, 0.9*rc*Math.cos(ang)); clockLine.add([c.x, c.y, c.z], [tip.x, tip.y, tip.z], cc); } });
  clockLine.done();
  [pk, hits, deps, cores].forEach(M3.flush);
  labels.forEach(L => { const b = W.B[L.i]; L.lab.textContent = 'ball ' + b.name + (L.i ? '  clock ÷' + b.z.toFixed(2) : '  clock ×1'); const up = new T.Vector3().setFromMatrixColumn(camera.matrixWorld, 1), ax = L.i ? new T.Vector3(...SB3.AXW[L.i - 1]) : up, p = new T.Vector3(b.c[0], b.c[1], b.c[2]).addScaledVector(ax, 1.22).addScaledVector(up, 0.24).project(camera); L.lab.style.display = O.show.names ? '' : 'none'; L.lab.style.transform = 'translate(' + ((p.x + 1)/2*stage.clientWidth) + 'px,' + ((1 - p.y)/2*stage.clientHeight) + 'px)'; }); }
const f3 = x => Number.isFinite(x) ? x.toFixed(3) : '—', row = (a, b) => '<div class="row"><span>' + a + '</span><b>' + b + '</b></div>';
function numbers(){ const bk = SB3.books(W), B = W.B, e = Math.max(1, bk.emitted);
  let h = row('time · breaths 8, 13, 21 (his drive)', W.t.toFixed(2)) + row('light emitted (one fan of ' + W.o.nray + ' rays = 1)', bk.emitted + (O.shine ? ' · one more every 2' : ''));
  h += row('books: in flight + on the ground + below the cut', f3(bk.flight) + ' + ' + f3(bk.ground) + ' + ' + f3(bk.cut) + ' = ' + bk.total.toFixed(9));
  h += row('light in flight in each ball', B.map((b, i) => b.name + ' ' + f3(bk.inBall[i])).join('  '));
  h += row('each neighbour: step r · z · Γ = tanh(r/2) · centre · radius', B.slice(1).map(b => b.name + ' ' + f3(b.r) + ' · ' + f3(b.z) + ' · ' + f3(b.G) + ' · ' + f3(b.cc) + ' · ' + f3(b.R)).join('\n'));
  const g = [[0,2],[2,4],[0,4]].map(([a, c]) => Math.sinh(B[1 + a].h)*Math.sinh(B[1 + c].h));
  h += row('neighbours on two arms: g = sinh h_a · sinh h_b (g < 1: the two balls overlap, faces cross)', ['I·J', 'J·K', 'I·K'].map((n, q) => n + ' ' + f3(g[q]) + (g[q] < 1 ? ' overlap' : ' apart')).join('  '));
  h += row('push on each ball so far (2R · light returned)', B.map((b, i) => b.name + ' ' + f3(W.push[i])).join('  '));
  if(O.mode === 'his') h += row('light on the ground (C’s rim), by the last ball it was in', B.map((b, i) => b.name + ' ' + f3(W.groundBy[i])).join('  '));
  h += row('walls met', String(W.nHits)) + row('packets in flight', String(W.pk.length)); $('num').innerHTML = h; }
let frameDt = 0;
function frame(now){ requestAnimationFrame(frame); const dt = Math.min(0.06, (now - last)/1000 || 0); last = now; frameDt = O.playing ? dt : 0;
  if(W && O.playing){ acc += dt*O.speed*0.6; const h = 0.02; let n = Math.floor(acc/h); acc -= n*h; n = Math.min(n, 6); for(let k=0;k<n;k++){ SB3.step(W, h); W.B.forEach((b, i) => { clockTau[i] += h*(i ? 1/b.z : 1); }); } if(n){ placeBalls(); numbers(); } }
  orbit(); if(W) draw(); renderer.render(scene, camera); }
function ui(){ document.querySelectorAll('[data-k]').forEach(b => { const v = O[b.dataset.k]; b.setAttribute('aria-pressed', String(v) === b.dataset.v || (typeof v === 'boolean' && (v ? '1' : '0') === b.dataset.v)); });
  document.querySelectorAll('[data-z]').forEach(b => b.setAttribute('aria-pressed', b.dataset.z === O.z.join(',') || (b.dataset.z === 'wall' && O.z.every(z => Math.abs(z - WALL) < 1e-9))));
  document.querySelectorAll('[data-show]').forEach(b => b.setAttribute('aria-pressed', !!O.show[b.dataset.show]));
  document.querySelectorAll('[data-src]').forEach(b => { b.setAttribute('aria-pressed', +b.dataset.src === O.source); b.disabled = O.mode === 'his' && +b.dataset.src !== 0; });
  $('A').value = O.A; $('Av').textContent = O.A.toFixed(2) + (Math.abs(O.A - 0.35) < 0.005 ? ' (his)' : ''); $('zoom').value = Math.round(O.zoom); $('panx').value = Math.round(O.panx); $('pany').value = Math.round(O.pany); $('play').textContent = O.playing ? 'Pause' : 'Play'; }
document.body.addEventListener('click', ev => { const b = ev.target.closest('button'); if(!b) return; const d = b.dataset;
  if(d.k){ O[d.k] = (d.k === 'breathe' || d.k === 'shine') ? d.v === '1' : d.v; if(d.k === 'mode'){ if(O.mode === 'his') O.source = 0; O.zoom = O.mode === 'his' ? 120 : 90; } build(); }
  else if(d.z){ O.z = d.z === 'wall' ? [WALL, WALL, WALL] : d.z.split(',').map(Number); build(); }
  else if(d.src != null && d.src !== undefined && b.hasAttribute('data-src')){ O.source = +d.src; build(); }
  else if(d.show){ O.show[d.show] = !O.show[d.show]; placeBalls(); }
  else if(b.id === 'play') O.playing = !O.playing; else if(b.id === 'kick') build();
  else if(b.id === 'zin') O.zoom = Math.min(400, O.zoom*1.25); else if(b.id === 'zout') O.zoom = Math.max(25, O.zoom/1.25); else if(b.id === 'reset'){ O.zoom = O.mode === 'his' ? 120 : 90; O.panx = O.pany = 0; az = 0.55; el = 0.35; }
  ui(); });
$('A').addEventListener('change', e => { O.A = +e.target.value; build(); }); $('speed').addEventListener('input', e => { O.speed = +e.target.value; });
$('zoom').addEventListener('change', e => { O.zoom = Math.max(25, Math.min(400, +e.target.value || 100)); ui(); }); $('panx').addEventListener('change', e => { O.panx = +e.target.value || 0; ui(); }); $('pany').addEventListener('change', e => { O.pany = +e.target.value || 0; ui(); });
let drag = null; canvas.addEventListener('pointerdown', e => { drag = { x:e.clientX, y:e.clientY, az, el }; canvas.setPointerCapture(e.pointerId); }); canvas.addEventListener('pointermove', e => { if(!drag) return; az = drag.az - (e.clientX - drag.x)*0.006; el = Math.max(-1.3, Math.min(1.3, drag.el + (e.clientY - drag.y)*0.006)); }); canvas.addEventListener('pointerup', () => { drag = null; });
canvas.addEventListener('wheel', e => { e.preventDefault(); O.zoom = Math.max(25, Math.min(400, O.zoom*(e.deltaY < 0 ? 1.1 : 1/1.1))); ui(); }, { passive:false });
addEventListener('resize', resize); resize(); build(); requestAnimationFrame(frame);
window.__SB3 = { O, get clockTau(){ return clockTau; }, get W(){ return W; }, build, ui };
})();
