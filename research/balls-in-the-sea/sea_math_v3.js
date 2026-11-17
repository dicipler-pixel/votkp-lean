/* SCRIPT: SEA-MATH-V3
   The balls in the sea: mathematics. Jeromie Beasley. 17 Nov 2026. AI-assisted.
   The Flock of Balls on the Field is left as it is (FL-MATH-V2, MM-MATH-V1). Under it goes the sea: a projector P on everything light can
   occupy, the two levels of every ball and every point of every link. Each ball's part of it is the 2 x 2 block C_i.
   Three ways the sea can move, kept side by side because the runs do not choose between them:
     'tied'    travelling, tied at the start: P is half of the spectrum of the Flock's own one-step map, the cut in the widest gaps (a rest
               state), then moved by that step. Needs the stored rest sea for this layout.                         [MODEL CHOICE: the filled half]
     'untied'  travelling, not tied: each ball's own lower level filled, the links empty, moved by the same step.
     'atonce'  all at once: one matrix H = D + A on the balls only (the Moving Matrix way), P moved by exp(-iHt).
   Ends: 'sealed'; 'leak' (the arm balls lose to a matched load, rate 0.1); 'container' (each arm ball also opens on a stretch of length 2
   ending in a mirror). Feeds: one kick; small kicks in or out of time; a squeeze of all clock rates in or out of time.
   push: each ball's field is turned by the sea's spin on it, measured from rest, and held by its faces (the Flock's static rule).
   Pure functions; needs FL and MM. */
var SEA = (function(){
"use strict";
const GOLD = (1 + Math.sqrt(5))/2;
function csr(M, rows, cols, vr, vi){ const cnt = new Int32Array(M + 1); for(const r of rows) cnt[r+1]++; for(let r=0;r<M;r++) cnt[r+1] += cnt[r]; const ptr = Int32Array.from(cnt), c = new Int32Array(rows.length), a = new Float64Array(rows.length), b = new Float64Array(rows.length), pos = Int32Array.from(cnt.subarray(0, M));
  for(let k=0;k<rows.length;k++){ const q = pos[rows[k]]++; c[q] = cols[k]; a[q] = vr[k]; b[q] = vi[k]; } return { M, ptr, c, a, b }; }
/* Y = S X, X and Y dense M x M (row-major, separate real and imaginary parts) */
function mulRows(S, Xr, Xi, Yr, Yi){ const M = S.M; Yr.fill(0); Yi.fill(0);
  for(let r=0;r<M;r++){ const o = r*M; for(let k=S.ptr[r];k<S.ptr[r+1];k++){ const q = S.c[k]*M, a = S.a[k], b = S.b[k];
      if(b === 0){ if(a === 1){ for(let j=0;j<M;j++){ Yr[o+j] += Xr[q+j]; Yi[o+j] += Xi[q+j]; } } else { for(let j=0;j<M;j++){ Yr[o+j] += a*Xr[q+j]; Yi[o+j] += a*Xi[q+j]; } } }
      else { for(let j=0;j<M;j++){ const xr = Xr[q+j], xi = Xi[q+j]; Yr[o+j] += a*xr - b*xi; Yi[o+j] += a*xi + b*xr; } } } } }
function dagger(Xr, Xi, Yr, Yi, M){ for(let i=0;i<M;i++) for(let j=0;j<M;j++){ Yr[j*M+i] = Xr[i*M+j]; Yi[j*M+i] = -Xi[i*M+j]; } }
/* 2 x 2 unitary exp(-i h d.sigma) as [re00, im00, re01, im01, re10, im10, re11, im11] */
function rot2(d, h){ const m = Math.hypot(d[0], d[1], d[2]); if(m < 1e-300) return [1,0,0,0,0,0,1,0]; const c = Math.cos(m*h), s = Math.sin(m*h)/m; return [c, -s*d[2], -s*d[1], -s*d[0], s*d[1], -s*d[0], c, s*d[2]]; }
function turn2(n, th){ const c = Math.cos(th), s = Math.sin(th); return [c, -s*n[2], -s*n[1], -s*n[0], s*n[1], -s*n[0], c, s*n[2]]; }
/* P <- K P K^dagger on ball i's two rows and columns */
function local(E, i, K){ const M = E.M, Pr = E.Pr, Pi = E.Pi, r0 = 2*i*M, r1 = r0 + M;
  for(let j=0;j<M;j++){ const ar = Pr[r0+j], ai = Pi[r0+j], br = Pr[r1+j], bi = Pi[r1+j]; Pr[r0+j] = K[0]*ar - K[1]*ai + K[2]*br - K[3]*bi; Pi[r0+j] = K[0]*ai + K[1]*ar + K[2]*bi + K[3]*br; Pr[r1+j] = K[4]*ar - K[5]*ai + K[6]*br - K[7]*bi; Pi[r1+j] = K[4]*ai + K[5]*ar + K[6]*bi + K[7]*br; }
  const c0 = 2*i, c1 = c0 + 1;
  for(let j=0;j<M;j++){ const o = j*M, ar = Pr[o+c0], ai = Pi[o+c0], br = Pr[o+c1], bi = Pi[o+c1]; Pr[o+c0] = ar*K[0] + ai*K[1] + br*K[2] + bi*K[3]; Pi[o+c0] = ai*K[0] - ar*K[1] + bi*K[2] - br*K[3]; Pr[o+c1] = ar*K[4] + ai*K[5] + br*K[6] + bi*K[7]; Pi[o+c1] = ai*K[4] - ar*K[5] + bi*K[6] - br*K[7]; } }
function scaleBall(E, i, f){ const M = E.M; for(let q=0;q<2;q++){ const r = (2*i+q)*M; for(let j=0;j<M;j++){ E.Pr[r+j] *= f; E.Pi[r+j] *= f; } } for(let q=0;q<2;q++){ const c = 2*i+q; for(let j=0;j<M;j++){ E.Pr[j*M+c] *= f; E.Pi[j*M+c] *= f; } } }
/* the sea's spin on ball i: [2 Re C10, 2 Im C10, C00 - C11] */
function spin(Pr, Pi, M, i){ const a = 2*i, b = a + 1; return [2*Pr[b*M+a], 2*Pi[b*M+a], Pr[a*M+a] - Pr[b*M+b]]; }
const cross = (u, v) => [u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0]];
function restFor(FL, MM, W, clocks){ if(clocks !== 'dilation') return; W.balls.forEach(b => b.rate = 1/Math.cosh(b.r)); let seed = 11; const rnd = () => (seed = (seed*16807) % 2147483647)/2147483647 - 0.5;
  W.d = W.balls.map(b => { const v = [0.2*rnd(), 0.2*rnd(), 1 + 0.2*rnd()], m = Math.hypot(...v); return v.map(x => x/m*W.opts.omega*b.rate/2); }); const R = MM.restState(W, { iters:60000, eta:0.08, withSea:false, tol:1e-12 }); W.d = R.d; W.dRest = R.d.map(v => v.slice()); }
/* the one-step map of the light, the balls' own clocks left out: layout as SEA-DUMP-01 */
function stepMap(FL, W){ const N = W.N, S = FL.initState(W, {}); let M = 2*N; const off = [], segs = [], segLink = []; W.links.forEach((l, li) => l.segs.forEach(sg => { off.push([M, M + 2*sg.n]); M += 4*sg.n; segs.push(sg); segLink.push(li); }));
  const rows = [], cols = [], vr = [], vi = [];
  for(let k=0;k<M;k++){ S.psi.forEach(p => p.fill(0)); segs.forEach(sg => { sg.f.fill(0); sg.b.fill(0); sg.head = 0; }); S.d = W.balls.map(() => [0, 0, 1e-13]);
    if(k < 2*N) S.psi[k >> 1][2*(k & 1)] = 1; else for(let q=0;q<segs.length;q++){ const sg = segs[q], of = off[q][0], ob = off[q][1]; if(k >= of && k < of + 2*sg.n){ sg.f[4*((k-of) >> 1) + 2*((k-of) & 1)] = 1; break; } if(k >= ob && k < ob + 2*sg.n){ sg.b[4*((k-ob) >> 1) + 2*((k-ob) & 1)] = 1; break; } }
    FL.step(W, S);
    for(let i=0;i<N;i++) for(let c=0;c<2;c++){ const re = S.psi[i][2*c], im = S.psi[i][2*c+1]; if(Math.abs(re) > 1e-15 || Math.abs(im) > 1e-15){ rows.push(2*i+c); cols.push(k); vr.push(re); vi.push(im); } }
    for(let q=0;q<segs.length;q++){ const sg = segs[q], of = off[q][0], ob = off[q][1]; for(let j=0;j<sg.n;j++){ const s = (sg.head + j) % sg.n; for(let c=0;c<2;c++){ let re = sg.f[4*s+2*c], im = sg.f[4*s+2*c+1]; if(Math.abs(re) > 1e-15 || Math.abs(im) > 1e-15){ rows.push(of+2*j+c); cols.push(k); vr.push(re); vi.push(im); }
          re = sg.b[4*s+2*c]; im = sg.b[4*s+2*c+1]; if(Math.abs(re) > 1e-15 || Math.abs(im) > 1e-15){ rows.push(ob+2*j+c); cols.push(k); vr.push(re); vi.push(im); } } } } }
  return { M, off, segs, segLink, rows, cols, vr, vi }; }
/* o: { N, z, clocks:'z'|'equal'|'dilation', h, machine:'tied'|'untied'|'atonce', ends:'sealed'|'leak'|'container', feed:'kick'|'kicks_in'|'kicks_out'|'squeeze_in'|'squeeze_out'|'none', push:bool, rest:{M, tri:Float32Array} or null,
   live:bool (rates, spacing and faces follow the sea: rate_i = (2/ω)|d_i + κ(s_i − s_i,rest)|, z_i = rate_A/rate_i, Γ = tanh(r/2) at every face, sign at each link sgn(d_i·R_ij d_j); false = the fixed rates of the sweep),
   heat: squeeze amplitude (0.1 as in the sweep), heatOn:'balls' (all clock rates, as in the sweep) | 'links' (only the port angle where each link meets its ball: the layer round the pocket; the sine is sampled at 12 phases a period, so this heat is a staircase) } */
function make(FL, MM, o){ const W = FL.makeWorld({ N:o.N, z:o.z, h:o.h, push:'off', torque:0, clocks:o.clocks === 'equal' ? 'equal' : 'z' }); restFor(FL, MM, W, o.clocks);
  const N = W.N, h = o.h, drest = W.dRest.map(v => v.slice()), E = { o, W, N, h, drest, d:drest.map(v => v.slice()), t:0, steps:0, omega:W.opts.omega, ok:true, why:'' };
  E.far = N === 3 ? 2 : 3; E.cross = W.links.filter(l => l.i === 0 && l.j === E.far)[0].d;
  if(o.machine === 'atonce'){ const M = 2*N, H0 = MM.denseH(W, W.balls.map(() => [0,0,0])); E.M = M; E.H0 = H0;
    if(o.ends === 'container'){ E.ok = false; E.why = 'The all-at-once way has no stretches, so it has no bigger container.'; }
    E.Pr = new Float64Array(M*M); E.Pi = new Float64Array(M*M); const ev = eigA(MM, E, drest), gp = []; for(let k=0;k<M-1;k++) gp.push(ev.vals[ev.ord[k+1]] - ev.vals[ev.ord[k]]); let kf = N; for(const c of [N-1, N, N+1]) if(gp[c-1] > gp[kf-1]) kf = c;
    for(let n=0;n<kf;n++){ const v = ev.vecs[ev.ord[n]]; for(let i=0;i<M;i++) for(let j=0;j<M;j++){ E.Pr[i*M+j] += v[0][i]*v[0][j] + v[1][i]*v[1][j]; E.Pi[i*M+j] += v[1][i]*v[0][j] - v[0][i]*v[1][j]; } } E.rank = kf; E.margin = gp[kf-1]; }
  else { const saved = W.links.map(l => l.marks.map(m => m.rho)); W.links.forEach(l => l.marks.forEach(m => { m.rho = 0; })); const sm = stepMap(FL, W); W.links.forEach((l, k) => l.marks.forEach((m, q) => { m.rho = saved[k][q]; }));
    /* the faces, taken out of the transport: face q of link l acts on the forward sample that has just entered segment q+1 and the backward sample that has just entered segment q */
    E.faces = []; W.links.forEach((l, li) => { const qs = []; sm.segLink.forEach((x, q) => { if(x === li) qs.push(q); }); l.marks.forEach((m, k) => { const sA = sm.segs[qs[k+1]], sB = sm.segs[qs[k]]; const pa = W.balls[l.i].p, pb = W.balls[l.j].p, ca = Math.sinh(l.d - m.s)/Math.sinh(l.d), cb = Math.sinh(m.s)/Math.sinh(l.d), x = pa.map((v, q) => ca*v + cb*pb[q]), dA = Math.acosh(Math.max(1, MM.mink(x, W.balls[0].p)));
      E.faces.push({ li, k, kind:m.kind, rho0:m.rho, rho:m.rho, a:sm.off[qs[k+1]][0] + 2*(sA.n - 1), b:sm.off[qs[k]][1] + 2*(sB.n - 1), U:l.U, nI:Math.round(m.s/h), nJ:Math.round((l.d - m.s)/h), nA:Math.round(dA/h) }); }); });
    E.n0 = W.balls.map((b, i) => i ? Math.round(W.links.filter(l => l.i === 0 && l.j === i)[0].d/h) : 0);
    const M0 = sm.M, arm = []; for(let i=1;i<N;i++) arm.push(i); const nc = o.ends === 'container' ? Math.round(2.0/h) : 0, M = M0 + arm.length*4*nc; E.M = M; E.M0 = M0; E.sm = sm; E.nc = nc; E.arm = arm;
    E.T = csr(M, sm.rows.concat(Array.from({length:M - M0}, (_, k) => M0 + k)), sm.cols.concat(Array.from({length:M - M0}, (_, k) => M0 + k)), sm.vr.concat(new Array(M - M0).fill(1)), sm.vi.concat(new Array(M - M0).fill(0)));
    if(nc){ const th = Math.sqrt(W.opts.gamma*h), c = Math.cos(th), s = Math.sin(th), rows = [], cols = [], vr = [], used = new Uint8Array(M); const put = (r, cc, v) => { rows.push(r); cols.push(cc); vr.push(v); used[r] = 1; };
      arm.forEach((i, a) => { const f0 = M0 + a*4*nc, b0 = f0 + 2*nc; for(let q=0;q<2;q++){ const p = 2*i + q, fo = f0 + q, bo = b0 + q, fn = f0 + 2*(nc-1) + q, bn = b0 + 2*(nc-1) + q;
          for(let j=1;j<nc;j++){ put(f0 + 2*(j-1) + q, f0 + 2*j + q, 1); put(b0 + 2*(j-1) + q, b0 + 2*j + q, 1); } put(fn, p, s); put(fn, bo, c); put(p, p, c); put(p, bo, -s); put(bn, fo, -1); } });
      for(let r=0;r<M;r++) if(!used[r]){ rows.push(r); cols.push(r); vr.push(1); } E.E = csr(M, rows, cols, vr, new Array(rows.length).fill(0)); }
    E.Pr = new Float64Array(M*M); E.Pi = new Float64Array(M*M);
    if(o.machine === 'tied'){ if(!o.rest || o.rest.M !== M){ E.ok = false; E.why = 'No stored tied rest sea for this layout. It is stored for 3, 4 and 7 balls at step ratios 3, 5, 7 with sealed or open ends, and for 3 balls in the bigger container. The other two ways run for any layout.'; }
      else { const tri = o.rest.tri; let k = 0; for(let i=0;i<M;i++) for(let j=i;j<M;j++){ const re = tri[k++], im = tri[k++]; E.Pr[i*M+j] = re; E.Pi[i*M+j] = im; E.Pr[j*M+i] = re; E.Pi[j*M+i] = -im; } E.rank = o.rest.rank; E.margin = o.rest.margin; } }
    if(o.machine === 'untied' || !E.ok){ if(o.machine === 'untied'){ for(let i=0;i<N;i++){ const d = drest[i], m = Math.hypot(...d), u = d.map(x => x/m), a = 2*i, b = a + 1; E.Pr[a*M+a] = (1 - u[2])/2; E.Pr[b*M+b] = (1 + u[2])/2; E.Pr[a*M+b] = -u[0]/2; E.Pi[a*M+b] = u[1]/2; E.Pr[b*M+a] = -u[0]/2; E.Pi[b*M+a] = -u[1]/2; } E.rank = N; } }
    E.Ar = new Float64Array(M*M); E.Ai = new Float64Array(M*M); E.Br = new Float64Array(M*M); E.Bi = new Float64Array(M*M); }
  const M = E.M; E.Rr = Float64Array.from(E.Pr); E.Ri = Float64Array.from(E.Pi); E.srest = []; for(let i=0;i<N;i++) E.srest.push(spin(E.Pr, E.Pi, M, i));
  let tr = 0; for(let i=0;i<M;i++) tr += E.Pr[i*M+i]; E.tr0 = tr; E.left = 0;
  /* histories of each ball's rate and field, so a face sees each ball's clock as it was one light-time ago (the retarded reading, as the delayed push keeps them) */
  { let HL = 2; (E.faces || []).forEach(f => { HL = Math.max(HL, f.nI, f.nJ, f.nA); }); (E.n0 || []).forEach(n => { HL = Math.max(HL, n); }); E.HL = HL + 2; E.hh = 0; E.rateH = []; E.dH = []; for(let i=0;i<N;i++){ const r0 = Math.hypot(...drest[i])*2/W.opts.omega; E.rateH.push(new Float64Array(E.HL).fill(r0)); const dh = new Float64Array(3*E.HL); for(let t=0;t<E.HL;t++) dh.set(drest[i], 3*t); E.dH.push(dh); } }
  const u = drest[0].map(x => x/Math.hypot(...drest[0])), a = Math.abs(u[0]) < 0.9 ? [1,0,0] : [0,1,0], n = cross(u, a), nm = Math.hypot(...n); E.kn = n.map(x => x/nm);
  E.heat = o.heat === undefined ? 0.1 : o.heat; E.heatOn = o.heatOn || 'balls';
  if(E.heatOn === 'links' && E.sm && o.feed.indexOf('squeeze') === 0 && E.heat > 0){ const g0 = W.opts.gamma, M0 = E.M0, ident = k => ({ rows:Array.from({length:M - M0}, (_, q) => M0 + q), cols:Array.from({length:M - M0}, (_, q) => M0 + q) }); E.Tset = [];
    for(let k=0;k<12;k++){ const th = Math.sqrt(g0*h)*(1 + E.heat*Math.sin(2*Math.PI*k/12)); W.opts.gamma = th*th/h; const sm = stepMap(FL, W), id = ident(); E.Tset.push(csr(M, sm.rows.concat(id.rows), sm.cols.concat(id.cols), sm.vr.concat(new Array(M - M0).fill(1)), sm.vi.concat(new Array(M - M0).fill(0)))); } W.opts.gamma = g0; }
  E.Tk = Math.PI*(o.feed === 'kicks_out' ? GOLD : 1); E.Om = 2*E.omega*(o.feed === 'squeeze_out' ? GOLD : 1); E.nextk = E.Tk; E.thl = Math.sqrt(0.1*h);
  if(o.feed === 'kick' && E.ok) kick(E, true); return E; }
function eigA(MM, E, d){ const M = E.M, Hr = E.H0.Hr.map(r => Float64Array.from(r)), Hi = E.H0.Hi.map(r => Float64Array.from(r)); for(let i=0;i<E.N;i++){ const a = 2*i, b = a + 1, v = d[i]; Hr[a][a] += v[2]; Hr[b][b] -= v[2]; Hr[a][b] += v[0]; Hi[a][b] -= v[1]; Hr[b][a] += v[0]; Hi[b][a] += v[1]; }
  const ev = MM.eigh(Hr, Hi); ev.ord = ev.vals.map((x, k) => k).sort((p, q) => ev.vals[p] - ev.vals[q]); return ev; }
/* a quarter turn (big) or a small turn (0.05) of ball A's block about an axis across its field */
function kick(E, big){ local(E, 0, turn2(E.kn, big ? Math.PI/4 : 0.05)); }
/* live rates (HYPOTHESIS, rate is weight): the sea's spin on a ball adds to its field with the push's own kappa; rate_i = (2/omega)|d_i + kappa (s_i - s_i,rest)|.
   Every comparison of two clocks is retarded: a face sees ball i's rate as it was s/h steps ago (s its distance to the face), and the centre's as it was one light-time from the centre ago. */
function liveRates(E){ const N = E.N, W = E.W, kap = W.opts.kappa, M = E.M, om = W.opts.omega, out = { rate:[], z:[], r:[], sigma:{} };
  for(let i=0;i<N;i++){ const d = E.d[i], s = E.o.live ? spin(E.Pr, E.Pi, M, i) : E.srest[i], v = [0,1,2].map(a => d[a] + kap*(s[a] - E.srest[i][a])); out.rate.push(Math.hypot(v[0], v[1], v[2])*2/om); }
  if(E.rateH){ const HL = E.HL; E.hh = (E.hh + 1) % HL; for(let i=0;i<N;i++){ E.rateH[i][E.hh] = out.rate[i]; E.dH[i].set(E.d[i], 3*E.hh); } }
  const past = (i, n) => E.rateH ? E.rateH[i][((E.hh - n) % E.HL + E.HL) % E.HL] : out.rate[i], pastD = (i, n) => { if(!E.dH) return E.d[i]; const o = 3*(((E.hh - n) % E.HL + E.HL) % E.HL); return [E.dH[i][o], E.dH[i][o+1], E.dH[i][o+2]]; };
  for(let i=0;i<N;i++){ const z = E.o.live ? past(0, E.n0 ? E.n0[i] : 0)/out.rate[i] : W.opts.omega/2/Math.hypot(...E.drest[i])*(i ? 1 : 1)/(W.opts.omega/2/Math.hypot(...E.drest[0])); out.z.push(z); out.r.push(Math.log(z)); }
  out.past = past; out.pastD = pastD; return out; }
function liveFaces(E, L){ const W = E.W, kg = W.opts.kgap, sg = -1; for(const f of E.faces){ const l = W.links[f.li]; if(!E.o.live){ f.rho = f.rho0; f.sigma = 1; continue; }
    const di = L.pastD(l.i, f.nI), dj = L.pastD(l.j, f.nJ), Rd = [0,1,2].map(a => l.R[a][0]*dj[0] + l.R[a][1]*dj[1] + l.R[a][2]*dj[2]), dot = di[0]*Rd[0] + di[1]*Rd[1] + di[2]*Rd[2], sig = dot < 0 ? -1 : 1, rA = L.past(0, f.nA); f.sigma = sig;
    if(l.i === 0) f.rho = sig*Math.tanh(Math.log(rA/L.past(l.j, f.nJ))/2);
    else { const ra = Math.log(rA/L.past(l.i, f.nI)), rb = Math.log(rA/L.past(l.j, f.nJ)); if(f.kind === 'gap'){ const g = Math.sinh(ra/2)*Math.sinh(rb/2); f.rho = Math.tanh(kg*(g > 1 ? Math.acosh(g) : 0)); } else f.rho = (f.k === 0 ? sig*sg : -sig*sg)*Math.tanh((f.k === 0 ? ra : rb)/2); } }
  L.sigma = {}; for(const f of E.faces) L.sigma[f.li] = f.sigma; }
/* P <- F P F^dagger for one face: F = [[tau I, -rho U], [rho U^dagger, tau I]] on (forward a, backward b), U the link's SU(2) */
function applyFace(E, f){ const M = E.M, Pr = E.Pr, Pi = E.Pi, rho = f.rho, tau = Math.sqrt(1 - rho*rho), U = f.U, idx = [f.a, f.a+1, f.b, f.b+1], Fr = [], Fi = [];
  for(let r=0;r<4;r++){ Fr.push([0,0,0,0]); Fi.push([0,0,0,0]); } for(let r=0;r<2;r++){ Fr[r][r] = tau; Fr[2+r][2+r] = tau; for(let c=0;c<2;c++){ const u = U[2*r+c]; Fr[r][2+c] = -rho*u[0]; Fi[r][2+c] = -rho*u[1]; const v = U[2*c+r]; Fr[2+r][c] = rho*v[0]; Fi[2+r][c] = -rho*v[1]; } }
  const tr = [0,0,0,0], ti = [0,0,0,0];
  for(let j=0;j<M;j++){ for(let r=0;r<4;r++){ let sr = 0, si = 0; for(let c=0;c<4;c++){ const pr = Pr[idx[c]*M+j], pi = Pi[idx[c]*M+j]; sr += Fr[r][c]*pr - Fi[r][c]*pi; si += Fr[r][c]*pi + Fi[r][c]*pr; } tr[r] = sr; ti[r] = si; } for(let r=0;r<4;r++){ Pr[idx[r]*M+j] = tr[r]; Pi[idx[r]*M+j] = ti[r]; } }
  for(let i=0;i<M;i++){ for(let r=0;r<4;r++){ let sr = 0, si = 0; for(let c=0;c<4;c++){ const pr = Pr[i*M+idx[c]], pi = Pi[i*M+idx[c]]; sr += pr*Fr[r][c] + pi*Fi[r][c]; si += pi*Fr[r][c] - pr*Fi[r][c]; } tr[r] = sr; ti[r] = si; } for(let r=0;r<4;r++){ Pr[i*M+idx[r]] = tr[r]; Pi[i*M+idx[r]] = ti[r]; } } }
function step(E){ if(!E.ok) return; const o = E.o, M = E.M, N = E.N, h = E.h, sc = (o.feed.indexOf('squeeze') === 0 && E.heatOn !== 'links') ? 1 + E.heat*Math.sin(E.Om*E.t) : 1;
  if(E.Tset){ const ph = (E.Om*E.t/(2*Math.PI)) % 1; E.T = E.Tset[Math.floor(ph*12) % 12]; }
  if(o.machine === 'atonce'){ E.L = liveRates(E); const ev = eigA(E.MM, E, E.d.map(v => v.map(x => x*sc))), Ur = new Float64Array(M*M), Ui = new Float64Array(M*M);
    for(let n=0;n<M;n++){ const v = ev.vecs[n], c = Math.cos(ev.vals[n]*h), s = -Math.sin(ev.vals[n]*h); for(let i=0;i<M;i++){ const ar = v[0][i]*c - v[1][i]*s, ai = v[0][i]*s + v[1][i]*c; for(let j=0;j<M;j++){ Ur[i*M+j] += ar*v[0][j] + ai*v[1][j]; Ui[i*M+j] += ai*v[0][j] - ar*v[1][j]; } } }
    const Ar = new Float64Array(M*M), Ai = new Float64Array(M*M), Br = new Float64Array(M*M), Bi = new Float64Array(M*M); mm(Ur, Ui, E.Pr, E.Pi, Ar, Ai, M); dagger(Ur, Ui, Br, Bi, M); mm(Ar, Ai, Br, Bi, E.Pr, E.Pi, M); }
  else { const conj = S => { mulRows(S, E.Pr, E.Pi, E.Ar, E.Ai); dagger(E.Ar, E.Ai, E.Br, E.Bi, M); mulRows(S, E.Br, E.Bi, E.Ar, E.Ai); dagger(E.Ar, E.Ai, E.Pr, E.Pi, M); };
    conj(E.T); E.L = liveRates(E); liveFaces(E, E.L); for(const f of E.faces) applyFace(E, f); if(E.E) conj(E.E);
    for(let i=0;i<N;i++) local(E, i, rot2(E.d[i].map(x => x*sc), h)); }
  if(o.ends === 'leak'){ let b = 0, a = 0; for(let i=0;i<M;i++) b += E.Pr[i*M+i]; for(let i=1;i<N;i++) scaleBall(E, i, Math.cos(E.thl)); for(let i=0;i<M;i++) a += E.Pr[i*M+i]; E.left += b - a; }
  if(o.push){ const k2 = 2*E.W.opts.kappa, G = E.d.map(() => [0,0,0]); for(const l of E.W.links){ const R = l.R, dj = E.drest[l.j], di = E.drest[l.i]; for(let a=0;a<3;a++){ let s1 = 0, s2 = 0; for(let b=0;b<3;b++){ s1 += R[a][b]*dj[b]; s2 += R[b][a]*di[b]; } G[l.i][a] += k2*(E.d[l.i][a] - s1); G[l.j][a] += k2*(E.d[l.j][a] - s2); } }
    for(let i=0;i<N;i++){ const s = spin(E.Pr, E.Pi, M, i), g = [0,1,2].map(a => G[i][a] + s[a] - E.srest[i][a]), gm = Math.hypot(...g); if(gm < 1e-300) continue; const u = g.map(x => x/gm), an = gm*h, ca = Math.cos(an), sa = Math.sin(an), di = E.d[i], ud = u[0]*di[0]+u[1]*di[1]+u[2]*di[2], cx = cross(u, di); E.d[i] = [0,1,2].map(a => di[a]*ca + cx[a]*sa + u[a]*ud*(1-ca)); } }
  if(o.feed.indexOf('kicks') === 0 && E.t + h >= E.nextk){ kick(E, false); E.nextk += E.Tk; }
  E.t += h; E.steps++; }
function mm(Ar, Ai, Br, Bi, Cr, Ci, M){ Cr.fill(0); Ci.fill(0); for(let i=0;i<M;i++) for(let k=0;k<M;k++){ const ar = Ar[i*M+k], ai = Ai[i*M+k]; if(ar === 0 && ai === 0) continue; for(let j=0;j<M;j++){ Cr[i*M+j] += ar*Br[k*M+j] - ai*Bi[k*M+j]; Ci[i*M+j] += ar*Bi[k*M+j] + ai*Br[k*M+j]; } } }
/* readings */
function read(E){ const M = E.M, N = E.N, out = { t:E.t, spin:[], fill:[], turn:[] }; let tr = 0, lift = 0; for(let i=0;i<M;i++) tr += E.Pr[i*M+i]; for(let k=0;k<M*M;k++) lift += E.Rr[k]*E.Pr[k] + E.Ri[k]*E.Pi[k];
  for(let i=0;i<N;i++){ const s = spin(E.Pr, E.Pi, M, i); out.spin.push([0,1,2].map(a => s[a] - E.srest[i][a])); out.fill.push(E.Pr[2*i*M+2*i] + E.Pr[(2*i+1)*M+2*i+1]); const a = E.d[i], b = E.drest[i]; out.turn.push(Math.acos(Math.max(-1, Math.min(1, (a[0]*b[0]+a[1]*b[1]+a[2]*b[2])/(Math.hypot(...a)*Math.hypot(...b)))))); }
  out.trace = tr; out.left = E.left; out.lifted = tr - lift; out.L = E.L || liveRates(E); out.faces = (E.faces || []).map(f => ({ li:f.li, k:f.k, kind:f.kind, rho:f.rho, sigma:f.sigma })); out.leak = []; for(let i=0;i<N;i++){ let q = 0; for(let p=0;p<2;p++) for(let r=0;r<2;r++){ const k = (2*i+p)*M + 2*i+r; q += (E.Pr[k]-E.Rr[k])**2 + (E.Pi[k]-E.Ri[k])**2; } out.leak.push(Math.sqrt(q)); } const f = E.far, blk = (i, j) => { let s = 0; for(let p=0;p<2;p++) for(let q=0;q<2;q++){ const k = (2*i+p)*M + 2*j+q; s += E.Pr[k]*E.Pr[k] + E.Pi[k]*E.Pi[k]; } return s; };
  let df = 0; for(let p=0;p<2;p++) for(let q=0;q<2;q++){ const k = (2*f+p)*M + 2*f+q; df += (E.Pr[k]-E.Rr[k])**2 + (E.Pi[k]-E.Ri[k])**2; } out.farChange = Math.sqrt(df); out.tie = []; for(let i=0;i<N;i++) for(let j=i+1;j<N;j++) out.tie.push([i, j, blk(i, j)]); return out; }
/* how far the sea's filling along a link stands from rest, forward and backward movers, in MP bins from ball i to ball j */
function linkChange(E, li, MP){ const F = new Float64Array(MP), B = new Float64Array(MP); if(!E.sm) return { F, B }; const M = E.M, l = E.W.links[li];
  E.sm.segs.forEach((sg, q) => { if(E.sm.segLink[q] !== li) return; const of = E.sm.off[q][0], ob = E.sm.off[q][1]; for(let j=0;j<sg.n;j++){ let df = 0, db = 0; for(let c=0;c<2;c++){ const a = of + 2*j + c, b = ob + 2*j + c; df += E.Pr[a*M+a] - E.Rr[a*M+a]; db += E.Pr[b*M+b] - E.Rr[b*M+b]; }
      const k = sg.n - 1 - j, sf = sg.s0 + (k + 0.5)*sg.len/sg.n, sb = sg.s0 + sg.len - (k + 0.5)*sg.len/sg.n; F[Math.min(MP-1, Math.floor(sf/l.d*MP))] += df; B[Math.min(MP-1, Math.floor(sb/l.d*MP))] += db; } }); return { F, B }; }
/* the filling of a link's gap, in MP bins from ball i to ball j: fill = occupation / capacity (both streams, both components), with the rest filling beside it */
function linkFill(E, li, MP){ const fill = new Float64Array(MP), rest = new Float64Array(MP), cap = new Float64Array(MP); if(!E.sm) return { fill, rest, cap }; const M = E.M, l = E.W.links[li];
  E.sm.segs.forEach((sg, q) => { if(E.sm.segLink[q] !== li) return; const of = E.sm.off[q][0], ob = E.sm.off[q][1]; for(let j=0;j<sg.n;j++){ const k = sg.n - 1 - j, sf = sg.s0 + (k + 0.5)*sg.len/sg.n, sb = sg.s0 + sg.len - (k + 0.5)*sg.len/sg.n, bf = Math.min(MP-1, Math.floor(sf/l.d*MP)), bb = Math.min(MP-1, Math.floor(sb/l.d*MP));
      for(let c=0;c<2;c++){ const a = of + 2*j + c, b = ob + 2*j + c; fill[bf] += E.Pr[a*M+a]; rest[bf] += E.Rr[a*M+a]; cap[bf] += 1; fill[bb] += E.Pr[b*M+b]; rest[bb] += E.Rr[b*M+b]; cap[bb] += 1; } } });
  for(let m=0;m<MP;m++) if(cap[m] > 0){ fill[m] /= cap[m]; rest[m] /= cap[m]; } return { fill, rest, cap }; }
return { linkFill, liveRates, make:(FL, MM, o) => { const E = make(FL, MM, o); E.MM = MM; return E; }, step, kick, read, linkChange, GOLD };
})();
if(typeof module !== 'undefined') module.exports = SEA;
