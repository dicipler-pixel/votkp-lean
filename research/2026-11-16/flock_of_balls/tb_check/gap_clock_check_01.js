// SCRIPT: GAP-CLOCK-CHECK-01
// Checks the Three Balls on the Field v1 matrix (MM-MATH-V1, TB-MATH-V1, unchanged copies) for three things Jeromie asked about:
//  C1  does a signal take time to cross the gap, or does it arrive at once?
//      Why this decides it: with a finite signal speed v and link length d, the light in B must be exactly zero for t < d/v.
//      If instead rho_B(t) grows like t^2 from t = 0, the hop is instantaneous (amplitude c*t after time t).
//      Kill line for "instantaneous": rho_B(t) == 0 for some t > 0 (then the model already has a light-cone).
//  C2  does each ball keep its own clock?  The balls sit one VOTKP peel step apart (a boost of rapidity r, radar ratio z = e^r).
//      Why this decides it: the matrix gives every ball the same level spacing omega in ONE shared time t; with a clock per ball,
//      a ball one step out runs at its own rate and the light it receives is shifted by the step ratio, so A and B are no longer
//      exactly in tune. We print the shared-clock resonance and the most light B can hold if the step's ratio z detunes it
//      (two-level Rabi bound c^2/(c^2 + (Delta/2)^2) with Delta = omega(1 - 1/z)).  Kill line for "one shared clock": any per-ball
//      time variable used in deriv().
//  C3  does the gap between faces enter the link?  Link strength is c0*sech(d/2) from the centre distance d only.
//      Why this decides it: in the Light at the Hypersurface model (M3, film_is_oplus) light crosses a real gap of width delta = arccosh g
//      only by tunnelling, |t|^2 ~ e^{-2 k delta}. If the link strength does not change when the faces open a gap, the gap is not in the matrix.
//      Kill line for "gap absent": link strength depends on g or delta.
//  C4  the per-ball offset clocks tau_i (Dirac Time: the clock is read from memory) after a kick, and the speed limit tau'^2 <= 4 g S.
const MM = require('../mm/mm_math_v1.js'), TB = require('./tb_math_v1.js');
const fmt = (x, n) => (x === null || !isFinite(x)) ? String(x) : (Math.abs(x) < 1e-3 && x !== 0 ? x.toExponential(n||2) : x.toFixed(n||4));
const r0 = [Math.log(3), Math.log(5)];                 // hold drive, zbar = (3, 5): the default I and J steps
const W = TB.makeWorld(r0);
console.log('steps r_I, r_J =', r0.map(x => fmt(x)).join(', '), '  link lengths d (AB, AC, BC) =', W.links.map(l => fmt(l.d)).join(', '), '  strengths c =', W.links.map(l => fmt(l.c)).join(', '));

// C1
console.log('\nC1  light in B and C after a kick at A, at very early times (shared clock t):');
for(const T of [1e-3, 3e-3, 1e-2, 3e-2]){ let S = MM.initState(W, { source:0, noSea:true }); const n = 50, h = T/n; for(let k=0;k<n;k++) S = MM.rk4(W, S, h);
  const rB = MM.lightDensity(S,1), rC = MM.lightDensity(S,2); console.log('   t =', fmt(T,3), '  rho_B =', fmt(rB,3), '  rho_B/t^2 =', fmt(rB/T/T,4), '  rho_C =', fmt(rC,3), '  rho_C/t^2 =', fmt(rC/T/T,4), '  c_AB^2 =', fmt(W.links[0].c**2,4)); }

// C2
console.log('\nC2  clocks: level spacing of each ball in the shared time t, and what the step ratio does to the tuning:');
const om = W.opts.omega; W.d.forEach((v,i) => console.log('   ball', TB.NAMES[i], ' spacing 2|d| =', fmt(2*Math.hypot(...v),6)));
{ let S = MM.initState(W, { source:0, noSea:true }), mx = [0,0,0]; for(let k=0;k<4000;k++){ S = MM.rk4(W, S, 0.005); for(let i=0;i<3;i++) mx[i] = Math.max(mx[i], MM.lightDensity(S,i)); }
  console.log('   shared clock, kick A, most light ever reaching B, C (t <= 20):', mx.slice(1).map(x => fmt(x,3)).join(', ')); }
W.links.slice(0,2).forEach((l, k) => { const z = Math.exp(r0[k]), Delta = om*(1 - 1/z), c = l.c, bound = c*c/(c*c + Delta*Delta/4);
  console.log('   link A-'+TB.NAMES[k+1]+': z =', fmt(z,3), ' detuning omega(1-1/z) =', fmt(Delta,4), ' link c =', fmt(c,4), ' -> most light the far ball could take (two-level bound) =', fmt(bound,3)); });

// C3
console.log('\nC3  does the gap between faces change the link?  faces at h = r/2 on the I and J arms, g = sinh h_I sinh h_J (g > 1: a gap delta = arccosh g):');
for(const zz of [[3,5],[5,7],[7,9],[9,13],[13,13]]){ const r = zz.map(Math.log), Wz = TB.makeWorld(r), g = Math.sinh(r[0]/2)*Math.sinh(r[1]/2), del = g > 1 ? Math.acosh(g) : 0;
  console.log('   z =', zz.join(','), ' g =', fmt(g,4), g > 1 ? ' gap delta = '+fmt(del,4) : ' faces cross (no gap)', '  link c (AB, AC, BC) =', Wz.links.map(l => fmt(l.c,4)).join(', '), '  c0 sech(d/2) from d only =', Wz.links.map(l => fmt(0.5/Math.cosh(l.d/2),4)).join(', ')); }

// C4
console.log('\nC4  each ball\'s offset clock tau_i (Dirac Time: read from memory) after a kick at A, with the sea on:');
{ let S = MM.initState(W, { source:0 }); const C0 = MM.ballCensus(W, S).map(c => c.tau);
  for(let k=1;k<=600;k++){ S = MM.rk4(W, S, 0.01); if(k % 100 === 0){ const C = MM.ballCensus(W, S), D = MM.deriv(W, S), g = MM.seaSpeed(W, S);
      const rows = [0,1,2].map(i => { const td = MM.tauDot(W, S, D, i); return TB.NAMES[i]+': tau-tau0 '+fmt(C[i].tau - C0[i],3)+' tau\' '+fmt(td,3)+' limit '+fmt(td*td/(4*g*C[i].S),3); });
      console.log('   t =', fmt(S.t,2), ' |', rows.join(' | ')); } } }
console.log('\n   deriv() advances every ball with the same step h in the one time t: no ball uses its own tau as its time.');
