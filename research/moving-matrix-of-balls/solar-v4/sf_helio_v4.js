/* SCRIPT: SF-HELIO-V4  (v3 plus the edge folded by pressure balance against the outside)
   formerly SF-HELIO-V3
   The heliosphere as one ball, the Sun its leader. Jeromie Beasley. 16 Nov 2026. AI-assisted.
   Chart (declared): the ball's rim is the edge of the Sun's reach (R_rim, where Voyager 1 left the heliosphere). A real point at distance r from
   the Sun sits at ball radius Gamma = r / R_rim. The ball model is conformal to flat space, so with this chart, and only this one, every real shape
   (a body, a field line, an orbit) keeps its true shape and its true size against the rim. In the ball's own measure the point stands a step
   d = 2 artanh(Gamma) = ln z from the Sun, z = (R_rim + r)/(R_rim - r), Gamma = (z - 1)/(z + 1), R = Gamma^2, T = 1 - Gamma^2.
   Positions: JPL Keplerian elements and rates (Table 1), solved at the Julian date asked for. Pure functions of the raw data block. */
var SFH = function(DATA){
"use strict";
const PI = Math.PI, deg = PI/180, C = DATA.constants, AU = C.AU_km, MU0 = 4e-7*PI, OUT = DATA.outside, MP = 1.67262192e-27, KB = 1.380649e-23;
/* ---- the edge: where the Sun's push equals the outside push, direction by direction ----
   Sun's push at distance r: P_sun(r) = P_Mercury (a_Mercury / r)^2 (measured at Mercury, falling as 1/r^2).
   Outside push on a surface facing direction n (unit, from the Sun), from the raw data:
     flow:  rho v^2 max(n.u, 0)^2      (u = nose; the flow presses only on the side that faces it)
     heat:  2 n k T                    (same in every direction)
     field: (B^2 / 2 mu0) (3/2) (1 - (n.b)^2)   (a field lying along the surface presses; one along n does not; the 3/2 keeps its sphere average at B^2/2mu0)
   Perfect world: each directional term replaced by its average over the sphere (flow 1/6, field 1), so the edge is a sphere of radius R0.
   Each dial f in [0, 1] blends a term from its average (0) to its direction (1). The sphere average of every term is the same at every dial.
   Edge distance: r(n) = a_Mercury sqrt(P_Mercury / P_out(n)). A reading of the balance face by face (each direction on its own), not a flow solution. */
const ecl = (l, b) => [Math.cos(b*deg)*Math.cos(l*deg), Math.cos(b*deg)*Math.sin(l*deg), Math.sin(b*deg)];
const NOSE = ecl(OUT.flow.inflow_ecl_lon_deg + 180, -OUT.flow.inflow_ecl_lat_deg), BDIR = ecl(OUT.field.ecl_lon_deg, OUT.field.ecl_lat_deg);
const EDGE = { flow:0, field:0, n:OUT.density_default_cm3 };
function pressures(){ const n = EDGE.n*1e6, v = OUT.flow.speed_km_s*1e3, B = OUT.field.strength_uG*1e-10; return { flow:n*MP*v*v, heat:2*n*KB*OUT.flow.temp_K, field:B*B/(2*MU0) }; }
function pOut(u){ const P = pressures(), c = Math.max(0, u[0]*NOSE[0] + u[1]*NOSE[1] + u[2]*NOSE[2]), cb = u[0]*BDIR[0] + u[1]*BDIR[1] + u[2]*BDIR[2];
  return P.flow*((1 - EDGE.flow)/6 + EDGE.flow*c*c) + P.heat + P.field*((1 - EDGE.field) + EDGE.field*1.5*(1 - cb*cb)); }
const edgeKm = u => C.mercury_mean_distance_km*Math.sqrt(C.ram_pressure_at_mercury_Pa/pOut(u));
const R0km = () => { const P = pressures(); return C.mercury_mean_distance_km*Math.sqrt(C.ram_pressure_at_mercury_Pa/(P.flow/6 + P.heat + P.field)); };
let RIM = R0km();
function setEdge(k, v){ EDGE[k] = v; RIM = R0km(); }
const SUN = DATA.sun, PLANETS = DATA.planets, BODIES = [SUN].concat(PLANETS);
const kepler = (M, e) => { let E = M + e*Math.sin(M); for(let k=0;k<30;k++){ const dE = (E - e*Math.sin(E) - M)/(1 - e*Math.cos(E)); E -= dE; if(Math.abs(dE) < 1e-14) break; } return E; };
function elementsAt(p, jd){ const T = (jd - 2451545.0)/36525, v = p.el.map((x, i) => x + p.rate[i]*T); return { a:v[0], e:v[1], I:v[2]*deg, L:v[3]*deg, peri:v[4]*deg, node:v[5]*deg }; }
/* heliocentric position in the J2000 ecliptic frame, km; anom = extra mean anomaly (radians) for drawing the path */
function posOf(p, jd, anom){ const q = elementsAt(p, jd), w = q.peri - q.node; let M = q.L - q.peri + (anom||0); M = M - 2*PI*Math.round(M/(2*PI)); const E = kepler(M, q.e);
  const xp = q.a*(Math.cos(E) - q.e), yp = q.a*Math.sqrt(1 - q.e*q.e)*Math.sin(E), cw = Math.cos(w), sw = Math.sin(w), cO = Math.cos(q.node), sO = Math.sin(q.node), cI = Math.cos(q.I), sI = Math.sin(q.I);
  return [ ((cw*cO - sw*sO*cI)*xp + (-sw*cO - cw*sO*cI)*yp)*AU, ((cw*sO + sw*cO*cI)*xp + (-sw*sO + cw*cO*cI)*yp)*AU, (sw*sI*xp + cw*sI*yp)*AU ]; }
const orbitNormal = (p, jd) => { const q = elementsAt(p, jd); return [Math.sin(q.I)*Math.sin(q.node), -Math.sin(q.I)*Math.cos(q.node), Math.cos(q.I)]; };
/* rotation pole (right ascension, declination, ICRF) turned into the ecliptic frame by the Earth's obliquity */
function poleEcl(b){ const ra = b.pole_ra_dec[0]*deg, de = b.pole_ra_dec[1]*deg, eps = C.earth_obliquity_deg*deg, x = Math.cos(de)*Math.cos(ra), y = Math.cos(de)*Math.sin(ra), z = Math.sin(de);
  return [x, Math.cos(eps)*y + Math.sin(eps)*z, -Math.sin(eps)*y + Math.cos(eps)*z]; }
const dot = (a,b) => a[0]*b[0]+a[1]*b[1]+a[2]*b[2], norm = a => Math.hypot(a[0],a[1],a[2]), cross = (a,b) => [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]], unit = a => { const n = norm(a); return [a[0]/n, a[1]/n, a[2]/n]; };
/* check on the raw data: the tilt of each pole from its own orbit normal, against the fact sheet's obliquity (the Sun: from the ecliptic pole) */
function obliquityCheck(jd){ return BODIES.map((b, i) => { const n = i === 0 ? [0,0,1] : orbitNormal(b, jd), got = Math.acos(Math.max(-1, Math.min(1, dot(poleEcl(b), n))))/deg; return { name:b.name, fromPole:got, sheet:b.obliquity_deg, diff:got - b.obliquity_deg }; }); }
/* the chart and the ball's own measures */
const gammaOf = r => r/RIM, stepOf = r => Math.log((RIM + r)/(RIM - r));   /* RIM: the perfect-world edge, the ball's rim */
/* share of everything the Sun sends out evenly that a round body of radius R at distance r takes: flat space, and the ball's own formula */
const shareFlat = (R, r) => { const s = R/r; return s*s/(2*(1 + Math.sqrt(1 - s*s))); };                 /* = (1 - sqrt(1 - s^2))/2, written so small s keeps its digits */
function shareBall(R, r){ const c = r/RIM, e = R/RIM, a = Math.log1p(2*e/(1 + c - e)), b = Math.log1p(2*e/(1 - c - e)), rho = (a + b)/2;      /* the body is a round ball in the ball's measure too: radius rho, centre at d */
  const d = (Math.log((1 + c - e)/(1 - c + e)) + Math.log((1 + c + e)/(1 - c - e)))/2, s = Math.sinh(rho)/Math.sinh(d); return { rho, d, share:s*s/(2*(1 + Math.sqrt(1 - s*s))) }; }
/* pressure of the Sun's wind at distance r (km), from the measured mean at Mercury, falling as 1/r^2 */
const ramP = r => C.ram_pressure_at_mercury_Pa*Math.pow(C.mercury_mean_distance_km/r, 2);
/* sunward edge of a body's field, in its radii: field pressure doubled at the edge against the wind, (2B)^2/(2 mu0) = P */
const edgeOf = (b, r) => b.dipole_G > 0 ? Math.pow(2*Math.pow(b.dipole_G*1e-4, 2)/(MU0*ramP(r)), 1/6) : NaN;
const edgeShape = (r0, th) => r0*Math.pow(2/(1 + Math.cos(th)), 0.5);                                     /* shape about the Sun line (the MESSENGER fit, flaring 0.5) */
/* symmetric eigen-solve (Jacobi) */
function eigSym(A){ const n = A.length, a = A.map(r => r.slice()), V = a.map((r, i) => r.map((_, j) => i === j ? 1 : 0));
  for(let sw=0;sw<100;sw++){ let off = 0; for(let i=0;i<n;i++) for(let j=i+1;j<n;j++) off += a[i][j]*a[i][j]; if(off < 1e-300) break;
    for(let p=0;p<n;p++) for(let q=p+1;q<n;q++){ if(a[p][q] === 0) continue; const th = (a[q][q] - a[p][p])/(2*a[p][q]), t = Math.sign(th || 1)/(Math.abs(th) + Math.sqrt(th*th + 1)), c = 1/Math.sqrt(t*t + 1), s = t*c;
      for(let k=0;k<n;k++){ const x = a[k][p], y = a[k][q]; a[k][p] = c*x - s*y; a[k][q] = s*x + c*y; } for(let k=0;k<n;k++){ const x = a[p][k], y = a[q][k]; a[p][k] = c*x - s*y; a[q][k] = s*x + c*y; }
      for(let k=0;k<n;k++){ const x = V[k][p], y = V[k][q]; V[k][p] = c*x - s*y; V[k][q] = s*x + c*y; } } }
  const o = a.map((_, i) => i).sort((i, j) => a[j][j] - a[i][i]); return { val:o.map(i => a[i][i]), vec:o.map(i => V.map(r => r[i])) }; }
/* everything at one moment */
function state(jd){ const pos = [[0,0,0]].concat(PLANETS.map(p => posOf(p, jd))), m = BODIES.map(b => b.mass_1e24kg + (b.name === 'Earth' ? 0.073 : 0)), Mtot = m.reduce((a, b) => a + b, 0);
  const bary = [0,1,2].map(k => pos.reduce((a, p, i) => a + m[i]*p[k], 0)/Mtot);
  const rows = BODIES.map((b, i) => { if(i === 0) return { name:b.name, r:0, pos:pos[0] }; const r = norm(pos[i]), g = gammaOf(r), sb = shareBall(b.Req_km, r), r0 = edgeOf(b, r), wind = r0 > 0 ? Math.pow(r0*b.Req_km/r, 2)/2 : shareFlat(b.Req_km, r);
    return { name:b.name, pos:pos[i], r, gamma:g, step:stepOf(r), T:1 - g*g, lightSec:r/C.c_km_s, light:shareFlat(b.Req_km, r), lightBall:sb.share, rho:sb.rho, d:sb.d, watts:shareFlat(b.Req_km, r)*C.sun_luminosity_W, edge:r0, wind }; });
  /* the leader: the matrix of pulls W_ij = m_i m_j / r_ij between every pair, and its leading eigenvector */
  const n = BODIES.length, W = BODIES.map((_, i) => BODIES.map((_, j) => i === j ? 0 : m[i]*m[j]/(norm([0,1,2].map(k => pos[i][k] - pos[j][k]))/AU))), ev = eigSym(W), lead = ev.vec[0].map(x => x*x);
  /* Gram of the mass-weighted places about the common centre, G = X^T X (3 by 3) */
  const G = [0,1,2].map(a => [0,1,2].map(b2 => pos.reduce((s, p, i) => s + m[i]*(p[a] - bary[a])*(p[b2] - bary[b2])/(AU*AU), 0))), ge = eigSym(G), tr = ge.val.reduce((a, b) => a + b, 0);
  const lightSum = rows.slice(1).reduce((a, r) => a + r.light, 0), windSum = rows.slice(1).reduce((a, r) => a + r.wind, 0);
  return { jd, rows, bary, baryR:norm(bary)/SUN.Req_km, sunMassShare:m[0]/Mtot, lead, leadVal:ev.val[0], gram:ge.val.map(v => v/tr), gramAxis:ge.vec[0], lightSum, windSum }; }
const jdNow = () => Date.now()/86400000 + 2440587.5, dateOf = jd => new Date((jd - 2440587.5)*86400000).toISOString().slice(0, 16).replace('T', ' ') + ' UT';
return { DATA, SUN, PLANETS, BODIES, AU, get RIM(){ return RIM; }, EDGE, setEdge, edgeKm, pOut, pressures, R0km, NOSE, BDIR, ecl, posOf, elementsAt, orbitNormal, poleEcl, obliquityCheck, gammaOf, stepOf, shareFlat, shareBall, ramP, edgeOf, edgeShape, eigSym, state, jdNow, dateOf, unit, cross, dot, norm };
};
if(typeof module !== 'undefined') module.exports = SFH;
