/* SCRIPT: HSB-MODEL-V1
   Hydrogen in the Space Between — the model. Jeromie Beasley. 17 Nov 2026. AI-assisted.
   Each ball is a hydrogen atom: one two-level site (its electron, field d_atom) resolved into a centre and six surface ports, the way the
   Light at the Hypersurface ball has six faces. The space between the atoms is a lattice of two-level field sites (field d_vac), the
   occupied background: every site is a real state in H. One operator does everything (MM-MATH-V1): H = D + A, with the peel step
   Γ = tanh(δ/2), c = c₀ sech(δ/2) on the surface links (VOTKP), the occupied ground projector at half filling (the Dirac sea, cut in the
   gap), a local SU(2) kick, exact evolution P(t) = e^{-iHt} P e^{iHt}. Light is the energy current 2 Im Tr(H_ij ρᴱ_ji), charge the
   occupation current 2 Im Tr(H_ij P_ji); the connection energy of a link is ‖D_i − U_ij D_j U_ij†‖² (Non-Normality Is Connection Energy);
   the weight between two sites is ‖P_ij‖²; an atom's offset is τ = ln det[(I − C) C⁻¹]. The travel time of a signal is not put in by
   hand: it comes from the sites between. Parallel or opposed electrons: the second atom's field along or against the first's. */
(function(root){
"use strict";
const MM = root.MM || (typeof require !== 'undefined' ? require('../mm/mm_math_v1.js') : null);
const z2 = () => [0,0];
function build(o){ o = Object.assign({ atoms:2, sep:4, contrast:2.4, spins:'opposed', faceZ:[3,5,7], c0:0.22, dvac:0.8, tilt:0.5, kick:1.1, source:0 }, o || {});
  const nA = o.atoms, nx = o.sep*(nA - 1) + 3, id = (x, y, z) => (x*3 + y)*3 + z, pos = [], body = [], d = [], links = [], atomsAt = [];
  for(let a=0;a<nA;a++) atomsAt.push(id(1 + a*o.sep, 1, 1));
  for(let x=0;x<nx;x++) for(let y=0;y<3;y++) for(let z=0;z<3;z++){ const i = id(x, y, z), b = atomsAt.indexOf(i); pos.push([(x - (nx-1)/2)*1.6, (y-1)*1.6, (z-1)*1.6]); body.push(b);
    if(b < 0) d.push([0, 0, o.dvac]); else { const ang = o.tilt + (o.spins === 'opposed' && (b % 2) ? Math.PI : 0), m = o.dvac*o.contrast; d.push([m*Math.sin(ang), 0, m*Math.cos(ang)]); } }
  const I3 = [[1,0,0],[0,1,0],[0,0,1]], U1 = [[1,0], z2(), z2(), [1,0]];
  for(let x=0;x<nx;x++) for(let y=0;y<3;y++) for(let z=0;z<3;z++){ const i = id(x, y, z);
    for(const [dx, dy, dz] of [[1,0,0],[0,1,0],[0,0,1]]){ if(x+dx >= nx || y+dy >= 3 || z+dz >= 3) continue; const j = id(x+dx, y+dy, z+dz), surface = body[i] >= 0 || body[j] >= 0, axis = dx ? 0 : dy ? 2 : 1;
      const delta = surface ? Math.log((o.extZ||o.faceZ)[axis]) : 0; links.push({ i, j, R:I3, U:U1, c:o.c0/Math.cosh(delta/2), Gam:Math.tanh(delta/2), d:delta, surface, axis, gap:false }); } }
  /* each atom: centre + six surface ports at the ball's own peel endpoints; the outside links land on the ports */
  const ports = [];
  for(let b=0;b<nA;b++){ const root_ = atomsAt[b], P = [];
    for(let axis=0;axis<3;axis++) for(const sign of [-1, 1]){ const physical = [0,2,1][axis], p = pos[root_].slice(), rad = 2.6*0.46*Math.tanh(Math.log(o.faceZ[axis])/2); p[physical] += sign*rad; const index = pos.length; pos.push(p); body.push(b); d.push(d[root_].slice()); P.push({ axis, sign, index });
      const delta = Math.log(o.faceZ[axis]); links.push({ i:root_, j:index, R:I3, U:U1, c:o.c0/Math.cosh(delta/2), Gam:Math.tanh(delta/2), d:delta, surface:false, internal:true, axis }); } ports.push(P); }
  for(const l of links){ if(!l.surface) continue; const root_ = atomsAt.includes(l.i) ? l.i : l.j, b = atomsAt.indexOf(root_), other = l.i === root_ ? l.j : l.i, physical = [0,2,1][l.axis], sign = pos[other][physical] > pos[root_][physical] ? 1 : -1, port = ports[b].find(p => p.axis === l.axis && p.sign === sign).index; if(l.i === root_) l.i = port; else l.j = port; }
  for(const l of links){ if(l.surface && l.axis === 0){ const pi = ports.flat().find(p => p.index === l.i || p.index === l.j); if(pi && pi.axis === 0){ const other = pi.index === l.i ? l.j : l.i; if(other % 9 === 4) l.gap = true; } } }
  const N = pos.length, nbr = Array.from({length:N}, () => []); links.forEach((l, k) => { nbr[l.i].push(k); nbr[l.j].push(k); });
  /* the gap row: the sites on the line between atom 0 and atom 1 (nothing drawn is made up: these are lattice sites) */
  const rowSites = []; for(let x=0;x<nx;x++) rowSites.push(id(x, 1, 1)); links.forEach((l, k) => { if(rowSites.includes(l.i) && rowSites.includes(l.j)) l.gap = true; });
  const W = { N, links, nbr, d, opts:{ kappa:0.25 } }, H = MM.denseH(W, d), E = MM.eigh(H.Hr, H.Hi), n = 2*N, k = N;
  /* connection energy per link, Non-Normality Is Connection Energy: ||D_i - U D_j U^dag||^2 with D = d.sigma; U = 1 here, so it is |d_i - d_j|^2 x 2 */
  const conn = links.map(l => { const a = d[l.i], b = d[l.j]; return 2*((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2); });
  const nnce = MM.nnceCheck(W, d);
  const M = { o, nx, N, n, k, pos, body, d, links, nbr, atomsAt, ports, rowSites, W, H, E, conn, nnce, gap:E.vals[k] - E.vals[k-1], Eground:E.vals.slice(0, k).reduce((s, v) => s + v, 0), t:0 };
  M.id = id; M.gapAtomSep = o.sep; prepare(M, o.kick, o.source); return M; }
/* the occupied sea after a local kick exp(-i angle sigma_y/2) on the source atom, expanded on the eigenbasis */
function prepare(M, angle, source){ const n = M.n, k = M.k, E = M.E, src = M.atomsAt[source || 0], a = 2*src, b = a + 1, c = Math.cos(angle/2), s = Math.sin(angle/2);
  const Qr = [], Qi = []; for(let j=0;j<k;j++){ const qr = Float64Array.from(E.vecs[j][0]), qi = Float64Array.from(E.vecs[j][1]); for(const q of [qr, qi]){ const u = q[a], v = q[b]; q[a] = c*u - s*v; q[b] = s*u + c*v; } Qr.push(qr); Qi.push(qi); }
  M.cr = []; M.ci = []; for(let j=0;j<k;j++){ const cr = new Float64Array(n), ci = new Float64Array(n); for(let m=0;m<n;m++){ const [vr, vi] = E.vecs[m]; let r = 0, im = 0; for(let x=0;x<n;x++){ r += vr[x]*Qr[j][x] + vi[x]*Qi[j][x]; im += vr[x]*Qi[j][x] - vi[x]*Qr[j][x]; } cr[m] = r; ci[m] = im; } M.cr.push(cr); M.ci.push(ci); }
  M.psr = Array.from({length:k}, () => new Float64Array(n)); M.psi = Array.from({length:k}, () => new Float64Array(n)); M.t = 0; at(M, 0);
  /* the ground sea's readings, for charge = occupation above the ground */
  const g = readFrom(M, E.vecs.slice(0, k).map(v => v[0]), E.vecs.slice(0, k).map(v => v[1])); M.ground = g; }
/* the occupied states at time t: psi_j(t) = sum_m c_jm e^{-i lam_m t} v_m */
function at(M, t){ const n = M.n, k = M.k, E = M.E, cs = new Float64Array(n), sn = new Float64Array(n); for(let m=0;m<n;m++){ cs[m] = Math.cos(E.vals[m]*t); sn[m] = -Math.sin(E.vals[m]*t); }
  for(let j=0;j<k;j++){ const pr = M.psr[j], pi = M.psi[j], cr = M.cr[j], ci = M.ci[j]; pr.fill(0); pi.fill(0); for(let m=0;m<n;m++){ const ar = cr[m]*cs[m] - ci[m]*sn[m], ai = cr[m]*sn[m] + ci[m]*cs[m]; if(Math.abs(ar) < 1e-14 && Math.abs(ai) < 1e-14) continue; const [vr, vi] = E.vecs[m]; for(let x=0;x<n;x++){ pr[x] += ar*vr[x] - ai*vi[x]; pi[x] += ar*vi[x] + ai*vr[x]; } } } M.t = t; }
/* P blocks from the occupied states: P_xy = sum_j psi_j(x) conj(psi_j(y)) */
function pblock(M, psr, psi, x, y){ let r = 0, im = 0; for(let j=0;j<M.k;j++){ const ar = psr[j][x], ai = psi[j][x], br = psr[j][y], bi = psi[j][y]; r += ar*br + ai*bi; im += ai*br - ar*bi; } return [r, im]; }
function readFrom(M, psr, psi){ const N = M.N, H = M.H, links = M.links, occ = new Float64Array(N), eloc = new Float64Array(N), jq = new Float64Array(links.length), jE = new Float64Array(links.length), X = new Float64Array(links.length), tau = [], Csite = [];
  for(let i=0;i<N;i++){ const a = 2*i, b = a + 1, c00 = pblock(M, psr, psi, a, a), c11 = pblock(M, psr, psi, b, b), c01 = pblock(M, psr, psi, a, b); occ[i] = c00[0] + c11[0]; Csite.push([c00[0], c01, c11[0]]);
    /* local energy: on-site part of Tr(P H) with half of each link */ eloc[i] = M.d[i][2]*(c00[0] - c11[0]) + 2*(M.d[i][0]*c01[0] + M.d[i][1]*c01[1]); }
  links.forEach((l, q) => { const a = 2*l.i, b = 2*l.j; let imQ = 0, imE = 0, x2 = 0, elink = 0;
    for(let r=0;r<2;r++) for(let s=0;s<2;s++){ const hr = H.Hr[a+r][b+s], hi = H.Hi[a+r][b+s], p = pblock(M, psr, psi, b+s, a+r); /* H_ij P_ji */ const tr = hr*p[0] - hi*p[1], ti = hr*p[1] + hi*p[0]; imQ += ti; elink += tr;
      const pij = pblock(M, psr, psi, a+r, b+s); x2 += pij[0]*pij[0] + pij[1]*pij[1];
      /* energy current with rho^E = (HP + PH)/2: Im Tr(H_ij rho_ji), rho_ji = (sum_x H_jx P_xi + P_jx H_xi)/2 over the two sites' own blocks and the link */
      let rr = 0, ri = 0; for(let x=0;x<M.n;x++){ const hjx = [H.Hr[b+s][x], H.Hi[b+s][x]]; if(hjx[0] || hjx[1]){ const pxi = pblock(M, psr, psi, x, a+r); rr += 0.5*(hjx[0]*pxi[0] - hjx[1]*pxi[1]); ri += 0.5*(hjx[0]*pxi[1] + hjx[1]*pxi[0]); } const hxi = [H.Hr[x][a+r], H.Hi[x][a+r]]; if(hxi[0] || hxi[1]){ const pjx = pblock(M, psr, psi, b+s, x); rr += 0.5*(pjx[0]*hxi[0] - pjx[1]*hxi[1]); ri += 0.5*(pjx[0]*hxi[1] + pjx[1]*hxi[0]); } }
      imE += hr*ri + hi*rr; }
    jq[q] = 2*imQ; jE[q] = 2*imE; X[q] = x2; eloc[l.i] += elink; eloc[l.j] += elink; });
  let Etot = 0, Eb = 0, Es = 0; for(let i=0;i<N;i++){ Etot += eloc[i]; if(M.body[i] >= 0) Eb += eloc[i]; else Es += eloc[i]; }
  M.atomsAt.forEach(i => { const C = Csite[i], det = (1 - C[0])*(1 - C[2]) - (C[1][0]**2 + C[1][1]**2), detC = C[0]*C[2] - (C[1][0]**2 + C[1][1]**2); tau.push(detC > 1e-300 && det > 1e-300 ? Math.log(det/detC) : NaN); });
  return { occ, eloc, jq, jE, X, Etot, Eb, Es, tau, Csite }; }
function read(M){ const r = readFrom(M, M.psr, M.psi); r.charge = r.occ.map((v, i) => v - M.ground.occ[i]); /* the change of each site's own state from the ground sea: ||C_i - C_i,ground|| (a kick turns the electron's spin on its site; the occupation alone would miss it) */
  r.change = r.Csite.map((C, i) => { const G = M.ground.Csite[i]; return Math.sqrt((C[0]-G[0])**2 + (C[2]-G[2])**2 + 2*((C[1][0]-G[1][0])**2 + (C[1][1]-G[1][1])**2)); });
  r.bodyChange = M.atomsAt.map((_, b) => { let s = 0; for(let i=0;i<M.N;i++) if(M.body[i] === b) s += r.change[i]; return s; }); r.bodyCharge = M.atomsAt.map((_, b) => { let s = 0; for(let i=0;i<M.N;i++) if(M.body[i] === b) s += r.charge[i]; return s; }); r.bodyAbs = M.atomsAt.map((_, b) => { let s = 0; for(let i=0;i<M.N;i++) if(M.body[i] === b) s += Math.abs(r.charge[i]); return s; }); r.dE = r.Etot - M.ground.Etot; r.t = M.t;
  /* the gap row: weight between neighbours along the line, and whether the chain connects (every gap link's weight above a third of the largest possible, 1/4) */
  r.row = M.links.map((l, q) => l.gap ? r.X[q] : null).filter(v => v !== null); r.rowMin = r.row.length ? Math.min(...r.row) : 0; r.connects = r.rowMin > (1/4)/3; return r; }
/* the bond curve: ground energy against separation, parallel and opposed, at the model's other settings (built once; a reading, not a claim) */
function bondCurve(o, seps){ const out = []; for(const sep of seps) for(const spins of ['parallel', 'opposed']){ const M = build(Object.assign({}, o, { sep, spins, kick:0 })); out.push({ sep, spins, E:M.Eground, gap:M.gap, N:M.N, rowMin:read(M).rowMin }); } return out; }
root.HSB = { build, at, read, prepare, bondCurve };
})(typeof window !== 'undefined' ? window : globalThis);
if(typeof module !== 'undefined') module.exports = globalThis.HSB;
