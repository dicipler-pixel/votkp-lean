/* SCRIPT: MM-MATH-V1
   The Moving Matrix of Balls — mathematics. Jeromie Beasley, 15 Nov 2026. AI-assisted.
   Built from his papers: VOTKP (peel step, Gamma = tanh(d/2)), IQGT (projector, tangent, metric g, curvature),
   Non-Normality Is Connection Energy (H = D + A, edge mismatch energy), The Weight Between (C, X, offset tau,
   tau_dot^2 <= 4 g S, g = ||P H (1-P)||^2), Dirac Time (the clock is read from memory: the offset).
   No DOM. Hyperboloid vectors (t,x,y,z), signature (+,-,-,-). */
(function(root){
"use strict";
const PI = Math.PI;
/* ---------- hyperboloid ---------- */
const mink = (p,q) => p[0]*q[0]-p[1]*q[1]-p[2]*q[2]-p[3]*q[3];
function boost(u, r){ const c = Math.cosh(r), s = Math.sinh(r), B = [[c, s*u[0], s*u[1], s*u[2]],[s*u[0],0,0,0],[s*u[1],0,0,0],[s*u[2],0,0,0]];
  for(let i=0;i<3;i++) for(let j=0;j<3;j++) B[i+1][j+1] = (i===j?1:0) + (c-1)*u[i]*u[j]; return B; }
const mm4 = (A,B) => A.map(r => [0,1,2,3].map(j => r[0]*B[0][j]+r[1]*B[1][j]+r[2]*B[2][j]+r[3]*B[3][j]));
const mv4 = (A,v) => A.map(r => r[0]*v[0]+r[1]*v[1]+r[2]*v[2]+r[3]*v[3]);
const O4 = [1,0,0,0];
const dist = (p,q) => Math.acosh(Math.max(1, mink(p,q)));
/* pure boost carrying O to p */
function boostTo(p){ const v = [p[1],p[2],p[3]], n = Math.hypot(...v); if(n < 1e-15) return [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]; return boost(v.map(x=>x/n), Math.acosh(p[0])); }
/* transvection along the geodesic p -> q (parallel transport of the ball) */
function transvect(p, q){ const c = mink(p,q), L = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]], eta = [1,-1,-1,-1];
  /* L x = x - (<x,p>+<x,q>)/(1+c) (p+q) + 2<x,p> q */
  for(let j=0;j<4;j++){ const x = [0,0,0,0]; x[j] = 1; const xp = mink(x,p), xq = mink(x,q);
    for(let i=0;i<4;i++) L[i][j] = x[i] - (xp+xq)/(1+c)*(p[i]+q[i]) + 2*xp*q[i]; } return L; }
function inv4(B){ /* inverse of a Lorentz matrix: eta B^T eta */ const e = [1,-1,-1,-1]; return B.map((r,i) => r.map((_,j) => e[i]*B[j][i]*e[j])); }
/* rotation (3x3) of the transport from ball j to ball i, read in each ball's own frame (boosted standard frame) */
/* stable form: work in SL(2,C) where the entries are square roots of the hyperboloid coordinates.
   The pure boost to p is A_p = (X_p + I)/sqrt(tr X_p + 2) with X_p = p0 I + p.sigma; A_p^{-1} uses X_p^{-1} = p0 I - p.sigma.
   Then R_ij = [ L_{q->O} Lambda(A_i^{-1} A_j) ] restricted to space, q = Lambda(A_i^{-1} A_j) O. */
const c2 = { mul:(a,b)=>[a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]], add:(a,b)=>[a[0]+b[0],a[1]+b[1]], conj:a=>[a[0],-a[1]] };
function sqrtBoost(p, inv){ const s = inv ? -1 : 1, X = [[p[0]+s*p[3],0],[s*p[1],-s*p[2]],[s*p[1],s*p[2]],[p[0]-s*p[3],0]], n = Math.sqrt(2*p[0]+2);
  return [[(X[0][0]+1)/n, X[0][1]/n],[X[1][0]/n, X[1][1]/n],[X[2][0]/n, X[2][1]/n],[(X[3][0]+1)/n, X[3][1]/n]]; }
function mul2(A,B){ return [c2.add(c2.mul(A[0],B[0]),c2.mul(A[1],B[2])), c2.add(c2.mul(A[0],B[1]),c2.mul(A[1],B[3])), c2.add(c2.mul(A[2],B[0]),c2.mul(A[3],B[2])), c2.add(c2.mul(A[2],B[1]),c2.mul(A[3],B[3]))]; }
const SIG = [[[1,0],[0,0],[0,0],[1,0]], [[0,0],[1,0],[1,0],[0,0]], [[0,0],[0,-1],[0,1],[0,0]], [[1,0],[0,0],[0,0],[-1,0]]];
const dag2 = A => [c2.conj(A[0]), c2.conj(A[2]), c2.conj(A[1]), c2.conj(A[3])];
function sl2to4(A){ const Ad = dag2(A), L = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];
  for(let m=0;m<4;m++) for(let n=0;n<4;n++){ const P = mul2(SIG[m], mul2(A, mul2(SIG[n], Ad))); L[m][n] = 0.5*(P[0][0]+P[3][0]); } return L; }
function relLorentz(pi, pj){ return sl2to4(mul2(sqrtBoost(pi, true), sqrtBoost(pj, false))); }
function linkRotation(pi, pj){ const Lam = relLorentz(pi, pj), q = Lam.map(r => r[0]), M = mm4(transvect(q, O4), Lam); return [1,2,3].map(a => [1,2,3].map(b => M[a][b])); }
function linkDistance(pi, pj){ return Math.acosh(Math.max(1, relLorentz(pi, pj)[0][0])); }
const m3 = (A,B) => A.map(r => [0,1,2].map(j => r[0]*B[0][j]+r[1]*B[1][j]+r[2]*B[2][j]));
const v3 = (A,v) => A.map(r => r[0]*v[0]+r[1]*v[1]+r[2]*v[2]);
const T3 = A => [0,1,2].map(i => [0,1,2].map(j => A[j][i]));
function rotAngle(R){ return Math.acos(Math.max(-1, Math.min(1, (R[0][0]+R[1][1]+R[2][2]-1)/2))); }
/* SU(2) lift of a rotation: U = w I - i (x sx + y sy + z sz), via the quaternion with w >= 0. Stored as 2x2 complex [re,im] */
function su2(R){ const tr = R[0][0]+R[1][1]+R[2][2]; let w, x, y, z;
  if(tr > -0.999){ w = Math.sqrt(Math.max(0,1+tr))/2; x = (R[2][1]-R[1][2])/(4*w); y = (R[0][2]-R[2][0])/(4*w); z = (R[1][0]-R[0][1])/(4*w); }
  else { const i = R[0][0] > R[1][1] ? (R[0][0] > R[2][2] ? 0 : 2) : (R[1][1] > R[2][2] ? 1 : 2), q = [0,0,0], s = Math.sqrt(Math.max(0,1 + 2*R[i][i] - tr))/2; q[i] = s;
    const j = (i+1)%3, k = (i+2)%3; q[j] = (R[j][i]+R[i][j])/(4*s); q[k] = (R[k][i]+R[i][k])/(4*s); w = (R[k][j]-R[j][k])/(4*s); [x,y,z] = q; if(w < 0){ w=-w; x=-x; y=-y; z=-z; } }
  /* exp(-i theta/2 n.sigma) = w - i(x sx + y sy + z sz) */
  return [[w,-z],[-y,-x],[y,-x],[w,z]]; }   /* entries: u00, u01, u10, u11 as [re,im] */
/* ---------- the series of super balls ---------- */
const AXES = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]];
const perp = (a,b) => Math.abs(AXES[a][0]*AXES[b][0]+AXES[a][1]*AXES[b][1]+AXES[a][2]*AXES[b][2]) < 0.5;
/* one super ball: centre + six spokes at step r (peel step of ratio z = e^r), octahedral links and triangles */
function pattern(){ const nodes = [-1,0,1,2,3,4,5], edges = [], tris = [];
  for(let a=0;a<6;a++) edges.push([0, a+1]);
  for(let a=0;a<6;a++) for(let b=a+1;b<6;b++) if(perp(a,b)){ edges.push([a+1,b+1]); tris.push([0,a+1,b+1]); }
  for(let a=0;a<6;a+=2) for(let b=2;b<6;b+=2) {} /* octahedral faces added below */
  for(const sx of [0,1]) for(const sy of [2,3]) for(const sz of [4,5]) tris.push([sx+1, sy+1, sz+1]);
  return { nodes, edges, tris }; }
function buildSeries(level, steps){ /* steps: [r1, R2, R3] hyperbolic step of each level */
  const P = pattern();
  let balls = [{ p:O4.slice(), path:[] }], edges = [], tris = [];
  for(let L=1; L<=level; L++){ const r = steps[L-1];
    /* each existing structure becomes the centre super ball; six copies placed by peel steps of length r along the axes */
    const copies = [{ M:[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], dir:-1 }].concat(AXES.map((u,k) => ({ M:boost(u, r), dir:k })));
    const nb = balls.length, nb2 = [], ne = [], nt = [];
    copies.forEach((cp, ci) => { balls.forEach(b => nb2.push({ p:mv4(cp.M, b.p), path:[ci].concat(b.path) }));
      edges.forEach(e => ne.push([e[0]+ci*nb, e[1]+ci*nb, e[2]])); tris.forEach(t => nt.push(t.map(v => v+ci*nb))); });
    /* links between copies, octahedral pattern of the copies: connect the closest pair of balls */
    const close = (ca, cb) => { let best = null; for(let i=0;i<nb;i++) for(let j=0;j<nb;j++){ const d = linkDistance(nb2[ca*nb+i].p, nb2[cb*nb+j].p); if(!best || d < best.d) best = { i:ca*nb+i, j:cb*nb+j, d }; } return best; };
    P.edges.forEach(([a,b]) => { const c = close(a,b); ne.push([c.i, c.j, L]); });
    balls = nb2; edges = ne.map(e => e.length === 3 ? e : [e[0], e[1], L]); tris = nt;
    if(L === 1){ edges = ne.map(e => [e[0], e[1], 1]); tris = P.tris.map(t => t.slice()); } }
  /* dedupe edges */
  const seen = new Set(), E2 = []; for(const e of edges){ const k = Math.min(e[0],e[1])+','+Math.max(e[0],e[1]); if(seen.has(k) || e[0]===e[1]) continue; seen.add(k); E2.push(e); }
  return { balls, edges:E2, tris }; }
/* ---------- the matrix ---------- */
/* H = blocks D_i = d_i . sigma on each ball (2 levels: ground at -|d|, excited at +|d|; |d| = omega/2, ground half a quantum down)
   plus links  c_ij U_ij  (U_ij in SU(2), c_ij = c0 * sqrt(1 - Gamma_ij^2) = c0 sech(d_ij/2), Gamma_ij = tanh(d_ij/2)) */
function makeWorld(level, opts){ opts = Object.assign({ steps:[0.9, 2.7, 6.0], c0:0.5, omega:2.0, kappa:0.25, seaBack:true }, opts||{});
  const S = buildSeries(level, opts.steps), N = S.balls.length;
  const links = S.edges.map(([i,j,L]) => { const d = linkDistance(S.balls[i].p, S.balls[j].p), R = linkRotation(S.balls[i].p, S.balls[j].p);
    return { i, j, L, d, Gam:Math.tanh(d/2), c:opts.c0/Math.cosh(d/2), R, U:su2(R) }; });
  const nbr = Array.from({length:N}, () => []); links.forEach((l,k) => { nbr[l.i].push(k); nbr[l.j].push(k); });
  /* initial ball orientations: radial (outward), centre ball up */
  const d = S.balls.map(b => { const v = [b.p[1],b.p[2],b.p[3]], n = Math.hypot(...v); const u = n < 1e-9 ? [0,0,1] : v.map(x=>x/n); return u.map(x => x*opts.omega/2); });
  return { N, balls:S.balls, links, tris:S.tris, nbr, d, opts }; }
/* complex vector helpers: arrays re, im of length 2N */
function applyH(W, d, xr, xi, yr, yi){ const N = W.N;
  for(let i=0;i<N;i++){ const a = 2*i, b = a+1, [dx,dy,dz] = d[i];
    /* (d.sigma) [x_a, x_b] : [[dz, dx - i dy],[dx + i dy, -dz]] */
    yr[a] = dz*xr[a] + dx*xr[b] + dy*xi[b]; yi[a] = dz*xi[a] + dx*xi[b] - dy*xr[b];
    yr[b] = dx*xr[a] - dy*xi[a] - dz*xr[b]; yi[b] = dx*xi[a] + dy*xr[a] - dz*xi[b]; }
  for(const l of W.links){ const a = 2*l.i, b = 2*l.j, U = l.U, c = l.c;
    /* y_i += c U x_j ; y_j += c U^dag x_i */
    for(let r=0;r<2;r++){ let sr = 0, si = 0; for(let s=0;s<2;s++){ const u = U[2*r+s], xr_ = xr[b+s], xi_ = xi[b+s]; sr += u[0]*xr_ - u[1]*xi_; si += u[0]*xi_ + u[1]*xr_; } yr[a+r] += c*sr; yi[a+r] += c*si; }
    for(let r=0;r<2;r++){ let sr = 0, si = 0; for(let s=0;s<2;s++){ const u = U[2*s+r], xr_ = xr[a+s], xi_ = xi[a+s]; sr += u[0]*xr_ + u[1]*xi_; si += u[0]*xi_ - u[1]*xr_; } yr[b+r] += c*sr; yi[b+r] += c*si; } } }
function denseH(W, d){ const n = 2*W.N, Hr = Array.from({length:n}, () => new Float64Array(n)), Hi = Array.from({length:n}, () => new Float64Array(n)), xr = new Float64Array(n), xi = new Float64Array(n), yr = new Float64Array(n), yi = new Float64Array(n);
  for(let j=0;j<n;j++){ xr.fill(0); xi.fill(0); xr[j] = 1; applyH(W, d, xr, xi, yr, yi); for(let i=0;i<n;i++){ Hr[i][j] = yr[i]; Hi[i][j] = yi[i]; } } return { Hr, Hi, n }; }
/* Hermitian eigen-decomposition by complex Jacobi rotations (cyclic sweeps), n up to ~200 */
function eigh(Hr0, Hi0){ const n = Hr0.length, Ar = Hr0.map(r => Float64Array.from(r)), Ai = Hi0.map(r => Float64Array.from(r)),
    Vr = Array.from({length:n}, (_,i) => { const r = new Float64Array(n); r[i] = 1; return r; }), Vi = Array.from({length:n}, () => new Float64Array(n));
  for(let sweep=0; sweep<80; sweep++){ let off = 0; for(let p=0;p<n;p++) for(let q=p+1;q<n;q++) off += Ar[p][q]**2 + Ai[p][q]**2; if(off < 1e-28) break;
    for(let p=0;p<n;p++) for(let q=p+1;q<n;q++){ const ar = Ar[p][q], ai = Ai[p][q], mod = Math.hypot(ar, ai); if(mod < 1e-300) continue;
      /* A_pq = mod e^{i phi}; rotate in the (p,q) plane with phase */
      const er = ar/mod, ei = ai/mod, app = Ar[p][p], aqq = Ar[q][q], th = (aqq - app)/(2*mod), t = Math.sign(th||1)/(Math.abs(th) + Math.sqrt(th*th+1)), c = 1/Math.sqrt(t*t+1), sn = t*c;
      /* columns: new_p = c*col_p - s*conj(e)*col_q ... implemented as A <- J^H A J with J = [[c, s e],[-s conj(e), c]] acting on (p,q) */
      for(let k=0;k<n;k++){ /* A * J : columns p, q */ const kpr = Ar[k][p], kpi = Ai[k][p], kqr = Ar[k][q], kqi = Ai[k][q];
        /* col_p' = c*col_p - s*conj(e)*col_q ; col_q' = s*e*col_p + c*col_q */
        Ar[k][p] = c*kpr - sn*(er*kqr + ei*kqi); Ai[k][p] = c*kpi - sn*(er*kqi - ei*kqr);
        Ar[k][q] = sn*(er*kpr - ei*kpi) + c*kqr; Ai[k][q] = sn*(er*kpi + ei*kpr) + c*kqi;
        const vpr = Vr[k][p], vpi = Vi[k][p], vqr = Vr[k][q], vqi = Vi[k][q];
        Vr[k][p] = c*vpr - sn*(er*vqr + ei*vqi); Vi[k][p] = c*vpi - sn*(er*vqi - ei*vqr);
        Vr[k][q] = sn*(er*vpr - ei*vpi) + c*vqr; Vi[k][q] = sn*(er*vpi + ei*vpr) + c*vqi; }
      for(let k=0;k<n;k++){ /* J^H * A : rows p, q ; row_p' = c*row_p - s*e*row_q ; row_q' = s*conj(e)*row_p + c*row_q */
        const pkr = Ar[p][k], pki = Ai[p][k], qkr = Ar[q][k], qki = Ai[q][k];
        Ar[p][k] = c*pkr - sn*(er*qkr - ei*qki); Ai[p][k] = c*pki - sn*(er*qki + ei*qkr);
        Ar[q][k] = sn*(er*pkr + ei*pki) + c*qkr; Ai[q][k] = sn*(er*pki - ei*pkr) + c*qki; }
      Ai[p][p] = 0; Ai[q][q] = 0; Ar[p][q] = Ai[p][q] = Ar[q][p] = Ai[q][p] = 0; } }
  const idx = Array.from({length:n}, (_,i) => i).sort((a,b) => Ar[a][a] - Ar[b][b]);
  return { vals:idx.map(k => Ar[k][k]), vecs:idx.map(k => [Float64Array.from(Vr.map(r => r[k])), Float64Array.from(Vi.map(r => r[k]))]) }; }
/* ---------- state: light psi, electron sea P (rank N projector, the ground of the whole matrix), ball orientations d ---------- */
/* the sea: the Riesz projector onto the levels below the gapped cut nearest half filling (a contour must sit in a gap) */
function chooseCut(vals, N){ let best = N, bg = -1; for(let k=Math.ceil(N/2); k<=Math.floor(3*N/2) && k<vals.length; k++){ const g = vals[k]-vals[k-1]; if(g > bg){ bg = g; best = k; } } return best; }
function groundProjector(W, d, kfix){ const H = denseH(W, d), E = eigh(H.Hr, H.Hi), n = H.n, N = kfix || chooseCut(E.vals, W.N), Pr = Array.from({length:n}, () => new Float64Array(n)), Pi = Array.from({length:n}, () => new Float64Array(n));
  for(let k=0;k<N;k++){ const [vr,vi] = E.vecs[k]; for(let i=0;i<n;i++) for(let j=0;j<n;j++){ Pr[i][j] += vr[i]*vr[j] + vi[i]*vi[j]; Pi[i][j] += vi[i]*vr[j] - vr[i]*vi[j]; } }
  return { Pr, Pi, gap:E.vals[N]-E.vals[N-1], vals:E.vals, k:N }; }
function initState(W, opts){ opts = opts || {}; const n = 2*W.N, psr = new Float64Array(n), psi = new Float64Array(n), src = opts.source || 0;
  /* light: one quantum placed in the excited level of the source ball */
  /* the photon carries its own spin direction: by default across the source ball's field (opts.spin overrides) */
  let sp = opts.spin; if(!sp){ const dd = W.d[src], m0 = Math.hypot(...dd), u = dd.map(x=>x/m0), a = Math.abs(u[0]) < 0.9 ? [1,0,0] : [0,1,0], c = [u[1]*a[2]-u[2]*a[1], u[2]*a[0]-u[0]*a[2], u[0]*a[1]-u[1]*a[0]]; sp = c; }
  const [dx,dy,dz] = sp, m = Math.hypot(dx,dy,dz), th = Math.acos(dz/m), ph = Math.atan2(dy,dx);
  psr[2*src] = Math.cos(th/2); psr[2*src+1] = Math.sin(th/2)*Math.cos(ph); psi[2*src+1] = Math.sin(th/2)*Math.sin(ph);
  const G = opts.noSea ? null : groundProjector(W, W.d); if(G) W.seaRest = Array.from({length:W.N}, (_,i) => spinSea(G.Pr, G.Pi, i));
  return { t:0, psr, psi, Pr:G ? G.Pr : null, Pi:G ? G.Pi : null, d:W.d.map(v => v.slice()), gap0:G ? G.gap : NaN, kSea:G ? G.k : 0, kick:0, input:0 }; }
/* the sea pushes each ball with its spin density measured from the rest sea: s_i(P) - s_i(P_rest) */
function seaPush(W, S, i){ const s_ = spinSea(S.Pr, S.Pi, i), s0 = W.seaRest ? W.seaRest[i] : [0,0,0]; return [s_[0]-s0[0], s_[1]-s0[1], s_[2]-s0[2]]; }
/* forces on the balls: dE/dd_i = s_i(light) + s_i(sea) + 2 kappa sum_j c-weighted (d_i - R_ij d_j) */
function spinLight(psr, psi, i){ const a = 2*i, b = a+1, ar = psr[a], ai = psi[a], br = psr[b], bi = psi[b];
  return [2*(ar*br + ai*bi), 2*(ar*bi - ai*br), ar*ar+ai*ai - br*br - bi*bi]; }
function spinSea(Pr, Pi, i){ const a = 2*i, b = a+1; /* Tr(P_ii sigma) with P_ii = [[Paa,Pab],[Pba,Pbb]] */
  return [2*Pr[b][a], 2*Pi[b][a], Pr[a][a] - Pr[b][b]]; }
function faceGrad(W, d, i){ const g = [0,0,0], k = W.opts.kappa;
  for(const li of W.nbr[i]){ const l = W.links[li]; const R = l.i === i ? l.R : T3(l.R), j = l.i === i ? l.j : l.i, Rd = v3(R, d[j]); for(let a=0;a<3;a++) g[a] += 2*k*(d[i][a] - Rd[a]); } return g; }
function faceEnergy(W, d){ let E = 0; const k = W.opts.kappa; const per = W.links.map(l => { const Rd = v3(l.R, d[l.j]); const e = k*((d[l.i][0]-Rd[0])**2 + (d[l.i][1]-Rd[1])**2 + (d[l.i][2]-Rd[2])**2); E += e; return e; }); return { E, per }; }
const cross = (a,b) => [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]];
/* time derivative of the whole state */
function deriv(W, S){ const n = 2*W.N, yr = new Float64Array(n), yi = new Float64Array(n);
  applyH(W, S.d, S.psr, S.psi, yr, yi);
  const dpsr = new Float64Array(n), dpsi = new Float64Array(n); for(let k=0;k<n;k++){ dpsr[k] = yi[k]; dpsi[k] = -yr[k]; }   /* i psi' = H psi */
  let dPr = null, dPi = null;
  if(S.Pr){ /* P' = -i [H, P] */ dPr = Array.from({length:n}, () => new Float64Array(n)); dPi = Array.from({length:n}, () => new Float64Array(n));
    const cr = new Float64Array(n), ci = new Float64Array(n), hr = new Float64Array(n), hi = new Float64Array(n);
    const HPr = Array.from({length:n}, () => new Float64Array(n)), HPi = Array.from({length:n}, () => new Float64Array(n));
    for(let j=0;j<n;j++){ for(let i=0;i<n;i++){ cr[i] = S.Pr[i][j]; ci[i] = S.Pi[i][j]; } applyH(W, S.d, cr, ci, hr, hi); for(let i=0;i<n;i++){ HPr[i][j] = hr[i]; HPi[i][j] = hi[i]; } }
    /* PH = (H P)^dag since both Hermitian */
    for(let i=0;i<n;i++) for(let j=0;j<n;j++){ const cRe = HPr[i][j] - HPr[j][i], cIm = HPi[i][j] + HPi[j][i]; dPr[i][j] = cIm; dPi[i][j] = -cRe; } }
  const dd = S.d.map((di, i) => { const F = spinLight(S.psr, S.psi, i), Fs = (S.Pr && W.opts.seaBack) ? seaPush(W, S, i) : [0,0,0], Ff = faceGrad(W, S.d, i); const G = [F[0]+Fs[0]+Ff[0], F[1]+Fs[1]+Ff[1], F[2]+Fs[2]+Ff[2]]; return cross(G, di); });
  return { dpsr, dpsi, dPr, dPi, dd }; }
function axpy(W, S, D, h){ const n = 2*W.N, T = { t:S.t+h, psr:new Float64Array(n), psi:new Float64Array(n), d:S.d.map((v,i) => [v[0]+h*D.dd[i][0], v[1]+h*D.dd[i][1], v[2]+h*D.dd[i][2]]), Pr:null, Pi:null };
  for(let k=0;k<n;k++){ T.psr[k] = S.psr[k] + h*D.dpsr[k]; T.psi[k] = S.psi[k] + h*D.dpsi[k]; }
  if(S.Pr){ T.Pr = S.Pr.map((r,i) => r.map((v,j) => v + h*D.dPr[i][j])); T.Pi = S.Pi.map((r,i) => r.map((v,j) => v + h*D.dPi[i][j])); } return T; }
function rk4(W, S, h){ const k1 = deriv(W,S), k2 = deriv(W, axpy(W,S,k1,h/2)), k3 = deriv(W, axpy(W,S,k2,h/2)), k4 = deriv(W, axpy(W,S,k3,h)), n = 2*W.N;
  const T = { t:S.t+h, psr:new Float64Array(n), psi:new Float64Array(n), Pr:null, Pi:null, d:null, kick:S.kick, input:S.input, gap0:S.gap0, kSea:S.kSea };
  for(let k=0;k<n;k++){ T.psr[k] = S.psr[k] + h/6*(k1.dpsr[k]+2*k2.dpsr[k]+2*k3.dpsr[k]+k4.dpsr[k]); T.psi[k] = S.psi[k] + h/6*(k1.dpsi[k]+2*k2.dpsi[k]+2*k3.dpsi[k]+k4.dpsi[k]); }
  T.d = S.d.map((v,i) => [0,1,2].map(a => v[a] + h/6*(k1.dd[i][a]+2*k2.dd[i][a]+2*k3.dd[i][a]+k4.dd[i][a])));
  if(S.Pr){ T.Pr = S.Pr.map((r,i) => r.map((v,j) => v + h/6*(k1.dPr[i][j]+2*k2.dPr[i][j]+2*k3.dPr[i][j]+k4.dPr[i][j]))); T.Pi = S.Pi.map((r,i) => r.map((v,j) => v + h/6*(k1.dPi[i][j]+2*k2.dPi[i][j]+2*k3.dPi[i][j]+k4.dPi[i][j]))); purify(T); }
  return T; }
/* McWeeny purification P <- 3P^2 - 2P^3: returns the nearest projector, removing integrator drift (the sea stays a projector) */
function cmul(Ar, Ai, Br, Bi){ const n = Ar.length, Cr = Array.from({length:n}, () => new Float64Array(n)), Ci = Array.from({length:n}, () => new Float64Array(n));
  for(let i=0;i<n;i++){ const cr = Cr[i], ci = Ci[i]; for(let k=0;k<n;k++){ const ar = Ar[i][k], ai = Ai[i][k], br = Br[k], bi = Bi[k]; for(let j=0;j<n;j++){ cr[j] += ar*br[j] - ai*bi[j]; ci[j] += ar*bi[j] + ai*br[j]; } } } return [Cr, Ci]; }
function purify(T){ const [P2r, P2i] = cmul(T.Pr, T.Pi, T.Pr, T.Pi), [P3r, P3i] = cmul(P2r, P2i, T.Pr, T.Pi), n = T.Pr.length;
  for(let i=0;i<n;i++) for(let j=0;j<n;j++){ T.Pr[i][j] = 3*P2r[i][j] - 2*P3r[i][j]; T.Pi[i][j] = 3*P2i[i][j] - 2*P3i[i][j]; } }
/* ---------- readouts ---------- */
function energies(W, S){ const n = 2*W.N, yr = new Float64Array(n), yi = new Float64Array(n); applyH(W, S.d, S.psr, S.psi, yr, yi); let EL = 0; for(let k=0;k<n;k++) EL += S.psr[k]*yr[k] + S.psi[k]*yi[k];
  let ES = 0; if(S.Pr){ const cr = new Float64Array(n), ci = new Float64Array(n), hr = new Float64Array(n), hi = new Float64Array(n); for(let j=0;j<n;j++){ for(let i=0;i<n;i++){ cr[i] = S.Pr[i][j]; ci[i] = S.Pi[i][j]; } applyH(W, S.d, cr, ci, hr, hi); ES += hr[j]; } }
  const F = faceEnergy(W, S.d); let Erest = 0; if(S.Pr && W.seaRest) for(let i=0;i<W.N;i++) Erest += W.seaRest[i][0]*S.d[i][0] + W.seaRest[i][1]*S.d[i][1] + W.seaRest[i][2]*S.d[i][2];
  return { EL, ES, EF:F.E, Erest, Eper:F.per, E:EL + F.E + ((S.Pr && W.opts.seaBack) ? ES - Erest : 0), Eall:EL + ES + F.E }; }
/* light bond current J_ij = 2 Im( psi_i^dag c U_ij psi_j ) : the flow of the light from j to i */
function lightCurrents(W, S){ return W.links.map(l => { const a = 2*l.i, b = 2*l.j, U = l.U; let im = 0;
  for(let r=0;r<2;r++) for(let s=0;s<2;s++){ const u = U[2*r+s], xr = S.psr[b+s], xi = S.psi[b+s], wr = u[0]*xr - u[1]*xi, wi = u[0]*xi + u[1]*xr; /* conj(psi_i) * w */ im += S.psr[a+r]*wi - S.psi[a+r]*wr; }
  return 2*l.c*im; }); }
const lightDensity = (S, i) => S.psr[2*i]**2 + S.psi[2*i]**2 + S.psr[2*i+1]**2 + S.psi[2*i+1]**2;
/* ball power: what the light and the sea give the ball (s . d'), and what the ball gives its faces; they cancel exactly */
function ballPowers(W, S){ const D = deriv(W, S); return S.d.map((di, i) => { const F = spinLight(S.psr, S.psi, i), Fs = (S.Pr && W.opts.seaBack) ? seaPush(W, S, i) : [0,0,0], Ff = faceGrad(W, S.d, i), v = D.dd[i];
  const dot = (a,b) => a[0]*b[0]+a[1]*b[1]+a[2]*b[2]; return { fromLight:dot(F,v), fromSea:dot(Fs,v), toFaces:-dot(Ff,v), speed:Math.hypot(...v) }; }); }
/* Weight Between readouts per ball: C_i = 2x2 block of P on ball i, nu (eigenvalues), Gamma = 1-2nu (bridge), offset tau, X_i = C_{i,rest} C_{rest,i} */
function ballCensus(W, S){ if(!S.Pr) return null; const n = 2*W.N;
  return Array.from({length:W.N}, (_,i) => { const a = 2*i, b = a+1, Caa = S.Pr[a][a], Cbb = S.Pr[b][b], Cr = S.Pr[a][b], Ci = S.Pi[a][b];
    const tr = Caa + Cbb, det = Caa*Cbb - (Cr*Cr + Ci*Ci), disc = Math.sqrt(Math.max(0, tr*tr/4 - det)), nu = [tr/2 - disc, tr/2 + disc];
    /* (C^2)_ii = C_ii^2 + X_i  ->  Tr X_i = Tr C_ii - Tr C_ii^2 for a projector */
    const trC2 = Caa*Caa + Cbb*Cbb + 2*(Cr*Cr + Ci*Ci), trX = tr - trC2;
    const tau = Math.log((1-nu[0])*(1-nu[1])/(nu[0]*nu[1])), S_ = 1/(nu[0]*(1-nu[0])) + 1/(nu[1]*(1-nu[1]));
    return { nu, Gamma:nu.map(v => 1-2*v), tau, trX, S:S_ }; }); }
/* sea speed g = 1/2 ||P'||^2 = ||P H (1-P)||_F^2 (rate is weight) */
function seaSpeed(W, S){ if(!S.Pr) return NaN; const D = deriv(W, S), n = 2*W.N; let g = 0; for(let i=0;i<n;i++) for(let j=0;j<n;j++) g += D.dPr[i][j]**2 + D.dPi[i][j]**2; return g/2; }
function triangleHolonomy(W, t){ /* product of link rotations around the triangle, and the hyperbolic area */
  const [a,b,c] = t, R = (i,j) => { const l = W.links.find(l => (l.i===i && l.j===j) || (l.i===j && l.j===i)); if(!l) return null; return l.i === i ? l.R : T3(l.R); };
  const Rab = R(a,b), Rbc = R(b,c), Rca = R(c,a); if(!Rab || !Rbc || !Rca) return null;
  const Hol = m3(Rab, m3(Rbc, Rca)), ang = rotAngle(Hol);
  const p = [W.balls[a].p, W.balls[b].p, W.balls[c].p], A = (x,y,z) => { const cxy = mink(x,y), cxz = mink(x,z), cyz = mink(y,z); /* angle at x from the hyperbolic law of cosines */
    const sa = linkDistance(y,z), sb = linkDistance(x,z), sc = linkDistance(x,y); return Math.acos(Math.max(-1,Math.min(1,(Math.cosh(sb)*Math.cosh(sc) - Math.cosh(sa))/(Math.sinh(sb)*Math.sinh(sc))))); };
  const area = PI - A(p[0],p[1],p[2]) - A(p[1],p[0],p[2]) - A(p[2],p[0],p[1]); return { ang, area }; }
/* connection energy identity (Non-Normality Is Connection Energy): H = D + A with unitary edge blocks A_ij = U_ij, A_ji = -U_ij^dag;
   (1/8)||[H,H*]||_F^2 = sum_edges ||D_i - U_ij D_j U_ij^dag||_F^2  (checked on the dense matrix) */
function nnceCheck(W, d){ const n = 2*W.N, Hr = Array.from({length:n}, () => new Float64Array(n)), Hi = Array.from({length:n}, () => new Float64Array(n));
  for(let i=0;i<W.N;i++){ const [dx,dy,dz] = d[i], a = 2*i; Hr[a][a] = dz; Hr[a][a+1] = dx; Hi[a][a+1] = -dy; Hr[a+1][a] = dx; Hi[a+1][a] = dy; Hr[a+1][a+1] = -dz; }
  for(const l of W.links){ const a = 2*l.i, b = 2*l.j; for(let r=0;r<2;r++) for(let s=0;s<2;s++){ const u = l.U[2*r+s]; Hr[a+r][b+s] += u[0]; Hi[a+r][b+s] += u[1]; Hr[b+s][a+r] -= u[0]; Hi[b+s][a+r] += u[1]; } }
  /* [H, H*] */ const mul = (Ar,Ai,Br,Bi) => { const Cr = Array.from({length:n}, () => new Float64Array(n)), Ci = Array.from({length:n}, () => new Float64Array(n)); for(let i=0;i<n;i++) for(let k=0;k<n;k++){ const ar = Ar[i][k], ai = Ai[i][k]; if(ar===0 && ai===0) continue; for(let j=0;j<n;j++){ Cr[i][j] += ar*Br[k][j] - ai*Bi[k][j]; Ci[i][j] += ar*Bi[k][j] + ai*Br[k][j]; } } return [Cr,Ci]; };
  const Sr = Hr.map((r,i) => r.map((_,j) => Hr[j][i])), Si = Hi.map((r,i) => r.map((_,j) => -Hi[j][i]));
  const [Ar,Ai] = mul(Hr,Hi,Sr,Si), [Br,Bi] = mul(Sr,Si,Hr,Hi); let lhs = 0; for(let i=0;i<n;i++) for(let j=0;j<n;j++) lhs += (Ar[i][j]-Br[i][j])**2 + (Ai[i][j]-Bi[i][j])**2; lhs /= 8;
  let rhs = 0; for(const l of W.links){ const Rd = v3(l.R, d[l.j]); rhs += 2*((d[l.i][0]-Rd[0])**2 + (d[l.i][1]-Rd[1])**2 + (d[l.i][2]-Rd[2])**2); }
  return { lhs, rhs }; }
function seaWorkRate(W, S){ if(!S.Pr) return 0; const D = deriv(W, S); let w = 0; for(let i=0;i<W.N;i++){ const s_ = spinSea(S.Pr, S.Pi, i); w += s_[0]*D.dd[i][0] + s_[1]*D.dd[i][1] + s_[2]*D.dd[i][2]; } return w; }
/* analytic offset rate of ball i: tau' = -Tr[(C(I-C))^{-1} C'], with C' the ball block of P' */
function tauDot(W, S, D, i){ const a = 2*i, b = a+1; const C = [[S.Pr[a][a],0],[S.Pr[a][b],S.Pi[a][b]],[S.Pr[b][a],S.Pi[b][a]],[S.Pr[b][b],0]], Cd = [[D.dPr[a][a],D.dPi[a][a]],[D.dPr[a][b],D.dPi[a][b]],[D.dPr[b][a],D.dPi[b][a]],[D.dPr[b][b],D.dPi[b][b]]];
  const c2m = (x,y)=>[x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]], mm2 = (A,B)=>[0,1,2,3].map(k => { const r = k>>1, c = k&1; const u = c2m(A[2*r],B[c]), v = c2m(A[2*r+1],B[2+c]); return [u[0]+v[0],u[1]+v[1]]; });
  const I = [[1,0],[0,0],[0,0],[1,0]], ImC = I.map((z,k)=>[z[0]-C[k][0], z[1]-C[k][1]]), K = mm2(C, ImC);
  /* inverse of 2x2 complex K */ const det = c2m(K[0],K[3]), det2 = c2m(K[1],K[2]), dt = [det[0]-det2[0], det[1]-det2[1]], dm = dt[0]*dt[0]+dt[1]*dt[1], idt = [dt[0]/dm, -dt[1]/dm];
  const Ki = [c2m(K[3],idt), c2m([-K[1][0],-K[1][1]],idt), c2m([-K[2][0],-K[2][1]],idt), c2m(K[0],idt)]; const X = mm2(Ki, Cd); return -(X[0][0] + X[3][0]); }
const api = { tauDot, seaPush, chooseCut, seaWorkRate, linkDistance, relLorentz, sl2to4, mink, boost, boostTo, transvect, linkRotation, su2, rotAngle, m3, v3, T3, AXES, buildSeries, makeWorld, applyH, denseH, eigh, groundProjector, initState,
  deriv, rk4, energies, lightCurrents, lightDensity, ballPowers, ballCensus, seaSpeed, triangleHolonomy, nnceCheck, faceEnergy, spinLight, spinSea, faceGrad, dist, O4, mv4 };
if(typeof module !== 'undefined' && module.exports) module.exports = api; else root.MM = api;
})(typeof window !== 'undefined' ? window : globalThis);
/* SCRIPT: MM-REST — the rest state of the matrix before any light: minimise faces + sea ground energy over the ball directions
   (|d_i| fixed), by projected gradient descent; the sea energy gradient is s_i(sea) by Hellmann-Feynman. */
(function(root){ const M = (typeof module !== 'undefined' && module.exports) ? module.exports : root.MM;
  M.restState = function(W, opts){ opts = Object.assign({ iters:400, eta:0.2, withSea:true, tol:1e-10 }, opts||{}); let d = W.d.map(v => v.slice()), last = Infinity, it = 0, res = 0;
    for(; it<opts.iters; it++){ const G = opts.withSea ? M.groundProjector(W, d) : null; res = 0;
      const nd = d.map((di,i) => { const Ff = M.faceGrad(W, d, i), Fs = G ? M.spinSea(G.Pr, G.Pi, i) : [0,0,0], F = [Ff[0]+Fs[0], Ff[1]+Fs[1], Ff[2]+Fs[2]], m = Math.hypot(...di), u = di.map(x=>x/m), fu = F[0]*u[0]+F[1]*u[1]+F[2]*u[2], Ft = F.map((x,a) => x - fu*u[a]);
        res = Math.max(res, Math.hypot(...Ft)); const v = di.map((x,a) => x - opts.eta*Ft[a]), mv = Math.hypot(...v); return v.map(x => x*m/mv); });
      d = nd; if(res < opts.tol) break; }
    return { d, iters:it, residual:res }; };
})(typeof window !== 'undefined' ? window : globalThis);
