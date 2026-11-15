/* IQGT Mixer 3D v5 eyes, Act II: the land under the map (v7.3.1 §4, §5, §8) */
(() => {
const M = API, V3 = (x,y,z) => new T.Vector3(x,y,z), Cr = window.Core, IQ = window.IQ;
const R0 = 1.55, onS = (n, r) => V3(n[0]*(r||R0), n[2]*(r||R0), n[1]*(r||R0));
const deg = r => r*180/Math.PI, rad = d => d*Math.PI/180, fx = (x, d) => (+x).toFixed(d), fe = x => (+x).toExponential(1);
const chk = (label, mixer, paper, ok) => ({label, mixer, paper, ok});
function sphereRig(g, r, opacity, at){ r = r || R0; const s = M.glass(r, PAL.metric, 2.6, opacity == null ? 0.5 : opacity); if(at) s.position.copy(at); g.add(s); const du = M.dust(700, r*1.03, r*1.3, 0x5ab0ff, 0.045, 13); if(at) du.position.copy(at); g.add(du);
  const eq = []; for(let i=0;i<=160;i++){ const a = 2*Math.PI*i/160; eq.push(V3(r*Math.cos(a), 0, r*Math.sin(a)).add(at || V3(0,0,0))); } g.add(M.line(eq, 0x2a3b5c, 0.7)); }
const EYES = [];

/* 6. Folds lie (§4, §8.5) */
EYES.push((() => {
  const SX = x => x*1.3, SZ = y => (0.3 - y)*2.0, PY = -2.0;
  return { id:'folds', title:'Degenerate pullback at a fold', section:'§4, §8.5', grade:'proved', gradeLabel:'Proved; numbers computed here',
    eq:'𝑔(𝑉,𝑉) = Tr(𝛱𝑉†𝑉) = ‖𝑋‖² > 0  for every tangent vector 𝑉 ≠ 0\ndet 𝛾*𝑔 → 0 where the map folds',
    text:'Below: the parameter plane (x, y). Above: its image on the Bloch sphere under the map θ = y + 1.1, φ = x²/2. Because x and −x map to the same point, the image folds over along the amber fold line x = 0. In these chart coordinates the pulled-back metric is degenerate there: its determinant, x² sin²θ / 16, vanishes. The intrinsic metric on T Gr(k,H) does not degenerate: g(V,V) = ‖X‖² > 0 for every nonzero tangent vector, and the gap stays at 2. The degeneracy belongs to the map, not to the Grassmannian.',
    legend:[['#5ab0ff','x > 0 half of the chart'],['#ff6f91','x < 0 half'],['#ffb547','the fold line, x = 0']],
    controls:[{id:'y', label:'Parameter y (chart coordinate)', min:-0.3, max:0.9, step:0.01, value:0.0}],
    view:[0.85, 0.3, 7.8, -0.25],
    make(g, ctx){ sphereRig(g, R0, 0.35);
      const sheet = new T.Group(); g.add(sheet);
      for(let i=0;i<=12;i++){ const x = -1.2 + 2.4*i/12, pts = [], img = []; for(let k=0;k<=30;k++){ const y = -0.3 + 1.2*k/30; pts.push(V3(SX(x), PY, SZ(y))); img.push(onS(IQ.foldN(x, y), R0*1.005)); }
        const c = Math.abs(x) < 1e-9 ? PAL.gap : x > 0 ? PAL.metric : PAL.tip; sheet.add(M.line(pts, c, 0.45)); g.add(M.line(img, c, x === 0 ? 1 : 0.55)); }
      for(let k=0;k<=12;k++){ const y = -0.3 + 1.2*k/12, pts = [], img = []; for(let i=0;i<=40;i++){ const x = -1.2 + 2.4*i/40; pts.push(V3(SX(x), PY, SZ(y))); img.push(onS(IQ.foldN(x, y), R0*1.005)); }
        sheet.add(M.line(pts, 0x6f86ad, 0.3)); g.add(M.line(img, 0x9fb4d8, 0.35)); }
      const crease = []; for(let k=0;k<=40;k++) crease.push(onS(IQ.foldN(0, -0.3 + 1.2*k/40), R0*1.01)); g.add(M.tube(crease, 0.016, PAL.gap, 0.95));
      const cs = []; for(let k=0;k<=40;k++) cs.push(V3(0, PY+0.01, SZ(-0.3 + 1.2*k/40))); g.add(M.tube(cs, 0.012, PAL.gap, 0.9));
      ctx.a = M.orb(0.045, 0xffffff, 7); ctx.b = M.orb(0.045, 0xffffff, 7); g.add(ctx.a); g.add(ctx.b); ctx.thr = M.dashed([V3(), V3(0,1,0)], 0xffffff, 0.35); g.add(ctx.thr);
      ctx.tr = M.trail(120, 0.07); g.add(ctx.tr);
      ctx.callout(V3(SX(-1.2), PY, SZ(-0.3)), 'The parameter plane', 'chart coordinates (x, y)', '#9fb4d8', -40, 36); ctx.callout(onS(IQ.foldN(0, 0.75), R0*1.01), 'The fold line', 'x and −x map to one point', '#ffb547', 44, -40); },
    step(dt, t, ctx){ const x = 1.2*Math.sin(0.55*t), y = ctx.p.y, P = V3(SX(x), PY, SZ(y)), Q = onS(IQ.foldN(x, y), R0*1.015);
      ctx.a.position.copy(P); ctx.b.position.copy(Q); M.setDashed(ctx.thr, [P, Q]); M.pushTrail(ctx.tr, Q, x >= 0 ? [0.35,0.69,1] : [1,0.44,0.57]);
      const G = IQ.pullG(IQ.foldN, x, y), r = Cr.rng(3); let mn = 9; for(let i=0;i<40;i++){ const q = IQ.tangent2(G.P0, r); const gg = IQ.Q2(G.P0, q.V, q.V)[0], xx = q.X.reduce((s, z) => s + z[0]*z[0] + z[1]*z[1], 0); mn = Math.min(mn, gg/xx); }
      return [['Parameter x', fx(x, 3)], ['det of the pulled-back metric', fx(G.det, 6), 'tip'], ['Exact value x² sin²θ / 16', fx(x*x*Math.sin(y+1.1)**2/16, 6)], ['Intrinsic: smallest g(V,V)/‖X‖²', fx(mn, 6), 'tail'], ['Gap', '2.000 everywhere', 'gap']]; },
    test(){ const a = IQ.pullG(IQ.foldN, 0.6, 0).det, b = IQ.pullG(IQ.foldN, 0, 0).det, r = Cr.rng(9), P0 = IQ.pullG(IQ.foldN, 0, 0).P0; let w = 0;
      for(let i=0;i<200;i++){ const q = IQ.tangent2(P0, r); const gg = IQ.Q2(P0, q.V, q.V)[0], xx = q.X.reduce((s, z) => s + z[0]*z[0] + z[1]*z[1], 0); w = Math.max(w, Math.abs(gg/xx - 1)); }
      return [chk('det of the pulled-back metric at x = 0.6', fx(a, 5), 'x² sin²1.1 / 16 = 0.01787 (computed here)', Math.abs(a - 0.6*0.6*Math.sin(1.1)**2/16) < 1e-8), chk('det on the fold line', fe(Math.abs(b)), '0', Math.abs(b) < 1e-12),
        chk('intrinsic g(V,V)/‖X‖² on the fold line, 200 vectors', '1 ± ' + fe(w), '1 (positive for every V ≠ 0, §2)', w < 1e-12)]; } };
})());

/* 7. Two kinds of nothing — a fold against a closing gap (§4, §8) */
EYES.push((() => {
  const L0 = V3(-1.9, 0, 0), R1 = 1.05, Rx = V3(1.7, -0.2, 0);
  return { id:'nothing', title:'Two ways the pullback degenerates', section:'§4.1, §8.5', grade:'proved',
    eq:'fold: det 𝛾*𝑔 = 0, while 𝛱 keeps moving\nclosing gap: 𝛱 itself is undefined,  ‖𝛱₁ − 𝛱₂‖ = |𝑛₁ − 𝑛₂| / √2',
    text:'Left: the fold line of the map from the fold example. The pulled-back metric is degenerate along it, yet the marker continues to move along the fold line: the subspace keeps changing. Right: the two energy surfaces near a Dirac point, with half gap m. When the gap is closed, the lower-band projector approached along two different directions tends to two different limits, so 𝛱 is not defined at the touching point. In a chart both cases appear as a zero, of det g at the fold and of the gap at the Dirac point; only the closing gap leaves a point at which 𝛱 is undefined.',
    legend:[['#ffb547','the fold line'],['#5ab0ff','upper band'],['#4fe3c1','lower band'],['#ffffff','two approach paths']],
    controls:[{id:'m', label:'Half gap m', min:0, max:0.6, step:0.01, value:0}, {id:'a', label:'Angle between the approach paths (degrees)', min:20, max:180, step:1, value:90, dp:0}],
    view:[0.25, 0.42, 7.4, 0],
    make(g, ctx){ sphereRig(g, R1, 0.45, L0);
      const cr = []; for(let k=0;k<=40;k++) cr.push(onS(IQ.foldN(0, -0.3 + 1.2*k/40), R1*1.01).add(L0)); g.add(M.tube(cr, 0.014, PAL.gap, 0.95));
      ctx.cp = M.orb(0.04, 0xffffff, 7); g.add(ctx.cp); ctx.ctr = M.trail(90, 0.06); g.add(ctx.ctr);
      ctx.up = M.surface(41, 41, -1.1, 1.1, -1.1, 1.1, 0.5); ctx.dn = M.surface(41, 41, -1.1, 1.1, -1.1, 1.1, 0.5); ctx.up.position.copy(Rx); ctx.dn.position.copy(Rx); g.add(ctx.up); g.add(ctx.dn);
      ctx.w1 = M.orb(0.04, 0xffffff, 7); ctx.w2 = M.orb(0.04, 0xffffff, 7); g.add(ctx.w1); g.add(ctx.w2); ctx.t1 = M.trail(70, 0.06); ctx.t2 = M.trail(70, 0.06); g.add(ctx.t1); g.add(ctx.t2);
      ctx.a1 = M.arrow(PAL.metric, 0.6, 0.12); ctx.a2 = M.arrow(PAL.tip, 0.6, 0.12); g.add(ctx.a1); g.add(ctx.a2);
      ctx.callout(V3(-1.9, 1.05, 0), 'A fold', 'det g = 0, yet 𝛱 keeps moving', '#ffb547', -40, -40); ctx.callout(() => Rx.clone().add(V3(0, 0.75*ctx.p.m, 0)), 'A closing gap', 'no single limit of 𝛱', '#ff6f91', 40, -46); this.change(ctx); },
    change(ctx){ const m = ctx.p.m, E = (x, z) => 0.75*Math.sqrt(m*m + x*x + z*z), xs = a => -1.1 + 2.2*a/40;
      M.setSurface(ctx.up, (a, b) => E(xs(a), xs(b)), () => [0.12, 0.3, 0.6]); M.setSurface(ctx.dn, (a, b) => -E(xs(a), xs(b)), () => [0.08, 0.38, 0.33]); },
    step(dt, t, ctx){ const k = (0.5 + 0.5*Math.sin(0.6*t)), y = -0.3 + 1.2*k, n = IQ.foldN(0, y), P = onS(n, R1*1.02).add(L0); ctx.cp.position.copy(P); M.pushTrail(ctx.ctr, P, [1,0.8,0.45]);
      const n0 = IQ.foldN(0, -0.3), along = IQ.piDist(n0, n);
      const m = ctx.p.m, al = rad(ctx.p.a), r = Math.max(0, 1 - ((t*0.35) % 1.25)), E = (x, z) => -0.75*Math.sqrt(m*m + x*x + z*z);
      const p1 = V3(r, 0, 0), p2 = V3(r*Math.cos(al), 0, r*Math.sin(al)); [ [ctx.w1, ctx.t1, p1], [ctx.w2, ctx.t2, p2] ].forEach(([o, tr, p]) => { const Q = V3(p.x, E(p.x, p.z), p.z).add(Rx); o.position.copy(Q); M.pushTrail(tr, Q, [1,1,1]); });
      const na = IQ.approach(m, 0, Math.max(r, 1e-9)), nb = IQ.approach(m, al, Math.max(r, 1e-9));
      M.setArrow(ctx.a1, Rx.clone().add(V3(0, 0.9, 0)), V3(na[0], na[2], na[1]).multiplyScalar(0.65)); M.setArrow(ctx.a2, Rx.clone().add(V3(0, 0.9, 0)), V3(nb[0], nb[2], nb[1]).multiplyScalar(0.65));
      const end = IQ.piDist(IQ.approach(m, 0, 1e-9), IQ.approach(m, al, 1e-9));
      return [['Along the fold line, 𝛱 has moved', fx(along, 4), 'gap'], ['Gap at the touching point', fx(2*m, 3), 'gap'], ['Distance between the two limits', fx(end, 4), end > 1e-6 ? 'tip' : 'tail'], ['Exact at m = 0', fx(Math.sqrt(2)*Math.sin(al/2), 4)]]; },
    test(){ const d0 = IQ.piDist(IQ.approach(0, 0, 1e-9), IQ.approach(0, Math.PI/2, 1e-9)), d1 = IQ.piDist(IQ.approach(0.3, 0, 0), IQ.approach(0.3, Math.PI/2, 0)), al = IQ.piDist(IQ.foldN(0, -0.3), IQ.foldN(0, 0.9));
      return [chk('closed gap, approach paths 90° apart', fx(d0, 6), '1 (two different limits)', Math.abs(d0 - 1) < 1e-9), chk('open gap, same two approach paths', fe(d1), '0 (one limit)', d1 < 1e-12), chk('the subspace moves along the fold line', fx(al, 4), '> 0 (det g = 0, yet 𝛱 moves)', al > 0.1)]; } };
})());

/* 8 and 9 share the terrain machinery */
function geodesicEye(o){
  const fam = Cr.families[o.fam];
  const runAll = (th, n) => Cr.geodesic(fam.a, fam.b, o.x0, o.y0, th, o.T1, n);
  const clip = p => { const out = []; for(const q of p){ if(q[0] > o.xr[1] + 0.02 || q[1] > o.yr[1] + 0.01 || q[1] < o.yr[0] - 0.01) break; out.push(q); } return out; };
  const turnY = (path, low) => { let k = 0; path.forEach((q, i) => { if(low ? q[1] < path[k][1] : q[1] < path[k][1]) k = i; }); if(k < 1 || k > path.length-2) return path[k][1];
    const a = path[k-1][1], b = path[k][1], c = path[k+1][1], den = a - 2*b + c; return den > 0 ? b - (a - c)*(a - c)/(8*den) : b; };
  const drift = (path, th, n) => { const dt = o.T1/n, C0 = fam.a(0, o.y0)*Math.sin(rad(th))**2; let w = 0;
    for(let i=1;i<path.length-1;i++){ const y = path[i][1], u = (path[i+1][0]-path[i-1][0])/(2*dt), a = fam.a(0, y); w = Math.max(w, Math.abs(a*a*u*u - C0)); } return {C0, w}; };
  const X = o.X, Z = o.Z, H = o.H, P = (x, y, l) => V3(X(x), H(y) + (l||0.012), Z(y));
  return { id:o.id, title:o.title, section:o.section, grade:'proved', gradeLabel:'Proved and integrated', eq:o.eq, text:o.text, legend:o.legend,
    controls:[{id:'th', label:'Incidence of the adjustable path (degrees)', min:5, max:85, step:1, value:o.th0, dp:0}], view:o.view,
    make(g, ctx){ const N = 90, Mm = 70, s = M.surface(N, Mm, X(o.xr[0]), X(o.xr[1]), Z(o.yr[0]), Z(o.yr[1]), 0.8); g.add(s);
      const yAt = b => o.yr[0] + (o.yr[1]-o.yr[0])*b/(Mm-1), lo = C3(0x0a1530), hi = C3(0x2f7fd8), am = C3(0xffb547);
      M.setSurface(s, (a, b) => H(yAt(b)), (a, b) => { const y = yAt(b), c = lo.clone().lerp(hi, Math.min(1, o.idx(y)/o.idxMax)); if(o.amber) c.lerp(am, o.amber(y)); return [c.r, c.g, c.b]; });
      if(o.decor) o.decor(g, P, ctx);
      ctx.paths = o.show.map(th => { const pts = clip(runAll(th, 2600)).map(q => P(q[0], q[1], 0.02)); g.add(M.tube(pts, 0.011, PAL.metric, 0.5));
        const ys = o.turn(o.y0, rad(th)), lv = []; for(let i=0;i<=40;i++) lv.push(P(o.xr[0] + (o.xr[1]-o.xr[0])*i/40, o.sign*ys, 0.015)); g.add(M.dashed(lv, PAL.gap, 0.4));
        const b = M.orb(0.03, PAL.metric, 5); g.add(b); const tr = M.trail(90, 0.08); g.add(tr); return {pts, b, tr}; });
      ctx.mine = M.tube([V3(), V3(0,0.01,0)], 0.019, 0xffffff, 0.95); g.add(ctx.mine); ctx.mlv = M.dashed([V3(), V3(0.1,0,0)], 0xffffff, 0.8); g.add(ctx.mlv);
      ctx.mb = M.orb(0.04, 0xffffff, 5); g.add(ctx.mb); ctx.mtr = M.trail(120, 0.11); g.add(ctx.mtr);
      const st = M.orb(0.04, 0xffffff, 5); st.position.copy(P(o.x0, o.y0, 0.03)); g.add(st); const base = M.grid(5, 25, 0x5ab0ff, 0.05); base.position.y = -0.03; g.add(base); this.change(ctx); },
    change(ctx){ const th = ctx.p.th, path = runAll(th, 2600), fine = runAll(th, 26000); ctx.myPts = clip(path).map(q => P(q[0], q[1], 0.03)); M.setTube(ctx.mine, ctx.myPts);
      const ys = o.turn(o.y0, rad(th)), lv = []; for(let i=0;i<=40;i++) lv.push(P(o.xr[0] + (o.xr[1]-o.xr[0])*i/40, o.sign*ys, 0.02)); M.setDashed(ctx.mlv, lv);
      ctx.pred = ys; ctx.obs = turnY(fine); ctx.dr = drift(fine, th, 26000); M.clearTrail(ctx.mtr); },
    step(dt, t, ctx){ const f = (t*0.2) % 1;
      ctx.paths.forEach(p => { if(!p.pts.length) return; const i = Math.max(0, Math.floor(f*(p.pts.length-1))); p.b.position.copy(p.pts[i]); M.pushTrail(p.tr, p.pts[i], [0.35,0.69,1.0]); });
      if(ctx.myPts.length){ const j = Math.max(0, Math.floor(f*(ctx.myPts.length-1))); ctx.mb.position.copy(ctx.myPts[j]); M.pushTrail(ctx.mtr, ctx.myPts[j], [1,1,1]); }
      return o.rows(ctx); },
    test(ctx){ return o.tests(runAll, turnY); } };
}
const C3 = c => new T.Color(c);

/* 8. Frozen ridge — total internal reflection at a polar stratum (§8.3–8.4, Figure 10) */
EYES.push(geodesicEye({ id:'ridge', title:'Total internal reflection', section:'§8.3–8.4, Figure 10', fam:'polar', x0:0.08, y0:0.6, T1:2.6, th0:35, show:[20, 35, 50, 65], sign:1,
  xr:[0, 2.6], yr:[-0.15, 0.85], X:x => (x - 1.3)*1.5, Z:y => (0.35 - y)*2.6, H:y => 1.7*Math.abs(Math.sin(y)), idx:y => 1.5*Math.abs(Math.sin(y)), idxMax:1.15, amber:y => Math.max(0, 1 - Math.abs(y)/0.05)*0.85,
  turn:(y0, th) => IQ.polarTurn(y0, th), view:[0.95, 0.62, 6.4, 0.25],
  eq:'𝑔∥ sin²𝜃 = 𝐶      𝑔∥ = (9/4) sin²𝑦\nturning line:  sin 𝑦* = sin 𝑦₀ sin 𝜃₀',
  text:'Along y = 0 the whole line is one projector: the subspace stops rotating there, so the index √g∥ falls to zero while the gap stays at 2. Each geodesic carries a conserved Clairaut level C = g∥ sin²θ, and since sin²θ ≤ 1 it can only reach points where g∥ ≥ C. A geodesic launched toward the polar stratum turns back tangentially where g∥ = C, as in total internal reflection in optics. Only an exactly normal path reaches the stratum.',
  legend:[['#5ab0ff','geodesics, launched at y = 0.60'],['#ffffff','the adjustable path'],['#ffb547','the polar line and turning levels']],
  decor(g, P, ctx){ const pole = []; for(let i=0;i<=60;i++) pole.push(P(2.6*i/60, 0, 0.02)); g.add(M.tube(pole, 0.022, PAL.gap, 0.95));
    ctx.callout(P(1.9, 0, 0.02), 'The polar line', 'the whole line is one projector; gap = 2', '#ffb547', 40, 44); ctx.callout(P(0.08, 0.6, 0.03), 'Launch', 'y = 0.60', '#ffffff', -50, -36); },
  rows:ctx => [['Clairaut level C = g∥ sin²θ at launch', fx(ctx.dr.C0, 8), 'metric'], ['Predicted turning line y*', fx(ctx.pred, 8), 'gap'], ['Integrated turning line', fx(ctx.obs, 8), 'metric'],
    ['Difference', fe(Math.abs(ctx.obs - ctx.pred))], ['Drift of g∥ sin²θ (from path samples)', fe(ctx.dr.w)], ['Paper at 35°', 'C 0.23600011 · y* 0.32981248', 'tail']],
  tests(runAll, turnY){ const y = turnY(runAll(35, 26000)), C = Cr.families.polar.a(0, 0.6)*Math.sin(rad(35))**2; let lowest = 9; for(let th=20; th<=89; th+=3) lowest = Math.min(lowest, turnY(runAll(th, 8000)));
    return [chk('Clairaut level at 35°', fx(C, 8), '0.23600011', Math.abs(C - 0.23600011) < 5e-9), chk('integrated turning line at 35°', fx(y, 8), '0.32981248', Math.abs(y - 0.32981248) < 5e-9), chk('every incidence 20° to 89° turns before y = 0', 'lowest y ' + fx(lowest, 4), 'none reaches the stratum', lowest > 0)]; } }));

/* 9. Pinched canyon — guiding where the gap narrows (§8.6, Figure 14) */
EYES.push(geodesicEye({ id:'canyon', title:'When the gap narrows instead', section:'§8.6, Figure 14', fam:'narrow', x0:0, y0:0.8, T1:3.0, th0:50, show:[35, 50, 65], sign:-1,
  xr:[-0.1, 4.2], yr:[-1.6, 1.6], X:x => (x - 2.05)*0.95, Z:y => -y*0.95, H:y => 0.9/Math.sqrt(1 + 6.25*y*y), idx:y => 1.5/Math.sqrt(1 + 6.25*y*y), idxMax:1.5, amber:null,
  turn:(y0, th) => IQ.narrowTurn(y0, th), view:[0.55, 0.55, 8.6, 0.55],
  eq:'𝛴 = cos 3𝑥 𝜎₁ + sin 3𝑥 𝜎₂ + 2.5𝑦 𝜎₃,   gap 2√(1 + 6.25𝑦²)\n𝑔∥ = 9 / (4(1 + 6.25𝑦²)),   the same refraction law',
  text:'Here the gap narrows toward y = 0 (amber curves) while the subspace never stops rotating, so the index √g∥ rises, and the surface, whose height shows the index, rises with it. The same Clairaut law now guides instead of reflecting: paths bend toward the narrow-gap line, cross it, and turn back only on the far side, where the index has fallen to their conserved level, as a graded-index fibre guides light.',
  legend:[['#5ab0ff','geodesics from y = 0.8'],['#ffffff','the adjustable path'],['#ffb547','the gap, narrowest at y = 0']],
  decor(g, P, ctx){ const X = x => (x - 2.05)*0.95, Z = y => -y*0.95; [1, -1].forEach(sg => { const pts = []; for(let k=0;k<=60;k++){ const y = -1.6 + 3.2*k/60; pts.push(V3(X(-0.1) - 0.35, 1.25 + sg*0.22*Math.sqrt(1 + 6.25*y*y), Z(y))); } g.add(M.tube(pts, 0.014, PAL.gap, 0.9)); });
    ctx.callout(V3(X(-0.1) - 0.35, 1.47, 0), 'The narrowing gap', 'narrowest at y = 0', '#ffb547', 40, -40); ctx.callout(P(2.0, 0, 0.02), 'Guiding line', 'index largest here', '#5ab0ff', 40, 40); },
  rows:ctx => [['Predicted turning level (Clairaut)', fx(ctx.pred, 6), 'gap'], ['Integrated turning point', fx(ctx.obs, 6), 'metric'], ['Difference', fe(Math.abs(Math.abs(ctx.obs) - ctx.pred))],
    ['Drift of g∥ sin²θ (from path samples)', fe(ctx.dr.w)], ['Paper at 50°', 'turns at −1.0969', 'tail']],
  tests(runAll, turnY){ const y = turnY(runAll(50, 30000)); return [chk('integrated turning point at 50°', fx(y, 5), '−1.0969', Math.abs(y + 1.0969) < 1e-4), chk('the path crosses the narrow-gap line first (guided, not reflected)', 'turns at y < 0', 'crosses y = 0', y < 0)]; } }));

/* 10. Walls set the speed (§5.2, §12.1, Figure 17 right) */
EYES.push((() => {
  const F = Cr.makeFeed(11), K = 3, S = 121, SX = s => s*1.0, EY = (w, w0) => -0.2 + (w - w0)*0.42, VY = v => -1.9 + 0.5*v;
  return { id:'speed', title:'The gap limits the driving speed', section:'§5.2, Theorem 5.2, Figure 17', grade:'proved',
    eq:'√𝑔 ≤ √𝑘 ‖∂ₜ𝛴‖ / 𝛥\nduration ≥ 𝛥ₘᵢₙ 𝓛 / (√𝑘 sup‖∂ₜ𝛴‖)',
    text:'Back plane: the six energy levels as the drive parameter s sweeps, with the three occupied levels in teal and the gap above them shaded amber. Front plane: the speed √g of the occupied subspace in the intrinsic metric (blue), beneath the ceiling √k‖∂ₜΣ‖/Δ set by the drive and the gap (amber), as in Theorem 5.2. Where the gap narrows, the ceiling falls toward the speed; where the gap widens, the speed stays well below the ceiling.',
    legend:[['#4fe3c1','the three occupied levels'],['#ffb547','gap and ceiling'],['#5ab0ff','speed of the occupied subspace']],
    controls:[{id:'outer', label:'Outer gap', min:0.3, max:2.5, step:0.05, value:0.9}, {id:'inner', label:'Inner spacing', min:0.05, max:0.6, step:0.01, value:0.3}],
    view:[0.25, 0.22, 8.4, -0.15],
    make(g, ctx){ ctx.lv = []; for(let i=0;i<6;i++){ const l = M.tube([V3(), V3(0,0.01,0)], 0.012, i < 3 ? PAL.tail : 0x6f7f9c, i < 3 ? 0.9 : 0.6); l.position.z = -0.9; g.add(l); ctx.lv.push(l); }
      ctx.fill = new T.Mesh(new T.BufferGeometry(), new T.MeshBasicMaterial({color:PAL.gap, transparent:true, opacity:0.14, side:T.DoubleSide, depthWrite:false, blending:T.AdditiveBlending})); ctx.fill.position.z = -0.9; g.add(ctx.fill);
      ctx.sp = M.tube([V3(), V3(0,0.01,0)], 0.02, PAL.metric, 0.95); ctx.ce = M.tube([V3(), V3(0,0.01,0)], 0.014, PAL.gap, 0.9); ctx.sp.position.z = 0.5; ctx.ce.position.z = 0.5; g.add(ctx.sp); g.add(ctx.ce);
      ctx.b = M.orb(0.05, 0xffffff, 6); g.add(ctx.b); ctx.dl = M.dashed([V3(), V3(0,1,0)], 0xffffff, 0.4); g.add(ctx.dl);
      ctx.callout(() => ctx.b.position, 'Speed √g', 'of the occupied subspace', '#5ab0ff', 40, 30); ctx.callout(() => ctx.ceilAt, 'Ceiling √k‖∂Σ‖/Δ', 'set by the drive and the gap', '#ffb547', 40, -40); ctx.ceilAt = V3();
      const fl = M.grid(5, 20, 0x5ab0ff, 0.05); fl.position.y = -1.95; g.add(fl); this.change(ctx); },
    change(ctx){ const o = ctx.p.outer, n = ctx.p.inner, ss = [], W = [], V = [], Cc = []; let worst = 0;
      for(let i=0;i<S;i++){ const s = -2 + 4*i/(S-1), e = Cr.eigh(Cr.feedOp(F, n, o, s)), r = Cr.speed(F, n, o, s, K); ss.push(s); W.push(e.w); V.push(r.v); Cc.push(r.ceil); worst = Math.max(worst, r.v/r.ceil); }
      const w0 = Math.min(...W.map(w => w[0]));
      ctx.lv.forEach((l, k) => M.setTube(l, ss.map((s, i) => V3(SX(s), EY(W[i][k], w0), 0))));
      const pos = []; for(let i=0;i<S-1;i++){ const a = V3(SX(ss[i]), EY(W[i][2], w0), 0), b = V3(SX(ss[i+1]), EY(W[i+1][2], w0), 0), c = V3(SX(ss[i+1]), EY(W[i+1][3], w0), 0), d = V3(SX(ss[i]), EY(W[i][3], w0), 0); pos.push(a,b,c, a,c,d); }
      ctx.fill.geometry.dispose(); ctx.fill.geometry = new T.BufferGeometry().setFromPoints(pos);
      M.setTube(ctx.sp, ss.map((s, i) => V3(SX(s), VY(V[i]), 0))); M.setTube(ctx.ce, ss.map((s, i) => V3(SX(s), Math.min(1.6, VY(Cc[i])), 0)));
      Object.assign(ctx, {ss, V, Cc, worst}); },
    step(dt, t, ctx){ const i = Math.floor(((Math.sin(0.35*t)+1)/2)*(S-1)), s = ctx.ss[i], P = V3(SX(s), VY(ctx.V[i]), 0.5); ctx.b.position.copy(P); ctx.ceilAt = V3(SX(s), Math.min(1.6, VY(ctx.Cc[i])), 0.5); M.setDashed(ctx.dl, [P, ctx.ceilAt]);
      return [['Drive position s', fx(s, 2)], ['Speed √g', fx(ctx.V[i], 4), 'metric'], ['Ceiling √k‖∂Σ‖/Δ', fx(ctx.Cc[i], 4), 'gap'], ['Speed over ceiling here', fx(ctx.V[i]/ctx.Cc[i], 3)], ['Largest over the whole sweep', fx(ctx.worst, 3) + ' ≤ 1', 'tail']]; },
    test(){ const F2 = Cr.makeFeed(11); let w = 0; for(let i=0;i<60;i++){ const r = Cr.speed(F2, 0.3, 0.9, -2 + 4*i/59, 3); w = Math.max(w, r.v/r.ceil); } return [chk('largest speed over ceiling, 60 points', fx(w, 3), '≤ 1 (Theorem 5.2)', w <= 1)]; } };
})());

/* 11. The toll — friction on projector rotations (§5.3, Theorem 5.3, Figure 4) */
EYES.push((() => {
  const D1 = 1.0, D2 = 2.6, ARC = 2.2, L = ARC/2;
  const wgt = (D, Gm) => 2*(Gm/(Gm*Gm + D*D))*D;
  const axis = V3(0.3, 1, 0.2).normalize(), start = V3(1, 0, 0).sub(axis.clone().multiplyScalar(axis.x)).normalize();
  const arcPt = (s, r) => start.clone().applyAxisAngle(axis, ARC*s - ARC/2).multiplyScalar(r || R0);
  return { id:'toll', title:'Friction on projector rotations', section:'§5.3, Theorem 5.3, Figure 4', grade:'proved', gradeLabel:'Proved; protocols computed here',
    eq:'min 2𝑐(𝛥ₙ)𝛥ₙ · 𝑔 ≤ 𝜁ᵣₒₜ ≤ max 2𝑐(𝛥ₙ)𝛥ₙ · 𝑔\n𝑊ₑₓ ≥ (min 2𝑐(𝛥ₙ)𝛥ₙ) 𝓛² / 𝑇',
    text:'Moving the subspace while the system is coupled to a bath dissipates work. The friction on projector rotations is the intrinsic metric reweighted by the spectrum and the bath; at zero temperature the friction per unit metric lies in a band between the weights 2c(Δₙ)Δₙ of the two excited levels (amber bar). Two markers traverse the same path in the same time T. The white marker moves at constant intrinsic speed, and its excess work equals the friction weight times 𝓛²/𝑇; the rose marker accelerates and decelerates, and its excess work is always larger.',
    legend:[['#ffffff','constant speed'],['#ff6f91','uneven speed'],['#ffb547','the zero-temperature band']],
    controls:[{id:'T', label:'Time allowed T', min:1, max:8, step:0.1, value:3}, {id:'ease', label:'Speed variation of the rose marker', min:0, max:0.95, step:0.01, value:0.6},
      {id:'mix', label:'Drive weight on the second excited level', min:0, max:1, step:0.01, value:0.3}, {id:'G', label:'Bath rate Γ', min:0.2, max:3, step:0.05, value:1}],
    view:[0.9, 0.36, 7.3, 0.1],
    make(g, ctx){ sphereRig(g, R0, 0.4); const pts = []; for(let i=0;i<=80;i++) pts.push(arcPt(i/80, R0*1.01)); g.add(M.tube(pts, 0.012, 0x9fb4d8, 0.7));
      ctx.c = M.orb(0.05, 0xffffff, 6); ctx.e = M.orb(0.05, PAL.tip, 6); g.add(ctx.c); g.add(ctx.e); ctx.ct = M.trail(60, 0.07); ctx.et = M.trail(60, 0.07); g.add(ctx.ct); g.add(ctx.et);
      ctx.mc = M.bar(0.22, 0.22, 0xffffff); ctx.me = M.bar(0.22, 0.22, PAL.tip); ctx.mc.position.set(2.15, -1.2, -0.25); ctx.me.position.set(2.15, -1.2, 0.25); g.add(ctx.mc); g.add(ctx.me);
      ctx.floor = M.dashed([V3(1.9, 0, 0), V3(2.4, 0, 0)], PAL.gap, 0.9); g.add(ctx.floor);
      ctx.band = M.slab(0.12, 1, 0.12, PAL.gap, 0.35); ctx.band.position.set(-2.4, 0, 0); g.add(ctx.band); ctx.bm = M.orb(0.045, PAL.gap, 6); g.add(ctx.bm);
      ctx.callout(V3(2.4, -1.2, 0.5), 'Excess work', 'white: constant speed · rose: uneven', '#9fb4d8', 30, 40); ctx.callout(() => ctx.bm.position, 'Zero-temperature band', 'friction per unit metric', '#ffb547', -40, -40); ctx.acc = 0; ctx.last = 0; this.change(ctx); },
    change(ctx){ const p = ctx.p, w1 = wgt(D1, p.G), w2 = wgt(D2, p.G), k = (1-p.mix)*w1 + p.mix*w2, lo = Math.min(w1, w2), hi = Math.max(w1, w2);
      const a = IQ.toll(L, p.T, 0), b = IQ.toll(L, p.T, p.ease); Object.assign(ctx, {w1, w2, k, lo, hi, Wc:k*a.W, We:k*b.W, floorW:lo*L*L/p.T, sE:b.s});
      const sc = 1.6/Math.max(1e-6, ctx.We*1.05); ctx.sc = sc; ctx.floor.position.y = -1.2 + ctx.Wc*sc;
      ctx.band.scale.y = Math.max(0.02, (hi - lo)*2.2); ctx.band.position.y = -1.2 + (lo + hi)/2*2.2; ctx.bm.position.set(-2.4, -1.2 + k*2.2, 0); },
    step(dt, t, ctx){ const T = ctx.p.T, tau = t % (T*1.3), x = Math.min(1, tau/T), se = ctx.sE(Math.min(T, tau)); const Pc = arcPt(x, R0*1.02), Pe = arcPt(se, R0*1.04);
      ctx.c.position.copy(Pc); ctx.e.position.copy(Pe); M.pushTrail(ctx.ct, Pc, [1,1,1]); M.pushTrail(ctx.et, Pe, [1,0.44,0.57]);
      M.setBar(ctx.mc, Math.max(0.01, ctx.Wc*x*ctx.sc)); const part = IQ.toll(L*se, Math.max(1e-3, Math.min(T, tau)), 0); M.setBar(ctx.me, Math.max(0.01, Math.min(ctx.We, ctx.k*IQ.toll(L, T, ctx.p.ease).W*Math.pow(x, 1))*ctx.sc));
      return [['Weights 2c(Δₙ)Δₙ for gaps 1 and 2.6', fx(ctx.w1, 3) + ', ' + fx(ctx.w2, 3), 'gap'], ['Friction per unit metric (inside the band)', fx(ctx.k, 3), 'gap'],
        ['Intrinsic length 𝓛 of the path', fx(L, 3), 'metric'], ['Excess work, constant speed', fx(ctx.Wc, 4)], ['Excess work, uneven speed', fx(ctx.We, 4), 'tip'], ['Floor (min weight) 𝓛²/T', fx(ctx.floorW, 4), 'tail']]; },
    test(){ const a = IQ.toll(1.1, 3, 0), b = IQ.toll(1.1, 3, 0.6); let inside = true; for(let i=0;i<=20;i++){ const G = 0.2 + 2.8*i/20, w1 = wgt(1, G), w2 = wgt(2.6, G); for(let j=0;j<=10;j++){ const k = (1-j/10)*w1 + j/10*w2; if(k < Math.min(w1,w2) - 1e-12 || k > Math.max(w1,w2) + 1e-12) inside = false; } }
      return [chk('constant speed: work equals 𝓛²/T', fx(a.W, 6) + ' vs ' + fx(a.bound, 6), 'equality only at constant speed (Theorem 6.3)', Math.abs(a.W - a.bound) < 1e-9), chk('uneven speed: work exceeds 𝓛²/T', fx(b.W, 4) + ' > ' + fx(b.bound, 4), '> floor', b.W > b.bound), chk('friction stays inside the band', inside ? 'every mix and rate' : 'left the band', '(5.4)', inside)]; } };
})());

window.__IQGT_EYES_B = EYES;
})();
