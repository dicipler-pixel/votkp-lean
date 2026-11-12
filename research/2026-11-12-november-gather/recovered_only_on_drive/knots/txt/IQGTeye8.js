{"imports":{"three":"https://cdn.jsdelivr.net/npm/three@0.158.0/build/three.module.js","three/addons/":"https://cdn.jsdelivr.net/npm/three@0.158.0/examples/jsm/"}}
/*=====*/

// SCRIPT: GRASSMANN-MIXER-CORE-V2
// Math core for the Grassmannian mixer. Pure functions, no DOM. Tested by core_test.js against the paper's numbers.
const Core = (() => {
  // seeded RNG (mulberry32) so every run of the page is reproducible
  function rng(seed) { let a = seed >>> 0; return () => { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
  function gauss(r) { let u = 0, v = 0; while (u === 0) u = r(); v = r(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }
  const zeros = (n, m) => Array.from({ length: n }, () => new Float64Array(m));
  const eye = n => { const A = zeros(n, n); for (let i = 0; i < n; i++) A[i][i] = 1; return A; };
  function matmul(A, B) { const n = A.length, m = B[0].length, p = B.length, C = zeros(n, m); for (let i = 0; i < n; i++) for (let k = 0; k < p; k++) { const a = A[i][k]; if (a) for (let j = 0; j < m; j++) C[i][j] += a * B[k][j]; } return C; }
  const T = A => { const n = A.length, m = A[0].length, B = zeros(m, n); for (let i = 0; i < n; i++) for (let j = 0; j < m; j++) B[j][i] = A[i][j]; return B; };
  // cyclic Jacobi for real symmetric matrices; returns ascending eigenvalues and column eigenvectors
  function eigh(A0) {
    const n = A0.length, A = A0.map(r => Float64Array.from(r)), V = eye(n);
    for (let sweep = 0; sweep < 100; sweep++) {
      let off = 0; for (let i = 0; i < n; i++) for (let j = i + 1; j < n; j++) off += A[i][j] * A[i][j];
      if (off < 1e-30) break;
      for (let p = 0; p < n; p++) for (let q = p + 1; q < n; q++) {
        if (Math.abs(A[p][q]) < 1e-300) continue;
        const th = (A[q][q] - A[p][p]) / (2 * A[p][q]);
        const t = Math.sign(th || 1) / (Math.abs(th) + Math.sqrt(th * th + 1));
        const c = 1 / Math.sqrt(t * t + 1), s = t * c;
        for (let k = 0; k < n; k++) { const akp = A[k][p], akq = A[k][q]; A[k][p] = c * akp - s * akq; A[k][q] = s * akp + c * akq; }
        for (let k = 0; k < n; k++) { const apk = A[p][k], aqk = A[q][k]; A[p][k] = c * apk - s * aqk; A[q][k] = s * apk + c * aqk; }
        for (let k = 0; k < n; k++) { const vkp = V[k][p], vkq = V[k][q]; V[k][p] = c * vkp - s * vkq; V[k][q] = s * vkp + c * vkq; }
      }
    }
    const idx = [...Array(n).keys()].sort((a, b) => A[a][a] - A[b][b]);
    return { w: idx.map(i => A[i][i]), V: V.map(r => Float64Array.from(idx.map(i => r[i]))) };
  }
  const cols = (V, ids) => V.map(r => Float64Array.from(ids.map(i => r[i])));
  // singular values of a small matrix via eigenvalues of M^T M
  function svals(M) { const e = eigh(matmul(T(M), M)).w; return e.map(x => Math.sqrt(Math.max(0, x))); }
  // principal angles between column spaces of orthonormal U (n x k) and W (n x k), radians, descending
  function principal(U, W) { const s = svals(matmul(T(U), W)); return s.map(x => Math.acos(Math.min(1, x))).sort((a, b) => b - a); }
  const deg = r => r * 180 / Math.PI;
  function randSym(n, r, scale = 1) { const A = zeros(n, n); for (let i = 0; i < n; i++) for (let j = i; j < n; j++) { const g = gauss(r) * scale; A[i][j] = g; A[j][i] = g; } return A; }
  function randOrth(n, r) { return eigh(randSym(n, r)).V; }
  function opnorm(A) { const e = eigh(matmul(T(A), A)).w; return Math.sqrt(Math.max(...e)); }
  // the feed: a spectrum with a 3-level cluster (inner gap) under an outer gap, in a random frame, plus a sweep direction
  function makeFeed(seed) { const r = rng(seed); return { Q: randOrth(6, r), H1: randSym(6, r, 0.35), r }; }
  function feedOp(F, inner, outer, s) {
    const w = [0, inner, 2 * inner, 2 * inner + outer, 2 * inner + outer + 0.6, 2 * inner + outer + 1.3];
    const D = zeros(6, 6); for (let i = 0; i < 6; i++) D[i][i] = w[i];
    const A = matmul(matmul(F.Q, D), T(F.Q));
    for (let i = 0; i < 6; i++) for (let j = 0; j < 6; j++) A[i][j] += s * F.H1[i][j];
    return A;
  }
  // clusters: consecutive levels whose relative gap is below thr fuse into one subspace
  function clusters(w, thr) { const span = (w[w.length - 1] - w[0]) || 1; const out = [[0]]; for (let i = 1; i < w.length; i++) { if ((w[i] - w[i - 1]) / span < thr) out[out.length - 1].push(i); else out.push([i]); } return out; }
  // tip and tail between two independent noisy halves of the same operator
  function tipTail(A, noise, r) {
    const n = A.length, Ea = randSym(n, r, noise), Eb = randSym(n, r, noise);
    const add = (X, Y) => X.map((row, i) => row.map((v, j) => v + Y[i][j]));
    const a = eigh(add(A, Ea)), b = eigh(add(A, Eb)), base = eigh(A);
    const rows = [];
    for (let k = 1; k < n; k++) {
      const vec = principal(cols(a.V, [k - 1]), cols(b.V, [k - 1]))[0];
      const sub = principal(cols(a.V, [...Array(k).keys()]), cols(b.V, [...Array(k).keys()]))[0];
      const gap = (base.w[k] - base.w[k - 1]) / ((base.w[n - 1] - base.w[0]) || 1);
      rows.push({ k, vec: deg(vec), sub: deg(sub), gap });
    }
    return rows;
  }
  // metric speed of the rank-k projector along s, and the ceiling sqrt(k)||H1||/gap of Theorem 5.2
  function speed(F, inner, outer, s, k) {
    const h = 1e-5, P = x => { const e = eigh(feedOp(F, inner, outer, x)); const U = cols(e.V, [...Array(k).keys()]); return { P: matmul(U, T(U)), w: e.w }; };
    const p1 = P(s + h), p0 = P(s - h), pc = P(s); let g = 0;
    for (let i = 0; i < 6; i++) for (let j = 0; j < 6; j++) { const d = (p1.P[i][j] - p0.P[i][j]) / (2 * h); g += 0.5 * d * d; }
    const ceil = Math.sqrt(k) * opnorm(F.H1) / (pc.w[k] - pc.w[k - 1]);
    return { v: Math.sqrt(g), ceil };
  }
  // geodesics of a diagonal 2D metric g = diag(a(x,y), b(x,y)), RK4; returns path and the Clairaut quantity a*sin^2(theta)
  function geodesic(a, b, x0, y0, thetaDeg, T1, steps, sgn = -1) {
    const d = 1e-6;
    const ax = (x, y) => (a(x + d, y) - a(x - d, y)) / (2 * d), ay = (x, y) => (a(x, y + d) - a(x, y - d)) / (2 * d);
    const bx = (x, y) => (b(x + d, y) - b(x - d, y)) / (2 * d), by = (x, y) => (b(x, y + d) - b(x, y - d)) / (2 * d);
    const f = s => { const [x, y, u, v] = s, A = a(x, y), B = b(x, y);
      const xa = -(ax(x, y) * u * u + 2 * ay(x, y) * u * v - bx(x, y) * v * v) / (2 * A);
      const ya = -(-ay(x, y) * u * u + 2 * bx(x, y) * u * v + by(x, y) * v * v) / (2 * B);
      return [u, v, xa, ya]; };
    const th = thetaDeg * Math.PI / 180;
    let s = [x0, y0, Math.sin(th) / Math.sqrt(a(x0, y0)), sgn * Math.cos(th) / Math.sqrt(b(x0, y0))];
    const dt = T1 / steps, path = [[s[0], s[1]]];
    for (let i = 0; i < steps; i++) {
      const k1 = f(s), k2 = f(s.map((v, j) => v + dt / 2 * k1[j])), k3 = f(s.map((v, j) => v + dt / 2 * k2[j])), k4 = f(s.map((v, j) => v + dt * k3[j]));
      s = s.map((v, j) => v + dt / 6 * (k1[j] + 2 * k2[j] + 2 * k3[j] + k4[j]));
      if (!s.every(Number.isFinite) || Math.abs(s[1]) > 50) break;
      path.push([s[0], s[1]]);
    }
    return path;
  }
  // three two-band families from the paper: metric components in (x, y)
  const families = {
    polar: { label: 'Subspace stops rotating (polar stratum)', a: (x, y) => 9 * Math.sin(y) ** 2 / 4, b: () => 0.25, y0: 0.6, view: [-0.1, 2.6, -0.15, 0.85], line: 0,
      gap: () => 2, note: 'g∥ = (9/4) sin²y falls to zero on y = 0: the whole line is one projector.' },
    narrow: { label: 'Gap narrows (guiding line)', a: (x, y) => 9 / (4 * (1 + 6.25 * y * y)), b: (x, y) => 6.25 / (4 * (1 + 6.25 * y * y) ** 2), y0: 0.8, view: [-0.1, 4.2, -1.6, 1.6], line: 0,
      gap: (x, y) => 2 * Math.sqrt(1 + 6.25 * y * y), note: 'Gap 2√(1+6.25y²) is narrowest on y = 0, where the index is largest.' },
    fold: { label: 'Fold (collapse across the line)', a: (x, y) => x * x * Math.sin(y + 1.1) ** 2 / 4 + 1e-9, b: () => 0.25, y0: 0.6, view: [-1.2, 1.2, -0.3, 0.9], line: 'x0',
      gap: () => 2, note: 'det g → 0 on x = 0 while the projector keeps moving along it.' }
  };
  // permutations: eigenphases of a permutation from its cycle type; principal angles between graph(I) and graph(pi)
  function cycleAngles(cycles, n) { // cycles: array of lengths; remaining points fixed
    const th = []; let used = 0;
    for (const l of cycles) { for (let j = 0; j < l; j++) { const phi = 2 * Math.PI * j / l; const p = phi > Math.PI ? 2 * Math.PI - phi : phi; th.push(p / 2); } used += l; }
    for (let i = used; i < n; i++) th.push(0);
    return th;
  }
  function permStats(cycles, n) {
    const th = cycleAngles(cycles, n), moved = cycles.reduce((a, l) => a + (l > 1 ? l : 0), 0);
    const s2 = th.reduce((a, t) => a + Math.sin(t) ** 2, 0), t2 = th.reduce((a, t) => a + t * t, 0);
    const gram = []; for (const l of cycles) for (let j = 0; j < l; j++) gram.push({ l, j, val: 2 * Math.sin(Math.PI * j / l) ** 2 });
    return { th, dH: moved / n, s2, L: Math.sqrt(t2), perPoint: t2 / n, gram };
  }
  // curvature bound at a projector: blocks X, Y (k x m complex); g = Re Tr(X Y*), Omega = -2 Im Tr(X Y*)
  function envelopePoint(r, k, m, alpha, mix) {
    const cplx = () => ({ re: Array.from({ length: k * m }, () => gauss(r)), im: Array.from({ length: k * m }, () => gauss(r)) });
    const X = cplx(), Z = cplx();
    const ca = Math.cos(alpha), sa = Math.sin(alpha);
    const Y = { re: X.re.map((v, i) => ca * v - sa * X.im[i] + mix * Z.re[i]), im: X.im.map((v, i) => ca * v + sa * X.re[i] + mix * Z.im[i]) };
    const tr = (A, B) => { let re = 0, im = 0; for (let i = 0; i < A.re.length; i++) { re += A.re[i] * B.re[i] + A.im[i] * B.im[i]; im += A.im[i] * B.re[i] - A.re[i] * B.im[i]; } return { re, im }; };
    const xy = tr(X, Y), xx = tr(X, X).re, yy = tr(Y, Y).re;
    const g12 = xy.re, Om = -2 * xy.im, bound = 2 * Math.sqrt(Math.max(0, xx * yy - g12 * g12));
    const cosG = g12 / Math.sqrt(xx * yy);
    return { Om, bound, ratio: Math.abs(Om) / bound, thetaG: Math.acos(Math.max(-1, Math.min(1, cosG))) };
  }
  return { rng, gauss, eigh, principal, cols, deg, randSym, randOrth, makeFeed, feedOp, clusters, tipTail, speed, geodesic, families, cycleAngles, permStats, envelopePoint, matmul, T, opnorm };
})();

// ---------- v2 additions: complex bands (Appendices B and C) and Fisher speed from fidelity (Lemma 5.1) ----------
Object.assign(Core, (() => {
  const C = Core;
  // gauge-fix a complex vector: component idx real and positive, unit norm
  function gauge(re, im, idx) { const a = re[idx], b = im[idx], m = Math.hypot(a, b) || 1, c = a / m, s = -b / m;
    const r2 = re.map((x, i) => x * c - im[i] * s), i2 = im.map((y, i) => re[i] * s + y * c); const n = Math.hypot(...r2, ...i2);
    return { re: r2.map(x => x / n), im: i2.map(x => x / n) }; }
  // lowest eigenvector of a complex Hermitian H = {re, im} through the real embedding [[A,-B],[B,A]]
  function lowestVec(H, idx) { const n = H.re.length, M = Array.from({ length: 2 * n }, () => new Float64Array(2 * n));
    for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) { M[i][j] = H.re[i][j]; M[i + n][j + n] = H.re[i][j]; M[i][j + n] = -H.im[i][j]; M[i + n][j] = H.im[i][j]; }
    const e = C.eigh(M), re = [], im = []; for (let i = 0; i < n; i++) { re.push(e.V[i][0]); im.push(e.V[i + n][0]); }
    if (idx === undefined) { let best = 0; re.forEach((x, i) => { if (Math.hypot(x, im[i]) > Math.hypot(re[best], im[best])) best = i; }); idx = best; }
    return Object.assign(gauge(re, im, idx), { idx, lam: e.w[0] }); }
  const cdot = (u, v) => { let re = 0, im = 0; for (let i = 0; i < u.re.length; i++) { re += u.re[i] * v.re[i] + u.im[i] * v.im[i]; im += u.re[i] * v.im[i] - u.im[i] * v.re[i]; } return { re, im }; };
  // tensor Q_ij = <d_i v_perp | d_j v_perp> of the lowest band of Hf(p), p in R^2
  function bandQ(Hf, p, h = 1e-5) { const v = lowestVec(Hf(p)), idx = v.idx, d = [];
    for (let i = 0; i < 2; i++) { const pp = p.slice(), pm = p.slice(); pp[i] += h; pm[i] -= h; const a = lowestVec(Hf(pp), idx), b = lowestVec(Hf(pm), idx);
      const dv = { re: a.re.map((x, j) => (x - b.re[j]) / (2 * h)), im: a.im.map((x, j) => (x - b.im[j]) / (2 * h)) }; const o = cdot(v, dv);
      d.push({ re: dv.re.map((x, j) => x - (v.re[j] * o.re - v.im[j] * o.im)), im: dv.im.map((x, j) => x - (v.re[j] * o.im + v.im[j] * o.re)) }); }
    return [[cdot(d[0], d[0]), cdot(d[0], d[1])], [cdot(d[1], d[0]), cdot(d[1], d[1])]]; }
  // one random pair of tangent directions V = a.d, W = b.d at the point; returns the same fields as envelopePoint
  function pairFromQ(Q, a, b) { const q = (x, y) => { let re = 0, im = 0; for (let i = 0; i < 2; i++) for (let j = 0; j < 2; j++) { re += x[i] * y[j] * Q[i][j].re; im += x[i] * y[j] * Q[i][j].im; } return { re, im }; };
    const xy = q(a, b), xx = q(a, a).re, yy = q(b, b).re, g12 = xy.re, Om = -2 * xy.im, bound = 2 * Math.sqrt(Math.max(0, xx * yy - g12 * g12));
    return { Om, bound, ratio: Math.abs(Om) / bound, thetaG: Math.acos(Math.max(-1, Math.min(1, g12 / Math.sqrt(xx * yy)))) }; }
  const r2 = Math.SQRT2;
  const SIG = { x: { re: [[0, 1], [1, 0]], im: [[0, 0], [0, 0]] }, y: { re: [[0, 0], [0, 0]], im: [[0, -1], [1, 0]] }, z: { re: [[1, 0], [0, -1]], im: [[0, 0], [0, 0]] } };
  const SPN = { x: { re: [[0, 1 / r2, 0], [1 / r2, 0, 1 / r2], [0, 1 / r2, 0]], im: [[0, 0, 0], [0, 0, 0], [0, 0, 0]] },
                y: { re: [[0, 0, 0], [0, 0, 0], [0, 0, 0]], im: [[0, -1 / r2, 0], [1 / r2, 0, -1 / r2], [0, 1 / r2, 0]] },
                z: { re: [[1, 0, 0], [0, 0, 0], [0, 0, -1]], im: [[0, 0, 0], [0, 0, 0], [0, 0, 0]] } };
  const comb = (cs, Ms) => { const n = Ms[0].re.length, out = { re: [], im: [] }; for (let i = 0; i < n; i++) { out.re.push(new Float64Array(n)); out.im.push(new Float64Array(n));
    for (let j = 0; j < n; j++) Ms.forEach((M, k) => { out.re[i][j] += cs[k] * M.re[i][j]; out.im[i][j] += cs[k] * M.im[i][j]; }); } return out; };
  const dirH = ops => p => comb([Math.sin(p[0]) * Math.cos(p[1]), Math.sin(p[0]) * Math.sin(p[1]), Math.cos(p[0])], [ops.x, ops.y, ops.z]);
  function randHerm(n, r) { const re = [], im = []; for (let i = 0; i < n; i++) { re.push(new Float64Array(n)); im.push(new Float64Array(n)); }
    for (let i = 0; i < n; i++) for (let j = i; j < n; j++) { const a = C.gauss(r), b = i === j ? 0 : C.gauss(r); re[i][j] = re[j][i] = a; im[i][j] = b; im[j][i] = -b; } return { re, im }; }
  const gr = C.rng(404), G0 = randHerm(3, gr), G1 = randHerm(3, gr), G2 = randHerm(3, gr);
  const bandFamilies = {
    two: { label: 'two levels (d·σ; the polariton case)', H: dirH(SIG), point: r => [0.3 + 2.5 * r(), 2 * Math.PI * r()] },
    spin1: { label: 'spin 1, lowest band (d·S)', H: dirH(SPN), point: r => [0.3 + 2.5 * r(), 2 * Math.PI * r()] },
    generic: { label: 'generic three levels (H₀ + aH₁ + bH₂)', H: p => comb([1, p[0], p[1]], [G0, G1, G2]), point: r => [C.gauss(r) * 0.5, C.gauss(r) * 0.5] } };
  function bandCloud(fam, n, seed) { const r = C.rng(seed), F = bandFamilies[fam], pts = [];
    for (let t = 0; t < n; t++) { const Q = bandQ(F.H, F.point(r)); pts.push(pairFromQ(Q, [C.gauss(r), C.gauss(r)], [C.gauss(r), C.gauss(r)])); } return pts; }
  // Fisher speed of rho = Pi_k / k from the Bures fidelity of neighbouring projectors: F_Q = 8 (1 - (1/k) Σ cos θ_j) / ds²
  function fisherSpeed(F, inner, outer, s, k, ds = 1e-4) { const ids = [...Array(k).keys()];
    const a = C.eigh(C.feedOp(F, inner, outer, s - ds / 2)), b = C.eigh(C.feedOp(F, inner, outer, s + ds / 2));
    const th = C.principal(C.cols(a.V, ids), C.cols(b.V, ids)); const fq = 8 * (1 - th.reduce((x, t) => x + Math.cos(t), 0) / k) / (ds * ds);
    return { fq, v: Math.sqrt(k * fq / 4) }; }
  return { lowestVec, bandQ, pairFromQ, bandFamilies, bandCloud, fisherSpeed };
})());
if (typeof module !== 'undefined') module.exports = Core;

window.Core = Core;
// SCRIPT: IQGT-MIXER-V5-MATH
// Physics for the IQGT Mixer 3D v5 eyes that the tested core (GRASSMANN-MIXER-CORE-V2) does not already hold.
// Pure functions, no DOM; tested by iqgt_math_v5_test.js against the paper's numbers before any eye uses them.
window.IQ = (() => {
  const C = window.Core;
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



/*=====*/

/* SCRIPT: mixer3d_parts_v2
   3D Mixer Parts v2 — Jeromie Beasley — 28 Oct 2026
   Shared 3D parts and the Atlas Memoriae instrument layout (v1 parts kept, new shell):
   stage with bloom, starfield, orbit / pinch / wheel, auto-turn; glow points, trails, lines, tubes,
   rim-lit glass spheres, arrows, rings, bars, terrain surfaces, labels;
   the shell: spectrum rail (eyes as levels, acts held apart by gaps), eye card (equation, controls,
   readouts), transport (previous / next, film, seconds, overlay for screen blending, clean view,
   frame PNG, record WebM), deep links (#eye), keyboard.
   This is NOT a mixer. Each paper's mixer writes its own eyes from its own physics on these parts.
   Loaded as an ES module with three r158 from the import map. */
import * as THREE from 'three';
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';
import { OutputPass } from 'three/addons/postprocessing/OutputPass.js';
const T = THREE;

/* ---------- palette (one meaning per colour, shared by every eye) ---------- */
const PAL = { metric:0x5ab0ff, twist:0xb18cff, gap:0xffb547, tail:0x4fe3c1, tip:0xff6f91, ink:0xe8eefb, dim:0x93a3c0, faint:0x3b4a66 };
const hex = c => '#' + c.toString(16).padStart(6, '0');
const rgb = c => [((c>>16)&255)/255, ((c>>8)&255)/255, (c&255)/255];

/* ---------- glow parts ---------- */
const sprite = (() => { const c = document.createElement('canvas'); c.width = c.height = 64; const x = c.getContext('2d');
  const g = x.createRadialGradient(32,32,0,32,32,32); g.addColorStop(0,'rgba(255,255,255,1)'); g.addColorStop(0.22,'rgba(255,255,255,.7)'); g.addColorStop(1,'rgba(255,255,255,0)');
  x.fillStyle = g; x.fillRect(0,0,64,64); const t = new T.CanvasTexture(c); return t; })();
const glowMat = size => new T.PointsMaterial({size, map:sprite, transparent:true, depthWrite:false, blending:T.AdditiveBlending, vertexColors:true, sizeAttenuation:true});
function points(n, size){ const geo = new T.BufferGeometry(); geo.setAttribute('position', new T.BufferAttribute(new Float32Array(n*3),3)); geo.setAttribute('color', new T.BufferAttribute(new Float32Array(n*3),3)); const p = new T.Points(geo, glowMat(size)); p.frustumCulled = false; return p; }
function setPt(p, i, P, c){ const a = p.geometry.attributes; a.position.setXYZ(i, P.x, P.y, P.z); if(c) a.color.setXYZ(i, c[0], c[1], c[2]); }
function flush(p){ const a = p.geometry.attributes; a.position.needsUpdate = true; a.color.needsUpdate = true; }
function line(pts, color, opacity){ const geo = new T.BufferGeometry().setFromPoints(pts.length ? pts : [new T.Vector3(), new T.Vector3()]); const l = new T.Line(geo, new T.LineBasicMaterial({color, transparent:true, opacity:opacity==null?1:opacity, depthWrite:false})); l.frustumCulled = false; return l; }
function setLine(l, pts){ l.geometry.dispose(); l.geometry = new T.BufferGeometry().setFromPoints(pts.length ? pts : [new T.Vector3(), new T.Vector3()]); }
function dashed(pts, color, opacity){ const l = new T.Line(new T.BufferGeometry().setFromPoints(pts), new T.LineDashedMaterial({color, dashSize:0.06, gapSize:0.05, transparent:true, opacity:opacity==null?0.7:opacity, depthWrite:false})); l.computeLineDistances(); l.frustumCulled = false; return l; }
function setDashed(l, pts){ l.geometry.dispose(); l.geometry = new T.BufferGeometry().setFromPoints(pts); l.computeLineDistances(); }
/* glowing tube along a polyline (for the curves that carry the argument) */
function tube(pts, r, color, opacity){ const m = new T.Mesh(tubeGeo(pts, r), new T.MeshBasicMaterial({color, transparent:true, opacity:opacity==null?1:opacity, depthWrite:false, blending:T.AdditiveBlending})); m.userData.r = r; m.frustumCulled = false; return m; }
function tubeGeo(pts, r){ if(pts.length < 2) pts = [new T.Vector3(), new T.Vector3(0,1e-4,0)]; const c = new T.CatmullRomCurve3(pts, false, 'centripetal'); return new T.TubeGeometry(c, Math.min(600, pts.length*2), r, 8, false); }
function setTube(m, pts){ m.geometry.dispose(); m.geometry = tubeGeo(pts, m.userData.r); }
function orb(r, color, glow){ const g = new T.Group(); const core = new T.Mesh(new T.SphereGeometry(r, 24, 16), new T.MeshBasicMaterial({color}));
  const halo = new T.Sprite(new T.SpriteMaterial({map:sprite, color, transparent:true, depthWrite:false, blending:T.AdditiveBlending, opacity:0.9}));
  halo.scale.setScalar(r*(glow||7)); g.add(core); g.add(halo); g.userData = {core, halo}; return g; }
function paintOrb(o, color){ o.userData.core.material.color.set(color); o.userData.halo.material.color.set(color); }
/* rim-lit glass sphere: bright at the silhouette, clear in the middle */
function glass(r, color, power, opacity){ const mat = new T.ShaderMaterial({ transparent:true, depthWrite:false, blending:T.AdditiveBlending, side:T.FrontSide,
  uniforms:{ c:{value:new T.Color(color)}, p:{value:power||2.6}, o:{value:opacity==null?0.55:opacity} },
  vertexShader:'varying vec3 vN; varying vec3 vV; void main(){ vec4 mv = modelViewMatrix*vec4(position,1.0); vN = normalize(normalMatrix*normal); vV = normalize(-mv.xyz); gl_Position = projectionMatrix*mv; }',
  fragmentShader:'uniform vec3 c; uniform float p; uniform float o; varying vec3 vN; varying vec3 vV; void main(){ float f = pow(1.0-abs(dot(vN,vV)), p); gl_FragColor = vec4(c*f*o, f*o); }' });
  return new T.Mesh(new T.SphereGeometry(r, 64, 48), mat); }
function ring(r, color, w, opacity){ const m = new T.Mesh(new T.TorusGeometry(r, w||0.006, 8, 160), new T.MeshBasicMaterial({color, transparent:true, opacity:opacity==null?0.8:opacity, depthWrite:false, blending:T.AdditiveBlending})); return m; }
function arrow(color, len, head){ const g = new T.Group(); const mat = new T.MeshBasicMaterial({color, transparent:true, opacity:0.95, depthWrite:false});
  const shaft = new T.Mesh(new T.CylinderGeometry(0.012, 0.012, 1, 10), mat); const tip = new T.Mesh(new T.ConeGeometry(0.045, head||0.14, 16), mat);
  g.add(shaft); g.add(tip); g.userData = {shaft, tip, head:head||0.14}; setArrow(g, new T.Vector3(), new T.Vector3(0,len||1,0)); return g; }
function setArrow(a, from, vec){ const L = vec.length(), u = a.userData, h = Math.min(u.head, L*0.45); const dir = L > 1e-9 ? vec.clone().divideScalar(L) : new T.Vector3(0,1,0);
  a.position.copy(from); a.quaternion.setFromUnitVectors(new T.Vector3(0,1,0), dir);
  u.shaft.scale.set(1, Math.max(1e-4, L-h), 1); u.shaft.position.set(0, (L-h)/2, 0); u.tip.position.set(0, L-h/2, 0); u.tip.scale.setScalar(L > 1e-6 ? 1 : 1e-4); a.visible = L > 1e-6; }
function bar(w, d, color){ const m = new T.Mesh(new T.BoxGeometry(w, 1, d), new T.MeshStandardMaterial({color, emissive:color, emissiveIntensity:0.55, roughness:0.35, metalness:0.1, transparent:true, opacity:0.92}));
  m.geometry.translate(0, 0.5, 0); return m; }
function setBar(m, h){ m.scale.y = Math.max(1e-3, h); }
function slab(w, h, d, color, opacity){ return new T.Mesh(new T.BoxGeometry(w, h, d), new T.MeshBasicMaterial({color, transparent:true, opacity:opacity==null?0.12:opacity, depthWrite:false, blending:T.AdditiveBlending})); }
function grid(size, n, color, opacity){ const pts = []; const h = size/2; for(let i=0;i<=n;i++){ const t = -h + size*i/n; pts.push(new T.Vector3(t,0,-h), new T.Vector3(t,0,h), new T.Vector3(-h,0,t), new T.Vector3(h,0,t)); }
  return new T.LineSegments(new T.BufferGeometry().setFromPoints(pts), new T.LineBasicMaterial({color, transparent:true, opacity, depthWrite:false})); }
function trail(n, size){ const p = points(n, size); p.userData = {n, i:0, filled:0}; return p; }
function pushTrail(p, P, c){ const u = p.userData, a = p.geometry.attributes;
  a.position.setXYZ(u.i, P.x, P.y, P.z); u.i = (u.i+1) % u.n; u.filled = Math.min(u.n, u.filled+1);
  for(let k=0;k<u.n;k++){ const age = ((u.i - 1 - k) % u.n + u.n) % u.n; const f = k < u.filled ? Math.pow(1 - age/u.n, 1.6)*0.9 : 0; a.color.setXYZ(k, c[0]*f, c[1]*f, c[2]*f); }
  a.position.needsUpdate = a.color.needsUpdate = true; }
function clearTrail(p){ p.userData.i = 0; p.userData.filled = 0; const a = p.geometry.attributes; a.color.array.fill(0); a.color.needsUpdate = true; }
/* terrain: height H(a,b) and colour C(a,b) over an N x M grid spanning x in [x0,x1], z in [z0,z1] */
function surface(N, M, x0, x1, z0, z1, opacity){ const geo = new T.PlaneGeometry(1, 1, N-1, M-1); geo.rotateX(-Math.PI/2);
  geo.setAttribute('color', new T.BufferAttribute(new Float32Array(N*M*3),3));
  const mesh = new T.Mesh(geo, new T.MeshStandardMaterial({vertexColors:true, roughness:0.6, metalness:0.0, side:T.DoubleSide, transparent:true, opacity:opacity==null?0.78:opacity, depthWrite:false}));
  const wire = new T.LineSegments(new T.WireframeGeometry(geo), new T.LineBasicMaterial({color:0x5ab0ff, transparent:true, opacity:0.07, depthWrite:false}));
  const grp = new T.Group(); grp.add(mesh); grp.add(wire); grp.userData = {N, M, x0, x1, z0, z1, geo, wire}; return grp; }
function setSurface(s, H, C){ const u = s.userData, pos = u.geo.attributes.position, col = u.geo.attributes.color;
  for(let b=0;b<u.M;b++) for(let a=0;a<u.N;a++){ const i = b*u.N + a; const x = u.x0 + (u.x1-u.x0)*a/(u.N-1), z = u.z0 + (u.z1-u.z0)*b/(u.M-1);
    pos.setXYZ(i, x, H(a,b), z); const c = C(a,b); col.setXYZ(i, c[0], c[1], c[2]); }
  pos.needsUpdate = col.needsUpdate = true; u.geo.computeVertexNormals(); u.geo.computeBoundingSphere();
  u.wire.geometry.dispose(); u.wire.geometry = new T.WireframeGeometry(u.geo); }
/* floating label, always facing the camera */
function label(text, color, scale){ const c = document.createElement('canvas'), x = c.getContext('2d'), f = 46;
  const font = `500 ${f}px "Instrument Sans",system-ui,sans-serif`; x.font = font; const w = Math.ceil(x.measureText(text).width) + 28; c.width = w; c.height = f + 22;
  x.font = font; x.fillStyle = color || '#c9d6ec'; x.textBaseline = 'middle'; x.fillText(text, 14, c.height/2);
  const tex = new T.CanvasTexture(c); tex.colorSpace = T.SRGBColorSpace; tex.anisotropy = 4;
  const s = new T.Sprite(new T.SpriteMaterial({map:tex, transparent:true, depthWrite:false, depthTest:false}));
  const k = 0.55*(scale || 0.3) / f; s.scale.set(w*k, c.height*k, 1); s.renderOrder = 10; s.userData.text = text; return s; }
function relabel(s, text, color){ if(s.userData.text === text) return; const n = label(text, color, s.userData.scale); s.material.map.dispose(); s.material.map = n.material.map; s.scale.copy(n.scale); s.userData.text = text; }

/* ---------- stage ---------- */
function stage(canvas, layout){
  const renderer = new T.WebGLRenderer({canvas, antialias:true, preserveDrawingBuffer:true, powerPreference:'high-performance'});
  renderer.setPixelRatio(Math.min(2, window.devicePixelRatio||1)); renderer.toneMapping = T.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.05;
  const scene = new T.Scene(); const BG = new T.Color(0x03060c); scene.background = BG;
  scene.fog = new T.FogExp2(0x03060c, 0.018);
  const camera = new T.PerspectiveCamera(42, 1, 0.05, 400);
  const world = new T.Group(); scene.add(world);
  scene.add(new T.AmbientLight(0x9fb4d8, 0.55)); const key = new T.DirectionalLight(0xffffff, 1.1); key.position.set(3,6,4); scene.add(key);
  const rim = new T.DirectionalLight(0x6f8cff, 0.6); rim.position.set(-5,-2,-4); scene.add(rim);
  /* the sky behind the stars: a faint, slow starfield shared by every eye */
  const stars = points(1800, 0.22); { const a = stars.geometry.attributes; for(let i=0;i<1800;i++){ const u = Math.random()*2-1, ph = Math.random()*Math.PI*2, R = 70+Math.random()*60, s = Math.sqrt(1-u*u);
    a.position.setXYZ(i, R*s*Math.cos(ph), R*u, R*s*Math.sin(ph)); const b = 0.25+0.55*Math.random()**3, t = Math.random(); a.color.setXYZ(i, b*(0.75+0.25*t), b*0.85, b); } flush(stars); }
  stars.material.fog = false; scene.add(stars);
  const composer = new EffectComposer(renderer); composer.addPass(new RenderPass(scene, camera));
  const bloom = new UnrealBloomPass(new T.Vector2(512, 512), 0.6, 0.45, 0.3); composer.addPass(bloom); composer.addPass(new OutputPass());
  const V = { yaw:0.7, pitch:0.38, dist:7.2, ty:0.3, auto:true };
  function size(){ const w = Math.max(1, window.innerWidth), h = Math.max(1, window.innerHeight); renderer.setSize(w,h,false); composer.setSize(w,h); bloom.setSize(Math.round(w/2), Math.round(h/2));
    camera.aspect = w/h; camera.updateProjectionMatrix(); const L = layout(); if(L.shiftX || L.shiftY) camera.setViewOffset(w, h, -L.shiftX, -L.shiftY, w, h); else camera.clearViewOffset(); }
  window.addEventListener('resize', size);
  const ptrs = new Map(); let pinch0 = 0, dist0 = V.dist;
  canvas.addEventListener('pointerdown', e => { canvas.setPointerCapture(e.pointerId); ptrs.set(e.pointerId, {x:e.clientX, y:e.clientY}); V.auto = false;
    if(ptrs.size === 2){ const [a,b] = [...ptrs.values()]; pinch0 = Math.hypot(a.x-b.x, a.y-b.y); dist0 = V.dist; } });
  canvas.addEventListener('pointermove', e => { if(!ptrs.has(e.pointerId)) return; const p = ptrs.get(e.pointerId);
    if(ptrs.size === 1){ V.yaw -= (e.clientX - p.x)*0.006; V.pitch = Math.max(-1.35, Math.min(1.35, V.pitch + (e.clientY - p.y)*0.006)); }
    p.x = e.clientX; p.y = e.clientY;
    if(ptrs.size === 2){ const [a,b] = [...ptrs.values()]; const d = Math.hypot(a.x-b.x, a.y-b.y); if(pinch0) V.dist = Math.max(2.5, Math.min(30, dist0*pinch0/d)); } });
  ['pointerup','pointercancel'].forEach(t => canvas.addEventListener(t, e => { ptrs.delete(e.pointerId); if(ptrs.size < 2) pinch0 = 0; }));
  canvas.addEventListener('wheel', e => { e.preventDefault(); V.dist = Math.max(2.5, Math.min(30, V.dist*Math.exp(e.deltaY*0.001))); }, {passive:false});
  const still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let last = performance.now(), tick = null;
  function frame(now){
    const dt = Math.min(0.05, (now - last)/1000); last = now;
    if(V.auto && !still) V.yaw += dt*0.06;
    const D = V.dist*(window.innerWidth < 720 ? 1.45 : 1);
    camera.position.set(D*Math.cos(V.pitch)*Math.sin(V.yaw), V.ty + D*Math.sin(V.pitch), D*Math.cos(V.pitch)*Math.cos(V.yaw));
    camera.lookAt(0, V.ty, 0); stars.rotation.y += dt*0.004;
    if(tick) tick(still ? 0.016 : dt, now/1000);
    composer.render();
    requestAnimationFrame(frame);
  }
  return { T, scene, camera, renderer, world, composer, bloom, stars, view:V, resize:size, still,
    start(fn){ tick = fn; size(); requestAnimationFrame(frame); },
    setView(v){ V.yaw = v[0]; V.pitch = v[1]; V.dist = v[2]; V.ty = v[3] == null ? 0.3 : v[3]; V.auto = v[4] !== false; },
    overlay(on){ scene.background = on ? new T.Color(0x000000) : BG; scene.fog.color.set(on ? 0x000000 : 0x03060c); stars.visible = !on; } };
}

/* ---------- the shell: Atlas Memoriae instrument layout ---------- */
const CSS = `
:root{--void:#03060c;--glass:rgba(9,14,27,.66);--glass2:rgba(14,21,38,.72);--edge:rgba(150,185,255,.13);--edge2:rgba(150,185,255,.26);
--ink:#e8eefb;--dim:#93a3c0;--faint:#5b6a86;--metric:#5ab0ff;--twist:#b18cff;--gap:#ffb547;--tail:#4fe3c1;--tip:#ff6f91;
--ui:"Instrument Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--math:"STIX Two Text","Cambria Math","Times New Roman",serif;
--rail:236px;--card:372px;--bar:64px;color-scheme:dark}
*{box-sizing:border-box}html,body{height:100%}
body{margin:0;background:var(--void);color:var(--ink);font-family:var(--ui);font-size:14px;line-height:1.5;overflow:hidden;-webkit-font-smoothing:antialiased;font-variant-numeric:tabular-nums}
#stage{position:fixed;inset:0;width:100%;height:100%;touch-action:none;cursor:grab;display:block}#stage:active{cursor:grabbing}
.vig{position:fixed;inset:0;pointer-events:none;background:radial-gradient(120% 90% at 55% 45%,transparent 55%,rgba(0,0,0,.55) 100%)}
.glass{background:var(--glass);border:1px solid var(--edge);backdrop-filter:blur(18px) saturate(1.2);-webkit-backdrop-filter:blur(18px) saturate(1.2);border-radius:14px}
button{font:inherit;color:inherit;background:none;border:0;cursor:pointer;padding:0}
:focus-visible{outline:2px solid var(--metric);outline-offset:2px;border-radius:6px}
/* masthead */
.mast{position:fixed;top:18px;left:22px;max-width:calc(100% - var(--card) - 70px);pointer-events:none}
.mast h1{font-family:var(--math);font-weight:400;font-size:30px;line-height:1.05;letter-spacing:-.005em;margin:0}
.mast p{margin:4px 0 0;color:var(--dim);font-size:13px}
.mast a{pointer-events:auto;color:var(--dim)}
/* spectrum rail: each eye is a level, acts are clusters held apart by gaps */
.rail{position:fixed;left:14px;top:96px;bottom:calc(var(--bar) + 26px);width:var(--rail);padding:12px 10px 12px 12px;overflow:auto;scrollbar-width:thin}
.act{position:relative;padding-left:18px}
.act+.act{margin-top:22px}
.act::before{content:"";position:absolute;left:5px;top:4px;bottom:4px;width:2px;border-radius:2px;background:linear-gradient(var(--tail),rgba(79,227,193,.15))}
.act+.act::after{content:"";position:absolute;left:0;top:-15px;width:12px;height:8px;border-top:1px solid var(--gap);border-bottom:1px solid var(--gap);opacity:.6}
.act h2{font-family:var(--math);font-style:italic;font-weight:400;font-size:14.5px;color:var(--dim);margin:0 0 4px}
.lv{display:flex;align-items:center;gap:10px;width:100%;text-align:left;padding:5px 6px 5px 0;color:var(--dim);font-size:13px;border-radius:6px;position:relative}
.lv i{flex:none;width:18px;height:2px;border-radius:2px;background:var(--faint);transition:width .25s,background .25s,box-shadow .25s;margin-left:-14px}
.lv:hover{color:var(--ink)}.lv:hover i{background:var(--dim)}
.lv[aria-current=true]{color:var(--ink)}.lv[aria-current=true] i{width:26px;background:var(--metric);box-shadow:0 0 10px var(--metric)}
.lv b{font-weight:400;color:var(--faint);font-size:11.5px;min-width:16px}
/* eye card */
.card{position:fixed;top:18px;right:18px;width:var(--card);max-height:calc(100% - var(--bar) - 44px);overflow:auto;padding:18px 18px 16px;display:grid;gap:12px;scrollbar-width:thin}
.card .sec{display:flex;justify-content:space-between;gap:12px;font-size:12.5px;color:var(--dim)}
.grade{padding:1px 8px;border-radius:99px;border:1px solid var(--edge2);color:var(--ink);font-size:11.5px;white-space:nowrap}
.grade[data-g=proved]{border-color:rgba(79,227,193,.5);color:var(--tail)}.grade[data-g=data]{border-color:rgba(255,181,71,.5);color:var(--gap)}
.grade[data-g=structural]{border-color:rgba(255,111,145,.5);color:var(--tip)}.grade[data-g=computed]{border-color:rgba(90,176,255,.5);color:var(--metric)}
.card h3{font-size:21px;font-weight:600;letter-spacing:-.01em;margin:0;line-height:1.2}
.eq{font-family:var(--math);font-size:19px;line-height:1.45;color:#f4f7ff;white-space:pre-wrap;padding:2px 0}
.what{color:var(--dim);margin:0;font-size:13.5px;line-height:1.55}
.ctl{display:grid;gap:10px}
.ctl label{display:grid;grid-template-columns:1fr auto;gap:4px 8px;font-size:12.5px;color:var(--dim)}
.ctl output{color:var(--ink)}
input[type=range]{grid-column:1/-1;width:100%;height:18px;margin:0;background:none;-webkit-appearance:none;appearance:none}
input[type=range]::-webkit-slider-runnable-track{height:3px;border-radius:3px;background:linear-gradient(90deg,var(--metric) var(--f,50%),rgba(150,185,255,.18) var(--f,50%))}
input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:14px;height:14px;border-radius:50%;background:#fff;margin-top:-5.5px;box-shadow:0 0 0 4px rgba(90,176,255,.25)}
input[type=range]::-moz-range-track{height:3px;border-radius:3px;background:rgba(150,185,255,.18)}input[type=range]::-moz-range-progress{height:3px;background:var(--metric);border-radius:3px}
input[type=range]::-moz-range-thumb{width:14px;height:14px;border:0;border-radius:50%;background:#fff}
.seg{display:flex;flex-wrap:wrap;gap:4px;padding:3px;border-radius:10px;background:rgba(150,185,255,.06);border:1px solid var(--edge)}
.seg button{flex:1 1 auto;padding:5px 10px;border-radius:7px;font-size:12.5px;color:var(--dim)}
.seg button[aria-pressed=true]{background:rgba(90,176,255,.16);color:var(--ink)}
.read{display:grid;gap:6px;border-top:1px solid var(--edge);padding-top:12px}
.read div{display:flex;justify-content:space-between;align-items:baseline;gap:12px;font-size:12.5px;color:var(--dim)}
.read b{font-weight:500;color:var(--ink);font-size:14px;text-align:right}
.read b[data-t=metric]{color:var(--metric)}.read b[data-t=twist]{color:var(--twist)}.read b[data-t=gap]{color:var(--gap)}.read b[data-t=tail]{color:var(--tail)}.read b[data-t=tip]{color:var(--tip)}
.legend{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:12px;color:var(--dim)}.legend span::before{content:"";display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:6px;background:var(--c);box-shadow:0 0 8px var(--c);vertical-align:-1px}
/* transport */
.bar{position:fixed;left:14px;right:14px;bottom:14px;height:var(--bar);display:flex;align-items:center;gap:14px;padding:0 14px}
.tb{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:38px;min-width:38px;padding:0 12px;border-radius:10px;color:var(--ink);font-size:13px;border:1px solid var(--edge)}
.tb:hover{border-color:var(--edge2);background:rgba(150,185,255,.06)}.tb[aria-pressed=true]{border-color:var(--metric);background:rgba(90,176,255,.14)}
.tb svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.tb.rec[aria-pressed=true]{border-color:var(--tip);background:rgba(255,111,145,.14);color:#ffd2dc}
.line{flex:1;display:flex;align-items:center;gap:3px;height:38px;min-width:0}
.line .grp{display:flex;gap:3px;flex:var(--n) 1 0;min-width:0}.line .grp+.grp{margin-left:9px}
.line button{flex:1;height:22px;border-radius:5px;position:relative;overflow:hidden;background:rgba(150,185,255,.07)}
.line button:hover{background:rgba(150,185,255,.16)}
.line button[aria-current=true]{background:rgba(90,176,255,.22)}
.line button i{position:absolute;left:0;top:0;bottom:0;width:0;background:linear-gradient(90deg,rgba(90,176,255,.5),rgba(79,227,193,.65))}
.sel{height:38px;border-radius:10px;border:1px solid var(--edge);background:transparent;color:var(--ink);font:inherit;font-size:13px;padding:0 8px}
.sel option{background:#0b1222}
.cleanexit{position:fixed;right:16px;bottom:16px;display:none;opacity:.35;font-size:12px;color:var(--dim)}
body.clean .rail,body.clean .card,body.clean .bar,body.clean .mast,body.clean .vig{display:none}body.clean .cleanexit{display:block}
.toast{position:fixed;left:50%;bottom:96px;transform:translateX(-50%);padding:8px 14px;border-radius:10px;font-size:13px;opacity:0;transition:opacity .3s;pointer-events:none}
.toast.on{opacity:1}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
@media (max-width:1100px){:root{--rail:200px;--card:330px}.mast h1{font-size:24px}}
@media (max-width:720px){
 :root{--bar:56px}
 .mast{top:10px;left:14px;right:14px;max-width:none}.mast h1{font-size:20px}.mast p{display:none}
 .rail{top:44px;left:8px;right:8px;bottom:auto;width:auto;height:46px;display:flex;gap:16px;overflow-x:auto;overflow-y:hidden;padding:6px 10px;align-items:center;white-space:nowrap}
 .act{display:flex;align-items:center;gap:4px;padding-left:0}.act+.act{margin-top:0}.act::before,.act+.act::after,.act h2{display:none}
 .lv{padding:4px 8px;width:auto;border:1px solid var(--edge);border-radius:99px;font-size:12px}.lv i{display:none}.lv[aria-current=true]{border-color:var(--metric)}
 .card{top:auto;right:8px;left:8px;bottom:calc(var(--bar) + 16px);width:auto;max-height:44%;padding:14px}
 .card>*{order:10}.card .sec{order:0}.card h3{order:1}.card .read{order:2;border-top:0;padding-top:0}.card .ctl{order:3}.card .eq{order:4;font-size:17px}.card .what{order:5}.card .legend{order:6}
 .bar{left:8px;right:8px;bottom:8px;gap:6px;padding:0 8px}.bar .wide{display:none}.line .grp+.grp{margin-left:5px}
}`;

const ICON = {
  prev:'<svg viewBox="0 0 24 24"><path d="M15 6l-6 6 6 6"/></svg>', next:'<svg viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"/></svg>',
  play:'<svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z"/></svg>', pause:'<svg viewBox="0 0 24 24"><path d="M8 5v14M16 5v14"/></svg>',
  clean:'<svg viewBox="0 0 24 24"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/></svg>', png:'<svg viewBox="0 0 24 24"><rect x="3.5" y="5.5" width="17" height="13" rx="2"/><circle cx="9" cy="10.5" r="1.6"/><path d="M20 16l-5-5-8 8"/></svg>',
  rec:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="5.5"/></svg>', layer:'<svg viewBox="0 0 24 24"><path d="M12 4l8.5 4.5L12 13 3.5 8.5z"/><path d="M3.5 13L12 17.5 20.5 13"/></svg>'
};

function run(MIX){
  const st = document.createElement('style'); st.textContent = CSS; document.head.append(st);
  const eyes = MIX.eyes, byId = {}; eyes.forEach(e => byId[e.id] = e);
  const order = MIX.acts.flatMap(a => a.eyes);
  document.body.insertAdjacentHTML('beforeend', `
<canvas id="stage" aria-label="3D view of the current eye. Drag to turn, scroll or pinch to zoom."></canvas><div class="vig"></div>
<header class="mast"><h1>${MIX.title}</h1><p>${MIX.subtitle||''}</p></header>
<nav class="rail glass" id="rail" aria-label="Eyes"></nav>
<section class="card glass" id="card" aria-live="polite">
  <div class="sec"><span id="c_sec"></span><span class="grade" id="c_grade"></span></div>
  <h3 id="c_title"></h3><div class="eq" id="c_eq"></div><p class="what" id="c_what"></p>
  <div class="legend" id="c_leg"></div><div class="ctl" id="c_ctl"></div><div class="read" id="c_read"></div>
</section>
<footer class="bar glass">
  <button class="tb" id="b_prev" aria-label="Previous eye">${ICON.prev}</button>
  <button class="tb" id="b_play" aria-pressed="false" aria-label="Play the film">${ICON.play}<span class="wide">Film</span></button>
  <button class="tb" id="b_next" aria-label="Next eye">${ICON.next}</button>
  <div class="line" id="line"></div>
  <select class="sel wide" id="b_sec" aria-label="Seconds per eye"><option value="6">6 s</option><option value="8">8 s</option><option value="10" selected>10 s</option><option value="15">15 s</option><option value="20">20 s</option><option value="30">30 s</option></select>
  <button class="tb wide" id="b_over" aria-pressed="false" title="Black ground for screen blending over footage">${ICON.layer}<span>Overlay</span></button>
  <button class="tb" id="b_clean" aria-label="Clean view">${ICON.clean}</button>
  <button class="tb wide" id="b_png" aria-label="Save frame as PNG">${ICON.png}</button>
  <button class="tb rec wide" id="b_rec" aria-pressed="false" aria-label="Record the stage as video">${ICON.rec}<span>Record</span></button>
</footer>
<button class="cleanexit" id="b_back">Show controls</button><div class="toast glass" id="toast" role="status"></div>`);
  const $ = id => document.getElementById(id);
  const isMobile = () => window.innerWidth <= 720;
  const layout = () => { const w = window.innerWidth; if(document.body.classList.contains('clean')) return {shiftX:0, shiftY:0};
    if(isMobile()) return {shiftX:0, shiftY:-window.innerHeight*0.16};
    const cs = getComputedStyle(document.documentElement), rail = parseFloat(cs.getPropertyValue('--rail'))+14, card = parseFloat(cs.getPropertyValue('--card'))+18;
    return {shiftX:(rail - card)/2, shiftY:0}; };
  const S3 = stage($('stage'), layout);
  /* rail and timeline */
  MIX.acts.forEach(a => {
    const div = document.createElement('div'); div.className = 'act'; div.innerHTML = `<h2>${a.name}</h2>`;
    const grp = document.createElement('div'); grp.className = 'grp'; grp.style.setProperty('--n', a.eyes.length);
    a.eyes.forEach(id => { const n = order.indexOf(id)+1;
      const b = document.createElement('button'); b.className = 'lv'; b.dataset.id = id; b.innerHTML = `<i></i><b>${n}</b><span>${byId[id].title}</span>`; b.addEventListener('click', () => { stopFilm(); show(id); }); div.append(b);
      const s = document.createElement('button'); s.dataset.id = id; s.setAttribute('aria-label', `${n}. ${byId[id].title}`); s.title = `${n}. ${byId[id].title}`; s.innerHTML = '<i></i>'; s.addEventListener('click', () => { if(film) { fi = order.indexOf(id); t0 = performance.now()/1000; } show(id); }); grp.append(s); });
    $('rail').append(div); $('line').append(grp); });
  /* per-eye state */
  eyes.forEach(e => { e.p = {}; (e.controls||[]).forEach(c => e.p[c.id] = c.value); (e.choices||[]).forEach(c => e.p[c.id] = c.value);
    e.group = new T.Group(); e.ctx = {S3, T, p:e.p, eye:e, M:API}; e.make(e.group, e.ctx); });
  let cur = null, film = false, fi = 0, t0 = 0, tEye = 0;
  const fmt = (c, v) => c.fmt ? c.fmt(v) : (+v).toFixed(c.dp == null ? 2 : c.dp);
  const fill = el => { const f = 100*(el.value - el.min)/(el.max - el.min); el.style.setProperty('--f', f + '%'); };
  function controls(e){
    const C = e.controls || [], H = e.choices || [];
    $('c_ctl').innerHTML = H.map(h => `<div class="seg" role="group" aria-label="${h.label}">${h.options.map(o => `<button data-h="${h.id}" data-v="${o[0]}" aria-pressed="${String(e.p[h.id])===String(o[0])}">${o[1]}</button>`).join('')}</div>`).join('')
      + C.map(c => `<label>${c.label} <output id="o_${c.id}">${fmt(c, e.p[c.id])}</output><input id="p_${c.id}" type="range" min="${c.min}" max="${c.max}" step="${c.step}" value="${e.p[c.id]}" aria-label="${c.label}"></label>`).join('');
    C.forEach(c => { const el = $('p_'+c.id); fill(el); el.addEventListener('input', ev => { e.p[c.id] = +ev.target.value; $('o_'+c.id).textContent = fmt(c, e.p[c.id]); fill(el); if(e.change) e.change(e.ctx, c.id); }); });
    $('c_ctl').querySelectorAll('.seg button').forEach(b => b.addEventListener('click', () => { const h = H.find(x => x.id === b.dataset.h); const v = typeof h.value === 'number' ? +b.dataset.v : b.dataset.v;
      e.p[h.id] = v; b.parentElement.querySelectorAll('button').forEach(x => x.setAttribute('aria-pressed', x === b)); if(e.change) e.change(e.ctx, h.id); }));
  }
  function show(id){
    if(!byId[id]) id = order[0];
    if(cur){ S3.world.remove(cur.group); if(cur.leave) cur.leave(cur.ctx); }
    cur = byId[id]; S3.world.add(cur.group); tEye = 0;
    document.querySelectorAll('[data-id]').forEach(b => b.setAttribute('aria-current', b.dataset.id === id));
    const n = order.indexOf(id)+1; $('c_sec').textContent = `Eye ${n} of ${order.length}, ${cur.section}`;
    $('c_grade').textContent = cur.gradeLabel || cur.grade; $('c_grade').dataset.g = cur.grade;
    $('c_title').textContent = cur.title; $('c_eq').textContent = cur.eq; $('c_what').textContent = cur.text;
    $('c_leg').innerHTML = (cur.legend||[]).map(l => `<span style="--c:${l[0]}">${l[1]}</span>`).join('');
    controls(cur); S3.setView(cur.view || [0.7,0.38,7.2,0.3]);
    if(cur.enter) cur.enter(cur.ctx);
    try { if(history.replaceState) history.replaceState(null, '', '#' + id); } catch(err) { /* sandboxed previews refuse URL changes; the eye still shows */ }
    const lv = document.querySelector(`.lv[data-id="${id}"]`); if(lv && lv.scrollIntoView) lv.scrollIntoView({block:'nearest', inline:'nearest'});
  }
  function step(d){ const i = (order.indexOf(cur.id) + d + order.length) % order.length; if(film){ fi = i; t0 = performance.now()/1000; } show(order[i]); }
  function startFilm(){ film = true; fi = order.indexOf(cur.id); t0 = performance.now()/1000; $('b_play').setAttribute('aria-pressed', true); $('b_play').innerHTML = ICON.pause + '<span class="wide">Film</span>'; }
  function stopFilm(){ film = false; $('b_play').setAttribute('aria-pressed', false); $('b_play').innerHTML = ICON.play + '<span class="wide">Film</span>'; document.querySelectorAll('.line i').forEach(i => i.style.width = '0'); }
  const toast = m => { const t = $('toast'); t.textContent = m; t.classList.add('on'); clearTimeout(toast.h); toast.h = setTimeout(() => t.classList.remove('on'), 2200); };
  $('b_prev').addEventListener('click', () => step(-1)); $('b_next').addEventListener('click', () => step(1));
  $('b_play').addEventListener('click', () => film ? stopFilm() : startFilm());
  const clean = on => { document.body.classList.toggle('clean', on); S3.resize(); };
  $('b_clean').addEventListener('click', () => clean(true)); $('b_back').addEventListener('click', () => clean(false));
  $('b_over').addEventListener('click', e => { const on = e.currentTarget.getAttribute('aria-pressed') !== 'true'; e.currentTarget.setAttribute('aria-pressed', on); S3.overlay(on); toast(on ? 'Overlay on: black ground for screen blending' : 'Overlay off'); });
  const fname = ext => (MIX.short || MIX.title).replace(/[^A-Za-z0-9]+/g,'_') + '_' + (order.indexOf(cur.id)+1) + '_' + cur.id + '.' + ext;
  $('b_png').addEventListener('click', () => { S3.composer.render(); const a = document.createElement('a'); a.href = $('stage').toDataURL('image/png'); a.download = fname('png'); a.click(); toast('Frame saved'); });
  let rec = null, chunks = [];
  $('b_rec').addEventListener('click', e => { const b = e.currentTarget;
    if(rec){ rec.stop(); return; }
    if(!window.MediaRecorder || !$('stage').captureStream){ toast('This browser cannot record the stage'); return; }
    const types = ['video/webm;codecs=vp9','video/webm;codecs=vp8','video/webm','video/mp4']; const type = types.find(t => MediaRecorder.isTypeSupported(t)) || '';
    chunks = []; rec = new MediaRecorder($('stage').captureStream(60), {mimeType:type, videoBitsPerSecond:16e6});
    rec.ondataavailable = ev => ev.data.size && chunks.push(ev.data);
    rec.onstop = () => { const blob = new Blob(chunks, {type: rec.mimeType}); const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = fname(rec.mimeType.includes('mp4') ? 'mp4' : 'webm'); a.click(); rec = null; b.setAttribute('aria-pressed', false); b.querySelector('span').textContent = 'Record'; toast('Recording saved'); };
    rec.start(250); b.setAttribute('aria-pressed', true); b.querySelector('span').textContent = 'Stop'; toast('Recording the stage'); });
  document.addEventListener('keydown', e => { if(e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;
    if(e.key === 'ArrowRight') step(1); else if(e.key === 'ArrowLeft') step(-1); else if(e.key === ' '){ e.preventDefault(); film ? stopFilm() : startFilm(); }
    else if(e.key === 'c' || e.key === 'C') clean(!document.body.classList.contains('clean')); else if(e.key === 'Escape') clean(false); });
  let readT = 0;
  S3.start((dt, now) => {
    tEye += dt;
    if(film){ const sec = +$('b_sec').value, t = now - t0; if(t > sec){ fi = (fi+1) % order.length; t0 = now; show(order[fi]); }
      document.querySelectorAll('.line button').forEach(b => { const k = order.indexOf(b.dataset.id); b.firstChild.style.width = k < fi ? '100%' : k === fi ? (100*Math.min(1,(now-t0)/sec)) + '%' : '0'; }); }
    let rows = null; try { rows = cur.step ? cur.step(dt, tEye, cur.ctx) : null; } catch(err) { if(!cur.warned){ cur.warned = true; console.error('eye ' + cur.id + ': ' + err.message); } }
    readT += dt; if(rows && readT > 0.15){ readT = 0; $('c_read').innerHTML = rows.map(r => `<div><span>${r[0]}</span><b${r[2] ? ` data-t="${r[2]}"` : ''}>${r[1]}</b></div>`).join(''); }
  });
  let start = order[0]; try { if(location.hash) start = decodeURIComponent(location.hash.slice(1)); } catch(err) {}
  show(start);
  window.addEventListener('resize', () => S3.resize());
  window.MIXER_API = { show, step, startFilm, stopFilm, clean, overlay:S3.overlay, eyes:byId, get cur(){ return cur; }, S3 };
}

const API = { T, PAL, hex, rgb, sprite, points, setPt, flush, line, setLine, dashed, setDashed, tube, setTube, orb, paintOrb, glass, ring, arrow, setArrow, bar, setBar, slab, grid, trail, pushTrail, clearTrail, surface, setSurface, label, relabel, stage, run };
window.Mixer3D2 = API;


/* SCRIPT: iqgt_mixer_3d_v5_body (eye 8, frozen ridge) — the paper's own eye, on 3D Mixer Parts v2 */
const M = API, V3 = (x,y,z) => new T.Vector3(x,y,z);
const Cr = window.Core, IQ = window.IQ;

/* ---------- eye 8: the frozen ridge (v7.3.1 §8.3–8.4, Figure 10) ---------- */
const ridge = (() => {
  const fam = Cr.families.polar;                       // g = diag((9/4) sin^2 y, 1/4); gap 2 everywhere
  const X = x => (x - 1.3)*1.5, Z = y => (0.35 - y)*2.6, Hh = y => 1.7*Math.abs(Math.sin(y));
  const P = (x, y, lift) => V3(X(x), Hh(y) + (lift||0.012), Z(y));
  const Y0 = 0.6, X0 = 0.08, SHOW = [20, 35, 50, 65];
  const runAll = (th, n) => Cr.geodesic(fam.a, fam.b, X0, Y0, th, 2.6, n);
  const run = (th, n) => { n = n || 2600; const p = Cr.geodesic(fam.a, fam.b, X0, Y0, th, 2.6, n); const out = []; for(const q of p){ if(q[0] > 2.62 || q[1] > 0.86) break; out.push(q); } return out; };
  const drift = (path, th, n) => { const dt = 2.6/n, C0 = fam.a(0, Y0)*Math.sin(th*Math.PI/180)**2; let w = 0;
    for(let i=1;i<path.length-1;i++){ const y = path[i][1], u = (path[i+1][0]-path[i-1][0])/(2*dt), a = fam.a(0, y); w = Math.max(w, Math.abs(a*a*u*u - C0)); } return {C0, w}; };
  const turnY = path => { let k = 0; path.forEach((q, i) => { if(q[1] < path[k][1]) k = i; }); if(k < 1 || k > path.length-2) return path[k][1];
    const a = path[k-1][1], b = path[k][1], c = path[k+1][1], den = a - 2*b + c; return den > 0 ? b - (a - c)*(a - c)/(8*den) : b; };
  return {
    id:'ridge', title:'Frozen ridge', section:'§8.3–8.4, Figure 10', grade:'proved', gradeLabel:'Proved and integrated',
    eq:'𝑔∥ sin²𝜃 = 𝐶      𝑔∥ = (9/4) sin²𝑦\nturning line:  sin 𝑦* = sin 𝑦₀ sin 𝜃₀',
    text:'Along y = 0 the whole line is one projector: the subspace stops rotating, so the index √g∥ falls to zero while the gap stays at 2. Every geodesic carries its own Clairaut level C, and since sin²θ can never pass 1 it can only visit ground where g∥ ≥ C. Aimed at the ridge, it turns back tangentially, as light does at a glass edge. Only an exactly normal path reaches it.',
    legend:[['#5ab0ff','geodesics, launched at y = 0.60'],['#ffffff','the one you steer'],['#ffb547','the polar line and turning levels']],
    controls:[{id:'th', label:'Incidence of your path (degrees)', min:5, max:85, step:1, value:35, dp:0}],
    view:[0.95, 0.62, 6.4, 0.25],
    make(g, ctx){
      const N = 90, Mm = 60, s = M.surface(N, Mm, X(0), X(2.6), Z(-0.15), Z(0.85), 0.82); ctx.surf = s; g.add(s);
      const lo = new T.Color(0x0a1530), hi = new T.Color(0x2f7fd8), am = new T.Color(0xffb547);
      M.setSurface(s, (a, b) => Hh(-0.15 + 1.0*b/(Mm-1)), (a, b) => { const y = -0.15 + 1.0*b/(Mm-1), t = Math.min(1, Math.abs(Math.sin(y))/0.75);
        const c = lo.clone().lerp(hi, t); c.lerp(am, Math.max(0, 1 - Math.abs(y)/0.05)*0.85); return [c.r, c.g, c.b]; });
      const pole = []; for(let i=0;i<=60;i++) pole.push(P(2.6*i/60, 0, 0.02)); g.add(M.tube(pole, 0.022, PAL.gap, 0.95));
      const lab = M.label('the whole line is one projector', '#b98a45', 0.24); lab.position.copy(P(2.3, -0.12, 0.25)); g.add(lab);
      const lab2 = M.label('index √g∥', '#6f8fb8', 0.22); lab2.position.copy(P(2.75, 0.85, 0.2)); g.add(lab2);
      const lab3 = M.label('gap stays 2', '#b98a45', 0.2); lab3.position.copy(P(-0.1, -0.12, 0.2)); g.add(lab3);
      ctx.paths = SHOW.map(th => { const path = run(th), pts = path.map(q => P(q[0], q[1], 0.02));
        const tb = M.tube(pts, 0.012, PAL.metric, 0.55); g.add(tb);
        const ys = IQ.polarTurn(Y0, th*Math.PI/180), lv = []; for(let i=0;i<=40;i++) lv.push(P(2.6*i/40, ys, 0.015)); const d = M.dashed(lv, PAL.gap, 0.45); g.add(d);
        const bead = M.orb(0.03, PAL.metric, 5); g.add(bead); const tr = M.trail(90, 0.09); g.add(tr);
        const l = M.label(th + '°', '#6f8fb8', 0.17); l.position.copy(P(X0, Y0, 0.12)); return {th, path, pts, bead, tr, l}; });
      ctx.paths.forEach((p, i) => { p.l.position.copy(P(0.1 + 0.18*i, Y0 + 0.08, 0.1)); g.add(p.l); });
      const launch = M.orb(0.04, 0xffffff, 5); launch.position.copy(P(X0, Y0, 0.03)); g.add(launch);
      ctx.mine = M.tube([V3(), V3(0,0.01,0)], 0.02, 0xffffff, 0.95); g.add(ctx.mine);
      ctx.mineLv = M.dashed([V3(), V3(0.1,0,0)], 0xffffff, 0.8); g.add(ctx.mineLv);
      ctx.mineBead = M.orb(0.04, 0xffffff, 5); g.add(ctx.mineBead); ctx.mineTr = M.trail(120, 0.12); g.add(ctx.mineTr);
      const base = M.grid(4.6, 23, 0x5ab0ff, 0.05); base.position.y = -0.02; g.add(base);
      this.change(ctx);
    },
    change(ctx){ const th = ctx.p.th, path = run(th), fine = runAll(th, 26000); ctx.my = path; ctx.myPts = path.map(q => P(q[0], q[1], 0.03)); M.setTube(ctx.mine, ctx.myPts);
      const ys = IQ.polarTurn(Y0, th*Math.PI/180), lv = []; for(let i=0;i<=40;i++) lv.push(P(2.6*i/40, ys, 0.02)); M.setDashed(ctx.mineLv, lv);
      ctx.pred = ys; ctx.obs = turnY(fine); ctx.dr = drift(fine, th, 26000); M.clearTrail(ctx.mineTr); ctx.k = 0; },
    enter(ctx){ ctx.t0 = 0; },
    step(dt, t, ctx){
      const f = (t*0.22) % 1;
      ctx.paths.forEach(p => { if(!p.pts.length) return; const i = Math.max(0, Math.floor(f*(p.pts.length-1))); p.bead.position.copy(p.pts[i]); M.pushTrail(p.tr, p.pts[i], [0.35,0.69,1.0]); });
      if(ctx.myPts.length){ const j = Math.max(0, Math.floor(f*(ctx.myPts.length-1))); ctx.mineBead.position.copy(ctx.myPts[j]); M.pushTrail(ctx.mineTr, ctx.myPts[j], [1,1,1]); }
      return [['Clairaut level C = g∥ sin²θ at launch', ctx.dr.C0.toFixed(8), 'metric'],
        ['Predicted turning line y*', ctx.pred.toFixed(8), 'gap'], ['Integrated turning line', ctx.obs.toFixed(8), 'metric'],
        ['Difference', Math.abs(ctx.obs - ctx.pred).toExponential(1)], ['Drift of g∥ sin²θ (from path samples)', ctx.dr.w.toExponential(1)],
        ['Paper at 35°, C, predicted, integrated', '0.23600011, 0.32981248, 0.32981248', 'tail']]; }
  };
})();

M.run({ title:'Maps Don’t Make the Sky', short:'IQGT_Mixer_3D_v5', subtitle:'The intrinsic quantum geometric tensor, explored. Jeromie Beasley',
  acts:[{name:'The land under the map', eyes:['ridge']}], eyes:[ridge] });

