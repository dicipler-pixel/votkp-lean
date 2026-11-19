/* SCRIPT: NU3D-LAYER-V1 — Steve McCormick's Figure 1, in 3D: the same lump of radiation three times over, as nested shells.
   Jeromie Beasley. 18 Nov 2026. AI-assisted. Physics, code and runs: Stephen McCormick, PBH_neutrino_simulation (commit eb7c4de), run unchanged.
   Every number drawn comes from his runs (NU3D-RUN-V2, checked against his archived figure data by NU3D-CHECK-01) through NU3D-EXPORT-V1.
   Each lump: 14 of his Lagrangian plasma shells at R/a (the background expansion divided out), coloured by his compaction C = 2(M − Mb)/R,
   white where a shell is falling in with 2M/R ≥ 1 (the apparent horizon). On each shell a clock bead turns at the shell's lapse A against the
   background. On the neutrino runs, fans on every second shell draw the neutrino intensity I(μ) against the outward direction (μ = cos θ), as a
   flower: round when the neutrinos are isotropic, stretched outward when they stream out, inward when they fall in. */
(()=>{
'use strict';
const $ = s => document.getElementById(s), T = THREE, M3 = window.Mixer3D, canvas = $('scene'), stage = $('stage'), TAU = 2*Math.PI;
const D = window.NU3D_FRAMES, RUNS = ['fluid', 'nu', 'nu535'], NAME = { fluid:'perfect fluid, δm 0.510', nu:'free-streaming ν, δm 0.510', nu535:'free-streaming ν, δm 0.535' };
const CURVE_COL = { fluid:'#9aa6b8', nu:'#63d3ff', nu535:'#63d3ff' }, ORANGE = [1, 0.62, 0.25];
const O = { eps:0.1, playing:true, speed:1, zoom:100, panx:0, pany:0, show:{ fluid:true, nu:true, nu535:true, shells:true, clocks:true, fans:true, names:true } };
const SC = 0.55, GAP = 3.6, NSEG = 56, FAN_PTS = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]];
let az = 0.35, el = 0.32, last = 0;
const scene = new T.Scene(), camera = new T.PerspectiveCamera(38, 1, 0.05, 400), renderer = new T.WebGLRenderer({ canvas, antialias:true, alpha:true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 1.6)); scene.add(new T.AmbientLight(0xb6dfff, 1.2));
const seg = (n, op) => { const g = new T.BufferGeometry(); g.setAttribute('position', new T.BufferAttribute(new Float32Array(n*6), 3)); g.setAttribute('color', new T.BufferAttribute(new Float32Array(n*6), 3));
  const m = new T.LineSegments(g, new T.LineBasicMaterial({ vertexColors:true, transparent:true, opacity:op, depthWrite:false, blending:T.AdditiveBlending })); m.frustumCulled = false; scene.add(m); let i = 0;
  return { reset(){ i = 0; }, add(a, b, c){ if(i >= n) return; const p = g.attributes.position, q = g.attributes.color; p.setXYZ(2*i, a[0], a[1], a[2]); p.setXYZ(2*i+1, b[0], b[1], b[2]); q.setXYZ(2*i, c[0], c[1], c[2]); q.setXYZ(2*i+1, c[0], c[1], c[2]); i++; }, done(){ g.setDrawRange(0, 2*i); g.attributes.position.needsUpdate = g.attributes.color.needsUpdate = true; } }; };
const shellLines = seg(3*14*NSEG*3 + 64*3, 0.9), fanLines = seg(3*7*6*64, 0.85), clockLines = seg(3*14*2, 1);
const beads = M3.points(3*14, 0.075), cores = M3.points(3, 0.5); [beads, cores].forEach(p => { p.frustumCulled = false; scene.add(p); });
const labels = RUNS.map(k => { const d = document.createElement('div'); d.className = 'lab'; $('labels').appendChild(d); return d; });
const ramp = x => M3.colour.ramp(Math.max(0, Math.min(1, x)));
const CIRC = [0, 1, 2].map(ax => Array.from({ length:NSEG + 1 }, (_, s) => { const t = TAU*s/NSEG, c = Math.cos(t), si = Math.sin(t); return ax === 0 ? [c, si, 0] : ax === 1 ? [c, 0, si] : [0, c, si]; }));
function frameOf(run, eps){ const F = D[run].frames; let lo = 0, hi = F.length - 1; if(eps <= F[0].eps) return 0; if(eps >= F[hi].eps) return hi; while(hi - lo > 1){ const m = (lo + hi) >> 1; if(F[m].eps <= eps) lo = m; else hi = m; } return lo; }
function origin(k){ return [(k - 1)*GAP + O.panx/100*6, O.pany/100*4, 0]; }
function resize(){ const w = stage.clientWidth, h = stage.clientHeight; renderer.setSize(w, h, false); camera.aspect = w/h; camera.updateProjectionMatrix(); }
function orbit(){ const base = 15, radius = base*100/O.zoom; camera.position.set(radius*Math.sin(az)*Math.cos(el), radius*Math.sin(el), radius*Math.cos(az)*Math.cos(el)); camera.lookAt(0, 0, 0); camera.updateMatrixWorld(); }
function draw(){ shellLines.reset(); fanLines.reset(); clockLines.reset(); const ws = 2*Math.PI/40;
  RUNS.forEach((run, k) => { const show = O.show[run], o = origin(k), F = D[run].frames, fi = frameOf(run, O.eps), f = F[fi], n = f.Ra.length, ended = O.eps > D[run].eps_end + 1e-9, nmu = D[run].nmu;
    if(!show){ for(let i=0;i<n;i++) M3.setPt(beads, k*14 + i, new T.Vector3(1e4, 1e4, 1e4), [0,0,0]); M3.setPt(cores, k, new T.Vector3(1e4, 1e4, 1e4), [0,0,0]); labels[k].style.display = 'none'; return; }
    for(let i=0;i<n;i++){ const R = f.Ra[i]*SC, horizon = f.fall[i] && f.twoMR[i] >= 1, inner = 1 - i/(n + 2), col = horizon ? [1, 1, 1] : ramp(0.12 + 0.8*Math.min(1, Math.max(0, f.C[i])/0.95)).map(v => v*(0.35 + 0.65*inner));
      if(O.show.shells) for(let ax=0;ax<3;ax++){ const C = CIRC[ax]; for(let s=0;s<NSEG;s++) shellLines.add([o[0] + R*C[s][0], o[1] + R*C[s][1], o[2] + R*C[s][2]], [o[0] + R*C[s+1][0], o[1] + R*C[s+1][1], o[2] + R*C[s+1][2]], col); }
      /* the shell's own clock: a bead on its equator turning at its lapse A against the background */
      const ang = ws*f.tau[i] + i*0.35, bp = [o[0] + R*Math.cos(ang), o[1], o[2] + R*Math.sin(ang)];
      M3.setPt(beads, k*14 + i, O.show.clocks ? new T.Vector3(...bp) : new T.Vector3(1e4, 1e4, 1e4), horizon ? [1,1,1] : col.map(v => Math.min(1, 1.5*v)));
      if(O.show.clocks) clockLines.add([o[0] + 0.86*R*Math.cos(ang), o[1], o[2] + 0.86*R*Math.sin(ang)], bp, col);
      /* the neutrinos on every second shell: I(μ)/mean as a flower against the outward normal at six points */
      if(nmu && O.show.fans && i % 2 === 1 && i < n - 2 && f.I){ const I = f.I[i], L = 0.1*SC*(0.7 + 0.3*R/SC), dn = f.dn[i], g = Math.min(1, 0.45 + 0.25*Math.log10(2 + Math.max(-1, dn)));
        for(const p of FAN_PTS){ const base = [o[0] + R*p[0], o[1] + R*p[1], o[2] + R*p[2]], tg = Math.abs(p[1]) > 0.5 ? [1,0,0] : [0,1,0];
          for(let j=0;j<nmu;j+=1){ const mu = -1 + (j + 0.5)*2/nmu, sn = Math.sqrt(1 - mu*mu), len = L*I[j];
            for(const side of [1, -1]){ const dir = [mu*p[0] + side*sn*tg[0], mu*p[1] + side*sn*tg[1], mu*p[2] + side*sn*tg[2]]; fanLines.add(base, [base[0] + len*dir[0], base[1] + len*dir[1], base[2] + len*dir[2]], ORANGE.map(v => 0.6*v*g*(0.35 + 0.65*Math.abs(mu)))); } } } } }
    const dp = f.dp[0], s = Math.min(1, 0.25 + 0.2*Math.log10(1 + Math.max(0, dp)));
    M3.setPt(cores, k, new T.Vector3(...o), ended && D[run].status === 'BH' ? [1, 1, 1] : [s, 0.85*s, 0.6*s]);
    const p = new T.Vector3(o[0], o[1] + 2.1, o[2]).project(camera); labels[k].style.display = O.show.names ? '' : 'none'; labels[k].style.transform = 'translate(' + ((p.x + 1)/2*stage.clientWidth) + 'px,' + ((1 - p.y)/2*stage.clientHeight) + 'px)';
    labels[k].innerHTML = NAME[run] + '<br><span>' + (D[run].status === 'BH' && O.eps >= D[run].eps_end ? 'apparent horizon at ε = ' + D[run].eps_end.toFixed(2) : (run === 'nu' && O.eps > 4.6 ? 'bounced, dispersing' : 'ε = ' + Math.min(O.eps, D[run].eps_end).toFixed(2))) + '</span>'; });
  shellLines.done(); fanLines.done(); clockLines.done(); [beads, cores].forEach(M3.flush); }
const f3 = x => Number.isFinite(x) ? x.toFixed(3) : '—', row = (a, b) => '<div class="row"><span>' + a + '</span><b>' + b + '</b></div>';
function numbers(){ let h = row('ε = 1/(aH r_m), the Hubble radius over the size of the lump; horizon crossing at 1', O.eps.toFixed(2));
  RUNS.forEach(run => { const F = D[run].frames, f = F[frameOf(run, O.eps)], im = f.C.indexOf(Math.max(...f.C)), rm = D[run].r.indexOf(1.0012);
    let s = 'largest C on the shells ' + f3(Math.max(...f.C)) + ' · centre plasma ρ/ρ_b ' + (1 + f.dp[0]).toPrecision(3) + ' · centre clock A ' + f3(f.A[0]);
    if(f.I){ const I = f.I[rm >= 0 ? rm : 7], nmu = I.length; let out = 0, inn = 0; for(let j=0;j<nmu;j++){ if(j >= nmu/2) out += I[j]; else inn += I[j]; } s += ' · centre ν ρ/ρ_b ' + (1 + f.dn[0]).toPrecision(3) + ' · ν out/in at r_m ' + f3(out/inn); }
    h += row(NAME[run] + (D[run].status === 'BH' ? ' → horizon at ε ' + D[run].eps_end.toFixed(2) : ' → no horizon to ε 9'), s); });
  $('num').innerHTML = h; charts(); }
function charts(){ const W1 = $('c1'), W2 = $('c2');
  [[W1, 'C'], [W2, 'rho']].forEach(([cv, kind]) => { const g = cv.getContext('2d'), W = cv.width = cv.clientWidth*devicePixelRatio, H = cv.height = 120*devicePixelRatio, x = e => 6 + (e/9)*(W - 12);
    const y = kind === 'C' ? v => H - 6 - v/1.05*(H - 12) : v => H - 6 - (Math.log10(Math.max(0.3, v)) + 0.53)/(4.3 + 0.53)*(H - 12);
    g.clearRect(0, 0, W, H); g.font = (10*devicePixelRatio) + 'px system-ui'; g.fillStyle = '#5c6b80';
    if(kind === 'C'){ g.strokeStyle = 'rgba(242,193,78,.55)'; g.setLineDash([4*devicePixelRatio, 4*devicePixelRatio]); g.beginPath(); g.moveTo(x(0), y(2/3)); g.lineTo(x(9), y(2/3)); g.stroke(); g.setLineDash([]); g.fillText('2/3', x(8.6), y(2/3) - 3);
      [[0.498, 'δc fluid 0.498'], [0.528, 'δc with ν 0.528']].forEach(([v, t]) => { g.fillStyle = '#7f8ca0'; g.fillRect(x(0), y(v), 6*devicePixelRatio, 1); }); }
    const plot = (pts, col, dash, w) => { g.strokeStyle = col; g.lineWidth = (w || 1.4)*devicePixelRatio; g.setLineDash(dash ? [5*devicePixelRatio, 3*devicePixelRatio] : []); g.beginPath(); pts.forEach((p, i) => i ? g.lineTo(x(p[0]), y(p[1])) : g.moveTo(x(p[0]), y(p[1]))); g.stroke(); g.setLineDash([]); };
    RUNS.forEach(run => { if(!O.show[run]) return; const cu = D[run].curve, dash = run === 'nu535';
      if(kind === 'C') plot(cu.map(r => [r[0], r[1]]), CURVE_COL[run], dash);
      else { plot(cu.map(r => [r[0], 1 + r[2]]), CURVE_COL[run], dash); if(run !== 'fluid') plot(cu.map(r => [r[0], 1 + r[3]]), '#ffa040', dash); }
      if(D[run].status === 'BH'){ const l = cu[cu.length - 1]; g.fillStyle = '#fff'; g.beginPath(); g.arc(x(l[0]), y(kind === 'C' ? l[1] : 1 + l[2]), 3*devicePixelRatio, 0, TAU); g.fill(); } });
    g.strokeStyle = 'rgba(255,255,255,.6)'; g.lineWidth = 1; g.beginPath(); g.moveTo(x(O.eps), 0); g.lineTo(x(O.eps), H); g.stroke(); }); }
function frame(now){ requestAnimationFrame(frame); const dt = Math.min(0.06, (now - last)/1000 || 0); last = now;
  if(O.playing){ O.eps += dt*O.speed*0.6; if(O.eps > 9) O.eps = 0.1; $('eps').value = O.eps; }
  orbit(); draw(); if(Math.floor(now/120) !== Math.floor((now - dt*1000)/120) || !O.playing) numbers(); renderer.render(scene, camera); }
function ui(){ document.querySelectorAll('[data-show]').forEach(b => b.setAttribute('aria-pressed', !!O.show[b.dataset.show])); $('play').textContent = O.playing ? 'Pause' : 'Play'; $('zoom').value = Math.round(O.zoom); $('panx').value = Math.round(O.panx); $('pany').value = Math.round(O.pany); }
document.body.addEventListener('click', ev => { const b = ev.target.closest('button'); if(!b) return;
  if(b.dataset.show){ O.show[b.dataset.show] = !O.show[b.dataset.show]; }
  else if(b.id === 'play') O.playing = !O.playing; else if(b.id === 'restart'){ O.eps = 0.1; }
  else if(b.dataset.jump){ O.eps = +b.dataset.jump; O.playing = false; $('eps').value = O.eps; }
  else if(b.id === 'zin') O.zoom = Math.min(400, O.zoom*1.25); else if(b.id === 'zout') O.zoom = Math.max(25, O.zoom/1.25); else if(b.id === 'reset'){ O.zoom = 100; O.panx = O.pany = 0; az = 0.35; el = 0.32; }
  ui(); numbers(); });
$('eps').addEventListener('input', e => { O.eps = +e.target.value; O.playing = false; ui(); numbers(); }); $('speed').addEventListener('input', e => { O.speed = +e.target.value; });
$('zoom').addEventListener('change', e => { O.zoom = Math.max(25, Math.min(400, +e.target.value || 100)); }); $('panx').addEventListener('change', e => { O.panx = +e.target.value || 0; }); $('pany').addEventListener('change', e => { O.pany = +e.target.value || 0; });
let drag = null; canvas.addEventListener('pointerdown', e => { drag = { x:e.clientX, y:e.clientY, az, el }; canvas.setPointerCapture(e.pointerId); }); canvas.addEventListener('pointermove', e => { if(!drag) return; az = drag.az - (e.clientX - drag.x)*0.006; el = Math.max(-1.3, Math.min(1.3, drag.el + (e.clientY - drag.y)*0.006)); }); canvas.addEventListener('pointerup', () => { drag = null; });
canvas.addEventListener('wheel', e => { e.preventDefault(); O.zoom = Math.max(25, Math.min(400, O.zoom*(e.deltaY < 0 ? 1.1 : 1/1.1))); ui(); }, { passive:false });
addEventListener('resize', resize); resize(); ui(); numbers(); requestAnimationFrame(frame);
window.__NU3D = { O };
})();
