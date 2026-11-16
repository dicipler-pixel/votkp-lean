// SCRIPT: L4-UNITARY-01
// One step of FL.step as a real-linear map on (ball amplitudes + every link sample), for a FIXED set of ball fields d.
// Why it decides the point: a map M is norm-preserving for every state iff M^T M = I. We build M column by column from FL.step itself
// (unit vector in, one step, read out), with ball fields set to arbitrary directions, and measure max |M^T M - I|.
// Kill line (written first): max |M^T M - I| > 1e-12 for any case.
const FL = require('/home/claude/balls/w/fl/fl_math_v1.js');
function pack(W,S){ const v=[]; S.psi.forEach(p=>v.push(...p)); W.links.forEach(l=>l.segs.forEach(sg=>{ for(const x of sg.f) v.push(x); for(const x of sg.b) v.push(x); })); return v; }
function unpack(W,S,v){ let o=0; S.psi.forEach(p=>{ for(let c=0;c<4;c++) p[c]=v[o++]; }); W.links.forEach(l=>l.segs.forEach(sg=>{ for(let k=0;k<sg.f.length;k++) sg.f[k]=v[o++]; for(let k=0;k<sg.b.length;k++) sg.b[k]=v[o++]; sg.head=0; })); }
let seed=7; const rnd=()=> (seed=(seed*16807)%2147483647)/2147483647-0.5;
for(const cfg of [{N:3,h:0.02,gamma:0.6},{N:3,h:0.02,gamma:2.0,z:[5,7,9]},{N:4,h:0.05,gamma:1.3,z:[7,9,11]},{N:7,h:0.2,gamma:0.6}]){
  const W=FL.makeWorld(cfg), S=FL.initState(W,{});
  // arbitrary ball fields (any direction, any size): unitarity must not depend on them
  const dArb=W.balls.map(()=>[rnd()*3,rnd()*3,rnd()*3]);
  const n=pack(W,S).length, M=[];
  for(let j=0;j<n;j++){ const e=new Array(n).fill(0); e[j]=1; unpack(W,S,e); S.d=dArb.map(v=>v.slice()); FL.step(W,S); M.push(Float64Array.from(pack(W,S))); }
  let worst=0; for(let a=0;a<n;a++) for(let b=a;b<n;b++){ let s=0; const A=M[a],B=M[b]; for(let k=0;k<n;k++) s+=A[k]*B[k]; worst=Math.max(worst,Math.abs(s-(a===b?1:0))); }
  // complex-linearity: M must commute with multiplication by i (J: (re,im)->(-im,re)) so that it is unitary, not merely orthogonal
  let wj=0; for(let j=0;j<n;j+=2){ for(let k=0;k<n;k+=2){ wj=Math.max(wj,Math.abs(M[j][k]-M[j+1][k+1]),Math.abs(M[j][k+1]+M[j+1][k])); } }
  console.log('N='+cfg.N+' h='+cfg.h+' gamma='+cfg.gamma+' real dimension '+n+' (scatterers per link: '+W.links.map(l=>l.marks.length).join(',')+')  max|M^T M - I| = '+worst.toExponential(2)+'  max departure from complex-linear = '+wj.toExponential(2)+(worst<1e-12&&wj<1e-12?'  HOLDS':'  KILLED'));
}
// the four pieces on their own, as 2x2 / 4x4 blocks
{ const g=0.6,h=0.005,th=Math.sqrt(g*h),c=Math.cos(th),s=Math.sin(th); console.log('port block [[c,s],[-s,c]]: c^2+s^2-1 = '+(c*c+s*s-1).toExponential(2)+', theta = sqrt(gamma h) = '+th.toFixed(6));
  const rho=Math.tanh(Math.log(3)/2),tau=Math.sqrt(1-rho*rho); console.log('face block [[tau,-rho U],[rho U^dag,tau]]: tau^2+rho^2-1 = '+(tau*tau+rho*rho-1).toExponential(2)+'; off-diagonal of S^dag S = tau rho U - rho U tau = 0 exactly'); }
