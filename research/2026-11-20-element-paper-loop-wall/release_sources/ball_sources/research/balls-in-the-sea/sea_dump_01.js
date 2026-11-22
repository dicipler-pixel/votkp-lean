// SCRIPT: SEA-DUMP-01
// Writes, for one flock world, everything the sea runs need: the one-step map T of the light (transport, faces, gaps, ball ports; the
// balls' own clocks left out), the layout of the state, the links, the rest directions for three clock choices, and the link matrix A of
// the all-at-once machine. Jeromie Beasley. 16 Nov 2026. AI-assisted. Uses FL-MATH-V2 and MM-MATH-V1 unchanged.
const MM = require('../mm/mm_math_v1.js'), FL = require('./fl_math_v2.js'), fs = require('fs');
const [,, Ns, sign, hs, out] = process.argv, N0 = +Ns, h = +hs;
const W = FL.makeWorld({ N:N0, h, push:'off', torque:0, clocks:'z', armSign:sign === 'v1' ? 'asBuiltV1' : 'v2' }), S = FL.initState(W, {}), N = W.N;
/* layout: ball i -> 2 complex; then per link, per segment: forward samples (oldest first), backward samples (oldest first), 2 complex each */
let M = 2*N; const off = []; W.links.forEach(l => l.segs.forEach(sg => { off.push([M, M + 2*sg.n]); M += 4*sg.n; }));
const segs = []; W.links.forEach(l => l.segs.forEach(sg => segs.push(sg)));
function write(k){ S.psi.forEach(p => p.fill(0)); segs.forEach(sg => { sg.f.fill(0); sg.b.fill(0); sg.head = 0; }); S.d = W.balls.map(() => [0, 0, 1e-13]);
  if(k < 2*N){ S.psi[k >> 1][2*(k & 1)] = 1; return; }
  for(let q=0;q<segs.length;q++){ const sg = segs[q], [of, ob] = off[q]; if(k >= of && k < of + 2*sg.n){ const j = (k - of) >> 1, c = (k - of) & 1; sg.f[4*j + 2*c] = 1; return; } if(k >= ob && k < ob + 2*sg.n){ const j = (k - ob) >> 1, c = (k - ob) & 1; sg.b[4*j + 2*c] = 1; return; } } }
function read(){ const re = new Float64Array(M), im = new Float64Array(M); for(let i=0;i<N;i++) for(let c=0;c<2;c++){ re[2*i+c] = S.psi[i][2*c]; im[2*i+c] = S.psi[i][2*c+1]; }
  for(let q=0;q<segs.length;q++){ const sg = segs[q], [of, ob] = off[q]; for(let j=0;j<sg.n;j++){ const s = (sg.head + j) % sg.n; for(let c=0;c<2;c++){ re[of+2*j+c] = sg.f[4*s+2*c]; im[of+2*j+c] = sg.f[4*s+2*c+1]; re[ob+2*j+c] = sg.b[4*s+2*c]; im[ob+2*j+c] = sg.b[4*s+2*c+1]; } } } return [re, im]; }
const rows = [], cols = [], vr = [], vi = [];
for(let k=0;k<M;k++){ write(k); FL.step(W, S); const [re, im] = read(); for(let r=0;r<M;r++) if(Math.abs(re[r]) > 1e-15 || Math.abs(im[r]) > 1e-15){ rows.push(r); cols.push(k); vr.push(re[r]); vi.push(im[r]); } }
/* rest directions for three clock choices: z (rate 1/z), equal (rate 1), dilation (rate 1/cosh r) */
function rest(rate){ W.balls.forEach((b, i) => b.rate = rate(b)); let seed = 11; const rnd = () => (seed = (seed*16807) % 2147483647)/2147483647 - 0.5;
  W.d = W.balls.map(b => { const v = [0.2*rnd(), 0.2*rnd(), 1 + 0.2*rnd()], m = Math.hypot(...v); return v.map(x => x/m*W.opts.omega*b.rate/2); }); const R = MM.restState(W, { iters:60000, eta:0.08, withSea:false, tol:1e-12 }); return { d:R.d, residual:R.residual, rate:W.balls.map(b => b.rate) }; }
const clocks = { z:rest(b => Math.exp(-b.r)), equal:rest(() => 1), dilation:rest(b => 1/Math.cosh(b.r)) };
const H0 = MM.denseH(W, W.balls.map(() => [0,0,0]));
fs.writeFileSync(out, JSON.stringify({ N, M, h, omega:W.opts.omega, gamma:W.opts.gamma, kappa:W.opts.kappa, sign, names:W.balls.map(b => b.name), r:W.balls.map(b => b.r),
  links:W.links.map(l => ({ i:l.i, j:l.j, d:l.d, R:l.R, c:l.c, marks:l.marks.map(m => ({ s:m.s, rho:m.rho, kind:m.kind })) })), T:{ rows, cols, vr, vi }, clocks, A:{ re:H0.Hr.map(r => Array.from(r)), im:H0.Hi.map(r => Array.from(r)) } }));
console.log(out, 'N', N, 'M', M, 'nnz', rows.length, 'links', W.links.length, 'residuals', Object.values(clocks).map(c => c.residual.toExponential(1)).join(' '));
