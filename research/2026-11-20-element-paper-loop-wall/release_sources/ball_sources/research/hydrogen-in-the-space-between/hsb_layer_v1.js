/* SCRIPT: HSB-LAYER-V1
   Hydrogen in the Space Between — the field, the drawing, the slim panel. Jeromie Beasley. 17 Nov 2026. AI-assisted.
   The field is the whole stage. Each atom is the Light at the Hypersurface ball (its own construction, unchanged); the sites between are the
   electrons that fill the space, drawn as small spheres sized by their occupation; the links carry what moves: charge (occupation current)
   or light (energy current), as beams, with an X on a gap link whose weight between is below a third of the largest possible. Zoom and pan
   are percentages. Nothing sits on the field but the field. */
(()=>{
'use strict';
const $ = s => document.getElementById(s), T = THREE, canvas = $('scene'), stage = $('stage'), HSB = window.HSB;
const O = { atoms:2, sep:4, spins:'opposed', view:'light', speed:1, zoom:100, panx:0, pany:0, playing:true };
let M = null, R = null, time = 0, last = 0, firstMove = null, az = 0.18, el = 0.24, group = new T.Group(), sites = [], balls = [], beams = [], xmarks = [], labels = [], building = false, bondNote = '';
const scene = new T.Scene(), camera = new T.PerspectiveCamera(42, 1, 0.1, 400), renderer = new T.WebGLRenderer({ canvas, antialias:true, alpha:true }); renderer.setPixelRatio(Math.min(devicePixelRatio, 1.6)); scene.add(group);
scene.add(new T.AmbientLight(0xb6dfff, 1.4)); const lamp = new T.DirectionalLight(0xffffff, 2); lamp.position.set(4, 10, 6); scene.add(lamp);
const v3 = p => new T.Vector3(p[0], p[1], p[2]), lg = (x, lo, hi) => Math.max(0, Math.min(1, (Math.log10(Math.abs(x) + 1e-300) - lo)/(hi - lo)));
function resize(){ const w = stage.clientWidth, h = stage.clientHeight; renderer.setSize(w, h, false); camera.aspect = w/h; camera.updateProjectionMatrix(); }
function orbit(){ const base = M ? 9 + 1.2*M.nx : 21, radius = base*100/O.zoom; camera.position.set(radius*Math.sin(az)*Math.cos(el), radius*Math.sin(el), radius*Math.cos(az)*Math.cos(el)); const look = new T.Vector3(O.panx/100*base*0.5, O.pany/100*base*0.5, 0); camera.position.add(look); camera.lookAt(look); }
function dispose(){ group.traverse(o => { if(o.geometry) o.geometry.dispose(); if(o.material){ (Array.isArray(o.material) ? o.material : [o.material]).forEach(m => m.dispose()); } }); while(group.children.length) group.remove(group.children[0]); sites = []; balls = []; beams = []; xmarks = []; $('labels').innerHTML = ''; labels = []; }
function makeScene(){ dispose();
  M.pos.forEach((p, i) => { const b = M.body[i]; if(b < 0){ const s = new T.Mesh(new T.SphereGeometry(1, 14, 10), new T.MeshBasicMaterial({ color:0x4fe0c0, transparent:true, opacity:0.85 })); s.position.copy(v3(p)); s.scale.setScalar(0.1); group.add(s); sites.push({ i, mesh:s }); }
    else if(M.atomsAt.includes(i)){ const orig = window.createOriginalMixerBall({ zI:M.o.faceZ[0], zJ:M.o.faceZ[1], zK:M.o.faceZ[2], drive:'hold' }); orig.layers({ rays:0, stack:0.3, press:0, hyp:0, loop:0.2 }); orig.world.position.copy(v3(p)); orig.world.scale.setScalar(0.46); group.add(orig.world); balls.push({ i, b, orig });
      const lab = document.createElement('div'); lab.className = 'lab'; lab.textContent = 'H ' + String.fromCharCode(65 + b); $('labels').appendChild(lab); labels.push({ i, lab }); } });
  M.links.forEach((l, q) => { const a = v3(M.pos[l.i]), b = v3(M.pos[l.j]), dir = b.clone().sub(a).normalize(), beam = new T.Mesh(new T.CylinderGeometry(1, 1, 1, 6, 1, true), new T.MeshBasicMaterial({ color:0x5bd8d1, transparent:true, opacity:0.2, depthWrite:false, blending:T.AdditiveBlending }));
    beam.position.copy(a).add(b).multiplyScalar(0.5); beam.quaternion.setFromUnitVectors(new T.Vector3(0, 1, 0), dir); beam.userData.len = a.distanceTo(b); beam.scale.set(0.02, beam.userData.len, 0.02); group.add(beam); beams.push({ q, mesh:beam, a, b, dir });
    if(l.gap){ const g = new T.BufferGeometry().setFromPoints([new T.Vector3(-0.18, -0.18, 0), new T.Vector3(0.18, 0.18, 0), new T.Vector3(-0.18, 0.18, 0), new T.Vector3(0.18, -0.18, 0)]), x = new T.LineSegments(g, new T.LineBasicMaterial({ color:0xd9a0ff, transparent:true, opacity:0.9 })); x.position.copy(a).add(b).multiplyScalar(0.5); group.add(x); xmarks.push({ q, mesh:x }); } });
  const floor = new T.GridHelper(40, 40, 0x1a2c40, 0x0f1b2a); floor.position.y = -2.4; group.add(floor); }
function build(){ building = true; $('status').textContent = 'Building the sea…'; setTimeout(() => { M = HSB.build({ atoms:O.atoms, sep:O.sep, spins:O.spins }); time = 0; firstMove = null; HSB.at(M, 0); R = HSB.read(M); M.dEkick = R.dE; makeScene(); orbit(); building = false; update(); }, 20); }
function update(){ if(!M || !R) return; const r = R, far = M.atomsAt.length > 1 ? 1 : 0;
  if(firstMove === null && r.bodyChange[far] > 1e-7) firstMove = time;
  const cam = camera.position;
  sites.forEach(s => { const i = s.i, occ = r.occ[i], ch = r.change[i], w = lg(ch, -8, -1); s.mesh.scale.setScalar(0.06 + 0.16*Math.min(1, occ) + 0.14*w); const c = s.mesh.material.color;
    c.setRGB(0.08 + 0.92*w, 0.22 + 0.78*w, 0.2 + 0.6*w); s.mesh.material.opacity = 0.55 + 0.45*w; });
  beams.forEach(bm => { const q = bm.q, l = M.links[q]; let v = 0, col = [0.3, 0.8, 0.8];
    if(O.view === 'light'){ v = lg(r.jE[q], -6, -1); col = r.jE[q] >= 0 ? [1, 0.85, 0.4] : [0.5, 0.75, 1]; }
    else if(O.view === 'connection'){ v = Math.min(1, M.conn[q]/Math.max(...M.conn)); col = [1, 0.55, 0.3]; } else { v = lg(r.X[q], -4, 0); col = [0.85, 0.55, 1]; }
    bm.mesh.scale.set(0.015 + 0.28*v, bm.mesh.userData.len, 0.015 + 0.28*v); bm.mesh.material.opacity = 0.08 + 0.85*v; bm.mesh.material.color.setRGB(col[0], col[1], col[2]); });
  xmarks.forEach(x => { x.mesh.visible = r.X[x.q] <= (1/4)/3; x.mesh.lookAt(cam); });
  balls.forEach(b => { b.orig.at(time); });
  labels.forEach(L => { const p = v3(M.pos[L.i]).add(new T.Vector3(0, 1.6, 0)).project(camera), w = stage.clientWidth, h = stage.clientHeight; L.lab.style.transform = 'translate(' + ((p.x + 1)/2*w) + 'px,' + ((1 - p.y)/2*h) + 'px)'; });
  numbers(); }
const e1 = x => Number.isFinite(x) ? x.toExponential(1) : '—', f3 = x => Number.isFinite(x) ? x.toFixed(3) : '—', row = (a, b) => '<div class="row"><span>' + a + '</span><b>' + b + '</b></div>';
function numbers(){ const r = R, far = M.atomsAt.length > 1 ? 1 : 0, dist = (M.o.sep*1.6).toFixed(1); let h = '';
  h += row('time', time.toFixed(2)) + row('sites · occupied', M.N + ' · ' + M.k + '  (gap ' + f3(M.gap) + ')') + row('books: Tr P − N, E(t) − E(kick)', e1(r.occ.reduce((s, v) => s + v, 0) - M.N) + ', ' + e1(r.dE - M.dEkick)) + row('energy put in by the kick', f3(M.dEkick)) + row('energy in atoms / in the space', f3(r.Eb) + ' / ' + f3(r.Es));
  h += row('atom A change · far atom ' + String.fromCharCode(65 + far) + ' change', e1(r.bodyChange[0]) + ' · ' + e1(r.bodyChange[far])) + row('occupation moved (largest site)', e1(Math.max(...r.charge.map(Math.abs))) + '  a turn carries no charge') + row('far atom first moved', (firstMove === null ? '—' : firstMove.toFixed(2)) + '  (distance ' + dist + ', largest lattice speed 0.704)');
  h += row('gap row: least weight between', e1(r.rowMin) + '  ' + (r.connects ? 'connects' : 'does not connect') + ' (a third of ¼)') + row('offset τ per atom', r.tau.map(f3).join('  ')) + row('connection energy, all links', f3(M.nnce.rhs) + '  (identity holds: ' + e1(M.nnce.lhs - M.nnce.rhs) + ')') + row('ground energy', f3(M.Eground));
  $('num').innerHTML = h; $('status').textContent = ''; }
function frame(now){ requestAnimationFrame(frame); const dt = Math.min(0.06, (now - last)/1000 || 0); last = now; if(M && !building && O.playing){ time += dt*O.speed; HSB.at(M, time); R = HSB.read(M); update(); } orbit(); renderer.render(scene, camera); }
/* ---- controls ---- */
function ui(){ document.querySelectorAll('[data-k]').forEach(b => b.setAttribute('aria-pressed', String(O[b.dataset.k]) === b.dataset.v)); $('sep').value = O.sep; $('sepv').textContent = O.sep + ' lattice steps (' + (O.sep*1.6).toFixed(1) + ' model units)'; $('zoom').value = Math.round(O.zoom); $('panx').value = Math.round(O.panx); $('pany').value = Math.round(O.pany); $('play').textContent = O.playing ? 'Pause' : 'Play'; }
document.body.addEventListener('click', ev => { const b = ev.target.closest('button'); if(!b) return; const d = b.dataset; if(d.k){ O[d.k] = isNaN(+d.v) ? d.v : +d.v; if(d.k === 'atoms' || d.k === 'spins') build(); }
  else if(b.id === 'play') O.playing = !O.playing; else if(b.id === 'replay'){ time = 0; firstMove = null; if(M){ HSB.at(M, 0); R = HSB.read(M); update(); } } else if(b.id === 'zin') O.zoom = Math.min(400, O.zoom*1.25); else if(b.id === 'zout') O.zoom = Math.max(25, O.zoom/1.25); else if(b.id === 'reset'){ O.zoom = 100; O.panx = O.pany = 0; az = 0.18; el = 0.24; } ui(); });
$('sep').addEventListener('change', e => { O.sep = +e.target.value; ui(); build(); }); $('zoom').addEventListener('change', e => { O.zoom = Math.max(25, Math.min(400, +e.target.value || 100)); ui(); }); $('panx').addEventListener('change', e => { O.panx = +e.target.value || 0; ui(); }); $('pany').addEventListener('change', e => { O.pany = +e.target.value || 0; ui(); }); $('speed').addEventListener('input', e => { O.speed = +e.target.value; });
let drag = null; canvas.addEventListener('pointerdown', e => { drag = { x:e.clientX, y:e.clientY, az, el }; canvas.setPointerCapture(e.pointerId); }); canvas.addEventListener('pointermove', e => { if(!drag) return; az = drag.az + (e.clientX - drag.x)*0.006; el = Math.max(-1.2, Math.min(1.2, drag.el + (e.clientY - drag.y)*0.006)); }); canvas.addEventListener('pointerup', () => { drag = null; });
canvas.addEventListener('wheel', e => { e.preventDefault(); O.zoom = Math.max(25, Math.min(400, O.zoom*(e.deltaY < 0 ? 1.1 : 1/1.1))); ui(); }, { passive:false });
addEventListener('resize', resize); resize(); ui(); build(); requestAnimationFrame(frame);
window.__HSB = { O, get M(){ return M; }, get R(){ return R; }, firstMove:() => firstMove, time:() => time, building:() => building };
})();
