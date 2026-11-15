/* SCRIPT: LH-MIXER-V1
   Light at the Hypersurface, Mixer v1 — Jeromie Beasley — 15 Nov 2026 — AI-assisted.
   One ball, one feed operator (the peel step), one clock. Every component is part of one shared object (WORLD);
   an eye is a camera, an emphasis and a readout on that same moving object. Built on 3D Mixer Parts v1 and LH-MATH-V1. */
(function(){
"use strict";
const M = window.Mixer3D, T = M.T, L = window.LH, PI = Math.PI, RB = 2.6, C = L.C;
const V3 = (x,y,z) => new T.Vector3(x,y,z);
const fmt = (x,n=4) => Number.isFinite(x) ? x.toFixed(n) : '—';
const sci = x => Number.isFinite(x) ? x.toExponential(1) : '—';
const deg = x => fmt(x*180/PI, 3) + '°';
const cfmt = (z,n=4) => fmt(z[0],n) + (z[1] < 0 ? ' − ' : ' + ') + fmt(Math.abs(z[1]),n) + 'i';
const AXN = ['I','J','K'], AXC = [0xff8d7c, 0x63d3ff, 0xf2c14e], AXV = [[1,0.55,0.49],[0.39,0.83,1],[0.95,0.76,0.31]];
const GEN = ['+I','−I','+J','−J','+K','−K'];
const AMBER = 0xffb347, AMBV = [1,0.7,0.28];
const toBall = p => { const k = RB/(1+p[0]); return V3(p[1]*k, p[3]*k, -p[2]*k); };
const w3 = u => V3(u[0], u[2], -u[1]);
const still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ---------------- the clock and the live parameters ---------------- */
const CLOCK = { tau:0, playing:!still, speed:1, dtFixed:1/60 };
const PP = Object.assign({}, L.DEF);
const HYP = { shown:true };
let ST = L.initState(), S = null, AUD = null, SELF = null, stepOnce = false;
const ELL0 = (() => { const d = [0.25,-0.35,0.9], n = Math.hypot(...d); return [1, d[0]/n, d[1]/n, d[2]/n]; })();

/* ---------------- emphasis: one object, weights per eye ---------------- */
const COMPS = ['rim','tree','balls','faces','cross','rays','stack','press','loop','rimf','hyp'];
const W = {}, WT = {}; COMPS.forEach(c => { W[c] = 1; WT[c] = 1; });
const REG = []; /* [material, comp, base] */
const reg = (mat, comp, base) => { mat.transparent = true; REG.push([mat, comp, base == null ? (mat.opacity == null ? 1 : mat.opacity) : base]); return mat; };
function regObj(o, comp, base){ o.traverse(x => { if(x.material) reg(x.material, comp, base == null ? x.material.opacity : base); }); return o; }
function applyEmph(dt){ const k = Math.min(1, dt*4); COMPS.forEach(c => { const tgt = WT[c]*(c === 'hyp' && !HYP.shown ? 0 : 1); W[c] += (tgt - W[c])*k; if(Math.abs(W[c]-tgt) < 1e-3) W[c] = tgt; });
  REG.forEach(([m,c,b]) => { m.opacity = b*W[c]; m.visible = W[c] > 0.01; }); }

/* ---------------- shared drawing helpers ---------------- */
function lineSegs(maxV, comp, base){ const g = new T.BufferGeometry(); g.setAttribute('position', new T.BufferAttribute(new Float32Array(maxV*3),3)); g.setAttribute('color', new T.BufferAttribute(new Float32Array(maxV*3),3)); g.setDrawRange(0,0);
  const l = new T.LineSegments(g, reg(new T.LineBasicMaterial({vertexColors:true, transparent:true, opacity:base, blending:T.AdditiveBlending, depthWrite:false}), comp, base)); l.frustumCulled = false; l.userData.n = 0; return l; }
function segPush(l, a, b, c){ const u = l.userData, g = l.geometry, P = g.attributes.position, Cc = g.attributes.color; if(u.n + 2 > P.count) return;
  P.setXYZ(u.n, a.x,a.y,a.z); Cc.setXYZ(u.n, c[0],c[1],c[2]); P.setXYZ(u.n+1, b.x,b.y,b.z); Cc.setXYZ(u.n+1, c[0],c[1],c[2]); u.n += 2; }
function segDone(l){ l.geometry.setDrawRange(0, l.userData.n); l.geometry.attributes.position.needsUpdate = l.geometry.attributes.color.needsUpdate = true; l.userData.n = 0; }
function pts(n, size, comp, base, map){ const p = M.points(n, size); if(map){ p.material.map = map; } reg(p.material, comp, base == null ? 1 : base); p.userData.n = 0; return p; }
function ptPush(p, P, c){ const u = p.userData; if(u.n >= p.geometry.attributes.position.count) return; M.setPt(p, u.n++, P, c); }
function ptDone(p){ const a = p.geometry.attributes; for(let i=p.userData.n;i<a.position.count;i++){ a.color.setXYZ(i,0,0,0); a.position.setXYZ(i,0,0,0); } p.geometry.setDrawRange(0, a.position.count); M.flush(p); p.userData.n = 0; }
const ringTex = (() => { const c = document.createElement('canvas'); c.width = c.height = 64; const x = c.getContext('2d'); x.strokeStyle = 'rgba(255,255,255,1)'; x.lineWidth = 7; x.beginPath(); x.arc(32,32,22,0,2*PI); x.stroke(); return new T.CanvasTexture(c); })();
function dashed(color, comp, base){ const m = new T.LineDashedMaterial({color, dashSize:0.07, gapSize:0.06, transparent:true, opacity:base}); reg(m, comp, base);
  const l = new T.Line(new T.BufferGeometry().setFromPoints([V3(),V3()]), m); l.frustumCulled = false; return l; }
function setDashed(l, P){ l.geometry.dispose(); l.geometry = new T.BufferGeometry().setFromPoints(P.length > 1 ? P : [V3(),V3()]); l.computeLineDistances(); }
function solid(color, comp, base){ const l = M.line([V3(),V3()], color, base); reg(l.material, comp, base); return l; }
function geoPts(X, v, s0, s1, n){ const out = []; for(let j=0;j<=n;j++){ const s = s0 + (s1-s0)*j/n; out.push(toBall(L.geoPoint(X,v,s))); } return out; }
function geoBetween(p, q, n){ const d = Math.acosh(Math.max(1, L.mink(p,q))), out = []; for(let j=0;j<=n;j++){ const t = j/n; if(d < 1e-9){ out.push(toBall(p)); continue; }
  const a = Math.sinh((1-t)*d)/Math.sinh(d), b = Math.sinh(t*d)/Math.sinh(d); out.push(toBall(L.lin(a,p,b,q))); } return out; }
/* the face perpendicular to u at hyperbolic distance h: a spherical cap; geometry updated in place */
const NT = 14, NP = 40;
function capParams(u, h){ const rho = Math.tanh(h/2), c = (1+rho*rho)/(2*rho), R = (1-rho*rho)/(2*rho), tmax = Math.atan(1/R), a = w3(u).normalize(),
  e1 = (Math.abs(a.y) < 0.9 ? V3(0,1,0) : V3(1,0,0)).cross(a).normalize(), e2 = a.clone().cross(e1); return { rho, c, R, tmax, a, e1, e2 }; }
const capPoint = (q, th, ph) => q.a.clone().multiplyScalar(q.c - q.R*Math.cos(th)).addScaledVector(q.e1, q.R*Math.sin(th)*Math.cos(ph)).addScaledVector(q.e2, q.R*Math.sin(th)*Math.sin(ph)).multiplyScalar(RB);
function makeCap(color, comp, base){ const n = (NT+1)*(NP+1), g = new T.BufferGeometry(); g.setAttribute('position', new T.BufferAttribute(new Float32Array(n*3),3)); g.setAttribute('color', new T.BufferAttribute(new Float32Array(n*3),3));
  const idx = []; for(let i=0;i<NT;i++) for(let j=0;j<NP;j++){ const k = i*(NP+1)+j; idx.push(k, k+1, k+NP+1, k+1, k+NP+2, k+NP+1); } g.setIndex(idx);
  const mat = reg(new T.MeshBasicMaterial({vertexColors:true, transparent:true, opacity:base, side:T.DoubleSide, depthWrite:false, blending:T.AdditiveBlending}), comp, base);
  const mesh = new T.Mesh(g, mat); mesh.frustumCulled = false; const edge = solid(color, comp, 0.75); const grp = new T.Group(); grp.add(mesh, edge); grp.userData = { mesh, edge, color:new T.Color(color) }; return grp; }
function setCap(grp, u, h, colFn){ const q = capParams(u, h), P = grp.userData.mesh.geometry.attributes.position, Cc = grp.userData.mesh.geometry.attributes.color, edge = [];
  for(let i=0;i<=NT;i++){ const th = q.tmax*i/NT; for(let j=0;j<=NP;j++){ const ph = 2*PI*j/NP, p = capPoint(q, th, ph), k = i*(NP+1)+j; P.setXYZ(k, p.x,p.y,p.z); const c = colFn(p); Cc.setXYZ(k, c[0],c[1],c[2]); if(i === NT) edge.push(p); } }
  P.needsUpdate = Cc.needsUpdate = true; grp.userData.mesh.geometry.computeBoundingSphere(); M.setLine(grp.userData.edge, edge); grp.userData.q = q; return q; }
function rimCircle(u, cosA, n){ const a = w3(u).normalize(), e1 = (Math.abs(a.y) < 0.9 ? V3(0,1,0) : V3(1,0,0)).cross(a).normalize(), e2 = a.clone().cross(e1), s = Math.sqrt(Math.max(0,1-cosA*cosA)), out = [];
  for(let i=0;i<=n;i++){ const t = 2*PI*i/n; out.push(a.clone().multiplyScalar(cosA).addScaledVector(e1, s*Math.cos(t)).addScaledVector(e2, s*Math.sin(t)).multiplyScalar(RB*1.002)); } return out; }

/* ---------------- WORLD: the one object ---------------- */
const WORLD = new T.Group();
const G = {}; COMPS.forEach(c => { G[c] = new T.Group(); WORLD.add(G[c]); });
/* rim: the ground */
(function(){ const sh = M.shell(RB, 0x63d3ff, 0.035); reg(sh.material, 'rim', 0.035); G.rim.add(sh);
  for(let k=0;k<3;k++){ const p = []; for(let i=0;i<=128;i++){ const a = 2*PI*i/128, c = RB*Math.cos(a), s = RB*Math.sin(a); p.push(k===0 ? V3(c,0,s) : k===1 ? V3(c,s,0) : V3(0,c,s)); } const l = M.line(p, 0x63d3ff, k===0 ? 0.5 : 0.18); reg(l.material, 'rim'); G.rim.add(l); }
  const lb = M.label('rim: the ground', '#63d3ff', 0.3); lb.position.set(-RB*0.74, 0.12, RB*0.74); reg(lb.material, 'rim', 1); G.rim.add(lb); })();
/* tree to depth 3 */
const TREE = (() => { const words = []; (function walk(w, d){ if(d === 3) return; for(let k=0;k<6;k++){ if(w.length && (w[w.length-1]^1) === k) continue; const w2 = w.concat([k]); words.push(w2); walk(w2, d+1); } })([], 0);
  const l = lineSegs(words.length*6*2, 'tree', 0.5); G.tree.add(l); return { words, l }; })();
/* balls */
const BALLS = (() => { const c = new T.Mesh(new T.SphereGeometry(0.11, 24, 16), new T.MeshStandardMaterial({color:0xffffff, emissive:0xffffff, emissiveIntensity:0.5})); regObj(c, 'balls', 1); G.balls.add(c);
  const lo = M.label('O  centre', '#dfe7ef', 0.26); lo.position.set(0.05, -0.28, 0); reg(lo.material, 'balls', 1); G.balls.add(lo);
  const orbs = [0,1,2].map(a => { const b = new T.Mesh(new T.SphereGeometry(1, 24, 16), new T.MeshStandardMaterial({color:AXC[a], emissive:AXC[a], emissiveIntensity:0.45, roughness:0.4})); regObj(b, 'balls', 1); G.balls.add(b); return b; });
  return { orbs, labels:[null,null,null], t:9 }; })();
/* the six faces of the centre cell, and the deeper faces along each + arm */
const FACES = [0,1,2,3,4,5].map(k => { const f = makeCap(AXC[k>>1], 'faces', 0.5); G.faces.add(f); return f; });
const DEEP = [0,1,2].map(a => [1,2,3,4,5].map(() => { const f = makeCap(AXC[a], 'stack', 0.14); G.stack.add(f); return f; }));
/* crossings and gaps */
const CROSS = [0,1,2].map(() => { const grp = new T.Group(); G.cross.add(grp); return grp; });
const GAPS = [0,1,2].map(() => { const l = solid(0xffffff, 'cross', 0.9); G.cross.add(l); return l; });
/* rays and markers */
const RAYL = lineSegs(60000, 'rays', 0.85); G.rays.add(RAYL);
const RAYP = pts(9000, 0.07, 'rays', 1); G.rays.add(RAYP);
const HITP = pts(800, 0.16, 'rays', 1); G.rays.add(HITP);
/* stack streams, composed point, echo circle */
const STKP = pts(6000, 0.075, 'stack', 1); G.stack.add(STKP);
const RPT = pts(2, 0.34, 'stack', 1); G.stack.add(RPT);
const XPT = pts(1, 0.3, 'stack', 1, ringTex); G.stack.add(XPT);
const ECHO = solid(0xffffff, 'stack', 0.75); G.stack.add(ECHO);
/* pressure arrows and the record rings */
const PRSP = pts(2400, 0.085, 'press', 1); G.press.add(PRSP);
const RECP = pts(3*6*48, 0.075, 'press', 1); G.press.add(RECP);
/* the square: path, orbit, moving centre, frames, carried direction */
const LOOPL = solid(0xf2c14e, 'loop', 1); G.loop.add(LOOPL);
const ORBP = pts(48, 0.1, 'loop', 0.8); G.loop.add(ORBP);
const MOVP = pts(1, 0.34, 'loop', 1); G.loop.add(MOVP);
const FRAMES = [0,1,2].map(i => { const s = solid(AXC[i], 'loop', 1), d = dashed(AXC[i], 'loop', 0.8); G.loop.add(s, d); return { s, d }; });
const CARRY = M.trail(220, 0.13); reg(CARRY.material, 'loop', 1); G.loop.add(CARRY);
const CARRYP = pts(1, 0.36, 'loop', 1); G.loop.add(CARRYP);
/* rim field, caps, face shadows */
const RIMDIRS = L.sphereSample(1600);
const RIMP = pts(RIMDIRS.length, 0.06, 'rimf', 0.9); G.rimf.add(RIMP);
for(let k=0;k<6;k++){ const l = M.line(rimCircle(L.genU(k), Math.SQRT1_2, 96), 0xdfe7ef, 0.55); reg(l.material, 'rimf', 0.55); G.rimf.add(l); }
const SHADOW = [0,1,2,3,4,5].map(k => { const l = solid(AXC[k>>1], 'rimf', 0.95); G.rimf.add(l); return l; });
/* hypothesis layer: amber, dashed or hollow */
const HYPX = pts(1200, 0.07, 'hyp', 1); G.hyp.add(HYPX);
const HYPY = pts(1200, 0.12, 'hyp', 1, ringTex); G.hyp.add(HYPY);
const OCC = [0,1,2].map(() => { const l = dashed(AMBER, 'hyp', 1); G.hyp.add(l); return l; });
const GAPH = [0,1,2].map(() => { const l = dashed(AMBER, 'hyp', 1); G.hyp.add(l); return l; });
(function(){ const a = M.label('hypothesis: the sea of electrons is the ground and keeps the record', '#ffb347', 0.15); a.position.set(0, -RB*1.1, 0); reg(a.material, 'hyp', 1); G.hyp.add(a);
  const b = M.label('hypothesis: the walls of each layer are electrons', '#ffb347', 0.15); b.position.set(RB*0.95, -RB*0.25, 0); reg(b.material, 'hyp', 1); G.hyp.add(b); })();

/* ---------------- update: everything from one state S ---------------- */
function admitFace(word){ return L.nodeAdmittance(word, S); }
function updateTree(){ const l = TREE.l, cc = AXC.map(c => new T.Color(c)), gens = [0,1,2,3,4,5].map(k => L.boost(L.genU(k), S.r[k>>1]));
  const cache = new Map([['', L.I4()]]);
  for(const w of TREE.words){ const pk = w.slice(0,-1).join(','), k = w[w.length-1], Mp = cache.get(pk), Mw = L.mm(Mp, gens[k]); cache.set(w.join(','), Mw);
    const g = geoBetween(L.mv(Mp, L.O4), L.mv(Mw, L.O4), 6), c = cc[k>>1], f = 0.55*Math.pow(0.6, w.length-1);
    for(let j=0;j<6;j++) segPush(l, g[j], g[j+1], [c.r*f, c.g*f, c.b*f]); } segDone(l); }
function updateBalls(dt){ for(let a=0;a<3;a++){ const p = toBall(L.mv(L.boost(L.AX[a], S.r[a]), L.O4)), f = 1 - p.lengthSq()/(RB*RB), o = BALLS.orbs[a]; o.position.copy(p); o.scale.setScalar(0.05 + 0.16*f); }
  BALLS.t += dt; if(BALLS.t > 0.5){ BALLS.t = 0; for(let a=0;a<3;a++){ if(BALLS.labels[a]){ G.balls.remove(BALLS.labels[a]); const i = REG.findIndex(r => r[0] === BALLS.labels[a].material); if(i >= 0) REG.splice(i,1); BALLS.labels[a].material.map.dispose(); }
    const lb = M.label(AXN[a] + '   z ' + fmt(S.z[a],2), '#' + AXC[a].toString(16).padStart(6,'0'), 0.28); reg(lb.material, 'balls', 1); lb.material.opacity = W.balls; G.balls.add(lb); BALLS.labels[a] = lb; } }
  for(let a=0;a<3;a++) if(BALLS.labels[a]) BALLS.labels[a].position.copy(BALLS.orbs[a].position).add(V3(0, 0.3, 0)); }
function updateFaces(){ const out = []; for(let k=0;k<6;k++){ const a = k>>1, u = L.genU(k), h = S.h[a], z = S.z[a], R = S.Rf[a], col = new T.Color(AXC[a]), ax = w3(u).normalize();
    const crit = PP.orient > 0 ? 1/z : 2;  /* rays from the centre cross while cosh h · sin ψ < 1/z */
    out.push(setCap(FACES[k], u, h, p => { const cp = Math.max(-1, Math.min(1, p.clone().normalize().dot(ax))), sp = Math.sqrt(1-cp*cp), win = Math.cosh(h)*sp < crit;
      const f = win ? 0.1 + 0.3*R : 0.018 + 0.03*R; return win ? [col.r*f, col.g*f, col.b*f] : [0.95*f, 0.4*f, 0.7*f]; })); }
  for(let a=0;a<3;a++){ const col = new T.Color(AXC[a]); for(let k=1;k<=5;k++){ const f = DEEP[a][k-1]; if(k >= S.depth){ f.visible = false; continue; } f.visible = true;
    setCap(f, L.AX[a], (k+0.5)*S.r[a], () => [col.r*(0.12+0.3*S.Rf[a]), col.g*(0.12+0.3*S.Rf[a]), col.b*(0.12+0.3*S.Rf[a])]); } }
  return out; }
function capSphere(q){ return { centre:q.a.clone().multiplyScalar(q.c), R:q.R }; }
function updateCross(Q){ L.PAIRS.forEach(([a,b], i) => { const grp = CROSS[i]; while(grp.children.length){ const c = grp.children[0]; grp.remove(c); c.geometry.dispose(); const j = REG.findIndex(r => r[0] === c.material); if(j >= 0) REG.splice(j,1); c.material.dispose(); }
    const p = S.pairs[i], A = capSphere(Q[2*a]), B = capSphere(Q[2*b]);
    if(p.over){ const d = A.centre.distanceTo(B.centre), x = (d*d + A.R*A.R - B.R*B.R)/(2*d), rr = A.R*A.R - x*x; GAPS[i].visible = false; setDashed(GAPH[i], []);
      if(rr > 0){ const n = B.centre.clone().sub(A.centre).normalize(), c0 = A.centre.clone().addScaledVector(n, x), e1 = (Math.abs(n.y) < 0.9 ? V3(0,1,0) : V3(1,0,0)).cross(n).normalize(), e2 = n.clone().cross(e1), r = Math.sqrt(rr);
        let cur = []; const segs = []; for(let s=0;s<=240;s++){ const t = 2*PI*s/240, q = c0.clone().addScaledVector(e1, r*Math.cos(t)).addScaledVector(e2, r*Math.sin(t)); if(q.lengthSq() <= 1.0001) cur.push(q.multiplyScalar(RB)); else if(cur.length){ segs.push(cur); cur = []; } }
        if(cur.length) segs.push(cur); segs.forEach(sg => { const l = M.line(sg, 0xffffff, 1); reg(l.material, 'cross', 1); l.material.opacity = W.cross; grp.add(l); }); } }
    else { const Na = L.facePlane(L.I4(), L.AX[a], S.h[a]), Nb = L.facePlane(L.I4(), L.AX[b], S.h[b]), g = L.mink(Na,Nb), sq = Math.sqrt(g*g-1);
      let fa = L.lin(1/sq, Nb, g/sq, Na), fb = L.lin(1/sq, Na, g/sq, Nb); if(fa[0] < 0) fa = fa.map(v=>-v); if(fb[0] < 0) fb = fb.map(v=>-v);
      const P = geoBetween(fa, fb, 24); GAPS[i].visible = true; M.setLine(GAPS[i], P); setDashed(GAPH[i], P.map(q => q.clone().multiplyScalar(1.004))); } }); }
function rayColour(sg){ const lv = Math.min(1, sg.word.length/4); return M.colour.ramp(0.15 + 0.7*lv); }
function updateRays(tau){ let tag = null; const v0 = 0.55;
  for(const sg of S.segs){ const isTag = sg.ray === PP.tag, f = Math.pow(sg.flux, 0.5), c = isTag ? [1,0.8,0.35] : rayColour(sg), k = isTag ? 1.25 : 0.75;
    const n = Math.max(4, Math.min(28, Math.ceil(sg.s*7))), P = geoPts(sg.X, sg.v, 0, sg.s, n); for(let j=0;j<n;j++) segPush(RAYL, P[j], P[j+1], c.map(v => v*f*k));
    const sp = 0.2, vel = v0*Math.min(6, 1/sg.Y), off = ((vel*tau) % sp + sp) % sp;
    for(let s = off; s < sg.s; s += sp) ptPush(RAYP, toBall(L.geoPoint(sg.X, sg.v, s)), c.map(v => v*Math.min(1, 0.25 + sg.flux)*(isTag ? 1.2 : 1)));
    if(sg.end === 'face'){ ptPush(HITP, toBall(sg.hit), [1,1,1].map(v => v*Math.min(1, 0.2 + 0.9*sg.flux*sg.sp.R)));
      if(sg.sp.total){ const m = L.mink(sg.tin, sg.N), dir = L.lin(Math.sign(-m), sg.N, 0, sg.N), l = Math.min(0.6, sg.sp.depth);
        for(let j=1;j<=6;j++){ const x = l*j/3; ptPush(RAYP, toBall(L.geoPoint(sg.hit, dir, x)), [1,0.45,0.7].map(v => v*sg.flux*Math.exp(-x/sg.sp.depth))); } }
      if(isTag && sg.depth === 0) tag = sg; } }
  segDone(RAYL); ptDone(RAYP); ptDone(HITP); return tag; }
const axisPoint = (a, d, off) => w3(L.AX[a]).multiplyScalar(RB*Math.tanh(Math.max(0,d)/2)).add(off);
function updateStack(tau){ for(let a=0;a<3;a++){ const st = S.stacks[a], r = S.r[a], D = S.depth, sel = a === PP.arm ? 1 : 0.45;
    const side = w3(L.AX[(a+1)%3]).multiplyScalar(0.045);
    for(let k=0;k<=D;k++){ const d0 = k === 0 ? 0.05 : (k-0.5)*r, d1 = k === D ? Math.max(d0+0.4, 4.2) : (k+0.5)*r, Yk = st.Ys[k][0], ap = st.amps[k].ap, am = st.amps[k].am,
      fp = Yk*C.abs2(ap), fm = Yk*C.abs2(am), vel = 0.5*Math.min(5, 1/Yk), sp = 0.12, off = ((vel*tau) % sp + sp) % sp;
      for(let d = d0 + off; d < d1; d += sp) ptPush(STKP, axisPoint(a, d, side), AXV[a].map(v => v*sel*Math.min(1, 0.15 + Math.sqrt(fp))));
      for(let d = d1 - off; d > d0; d -= sp) ptPush(STKP, axisPoint(a, d, side.clone().negate()), [1,0.45,0.7].map(v => v*sel*Math.min(1, 0.1 + Math.sqrt(fm)))); } }
  ptDone(STKP);
  /* composed reflection on the first face of the selected arm, the cap used as the Smith disk */
  const a = PP.arm, q = capParams(L.AX[a], S.h[a]), st = S.stacks[a], onCap = z => { const m = Math.min(1, C.abs(z)); return capPoint(q, m*q.tmax*0.999, C.arg(z)); };
  ptPush(RPT, onCap(st.r), [1,1,1]); ptPush(RPT, capPoint(q, 0, 0), [0.35,0.35,0.35]); ptDone(RPT);
  ptPush(XPT, onCap(st.xNow), AXV[a]); ptDone(XPT);
  const ec = st.echo, pts2 = []; for(let i=0;i<=180;i++){ const t = 2*PI*i/180, z = C.add(ec.xc, [C.abs(ec.xc)*Math.cos(t), C.abs(ec.xc)*Math.sin(t)]); if(C.abs(z) <= 1) pts2.push(onCap(z)); else if(pts2.length && pts2[pts2.length-1] !== null) pts2.push(null); }
  const seg = []; let cur = []; pts2.forEach(p => { if(p) cur.push(p); else if(cur.length){ seg.push(cur); cur = []; } }); if(cur.length) seg.push(cur); seg.sort((u,v) => v.length - u.length); M.setLine(ECHO, seg[0] && seg[0].length > 1 ? seg[0] : [V3(),V3()]); }
function updatePress(){ for(let a=0;a<3;a++){ const st = S.stacks[a], r = S.r[a];
    for(let k=0;k<S.depth;k++){ const d = (k+0.5)*r, base = axisPoint(a, d, V3()), dir = w3(L.AX[a]).normalize(), len = 0.55*Math.min(2, Math.abs(st.push[k])), sg = Math.sign(st.push[k]) || 1;
      for(let j=0;j<10;j++){ const x = len*j/9; ptPush(PRSP, base.clone().addScaledVector(dir, sg*x).add(w3(L.AX[(a+2)%3]).multiplyScalar(0.03)), [1,0.9,0.6].map(v => v*(1 - 0.6*j/9))); }
      const Kk = ST.K[a][k], frac = (Kk/5) - Math.floor(Kk/5), ang = (6 + 3.5*k)*PI/180, ring = rimCircle(L.AX[a], Math.cos(ang), 48);
      for(let j=0;j<48;j++){ const lit = j/48 < frac; ptPush(RECP, ring[j], lit ? [1,0.85,0.45] : [0.18,0.16,0.12]); } } }
  ptDone(PRSP); ptDone(RECP); }
function updateLoop(tau){ const pi = PP.pair, p = S.pairs[pi], ua = L.AX[p.a], ub = L.AX[p.b], ra = S.r[p.a], rb = S.r[p.b];
  const st = [[ua,ra],[ub,rb],[ua.map(v=>-v),ra],[ub.map(v=>-v),rb]]; let Mc = L.I4(); const corners = [L.O4]; st.forEach(s => { Mc = L.mm(Mc, L.boost(s[0], s[1])); corners.push(L.mv(Mc, L.O4)); });
  let path = []; for(let i=0;i<4;i++) path = path.concat(geoBetween(corners[i], corners[i+1], 20)); M.setLine(LOOPL, path);
  let x = L.O4; for(let m=1;m<=40;m++){ x = L.mv(p.W4, x); const s = Math.sqrt(Math.max(1e-300, L.mink(x,x))); x = x.map(v => v/s); if(!(x[0] < 1e6)) break; ptPush(ORBP, toBall(x), [0.8,0.8,0.8]); } ptDone(ORBP);
  const f = (tau/L.T_LOOP) - Math.floor(tau/L.T_LOOP + 1e-12), Mf = L.mm(ST.Wacc, L.partialSquare(S, pi, f)), xc = L.mv(Mf, L.O4);
  if(xc[0] < 1e6) ptPush(MOVP, toBall(xc), [1,0.76,0.3]); ptDone(MOVP);
  const ell = L.mv(Mf, ELL0), dn = V3(ell[1]/ell[0], ell[3]/ell[0], -ell[2]/ell[0]).normalize().multiplyScalar(RB*1.005);
  M.pushTrail(CARRY, dn, [1,0.9,0.5]); ptPush(CARRYP, dn, [1,1,0.8]); ptDone(CARRYP);
  /* frames at the corner reached by the two steps: solid = carried, dashed = pure boost */
  const th = p.thomas, P0 = L.mv(th.Lam, L.O4);
  for(let i=0;i<3;i++){ const e = [0,0,0,0]; e[i+1] = 1; const v1 = L.mv(th.Lam, e), v2 = L.mv(th.L, e);
    M.setLine(FRAMES[i].s, geoPts(P0, v1, 0, 0.5, 8)); setDashed(FRAMES[i].d, geoPts(P0, v2, 0, 0.5, 8)); }
  return { ell, xc }; }
function updateRim(tau){ const cyc = 7, a = ((Math.floor(tau/cyc) % 3) + 3) % 3, ph = (((tau % cyc) + cyc) % cyc)/cyc, f = 0.5 - 0.5*Math.cos(2*PI*ph), r = f*S.r[a], u = L.AX[a]; let inside = 0;
  for(const n of RIMDIRS){ const b = L.boostNull(n, u, r), q = V3(b.n[0], b.n[2], -b.n[1]).multiplyScalar(RB*0.996), x = S.r[a] > 0 ? Math.log(b.f)/S.r[a] : 0;
    let ins = false; for(let k=0;k<6;k++) if(L.inCap(b.n, L.genU(k))) ins = true; if(ins) inside++;
    const c = M.colour.ramp(0.5 + 0.5*x); ptPush(RIMP, q, c.map(v => v*0.8)); } ptDone(RIMP);
  for(let k=0;k<6;k++) M.setLine(SHADOW[k], rimCircle(L.genU(k), S.shadow[k>>1], 96));
  return { arm:a, f, r, share:inside/RIMDIRS.length }; }
function updateHyp(){ for(let a=0;a<3;a++){ const r = S.r[a];
    for(let k=0;k<S.depth;k++){ const sx = ST.stocks[a][k][0], sy = ST.stocks[a][k][1], nx = Math.min(40, Math.round(sx*12)), ny = Math.min(40, Math.round(sy*12)), dir = w3(L.AX[a]).normalize(),
      e1 = w3(L.AX[(a+1)%3]), e2 = w3(L.AX[(a+2)%3]), base = axisPoint(a, (k+0.5)*r, V3());
      for(let j=0;j<nx;j++){ const t = j*2.39996, rr = 0.06 + 0.012*j; ptPush(HYPX, base.clone().addScaledVector(dir, -0.06 - 0.004*j).addScaledVector(e1, rr*Math.cos(t)).addScaledVector(e2, rr*Math.sin(t)), AMBV); }
      for(let j=0;j<ny;j++){ const t = j*2.39996 + 1, rr = 0.05 + 0.011*j; ptPush(HYPY, base.clone().addScaledVector(e1, rr*Math.cos(t)).addScaledVector(e2, rr*Math.sin(t)), AMBV); } }
    const q = capParams(L.AX[a], S.h[a]), arc = []; const n = Math.max(2, Math.round(96*S.Cocc[a])); for(let j=0;j<=n;j++) arc.push(capPoint(q, q.tmax*0.86, 2*PI*S.Cocc[a]*j/n)); setDashed(OCC[a], arc); }
  ptDone(HYPX); ptDone(HYPY); }
function update(dt){ if(CLOCK.playing || stepOnce){ const d = stepOnce ? CLOCK.dtFixed*CLOCK.speed : Math.max(0, Math.min(0.05, dt))*CLOCK.speed;  /* the first frame can report a negative dt */ L.advance(ST, PP, CLOCK.tau, d); CLOCK.tau += d; stepOnce = false; }
  S = L.feed(PP, CLOCK.tau);
  /* the composed stack also needs ρ seen from inside layer 1 and the echo circle of the first face */
  S.stacks.forEach(st => { const D = st.G.length; let rho = st.G[D-1]; for(let k=D-2;k>=1;k--) rho = L.oplus(st.G[k], C.mul(rho, C.exp([0, 2*st.phis[k+1]])));
    st.xNow = D > 1 ? C.mul(rho, C.exp([0, 2*st.phis[1]])) : [0,0]; st.echo = L.echoCircle(st.G[0]); st.bounce = L.bounceSum(st.G[0], st.xNow, 12); });
  AUD = L.audit(S);
  updateTree(); updateBalls(dt); const Q = updateFaces(); updateCross(Q); const tag = updateRays(CLOCK.tau); updateStack(CLOCK.tau); updatePress();
  const lp = updateLoop(CLOCK.tau), rm = updateRim(CLOCK.tau); updateHyp(); applyEmph(dt);
  LIVE.tag = tag; LIVE.loop = lp; LIVE.rim = rm; strip(); }
const LIVE = {};

/* ---------------- chips ---------------- */
const chip = (t, kind) => `<span class="chip ${kind||''}" title="${kind === 'lean' ? 'Lean theorem in the author’s repository; repo CI, not re-run here' : ''}">${t}</span>`;
const LEAN = t => chip('LEAN · ' + t, 'lean'), PROV = t => chip('PROVED · ' + t), CHK = t => chip('CHECKED · ' + t), CARD = t => chip('CARD · ' + t), READ = chip('READING'), DRIVE = chip('DRIVE'), DRAW = chip('DRAWING'), HYPC = chip('HYPOTHESIS', 'hyp');

/* ---------------- readout helpers ---------------- */
function tagRows(){ const g = LIVE.tag; if(!g) return [['tagged ray', 'leaves through no face (reaches the rim)']];
  const k = g.k, a = k>>1, u = L.genU(k), d = [g.v[1], g.v[2], g.v[3]], psi = Math.acos(Math.max(-1,Math.min(1, d[0]*u[0]+d[1]*u[1]+d[2]*u[2])));
  const c1 = Math.abs(L.mink(g.tin, g.N)), s1sq = 1 - c1*c1, rows = [['tagged ray meets the face of', GEN[k]], ['ψ at the centre', deg(psi)], ['θ₁ from the drawn tangent', deg(Math.acos(c1))],
    ['cosh h · sin ψ  against  sin θ₁', fmt(Math.cosh(S.h[a])*Math.sin(psi),10) + '  ' + fmt(Math.sqrt(s1sq),10)], ['a₁ sin²θ₁', fmt(g.a1*s1sq,10)]];
  if(!g.sp.total){ const c2 = Math.abs(L.mink(g.tt, g.N)), s2sq = 1 - c2*c2; rows.push(['a₂ sin²θ₂ from the drawn refracted tangent', fmt(g.a2*s2sq,10)], ['difference', sci(Math.abs(g.a1*s1sq - g.a2*s2sq))], ['θ₂', deg(Math.acos(c2))]); }
  else rows.push(['a₂ sin²θ₂', 'no transmitted ray: returned whole']);
  rows.push(['R(θ),  T(θ)', fmt(g.sp.R,6) + ',  ' + fmt(g.sp.T,6)], ['layer speeds √(2E/a₁),  √(2E/a₂)  (E = ½)', fmt(1/Math.sqrt(g.a1),4) + ',  ' + fmt(1/Math.sqrt(g.a2),4)], ['cell word after the face', g.sp.total ? 'none: the ray stays in the centre cell' : (g.w2.length ? g.w2.map(q => GEN[q]).join(' ') : 'centre')]);
  return rows; }
const passRow = () => ['clock τ  ·  drive', fmt(CLOCK.tau,2) + ' s  ·  ' + PP.drive];

/* ---------------- the eyes ---------------- */
const EQ = {
  A:'step:  B(u, r),  r = ln z,  Γ = tanh(r/2) = (z − 1)/(z + 1)\nfaces at r/2;  two faces:  g = sinh(h₁) sinh(h₂)\ng < 1: cross at arccos g      g > 1: apart by arccosh g\nthe wall:  Γ² = ½  ⇔  z = 3 + 2√2',
  B:'r = (Y₁ − Y₂)/(Y₁ + Y₂),   t = 2Y₁/(Y₁ + Y₂)\nr² + (Y₂/Y₁) t² = 1\n(Y₁ − Y₂)/(Y₁ + Y₂) = tanh(½ ln Y₁/Y₂)\nreading Y₁/Y₂ = z:   R = Γ²,  T = 1 − Γ² = 1/cosh²(r/2)\nE⁻/E⁺ = Γ²',
  C:'a₁ sin²θ₁ = a₂ sin²θ₂        (a = n², reading)\noblique admittance  Y = ω √(a − C),  C = a₁ sin²θ₁\nray from the centre:  sin θ = cosh h · sin ψ\nspeed in a layer  |ẇ| = √(2E/a)',
  D:'θ_crit = arcsin √(a₂/a₁) = arcsin(1/z)\npast it:  Y₂ = iκₑ,  |Γ| = 1,  arg Γ = −2 arctan(κₑ/y)\ndepth ℓ = 1/|k⊥|,  |k⊥| = ω √((C − a₂)/a₂)\ngap:  r = r₀₁ ⊕ (r₁₂ e^{−2|k⊥| w}),   |r|² + |t|² = 1',
  E:'r = (Γ + x)/(1 + Γx) = Γ ⊕ x,   x = r₁₂ e^{2iφ}\nΣ (−Γ)^m x^{m+1} = x/(1 + Γx)\nzero phase:  r₀₁ ⊕ r₁₂ = r₀₂   (D equal faces: tanh(D r/2))\necho circle:  |r|² > |a|²  ⇔  |x − x_c| > |x_c|',
  F:'normal stress of a wave front = −(E² + H²)/8π\non a plane tilted by θ:  −u cos²θ\npush per face  P = 2R,   K = 1/(1 − P),   sinh²(r/2) = R/T\noblique  P(θ) = 2R(θ) cos²θ        record  K_k(τ) = ∫ P_k dτ',
  G:'two steps:  B_a B_b = L · Rot(θ_T),   tan(θ_T/2) = Γ_a Γ_b\nsquare:  W = B_a B_b B_a⁻¹ B_b⁻¹ = L R L⁻¹ R\nSL(2) trace  2 − 4g²;   g < 1 turn, cos φ = 8g⁴ − 8g² + 1\ng > 1 run 4 arccosh g;   the wall: trace −2, one Jordan block',
  H:'cos ψ′ = (cos ψ + tanh r)/(1 + cos ψ tanh r) = cos ψ ⊕ tanh r\nt′/t = cosh r + sinh r cos ψ;   on the axis t′/t = z\ncaps cos ψ > 1/√2;   the face meets the rim at cos ψ₀ = Γ\nping-pong holds for z ≥ 3 + 2√2  (Lean: z = 7)',
  I:'ẋ = 𝒫 − (κ + a)x + b y,   ẏ = a x − b y\nmean residence (1 + a/b)/κ;   b = 0 keeps a/(κ + a)\noccupation C = 1/(z + 1),   1 − 2C = Γ,   T = 4C(1 − C)\nroute 2Σ|r_j|,  endpoint 2|Σ r_j|,  defect 4 min(R₊, R₋)',
  J:'every balance law, recomputed from the drawn objects on every frame' };
const NOT_CLAIMED = 'What this page does not claim: the faces move on a declared schedule (DRIVE) and no law of motion for z(τ) is claimed; no retardation and no Doppler shift from the motion of a face is modelled; reading a peel step as an admittance step (Y₁/Y₂ = z) and a = n² are readings; with a phase, Γ ⊕ x is not velocity addition; steps compose as one velocity on one axis only, so the layer stack is computed on each arm’s axis; off-axis rays split by flux without phases; P = 2R as a physical pressure is untested; the ping-pong statement above the wall is a numerical check here, Lean covers z = 7; the Thomas turn is of a frame, not a statement about polarisation; Lean was not re-run in this session, chips name the theorem and file.';
const views = { A:[0.62,0.36,8.2,0], B:[0.12,0.22,6.6,0], C:[0.85,0.55,7.0,0.2], D:[0.95,0.35,6.6,0.2], E:[0.12,0.25,6.6,0], F:[0.25,0.3,6.8,0], G:[0.5,0.7,7.2,0], H:[0.7,0.45,8.6,0], I:[1.2,0.3,7.0,0], J:[0.62,0.36,8.6,0] };
const EMPH = {
  A:{rim:1,tree:1,balls:1,faces:1,cross:1,rays:0.3,stack:0.25,press:0.2,loop:0.15,rimf:0.2,hyp:0.2},
  B:{rim:0.6,tree:0.25,balls:1,faces:1,cross:0.3,rays:0.2,stack:1,press:0.2,loop:0.05,rimf:0.1,hyp:0.2},
  C:{rim:0.5,tree:0.15,balls:0.7,faces:0.8,cross:0.3,rays:1,stack:0.1,press:0.1,loop:0.05,rimf:0.1,hyp:0.2},
  D:{rim:0.5,tree:0.15,balls:0.7,faces:1,cross:1,rays:1,stack:0.1,press:0.1,loop:0.05,rimf:0.15,hyp:0.2},
  E:{rim:0.5,tree:0.15,balls:0.8,faces:0.6,cross:0.2,rays:0.15,stack:1,press:0.3,loop:0.05,rimf:0.1,hyp:0.2},
  F:{rim:0.6,tree:0.15,balls:0.8,faces:0.6,cross:0.2,rays:0.5,stack:0.7,press:1,loop:0.05,rimf:0.1,hyp:0.2},
  G:{rim:0.6,tree:0.3,balls:0.8,faces:0.45,cross:0.7,rays:0.1,stack:0.1,press:0.1,loop:1,rimf:0.35,hyp:0.2},
  H:{rim:1,tree:0.15,balls:0.6,faces:0.5,cross:0.3,rays:0.2,stack:0.1,press:0.15,loop:0.6,rimf:1,hyp:0.2},
  I:{rim:0.6,tree:0.2,balls:0.8,faces:0.6,cross:0.7,rays:0.25,stack:0.6,press:0.7,loop:0.1,rimf:0.15,hyp:1},
  J:{rim:1,tree:1,balls:1,faces:1,cross:1,rays:1,stack:1,press:1,loop:1,rimf:1,hyp:1} };
const pairBtns = () => `<div class="row">` + ['I and J','J and K','I and K'].map((t,i) => `<button data-pair="${i}" aria-pressed="${PP.pair===i}">${t}</button>`).join('') + `</div>`;
const armBtns = () => `<div class="row">` + AXN.map((t,i) => `<button data-arm="${i}" aria-pressed="${PP.arm===i}">arm ${t}</button>`).join('') + `</div>`;
const absBtns = () => `<div class="row"><button data-abs="0" aria-pressed="${!PP.absorb}">balls radiate (b > 0)</button><button data-abs="1" aria-pressed="${!!PP.absorb}">balls absorb (b = 0)</button></div>`;
function bindBtns(){ document.querySelectorAll('#ctl button[data-pair]').forEach(b => b.addEventListener('click', () => { PP.pair = +b.dataset.pair; ST.Wacc = L.I4(); M.clearTrail(CARRY); document.querySelectorAll('#ctl button[data-pair]').forEach(q => q.setAttribute('aria-pressed', q === b)); }));
  document.querySelectorAll('#ctl button[data-arm]').forEach(b => b.addEventListener('click', () => { PP.arm = +b.dataset.arm; document.querySelectorAll('#ctl button[data-arm]').forEach(q => q.setAttribute('aria-pressed', q === b)); }));
  document.querySelectorAll('#ctl button[data-abs]').forEach(b => b.addEventListener('click', () => { PP.absorb = +b.dataset.abs; document.querySelectorAll('#ctl button[data-abs]').forEach(q => q.setAttribute('aria-pressed', q === b)); })); }
let made = false;
function eye(o){ return Object.assign({ make(g, S3){ if(!made){ S3.world.add(WORLD); made = true; window.__S3 = S3; } }, enter(){ Object.assign(WT, EMPH[o.id]); }, bind:bindBtns, view:views[o.id],
  step(dt){ if(o.id === CUR.id || true){ update(dt); } CUR.id = o.id; return o.rows(); } }, o); }
const CUR = { id:'A' };
const pairRows = () => S.pairs.map(p => ['faces of ' + AXN[p.a] + ' and ' + AXN[p.b], p.over ? 'cross at ' + deg(p.alpha) : 'apart by δ = ' + fmt(p.delta,5)]);
const E_A = eye({ id:'A', title:'A · The object: four balls, faces, rim', section:'Two Trees Def. 4.1; faces Thm 8.4', grade: PROV('Two Trees v4, Thm 5.3, 8.4') + DRIVE,
  eq:EQ.A, uses:['zI','zJ','zK','A'],
  text:'One ball holds everything on this page. The centre O and its three neighbours I, J and K are balls of one tree, each one peel step from the centre along its own axis; a step of ratio z has hyperbolic length ln z. The face halfway to each neighbour, and to the three neighbours on the far side, is a plane of the ball drawn as a coloured cap. The three step ratios move on a declared schedule, so the balls, the faces, where two faces cross or stand apart, the rays, the layers and the light on the rim all change together, from one clock.',
  rows(){ const r = [passRow()]; for(let a=0;a<3;a++) r.push([AXN[a] + ':  z,  ln z,  Γ', fmt(S.z[a],4) + ',  ' + fmt(S.r[a],4) + ',  ' + fmt(S.G[a],5)], [AXN[a] + ':  R = Γ²,  T,  Γ² against ½', fmt(S.Rf[a],5) + ',  ' + fmt(S.Tf[a],5) + ',  ' + (S.Rf[a] < 0.5 ? 'below' : 'above')]);
    return r.concat(pairRows()); } });
const E_B = eye({ id:'B', title:'B · One face is one reflecting step', section:'M1 · Event Horizon Ed. 10; VOTKP Film, Smith', grade: LEAN('step_matching, flux_balance') + LEAN('interface_smith') + LEAN('matched_load, polar_mirror') + CARD('B189 (theorem)') + READ,
  eq:EQ.B, uses:['zI','zJ','zK','depth'], extra:armBtns,
  text:'A face between two cells is a step in admittance. A wave meeting it splits: the fraction R = Γ² returns and T = 1 − Γ² goes on, and the flux balance holds exactly. Reading the admittance ratio across a face as the step ratio z, the Smith coordinate of the face is Γ = tanh(r/2). On each arm the stream running out from the centre is drawn in the arm colour and the returned stream in rose; their brightness is the flux they carry. A matched face (z = 1) returns nothing; a face to zero admittance is a mirror.',
  rows(){ const a = PP.arm, z = S.z[a], s = L.step(z, 1), G2 = L.smith(-z)*L.smith(z);
    return [passRow(), ['arm', AXN[a]], ['Y₁/Y₂', fmt(z,5)], ['r,  t', fmt(s.r[0],6) + ',  ' + fmt(s.t[0],6)], ['R,  T', fmt(s.R,6) + ',  ' + fmt(s.T,6)], ['R + (Y₂/Y₁) t² − 1', sci(s.R + (1/z)*s.t[0]**2 - 1)],
      ['E⁻/E⁺ = Γ²', fmt(S.Rf[a],6)], ['Γ reversed (Y₂ → Y₁)', fmt(L.step(1,z).r[0],6)], ['distance to matched load |Γ|', fmt(Math.abs(S.G[a]),5)], ['distance to the mirror 1 − |Γ|', fmt(1-Math.abs(S.G[a]),5)], ['Γ(−z)·Γ(z)', fmt(G2,12)]]; } });
const E_C = eye({ id:'C', title:'C · Refraction at the face', section:'M2 · card B30; square-case, UPG Dirac refraction', grade: CARD('B30 (theorem)') + LEAN('three_body_refraction_is_squared_snell') + LEAN('refraction_law, admittance') + CHK('1e-10') + READ,
  eq:EQ.C, uses:['fan','omega','tag'],
  text:'A fan of rays leaves the centre and turns slowly about the diagonal. Every ray is a true shortest path of the ball. At each face it splits into a returned ray and a ray that goes on, and the quantity a sin²θ is the same on both sides. The angles in the readout are measured from the drawn tangent vectors, not from the formula that built them. The cell a ray is in is a word of the tree; below the wall the cells overlap, so the word belongs to the ray, not to the point. The gold ray is the tagged one.',
  rows(){ return [passRow()].concat(tagRows()); } });
const E_D = eye({ id:'D', title:'D · Total return and the gap', section:'M3 · card B39; Event Horizon Ed. 10; Film', grade: CARD('B39 (theorem)') + LEAN('total_reflection, turning_point') + LEAN('film_is_oplus') + PROV('Event Horizon Ed. 10 §8.3 (model equation)') + CHK('1e-12'),
  eq:EQ.D, uses:['fan','tag','omega'], extra:pairBtns,
  text:'Past the critical angle no ray goes on: the whole ray returns, with a phase, and a short tail beyond the face shows the depth the wave reaches before it dies away. On each cap the window of rays from the centre that cross is drawn in the arm colour and the ring of total return in rose. Where two faces stand apart, the white line is their common perpendicular, of length δ = arccosh g; across a gap of that width a wave past the critical angle still tunnels a fraction, computed here as a plane-parallel film.',
  rows(){ const g = LIVE.tag, rows = [passRow()]; const a = g ? g.k>>1 : 0, z = S.z[a], h = S.h[a];
    rows.push(['κ = a₁/a₂ at the face of ' + AXN[a], fmt(z*z,4) + (PP.orient < 0 ? '  (rises outward: no total return going out)' : '')], ['θ_crit = arcsin(1/z)', deg(Math.asin(1/z))], ['window half-angle at the centre arcsin(1/(z cosh h))', deg(Math.asin(Math.min(1, 1/(z*Math.cosh(h)))))]);
    if(g){ rows.push(['tagged ray', g.sp.total ? 'returned whole' : 'crosses'], ['|Γ|', fmt(C.abs(Array.isArray(g.sp.r) ? g.sp.r : [g.sp.r,0]),12)]);
      if(g.sp.total) rows.push(['return phase arg Γ', deg(g.sp.phase)], ['θ₂', 'π/2 + i·' + fmt(g.sp.theta2[1],5)], ['penetration depth ℓ', fmt(g.sp.depth,5)]); }
    const p = S.pairs[PP.pair]; rows.push(['selected pair', AXN[p.a] + ' and ' + AXN[p.b]]);
    if(p.over) rows.push(['faces cross at', deg(p.alpha)], ['gap', 'none: the faces cross']);
    else { const a1 = 1, a2 = 1/(S.z[p.a]**2), th = g && g.sp.total ? Math.acos(Math.abs(L.mink(g.tin,g.N))) : Math.asin(1/S.z[p.a]) + 0.15, Cc = a1*Math.sin(th)**2;
      const ke = PP.omega*Math.sqrt(Math.max(0,Cc-a2)), kp = PP.omega*Math.sqrt(Math.max(0,(Cc-a2)/a2)), tg = L.tunnelGap(PP.omega*Math.sqrt(a1-Cc), ke, kp, p.delta);
      rows.push(['gap δ = arccosh g', fmt(p.delta,6)], ['incidence used', deg(th)], ['tunnelled fraction across δ (plane-parallel film)', sci(tg.T)], ['|r|² + |t|² − 1', sci(tg.R + tg.T - 1)]); }
    return rows; } });
const E_E = eye({ id:'E', title:'E · Layers: echoes and Smith addition', section:'M4 · VOTKP Film.lean, Directed, Smith; cards B100, B101, B203', grade: LEAN('film_is_oplus, echo_series, echo_resum') + LEAN('stack_telescopes') + LEAN('echo_circle') + CARD('B100 (theorem)') + READ,
  eq:EQ.E, uses:['depth','omega'], extra:armBtns,
  text:'Along each arm the faces at (k + ½) ln z cut the line into layers. Light trapped in a layer runs both ways and each pass returns part of itself: the outgoing and returning streams in every layer carry the exact amplitudes of the stack, and the net flux is the same number in every layer. The white point on the first face of the chosen arm is the composed reflection r, with the cap used as the Smith disk: centre matched, edge a mirror. The coloured ring marks x, and the white arc is the echo circle: x outside it means the layers behind return more than the first face alone.',
  rows(){ const a = PP.arm, st = S.stacks[a], D = S.depth, z0 = L.stackAxis(st.Ys, st.Ys.map(() => 0)), spread = Math.max(...st.flux) - Math.min(...st.flux), ec = st.echo;
    return [passRow(), ['arm, faces drawn', AXN[a] + ', ' + D], ['Γ of every face', fmt(st.G[0][0],6)], ['phases φ_k', st.phis.slice(1,D).map(v => fmt(v % (2*PI),3)).join(', ') || '—'],
      ['composed r by ⊕', cfmt(st.r,6)], ['composed r by the transfer matrix', cfmt(st.rTM,6)], ['first face ⊕ bounce sum (12 echoes)', cfmt(st.bounce,6)], ['difference', sci(C.abs(C.sub(st.bounce, st.r)))],
      ['|r|²,  T_total', fmt(C.abs2(st.r),6) + ',  ' + fmt(st.Ttot,6)], ['net flux in every layer (spread)', fmt(st.flux[0],6) + '  (' + sci(spread) + ')'],
      ['zero phase: composed r against tanh(D r/2)', fmt(z0.r[0],8) + ',  ' + fmt(Math.tanh(D*S.r[a]/2)*(PP.orient > 0 ? 1 : -1),8)],
      ['x against the echo circle', (C.abs(C.sub(st.xNow, ec.xc)) > C.abs(ec.xc) ? 'outside: |r|² > Γ²' : 'inside: |r|² < Γ²')], ['x_c', cfmt(ec.xc,4)]]; } });
const E_F = eye({ id:'F', title:'F · Pressure and the kick record', section:'M5 · Maxwell Treatise art. 792; FEED-LOOP-03', grade: LEAN('art792_radiation_pressure_components') + CHK('FEED-LOOP-03 P1–P3') + READ + chip('as physical pressure: untested'),
  eq:EQ.F, uses:['depth','tag'], extra:armBtns,
  text:'A wave front presses on a plane with its energy per unit volume, and on a plane tilted by θ with u cos²θ. Each face that returns a fraction R of the light reaching it is pushed by 2R in units of the push of full absorption. Here the push on each face along an arm is the light arriving from each side, pushing in opposite senses; the short bright arrows show its size and sense. Each face keeps a running record of its kicks, K_k(τ), drawn as the lit share of a ring round the arm’s point on the rim; the ring fills once per 5 units.',
  rows(){ const a = PP.arm, st = S.stacks[a], g = LIVE.tag, R = S.Rf[a], P = 2*R, s = L.stress([1,0,0],[0,1,0]), th = g ? Math.acos(Math.abs(L.mink(g.tin, g.N))) : 0;
    const rows = [passRow(), ['arm', AXN[a]], ['P = 2R per face', fmt(P,6)], ['K = 1/(1 − P)', P < 1 ? fmt(1/(1-P),5) : '— (past the wall: R > ½)'], ['sinh²(r/2) against R/T', fmt(Math.sinh(S.r[a]/2)**2,8) + ',  ' + fmt(R/(1-R),8)]];
    if(g) rows.push(['tagged ray: 2R(θ) cos²θ', fmt(2*g.sp.R*Math.cos(th)**2,6)], ['Maxwell normal stress at θ, over u', fmt(L.normalStress(s.s, [0, Math.sin(th), Math.cos(th)])/s.u,8) + '  (−cos²θ = ' + fmt(-(Math.cos(th)**2),8) + ')']);
    st.push.forEach((v,k) => rows.push(['face ' + (k+1) + ': push from arriving light,  record K', fmt(v,5) + ',  ' + fmt(ST.K[a][k],4)])); return rows; } });
const E_G = eye({ id:'G', title:'G · Rotation within and outside the layers', section:'M6 · Two Trees v4 Thm 4.7, 5.3; PeelTrees', grade: LEAN('thomas5, thomas7, thomas_half_angle') + LEAN('comm_trace') + LEAN('schottky_ratio') + CHK('1e-8 (W = L R L⁻¹ R; unequal steps)'),
  eq:EQ.G, uses:['zI','zJ','zK'], extra:pairBtns,
  text:'Two steps along different arms are one step and a turn. At the corner reached by the two steps the solid frame is the frame carried by the steps and the dashed frame is the one a single straight step would give: the angle between them is the Thomas turn, a rotation inside the layers. The gold square of four steps does not close. Below the wall it turns about a fixed point and carries the centre round a ring; at the wall it locks; past the wall it runs out to the rim. The bright point on the rim is one light direction carried round the same square, pass after pass; every eighth pass starts again from the prepared direction.',
  rows(){ const p = S.pairs[PP.pair], aud = AUD, kind = p.g < 1 ? 'turns' : p.g > 1 ? 'runs' : 'locks', ell = LIVE.loop.ell, d1 = [ell[1]/ell[0], ell[2]/ell[0], ell[3]/ell[0]], d0 = [ELL0[1],ELL0[2],ELL0[3]];
    return [passRow(), ['pair', AXN[p.a] + ' and ' + AXN[p.b]], ['Thomas turn θ_T', deg(p.thetaT)], ['2 arctan(Γ_a Γ_b)', deg(2*Math.atan(S.G[p.a]*S.G[p.b]))], ['g = sinh h_a sinh h_b', fmt(p.g,6)],
      ['SL(2) trace,  2 − 4g²', fmt(p.tr2,8) + ',  ' + fmt(2 - 4*p.g*p.g,8)], ['the square', kind], p.g < 1 ? ['turn per pass φ', deg(p.phi)] : ['run per pass 4 arccosh g', fmt(p.run,6)],
      ['‖W − L R L⁻¹ R‖/‖W‖ (all pairs)', sci(aud.LRLR)], ['loop phase n(τ)', fmt(ST.n,3)], ['carried direction: angle from the prepared one', deg(Math.acos(Math.max(-1,Math.min(1, d0[0]*d1[0]+d0[1]*d1[1]+d0[2]*d1[2]))))]]; } });
const E_H = eye({ id:'H', title:'H · Light on the rim', section:'M7 · PingPong7; Smith.lean', grade: LEAN('caps_disjoint, pingpong_step (z = 7)') + LEAN('step_plane, hyperbolic_length') + CHK('1e-12; ping-pong above the wall, 0 exceptions') + READ,
  eq:EQ.H, uses:['zI','zJ','zK'],
  text:'Every point of the rim is a direction of light. A step acts on the directions by the same Smith addition, cos ψ′ = cos ψ ⊕ tanh r, and changes their frequency by t′/t; the colour of each direction is that ratio. The six white circles are the 45° caps of the ping-pong. The coloured circles are where each face meets the rim, at cos ψ₀ = Γ; they pass through the cap circles exactly at the wall. Above the wall one step sends every direction outside the opposite cap into its own cap.',
  rows(){ const rm = LIVE.rim, rows = [passRow(), ['step acting now', AXN[rm.arm] + ', fraction ' + fmt(rm.f,3) + ' of ln z']];
    for(let a=0;a<3;a++) rows.push([AXN[a] + ': ψ₀ = arccos Γ,  minus the 45° cap', deg(Math.acos(S.shadow[a])) + ',  ' + fmt((Math.acos(S.shadow[a]) - PI/4)*180/PI,3) + '°'],
      [AXN[a] + ': tanh r,  t′/t on the axis', fmt(Math.tanh(S.r[a]),6) + ',  ' + fmt(L.doppler(1, S.r[a]),5) + ' (z = ' + fmt(S.z[a],5) + ')'], [AXN[a] + ': ping-pong at this z', S.ping[a] === 0 ? 'holds (0 exceptions in 3600 tests)' : 'fails (' + S.ping[a] + ' exceptions in 3600 tests)']);
    rows.push(['share of rim directions inside the six caps', fmt(100*rm.share,1) + ' %'], ['note', 'Lean: z = 7']); return rows; } });
const E_I = eye({ id:'I', title:'I · The hypothesis layer', section:'his picture, drawn on the same object', grade: HYPC + CARD('B182 (theorem, conditional energy model)') + LEAN('fermion_smith, particle_hole') + CARD('B203 (theorem)'),
  eq:EQ.I, uses:['kappa','ha','hb','depth'], extra:() => absBtns() + armBtns(),
  text:'Hypothesis, the author’s picture: light is trapped between layers and kicks itself on the hypersurface; it is absorbed and given out again further on; the sea of electrons is the ground and follows the light, keeping a record of each kick; balls join at levels but always keep a gap layer, as a crystal keeps its spacing; and exclusion at the face is his Snell’s law and Pauli principle at the hypersurface. Each piece is drawn in amber, dashed or hollow, on the proved part it stands on: the stocks of card B182 per layer (filled: free, hollow: held on the face), the occupation C = 1/(z + 1) as the dashed arc on each face, and the gap between separated faces. What is hypothesis is the assignment, not the arithmetic.',
  rows(){ const a = PP.arm, st = ST.stocks[a], b = PP.absorb ? 0 : PP.hb, rows = [['hypothesis: arm, ball class', AXN[a] + ', ' + (PP.absorb ? 'absorbing (b = 0)' : 'radiating (b > 0)')]];
    st.slice(0, S.depth).forEach((q,k) => rows.push(['hypothesis: layer ' + (k+1) + '  free x,  held y', fmt(q[0],4) + ',  ' + fmt(q[1],4)]));
    rows.push(['hypothesis: mean residence (1 + a/b)/κ', b > 0 ? fmt((1 + PP.ha/b)/PP.kappa,4) : '— (b = 0)'], ['hypothesis: share kept at b = 0, a/(κ + a)', fmt(PP.ha/(PP.kappa+PP.ha),4)]);
    for(let i=0;i<3;i++) rows.push(['hypothesis: ' + AXN[i] + ' occupation C,  4C(1 − C) against T', fmt(S.Cocc[i],5) + ',  ' + fmt(4*S.Cocc[i]*(1-S.Cocc[i]),6) + ' / ' + fmt(S.Tf[i],6)]);
    const ch = LIVE.tag ? LIVE.tag.chain : []; if(ch.length){ const route = 2*ch.reduce((s,v)=>s+Math.abs(v),0), end = 2*Math.abs(ch.reduce((s,v)=>s+v,0)), Rp = ch.filter(v=>v>0).reduce((s,v)=>s+v,0), Rm = -ch.filter(v=>v<0).reduce((s,v)=>s+v,0);
      rows.push(['hypothesis: kick record of the tagged ray, route, endpoint', fmt(route,4) + ',  ' + fmt(end,4)], ['hypothesis: defect, 4 min(R₊, R₋)', fmt(route-end,6) + ',  ' + fmt(4*Math.min(Rp,Rm),6)]); }
    S.pairs.forEach(p => rows.push(['hypothesis: ' + AXN[p.a] + AXN[p.b] + ' gap layer', p.over ? 'faces cross at ' + deg(p.alpha) + ', balls round an edge 360°/α = ' + fmt(2*PI/p.alpha,3) : 'gap δ = ' + fmt(p.delta,5)]));
    return rows; } });
const E_J = eye({ id:'J', title:'J · Everything at once, and the ledger', section:'audit of every frame', grade: CHK('residuals live') + DRIVE,
  eq:EQ.J, uses:[], text:'Every part at once, all moving from the one clock. The ledger below recomputes each balance law on this frame from the drawn objects themselves. ' + NOT_CLAIMED,
  extra:() => `<div class="row"><button id="selfbtn">Run self-test (this page’s arithmetic)</button></div>`,
  bind(){ bindBtns(); const b = document.getElementById('selfbtn'); if(b) b.addEventListener('click', () => { SELF = L.selftest(); }); },
  rows(){ const a = AUD, r = [passRow(), ['flux at every face, R + T − 1  (≤ 1e-12)', sci(a.flux)], ['a sin²θ across every face, relative  (≤ 1e-10)', sci(a.snell)], ['returned angle = incident angle  (≤ 1e-10)', sci(a.refl)],
      ['ray-tree nodes: unit tangent on the hyperboloid  (≤ 1e-10)', sci(a.node)], ['stack net flux spread  (≤ 1e-12)', sci(a.stackFlux)], ['stack ⊕ against transfer matrix  (≤ 1e-12)', sci(a.stackRec)], ['|det W − 1|  (≤ 1e-12)', sci(a.detW)],
      ['W = L R L⁻¹ R, relative  (≤ 1e-8)', sci(a.LRLR)], ['segments in the ray tree', String(S.segs.length)]];
    const ell = LIVE.loop.ell; r.push(['null norm of the carried direction (relative)', sci(Math.abs(L.mink(ell,ell))/(ell[0]*ell[0]))]);
    if(SELF) r.push(['self-test', SELF.filter(x => x.pass).length + ' of ' + SELF.length + ' lines hold']); else r.push(['self-test', 'not run']);
    return r; } });

/* ---------------- run ---------------- */
const params = [
  {id:'zI', label:'Ball I: mean step ratio z̄', min:1.5, max:13, step:0.01, value:3}, {id:'zJ', label:'Ball J: mean step ratio z̄', min:1.5, max:13, step:0.01, value:5}, {id:'zK', label:'Ball K: mean step ratio z̄', min:1.5, max:13, step:0.01, value:7},
  {id:'A', label:'Breathing amplitude in ln z', min:0, max:0.6, step:0.01, value:0.35}, {id:'fan', label:'Fan half-angle (degrees)', min:5, max:85, step:1, value:62},
  {id:'omega', label:'Light frequency ω', min:0.5, max:8, step:0.05, value:3}, {id:'tag', label:'Tagged ray', min:0, max:8, step:1, value:6}, {id:'depth', label:'Layers on each arm (faces)', min:2, max:6, step:1, value:4},
  {id:'kappa', label:'hypothesis: κ (loss)', min:0.1, max:3, step:0.05, value:1}, {id:'ha', label:'hypothesis: a (held)', min:0, max:3, step:0.05, value:1}, {id:'hb', label:'hypothesis: b (given back)', min:0.02, max:2, step:0.01, value:0.2} ];
M.run({ title:'Light at the Hypersurface', byline:'JEROMIE BEASLEY · MIXER v1 · 15 NOV 2026 · AI-ASSISTED', note:'an explorer of checked formulas, not a test of them',
  feed:{ params, build(P){ ['zI','zJ','zK','A','fan','omega','tag','depth','kappa','ha','hb'].forEach(k => { if(P[k] != null) PP[k] = +P[k]; }); return PP; } },
  eyes:[E_A,E_B,E_C,E_D,E_E,E_F,E_G,E_H,E_I,E_J], film:['A','B','C','D','E','F','G','H','I','J'] });
/* chips and the strip */
const css = document.createElement('style'); css.textContent = `.chip{display:inline-block;font-family:var(--mono);font-size:10px;letter-spacing:.04em;color:#05070b;background:#8fd9ff;border-radius:3px;padding:1px 5px;margin:2px 4px 2px 0}
.chip.lean{background:#f2c14e}.chip.hyp{background:transparent;color:#ffb347;border:1px solid #ffb347}
.strip{position:fixed;top:calc(12px + env(safe-area-inset-top,0px));right:12px;display:flex;flex-wrap:wrap;gap:5px;align-items:center;max-width:min(560px,calc(100% - 390px));justify-content:flex-end;background:var(--panel);border:1px solid var(--edge);border-radius:8px;padding:7px 8px;font-size:12px}
.strip button{font-size:11.5px;padding:4px 8px}.strip button[aria-pressed=true]{border-color:var(--gold);color:var(--gold)}.strip .tau{font-family:var(--mono);color:var(--ink);min-width:86px}
.strip input{width:80px;accent-color:var(--cyan)}body.clean .strip{display:none}
@media (max-width:640px){.strip{left:8px;right:8px;max-width:none;top:calc(8px + env(safe-area-inset-top,0px));justify-content:flex-start}}`; document.head.append(css);
document.body.insertAdjacentHTML('beforeend', `<div class="strip" id="strip"><span class="tau" id="tau">τ 0.00 s</span><button id="s_play" aria-pressed="${CLOCK.playing}">${CLOCK.playing ? 'Pause' : 'Play'}</button><button id="s_step">Step</button>
<label>Speed <input id="s_speed" type="range" min="0.1" max="4" step="0.1" value="1"></label><button id="s_reset">Reset τ</button>
<button data-drive="hold">hold</button><button data-drive="breathe">breathe</button><button data-drive="sweep">sweep</button>
<button id="s_hyp" aria-pressed="true">Hypothesis layer: shown</button><button id="s_or" aria-pressed="false">Admittance: falls outward</button></div>`);
const $ = id => document.getElementById(id);
function strip(){ $('tau').textContent = 'τ ' + fmt(CLOCK.tau,2) + ' s'; document.querySelectorAll('#strip button[data-drive]').forEach(b => b.setAttribute('aria-pressed', b.dataset.drive === PP.drive)); }
$('s_play').addEventListener('click', () => { CLOCK.playing = !CLOCK.playing; $('s_play').textContent = CLOCK.playing ? 'Pause' : 'Play'; $('s_play').setAttribute('aria-pressed', CLOCK.playing); });
$('s_step').addEventListener('click', () => { stepOnce = true; });
$('s_speed').addEventListener('input', e => CLOCK.speed = +e.target.value);
$('s_reset').addEventListener('click', () => { CLOCK.tau = 0; ST = L.initState(); M.clearTrail(CARRY); });
document.querySelectorAll('#strip button[data-drive]').forEach(b => b.addEventListener('click', () => { PP.drive = b.dataset.drive; }));
$('s_hyp').addEventListener('click', () => { HYP.shown = !HYP.shown; $('s_hyp').textContent = 'Hypothesis layer: ' + (HYP.shown ? 'shown' : 'hidden'); $('s_hyp').setAttribute('aria-pressed', HYP.shown); });
$('s_or').addEventListener('click', () => { PP.orient = -PP.orient; $('s_or').textContent = 'Admittance: ' + (PP.orient > 0 ? 'falls outward' : 'rises outward'); $('s_or').setAttribute('aria-pressed', PP.orient < 0); });
window.__lh = { go:id => { window.MIXER_API.show(id); }, setTau:t => { CLOCK.tau = t; ST = L.initState(); const n = Math.round(t*60); for(let i=0;i<n;i++) L.advance(ST, PP, i/60, 1/60); CLOCK.tau = n/60; },
  play:b => { CLOCK.playing = b; }, set:(k,v) => { PP[k] = v; }, hyp:b => { HYP.shown = b; }, selftest:() => L.selftest(), get S(){ return S; }, get AUD(){ return AUD; }, get ST(){ return ST; },
  rows:() => document.getElementById('read').innerText, CLOCK, PP,
  bench:n => { const was = CLOCK.playing; CLOCK.playing = false; const t0 = performance.now(); for(let i=0;i<n;i++) update(1/60); CLOCK.playing = was; return (performance.now()-t0)/n; } };
})();
