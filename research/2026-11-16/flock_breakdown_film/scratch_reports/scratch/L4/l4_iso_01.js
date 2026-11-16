// SCRIPT: L4-ISO-01
// One ball alone (ports closed: gamma = 0; face push off) holding the whole quantum, torque on against torque off.
// Derivation tested: with s = light spin (psi^dag sigma psi, length = light held) and d = ball field,
//   ds/dt = 2 d x s (step b),  dd/dt = torque * s x d (step c)  =>  d(s + 2 d)/dt = 0 when torque = 1: both turn about J = s + 2d at rate |J|.
// For a kick across the field (s perpendicular to d, |s| = 1): |J| = sqrt((omega rate)^2 + 1), against omega*rate with torque off.
// Why it decides the point: if true, the measured turning rate of the spin (angle swept by s about the fixed axis J per unit time) equals |J|.
// Kill line: measured rate differs from |J| by more than 1e-3 (first-order splitting in h = 0.005 allowed for).
const FL = require('/home/claude/balls/w/fl/fl_math_v1.js');
for(const torque of [0,1]){ const W=FL.makeWorld({N:4,gamma:0,push:'off',torque,h:0.005}); const out=[];
  for(let i=0;i<4;i++){ const S=FL.initState(W,{source:i}); const s0=FL.bloch(S.psi[i]), d0=S.d[i].slice(), J=[0,1,2].map(a=>torque*s0[a]+2*d0[a]), Jm=Math.hypot(...J), u=J.map(x=>x/Jm);
    const perpTo=(v)=>{ const p=v[0]*u[0]+v[1]*u[1]+v[2]*u[2]; return v.map((x,a)=>x-p*u[a]); };
    const e1=perpTo(s0), m1=Math.hypot(...e1), f1=e1.map(x=>x/m1), f2=[u[1]*f1[2]-u[2]*f1[1],u[2]*f1[0]-u[0]*f1[2],u[0]*f1[1]-u[1]*f1[0]];
    let lastA=0, tot=0, cp0=FL.clockPhase(S,i).phase, cpt=0, Jdrift=0;
    for(let k=0;k<20000;k++){ FL.step(W,S); const s=FL.bloch(S.psi[i]), t=perpTo(s), a=Math.atan2(t[0]*f2[0]+t[1]*f2[1]+t[2]*f2[2], t[0]*f1[0]+t[1]*f1[1]+t[2]*f1[2]); let da=a-lastA; while(da>Math.PI) da-=2*Math.PI; while(da<-Math.PI) da+=2*Math.PI; tot+=da; lastA=a;
      const cp=FL.clockPhase(S,i).phase; let dc=cp-cp0; while(dc>Math.PI) dc-=2*Math.PI; while(dc<-Math.PI) dc+=2*Math.PI; cpt+=dc; cp0=cp;
      const Jn=[0,1,2].map(a=>torque*s[a]+2*S.d[i][a]); Jdrift=Math.max(Jdrift,Math.hypot(Jn[0]-J[0],Jn[1]-J[1],Jn[2]-J[2])); }
    out.push('  ball '+FL.NAMES[i]+': omega*rate = '+(W.opts.omega*W.balls[i].rate).toFixed(6)+'  |J| = '+Jm.toFixed(6)+'  measured turning rate of the spin about J = '+(Math.abs(tot)/S.t).toFixed(6)+'  slope of FL.clockPhase = '+(cpt/S.t).toFixed(6)+'  largest drift of s + 2d = '+Jdrift.toExponential(2)+'  largest tilt of the field '+FL.tilt(W,S,i).toFixed(3)); }
  console.log('torque '+torque+' (t = 100)'); out.forEach(x=>console.log(x)); }
