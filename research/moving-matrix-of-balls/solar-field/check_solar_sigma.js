// SCRIPT: SF-SIGMA-CHECK-V1 — the opposite orientation: admittance rising outward; shares averaged over one perfect year (node, no page)
const LH = require('../surprise/src/lh_math.js'), SF = require('./sf_math_v1.js'), PI = Math.PI, RAD = SF.R0/2, NB = 900, OPT = { maxEv:14, fmin:2e-5, smax:9, maxSeg:160 };
function cone(u, beta, n){ const a0 = Math.abs(u[2]) < 0.9 ? [0,0,1] : [1,0,0], e1 = [u[1]*a0[2]-u[2]*a0[1], u[2]*a0[0]-u[0]*a0[2], u[0]*a0[1]-u[1]*a0[0]], l = Math.hypot(...e1); for(let k=0;k<3;k++) e1[k] /= l;
  const e2 = [u[1]*e1[2]-u[2]*e1[1], u[2]*e1[0]-u[0]*e1[2], u[0]*e1[1]-u[1]*e1[0]], out = [], ga = PI*(3 - Math.sqrt(5)), cb = Math.cos(beta);
  for(let i=0;i<n;i++){ const c = 1 - (1 - cb)*(i + 0.5)/n, sn = Math.sqrt(1 - c*c), t = ga*i; out.push([0,1,2].map(k => c*u[k] + sn*(Math.cos(t)*e1[k] + Math.sin(t)*e2[k]))); } return out; }
function share(S, p){ const c = SF.centre(p), n = Math.hypot(c[1],c[2],c[3]), u = [c[1]/n,c[2]/n,c[3]/n], alpha = Math.asin(Math.min(1, Math.sinh(RAD)/Math.sinh(Math.max(RAD,p.d)))), beta = Math.min(PI, 3*alpha+0.02), sky = (1-Math.cos(beta))/2;
  const dirs = cone(u, beta, NB), TR = LH.trace(S, dirs, OPT), best = new Float32Array(NB); for(const s of TR.segs){ if(s.flux > best[s.ray] && SF.segDist(c, LH.mv(s.g,s.X), LH.mv(s.g,s.v), s.s) <= RAD) best[s.ray] = s.flux; } let t = 0; for(let i=0;i<NB;i++) t += best[i]; return sky*t/NB; }
const out = {};
for(const [tag, D, z] of [['perfect', {steps:0,ellipse:0,tilt:0,timing:0}, [3,3,3]], ['measured steps', {steps:1,ellipse:0,tilt:0,timing:0}, [3,3,3]]]) for(const sigma of [1, -1]){
  const P = { zbar:z, amp:0, T:[8,13,21], ph:[0,2*PI/3,4*PI/3], sigma, Tphi:9, Tchi:55 }, S = LH.feed(P, 0), acc = [[],[],[],[]];
  for(let k=0;k<24;k++){ const PL = SF.state(SF.T0*k/24, D); PL.forEach((p,b) => acc[b].push(share(S, p))); }
  const st = SF.state(0, D); const row = acc.map((a,b) => ({ name:st[b].name, mean:+(a.reduce((x,y)=>x+y,0)/a.length).toExponential(2), min:+Math.min(...a).toExponential(2), max:+Math.max(...a).toExponential(2), open:+SF.freeShare(st[b].d, RAD).toExponential(2) }));
  out[tag + (sigma > 0 ? ' | admittance falls outward' : ' | admittance rises outward')] = row; console.log(tag, sigma > 0 ? 'falls outward' : 'rises outward'); row.forEach(r => console.log('  ', JSON.stringify(r))); }
require('fs').writeFileSync('check_solar_sigma.out.json', JSON.stringify(out, null, 1));
