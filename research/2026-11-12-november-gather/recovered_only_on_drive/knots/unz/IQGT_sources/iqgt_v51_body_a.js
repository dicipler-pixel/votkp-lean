/* SCRIPT: iqgt_mixer_3d_v5_body — IQGT Mixer 3D v5 eyes, written for this paper (v7.3.1) on 3D Mixer Parts v3.
   Every number the paper prints is shown beside the number the mixer computes, labelled. */
(() => {
const M = API, V3 = (x,y,z) => new T.Vector3(x,y,z), Cr = window.Core, IQ = window.IQ;
const R0 = 1.55, onS = (n, r) => V3(n[0]*(r||R0), n[2]*(r||R0), n[1]*(r||R0));
const deg = r => r*180/Math.PI, rad = d => d*Math.PI/180;
const fx = (x, d) => (+x).toFixed(d), fe = x => (+x).toExponential(1);
const chk = (label, mixer, paper, ok) => ({label, mixer, paper, ok});
const med = a => a.slice().sort((p,q) => p-q)[a.length>>1];
const C3 = c => new T.Color(c);
function sphereRig(g, r, opacity){ r = r || R0; g.add(M.glass(r, PAL.metric, 2.6, opacity == null ? 0.5 : opacity)); g.add(M.dust(900, r*1.03, r*1.35, 0x5ab0ff, 0.045, 11));
  const eq = []; for(let i=0;i<=160;i++){ const a = 2*Math.PI*i/160; eq.push(V3(r*Math.cos(a), 0, r*Math.sin(a))); } g.add(M.line(eq, 0x2a3b5c, 0.7));
  const mer = []; for(let i=0;i<=160;i++){ const a = Math.PI*i/160; mer.push(V3(r*Math.sin(a), r*Math.cos(a), 0)); } g.add(M.line(mer, 0x22324f, 0.5));
  const np = M.orb(0.022, 0x9fb4d8, 4); np.position.set(0, r, 0); g.add(np); }
/* small 3x3 helpers for real frames */
const mm = Cr.matmul, tr = Cr.T;
function polarAlign(U, U0){ const A = mm(tr(U), U0), e = Cr.eigh(mm(tr(A), A)), k = A.length;
  const inv = Array.from({length:k}, (_, i) => Float64Array.from({length:k}, (_, j) => { let s = 0; for(let a=0;a<k;a++) s += e.V[i][a]*e.V[j][a]/Math.sqrt(Math.max(1e-300, e.w[a])); return s; }));
  return mm(U, mm(A, inv)); }
const proj = U => mm(U, tr(U));
const hsDiff = (A, B) => { let s = 0; for(let i=0;i<A.length;i++) for(let j=0;j<A.length;j++) s += (A[i][j]-B[i][j])**2; return Math.sqrt(s); };
function rot3(axis, ang){ const [x,y,z] = axis, c = Math.cos(ang), s = Math.sin(ang), t = 1-c;
  return [Float64Array.from([t*x*x+c, t*x*y-s*z, t*x*z+s*y]), Float64Array.from([t*x*y+s*z, t*y*y+c, t*y*z-s*x]), Float64Array.from([t*x*z-s*y, t*y*z+s*x, t*z*z+c])]; }
function ladder(g, x, n){ const rings = []; for(let i=0;i<n;i++){ const r = M.ring(0.42, PAL.dim, 0.008, 0.85); r.rotation.x = Math.PI/2; r.position.x = x; g.add(r); rings.push(r); } return rings; }
function placeLadder(rings, w, y0, sc, k, x){ const lo = w[0]; rings.forEach((r, i) => { r.position.y = y0 + (w[i]-lo)*sc; r.material.color.set(i < k ? PAL.tail : 0x6f7f9c); r.position.x = x; }); }
const EYES = [];

/* ================= Act I: the tensor and its pullbacks ================= */

/* 1. Charts on the sky — the pullback (§4.1) */
EYES.push((() => {
  const pathAt = t => { const th = 1.25 + 0.55*Math.sin(0.7*t), ph = ((0.5*t) % (2*Math.PI) + 2*Math.PI) % (2*Math.PI); return [th, ph, [0.385*Math.cos(0.7*t), 0.5]]; };
  function lengths(th, ph, xd, w){ const uv = IQ.chartInv(th, ph, w), J = IQ.chartJ(uv[0], uv[1], w), det = J[0][0]*J[1][1]-J[0][1]*J[1][0];
    const ud = [( J[1][1]*xd[0]-J[0][1]*xd[1])/det, (-J[1][0]*xd[0]+J[0][0]*xd[1])/det], GA = IQ.gRound(th), GB = IQ.pull(GA, J);
    const h = 1e-6, P = s => IQ.piOf(IQ.sph(th + xd[0]*s, ph + xd[1]*s)), V = IQ.sub2(P(h), P(-h), 1/(2*h));
    return { uv, GA, GB, lA:IQ.quad(GA, xd, xd), lB:IQ.quad(GB, ud, ud), lT:IQ.Q2(P(0), V, V)[0] }; }
  return { id:'charts', title:'Pullback of the metric under a change of chart', section:'§4.1, Figure 3', grade:'proved',
    eq:'𝛾*𝑄 = 𝑄ᵢⱼ = ⟨∂ᵢ𝜓|(1 − |𝜓⟩⟨𝜓|)|∂ⱼ𝜓⟩\n𝑄(𝑉,𝑉) = Tr(𝛱 𝑉†𝑉)',
    text:'The grid is a coordinate chart on the Bloch sphere of states. Deforming the chart moves every coordinate line, and the components gᵢⱼ change by the tensor transformation rule. The tangent vector itself, shown as the arrow, is unchanged. Its squared length is the same in every chart and equals the intrinsic value Tr(𝛱𝑉†𝑉) on T Gr(k,H): the parameters only select a path through a geometry that exists independently of them.',
    legend:[['#9fc3ff','coordinate chart'],['#ffffff','the state and its coordinate lines'],['#5ab0ff','tangent vector']],
    controls:[{id:'w', label:'Chart deformation', min:0, max:1, step:0.01, value:0.65}],
    view:[0.6, 0.35, 5.6, 0],
    make(g, ctx){ sphereRig(g); ctx.grid = new T.Group(); g.add(ctx.grid);
      ctx.pt = M.orb(0.045, 0xffffff, 7); g.add(ctx.pt); ctx.ar = M.arrow(PAL.metric, 1, 0.16); g.add(ctx.ar); ctx.tr = M.trail(140, 0.07); g.add(ctx.tr);
      ctx.ku = M.line([], 0xdfe8ff, 0.9); ctx.kv = M.line([], 0xdfe8ff, 0.9); g.add(ctx.ku); g.add(ctx.kv); this.change(ctx); },
    change(ctx){ const w = ctx.p.w; ctx.grid.clear();
      for(let i=1;i<12;i++){ const u = i/12, pts = []; for(let k=0;k<=120;k++){ const q = IQ.chart(u, 2*Math.PI*k/120, w); pts.push(onS(IQ.sph(q[0], q[1]), R0*1.004)); } ctx.grid.add(M.line(pts, 0x6f9ee6, 0.28)); }
      for(let j=0;j<16;j++){ const v = 2*Math.PI*j/16, pts = []; for(let k=0;k<=80;k++){ const q = IQ.chart(k/80, v, w); pts.push(onS(IQ.sph(q[0], q[1]), R0*1.004)); } ctx.grid.add(M.line(pts, 0x6f9ee6, 0.28)); } },
    step(dt, t, ctx){ const w = ctx.p.w, [th, ph, xd] = pathAt(t), n = IQ.sph(th, ph), P = onS(n, R0*1.01);
      ctx.pt.position.copy(P); M.pushTrail(ctx.tr, P, [1,1,1]);
      const n2 = IQ.sph(th + xd[0]*0.01, ph + xd[1]*0.01), d = onS(n2).sub(onS(n)).multiplyScalar(80); M.setArrow(ctx.ar, P, d.clampLength(0.2, 0.9));
      const L = lengths(th, ph, xd, w), u0 = L.uv[0], v0 = L.uv[1], pu = [], pv = [];
      for(let k=0;k<=100;k++){ const q = IQ.chart(u0, 2*Math.PI*k/100, w); pu.push(onS(IQ.sph(q[0], q[1]), R0*1.006)); const r = IQ.chart(k/100, v0, w); pv.push(onS(IQ.sph(r[0], r[1]), R0*1.006)); }
      M.setLine(ctx.ku, pu); M.setLine(ctx.kv, pv);
      return [['g₁₁ in the round chart', fx(L.GA[0][0], 5)], ['g₁₁ in the deformed chart', fx(L.GB[0][0], 5), 'gap'],
        ['Squared length, round chart', fx(L.lA, 8), 'metric'], ['Squared length, deformed chart', fx(L.lB, 8), 'metric'], ['Intrinsic value, Tr(𝛱𝑉†𝑉)', fx(L.lT, 8), 'tail']]; },
    test(ctx){ const L = lengths(1.3, 0.9, [0.4, 0.7], 0.8); return [chk('one tangent vector in two charts and intrinsically', fx(L.lB, 8) + ' / ' + fx(L.lT, 8), 'equal (pullback, §4.1)', Math.abs(L.lA-L.lB) < 1e-7 && Math.abs(L.lA-L.lT) < 1e-6),
      chk('the components gᵢⱼ change with the chart', fx(L.GB[0][0], 3) + ' vs 0.250', 'they must change', Math.abs(L.GB[0][0]-0.25) > 0.01)]; } };
})());

/* 2. Spectral realization — the tangent law and the gap bound (§2–3) */
EYES.push((() => {
  const F = Cr.makeFeed(11), K = 3, INNER = 0.3, H1n = Cr.opnorm(F.H1);
  const base = outer => { const e = Cr.eigh(Cr.feedOp(F, INNER, outer, 0)); return { w:e.w, U:Cr.cols(e.V, [0,1,2]) }; };
  const at = (outer, s, U0) => { const e = Cr.eigh(Cr.feedOp(F, INNER, outer, s)); return { w:e.w, U:polarAlign(Cr.cols(e.V, [0,1,2]), U0) }; };
  function bound(outer, s, U0){ const h = 1e-5, a = proj(at(outer, s+h, U0).U), b = proj(at(outer, s-h, U0).U), w = at(outer, s, U0).w;
    let n = 0; for(let i=0;i<6;i++) for(let j=0;j<6;j++) n += ((a[i][j]-b[i][j])/(2*h))**2; return Math.sqrt(n) / (Math.sqrt(2*K)*H1n/(w[3]-w[2])); }
  return { id:'crew', title:'Spectral realization of tangent deformations', section:'§2, §3, Proposition 3.5', grade:'proved',
    eq:'𝑉 = 𝛱𝑉(1−𝛱) + (1−𝛱)𝑉𝛱\n‖𝑉‖ ≤ √(2𝑘) ‖𝛿𝛴‖ / 𝛥',
    text:'Three eigenvectors span an isolated spectral subspace, separated from the rest of the spectrum by the gap (amber slab). The teal bars are the entries of the projector 𝛱. A rotation within the subspace, a U(3) gauge transformation, changes the eigenvectors (rose bars) but leaves every entry of 𝛱 unchanged, so it is not a tangent vector on the Grassmannian. A perturbation that couples the subspace to its complement changes 𝛱, at a rate never larger than √(2k)‖𝛿𝛴‖/𝛥 (Proposition 3.5).',
    legend:[['#4fe3c1','projector 𝛱, entry by entry'],['#ff6f91','three eigenvectors'],['#ffb547','spectral gap']],
    choices:[{id:'mode', label:'Motion', value:'inside', options:[['inside','Rotation within the subspace'],['across','Coupling across the gap']]}],
    controls:[{id:'outer', label:'Outer gap', min:0.5, max:3, step:0.05, value:1.5}, {id:'drive', label:'Perturbation strength', min:0.05, max:0.6, step:0.01, value:0.35}],
    view:[0.62, 0.52, 9.0, -0.15], stageView:[0.62, 0.5, 8.6, 0.1],
    make(g, ctx){ g.position.x = 0.55; ctx.rings = ladder(g, -2.7, 6); ctx.slab = M.slab(1.1, 1, 1.1, PAL.gap, 0.22); ctx.slab.position.x = -2.7; g.add(ctx.slab);
      ctx.tw = []; for(let i=0;i<6;i++) for(let j=0;j<6;j++){ const b = M.bar(0.3, 0.3, PAL.tail); b.position.set(-0.55 + i*0.42, -0.6, -1.05 + j*0.42); g.add(b); ctx.tw.push(b); }
      ctx.fr = []; for(let i=0;i<6;i++) for(let a=0;a<3;a++){ const b = M.bar(0.26, 0.26, PAL.tip); b.position.set(-0.55 + i*0.42, -0.6, 1.55 + a*0.36); g.add(b); ctx.fr.push(b); }
      ctx.shipAt = V3(); ctx.callout(() => ctx.shipAt, 'Projector 𝛱', 'entry by entry', '#4fe3c1', 40, -50); ctx.callout(V3(1.55, -0.3, 2.27), 'Eigenvectors', 'three columns of 𝑈', '#ff6f91', 40, 46);
      ctx.gapAt = V3(-2.7, 0, 0.55); ctx.callout(() => ctx.gapAt, 'Spectral gap 𝛥', 'isolates the subspace', '#ffb547', -40, 46);
      const fl = M.grid(5.2, 26, 0x5ab0ff, 0.05); fl.position.y = -0.62; g.add(fl); this.change(ctx); },
    change(ctx){ ctx.B = base(ctx.p.outer); ctx.P0 = proj(ctx.B.U); },
    step(dt, t, ctx){ const ph = 0.9*t, outer = ctx.p.outer; let U, w, P;
      if(ctx.p.mode === 'inside'){ const R = rot3([1/Math.sqrt(3),1/Math.sqrt(3),1/Math.sqrt(3)], 1.4*Math.sin(ph)); U = mm(ctx.B.U, R); w = ctx.B.w; P = proj(ctx.B.U); }
      else { const s = ctx.p.drive*Math.sin(ph), r = at(outer, s, ctx.B.U); U = r.U; w = r.w; P = proj(U); ctx.s = s; }
      placeLadder(ctx.rings, w, -0.6, 0.55, 3, -2.7); const y2 = -0.6 + (w[2]-w[0])*0.55, y3 = -0.6 + (w[3]-w[0])*0.55; ctx.slab.scale.y = Math.max(0.01, y3-y2); ctx.slab.position.y = (y2+y3)/2; ctx.gapAt.y = (y2+y3)/2;
      for(let i=0;i<6;i++) for(let j=0;j<6;j++){ const b = ctx.tw[i*6+j]; M.setBar(b, 0.04 + 1.7*Math.abs(P[i][j])); b.material.emissiveIntensity = P[i][j] >= 0 ? 0.34 : 0.12; }
      { let bi = 0, bv = -1; for(let i=0;i<6;i++){ const v = Math.abs(P[i][i]); if(v > bv){ bv = v; bi = i; } } ctx.shipAt.set(-0.55 + bi*0.42, -0.6 + 0.04 + 1.7*bv, -1.05 + bi*0.42); }
      for(let i=0;i<6;i++) for(let a=0;a<3;a++) M.setBar(ctx.fr[i*3+a], 0.03 + 1.3*Math.abs(U[i][a]));
      const dP = hsDiff(P, ctx.P0), ang = deg(Cr.principal(U, ctx.B.U)[0]);
      const one = deg(Math.acos(Math.min(1, Math.abs(U.reduce((s, r, i) => s + r[0]*ctx.B.U[i][0], 0)))));
      const rows = [['‖𝛱 − 𝛱₀‖, change of the projector', fx(dP, 6), 'tail'], ['Largest principal angle', fx(ang, 3) + '°', 'tail'], ['Rotation of one eigenvector', fx(one, 2) + '°', 'tip']];
      if(ctx.p.mode === 'across'){ ctx.br = ctx.br == null || ctx.k % 10 === 0 ? bound(outer, ctx.s, ctx.B.U) : ctx.br; ctx.k = (ctx.k||0)+1; rows.push(['Rate relative to the bound (Prop. 3.5)', fx(ctx.br, 3) + ' ≤ 1', 'gap']); }
      else rows.push(['Change of 𝛱 under an internal rotation', 'exactly 0', 'gap']);
      return rows; },
    test(ctx){ const B = base(1.5), R = rot3([0.6,0.0,0.8], 1.1), P1 = proj(mm(B.U, R)); let worst = 0; for(let q=0;q<30;q++) worst = Math.max(worst, bound(1.5, -0.6 + 1.2*q/29, B.U));
      return [chk('an internal U(3) rotation changes 𝛱 by', fe(hsDiff(P1, proj(B.U))), '0 (tangent law)', hsDiff(P1, proj(B.U)) < 1e-12), chk('largest rate relative to the bound, 30 perturbation values', fx(worst, 3), '≤ 1 (Prop. 3.5)', worst <= 1)]; } };
})());

/* 3. Metric–curvature inequalities — the sharp curvature bound (§6, Figure 21) */
EYES.push((() => {
  const cache = {}; const cloud = fam => cache[fam] || (cache[fam] = Cr.bandCloud(fam, 360, fam === 'generic' ? 77 : 41));
  const MX = l => Math.max(0, Math.min(1, (l + 4)/5))*3.8 - 1.9, MY = l => Math.max(0, Math.min(1, (l + 4)/5))*3.2 - 0.8, MZ = th => th/Math.PI*2.6 - 1.3;
  return { id:'twist', title:'Metric–curvature inequalities', section:'§6, Theorem 6.1, Figure 21', grade:'proved',
    eq:'|𝛺(𝑉,𝑊)| ≤ 2√( 𝑔(𝑉,𝑉) 𝑔(𝑊,𝑊) − 𝑔(𝑉,𝑊)² )\nequality only on a complex line, 𝑊 = 𝑐𝑉',
    text:'Each point is one pair of tangent vectors (𝑉,𝑊). The horizontal axis is the metric bound 2√det 𝑔, the vertical axis is the curvature |𝛺(𝑉,𝑊)|, and the depth axis is the angle between the two vectors. The plane is the bound of Theorem 6.1, and no point lies above it. For a two-level system and for the lowest spin-one band every pair lies on the plane: the bound is saturated. A generic three-level band lies strictly below it, in some cases far below.',
    legend:[['#b18cff','pairs of tangent vectors'],['#ffffff','pairs that saturate the bound'],['#7f7cff','the bound']],
    choices:[{id:'fam', label:'Band', value:'two', options:[['two','Two levels'],['spin1','Spin one, lowest band'],['generic','Generic three levels']]}],
    view:[0.95, 0.25, 7.8, 0.7],
    make(g, ctx){ const lo = -4, hi = 1, pl = [];
      const a = V3(MX(lo), MY(lo), -1.3), b = V3(MX(hi), MY(hi), -1.3), c = V3(MX(hi), MY(hi), 1.3), d = V3(MX(lo), MY(lo), 1.3);
      const geo = new T.BufferGeometry().setFromPoints([a,b,c, a,c,d]); const plane = new T.Mesh(geo, new T.MeshBasicMaterial({color:0x7f7cff, transparent:true, opacity:0.13, side:T.DoubleSide, depthWrite:false, blending:T.AdditiveBlending})); g.add(plane);
      g.add(M.tube([a,b], 0.01, 0x9d8cff, 0.9)); g.add(M.tube([d,c], 0.01, 0x9d8cff, 0.9));
      g.add(M.line([V3(-1.9,-0.8,1.3), V3(1.9,-0.8,1.3)], 0x55657a)); g.add(M.line([V3(-1.9,-0.8,1.3), V3(-1.9,2.4,1.3)], 0x55657a)); g.add(M.line([V3(-1.9,-0.8,1.3), V3(-1.9,-0.8,-1.3)], 0x55657a));
      const l1 = M.label('bound 2√det g', '#aab7d2', 0.32); l1.position.set(1.4, -1.0, 1.5); g.add(l1); const l2 = M.label('|Ω|', '#d4c6ff', 0.36); l2.position.set(-2.1, 2.5, 1.3); g.add(l2);
      const l3 = M.label('angle between 𝑉 and 𝑊', '#aab7d2', 0.3); l3.position.set(-2.3, -0.95, -0.2); g.add(l3);
      ctx.pts = M.points(360, 0.11); g.add(ctx.pts); ctx.hl = M.orb(0.05, 0xffffff, 8); g.add(ctx.hl); this.change(ctx); },
    change(ctx){ const c = cloud(ctx.p.fam); ctx.c = c; c.forEach((q, i) => { const P = V3(MX(Math.log10(q.bound)), MY(Math.log10(Math.abs(q.Om) || 1e-12)), MZ(q.thetaG)); const on = q.ratio > 0.999;
      M.setPt(ctx.pts, i, P, on ? [0.95,0.9,1] : [0.62,0.48,1]); }); M.flush(ctx.pts);
      const r = c.map(q => q.ratio); ctx.stats = { on:r.filter(x => x > 0.999).length, med:med(r), min:Math.min(...r) }; },
    step(dt, t, ctx){ const i = Math.floor(t*1.5) % ctx.c.length, q = ctx.c[i]; ctx.hl.position.set(MX(Math.log10(q.bound)), MY(Math.log10(Math.abs(q.Om) || 1e-12)), MZ(q.thetaG));
      return [['Pairs drawn', String(ctx.c.length)], ['Saturating the bound (ratio above 0.999)', String(ctx.stats.on), 'twist'], ['Median |Ω| over the bound', fx(ctx.stats.med, 4), 'twist'],
        ['Smallest |Ω| over the bound', fx(ctx.stats.min, 4)], ['This pair', fx(q.ratio, 6), 'metric'], ['Paper', 'two levels and spin one: every pair saturates the bound', 'tail']]; },
    test(){ const a = Math.min(...cloud('two').map(q => q.ratio)), b = Math.min(...cloud('spin1').map(q => q.ratio)), c = Math.max(...cloud('generic').map(q => q.ratio));
      return [chk('two levels, smallest ratio over 360 pairs', fx(a, 6), '1 (every pair saturates, App. B)', a > 0.999), chk('spin one lowest band, smallest ratio', fx(b, 6), '1 (App. C)', b > 0.999), chk('generic three levels, largest ratio', fx(c, 4), '≤ 1, below the bound', c <= 1 + 1e-9)]; } };
})());

/* 4. One pair sum, many weights (§7.2, Figures 8 and 9) */
EYES.push((() => {
  const ROWS = [{p:3, name:'Berry connection polarizability', c:0x9fd6ff}, {p:2, name:'quantum metric', c:PAL.metric}, {p:2, name:'Berry curvature', c:PAL.twist, curv:true}, {p:1, name:'static response, friction', c:0x3f7fd0}, {p:1, name:'orbital moment', c:0xd8c6ff, curv:true}];
  const A2 = IQ.weights.amps.map(a => a*a), G = IQ.weights.gaps, pm = IQ.pairModel;
  const CURVES = [['metric', D => pm.metric(D), PAL.metric, '−2.00'], ['curvature', D => pm.curvature(D), PAL.twist, '−2.00'], ['metric dipole', D => pm.dipole(D), 0x9fd6ff, '−3.00'], ['friction, zero temperature', D => pm.friction0(D), PAL.gap, '−1.01'], ['friction, finite temperature', D => pm.frictionT(D, 0.3), PAL.tail, '−0.01']];
  const WX = l => (l + 2)/2*3.6 - 1.8, WY = (f, D) => 0.3*Math.log10(f(D)/f(1)) + 0.15;
  return { id:'weights', title:'One pair sum, many weights', section:'§7.2, Figures 8 and 9', grade:'computed', gradeLabel:'Computed, model shown',
    eq:'𝑔 = 𝛴ₙ |⟨0|∂𝛴|𝑛⟩|² / 𝛥ₙ²     one pair sum, read with 𝛥ₙ⁻³, 𝛥ₙ⁻², 𝛥ₙ⁻¹',
    text:'Each column is one excited level 𝑛, and each row weights the same interband amplitudes |⟨0|∂𝛴|𝑛⟩|² by a different power of the gap 𝛥ₙ. The power 𝛥ₙ⁻³ gives the Berry connection polarizability (the nonlinear Hall input), 𝛥ₙ⁻² the quantum metric and the Berry curvature, and 𝛥ₙ⁻¹ the static response and the friction. As the gap closes every row grows, each with its own power law; the rear panel shows the log–log slopes.',
    legend:[['#9fd6ff','gap⁻³'],['#5ab0ff','gap⁻² metric'],['#b18cff','gap⁻² curvature'],['#ffb547','friction']],
    controls:[{id:'lg', label:'Gap scale, log₁₀', min:-2, max:0, step:0.01, value:-0.4, fmt:v => (+v).toFixed(2) + '  (gap ×' + Math.pow(10, v).toFixed(3) + ')'}],
    view:[0.72, 0.36, 7.6, 0.6],
    make(g, ctx){ ctx.bars = []; ROWS.forEach((r, ri) => { G.forEach((_, n) => { const b = M.bar(0.3, 0.3, r.c); b.position.set(-1.4 + n*0.5, -0.8, -0.9 + ri*0.55); g.add(b); ctx.bars.push({b, r, n}); });
        const tot = M.bar(0.36, 0.36, r.c); tot.material.opacity = 0.55; tot.position.set(1.4, -0.8, -0.9 + ri*0.55); g.add(tot); ctx.bars.push({b:tot, r, n:-1});
        const l = M.label(r.name, '#a9b8d6', 0.24); l.position.set(2.75, -0.62, -0.9 + ri*0.55); g.add(l); });
      const fl = M.grid(5, 20, 0x5ab0ff, 0.05); fl.position.y = -0.81; g.add(fl);
      ctx.wall = new T.Group(); ctx.wall.position.set(0, 0.2, -2.2); g.add(ctx.wall);
      CURVES.forEach(c => { const pts = []; for(let k=0;k<=80;k++){ const l = -2 + 2*k/80, D = Math.pow(10, l); pts.push(V3(WX(l), Math.min(2.6, WY(c[1], D)), 0)); } ctx.wall.add(M.tube(pts, 0.012, c[2], 0.9)); });
      ctx.wall.add(M.line([V3(-1.8,0,0), V3(1.8,0,0)], 0x3a4a66)); const wl = M.label('each quantity against the gap, log–log', '#a9b8d6', 0.24); wl.position.set(0, -0.25, 0); ctx.wall.add(wl);
      ctx.cur = M.line([V3(0,-0.1,0), V3(0,2.7,0)], 0xffffff, 0.5); ctx.wall.add(ctx.cur); this.change(ctx); },
    change(ctx){ const s = Math.pow(10, ctx.p.lg); ctx.bars.forEach(o => { const v = o.n < 0 ? A2.reduce((a, x, n) => a + x/Math.pow(G[n]*s, o.r.p), 0) : A2[o.n]/Math.pow(G[o.n]*s, o.r.p); M.setBar(o.b, Math.max(0.02, 0.32*(Math.log10(v) + 1.4))); });
      ctx.cur.position.x = WX(ctx.p.lg); },
    step(dt, t, ctx){ const D = Math.pow(10, ctx.p.lg); return CURVES.map(c => [c[0] + ' slope, model / paper', fx(IQ.slope(c[1], D), 2).replace('-', '−') + ' / ' + c[3], c[0].startsWith('fric') ? 'gap' : 'metric']); },
    test(){ const D = 0.01; return CURVES.map(c => { const s = IQ.slope(c[1], D), p = +c[3].replace('−','-'); return chk(c[0] + ' slope as the gap closes', fx(s, 2), c[3] + ' (Figure 9)', Math.abs(s - p) < 0.02); }); } };
})());

/* 5. Chern number without a metric — the Chern number (App. B) */
EYES.push((() => {
  const N = 30; let cache = {};
  const get = (k, w) => { const key = k + ':' + w.toFixed(2); return cache[key] || (cache[key] = IQ.chern(k, w, N)); };
  return { id:'count', title:'Chern number without a metric', section:'Appendix B, (B.3)', grade:'proved',
    eq:'𝐶 = (1/2𝜋) ∫ 𝛾*𝛺 = 1     no metric on parameter space enters',
    text:'Each tile is a small cell of parameter space, coloured by the Berry flux of the subspace through it. Summed over all tiles, the flux divided by 2𝜋 is an integer, the Chern number, for every deformation of the chart, because no metric enters the integral. Where the map reverses orientation the flux has the opposite sign and cancels. The Chern number equals the degree of the map onto the sphere.',
    legend:[['#b18cff','positive Berry flux'],['#5ab0ff','negative Berry flux'],['#ffffff','running sum']],
    choices:[{id:'k', label:'Degree of the map', value:1, options:[[0,'Degree 0'],[1,'Degree 1'],[2,'Degree 2']]}],
    controls:[{id:'w', label:'Chart deformation', min:0, max:1, step:0.05, value:0.5}],
    view:[0.5, 0.45, 5.6, 0],
    make(g, ctx){ sphereRig(g, R0, 0.35); ctx.pts = M.points(N*2*N, 0.12); g.add(ctx.pts); ctx.sweep = M.ring(R0*1.02, 0xffffff, 0.006, 0.6); g.add(ctx.sweep); this.change(ctx); },
    change(ctx){ const k = ctx.p.k, w = ctx.p.w, C = get(k, w), f = IQ.mapN(k, w); ctx.C = C; const mx = Math.max(...C.tiles.map(Math.abs)) || 1; ctx.cent = [];
      let i = 0; for(let a=0;a<N;a++) for(let b=0;b<2*N;b++){ const n = f((a+0.5)/N, 2*Math.PI*(b+0.5)/(2*N)); const P = onS(n, R0*1.01); ctx.cent.push(P); const F = C.tiles[i]/mx;
        M.setPt(ctx.pts, i, P, F >= 0 ? [0.69*F, 0.55*F, F] : [0.35*-F, 0.69*-F, -F]); i++; } M.flush(ctx.pts); },
    step(dt, t, ctx){ const frac = (t*0.12) % 1.15, upto = Math.floor(Math.min(1, frac)*ctx.C.tiles.length); let s = 0; for(let i=0;i<upto;i++) s += ctx.C.tiles[i];
      const a = Math.min(1, frac), th = Math.PI*a; ctx.sweep.scale.setScalar(Math.max(0.02, Math.sin(th))); ctx.sweep.position.y = R0*Math.cos(th)*1.0; ctx.sweep.rotation.x = Math.PI/2;
      return [['Running sum of flux / 2𝜋', fx(s/(2*Math.PI), 4), 'twist'], ['Lattice Chern number, all tiles', fx(ctx.C.lattice, 6), 'twist'], ['(1/2𝜋)∫𝛺 by quadrature', fx(ctx.C.riemann, 5), 'metric'], ['Paper, degree 1', '1 (quadrature 1.0000026)', 'tail']]; },
    test(){ const a = IQ.chern(1, 0, 40), b = IQ.chern(1, 1, 40), c = IQ.chern(2, 0.5, 40), d = IQ.chern(0, 0.5, 40);
      return [chk('degree 1, round chart', fx(a.lattice, 6), '1 (App. B)', Math.abs(a.lattice - 1) < 1e-6), chk('degree 1, deformed chart', fx(b.lattice, 6), '1, chart independent', Math.abs(b.lattice - 1) < 1e-6),
        chk('degree 2', fx(c.lattice, 6), '2', Math.abs(c.lattice - 2) < 1e-6), chk('degree 0', fx(d.lattice, 6), '0', Math.abs(d.lattice) < 1e-6)]; } };
})());

window.__IQGT_EYES_A = EYES;
})();
