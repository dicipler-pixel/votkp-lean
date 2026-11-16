// SCRIPT: SF-T1 — checks of the solar field maths (node)
const SF = require('./sf_math_v1.js'), LH = require('../surprise/src/lh_math.js');
const perfect = { steps:0, ellipse:0, tilt:0, timing:0 }, real = { steps:1, ellipse:1, tilt:1, timing:1 };
let st = SF.state(0, perfect); console.log('perfect: distances', st.map(p => p.d.toFixed(4)).join(' '), ' periods', st.map(p => p.T).join(' '));
// centre sits at hyperbolic distance d from the Sun; cell and cellInv are inverse
let w = 0, w2 = 0; for(const D of [perfect, real]) for(const day of [0, 37, 200, 555]) for(const p of SF.state(day, D)){ const c = SF.centre(p); w = Math.max(w, Math.abs(Math.acosh(c[0]) - p.d)); const I = SF.mm(SF.cellInv(p), SF.cell(p)); for(let i=0;i<4;i++) for(let j=0;j<4;j++) w2 = Math.max(w2, Math.abs(I[i][j] - (i===j?1:0))); }
console.log('centre at distance d: worst', w.toExponential(1), ' cell * cellInv = 1: worst', w2.toExponential(1));
// segDist against brute force
let w3 = 0; for(let k=0;k<200;k++){ const r = () => Math.random()*2-1, d = [r(),r(),r()], n = Math.hypot(...d), V = [0, d[0]/n, d[1]/n, d[2]/n], P = [1,0,0,0], p = SF.state(k*7, real)[k%4], c = SF.centre(p); let bf = 1e9; for(let s=0;s<=6;s+=0.0005) bf = Math.min(bf, Math.acosh(Math.max(1, SF.mink(c, [Math.cosh(s), V[1]*Math.sinh(s), V[2]*Math.sinh(s), V[3]*Math.sinh(s)])))); w3 = Math.max(w3, Math.abs(bf - SF.segDist(c, P, V, 6))); }
console.log('least distance to a ray vs brute force: worst', w3.toExponential(1));
// free share against a Monte Carlo of straight rays from the Sun
const p = SF.state(0, perfect)[1], c = SF.centre(p), rad = SF.R0/2; let hit = 0, N = 400000; for(let k=0;k<N;k++){ const z = 2*Math.random()-1, a = 2*Math.PI*Math.random(), s = Math.sqrt(1-z*z); if(SF.segDist(c, [1,0,0,0], [0, s*Math.cos(a), s*Math.sin(a), z], 12) <= rad) hit++; }
console.log('free share at Venus (perfect): formula', SF.freeShare(p.d, rad).toFixed(5), ' Monte Carlo', (hit/N).toFixed(5));
// Kepler: real Mercury distance swings between perihelion and aphelion ratios
let mn = 9, mx = 0; for(let day=0; day<88; day+=0.25){ const q = SF.state(day, real)[0]; mn = Math.min(mn, q.rho); mx = Math.max(mx, q.rho); } console.log('Mercury distance over a: min', mn.toFixed(4), 'max', mx.toFixed(4), ' (1 ∓ e = 0.794, 1.206)');
st = SF.state(0, real); console.log('real: distances from the Sun centre', st.map(p => p.name + ' ' + p.d.toFixed(3)).join('  '), ' light minutes', st.map(p => (p.lightSec/60).toFixed(2)).join(' '));
console.log('real steps between neighbours', [0,1,2].map(i => (Math.log(SF.BODIES[i+1].a/SF.BODIES[i].a)).toFixed(3)).join(' '));
