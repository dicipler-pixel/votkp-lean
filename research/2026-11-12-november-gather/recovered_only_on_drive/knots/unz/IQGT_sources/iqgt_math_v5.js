// SCRIPT: IQGT-MIXER-V5-MATH
// Physics for the IQGT Mixer 3D v5 eyes that the tested core (GRASSMANN-MIXER-CORE-V2) does not already hold.
// Pure functions, no DOM; tested by iqgt_math_v5_test.js against the paper's numbers before any eye uses them.
const IQ = (() => {
  const C = (typeof Core !== 'undefined') ? Core : require('./core_v2.js');
  // ---- Bloch sphere (rank one in C^2): Pi = (1 - n.sigma)/2 is the lower band of n.sigma
  const sph = (th, ph) => [Math.sin(th)*Math.cos(ph), Math.sin(th)*Math.sin(ph), Math.cos(th)];
  // complex 2x2 as [a,b,c,d] each [re,im]
  const c = (re, im) => [re, im || 0], cm = (x, y) => [x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]], ca = (x, y) => [x[0]+y[0], x[1]+y[1]];
  const m2 = (A, B) => [ca(cm(A[0],B[0]),cm(A[1],B[2])), ca(cm(A[0],B[1]),cm(A[1],B[3])), ca(cm(A[2],B[0]),cm(A[3],B[2])), ca(cm(A[2],B[1]),cm(A[3],B[3]))];
  const tr2 = A => ca(A[0], A[3]);
  const piOf = n => [c((1-n[2])/2), c(-n[0]/2, n[1]/2), c(-n[0]/2, -n[1]/2), c((1+n[2])/2)];
  const sub2 = (A, B, s) => A.map((x, i) => [(x[0]-B[i][0])*s, (x[1]-B[i][1])*s]);
  // intrinsic Q(V,W) = Tr(Pi V^dag W) for Hermitian V, W (V^dag = V)
  const Q2 = (P, V, W) => tr2(m2(P, m2(V, W)));
  const hs2 = A => Math.sqrt(A.reduce((s, x) => s + x[0]*x[0] + x[1]*x[1], 0));
  // a random tangent vector at Pi: V = Pi A (1-Pi) + (1-Pi) A Pi with A Hermitian; returns V and its block X = Pi V (1-Pi)
  function tangent2(P, r){ const a = C.gauss(r), b = C.gauss(r), d = C.gauss(r), e = C.gauss(r);
    const A = [c(a), c(b, -d), c(b, d), c(e)], I = [c(1), c(0), c(0), c(1)], Pc = sub2(I, P, 1);
    const V = m2(m2(P, A), Pc).map((x, i) => ca(x, m2(m2(Pc, A), P)[i])); const X = m2(m2(P, V), Pc); return { V, X }; }
  // ---- chart warp on the sphere (eye 1): knobs (u,v) -> (theta, phi)
  const chart = (u, v, w) => [Math.PI*u + w*0.35*Math.sin(Math.PI*u)*Math.sin(v), v + w*0.4*Math.sin(Math.PI*u)**2*Math.cos(v)];
  function chartJ(u, v, w){ const h = 1e-6, a = chart(u+h, v, w), b = chart(u-h, v, w), e = chart(u, v+h, w), f = chart(u, v-h, w);
    return [[(a[0]-b[0])/(2*h), (e[0]-f[0])/(2*h)], [(a[1]-b[1])/(2*h), (e[1]-f[1])/(2*h)]]; }
  function chartInv(th, ph, w){ let u = th/Math.PI, v = ph; for(let i=0;i<40;i++){ const p = chart(u, v, w), J = chartJ(u, v, w), r0 = p[0]-th, r1 = p[1]-ph, det = J[0][0]*J[1][1]-J[0][1]*J[1][0];
      u -= ( J[1][1]*r0 - J[0][1]*r1)/det; v -= (-J[1][0]*r0 + J[0][0]*r1)/det; if(Math.abs(r0)+Math.abs(r1) < 1e-14) break; } return [u, v]; }
  // round-chart metric of the lower band in (theta, phi): diag(1/4, sin^2 theta / 4)
  const gRound = th => [[0.25, 0], [0, Math.sin(th)**2/4]];
  const quad = (G, a, b) => a[0]*(G[0][0]*b[0]+G[0][1]*b[1]) + a[1]*(G[1][0]*b[0]+G[1][1]*b[1]);
  const pull = (G, J) => { const out = [[0,0],[0,0]]; for(let i=0;i<2;i++) for(let j=0;j<2;j++) for(let a=0;a<2;a++) for(let b=0;b<2;b++) out[i][j] += J[a][i]*G[a][b]*J[b][j]; return out; };
  // ---- Chern number (eye 5): pulled-back Omega_uv = (1/2) n.(d_u n x d_v n), and a lattice count (Fukui-Hatsugai-Suzuki)
  // knobs (u,v) are first warped (endpoints and the v-loop kept), then sent to the sphere: kind 0 folds back (no wrap), kind k wraps k times
  const warpUV = (u, v, w) => [u + w*0.12*Math.sin(Math.PI*u)**2*Math.sin(v), v + w*0.5*Math.sin(Math.PI*u)*Math.sin(v)];
  function mapN(kind, w){ return (u, v) => { const q = warpUV(u, v, w); return kind === 0 ? sph(0.9*Math.PI*4*q[0]*(1-q[0]), q[1]) : sph(Math.PI*q[0], kind*q[1]); }; }
  function lowerVec(n){ const a1 = [n[0], -n[1]], b1 = [-(1+n[2]), 0], a2 = [-(1-n[2]), 0], b2 = [n[0], n[1]];
    const n1 = Math.hypot(a1[0], a1[1], b1[0]), n2 = Math.hypot(a2[0], b2[0], b2[1]);
    return n1 >= n2 ? [[a1[0]/n1, a1[1]/n1], [b1[0]/n1, 0]] : [[a2[0]/n2, 0], [b2[0]/n2, b2[1]/n2]]; }
  const inner = (x, y) => [x[0][0]*y[0][0]+x[0][1]*y[0][1] + x[1][0]*y[1][0]+x[1][1]*y[1][1], x[0][0]*y[0][1]-x[0][1]*y[0][0] + x[1][0]*y[1][1]-x[1][1]*y[1][0]];
  function chern(kind, w, N){ const f = mapN(kind, w), M = 2*N, V = [];
    for(let i=0;i<=N;i++){ V.push([]); for(let j=0;j<M;j++) V[i].push(lowerVec(f(i/N, 2*Math.PI*j/M))); }
    let flux = 0, riem = 0; const tiles = [];
    for(let i=0;i<N;i++) for(let j=0;j<M;j++){ const a = V[i][j], b = V[i+1][j], cc = V[i+1][(j+1)%M], d = V[i][(j+1)%M];
      const u1 = inner(a,b), u2 = inner(b,cc), u3 = inner(cc,d), u4 = inner(d,a);
      const z = cm(cm(u1,u2), cm(u3,u4)); const F = -Math.atan2(z[1], z[0]); flux += F; tiles.push(F);
      const uu = (i+0.5)/N, vv = 2*Math.PI*(j+0.5)/M, h = 1e-5, n0 = f(uu, vv), nu = f(uu+h, vv).map((x,k) => (x - f(uu-h, vv)[k])/(2*h)), nv = f(uu, vv+h).map((x,k) => (x - f(uu, vv-h)[k])/(2*h));
      const cr = [nu[1]*nv[2]-nu[2]*nv[1], nu[2]*nv[0]-nu[0]*nv[2], nu[0]*nv[1]-nu[1]*nv[0]];
      riem += 0.5*(n0[0]*cr[0]+n0[1]*cr[1]+n0[2]*cr[2]) * (1/N) * (2*Math.PI/M); }
    return { lattice: flux/(2*Math.PI), riemann: riem/(2*Math.PI), tiles, N, M }; }
  // ---- fold family (eye 6): theta = y + 1.1, phi = x^2/2, gap 2 everywhere
  const foldN = (x, y) => sph(y + 1.1, x*x/2);
  function pullG(fn, x, y){ const h = 1e-5, P = (a, b) => piOf(fn(a, b)), P0 = P(x, y);
    const dx = sub2(P(x+h, y), P(x-h, y), 1/(2*h)), dy = sub2(P(x, y+h), P(x, y-h), 1/(2*h));
    const g = [[Q2(P0, dx, dx)[0], Q2(P0, dx, dy)[0]], [Q2(P0, dy, dx)[0], Q2(P0, dy, dy)[0]]];
    return { g, det: g[0][0]*g[1][1] - g[0][1]*g[1][0], P0 }; }
  // ---- gap closing (eye 7): two approaches to a Dirac point; Pi(d) of d.sigma with d = (r cos a, r sin a, m)
  function approach(m, a, r){ const d = [r*Math.cos(a), r*Math.sin(a), m], L = Math.hypot(...d) || 1; return d.map(x => x/L); }
  const piDist = (n1, n2) => Math.hypot(n1[0]-n2[0], n1[1]-n2[1], n1[2]-n2[2]) / Math.SQRT2;   // ||Pi1 - Pi2||_HS
  // ---- weights family (eye 4): pair sums with different powers of the gap
  const weights = { amps:[1.0, 0.62, 0.8, 0.42, 0.55], gaps:[1.0, 1.7, 2.4, 3.2, 4.1] };
  const pairModel = { metric: D => 1/(D*D), curvature: D => 2/(D*D), dipole: D => 2/(D*D*D), friction0: D => 2*D/(D*D), frictionT: (D, T) => 2*D*Math.tanh(D/(2*T))/(D*D) };
  const slope = (f, D) => { const h = 1e-4; return (Math.log(f(D*(1+h))) - Math.log(f(D*(1-h)))) / (Math.log(1+h) - Math.log(1-h)); };
  // ---- polar and narrowing turning points (eyes 8, 9)
  const polarTurn = (y0, th) => Math.asin(Math.sin(y0)*Math.sin(th));
  const narrowTurn = (y0, th) => Math.sqrt((1 + 6.25*y0*y0)/Math.sin(th)**2 - 1)/2.5;
  // ---- the toll (eye 11): excess work kappa * integral of v^2 dt for a schedule s(t) along a path of intrinsic length L
  function toll(L, T, ease, N){ N = N || 2000; let W = 0; const s = t => { const x = t/T; return x + ease*Math.sin(2*Math.PI*x)/(2*Math.PI); };
    for(let i=0;i<N;i++){ const t = (i+0.5)*T/N, h = T/N/2, v = L*(s(t+h)-s(t-h))/(2*h); W += v*v*T/N; } return { W, bound: L*L/T, s }; }
  // ---- corridor (eye 12): 7 levels, a 3-level cluster with inner gap delta under an outer gap
  function corridorOp(delta, outer){ return [0, delta, 2*delta, 2*delta + outer, 2*delta + outer + 0.7, 2*delta + outer + 1.5, 2*delta + outer + 2.4]; }
  function corridorTrial(delta, outer, eps, r, Q){ const n = 7, w = corridorOp(delta, outer), D = Array.from({length:n}, (_, i) => Float64Array.from({length:n}, (_, j) => i === j ? w[i] : 0));
    const A = C.matmul(C.matmul(Q, D), C.T(Q)); const E = C.randSym(n, r, 1), nE = C.opnorm(E); const B = A.map((row, i) => row.map((v, j) => v + eps*E[i][j]/nE));
    const a = C.eigh(A), b = C.eigh(B); const tip = C.principal(C.cols(a.V, [1]), C.cols(b.V, [1]))[0], tail = C.principal(C.cols(a.V, [0,1,2]), C.cols(b.V, [0,1,2]))[0];
    return { tip, tail, tipBound: eps/delta, tailBound: eps/(outer - eps) }; }
  // ---- fog (eye 14): symmetric logarithmic derivative of a rank-2 state in three levels, regularised
  function sld(p1, leak, eta){ const lam = [p1, 1 - p1, 0], d = [[0.30, 0.22, 0.35], [0.22, -0.30, 0.28], [0.35, 0.28, leak]];
    let res = 0, bures = 0; const L = [[0,0,0],[0,0,0],[0,0,0]];
    for(let i=0;i<3;i++) for(let j=0;j<3;j++){ L[i][j] = 2*d[i][j]/(lam[i] + lam[j] + 2*eta); const r = 0.5*(lam[i] + lam[j])*L[i][j] - d[i][j]; res += r*r; }
    for(let i=0;i<3;i++) for(let j=0;j<3;j++) bures += 0.25*lam[i]*L[i][j]*L[j][i];
    return { res: Math.sqrt(res), bures, L }; }
  // ---- cards (eye 15): permutations as graph subspaces
  const perms = { swaps: { n:20, map: i => i < 10 ? (i % 2 ? i - 1 : i + 1) : i, cycles:[2,2,2,2,2] },
                  cycle: { n:20, map: i => i < 10 ? (i + 1) % 10 : i, cycles:[10] },
                  dbl:   { n:9,  map: i => (2*i) % 9, cycles:[6,2] } };
  function permRead(key){ const P = perms[key], s = C.permStats(P.cycles, P.n), dH = s.dH, upper = Math.PI*Math.PI/8*dH;
    return Object.assign(s, { upper, lower: dH/2, pos: s.perPoint/upper }); }
  return { C, warpUV, sph, piOf, sub2, Q2, hs2, tangent2, chart, chartJ, chartInv, gRound, quad, pull, mapN, chern, foldN, pullG, approach, piDist,
           weights, pairModel, slope, polarTurn, narrowTurn, toll, corridorOp, corridorTrial, sld, perms, permRead, m2, tr2 };
})();
if (typeof module !== 'undefined') module.exports = IQ;
