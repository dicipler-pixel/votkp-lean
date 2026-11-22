/* SCRIPT: SEA-MATH-V1
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
/* o: { N, z, clocks:'z'|'equal'|'dilation', h, machine:'tied'|'untied'|'atonce', ends:'sealed'|'leak'|'container', feed:'kick'|'kicks_in'|'kicks_out'|'squeeze_in'|'squeeze_out'|'none', push:bool, rest:{M, tri:Float32Array} or null } */
function make(FL, MM, o){ const W = FL.makeWorld({ N:o.N, z:o.z, h:o.h, push:'off', torque:0, clocks:o.clocks === 'equal' ? 'equal' : 'z' }); restFor(FL, MM, W, o.clocks);
  const N = W.N, h = o.h, drest = W.dRest.map(v => v.slice()), E = { o, W, N, h, drest, d:drest.map(v => v.slice()), t:0, steps:0, omega:W.opts.omega, ok:true, why:'' };
  E.far = N === 3 ? 2 : 3; E.cross = W.links.filter(l => l.i === 0 && l.j === E.far)[0].d;
  if(o.machine === 'atonce'){ const M = 2*N, H0 = MM.denseH(W, W.balls.map(() => [0,0,0])); E.M = M; E.H0 = H0;
    if(o.ends === 'container'){ E.ok = false; E.why = 'The all-at-once way has no stretches, so it has no bigger container.'; }
    E.Pr = new Float64Array(M*M); E.Pi = new Float64Array(M*M); const ev = eigA(MM, E, drest), gp = []; for(let k=0;k<M-1;k++) gp.push(ev.vals[ev.ord[k+1]] - ev.vals[ev.ord[k]]); let kf = N; for(const c of [N-1, N, N+1]) if(gp[c-1] > gp[kf-1]) kf = c;
    for(let n=0;n<kf;n++){ const v = ev.vecs[ev.ord[n]]; for(let i=0;i<M;i++) for(let j=0;j<M;j++){ E.Pr[i*M+j] += v[0][i]*v[0][j] + v[1][i]*v[1][j]; E.Pi[i*M+j] += v[1][i]*v[0][j] - v[0][i]*v[1][j]; } } E.rank = kf; E.margin = gp[kf-1]; }
  else { const sm = stepMap(FL, W), M0 = sm.M, arm = []; for(let i=1;i<N;i++) arm.push(i); const nc = o.ends === 'container' ? Math.round(2.0/h) : 0, M = M0 + arm.length*4*nc; E.M = M; E.M0 = M0; E.sm = sm; E.nc = nc; E.arm = arm;
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
  const u = drest[0].map(x => x/Math.hypot(...drest[0])), a = Math.abs(u[0]) < 0.9 ? [1,0,0] : [0,1,0], n = cross(u, a), nm = Math.hypot(...n); E.kn = n.map(x => x/nm);
  E.Tk = Math.PI*(o.feed === 'kicks_out' ? GOLD : 1); E.Om = 2*E.omega*(o.feed === 'squeeze_out' ? GOLD : 1); E.nextk = E.Tk; E.thl = Math.sqrt(0.1*h);
  if(o.feed === 'kick' && E.ok) kick(E, true); return E; }
function eigA(MM, E, d){ const M = E.M, Hr = E.H0.Hr.map(r => Float64Array.from(r)), Hi = E.H0.Hi.map(r => Float64Array.from(r)); for(let i=0;i<E.N;i++){ const a = 2*i, b = a + 1, v = d[i]; Hr[a][a] += v[2]; Hr[b][b] -= v[2]; Hr[a][b] += v[0]; Hi[a][b] -= v[1]; Hr[b][a] += v[0]; Hi[b][a] += v[1]; }
  const ev = MM.eigh(Hr, Hi); ev.ord = ev.vals.map((x, k) => k).sort((p, q) => ev.vals[p] - ev.vals[q]); return ev; }
/* a quarter turn (big) or a small turn (0.05) of ball A's block about an axis across its field */
function kick(E, big){ local(E, 0, turn2(E.kn, big ? Math.PI/4 : 0.05)); }
function step(E){ if(!E.ok) return; const o = E.o, M = E.M, N = E.N, h = E.h, sc = o.feed.indexOf('squeeze') === 0 ? 1 + 0.1*Math.sin(E.Om*E.t) : 1;
  if(o.machine === 'atonce'){ const ev = eigA(E.MM, E, E.d.map(v => v.map(x => x*sc))), Ur = new Float64Array(M*M), Ui = new Float64Array(M*M);
    for(let n=0;n<M;n++){ const v = ev.vecs[n], c = Math.cos(ev.vals[n]*h), s = -Math.sin(ev.vals[n]*h); for(let i=0;i<M;i++){ const ar = v[0][i]*c - v[1][i]*s, ai = v[0][i]*s + v[1][i]*c; for(let j=0;j<M;j++){ Ur[i*M+j] += ar*v[0][j] + ai*v[1][j]; Ui[i*M+j] += ai*v[0][j] - ar*v[1][j]; } } }
    const Ar = new Float64Array(M*M), Ai = new Float64Array(M*M), Br = new Float64Array(M*M), Bi = new Float64Array(M*M); mm(Ur, Ui, E.Pr, E.Pi, Ar, Ai, M); dagger(Ur, Ui, Br, Bi, M); mm(Ar, Ai, Br, Bi, E.Pr, E.Pi, M); }
  else { mulRows(E.T, E.Pr, E.Pi, E.Ar, E.Ai); let Xr = E.Ar, Xi = E.Ai, Yr = E.Br, Yi = E.Bi; if(E.E){ mulRows(E.E, Xr, Xi, Yr, Yi); [Xr, Yr] = [Yr, Xr]; [Xi, Yi] = [Yi, Xi]; }
    dagger(Xr, Xi, Yr, Yi, M); mulRows(E.T, Yr, Yi, Xr, Xi); if(E.E){ mulRows(E.E, Xr, Xi, Yr, Yi); [Xr, Yr] = [Yr, Xr]; [Xi, Yi] = [Yi, Xi]; } dagger(Xr, Xi, E.Pr, E.Pi, M);
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
  out.trace = tr; out.left = E.left; out.lifted = tr - lift; const f = E.far, blk = (i, j) => { let s = 0; for(let p=0;p<2;p++) for(let q=0;q<2;q++){ const k = (2*i+p)*M + 2*j+q; s += E.Pr[k]*E.Pr[k] + E.Pi[k]*E.Pi[k]; } return s; };
  let df = 0; for(let p=0;p<2;p++) for(let q=0;q<2;q++){ const k = (2*f+p)*M + 2*f+q; df += (E.Pr[k]-E.Rr[k])**2 + (E.Pi[k]-E.Ri[k])**2; } out.farChange = Math.sqrt(df); out.tie = []; for(let i=0;i<N;i++) for(let j=i+1;j<N;j++) out.tie.push([i, j, blk(i, j)]); return out; }
/* how far the sea's filling along a link stands from rest, forward and backward movers, in MP bins from ball i to ball j */
function linkChange(E, li, MP){ const F = new Float64Array(MP), B = new Float64Array(MP); if(!E.sm) return { F, B }; const M = E.M, l = E.W.links[li];
  E.sm.segs.forEach((sg, q) => { if(E.sm.segLink[q] !== li) return; const of = E.sm.off[q][0], ob = E.sm.off[q][1]; for(let j=0;j<sg.n;j++){ let df = 0, db = 0; for(let c=0;c<2;c++){ const a = of + 2*j + c, b = ob + 2*j + c; df += E.Pr[a*M+a] - E.Rr[a*M+a]; db += E.Pr[b*M+b] - E.Rr[b*M+b]; }
      const k = sg.n - 1 - j, sf = sg.s0 + (k + 0.5)*sg.len/sg.n, sb = sg.s0 + sg.len - (k + 0.5)*sg.len/sg.n; F[Math.min(MP-1, Math.floor(sf/l.d*MP))] += df; B[Math.min(MP-1, Math.floor(sb/l.d*MP))] += db; } }); return { F, B }; }
return { make:(FL, MM, o) => { const E = make(FL, MM, o); E.MM = MM; return E; }, step, kick, read, linkChange, GOLD };
})();
if(typeof module !== 'undefined') module.exports = SEA;
