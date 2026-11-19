/* SCRIPT: ST3D-LAYER-V1 — Steve McCormick's step, in 3D: one lump, amplitude δm = 0.515, at seven horizon masses, twice over.
   Jeromie Beasley. 18 Nov 2026. AI-assisted. Physics, code and runs: Stephen McCormick, PBH_neutrino_simulation (commit eb7c4de), run unchanged.
   Every number drawn comes from his runs (ST3D-RUN-V1, checked against his archive by ST3D-CHECK-01) through ST3D-EXPORT-V1.
   Columns: horizon temperature T_H 16, 4, 2, 1, 0.5, 0.17, 0.0625 MeV (horizon mass 585 to 6.7e7 solar masses), hot on the left.
   Top row: the neutrinos never leave (his perfect fluid with the e± equation of state). Bottom row: his full model, the neutrinos decoupling
   through his collision rate with T_dec = 1 MeV (one fluid while κ/H > 100, then plasma plus transported neutrinos).
   Each lump: 14 of his plasma shells at R/a, coloured by his compaction C, white at the apparent horizon; a clock bead on each shell turning at
   its lapse A; on the bottom row, neutrino fans I(μ) on every second shell, bright orange where the shell's own κ/H < 1 (streaming), pale where
   κ/H ≥ 1 (held by collisions). */
(()=>{
'use strict';
const $ = s => document.getElementById(s), T = THREE, M3 = window.Mixer3D, canvas = $('scene'), stage = $('stage'), TAU = 2*Math.PI;
const D = window.ST3D_FRAMES, COLS = ['160', '40', '20', '10', '5', '1.5', '0.5'], ROWS = ['pf', 'nu'], RUNS = [];
ROWS.forEach((row, j) => COLS.forEach((c, i) => RUNS.push({ key:row + '_' + c, row, col:i, j, d:D.runs[row + '_' + c] })));
const EPS_MAX = Math.max(...RUNS.map(r => r.d.eps_end)) + 0.4, ORANGE = [1, 0.62, 0.25], PALE = [0.62, 0.78, 0.86];
const O = { eps:0.1, playing:true, speed:1, zoom:100, panx:0, pany:0, show:{ pf:true, nu:true, shells:true, clocks:true, fans:true, names:true } };
const SC = 0.4, GAP = 3.0, GAPY = 1.75, NSEG = 44, FAN_PTS = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]], NR = RUNS.length;
let az = 0.06, el = 0.12, last = 0;
const scene = new T.Scene(), camera = new T.PerspectiveCamera(20, 1, 0.05, 900), renderer = new T.WebGLRenderer({ canvas, antialias:true, alpha:true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 1.6)); scene.add(new T.AmbientLight(0xb6dfff, 1.2));
const seg = (n, op) => { const g = new T.BufferGeometry(); g.setAttribute('position', new T.BufferAttribute(new Float32Array(n*6), 3)); g.setAttribute('color', new T.BufferAttribute(new Float32Array(n*6), 3));
  const m = new T.LineSegments(g, new T.LineBasicMaterial({ vertexColors:true, transparent:true, opacity:op, depthWrite:false, blending:T.AdditiveBlending })); m.frustumCulled = false; scene.add(m); let i = 0;
  return { reset(){ i = 0; }, add(a, b, c){ if(i >= n) return; const p = g.attributes.position, q = g.attributes.color; p.setXYZ(2*i, a[0], a[1], a[2]); p.setXYZ(2*i+1, b[0], b[1], b[2]); q.setXYZ(2*i, c[0], c[1], c[2]); q.setXYZ(2*i+1, c[0], c[1], c[2]); i++; }, done(){ g.setDrawRange(0, 2*i); g.attributes.position.needsUpdate = g.attributes.color.needsUpdate = true; } }; };
const shellLines = seg(NR*14*NSEG*3, 0.85), fanLines = seg(7*7*6*64, 0.85), clockLines = seg(NR*14, 1);
const beads = M3.points(NR*14, 0.06), cores = M3.points(NR, 0.4); [beads, cores].forEach(p => { p.frustumCulled = false; scene.add(p); });
const mk = cls => { const d = document.createElement('div'); d.className = cls; $('labels').appendChild(d); return d; };
const labs = RUNS.map(() => mk('lab')), heads = COLS.map(() => mk('head')), rowl = ROWS.map(() => mk('rowl'));
/* compaction colour: C ≤ 0 deep blue, 0.25 teal, 0.5 gold, 0.75 orange, ≥ 1 red; white is kept for the horizon */
const STOPS = [[0, [0.10, 0.22, 0.55]], [0.25, [0.20, 0.75, 0.80]], [0.5, [0.95, 0.80, 0.30]], [0.75, [1.0, 0.50, 0.18]], [1.0, [0.95, 0.20, 0.20]]];
const ramp = c => { c = Math.max(0, Math.min(1, c)); for(let q=1;q<STOPS.length;q++){ if(c <= STOPS[q][0]){ const [a, A] = STOPS[q-1], [b, B] = STOPS[q], t = (c - a)/(b - a); return A.map((v, z) => v + t*(B[z] - v)); } } return STOPS[STOPS.length-1][1]; };
/* the three great circles of each shell, turned 35° about y and 25° about x so that none is seen edge-on from the front */
const TILT = (p => { const a = 0.61, b = 0.44, x1 = p[0]*Math.cos(a) + p[2]*Math.sin(a), z1 = -p[0]*Math.sin(a) + p[2]*Math.cos(a); return [x1, p[1]*Math.cos(b) - z1*Math.sin(b), p[1]*Math.sin(b) + z1*Math.cos(b)]; });
const CIRC = [0, 1, 2].map(ax => Array.from({ length:NSEG + 1 }, (_, s) => { const t = TAU*s/NSEG, c = Math.cos(t), si = Math.sin(t); return TILT(ax === 0 ? [c, si, 0] : ax === 1 ? [c, 0, si] : [0, c, si]); }));
const HIDE = new T.Vector3(1e4, 1e4, 1e4);
function frameOf(d, eps){ const F = d.frames; let lo = 0, hi = F.length - 1; if(eps <= F[0].eps) return 0; if(eps >= F[hi].eps) return hi; while(hi - lo > 1){ const m = (lo + hi) >> 1; if(F[m].eps <= eps) lo = m; else hi = m; } return lo; }
function origin(R){ return [(R.col - 3)*GAP + O.panx/100*8, (R.j ? -GAPY : GAPY) + O.pany/100*4, 0]; }
function resize(){ const w = stage.clientWidth, h = stage.clientHeight; renderer.setSize(w, h, false); camera.aspect = w/h; camera.updateProjectionMatrix(); }
function orbit(){ const base = 50*Math.max(1, 1.35/camera.aspect), radius = base*100/O.zoom; camera.position.set(radius*Math.sin(az)*Math.cos(el), radius*Math.sin(el), radius*Math.cos(az)*Math.cos(el)); camera.lookAt(O.panx/100*8, O.pany/100*4, 0); camera.updateMatrixWorld(); }
const scr = v => { const p = v.project(camera); return [(p.x + 1)/2*stage.clientWidth, (1 - p.y)/2*stage.clientHeight]; };
const place = (el, xy) => { el.style.transform = 'translate(' + xy[0] + 'px,' + xy[1] + 'px)'; };
const mass = m => { const e = Math.floor(Math.log10(m)), s = m/Math.pow(10, e); return (e < 4 ? Math.round(m).toString() : s.toFixed(1) + '×10<sup>' + e + '</sup>') + ' M<sub>⊙</sub>'; };
function draw(){ shellLines.reset(); fanLines.reset(); clockLines.reset(); const ws = TAU/40;
  RUNS.forEach((Rn, k) => { const d = Rn.d, show = O.show[Rn.row], o = origin(Rn), f = d.frames[frameOf(d, O.eps)], n = f.Ra.length, ended = O.eps >= d.eps_end - 1e-9;
    if(!show){ for(let i=0;i<n;i++) M3.setPt(beads, k*14 + i, HIDE, [0,0,0]); M3.setPt(cores, k, HIDE, [0,0,0]); labs[k].style.display = 'none'; return; }
    for(let i=0;i<n;i++){ const R = f.Ra[i]*SC, horizon = f.fall[i] && f.twoMR[i] >= 1, inner = 1 - i/(n + 2), col = horizon ? [1, 1, 1] : ramp(f.C[i]).map(v => v*(0.45 + 0.55*inner));
      if(O.show.shells) for(let ax=0;ax<3;ax++){ const C = CIRC[ax]; for(let s=0;s<NSEG;s++) shellLines.add([o[0] + R*C[s][0], o[1] + R*C[s][1], o[2] + R*C[s][2]], [o[0] + R*C[s+1][0], o[1] + R*C[s+1][1], o[2] + R*C[s+1][2]], col); }
      /* the shell's own clock: a bead on its equator turning at its lapse A (his A = 1 at the outer cell) */
      const ang = ws*f.tau[i] + i*0.35, bp = [o[0] + R*Math.cos(ang), o[1], o[2] + R*Math.sin(ang)];
      M3.setPt(beads, k*14 + i, O.show.clocks ? new T.Vector3(...bp) : HIDE, horizon ? [1,1,1] : col.map(v => Math.min(1, 1.5*v)));
      if(O.show.clocks) clockLines.add([o[0] + 0.86*R*Math.cos(ang), o[1], o[2] + 0.86*R*Math.sin(ang)], bp, col);
      /* the neutrinos (bottom row, after his split): I(μ)/mean as a flower about the outward normal at six points;
         orange where this shell's own κ/H < 1 (streaming), pale where κ/H ≥ 1 (held by collisions) */
      if(Rn.row === 'nu' && O.show.fans && i % 2 === 1 && i >= 3 && i < n - 2 && f.I){ const I = f.I[i], nmu = I.length, L = 0.2*SC, kh = f.kH[i], held = Math.max(0, Math.min(1, 0.5 + 0.5*Math.log10(Math.max(1e-6, kh)))), base0 = ORANGE.map((v, q) => v*(1 - held) + PALE[q]*held);
        for(const p of FAN_PTS){ const base = [o[0] + R*p[0], o[1] + R*p[1], o[2] + R*p[2]], tg = Math.abs(p[1]) > 0.5 ? [1,0,0] : [0,1,0];
          for(let jj=0;jj<nmu;jj+=2){ const mu = -1 + (jj + 1)*2/nmu, sn = Math.sqrt(1 - mu*mu), len = L*0.5*(I[jj] + I[jj+1]);
            for(const side of [1, -1]){ const dir = [mu*p[0] + side*sn*tg[0], mu*p[1] + side*sn*tg[1], mu*p[2] + side*sn*tg[2]]; fanLines.add(base, [base[0] + len*dir[0], base[1] + len*dir[1], base[2] + len*dir[2]], base0.map(v => 0.42*v*(0.3 + 0.7*Math.abs(mu)))); } } } } }
    const c0 = Math.max(0, f.C[0]), s = Math.min(1, 0.25 + 0.6*c0);
    M3.setPt(cores, k, new T.Vector3(...o), ended && d.status === 'BH' ? [1, 1, 1] : [s, 0.85*s, 0.6*s]);
    labs[k].style.display = O.show.names ? '' : 'none'; place(labs[k], scr(new T.Vector3(o[0], o[1] - 1.45, o[2])));
    labs[k].innerHTML = ended ? (d.status === 'BH' ? '<b class="bh">horizon</b> ε ' + d.eps_end.toFixed(2) : '<b class="ds">bounced</b> ε ' + d.eps_end.toFixed(2)) : (Rn.row === 'nu' ? (f.one ? 'one fluid' : 'κ<sub>b</sub>/H ' + (f.kbH < 0.01 ? f.kbH.toExponential(1) : f.kbH.toFixed(2))) : 'C<sub>max</sub> ' + f.Cmax.toFixed(2)); });
  COLS.forEach((c, i) => { const d = D.runs['nu_' + c]; heads[i].style.display = O.show.names ? '' : 'none'; place(heads[i], scr(new T.Vector3((i - 3)*GAP + O.panx/100*8, GAPY + 1.65 + O.pany/100*4, 0)));
    heads[i].innerHTML = 'T<sub>H</sub> ' + (d.TH >= 1 ? d.TH.toFixed(0) : d.TH.toFixed(d.TH < 0.1 ? 3 : 2)) + ' MeV<br><span>M<sub>H</sub> ' + mass(d.MH) + '</span>'; });
  rowl.forEach((el, j) => { el.style.display = O.show.names ? '' : 'none'; place(el, scr(new T.Vector3(-3*GAP - 2.35 + O.panx/100*8, (j ? -GAPY : GAPY) + O.pany/100*4, 0)));
    el.innerHTML = j ? 'neutrinos<br>leave<br><span>his full model</span>' : 'neutrinos<br>held in<br><span>one fluid</span>'; });
  shellLines.done(); fanLines.done(); clockLines.done(); [beads, cores].forEach(M3.flush); }
const f3 = x => Number.isFinite(x) ? x.toFixed(3) : '—', row = (a, b) => '<div class="row"><span>' + a + '</span><b>' + b + '</b></div>';
function numbers(){ let h = row('ε = 1/(aH r_m), the Hubble radius over the size of the lump; horizon crossing at 1', O.eps.toFixed(2));
  COLS.forEach(c => { const a = D.runs['pf_' + c], b = D.runs['nu_' + c], fa = a.frames[frameOf(a, O.eps)], fb = b.frames[frameOf(b, O.eps)];
    const TH = b.TH, ph = D.curves.phys.reduce((p, q) => Math.abs(Math.log(q.TH/TH)) < Math.abs(Math.log(p.TH/TH)) ? q : p), pf = D.curves.pf.reduce((p, q) => Math.abs(Math.log(q.TH/TH)) < Math.abs(Math.log(p.TH/TH)) ? q : p);
    h += row('T_H ' + TH.toPrecision(3) + ' MeV · his δc: held ' + pf.dc.toFixed(4) + ', leave ' + ph.dc.toFixed(4),
      'held: C_max ' + f3(fa.Cmax) + ' · centre A ' + f3(fa.A[0]) + (O.eps >= a.eps_end ? ' · ' + a.status + ' at ε ' + a.eps_end.toFixed(2) : '') +
      '<br>leave: T_b ' + (fb.Tb).toPrecision(3) + ' MeV · κ_b/H ' + (fb.one ? '> 100 (one fluid)' : fb.kbH.toPrecision(2)) + ' · centre κ/H ' + (fb.one ? '—' : fb.kH[0].toPrecision(2)) + ' · C_max ' + f3(fb.Cmax) + ' · centre A ' + f3(fb.A[0]) + (O.eps >= b.eps_end ? ' · ' + (b.status === 'BH' ? 'BH' : 'bounced') + ' at ε ' + b.eps_end.toFixed(2) : '')); });
  $('num').innerHTML = h; charts(); }
const BLUE = '#63d3ff', GREY = '#9aa6b8';
function charts(){ const dpr = devicePixelRatio;
  { const cv = $('c0'), g = cv.getContext('2d'), W = cv.width = cv.clientWidth*dpr, H = cv.height = 150*dpr, lx0 = Math.log10(300), lx1 = Math.log10(1.5e8), y0 = 0.482, y1 = 0.531;
    const x = m => 26*dpr + (Math.log10(m) - lx0)/(lx1 - lx0)*(W - 32*dpr), y = v => H - 16*dpr - (v - y0)/(y1 - y0)*(H - 24*dpr);
    g.clearRect(0, 0, W, H); g.font = (9.5*dpr) + 'px system-ui'; g.fillStyle = '#5c6b80';
    for(let e=3;e<=8;e++){ g.fillText('10' + '⁰¹²³⁴⁵⁶⁷⁸'[e], x(Math.pow(10, e)) - 6*dpr, H - 3*dpr); g.fillRect(x(Math.pow(10, e)), H - 16*dpr, 1, 3*dpr); }
    [0.49, 0.50, 0.51, 0.52, 0.53].forEach(v => { g.fillText(v.toFixed(2), 0, y(v) + 3*dpr); g.fillStyle = 'rgba(92,107,128,.25)'; g.fillRect(26*dpr, y(v), W, 1); g.fillStyle = '#5c6b80'; });
    g.strokeStyle = 'rgba(242,193,78,.75)'; g.setLineDash([4*dpr, 4*dpr]); g.beginPath(); g.moveTo(x(300), y(0.515)); g.lineTo(W, y(0.515)); g.stroke(); g.setLineDash([]); g.fillStyle = 'rgba(242,193,78,.9)'; g.fillText('δm 0.515, this lump', x(400), y(0.515) - 3*dpr);
    const line = (pts, col) => { g.strokeStyle = col; g.lineWidth = 1.6*dpr; g.beginPath(); pts.forEach((p, i) => i ? g.lineTo(x(p.MH), y(p.dc)) : g.moveTo(x(p.MH), y(p.dc))); g.stroke(); pts.forEach(p => { g.fillStyle = col; g.fillRect(x(p.MH) - 1.5*dpr, y(p.dc) - 1.5*dpr, 3*dpr, 3*dpr); }); };
    if(O.show.pf) line(D.curves.pf, GREY); if(O.show.nu) line(D.curves.phys, BLUE);
    g.fillStyle = GREY; g.fillText('held in', x(2e7), y(0.4865) + 12*dpr); g.fillStyle = BLUE; g.fillText('neutrinos leave', x(1.1e4), y(0.5035) - 6*dpr);
    COLS.forEach(c => ROWS.forEach(rw => { const d = D.runs[rw + '_' + c]; if(!O.show[rw]) return; const done = O.eps >= d.eps_end, px = x(d.MH), py = y(0.515) + (rw === 'pf' ? -0 : 0);
      g.beginPath(); g.arc(px, py, (rw === 'nu' ? 4.2 : 2.4)*dpr, 0, TAU); if(done && d.status === 'BH'){ g.fillStyle = '#fff'; g.fill(); } else { g.strokeStyle = done ? BLUE : '#7f8ca0'; g.lineWidth = 1.3*dpr; g.stroke(); } })); }
  { const cv = $('c1'), g = cv.getContext('2d'), W = cv.width = cv.clientWidth*dpr, H = cv.height = 120*dpr, x = e => 6*dpr + (e/EPS_MAX)*(W - 12*dpr), y = v => H - 6*dpr - Math.max(0, v)/1.05*(H - 12*dpr);
    g.clearRect(0, 0, W, H); g.font = (9.5*dpr) + 'px system-ui';
    RUNS.forEach(Rn => { if(!O.show[Rn.row]) return; const F = Rn.d.frames, t = Rn.col/6, col = Rn.row === 'pf' ? 'rgba(154,166,184,' + (0.35 + 0.5*(1 - t)) + ')' : 'rgba(99,211,255,' + (0.35 + 0.6*(1 - t)) + ')';
      g.strokeStyle = col; g.lineWidth = 1.2*dpr; g.setLineDash(Rn.row === 'pf' ? [3*dpr, 2*dpr] : []); g.beginPath(); F.forEach((f, i) => i ? g.lineTo(x(f.eps), y(f.Cmax)) : g.moveTo(x(f.eps), y(f.Cmax))); g.stroke(); g.setLineDash([]);
      const l = F[F.length - 1]; if(Rn.d.status === 'BH'){ g.fillStyle = '#fff'; g.beginPath(); g.arc(x(l.eps), y(l.Cmax), 2.2*dpr, 0, TAU); g.fill(); } });
    g.strokeStyle = 'rgba(255,255,255,.6)'; g.lineWidth = 1; g.beginPath(); g.moveTo(x(O.eps), 0); g.lineTo(x(O.eps), H); g.stroke(); } }
function frame(now){ requestAnimationFrame(frame); const dt = Math.min(0.06, (now - last)/1000 || 0); last = now;
  if(O.playing){ O.eps += dt*O.speed*0.5; if(O.eps > EPS_MAX) O.eps = 0.1; $('eps').value = O.eps; }
  orbit(); draw(); if(Math.floor(now/150) !== Math.floor((now - dt*1000)/150) || !O.playing) numbers(); renderer.render(scene, camera); }
function ui(){ document.querySelectorAll('[data-show]').forEach(b => b.setAttribute('aria-pressed', !!O.show[b.dataset.show])); $('play').textContent = O.playing ? 'Pause' : 'Play'; $('zoom').value = Math.round(O.zoom); $('panx').value = Math.round(O.panx); $('pany').value = Math.round(O.pany); }
document.body.addEventListener('click', ev => { const b = ev.target.closest('button'); if(!b) return;
  if(b.dataset.show){ O.show[b.dataset.show] = !O.show[b.dataset.show]; }
  else if(b.id === 'play') O.playing = !O.playing; else if(b.id === 'restart'){ O.eps = 0.1; }
  else if(b.dataset.jump){ O.eps = +b.dataset.jump; O.playing = false; $('eps').value = O.eps; }
  else if(b.id === 'zin') O.zoom = Math.min(400, O.zoom*1.25); else if(b.id === 'zout') O.zoom = Math.max(25, O.zoom/1.25); else if(b.id === 'reset'){ O.zoom = 100; O.panx = O.pany = 0; az = 0.06; el = 0.12; }
  ui(); numbers(); });
$('eps').max = EPS_MAX.toFixed(2);
$('eps').addEventListener('input', e => { O.eps = +e.target.value; O.playing = false; ui(); numbers(); }); $('speed').addEventListener('input', e => { O.speed = +e.target.value; });
$('zoom').addEventListener('change', e => { O.zoom = Math.max(25, Math.min(400, +e.target.value || 100)); }); $('panx').addEventListener('change', e => { O.panx = +e.target.value || 0; }); $('pany').addEventListener('change', e => { O.pany = +e.target.value || 0; });
let drag = null; canvas.addEventListener('pointerdown', e => { drag = { x:e.clientX, y:e.clientY, az, el }; canvas.setPointerCapture(e.pointerId); }); canvas.addEventListener('pointermove', e => { if(!drag) return; az = drag.az - (e.clientX - drag.x)*0.006; el = Math.max(-1.3, Math.min(1.3, drag.el + (e.clientY - drag.y)*0.006)); }); canvas.addEventListener('pointerup', () => { drag = null; });
canvas.addEventListener('wheel', e => { e.preventDefault(); O.zoom = Math.max(25, Math.min(400, O.zoom*(e.deltaY < 0 ? 1.1 : 1/1.1))); ui(); }, { passive:false });
addEventListener('resize', resize); resize(); ui(); numbers(); requestAnimationFrame(frame);
window.__ST3D = { O };
})();
