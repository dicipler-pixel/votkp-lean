// SCRIPT: FL-CHECK-02
// Checks of FL-MATH-V1 (the flock of balls with real gaps and a clock per ball). Each line: why it decides the point, the kill line, then the run.
const MM = require('../mm/mm_math_v1.js'), FL = require('./fl_math_v2.js');
const f = (x, n) => (x === null || x === undefined || !isFinite(x)) ? String(x) : (Math.abs(x) < 1e-3 && x !== 0 ? x.toExponential(2) : x.toFixed(n == null ? 4 : n));
let kills = 0; const line = (name, ok, txt) => { if(!ok) kills++; console.log((ok ? 'HOLDS  ' : 'KILLED ') + name + '  ' + txt); };

// K1 the signal takes the link's length in time. Why: with a real travel time, ball B must hold exactly zero light before t = d_AB.
//    Kill: any light in B (> 1e-30) before d_AB - 2h, or no light by d_AB + 4h.
{ const W = FL.makeWorld({ N:3 }), S = FL.initState(W, { source:0 }), h = W.opts.h, first = [null,null,null], before = [0,0,0];
  for(let k=0;k<1200;k++){ FL.step(W, S); for(let i=1;i<3;i++){ const e = FL.ballLight(S, i); if(S.t < W.links[i-1].d - 2*h) before[i] = Math.max(before[i], e); if(first[i] === null && e > 1e-30) first[i] = S.t; } }
  for(let i=1;i<3;i++){ const d = W.links[i-1].d; line('K1 travel time A->'+FL.NAMES[i], before[i] === 0 && first[i] !== null && Math.abs(first[i]-d) <= 4*h, 'link length d = '+f(d)+', light in '+FL.NAMES[i]+' before then = '+before[i]+', first light at t = '+f(first[i])); } }

// K2 the books. Why: every step is a product of exact rotations, so light in balls + light in gaps must stay 1.
//    Kill: |total - 1| > 1e-10 at any time up to t = 200, for N = 3 and N = 7.
for(const N of [3, 7]){ const W = FL.makeWorld({ N }), S = FL.initState(W, { source:0 }); let worst = 0, minB = 1; for(let k=0;k<40000;k++){ FL.step(W, S); if(k % 50 === 0){ const b = FL.books(W, S); worst = Math.max(worst, Math.abs(b.total-1)); minB = Math.min(minB, b.balls); } }
  line('K2 books, N = '+N, worst < 1e-10, 'largest |balls + gaps - 1| to t = 200: '+worst.toExponential(1)+'; least light ever held in the balls '+f(minB,3)); }

// K3 one face is one reflecting step. Why: a pulse sent into the A-B link must split R = Gamma^2 back, T = 1 - Gamma^2 on, with Gamma = tanh(r/2) = (z-1)/(z+1).
//    Kill: either fraction off by more than 1e-12.
{ const W = FL.makeWorld({ N:3, gamma:0 }), S = FL.initState(W, {}), l = W.links[0], sg = l.segs[0]; sg.f[4*((sg.head-1+sg.n)%sg.n)] = 1;   /* unit amplitude just entered at ball A's side */
  const n = l.segs[0].n + Math.floor(l.segs[1].n/2); for(let k=0;k<n;k++) FL.step(W, S);
  let eb = 0, ef = 0; for(let k=0;k<4*l.segs[0].n;k++) eb += l.segs[0].b[k]**2; for(let k=0;k<4*l.segs[1].n;k++) ef += l.segs[1].f[k]**2;
  const G = (3-1)/(3+1); line('K3 face A|B (z = 3)', Math.abs(eb-G*G) < 1e-12 && Math.abs(ef-(1-G*G)) < 1e-12, 'returned '+f(eb,12)+' (Gamma^2 = '+f(G*G,12)+'), passed '+f(ef,12)+' (1 - Gamma^2 = '+f(1-G*G,12)+')'); }

// K4 the gap between the faces. Why: on an arm-arm link the light crosses face a, the centre cell, face b. When the faces stand apart
//    (g > 1) the passed fraction must fall by sech^2(k_g delta); when they meet (g <= 1) it must not. Continuous at the wall g = 1.
//    Kill: passed fraction differs from (1-Ga^2)(1-Gb^2) sech^2(k_g delta) by more than 1e-12 (first pass, no echoes yet).
for(const z of [[3,5,7],[5,7,9],[7,9,11],[9,13,13],[5.8284271247,5.8284271247,7]]){ const W = FL.makeWorld({ N:3, z, gamma:0 }), S = FL.initState(W, {}), l = W.links[2], sg = l.segs[0]; sg.f[4*((sg.head-1+sg.n)%sg.n)] = 1;
  const last = l.segs[l.segs.length-1]; let nn = 0; l.segs.forEach((s,k) => nn += k < l.segs.length-1 ? s.n : Math.floor(s.n/2)); for(let k=0;k<nn;k++) FL.step(W, S);
  let ef = 0; for(let k=0;k<4*last.n;k++) ef += last.f[k]**2; const Ga = Math.tanh(Math.log(z[0])/2), Gb = Math.tanh(Math.log(z[1])/2), want = (1-Ga*Ga)*(1-Gb*Gb)/(l.delta > 0 ? Math.cosh(W.opts.kgap*l.delta)**2 : 1);
  line('K4 gap, z = '+z.slice(0,2).map(x => f(x,3)).join(','), Math.abs(ef-want) < 1e-12, 'g = '+f(l.g)+(l.delta > 0 ? ', gap delta = '+f(l.delta) : ', faces meet')+', link length '+f(l.d)+', faces at '+l.marks.filter(m => m.kind==='face').map(m => f(m.s,3)).join(' and ')+', passed first time '+f(ef,10)+' (formula '+f(want,10)+')'); }

// K5 a clock per ball. Why: a ball left alone (ports closed, field held) must turn its light spin about its field at omega x rate, rate = 1 at the centre and 1/z one step out.
//    Kill: measured rate off by more than 1e-9, or ratio centre/arm not z.
{ const W = FL.makeWorld({ N:4, gamma:0, push:'off', torque:0 }), rates = []; for(let i=0;i<4;i++){ const S = FL.initState(W, { source:i }); let p0 = FL.clockPhase(S, i).phase, tot = 0; for(let k=0;k<2000;k++){ FL.step(W, S); const p = FL.clockPhase(S, i).phase; let dp = p - p0; while(dp > Math.PI) dp -= 2*Math.PI; while(dp < -Math.PI) dp += 2*Math.PI; tot += dp; p0 = p; } rates.push(Math.abs(tot)/S.t); }
  const want = W.balls.map(b => W.opts.omega*b.rate); let worst = 0; rates.forEach((x,i) => worst = Math.max(worst, Math.abs(x-want[i])));
  line('K5 clocks', worst < 1e-9, 'measured rates A,B,C,D = '+rates.map(x => f(x,9)).join(', ')+'; omega/z = '+want.map(x => f(x,9)).join(', ')+'; ratios A/B, A/C, A/D = '+[1,2,3].map(i => f(rates[0]/rates[i],6)).join(', ')); }

// K6 rest. Why: with no light, nothing should move. Kill: any ball field turns more than 1e-9 by t = 50.
{ const W = FL.makeWorld({ N:7 }), S = FL.initState(W, {}); let mv = 0; for(let k=0;k<10000;k++) FL.step(W, S); for(let i=0;i<W.N;i++) mv = Math.max(mv, FL.tilt(W, S, i)); line('K6 rest, N = 7', mv < 1e-9, 'largest turn with no light '+mv.toExponential(1)+', rest residual '+W.restResidual.toExponential(1)); }

// K6b the retarded face push (kept only as an option). Why: a push that arrives late with no field carrying it is not energy-booked;
//    if rest is unstable under it, the balls would swing with no light at all. Reported, not a kill line for the default model.
{ const W = FL.makeWorld({ N:7, push:'retarded' }), S = FL.initState(W, {}); const tr = []; for(let k=0;k<20000;k++){ FL.step(W, S); if((k+1) % 5000 === 0){ let mv = 0; for(let i=0;i<W.N;i++) mv = Math.max(mv, FL.tilt(W, S, i)); tr.push('t='+f(S.t,0)+': '+mv.toExponential(1)); } } console.log('NOTE   K6b retarded push, N = 7, no light: largest field turn  '+tr.join('  ')); }

// K7 step size. Why: the scheme is exact in the gaps and first order at the ports, so halving h should about halve the change in a readout.
//    Kill: the light held in B at t = 6 changes by more than 0.02 between h = 0.005 and h = 0.0025.
{ const v = [0.01, 0.005, 0.0025].map(h => { const W = FL.makeWorld({ N:3, h }), S = FL.initState(W, { source:0 }); FL.advance(W, S, 6); return FL.ballLight(S, 1); });
  line('K7 step size', Math.abs(v[1]-v[2]) < 0.02, 'light in B at t = 6 for h = 0.01, 0.005, 0.0025: '+v.map(x => f(x,5)).join(', ')); }

// Exploration (no kill line): how much light each ball ever takes, and how in step the flock is, with clocks at z against all clocks equal.
console.log('\nExploration: kick A, run to t = 300. Most light ever in each ball; time-average share; order parameter r (Kuramoto, weighted) mean and spread over the last 100.');
for(const N of [3, 4, 7]) for(const clocks of ['z', 'equal']){ const W = FL.makeWorld({ N, clocks }), S = FL.initState(W, { source:0 }), mx = new Array(W.N).fill(0), av = new Array(W.N).fill(0); let cnt = 0, rs = [], gapAv = 0, tl = new Array(W.N).fill(0);
  for(let k=0;k<60000;k++){ FL.step(W, S); if(k % 20 === 0){ cnt++; for(let i=0;i<W.N;i++){ const e = FL.ballLight(S,i); mx[i] = Math.max(mx[i], e); av[i] += e; tl[i] = Math.max(tl[i], FL.tilt(W,S,i)); } gapAv += FL.books(W,S).gaps; if(S.t > 200) rs.push(FL.order(W,S).r); } }
  const m = rs.reduce((a,b) => a+b, 0)/rs.length, sd = Math.sqrt(rs.reduce((a,b) => a+(b-m)**2, 0)/rs.length);
  console.log('  N = '+N+', clocks '+clocks.padEnd(5)+' | most light '+mx.map(x => f(x,2)).join(' ')+' | mean share '+av.map(x => f(x/cnt,2)).join(' ')+' | in gaps '+f(gapAv/cnt,2)+' | largest field turn '+tl.map(x => f(x,2)).join(' ')+' | r = '+f(m,3)+' +- '+f(sd,3)); }
{ const W = FL.makeWorld({ N:7 }), M = FL.modes(W); console.log('\nReference, instantaneous matrix on the same 7 balls: leading eigenvalue '+f(M.vals[M.lead])+', shares '+M.share[M.lead].map(x => f(x,3)).join(' ')+', margin '+f(M.margin)); }
console.log('\n'+(kills ? kills+' line(s) KILLED' : 'all kill lines hold'));
