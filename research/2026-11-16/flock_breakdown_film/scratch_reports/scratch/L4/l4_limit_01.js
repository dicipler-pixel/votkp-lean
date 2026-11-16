// SCRIPT: L4-LIMIT-01
// The continuous-time limit of FL.step, tested against a closed form, and the order of convergence in h.
// Setting: N = 3, ball A kicked, arm I step r = 1 exactly (z = e), arm J step huge (z = 1e9) so nothing returns from C in the run.
// Ball A has two ports. Limit equations claimed (flux amplitude b = sample / sqrt(h)):
//   d psi/dt = -i (d.sigma) psi - (gamma/2)(number of ports) psi - sqrt(gamma) * sum of arriving b_in ;  b_out = b_in + sqrt(gamma) psi.
// With the one face at r/2 (reflection rho = tanh(r/2)) the arriving light at A for r < t < 2r is rho * b_out(t - r), so
//   psi(t) = E(t) psi0                         for t < r,      E(t) = exp(-gamma t) exp(-i t d.sigma)
//   psi(t) = E(t) psi0 - rho gamma (t - r) E(t - r) psi0   for r < t < 2r.
// Why it decides the point: if FL.step converges to these equations, the error against this closed form must go to zero with h,
// and the ratio of errors on halving h gives the order (2 = first order, 4 = second order).
// Kill line (written first): error does not fall with h, or the measured decay rate of A for t < r differs from the closed discrete
// value -ln(cos^2 sqrt(gamma h))/h per port by more than 1e-9.
const FL = require('/home/claude/balls/w/fl/fl_math_v1.js');
const gamma = 0.6, r = 1, rho = Math.tanh(r/2);
function exact(d, psi0, t){ const m=Math.hypot(...d); const E=(tt,p)=>{ const c=Math.cos(m*tt), s=Math.sin(m*tt)/m, a0=p[0],a1=p[1],b0=p[2],b1=p[3];
    const yr0=d[2]*a0+d[0]*b0+d[1]*b1, yi0=d[2]*a1+d[0]*b1-d[1]*b0, yr1=d[0]*a0-d[1]*a1-d[2]*b0, yi1=d[0]*a1+d[1]*a0-d[2]*b1, e=Math.exp(-gamma*tt);
    return [e*(c*a0+s*yi0), e*(c*a1-s*yr0), e*(c*b0+s*yi1), e*(c*b1-s*yr1)]; };
  const a=E(t,psi0); if(t<=r) return a; const b=E(t-r,psi0); return a.map((x,k)=>x-rho*gamma*(t-r)*b[k]); }
console.log('A. closed form against FL.step (torque 0, push static, gamma = 0.6, two ports on A), psi_A at t = 0.8 and t = 1.5');
let prev=null;
for(const h of [0.1,0.05,0.025,0.0125,0.00625,0.003125]){ const W=FL.makeWorld({N:3,z:[Math.E,1e9,7],gamma,h,torque:0}), S=FL.initState(W,{source:0}), psi0=S.psi[0].slice(), d=S.d[0].slice();
  const out=[]; for(const T of [0.8,1.5]){ while(S.t < T - 1e-9) FL.step(W,S); const ex=exact(d,psi0,T); out.push(Math.hypot(...S.psi[0].map((x,k)=>x-ex[k]))); }
  // decay rate on t < r from the light count alone
  const W2=FL.makeWorld({N:3,z:[Math.E,1e9,7],gamma,h,torque:0}), S2=FL.initState(W2,{source:0}); const n=Math.round(0.8/h); for(let k=0;k<n;k++) FL.step(W2,S2);
  const rate=-Math.log(FL.ballLight(S2,0))/S2.t, disc=-2*Math.log(Math.cos(Math.sqrt(gamma*h))**2)/h;
  console.log('  h='+h.toFixed(6)+'  link samples AB '+W.links[0].segs.map(s=>s.n).join('+')+'  |psi_A - exact| at 0.8: '+out[0].toExponential(3)+'  at 1.5: '+out[1].toExponential(3)+(prev?'  ratios '+(prev[0]/out[0]).toFixed(3)+', '+(prev[1]/out[1]).toFixed(3):'')+'  | light decay rate of A (2 ports) '+rate.toFixed(9)+'  per port '+(rate/2).toFixed(9)+'  discrete closed form per port '+(disc/2).toFixed(9)+'  gamma = '+gamma+'  (rate/port - gamma)/h = '+((rate/2-gamma)/h).toFixed(5)+' ; gamma^2/3 = '+(gamma*gamma/3).toFixed(5));
  prev=out; }
console.log('\nB. one port alone into an endless link (scratch, the same rotation as fl_math_v1.js line 79 with nothing arriving): p <- cos(sqrt(gamma h)) p');
for(const g of [0.1,0.6,2.0]) for(const h of [0.01,0.005,0.0025]){ let p=1; const n=Math.round(10/h); for(let k=0;k<n;k++) p*=Math.cos(Math.sqrt(g*h)); const ampRate=-Math.log(p)/(n*h); console.log('  gamma='+g+' h='+h+'  amplitude decay rate '+ampRate.toFixed(8)+'  gamma/2 = '+(g/2).toFixed(8)+'  difference/h = '+((ampRate-g/2)/h).toFixed(6)+'  gamma^2/12 = '+(g*g/12).toFixed(6)); }
console.log('\nC. full nonlinear step (torque on), geometry with link lengths that are whole numbers of steps (z = e, e^2): light in B and tilt of A at t = 1.8; successive differences and their ratios');
{ const hs=[0.1,0.05,0.025,0.0125,0.00625,0.003125], v=hs.map(h=>{ const W=FL.makeWorld({N:3,z:[Math.E,Math.E**2,7],gamma,h}), S=FL.initState(W,{source:0}); while(S.t<1.8-1e-9) FL.step(W,S); return [FL.ballLight(S,1), FL.tilt(W,S,0), W.links[2].marks[0].s, FL.books(W,S).total]; });
  console.log('  first face on link B-C at s = '+v[0][2].toFixed(4)+' (its echo reaches B after t = 1 + '+(2*v[0][2]).toFixed(3)+', so the readout at 1.8 '+(1+2*v[0][2]>1.8?'is':'IS NOT')+' free of it)');
  hs.forEach((h,k)=>{ console.log('  h='+h.toFixed(6)+'  light in B '+v[k][0].toFixed(9)+'  tilt A '+v[k][1].toFixed(9)+'  books '+v[k][3].toFixed(13)+(k>1?'  diff ratios: light '+((v[k-2][0]-v[k-1][0])/(v[k-1][0]-v[k][0])).toFixed(3)+', tilt '+((v[k-2][1]-v[k-1][1])/(v[k-1][1]-v[k][1])).toFixed(3):'')); }); }
console.log('\nD. the shipped geometry (z = 3, 5, 7; link lengths are rounded to whole steps): light in B at t = 6');
{ const hs=[0.02,0.01,0.005,0.0025,0.00125], v=hs.map(h=>{ const W=FL.makeWorld({N:3,h}), S=FL.initState(W,{source:0}); FL.advance(W,S,6); return FL.ballLight(S,1); });
  hs.forEach((h,k)=>console.log('  h='+h+'  light in B '+v[k].toFixed(7)+(k>0?'  change '+(v[k]-v[k-1]).toExponential(2):''))); }
