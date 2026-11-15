
/* ================= v3 additions: four tree eyes ================= */
X.stand = -1; X.ord = 0;
const col3 = h => [((h>>16)&255)/255, ((h>>8)&255)/255, (h&255)/255];
const gam = z => (z-1)/(z+1);
function gens6(r){ const g = []; for(let a=0;a<3;a++) g.push(boost(UNIT[a], r), boost(UNIT[a].map(v => -v), r)); return g; }
function lineShell(g){ g.add(M.shell(RB*Math.SQRT1_2, 0xf2c14e, 0.06)); const l = M.label('the line  Γ² = 1/2', '#f2c14e', 0.26); l.position.set(0, -RB*Math.SQRT1_2 - 0.14, 0); g.add(l); }
function segs(g, pos, col, op){ const bg = new T.BufferGeometry(); bg.setAttribute('position', new T.Float32BufferAttribute(pos,3)); bg.setAttribute('color', new T.Float32BufferAttribute(col,3));
  const ls = new T.LineSegments(bg, new T.LineBasicMaterial({vertexColors:true, transparent:true, opacity:op})); ls.frustumCulled = false; g.add(ls); }

/* ---- EYE 4: the tree, its level shells, and the same tree from every ball ---- */
const STAND = ['the centre O', 'the neighbour along i', 'the neighbour along j', 'the neighbour along k'];
const eyeTree = { id:'tree', title:'The tree and its level shells', section:'Two Trees v4: peel_ladder, gam_mul, free5, free7', grade:'placement exact; freeness in Lean at ratios 5 and 7 (not re-run here); numbers computed live',
  eq:'six arms at every ball, five onward\nlevel L straight out:  Γ_L = (z^L − 1)/(z^L + 1)\nballs to depth 4:  1 + 6 + 30 + 150 + 750 = 937',
  text:'Every ball of the tree carries the same six arms: the axes i, j, k and their reverses. All 937 balls reached in up to four steps are drawn, each edge along its true shortest path and coloured by its axis. The gold shells are the levels: L steps straight out along one arm reach the shell of radius Γ_L exactly. Balls reached by turning between arms fall inside their shell. Stand on a neighbour and the whole tree slides by one peel step: what is then seen from the new ball is the same tree that was seen from the centre.',
  uses:['zt'], view:[0.62,0.36,8.2,0],
  extra: () => `<div class="row">` + STAND.map((s,i) => `<button data-s="${i-1}">stand on ${s}</button>`).join('') + `</div>`,
  bind(){ document.querySelectorAll('#ctl button[data-s]').forEach(bn => { bn.setAttribute('aria-pressed', +bn.dataset.s === X.stand);
    bn.addEventListener('click', () => { X.stand = +bn.dataset.s; document.querySelectorAll('#ctl button[data-s]').forEach(q => q.setAttribute('aria-pressed', q === bn)); refresh(); }); }); },
  make(g){ this.s = new T.Group(); this.d = new T.Group(); g.add(this.s, this.d); rim(this.s); },
  enter(S){ clear(this.d); const z = S.zt, r = Math.log(z), gens = gens6(r), back = X.stand < 0 ? I4() : boost(UNIT[X.stand].map(v => -v), r);
    const nodes = [{p:O4, d:0}], pos = [], col = [], cc = AXC.map(col3);
    (function walk(Mt, p, last, d){ if(d === 4) return; for(let k=0;k<6;k++){ if(last >= 0 && (k^1) === last) continue; const M2 = mm(Mt, gens[k]), q = mv(M2, O4); nodes.push({p:q, d:d+1});
        const gg = geo(mv(back,p), mv(back,q), 5), c = cc[k>>1], f = Math.pow(0.62, d);
        for(let j=0;j<5;j++){ pos.push(gg[j].x,gg[j].y,gg[j].z, gg[j+1].x,gg[j+1].y,gg[j+1].z); col.push(c[0]*f,c[1]*f,c[2]*f, c[0]*f,c[1]*f,c[2]*f); } walk(M2, q, k, d+1); } })(I4(), O4, -1, 0);
    segs(this.d, pos, col, 0.7);
    const moved = nodes.map(n => mv(back, n.p)), pp = M.points(nodes.length, 0.07);
    moved.forEach((p,i) => { const f = 0.35 + 0.65*Math.pow(0.7, nodes[i].d); M.setPt(pp, i, toBall(p), [f,f,f]); }); M.flush(pp); this.d.add(pp);
    const GL = [1,2,3,4].map(L => gam(Math.pow(z,L))); GL.forEach((G,i) => { this.d.add(M.shell(RB*G, 0xf2c14e, 0.05)); const l = M.label('level ' + (i+1), '#f2c14e', 0.2); l.position.set(0, RB*G + 0.07, 0); this.d.add(l); });
    const here = new T.Mesh(new T.SphereGeometry(0.1, 20, 14), new T.MeshBasicMaterial({color:0xffffff})); this.d.add(here);
    let worst = 0, Mt = I4(); for(let L=1;L<=4;L++){ Mt = mm(Mt, gens[0]); const p = mv(Mt, O4); worst = Math.max(worst, Math.abs(p[1]/(1+p[0]) - GL[L-1])); }
    let ms = 1e300; for(let i=0;i<nodes.length;i++) for(let j=i+1;j<nodes.length;j++){ const ip = mink(nodes[i].p, nodes[j].p); if(ip < ms) ms = ip; } ms = Math.acosh(Math.max(1,ms));
    let same = 0; if(X.stand >= 0){ for(const n of nodes){ if(n.d > 3) continue; let best = 1e300; for(const q of moved){ const dd = Math.max(Math.abs(n.p[0]-q[0]), Math.abs(n.p[1]-q[1]), Math.abs(n.p[2]-q[2]), Math.abs(n.p[3]-q[3]))/n.p[0]; if(dd < best) best = dd; } same = Math.max(same, best); } }
    this.rows = [['Γ,  ln z,  Γ² against 1/2', fmt(gam(z),4) + ',  ' + fmt(r,4) + ',  ' + (gam(z)*gam(z) < 0.5 ? 'below' : 'above')],
      ['level shells Γ₁ … Γ₄', GL.map(v => fmt(v,4)).join(',  ')], ['straight arm against Γ_L, largest difference', worst.toExponential(1)],
      ['balls drawn (depth 0 to 4)', String(nodes.length)], ['smallest distance between two balls', fmt(ms,4)], ['that distance in steps of ln z', fmt(ms/r,4)],
      ['standing on', STAND[X.stand+1]],
      ['tree from here against tree from the centre', X.stand < 0 ? 'stand on a neighbour to compare' : 'same to depth 3, largest difference ' + same.toExponential(1)],
      ['no word returns (freeness)', Math.abs(z-5) < 1e-9 || Math.abs(z-7) < 1e-9 ? 'in Lean at this ratio' : 'Lean covers ratios 5 and 7; here computed to depth 4 only']]; },
  change(S){ this.enter(S); },
  step(){ return this.rows; } };

/* ---- EYE 5: one step then another: the frame turns (Thomas turn) ---- */
const gcd = (a,b) => b ? gcd(b, a % b) : Math.abs(a);
function arc(u, v, n){ const out = [], w = Math.acos(Math.max(-1, Math.min(1, u.dot(v)))); for(let i=0;i<=n;i++){ const t = i/n; if(w < 1e-9){ out.push(u.clone()); continue; }
  out.push(u.clone().multiplyScalar(Math.sin((1-t)*w)/Math.sin(w)).addScaledVector(v, Math.sin(t*w)/Math.sin(w))); } return out; }
const eyeThomas = { id:'thomas', title:'One step then another: the frame turns', section:'Two Trees v4 thomas5; BallJoins J5 (euclid_is_thomas, garrett_pair), J7 (reverse_turn)', grade:'exact; computed live from the step matrices',
  eq:'step along i, then along j\n= one straight step, and a turn θ of the frame\ntan(θ/2) = Γ₁ · Γ₂\nother order: the same turn, the other way',
  text:'Two steps along different arms do not add up to one straight step. The gold path goes to ball I and then on by the step of J. The pink line is the one straight step that reaches the same ball. What is left over is a turn of the frame: the dim axes are the frame carried by the straight step, the bright axes the frame carried by the two steps, and the white arc is the turn between them. The turn is read off the matrices and set beside the formula. With whole step ratios the turn is a whole-number right triangle: ratios 5 and 5 give 65, 72, 97. Taking the steps in the other order gives the same size of turn in the opposite sense.',
  uses:['zI','zJ'], view:[0.5,0.62,7.4,0],
  extra: () => `<div class="row"><button data-o="0">I then J</button><button data-o="1">J then I</button></div>`,
  bind(){ document.querySelectorAll('#ctl button[data-o]').forEach(bn => { bn.setAttribute('aria-pressed', +bn.dataset.o === X.ord);
    bn.addEventListener('click', () => { X.ord = +bn.dataset.o; document.querySelectorAll('#ctl button[data-o]').forEach(q => q.setAttribute('aria-pressed', q === bn)); refresh(); }); }); },
  make(g){ this.s = new T.Group(); this.d = new T.Group(); g.add(this.s, this.d); rim(this.s); },
  enter(S){ clear(this.d); const f = X.ord ? 1 : 0, s = 1 - f, B1 = boost(UNIT[f], S.r[f]), B2 = boost(UNIT[s], S.r[s]), A = mm(B1, B2), p1 = mv(B1, O4), p = mv(A, O4);
    const rap = Math.acosh(p[0]), n = [p[1],p[2],p[3]].map(v => v/Math.sinh(rap)), R = mm(boost(n.map(v => -v), rap), A);
    const th = Math.acos(Math.max(-1, Math.min(1, (R[1][1]+R[2][2]+R[3][3]-1)/2))), ak = (R[2][1]-R[1][2])/(2*Math.sin(th));
    balls(this.d, S, [0,1]);
    this.d.add(M.line(geo(O4, p1, 24).concat(geo(p1, p, 24)), 0xf2c14e, 1)); this.d.add(M.line(geo(O4, p, 32), 0xff6fae, 1));
    const e = new T.Mesh(new T.SphereGeometry(0.08, 20, 14), new T.MeshBasicMaterial({color:0xffffff})); e.position.copy(toBall(p)); this.d.add(e);
    const L = 1.15; for(let a=0;a<3;a++){ const u = w3(UNIT[a]), v = w3([R[1][a+1], R[2][a+1], R[3][a+1]]);
      this.d.add(M.line([V3(0,0,0), u.clone().multiplyScalar(L)], AXC[a], 0.3)); this.d.add(M.line([V3(0,0,0), v.clone().multiplyScalar(L)], AXC[a], 1));
      if(a < 2) this.d.add(M.line(arc(u, v, 24).map(q => q.multiplyScalar(L*(0.8 + 0.12*a))), 0xffffff, 0.95)); }
    const G1 = S.G[0], G2 = S.G[1], form = 2*Math.atan(G1*G2), z1 = S.z[0], z2 = S.z[1], whole = Math.abs(z1-Math.round(z1)) < 1e-9 && Math.abs(z2-Math.round(z2)) < 1e-9;
    let tri = 'whole step ratios give a whole triangle';
    if(whole){ let a = (Math.round(z1)+1)*(Math.round(z2)+1), b = (Math.round(z1)-1)*(Math.round(z2)-1); const k = gcd(a,b); a /= k; b /= k; let t = [a*a-b*b, 2*a*b, a*a+b*b]; const k2 = gcd(gcd(t[0],t[1]),t[2]); t = t.map(v => v/k2);
      tri = t.join(',  ') + '   (cos θ = ' + t[0] + '/' + t[2] + ' against ' + fmt(Math.cos(th),6) + ')'; }
    this.rows = [['order', X.ord ? 'J then I' : 'I then J'], ['Γ₁,  Γ₂', fmt(G1,4) + ',  ' + fmt(G2,4)], ['turn of the frame, from the matrices', fmt(th*180/PI,4) + '°'], ['2·arctan(Γ₁Γ₂)', fmt(form*180/PI,4) + '°'],
      ['difference', Math.abs(th-form).toExponential(1)], ['sense about the third axis', ak > 0 ? 'counter-clockwise' : 'clockwise'], ['the triangle of the turn', tri],
      ['two steps, ln z₁ + ln z₂', fmt(S.r[0]+S.r[1],4)], ['the one straight step that reaches the same ball', fmt(rap,4)]]; },
  change(S){ this.enter(S); },
  step(){ return this.rows; } };

/* ---- EYE 6: across the line: the turn becomes a run ---- */
const LSPEC = [['z = 3', 3], ['z = 5', 5], ['z = 5.5', 5.5], ['the line', LINE], ['z = 6', 6], ['z = 7', 7]];
const eyeLine = { id:'line', title:'Across the line: the turn becomes a run', section:'Two Trees Thm 5.3, 5.4; BallJoins J3 (line_ratio, five_inside_seven_outside)', grade:'exact; computed live from the step matrices',
  eq:'equal steps:  g = (z − 1)²/(4z)\nbelow the line: turn 4·arccos g about a fixed point\nfixed point at ρ:  tanh²(ρ/2) = (1 − s)/(1 + s),  s = √(1 − 2Γ²)\non the line Γ² = 1/2 the fixed point reaches the rim',
  text:'Both arms take the same step. Below the line the square of four steps is a turn about the white point, and repeating it carries the centre round a ring through the centre: the walk is held. Raise the step and the white point moves outward and the ring grows. On the line, at z = 3 + 2√2, the white point reaches the rim: the ring opens. Past the line the square is a run and each pass carries the centre further toward the rim. Ratio 5 sits inside the line and ratio 7 outside it. The return counts say after how many passes the centre comes back to within a set distance of where it started.',
  uses:['zl','np'], view:[0.5,0.62,7.4,0],
  extra: () => `<div class="row">` + LSPEC.map((s,i) => `<button data-l="${i}">${s[0]}</button>`).join('') + `</div>`,
  bind(){ document.querySelectorAll('#ctl button[data-l]').forEach(bn => bn.addEventListener('click', () => window.MIXER_API.set('zl', LSPEC[+bn.dataset.l][1]))); },
  make(g){ this.s = new T.Group(); this.d = new T.Group(); g.add(this.s, this.d); rim(this.s); lineShell(this.s); this.mk = M.points(1, 0.3); g.add(this.mk); },
  enter(S){ clear(this.d); const z = S.zl, r = Math.log(z), S2 = { z:[z,z,z], r:[r,r,r], G:[gam(z),gam(z),gam(z)] }, keep = X.dir; X.dir = [1,1,1]; const m = pairMath(S2, 0, 1); X.dir = keep; this.m = m;
    balls(this.d, S2, [0,1]); const Fa = face(this.d, UNIT[0], r/2, AXC[0], 0.16), Fb = face(this.d, UNIT[1], r/2, AXC[1], 0.16);
    if(m.over){ const sg = crossing(Fa, Fb); if(sg) sg.forEach(s => this.d.add(M.line(s, 0xffffff, 0.8))); }
    let path = []; for(let i=0;i<4;i++) path = path.concat(geo(m.corners[i], m.corners[i+1], 24)); this.d.add(M.line(path, 0xf2c14e, 1));
    this.orb = [V3(0,0,0)]; let x = O4; for(let n=1;n<=S.np;n++){ x = mv(m.C, x); const s = Math.sqrt(Math.max(1e-300, mink(x,x))); x = x.map(v => v/s); if(!(x[0] < 1e7)) break; this.orb.push(toBall(x)); }
    const op = M.points(this.orb.length, 0.12); this.orb.forEach((p,i) => M.setPt(op, i, p, [0.85,0.85,0.85])); M.flush(op); this.d.add(op);
    const G2 = gam(z)*gam(z), rows = [['Γ² of the step against 1/2', fmt(G2,6) + (G2 < 0.5 - 1e-9 ? '  below' : G2 > 0.5 + 1e-9 ? '  above' : '  on the line')], ['g', fmt(m.g,6)]];
    if(m.p){ const fp = new T.Mesh(new T.SphereGeometry(0.07, 16, 12), new T.MeshBasicMaterial({color:0xffffff})); fp.position.copy(toBall(m.p)); this.d.add(fp);
      const rho = Math.acosh(m.p[0]), s = Math.sqrt(Math.max(0, 1-2*G2)), rf = 2*Math.atanh(Math.sqrt((1-s)/(1+s)));
      const got = {}; x = O4; for(let n=1;n<=8000;n++){ x = mv(m.C, x); const s2 = Math.sqrt(Math.max(1e-300, mink(x,x))); x = x.map(v => v/s2); const d = Math.acosh(Math.max(1,x[0])); if(!got.a && d < 0.1) got.a = n; if(!got.b && d < 0.01){ got.b = n; break; } }
      rows.push(['the square', 'turn'], ['turn per pass, from the matrices', fmt(m.phi,4) + '°'], ['4·arccos g (same turn, either way round)', fmt(Math.min(4*Math.acos(m.g)*180/PI, 360-4*Math.acos(m.g)*180/PI),4) + '°'],
        ['fixed point, distance ρ from the centre', fmt(rho,5)], ['ρ from the formula', fmt(rf,5)], ['fixed point, radius in the ball (rim = 1)', fmt(Math.tanh(rho/2),5)],
        ['the centre is held within 2ρ', fmt(2*rho,4)], ['back within 0.1 after', got.a ? got.a + ' passes' : 'more than 8000 passes'], ['back within 0.01 after', got.b ? got.b + ' passes' : 'more than 8000 passes']); }
    else rows.push(['the square', m.g > 1 + 1e-9 ? 'run' : 'on the line: neither turn nor run'], ['run per pass, from the matrices', fmt(m.tau,5)], ['4·arccosh g', fmt(4*Math.acosh(Math.max(1,m.g)),5)],
        ['fixed point', 'none inside the ball'], ['gap between the two faces', fmt(Math.acosh(Math.max(1,m.g)),5)], ['the centre returns', 'never: each pass carries it further']);
    this.rows = rows; },
  change(S){ this.enter(S); },
  step(dt, S, t){ const i = Math.floor(t*3) % this.orb.length; M.setPt(this.mk, 0, this.orb[i], [1,0.76,0.3]); M.flush(this.mk); return this.rows.concat([['pass shown', String(i)]]); } };

/* ---- EYE 7: the twin-prime chain as one path in the tree ---- */
const TWN = (function(){ const N = 400000, sv = new Uint8Array(N+3).fill(1); sv[0] = sv[1] = 0; for(let i=2;i*i<=N+2;i++) if(sv[i]) for(let j=i*i;j<N+3;j+=i) sv[j] = 0;
  const tw = []; for(let a=11;a<N;a++) if(sv[a] && sv[a+2]) tw.push(a); return tw; })();
const AXOF = a => ({1:0, 7:1, 9:2})[a % 10];
const CHN = (function(){ const n = 2400, pts = [], d = [], len = [], arm = []; let G = I4();
  for(let j=0;j<n;j++){ const p = mv(G, O4), s = Math.sqrt(mink(p,p)), q = p.map(v => v/s); pts.push(q); d.push(Math.acosh(Math.max(1,q[0]))); len.push(Math.log(TWN[j]/TWN[0])); arm.push(j ? AXOF(TWN[j]) : -1);
    G = mm(G, boost(UNIT[AXOF(TWN[j+1])], Math.log(TWN[j+1]/TWN[j]))); } return { n, pts, d, len, arm }; })();
const eyeChain = { id:'chain', title:'The twin-prime chain as one path in the tree', section:'BallJoins J6 (twin_start_digit); Two Trees v4 gam_mul; One Tree, One Ball', grade:'end-digit rule in Lean; the path computed live from exact steps',
  eq:'twin pair (a, a + 2), a > 5:  a ends in 1, 7 or 9\nend digit 1, 7, 9  →  arm i, j, k\nstep to the next pair: ratio a′/a along its arm\npath length = ln(a/11)',
  text:'Each twin pair is a ball. The step from one pair to the next is a peel step of its true size, the ratio of the two starting numbers, taken along the arm of the next pair’s end digit. Ratios multiply and lengths add, so the length of the path walked is exactly the logarithm of the starting number over 11. The path keeps changing arm, so it ends closer to the centre than the length it has walked; the readout gives both. The faint tree and the gold shells are the tree of ratio 5 and its levels, for scale. The chain starts at the pair 11, 13 at the centre.',
  uses:['nc'], view:[0.62,0.36,8.2,0],
  make(g){ this.s = new T.Group(); this.d = new T.Group(); g.add(this.s, this.d); rim(this.s); const r5 = Math.log(5); tree(this.s, { r:[r5,r5,r5], depth:3 });
    [1,2,3].forEach(L => this.s.add(M.shell(RB*gam(Math.pow(5,L)), 0xf2c14e, 0.045))); },
  enter(S){ clear(this.d); const n = Math.max(2, Math.min(CHN.n, Math.round(S.nc))), pos = [], col = [], cc = AXC.map(col3), cnt = [0,0,0];
    for(let j=1;j<n;j++){ const gg = geo(CHN.pts[j-1], CHN.pts[j], 3), c = cc[CHN.arm[j]]; cnt[CHN.arm[j]]++; for(let k=0;k<3;k++){ pos.push(gg[k].x,gg[k].y,gg[k].z, gg[k+1].x,gg[k+1].y,gg[k+1].z); col.push(c[0],c[1],c[2], c[0],c[1],c[2]); } }
    segs(this.d, pos, col, 1);
    const pp = M.points(n, 0.06); for(let j=0;j<n;j++) M.setPt(pp, j, toBall(CHN.pts[j]), j === 0 ? [1,1,1] : cc[CHN.arm[j]]); M.flush(pp); this.d.add(pp);
    const e = new T.Mesh(new T.SphereGeometry(0.06, 16, 12), new T.MeshBasicMaterial({color:0xffffff})); e.position.copy(toBall(CHN.pts[n-1])); this.d.add(e);
    const a = TWN[n-1], len = CHN.len[n-1], d = CHN.d[n-1];
    this.rows = [['twin pairs drawn', String(n)], ['latest pair', a + ',  ' + (a+2)], ['its end digit → arm', (a % 10) + ' → ' + AXL[AXOF(a)]], ['path length ln(a/11)', fmt(len,4)],
      ['distance from the centre ball', fmt(d,4)], ['distance / path length', fmt(d/len,4)], ['level of the ratio-5 tree reached', fmt(d/Math.log(5),2)],
      ['steps taken along i,  j,  k', cnt.join(',  ')], ['twin starts from 11 below 400000', String(TWN.length)]]; },
  change(S){ this.enter(S); },
  step(){ return this.rows; } };
