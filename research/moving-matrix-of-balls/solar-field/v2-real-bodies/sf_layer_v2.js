/* SCRIPT: SF-LAYER-V2
   Solar Field v2 — each ball is its own body: measured shape, rotation axis and magnetic field (SF-BODIES-V2); sized on a logarithmic scale.
   The copy of the Sun's faces is no longer drawn in the planets: a planet's ball shows its rim, its own body and field, and the Sun's light as it sees it.
   Built on v1 — the Sun and the planets out to Mars as five balls of one kind on the field. Jeromie Beasley. 15 Nov 2026. AI-assisted.
   The page's own ball is drawn once for the Sun and once for each planet. The light is traced once, from the Sun, by the ball's own law,
   and drawn in every ball as that ball sees it (each drawn point X goes to G_p^-1 X, G_p = the step from the Sun's centre to the planet's).
   Each planet keeps its I arm pointing away from the Sun (drawing convention). Perfect world first; each natural effect has its own dial.
   Host adapter window.__TBHOST = { S3, WORLD, tau(), S(), light:[...], P, CLOCK } is set by the page app. Needs Mixer3D, LH, SF. */
(function(){
"use strict";
const H = window.__TBHOST, M = window.Mixer3D, T = M.T, S3 = H.S3, WORLD = H.WORLD, RB = 2.6, PI = Math.PI, DAYS = 10;      /* days of the calendar per unit of the page clock */
const fmt = (x,n) => Number.isFinite(x) ? x.toFixed(n == null ? 4 : n) : '—', sci = x => Number.isFinite(x) ? x.toExponential(1) : '—';
const D = { steps:0, ellipse:0, tilt:0, timing:0, field:0 }, X = { on:true, lightIn:'all', focus:-1 };
const NAT = { zbar:H.P.zbar.slice(), amp:H.P.amp }, PERF = { zbar:[3,3,3], amp:0 };
function applyField(){ for(let a=0;a<3;a++) H.P.zbar[a] = PERF.zbar[a] + (NAT.zbar[a] - PERF.zbar[a])*D.field; H.P.amp = PERF.amp + (NAT.amp - PERF.amp)*D.field; const o = document.getElementById('o_amp'), i = document.getElementById('amp'); if(o){ o.textContent = H.P.amp.toFixed(2); i.value = H.P.amp; } }
applyField();
const RAD = SF.R0/2, ring = d => RB*(1 + Math.tanh(SF.R0/4))*d/SF.R0;      /* a ball's own reach (half the perfect step); field distance of a ball at hyperbolic distance d */
let PL = SF.state(0, D), pos = [], BOOK = null, wob = null, bookT = -1;
const FIELD = new T.Group(); S3.world.add(FIELD);
const seg = (n, op) => { const g = new T.BufferGeometry(); g.setAttribute('position', new T.BufferAttribute(new Float32Array(n*6), 3)); g.setAttribute('color', new T.BufferAttribute(new Float32Array(n*6), 3));
  const m = new T.LineSegments(g, new T.LineBasicMaterial({ vertexColors:true, transparent:true, opacity:op, depthWrite:false, blending:T.AdditiveBlending })); m.frustumCulled = false; FIELD.add(m); let i = 0;
  return { reset(){ i = 0; }, add(a, b, c){ if(i >= n) return; const p = g.attributes.position, q = g.attributes.color; p.setXYZ(2*i, a.x, a.y, a.z); p.setXYZ(2*i+1, b.x, b.y, b.z); q.setXYZ(2*i, c[0], c[1], c[2]); q.setXYZ(2*i+1, c[0], c[1], c[2]); i++; }, done(){ g.setDrawRange(0, 2*i); g.attributes.position.needsUpdate = g.attributes.color.needsUpdate = true; } }; };
const orbits = seg(4*200, 0.55), spokes = seg(4*2, 0.8);
const labels = [M.label('Sun', '#ffe9a8', 0.55)].concat(SF.BODIES.map(b => M.label(b.name, '#' + b.col.map(v => Math.round(255*v).toString(16).padStart(2,'0')).join(''), 0.5))); labels.forEach(l => FIELD.add(l));
/* ---- each body in its own ball: chart x = r/R -> Smith coordinate of 3x (surface at half the ball radius) ---- */
const BODY = SFB.BODY, RMIN = Math.min(...BODY.map(b => b.Req)), RMAX = Math.max(...BODY.map(b => b.Req));
const sizeOf = b => 0.42 + 0.58*Math.log(b.Req/RMIN)/Math.log(RMAX/RMIN);            /* drawn size of a ball: logarithm of its radius, Mercury 0.42 to the Sun 1 */
const deg = PI/180, w = v => new T.Vector3(v[0], v[2], -v[1]);                        /* ball (i, j, k) -> world */
const rotAxis = b => [0, Math.sin(b.obl*deg), Math.cos(b.obl*deg)];                   /* rotation axis: tilted from the orbit normal K by the obliquity, toward J (the node direction is not modelled) */
const dipAxis = b => { const o = (b.obl + b.tilt)*deg; return [0, Math.sin(o), Math.cos(o)]; };   /* dipole axis: a further tilt in the same plane (its phase about the rotation axis is not modelled) */
const BG = BODY.map(b => { const g = new T.Group(); g.visible = false; S3.world.add(g);
  const ball = new T.Mesh(new T.SphereGeometry(SFB.chart(1)*RB, 40, 28), new T.MeshStandardMaterial({ color:new T.Color(b.col[0], b.col[1], b.col[2]), emissive:new T.Color(b.col[0]*0.35, b.col[1]*0.35, b.col[2]*0.35), roughness:0.6, transparent:true, opacity:0.9 }));
  const ax = rotAxis(b), q = new T.Quaternion().setFromUnitVectors(new T.Vector3(0,1,0), w(ax).normalize()); ball.quaternion.copy(q); ball.scale.set(1, 1 - b.f, 1); g.add(ball);   /* flattened along its own rotation axis by the measured amount */
  const mk = (n, op) => { const geo = new T.BufferGeometry(); geo.setAttribute('position', new T.BufferAttribute(new Float32Array(n*6), 3)); geo.setAttribute('color', new T.BufferAttribute(new Float32Array(n*6), 3));
    const m = new T.LineSegments(geo, new T.LineBasicMaterial({ vertexColors:true, transparent:true, opacity:op, depthWrite:false, blending:T.AdditiveBlending })); m.frustumCulled = false; g.add(m); let i = 0;
    return { reset(){ i = 0; }, add(a, c, col){ if(i >= n) return; const p = geo.attributes.position, k = geo.attributes.color; p.setXYZ(2*i, a.x, a.y, a.z); p.setXYZ(2*i+1, c.x, c.y, c.z); k.setXYZ(2*i, col[0], col[1], col[2]); k.setXYZ(2*i+1, col[0], col[1], col[2]); i++; }, done(){ geo.setDrawRange(0, 2*i); geo.attributes.position.needsUpdate = geo.attributes.color.needsUpdate = true; } }; };
  return { g, ball, lines:mk(9000, 0.85), edge:mk(4000, 0.7), r0:NaN }; });
/* a physical point (in body radii, ball axes) to its place in the ball */
const place = v => { const r = Math.hypot(v[0], v[1], v[2]), c = SFB.chart(r)*RB/r; return new T.Vector3(v[0]*c, v[2]*c, -v[1]*c); };
function drawBody(k, aNow){ const b = BODY[k], G = BG[k]; G.lines.reset(); G.edge.reset();
  const ra = rotAxis(b), da = dipAxis(b), white = [0.9,0.9,0.95];
  G.lines.add(place(ra.map(x => x*1.0)), place(ra.map(x => x*2.2)), white); G.lines.add(place(ra.map(x => -x*1.0)), place(ra.map(x => -x*2.2)), white);          /* rotation axis */
  if(b.dipG > 0){ const r0 = b.name === 'Sun' ? NaN : SFB.standoff(b, aNow); G.r0 = r0; const sun = [-1,0,0];                                                    /* the Sun lies along this ball's -I arm */
    const e0 = (() => { const a = Math.abs(da[0]) < 0.9 ? [1,0,0] : [0,1,0], c = [da[1]*a[2]-da[2]*a[1], da[2]*a[0]-da[0]*a[2], da[0]*a[1]-da[1]*a[0]], l = Math.hypot(...c); return c.map(x => x/l); })(), e1 = [da[1]*e0[2]-da[2]*e0[1], da[2]*e0[0]-da[0]*e0[2], da[0]*e0[1]-da[1]*e0[0]];
    const off = da.map(x => x*b.off), Ls = b.name === 'Sun' ? [1.5, 2.2, 3.2, 5, 8, 14, 30] : [1.15, 1.3, 1.5, 1.8, 2.3, 3, 4, 5.5, 7.5, 10, 14], inside = v => { if(!(r0 > 0)) return true; const r = Math.hypot(...v), th = Math.acos(Math.max(-1, Math.min(1, (v[0]*sun[0] + v[1]*sun[1] + v[2]*sun[2])/r))); return r <= SFB.boundary(r0, th); };
    for(const L of Ls) for(let m=0;m<8;m++){ const ph = 2*PI*m/8, eq = [0,1,2].map(i => Math.cos(ph)*e0[i] + Math.sin(ph)*e1[i]); let prev = null, pv = null;
      for(let s=0;s<=64;s++){ const lam = -PI/2 + PI*s/64, r = L*Math.cos(lam)*Math.cos(lam), v = [0,1,2].map(i => r*(Math.cos(lam)*eq[i] + Math.sin(lam)*da[i]) + off[i]), rr = Math.hypot(...v); const ok = rr >= 1 && inside(v);
        if(ok && prev && pv){ const f = 0.35 + 0.65/Math.sqrt(L); G.lines.add(prev, place(v), [b.col[0]*f, b.col[1]*f, b.col[2]*f]); } prev = ok ? place(v) : null; pv = ok; } }
    G.lines.add(place(da.map((x,i) => x*1.0 + off[i])), place(da.map((x,i) => x*2.6 + off[i])), [1,0.75,0.3]); G.lines.add(place(da.map((x,i) => -x*1.0 + off[i])), place(da.map((x,i) => -x*2.6 + off[i])), [1,0.75,0.3]);   /* dipole axis */
    if(r0 > 0){ /* the outer boundary of the field, computed from pressure balance, about the Sun line */
      for(let m=0;m<16;m++){ const ph = 2*PI*m/16; let prev = null; for(let s=0;s<=48;s++){ const th = 2.6*s/48, r = SFB.boundary(r0, th), v = [-r*Math.cos(th), r*Math.sin(th)*Math.cos(ph), r*Math.sin(th)*Math.sin(ph)], p = place(v); if(prev) G.edge.add(prev, p, [0.45,0.8,1]); prev = p; } }
      for(const th of [0.5, 1.0, 1.5, 2.0, 2.5]){ let prev = null; for(let m=0;m<=48;m++){ const ph = 2*PI*m/48, r = SFB.boundary(r0, th), p = place([-r*Math.cos(th), r*Math.sin(th)*Math.cos(ph), r*Math.sin(th)*Math.sin(ph)]); if(prev) G.edge.add(prev, p, [0.3,0.55,0.75]); prev = p; } }
      if(b.mp){ let prev = null; for(let m=0;m<=64;m++){ const ph = 2*PI*m/64, th = 0.35, r = SFB.boundary(b.mp, th), p = place([-r*Math.cos(th), r*Math.sin(th)*Math.cos(ph), r*Math.sin(th)*Math.sin(ph)]); if(prev && m%2) G.edge.add(prev, p, [1,0.75,0.3]); prev = p; } } } }   /* dashed gold ring: the measured boundary near its nose */
  G.lines.done(); G.edge.done(); }
/* field position of a planet: the direction of its centre as the Sun sees it, at the field distance of its ring; ball (i, j, k) -> world (x, y, z) = (i, k, -j) */
function fieldPos(p){ const c = SF.centre(p), n = Math.hypot(c[1], c[2], c[3]), F = ring(p.d); return new T.Vector3(F*c[1]/n, F*c[3]/n, -F*c[2]/n); }
function carry(src, dst, n, Mx){ for(let o=0;o<n*3;o+=3){ const bi = src[o]/RB, bk = src[o+1]/RB, bj = -src[o+2]/RB, r2 = bi*bi + bj*bj + bk*bk; if(r2 === 0){ dst[o] = dst[o+1] = dst[o+2] = 0; continue; }
    let q0, q1, q2, q3, s;
    if(r2 < 0.9996){ const d = 1 - r2, p0 = (1 + r2)/d, p1 = 2*bi/d, p2 = 2*bj/d, p3 = 2*bk/d;
      q0 = Mx[0][0]*p0 + Mx[0][1]*p1 + Mx[0][2]*p2 + Mx[0][3]*p3; q1 = Mx[1][0]*p0 + Mx[1][1]*p1 + Mx[1][2]*p2 + Mx[1][3]*p3; q2 = Mx[2][0]*p0 + Mx[2][1]*p1 + Mx[2][2]*p2 + Mx[2][3]*p3; q3 = Mx[3][0]*p0 + Mx[3][1]*p1 + Mx[3][2]*p2 + Mx[3][3]*p3; s = RB/(1 + q0); }
    else { const r = Math.sqrt(r2), p1 = bi/r, p2 = bj/r, p3 = bk/r; q0 = Mx[0][0] + Mx[0][1]*p1 + Mx[0][2]*p2 + Mx[0][3]*p3; q1 = Mx[1][0] + Mx[1][1]*p1 + Mx[1][2]*p2 + Mx[1][3]*p3; q2 = Mx[2][0] + Mx[2][1]*p1 + Mx[2][2]*p2 + Mx[2][3]*p3; q3 = Mx[3][0] + Mx[3][1]*p1 + Mx[3][2]*p2 + Mx[3][3]*p3; s = RB*r/q0; }
    dst[o] = q1*s; dst[o+1] = q3*s; dst[o+2] = -q2*s; } }
const LIGHT = H.light.map(o => ({ o, attr:o.geometry.attributes.position, back:new Float32Array(o.geometry.attributes.position.array.length) }));
const KEEP = new Set(H.light.concat(WORLD.children.slice(0, 4)));
const count = L => { const dr = L.o.geometry.drawRange, c = L.attr.count; return Math.min(c, Number.isFinite(dr.count) ? dr.start + dr.count : c); };
/* ---- the books ----
   For each planet a bundle of NB rays is launched from the Sun inside a cone about the planet's direction (half-angle beta, a few times
   the angle the ball subtends), even in solid angle, and traced by the page's own law to depth 14. The share of all the Sun's light passing
   through the ball is (cone's part of the sky) x (mean flux of the bundle that passes through it). The same bundle kept straight is the
   control against the solid-angle formula. One even set of NL rays gives the Sun's own ledger. */
const NB = 900, NL = 1500, OPT = { maxEv:14, fmin:2e-5, smax:9, maxSeg:160 };
const LDIRS = (() => { const o = [], ga = PI*(3 - Math.sqrt(5)); for(let i=0;i<NL;i++){ const y = 1 - 2*(i + 0.5)/NL, r = Math.sqrt(1 - y*y), a = ga*i; o.push([r*Math.cos(a), y, r*Math.sin(a)]); } return o; })();
function cone(u, beta, n){ const a0 = Math.abs(u[2]) < 0.9 ? [0,0,1] : [1,0,0], e1 = [u[1]*a0[2]-u[2]*a0[1], u[2]*a0[0]-u[0]*a0[2], u[0]*a0[1]-u[1]*a0[0]], l = Math.hypot(...e1); for(let k=0;k<3;k++) e1[k] /= l;
  const e2 = [u[1]*e1[2]-u[2]*e1[1], u[2]*e1[0]-u[0]*e1[2], u[0]*e1[1]-u[1]*e1[0]], out = [], ga = PI*(3 - Math.sqrt(5)), cb = Math.cos(beta);
  for(let i=0;i<n;i++){ const c = 1 - (1 - cb)*(i + 0.5)/n, sn = Math.sqrt(1 - c*c), t = ga*i; out.push([0,1,2].map(k => c*u[k] + sn*(Math.cos(t)*e1[k] + Math.sin(t)*e2[k]))); } return out; }
let bookI = 0;
function books(S){ if(!BOOK) BOOK = { share:PL.map(() => NaN), straight:PL.map(() => NaN), free:PL.map(() => NaN), beta:PL.map(() => NaN), rim:NaN, cut:NaN, small:NaN, ledger:NaN, flux:NaN, cons:NaN };
  if(bookI === PL.length){ const TR = LH.trace(S, LDIRS); BOOK.rim = TR.rim/NL; BOOK.cut = TR.cut/NL; BOOK.small = TR.small/NL; BOOK.ledger = TR.resLedger; BOOK.flux = TR.resFlux; BOOK.cons = TR.resCons; }
  else { const b = bookI, p = PL[b], c = SF.centre(p), n = Math.hypot(c[1], c[2], c[3]), u = [c[1]/n, c[2]/n, c[3]/n], alpha = Math.asin(Math.min(1, Math.sinh(RAD)/Math.sinh(Math.max(RAD, p.d)))), beta = Math.min(PI, 3*alpha + 0.02), sky = (1 - Math.cos(beta))/2;
    const dirs = cone(u, beta, NB), TR = LH.trace(S, dirs, OPT), best = new Float32Array(NB); let st = 0;
    for(const s of TR.segs){ if(s.flux > best[s.ray] && SF.segDist(c, LH.mv(s.g, s.X), LH.mv(s.g, s.v), s.s) <= RAD) best[s.ray] = s.flux; }
    for(let i=0;i<NB;i++){ const d = dirs[i]; if(SF.segDist(c, [1,0,0,0], [0,d[0],d[1],d[2]], 16) <= RAD) st++; }
    let t = 0; for(let i=0;i<NB;i++) t += best[i]; BOOK.share[b] = sky*t/NB; BOOK.straight[b] = sky*st/NB; BOOK.free[b] = SF.freeShare(p.d, RAD); BOOK.beta[b] = beta;
    if(!wob) wob = PL.map(() => [1e9, -1e9]); wob[b][0] = Math.min(wob[b][0], BOOK.share[b]); wob[b][1] = Math.max(wob[b][1], BOOK.share[b]); }
  bookI = (bookI + 1) % (PL.length + 1); }
/* ---- draw ---- */
const R = S3.renderer, cam = S3.camera, scene = S3.scene, orig = R.render.bind(R), bg = scene.background ? scene.background.clone() : new T.Color(0x05070b);
R.render = function(sc, cm){ if(sc !== scene || !X.on){ FIELD.visible = false; BG.forEach(G => G.g.visible = false); WORLD.scale.setScalar(1); WORLD.position.set(0,0,0); R.autoClear = true; scene.background = bg; return orig(sc, cm); }
  const S = H.S(), day = H.tau()*DAYS; PL = SF.state(day, D); pos = PL.map(fieldPos);
  const now = performance.now(); if(now - bookT > 250){ bookT = now; books(S); }
  /* orbits (one turn of each planet's path at the present dials) and the line from the Sun to each planet */
  orbits.reset(); spokes.reset(); PL.forEach((p, b) => { const Tp = p.T; let prev = null; for(let k=0;k<=200;k++){ const q = fieldPos(SF.state(day + Tp*k/200, D)[b]); if(prev) orbits.add(prev, q, p.col.map(v => v*0.5)); prev = q; }
    spokes.add(new T.Vector3(0,0,0), pos[b], p.col.map(v => v*0.25)); labels[b+1].position.set(pos[b].x, pos[b].y + RB*sizeOf(BODY[b+1]) + 0.4, pos[b].z); }); orbits.done(); spokes.done(); labels[0].position.set(0, RB + 0.45, 0);
  const ext = Math.max(...pos.map(v => v.length())) + RB, V = S3.view, Dc = V.dist*(0.55 + ext/RB*0.62)*(window.innerWidth < 640 ? 1.5 : 1), pt = Math.max(-1.3, Math.min(1.4, V.pitch + 0.75)), yw = V.yaw;
  const tg = X.focus <= 0 ? new T.Vector3(0,0,0) : pos[X.focus-1], Df = X.focus < 0 ? Dc : V.dist*1.75*sizeOf(BODY[X.focus]), pf = X.focus < 0 ? pt : V.pitch;   /* zoom: the whole field, or close on one body */
  cam.position.set(tg.x + Df*Math.cos(pf)*Math.sin(yw), tg.y + Df*Math.sin(pf), tg.z + Df*Math.cos(pf)*Math.cos(yw)); cam.lookAt(tg.x, tg.y, tg.z); cam.updateMatrixWorld();
  scene.background = null; R.autoClear = false; R.setClearColor(bg, 1); R.clear();
  const Ns = LIGHT.map(count); LIGHT.forEach((L, k) => L.back.set(L.attr.array.subarray(0, Ns[k]*3)));
  BODY.forEach((b, k) => drawBody(k, k === 0 ? 0 : SF.BODIES[k-1].a*PL[k-1].rho));
  const show = k => BG.forEach((G, i) => G.g.visible = i === k);
  WORLD.position.set(0,0,0); WORLD.scale.setScalar(sizeOf(BODY[0])); BG[0].g.position.set(0,0,0); BG[0].g.scale.setScalar(sizeOf(BODY[0])); show(0); FIELD.visible = true; orig(sc, cm);                 /* the Sun: its own ball in full */
  const vis = WORLD.children.map(c => c.visible); WORLD.children.forEach(c => { if(!KEEP.has(c)) c.visible = false; });                                    /* planets: rim and light only, no copy of the Sun's faces */
  for(let b=0;b<PL.length;b++){ const Mx = SF.cellInv(PL[b]), sz = sizeOf(BODY[b+1]); LIGHT.forEach((L, k) => { if(X.lightIn === 'all') carry(L.back, L.attr.array, Ns[k], Mx); else L.attr.array.fill(0, 0, Ns[k]*3); L.attr.needsUpdate = true; });
    WORLD.position.copy(pos[b]); WORLD.scale.setScalar(sz); BG[b+1].g.position.copy(pos[b]); BG[b+1].g.scale.setScalar(sz); show(b+1); FIELD.visible = false; orig(sc, cm); }
  WORLD.children.forEach((c, i) => c.visible = vis[i]); show(-1); WORLD.scale.setScalar(1);
  LIGHT.forEach((L, k) => { L.attr.array.set(L.back.subarray(0, Ns[k]*3)); L.attr.needsUpdate = true; }); WORLD.position.set(0,0,0); };
/* ---- panel ---- */
const css = document.createElement('style'); css.textContent = `.tb{position:fixed;top:12px;right:12px;width:min(430px,calc(100% - 420px));max-height:calc(100% - 30px);overflow:auto;background:var(--panel,rgba(9,13,20,.86));border:1px solid var(--edge,#1f2a38);border-radius:8px;padding:11px 12px;font-size:12px;color:var(--ink,#dfe7ef);backdrop-filter:blur(6px);z-index:5}
.tb h2{margin:0 0 4px;font-size:13px;letter-spacing:.08em;text-transform:uppercase;font-family:var(--head,inherit)}.tb p{margin:4px 0 8px;color:var(--dim,#8a9aab);font-size:11.5px;line-height:1.5}
.tb .r{display:flex;flex-wrap:wrap;gap:5px;margin:5px 0;align-items:center}.tb button{font-size:11.5px;padding:4px 8px;background:#0e1520;color:inherit;border:1px solid var(--edge,#1f2a38);border-radius:5px;cursor:pointer}.tb button[aria-pressed=true]{border-color:#f2c14e;color:#f2c14e}
.tb .row{display:flex;justify-content:space-between;gap:10px;padding:4px 0;border-bottom:1px solid rgba(31,42,56,.6);color:var(--dim,#8a9aab)}.tb .row b{font-family:var(--mono,monospace);font-weight:400;color:var(--ink,#dfe7ef);text-align:right;font-size:11px;white-space:pre-wrap}
.tb .g{font-size:10px;color:var(--faint,#55657a);margin:-1px 0 2px}.tb input{accent-color:#63d3ff;width:110px;vertical-align:middle}.tb summary{cursor:pointer;color:var(--dim,#8a9aab)}.tb label{display:flex;justify-content:space-between;align-items:center;gap:6px;width:100%;font-size:11.5px}
.tb table{width:100%;border-collapse:collapse;font-family:var(--mono,monospace);font-size:10px}.tb td,.tb th{padding:3px 4px;text-align:right;border-bottom:1px solid rgba(31,42,56,.6);font-weight:400}.tb th{color:var(--dim,#8a9aab)}.tb td:first-child,.tb th:first-child{text-align:left}body.clean .tb{display:none}
@media (max-width:900px){.tb{top:auto;bottom:8px;left:8px;right:8px;width:auto;max-height:36%}}`; document.head.append(css);
const DIALS = [['steps','Steps: equal → as measured'],['ellipse','Paths: circles → ellipses'],['tilt','Planes: one plane → tilted'],['timing','Timing: equal → own periods'],['field','Faces: equal and still → uneven and breathing']];
document.body.insertAdjacentHTML('beforeend', `<div class="tb" id="tb"><h2>Solar field</h2>
<details><summary>What this shows</summary><p>The Sun and the planets out to Mars as five balls of one kind. The light is traced once, from the Sun, by this page’s own law at the faces, and drawn in every ball as that ball sees it. It starts in the perfect world: equal steps (each planet one step of ratio 3 beyond the last), circles, one plane, equal timing, equal still faces. Each dial turns one natural effect from perfect (0) to as measured (1). Reading, not a theorem: a step is the logarithm of a ratio of distances from the Sun, and the ball is the peel coordinate, not space. Each ball is its own body: its measured size (logarithmic scale), flattening, rotation axis, and its magnetic field where it has one. Orbit data: NASA Planetary Fact Sheet.</p></details>
<div class="r"><button id="sf_perfect" aria-pressed="true">Perfect world</button><button id="sf_real" aria-pressed="false">All as measured</button><button id="sf_one">Sun only</button><button id="sf_light" aria-pressed="true">Light in every ball</button></div>
` + DIALS.map(([k,n]) => `<div class="r"><label>${n} <span><span id="sf_o_${k}">0.00</span> <input data-dial="${k}" type="range" min="0" max="1" step="0.01" value="0"></span></label></div>`).join('') + `
<div class="r" id="sf_zoom"><span style="color:var(--dim,#8a9aab)">Zoom</span><button data-f="-1" aria-pressed="true">Field</button><button data-f="0">Sun</button><button data-f="1">Mercury</button><button data-f="2">Venus</button><button data-f="3">Earth</button><button data-f="4">Mars</button></div><div class="row"><span>day</span><b id="sf_day"></b></div><details open><summary>The bodies, as measured</summary><div id="sf_bod"></div></details><div id="sf_tab"></div><details open><summary>The books</summary><div id="sf_rows"></div></details></div>`);
const $ = id => document.getElementById(id);
function setDial(k, v){ D[k] = v; const i = document.querySelector('#tb input[data-dial="' + k + '"]'); i.value = v; $('sf_o_' + k).textContent = v.toFixed(2); if(k === 'field') applyField(); wob = null;
  const all0 = Object.values(D).every(x => x === 0), all1 = Object.values(D).every(x => x === 1); $('sf_perfect').setAttribute('aria-pressed', all0); $('sf_real').setAttribute('aria-pressed', all1); }
document.querySelectorAll('#tb input[data-dial]').forEach(i => i.addEventListener('input', () => setDial(i.dataset.dial, +i.value)));
$('sf_perfect').addEventListener('click', () => DIALS.forEach(([k]) => setDial(k, 0))); $('sf_real').addEventListener('click', () => DIALS.forEach(([k]) => setDial(k, 1)));
$('sf_one').addEventListener('click', () => { X.on = !X.on; $('sf_one').textContent = X.on ? 'Sun only' : 'The whole field'; });
document.querySelectorAll('#sf_zoom button').forEach(b => b.addEventListener('click', () => { X.focus = +b.dataset.f; document.querySelectorAll('#sf_zoom button').forEach(q => q.setAttribute('aria-pressed', q === b)); }));
$('sf_light').addEventListener('click', () => { X.lightIn = X.lightIn === 'all' ? 'sun' : 'all'; $('sf_light').setAttribute('aria-pressed', X.lightIn === 'all'); });
const row = (a, b, g) => `<div class="row"><span>${a}</span><b>${b}</b></div>` + (g ? `<div class="g">${g}</div>` : '');
function rows(){ if(!BOOK) return; $('sf_day').textContent = fmt(H.tau()*DAYS, 1);
  let bt = '<table><tr><th>body</th><th>radius km</th><th>flattening</th><th>dipole G·R³</th><th>tilt</th><th>edge calc</th><th>meas.</th></tr>';
  BODY.forEach((b, k) => { bt += `<tr><td>${b.name}</td><td>${b.Req}</td><td>${b.f}</td><td>${b.dipG || 'none'}</td><td>${b.dipG ? b.tilt + '°' : '—'}</td><td>${Number.isFinite(BG[k].r0) ? fmt(BG[k].r0, 2) + ' R' : '—'}</td><td>${b.mp ? b.mp + ' R' : '—'}</td></tr>`; });
  $('sf_bod').innerHTML = bt + '</table><div class="g">Radius, flattening, dipole, tilt: NASA fact sheets. Field edge computed from pressure balance, r₀/R = (2B²/(μ₀P))^(1/6), with the ram pressure MESSENGER measured at Mercury (14.3 nPa) scaled by the inverse square of the present distance; measured: MESSENGER 1.45 R for Mercury, typical 10 R for the Earth. Venus and Mars: no magnetic field listed, none drawn. In each ball the body\u2019s surface sits at half the ball\u2019s radius and a distance r is drawn at (3r/R − 1)/(3r/R + 1); ball sizes are on a logarithmic scale of the measured radii. Field lines are those of a dipole, cut at the computed edge (their squeezing on the sunward side is not modelled).</div>';
  let t = '<table><tr><th>ball</th><th>distance</th><th>step in</th><th>Γ</th><th>T</th><th>period d</th><th>light min</th></tr>';
  PL.forEach((p, b) => { const stepIn = b === 0 ? p.d : p.d - PL[b-1].d, G = Math.tanh(Math.abs(stepIn)/2); t += `<tr><td>${p.name}</td><td>${fmt(p.d,3)}</td><td>${fmt(stepIn,3)}</td><td>${fmt(G,3)}</td><td>${fmt(1-G*G,3)}</td><td>${fmt(p.T,1)}</td><td>${fmt(p.lightSec/60,2)}</td></tr>`; }); $('sf_tab').innerHTML = t + '</table><div class="g">distance and step are lengths in the ball (logarithms of distance ratios); light minutes are the measured ones, for reference</div>';
  let h = '<table><tr><th>ball</th><th>light through it</th><th>straight rays</th><th>open-ball formula</th><th>swing so far</th></tr>';
  PL.forEach((p, b) => { h += `<tr><td>${p.name}</td><td>${sci(BOOK.share[b])}</td><td>${sci(BOOK.straight[b])}</td><td>${sci(BOOK.free[b])}</td><td>${wob ? sci(wob[b][1] - wob[b][0]) : '—'}</td></tr>`; }); h += '</table>';
  h += `<div class="g">share of all the light the Sun sends out that passes through each ball (reach ${fmt(RAD,3)}): a bundle of ${NB} rays aimed at the ball, traced through the faces by the step law; the same bundle kept straight; and the solid-angle formula for an open ball. Swing is the largest minus the smallest traced share since the dials last moved.</div>`;
  h += row('Sun’s ledger: reached the rim + still inside + dropped small', fmt(BOOK.rim,4) + ' + ' + fmt(BOOK.cut,4) + ' + ' + fmt(BOOK.small,4), 'sums to 1; residual ' + sci(BOOK.ledger));
  h += row('flux balance at every face; a sin²θ across every crossing', sci(BOOK.flux) + ';  ' + sci(BOOK.cons));
  $('sf_rows').innerHTML = h; }
setInterval(rows, 300);
window.__sf = { BG, BODY, sizeOf, D, X, setDial, get PL(){ return PL; }, get BOOK(){ return BOOK; }, get wob(){ return wob; }, rows };
})();
