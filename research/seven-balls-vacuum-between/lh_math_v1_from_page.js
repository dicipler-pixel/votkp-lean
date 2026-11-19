/* SCRIPT: LH-MATH-V1 (his, unchanged) *//* SCRIPT: LH-MATH-V1
   Light at the Hypersurface — pure mathematics. Jeromie Beasley, 15 Nov 2026. AI-assisted.
   No DOM, no three.js. One feed operator: the peel step B(u, r), r = ln z, Γ = tanh(r/2).
   Hyperboloid vectors (t, x, y, z), signature (+,−,−,−). Tree coordinates i, j, k. */
(function(root){
"use strict";
const PI = Math.PI, SQ2 = Math.SQRT2, ZW = 3 + 2*SQ2;
/* ---------- complex numbers as [re, im] ---------- */
const C = {
  add:(a,b)=>[a[0]+b[0],a[1]+b[1]], sub:(a,b)=>[a[0]-b[0],a[1]-b[1]],
  mul:(a,b)=>[a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]],
  div:(a,b)=>{ const d = b[0]*b[0]+b[1]*b[1]; return [(a[0]*b[0]+a[1]*b[1])/d, (a[1]*b[0]-a[0]*b[1])/d]; },
  abs2:a=>a[0]*a[0]+a[1]*a[1], abs:a=>Math.hypot(a[0],a[1]), arg:a=>Math.atan2(a[1],a[0]),
  exp:a=>{ const e = Math.exp(a[0]); return [e*Math.cos(a[1]), e*Math.sin(a[1])]; },
  conj:a=>[a[0],-a[1]], re:x=>[x,0], scale:(a,s)=>[a[0]*s,a[1]*s], sqrt:a=>{ const m = Math.hypot(a[0],a[1]); const re = Math.sqrt((m+a[0])/2), im = Math.sign(a[1]||1)*Math.sqrt(Math.max(0,(m-a[0])/2)); return [re, im]; }
};
/* ---------- M1: Smith coordinate, step, Smith addition ---------- */
const smith = z => (z-1)/(z+1);
const oplus = (u,v) => C.div(C.add(u,v), C.add([1,0], C.mul(u,v)));
function step(Y1, Y2){ Y1 = Array.isArray(Y1) ? Y1 : [Y1,0]; Y2 = Array.isArray(Y2) ? Y2 : [Y2,0];
  const r = C.div(C.sub(Y1,Y2), C.add(Y1,Y2)), t = C.div(C.scale(Y1,2), C.add(Y1,Y2));
  const R = C.abs2(r), T = (Y2[1] === 0 && Y1[1] === 0) ? (Y2[0]/Y1[0])*C.abs2(t) : 0; return { r, t, R, T }; }
/* ---------- hyperboloid geometry ---------- */
const AX = [[1,0,0],[0,1,0],[0,0,1]];
const genU = k => AX[k>>1].map(v => (k&1) ? -v : v);           /* generator k: axis k>>1, sign k&1 */
const O4 = [1,0,0,0];
const mink = (p,q) => p[0]*q[0]-p[1]*q[1]-p[2]*q[2]-p[3]*q[3];
function boost(u, r){ const c = Math.cosh(r), s = Math.sinh(r), B = [[c, s*u[0], s*u[1], s*u[2]],[s*u[0],0,0,0],[s*u[1],0,0,0],[s*u[2],0,0,0]];
  for(let i=0;i<3;i++) for(let j=0;j<3;j++) B[i+1][j+1] = (i===j ? 1 : 0) + (c-1)*u[i]*u[j]; return B; }
const mm = (A,B) => A.map(r => [0,1,2,3].map(j => r[0]*B[0][j]+r[1]*B[1][j]+r[2]*B[2][j]+r[3]*B[3][j]));
const mv = (A,v) => A.map(r => r[0]*v[0]+r[1]*v[1]+r[2]*v[2]+r[3]*v[3]);
const I4 = () => [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]];
const lin = (a,x,b,y) => [a*x[0]+b*y[0], a*x[1]+b*y[1], a*x[2]+b*y[2], a*x[3]+b*y[3]];
/* face of generator k at the centre: unit spacelike normal, inside is <Y,N> > 0 */
function facePlane(G, u, h){ return mv(G, [Math.sinh(h), Math.cosh(h)*u[0], Math.cosh(h)*u[1], Math.cosh(h)*u[2]]); }
function hitPlane(X, v, N){ const A = mink(X,N), B = mink(v,N); if(!(A > 1e-12) || !(B < 0)) return null; const q = -A/B; if(q >= 1) return null; return Math.atanh(q); }
const geoPoint = (X,v,s) => lin(Math.cosh(s), X, Math.sinh(s), v);
const geoTangent = (X,v,s) => lin(Math.sinh(s), X, Math.cosh(s), v);
function incidence(t, N){ const c = Math.min(1, Math.abs(mink(t,N))); return { cos:c, sin:Math.sqrt(Math.max(0,1-c*c)) }; }
const reflectDir = (t,N) => lin(1, t, 2*mink(t,N), N);
function refractDir(t, N, sin2sq){ const m = mink(t,N), c = -m;                 /* Riemannian <t,N> */
  const tp = lin(1, t, m, N), s1 = Math.sqrt(Math.max(0, -mink(tp,tp)));     /* tangential part, length sin θ1 */
  const s2 = Math.sqrt(Math.max(0,Math.min(1,sin2sq))), c2 = Math.sqrt(Math.max(0,1-s2*s2));
  return s1 < 1e-15 ? lin(Math.sign(c)*c2, N, 0, N) : lin(Math.sign(c)*c2, N, s2/s1, tp); }
/* ---------- M2/M3: the split at a face, oblique ---------- */
function splitAtFace(a1, a2, sin1sq, omega, b){ b = b == null ? 1 : b;
  const Cc = a1*sin1sq, y1 = omega*Math.sqrt(Math.max(0,a1-Cc));
  if(a2 > Cc){ const y2 = omega*Math.sqrt(a2-Cc), s = step(y1, y2);
    return { C:Cc, Y1:y1, Y2:y2, r:s.r[0], R:s.R, T:s.T, total:false, sin2sq:Cc/a2, phase:s.r[0] < 0 ? PI : 0, kperp:0, depth:0 }; }
  const ke = omega*Math.sqrt(Cc-a2), g = C.div([y1,-ke],[y1,ke]), kperp = omega*Math.sqrt(b*(Cc-a2)/a2);
  return { C:Cc, Y1:y1, Y2:[0,ke], r:g, R:C.abs2(g), T:0, total:true, sin2sq:Cc/a2, theta2:[PI/2, Math.acosh(Math.sqrt(sin1sq*a1/a2))],
    phase:C.arg(g), kappaE:ke, kperp, depth:kperp > 0 ? 1/kperp : Infinity }; }
const thetaCrit = (a1,a2) => a2 < a1 ? Math.asin(Math.sqrt(a2/a1)) : null;
/* ---------- M4: the stack on one arm's axis (recursion by ⊕ and transfer matrix) ---------- */
function stackAxis(Ys, phis){ const D = Ys.length - 1, G = [];
  for(let k=0;k<D;k++) G.push(C.div(C.sub(Ys[k],Ys[k+1]), C.add(Ys[k],Ys[k+1])));
  let rho = G[D-1]; for(let k=D-2;k>=0;k--) rho = oplus(G[k], C.mul(rho, C.exp([0, 2*phis[k+1]])));
  /* transfer matrix: start in the last layer with a+ = 1, a- = 0, at its left end */
  const amp = new Array(D+1); amp[D] = { ap:[1,0], am:[0,0] };
  for(let k=D-1;k>=0;k--){ const b = amp[k+1], E = C.add(b.ap,b.am), H = C.mul(Ys[k+1], C.sub(b.ap,b.am)), HY = C.div(H, Ys[k]);
    let cp = C.scale(C.add(E,HY),0.5), cm = C.scale(C.sub(E,HY),0.5);
    if(k > 0){ cp = C.mul(cp, C.exp([0,-phis[k]])); cm = C.mul(cm, C.exp([0,phis[k]])); }
    amp[k] = { ap:cp, am:cm }; }
  const n0 = amp[0].ap, amps = amp.map(q => ({ ap:C.div(q.ap,n0), am:C.div(q.am,n0) }));
  const rTM = amps[0].am, t = amps[D].ap;
  const flux = amps.map((q,k) => (Ys[k][0]/Ys[0][0])*(C.abs2(q.ap) - C.abs2(q.am)));
  return { G, r:rho, rTM, t, amps, flux, Ttot:1 - C.abs2(rho) }; }
function bounceSum(g, x, M){ let s = [0,0], p = C.re(1); const mg = [-g[0], -g[1]];
  for(let m=0;m<M;m++){ s = C.add(s, C.mul(p, x)); p = C.mul(p, C.mul(mg, x)); }
  return C.add(g, C.mul(C.sub([1,0], C.mul(g,g)), s)); }
function echoCircle(a){ const A = 1 - Math.pow(C.abs2(a),2), Cc = C.mul(C.conj(a), C.sub([1,0], C.mul(a,a))); return { A, C:Cc, xc:C.scale(C.conj(Cc), -1/A) }; }
/* the gap as an evanescent film: medium Y1, gap with admittance i·ke and decay kperp, width w, medium Y1 */
function tunnelGap(Y1, ke, kperp, w){ const g = C.div([Y1,-ke],[Y1,ke]), x = C.scale(C.scale(g,-1), Math.exp(-2*kperp*w));
  const r = oplus(g, x);
  /* t by transfer: the gap is one layer of complex phase i·kperp·w */
  const amp2 = { ap:[1,0], am:[0,0] }, Yg = [0,ke];
  const E = C.add(amp2.ap,amp2.am), H = C.mul([Y1,0], C.sub(amp2.ap,amp2.am)), HY = C.div(H, Yg);
  let cp = C.scale(C.add(E,HY),0.5), cm = C.scale(C.sub(E,HY),0.5);
  cp = C.scale(cp, Math.exp(kperp*w)); cm = C.scale(cm, Math.exp(-kperp*w));          /* e^{∓iφ}, φ = i·kperp·w */
  const E0 = C.add(cp,cm), H0 = C.mul(Yg, C.sub(cp,cm)), H0Y = C.scale(H0, 1/Y1);
  const ap0 = C.scale(C.add(E0,H0Y),0.5), am0 = C.scale(C.sub(E0,H0Y),0.5);
  const rT = C.div(am0, ap0), t = C.div([1,0], ap0);
  return { r, rT, t, T:C.abs2(t), R:C.abs2(r) }; }
/* ---------- M5: Maxwell stress on a tilted plane ---------- */
function stress(E,H){ const s = [[0,0,0],[0,0,0],[0,0,0]], u = (E[0]*E[0]+E[1]*E[1]+E[2]*E[2]+H[0]*H[0]+H[1]*H[1]+H[2]*H[2])/(8*PI);
  for(let i=0;i<3;i++) for(let j=0;j<3;j++) s[i][j] = (E[i]*E[j]+H[i]*H[j])/(4*PI) - (i===j ? u : 0); return { s, u }; }
const normalStress = (s, n) => { let v = 0; for(let i=0;i<3;i++) for(let j=0;j<3;j++) v += n[i]*s[i][j]*n[j]; return v; };
/* ---------- M6: SL(2,C), the Lorentz image, Thomas turn, the square ---------- */
const S2 = {
  mul:(A,B)=>[C.add(C.mul(A[0],B[0]),C.mul(A[1],B[2])), C.add(C.mul(A[0],B[1]),C.mul(A[1],B[3])), C.add(C.mul(A[2],B[0]),C.mul(A[3],B[2])), C.add(C.mul(A[2],B[1]),C.mul(A[3],B[3]))],
  boost:(u,r)=>{ const c = Math.cosh(r/2), s = Math.sinh(r/2); return [[c+s*u[2],0],[s*u[0],-s*u[1]],[s*u[0],s*u[1]],[c-s*u[2],0]]; },
  tr:A=>C.add(A[0],A[3]), I:()=>[[1,0],[0,0],[0,0],[1,0]]
};
const SIG = [[[1,0],[0,0],[0,0],[1,0]], [[0,0],[1,0],[1,0],[0,0]], [[0,0],[0,-1],[0,1],[0,0]], [[1,0],[0,0],[0,0],[-1,0]]];
const dag = A => [C.conj(A[0]), C.conj(A[2]), C.conj(A[1]), C.conj(A[3])];
function sl2to4(A){ const Ad = dag(A), L = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];
  for(let m=0;m<4;m++) for(let n=0;n<4;n++){ const P = S2.mul(SIG[m], S2.mul(A, S2.mul(SIG[n], Ad))); L[m][n] = 0.5*(P[0][0]+P[3][0]); } return L; }
function thomas(ra, rb, ua, ub){ const Lam = mm(boost(ua,ra), boost(ub,rb)), p = mv(Lam,O4), pv = [p[1],p[2],p[3]], n = Math.hypot(pv[0],pv[1],pv[2]);
  const L = boost(pv.map(v=>v/n), Math.acosh(p[0])), Li = boost(pv.map(v=>-v/n), Math.acosh(p[0])), R = mm(Li, Lam);
  const tr3 = R[1][1]+R[2][2]+R[3][3], theta = Math.acos(Math.max(-1,Math.min(1,(tr3-1)/2)));
  return { theta, L, Li, R, Lam }; }
function loopSL2(ra, rb, ua, ub){ const Ba = S2.boost(ua,ra), Bb = S2.boost(ub,rb), Bai = S2.boost(ua,-ra), Bbi = S2.boost(ub,-rb);
  return S2.mul(S2.mul(Ba,Bb), S2.mul(Bai,Bbi)); }
function loop4(ra, rb, ua, ub){ return mm(mm(boost(ua,ra), boost(ub,rb)), mm(boost(ua.map(v=>-v),ra), boost(ub.map(v=>-v),rb))); }
function loopKind(tr2, g){ return Math.abs(g - 1) < 1e-9 ? 'wall' : (g < 1 ? 'turn' : 'run'); }
/* ---------- M7: light on the rim ---------- */
function aberrate(cosPsi, r){ const t = Math.tanh(r); return (cosPsi + t)/(1 + cosPsi*t); }
const doppler = (cosPsi, r) => Math.cosh(r) + Math.sinh(r)*cosPsi;
function boostNull(n, u, r){ const c = n[0]*u[0]+n[1]*u[1]+n[2]*u[2], t = Math.cosh(r) + Math.sinh(r)*c, par = Math.sinh(r) + Math.cosh(r)*c;
  return { n:[ (n[0]-c*u[0] + par*u[0])/t, (n[1]-c*u[1] + par*u[1])/t, (n[2]-c*u[2] + par*u[2])/t ], f:t }; }
const inCap = (n, u) => n[0]*u[0]+n[1]*u[1]+n[2]*u[2] > Math.SQRT1_2;
const faceShadow = h => Math.tanh(h);
function sphereSample(N){ const out = []; for(let i=0;i<N;i++){ const y = 1 - 2*(i+0.5)/N, rr = Math.sqrt(1-y*y), ph = i*2.399963229728653; out.push([rr*Math.cos(ph), rr*Math.sin(ph), y]); } return out; }
function pingpongExceptions(z, dirs){ let ex = 0; const r = Math.log(z);
  for(let k=0;k<6;k++){ const u = genU(k), mu = u.map(v=>-v); for(const n of dirs){ if(inCap(n, mu)) continue; if(!inCap(boostNull(n,u,r).n, u)) ex++; } } return ex; }
/* ---------- hypothesis layer: B182 stocks, exact step with Simpson source ---------- */
function expM2(M, t){ /* exp(tM) for real 2x2 [[a,b],[c,d]] */ const a = M[0][0], b = M[0][1], c = M[1][0], d = M[1][1], m = (a+d)/2, q = (a-d)/2, D2 = q*q + b*c;
  let ch, sh; if(D2 > 0){ const s = Math.sqrt(D2); ch = Math.cosh(s*t); sh = Math.sinh(s*t)/s; } else if(D2 < 0){ const s = Math.sqrt(-D2); ch = Math.cos(s*t); sh = Math.sin(s*t)/s; } else { ch = 1; sh = t; }
  const e = Math.exp(m*t); return [[e*(ch + q*sh), e*b*sh],[e*c*sh, e*(ch - q*sh)]]; }
function stocksStep(x, y, P0, Pm, P1, kappa, a, b, dt){ const M = [[-(kappa+a), b],[a, -b]], E = expM2(M, dt), Eh = expM2(M, dt/2);
  const xn = E[0][0]*x + E[0][1]*y + (dt/6)*(E[0][0]*P0 + 4*Eh[0][0]*Pm + P1), yn = E[1][0]*x + E[1][1]*y + (dt/6)*(E[1][0]*P0 + 4*Eh[1][0]*Pm);
  return [xn, yn]; }
const occupation = z => 1/(z+1);
/* ---------- the feed ---------- */
const DEF = { zI:3, zJ:5, zK:7, drive:'breathe', A:0.35, fan:62, omega:3, depth:4, orient:1, tag:6, arm:0, pair:0, kappa:1, ha:1, hb:0.2, absorb:0, nray:9 };
const PER = [8,13,21], PHS = [0, 2*PI/3, 4*PI/3], RLO = Math.log(1.5), RHI = Math.log(13);
const PAIRS = [[0,1],[1,2],[0,2]];
const SAMPLE = sphereSample(600);
function rOf(P, a, tau){ const zb = [P.zI,P.zJ,P.zK][a], r0 = Math.log(zb);
  if(P.drive === 'hold') return r0;
  if(P.drive === 'breathe') return Math.max(Math.log(1.05), r0 + P.A*Math.sin(2*PI*tau/PER[a] + PHS[a]));
  let x = tau/(3*PER[a]) + PHS[a]/(2*PI); x -= Math.floor(x); const tri = 1 - Math.abs(2*x - 1); return RLO + (RHI-RLO)*tri; }
function reduce(word, k){ const w = word.slice(); if(w.length && (w[w.length-1]^1) === k) w.pop(); else w.push(k); return w; }
function nodeAdmittance(word, S){ let Y = 1; for(const k of word) Y *= Math.pow(S.z[k>>1], -S.orient); return Y; }
function cellMatrix(word, S){ let G = I4(); for(const k of word) G = mm(G, boost(genU(k), S.r[k>>1])); return G; }
function traceRay(X0, v0, word, flux, S, out, info){
  const stack = [{ X:X0, v:v0, word, G:cellMatrix(word,S), flux, depth:0, excl:-1, ray:info.ray, chain:[] }];
  while(stack.length){ const q = stack.pop(); let best = null;
    for(let k=0;k<6;k++){ if(k === q.excl) continue; const N = facePlane(q.G, genU(k), S.h[k>>1]), s = hitPlane(q.X, q.v, N); if(s != null && (!best || s < best.s)) best = { s, k, N }; }
    if(!best){ let s = 0; for(; s < 9; s += 0.05){ const p = geoPoint(q.X,q.v,s); if(Math.hypot(p[1],p[2],p[3])/(1+p[0]) > 0.985) break; }
      out.push({ X:q.X, v:q.v, s, flux:q.flux, word:q.word, Y:nodeAdmittance(q.word,S), ray:q.ray, end:'rim', depth:q.depth }); continue; }
    const Yh = geoPoint(q.X,q.v,best.s), th = geoTangent(q.X,q.v,best.s), inc = incidence(th, best.N);
    const w2 = reduce(q.word, best.k), Y1 = nodeAdmittance(q.word,S), Y2 = nodeAdmittance(w2,S), a1 = Y1*Y1, a2 = Y2*Y2;
    const sp = splitAtFace(a1, a2, inc.sin*inc.sin, S.omega, 1);
    const seg = { X:q.X, v:q.v, s:best.s, flux:q.flux, word:q.word, Y:Y1, ray:q.ray, end:'face', depth:q.depth, k:best.k, N:best.N, hit:Yh, tin:th, a1, a2, sp, w2 };
    const tr = reflectDir(th, best.N); seg.tr = tr;
    if(!sp.total){ seg.tt = refractDir(th, best.N, sp.sin2sq); }
    seg.signedG = (Y1 - Y2)/(Y1 + Y2); seg.chain = q.chain.concat(sp.total ? [] : [seg.signedG]);
    out.push(seg);
    if(q.depth + 1 >= 6) continue;
    const fr = q.flux*sp.R, ft = q.flux*sp.T;
    if(fr > info.cut) stack.push({ X:Yh, v:tr, word:q.word, G:q.G, flux:fr, depth:q.depth+1, excl:best.k, ray:q.ray, chain:q.chain });
    if(!sp.total && ft > info.cut) stack.push({ X:Yh, v:seg.tt, word:w2, G:mm(q.G, boost(genU(best.k), S.r[best.k>>1])), flux:ft, depth:q.depth+1, excl:best.k^1, ray:q.ray, chain:seg.chain });
  } }
function fanDirs(S){ const d0 = [1,1,1].map(v=>v/Math.sqrt(3)), e1 = [1,-1,0].map(v=>v/SQ2), e2 = [1,1,-2].map(v=>v/Math.sqrt(6));
  const e = [0,1,2].map(i => Math.cos(S.chi)*e1[i] + Math.sin(S.chi)*e2[i]), out = [], n = S.nray, half = S.fan*PI/180;
  for(let j=0;j<n;j++){ const b = n === 1 ? 0 : -half + 2*half*j/(n-1); out.push([0,1,2].map(i => Math.cos(b)*d0[i] + Math.sin(b)*e[i])); } return out; }
function traceAll(S, cut){ const segs = []; fanDirs(S).forEach((d,j) => traceRay(O4, [0,d[0],d[1],d[2]], [], 1, S, segs, { ray:j, cut:cut||1e-3 })); return segs; }
function axisStack(S, a){ const D = S.depth, Ys = [], phis = []; for(let k=0;k<=D;k++){ const Y = Math.pow(S.z[a], -S.orient*k); Ys.push([Y,0]); phis.push(S.omega*Y*S.r[a]); }
  const st = stackAxis(Ys, phis); st.Ys = Ys; st.phis = phis;
  /* push on face k: arriving flux from each side, 2R each, opposite senses (reading) */
  const Rk = st.G.map(g => C.abs2(g));
  st.push = st.G.map((g,k) => 2*Rk[k]*((Ys[k][0])*C.abs2(st.amps[k].ap) - (Ys[k+1][0])*C.abs2(C.mul(st.amps[k+1].am, k+1 < D ? C.exp([0,-phis[k+1]]) : [1,0])))/Ys[0][0]);
  st.arrive = st.G.map((g,k) => Ys[k][0]*C.abs2(st.amps[k].ap)/Ys[0][0]);
  return st; }
function feed(P, tau){ const S = { tau, P, orient:P.orient, omega:P.omega, depth:P.depth, fan:P.fan, nray:P.nray };
  S.r = [0,1,2].map(a => rOf(P,a,tau)); S.z = S.r.map(Math.exp); S.h = S.r.map(r => r/2);
  S.G = S.r.map(r => Math.tanh(r/2)); S.Rf = S.G.map(g => g*g); S.Tf = S.Rf.map(R => 1-R); S.Pf = S.Rf.map(R => 2*R); S.Cocc = S.z.map(occupation);
  S.chi = 2*PI*tau/34;
  S.pairs = PAIRS.map(([a,b]) => { const g = Math.sinh(S.h[a])*Math.sinh(S.h[b]), over = g < 1;
    const ua = AX[a], ub = AX[b], th = thomas(S.r[a], S.r[b], ua, ub), W2 = loopSL2(S.r[a], S.r[b], ua, ub), W4 = loop4(S.r[a], S.r[b], ua, ub);
    const tr2 = S2.tr(W2)[0], kind = loopKind(tr2, g);
    return { a, b, g, over, alpha: over ? Math.acos(g) : NaN, delta: over ? NaN : Math.acosh(g), thetaT:th.theta, thomas:th, W2, W4, tr2, kind,
      phi: g < 1 ? Math.acos(8*g**4 - 8*g*g + 1) : NaN, run: g > 1 ? 4*Math.acosh(g) : NaN }; });
  S.segs = traceAll(S); S.stacks = [0,1,2].map(a => axisStack(S, a));
  S.ping = S.z.map(z => pingpongExceptions(z, SAMPLE));
  S.shadow = S.h.map(faceShadow);
  return S; }
/* pushes alone, for Simpson integration of the record */
function pushAt(P, tau){ const S = { orient:P.orient, omega:P.omega, depth:P.depth }; S.r = [0,1,2].map(a => rOf(P,a,tau)); S.z = S.r.map(Math.exp);
  return [0,1,2].map(a => { const st = axisStack(S, a); return { push:st.push, arrive:st.arrive }; }); }
/* ---------- the square carried on light: integrated state ---------- */
const T_LOOP = 5, NPASS = 8;
function passMatrix(S, pi){ const p = S.pairs[pi]; return p.W4; }
function partialSquare(S, pi, f){ /* the four steps, f in [0,1) through them */ const p = S.pairs[pi], ra = S.r[p.a], rb = S.r[p.b], ua = AX[p.a], ub = AX[p.b];
  const q = Math.min(3.999999, f*4), i = Math.floor(q), s = q - i; const st = [[ua,ra],[ub,rb],[ua.map(v=>-v),ra],[ub.map(v=>-v),rb]];
  let M = I4(); for(let k=0;k<i;k++) M = mm(M, boost(st[k][0], st[k][1])); return mm(M, boost(st[i][0], s*st[i][1])); }
function initState(){ return { pass:0, Wacc:I4(), K:[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]], stocks:[0,1,2].map(() => [0,0,0,0,0,0].map(() => [0,0])), n:0 }; }
function advance(st, P, tau0, dtau){ const tau1 = tau0 + dtau, taum = tau0 + dtau/2;
  /* passes of the square: the accumulated product is updated exactly at pass boundaries */
  const n0 = Math.floor(tau0/T_LOOP + 1e-12), n1 = Math.floor(tau1/T_LOOP + 1e-12);
  for(let m = n0+1; m <= n1; m++){ const Sm = feedLite(P, m*T_LOOP); if(m % NPASS === 0) st.Wacc = I4(); else st.Wacc = mm(st.Wacc, Sm.pairs[P.pair].W4); }
  st.n = tau1/T_LOOP;
  const p0 = pushAt(P,tau0), pm = pushAt(P,taum), p1 = pushAt(P,tau1);
  for(let a=0;a<3;a++) for(let k=0;k<P.depth;k++){ st.K[a][k] += (dtau/6)*(p0[a].push[k] + 4*pm[a].push[k] + p1[a].push[k]);
    const bb = P.absorb ? 0 : P.hb; st.stocks[a][k] = stocksStep(st.stocks[a][k][0], st.stocks[a][k][1], p0[a].arrive[k], pm[a].arrive[k], p1[a].arrive[k], P.kappa, P.ha, bb, dtau); }
  return st; }
function feedLite(P, tau){ const S = { tau }; S.r = [0,1,2].map(a => rOf(P,a,tau)); S.h = S.r.map(r=>r/2);
  S.pairs = PAIRS.map(([a,b]) => ({ a, b, W4:loop4(S.r[a], S.r[b], AX[a], AX[b]) })); return S; }
/* ---------- audit: balance laws recomputed from the drawn objects ---------- */
function audit(S){ let flux = 0, snell = 0, refl = 0, node = 0;
  for(const g of S.segs){ if(g.end !== 'face') continue; const sp = g.sp;
    /* flux at the face from r and t separately */
    if(!sp.total){ const s = step(sp.Y1, sp.Y2), res = Math.abs(s.R + s.T - 1); flux = Math.max(flux, res);
      const c1 = Math.abs(mink(g.tin, g.N)), c2 = Math.abs(mink(g.tt, g.N)), s1 = 1 - c1*c1, s2 = 1 - c2*c2;
      snell = Math.max(snell, Math.abs(g.a1*s1 - g.a2*s2)/g.a1);
      node = Math.max(node, Math.abs(mink(g.tt,g.tt) + 1), Math.abs(mink(g.tt, g.hit))); }
    else flux = Math.max(flux, Math.abs(C.abs(sp.r) - 1));
    const cr = Math.abs(mink(g.tr, g.N)), ci = Math.abs(mink(g.tin, g.N)); refl = Math.max(refl, Math.abs(cr - ci), Math.abs(mink(g.tr,g.tr)+1)); }
  let stackFlux = 0, stackRec = 0; for(const st of S.stacks){ const f = st.flux; for(const v of f) stackFlux = Math.max(stackFlux, Math.abs(v - st.Ttot)); stackRec = Math.max(stackRec, C.abs(C.sub(st.r, st.rTM))); }
  let detW = 0, wallR = 0; for(const p of S.pairs){ const W = p.W2, d = C.sub(C.mul(W[0],W[3]), C.mul(W[1],W[2])); detW = Math.max(detW, C.abs(C.sub(d,[1,0])));
    const th = p.thomas, LRLR = mm(mm(th.L, th.R), mm(th.Li, th.R)); let e = 0, n = 0; for(let i=0;i<4;i++) for(let j=0;j<4;j++){ e = Math.max(e, Math.abs(LRLR[i][j] - p.W4[i][j])); n = Math.max(n, Math.abs(p.W4[i][j])); } wallR = Math.max(wallR, e/n); }
  return { flux, snell, refl, node, stackFlux, stackRec, detW, LRLR:wallR }; }

/* ---------- self-test: this page's arithmetic (same function in the browser and in node) ---------- */
function selftest(){ let seed = 12345; const rnd = () => (seed = (seed*1103515245 + 12345) % 2147483648) / 2147483648;
  const out = [], add = (id, value, tol) => out.push({ id, value, tol, pass: value <= tol });
  let e = 0; for(let i=0;i<2000;i++){ const Y1 = Math.exp(rnd()*9.2-4.6), Y2 = Math.exp(rnd()*9.2-4.6), s = step(Y1,Y2); e = Math.max(e, Math.abs(s.R + s.T - 1), Math.abs(s.r[0] - Math.tanh(0.5*Math.log(Y1/Y2)))); } add('K1/K2 step flux and Smith form', e, 1e-12);
  e = 0; for(let i=0;i<2000;i++){ const a1 = Math.exp(rnd()*4-2), a2 = Math.exp(rnd()*4-2), s1 = rnd(), sp = splitAtFace(a1,a2,s1*s1,1+rnd()*5,1); e = Math.max(e, sp.total ? Math.abs(Math.sqrt(sp.R)-1) : Math.abs(sp.R+sp.T-1)); } add('K4 oblique flux / total return', e, 1e-12);
  { const a1 = 4, a2 = 1; let lo = 0, hi = PI/2; for(let i=0;i<80;i++){ const m = (lo+hi)/2; if(splitAtFace(a1,a2,Math.sin(m)**2,1,1).total) hi = m; else lo = m; } add('K5 critical angle at κ = 4 against 30°', Math.abs(lo - PI/6), 1e-9); }
  e = 0; for(let i=0;i<300;i++){ const g = [rnd()*1.6-0.8, 0], x = C.mul([rnd()*0.9,0], C.exp([0, rnd()*6.283])); if(C.abs(C.mul(g,x)) > 0.9) continue; e = Math.max(e, C.abs(C.sub(bounceSum(g,x,400), oplus(g,x)))); } add('K6 ⊕ against the bounce sum', e, 1e-10);
  e = 0; for(let i=0;i<300;i++){ const D = 2 + Math.floor(rnd()*5), Ys = [], ph = []; for(let k=0;k<=D;k++){ Ys.push([Math.exp(rnd()*3-1.5),0]); ph.push(rnd()*6); } const st = stackAxis(Ys, ph);
    e = Math.max(e, C.abs(C.sub(st.r, st.rTM))); for(const f of st.flux) e = Math.max(e, Math.abs(f - st.Ttot)); } add('K6 recursion = transfer matrix; equal net flux', e, 1e-12);
  { let ex = 0; for(let i=0;i<4000;i++){ const a = [rnd()*1.8-0.9, rnd()*1.8-0.9], x = [rnd()*2-1, rnd()*2-1]; if(C.abs(a) > 0.95 || C.abs(x) > 1) continue; const ec = echoCircle(a), d1 = C.abs2(oplus(a,x)) - C.abs2(a), d2 = C.abs(C.sub(x,ec.xc)) - C.abs(ec.xc); if(Math.abs(d1) > 1e-9 && Math.abs(d2) > 1e-9 && Math.sign(d1) !== Math.sign(d2)) ex++; } add('K6 echo circle sign exceptions', ex, 0);
    add('K6 witness 49/121 and 1/9', Math.max(Math.abs(C.abs2(oplus([0.5,0],[0.2,0])) - 49/121), Math.abs(C.abs2(oplus([0.5,0],[-0.2,0])) - 1/9)), 1e-15); }
  e = 0; for(let i=0;i<200;i++){ const g = tunnelGap(0.2+rnd()*2, 0.1+rnd()*2, 0.1+rnd()*2, rnd()*3); e = Math.max(e, Math.abs(g.R + g.T - 1)); } add('K7 gap |r|² + |t|² = 1', e, 1e-12);
  { const r = Math.log(ZW), W = loopSL2(r, r, AX[0], AX[1]), tr = S2.tr(W), Wp = [C.add(W[0],[1,0]), W[1], W[2], C.add(W[3],[1,0])], sq = S2.mul(Wp,Wp);
    add('K8 wall: |R − ½|', Math.abs(Math.tanh(r/2)**2 - 0.5), 1e-14); add('K8 wall: SL(2) trace + 2', C.abs(C.add(tr,[2,0])), 1e-12);
    add('K8 wall: ‖(W + I)²‖ (with ‖W + I‖ > 1e-3)', Math.max(...sq.map(C.abs)) + (Math.max(...Wp.map(C.abs)) > 1e-3 ? 0 : 1), 1e-10); }
  e = 0; for(let i=0;i<300;i++){ const ra = 0.05+rnd()*3, rb = 0.05+rnd()*3, th = thomas(ra, rb, AX[0], AX[1]); e = Math.max(e, Math.abs(th.theta - 2*Math.atan(Math.tanh(ra/2)*Math.tanh(rb/2)))); } add('K9 Thomas angle 2 arctan(Γa Γb)', e, 1e-9);
  { const t5 = thomas(Math.log(5),Math.log(5),AX[0],AX[1]).theta, t7 = thomas(Math.log(7),Math.log(7),AX[0],AX[1]).theta;
    add('K9 exact 65/97, 72/97, 175/337, 288/337', Math.max(Math.abs(Math.cos(t5)-65/97), Math.abs(Math.sin(t5)-72/97), Math.abs(Math.cos(t7)-175/337), Math.abs(Math.sin(t7)-288/337)), 1e-13); }
  e = 0; let e2 = 0; for(let i=0;i<300;i++){ const ra = 0.05+rnd()*3, rb = 0.05+rnd()*3, th = thomas(ra, rb, AX[0], AX[1]), W = loop4(ra, rb, AX[0], AX[1]), X = mm(mm(th.L, th.R), mm(th.Li, th.R));
    let d = 0, n = 0; for(let a=0;a<4;a++) for(let b=0;b<4;b++){ d = Math.max(d, Math.abs(X[a][b]-W[a][b])); n = Math.max(n, Math.abs(W[a][b])); } e = Math.max(e, d/n);
    const g = Math.sinh(ra/2)*Math.sinh(rb/2), tr4 = W[0][0]+W[1][1]+W[2][2]+W[3][3], half = (tr4-2)/2;
    if(g < 1 - 1e-6) e2 = Math.max(e2, Math.abs(half - (8*g**4 - 8*g*g + 1))); else if(g > 1 + 1e-6) e2 = Math.max(e2, Math.abs(Math.acosh(half) - 4*Math.acosh(g))/(4*Math.acosh(g))); }
  add('K10 W = L R L⁻¹ R (relative)', e, 1e-8); add('K10 turn cos φ = 8g⁴ − 8g² + 1; run 4 arccosh g', e2, 1e-10);
  e = 0; for(let i=0;i<2000;i++){ const c = rnd()*2-1, r = rnd()*3, u = AX[i%3], perp = AX[(i+1)%3], s = Math.sqrt(1-c*c), n = [0,1,2].map(k => c*u[k] + s*perp[k]), b = boostNull(n, u, r);
    e = Math.max(e, Math.abs(b.n[0]*u[0]+b.n[1]*u[1]+b.n[2]*u[2] - aberrate(c, r)), Math.abs(b.f - doppler(c, r))); } add('K11 aberration is ⊕; Doppler factor', e, 1e-12);
  { const D = sphereSample(4000); add('K11 ping-pong exceptions just above the wall and at 7, 9, 13', pingpongExceptions(ZW*(1+1e-6), D) + pingpongExceptions(7, D) + pingpongExceptions(9, D) + pingpongExceptions(13, D), 0);
    add('K11 ping-pong must fail at z = 5 (0 means it did)', pingpongExceptions(5, D) > 0 ? 0 : 1, 0); }
  e = 0; for(let i=0;i<200;i++){ const h = rnd()*3, N = facePlane(I4(), AX[0], h), c = Math.tanh(h), s = Math.sqrt(1-c*c); e = Math.max(e, Math.abs(mink([1, c, s, 0], N))); } add('K12 face shadow cos ψ0 = Γ', e, 1e-12);
  e = 0; for(let i=0;i<200;i++){ const th = rnd()*PI/2, E = [1,0,0], H = [0,1,0], s = stress(E,H), n = [Math.sin(th)*0, Math.sin(th), Math.cos(th)]; e = Math.max(e, Math.abs(normalStress(s.s, n) + s.u*Math.cos(th)**2)); } add('K13 Maxwell normal stress −u cos²θ', e, 1e-12);
  { const mean = (k,a,b) => (1 + a/b)/k; add('K15 residence (1,1,0.2) → 6 and (1,1,0.02) → 51', Math.max(Math.abs(mean(1,1,0.2)-6), Math.abs(mean(1,1,0.02)-51)), 1e-9); }
  e = 0; for(let i=0;i<500;i++){ const n = 2 + Math.floor(rnd()*10), r = []; for(let j=0;j<n;j++) r.push(rnd()*2-1); const Rp = r.filter(v=>v>0).reduce((a,b)=>a+b,0), Rm = -r.filter(v=>v<0).reduce((a,b)=>a+b,0);
    e = Math.max(e, Math.abs(2*r.reduce((a,b)=>a+Math.abs(b),0) - 2*Math.abs(r.reduce((a,b)=>a+b,0)) - 4*Math.min(Rp,Rm))); } add('K16 route − endpoint = 4 min(R₊, R₋)', e, 1e-12);
  e = 0; for(let i=0;i<500;i++){ const z = Math.exp(rnd()*6-3), Cc = occupation(z), G = smith(z); e = Math.max(e, Math.abs(1 - 2*Cc - G), Math.abs(4*Cc*(1-Cc) - (1 - G*G))); } add('K17 1 − 2C = Γ and 4C(1 − C) = T', e, 1e-14);
  e = 0; for(let i=0;i<200;i++){ const ha = rnd()*2, hb = rnd()*2, Na = facePlane(I4(), AX[0], ha), Nb = facePlane(I4(), AX[1], hb); e = Math.max(e, Math.abs(mink(Na,Nb) - Math.sinh(ha)*Math.sinh(hb))); } add('K18 <Na, Nb> = sinh ha sinh hb', e, 1e-12);
  return out; }
const api = { selftest, PI, ZW, C, smith, oplus, step, AX, genU, O4, mink, boost, mm, mv, I4, lin, facePlane, hitPlane, geoPoint, geoTangent, incidence, reflectDir, refractDir,
  splitAtFace, thetaCrit, stackAxis, bounceSum, echoCircle, tunnelGap, stress, normalStress, S2, sl2to4, thomas, loopSL2, loop4, loopKind, aberrate, doppler, boostNull,
  inCap, faceShadow, sphereSample, pingpongExceptions, expM2, stocksStep, occupation, DEF, PER, PAIRS, rOf, reduce, nodeAdmittance, cellMatrix, traceRay, fanDirs, traceAll,
  axisStack, feed, pushAt, T_LOOP, NPASS, partialSquare, initState, advance, feedLite, audit };
if(typeof module !== 'undefined' && module.exports) module.exports = api; else root.LH = api;
})(typeof window !== 'undefined' ? window : globalThis);
