
/* ================= v4 additions: two knot eyes ================= */
X.mir = 1; X.same = 0; X.bv = 0;
const KNAME = m => m === 1 ? 'unknot' : m === 3 ? 'T(2,3) = 3₁, the trefoil' : m === 5 ? 'T(2,5) = 5₁' : m === 7 ? 'T(2,7) = 7₁' : 'T(2,' + m + ')';
function tkPts(m, R, rho, hand, cut){ const out = [], top = (m === 1 ? 2 : 4)*PI, a0 = cut || 0, N = m === 1 ? 160 : 90*m + 180;
  for(let i=0;i<=N;i++){ const f = a0 + (top - 2*a0)*i/N, rr = m === 1 ? R + rho : R + rho*Math.cos(m*f/2); out.push([rr*Math.cos(f), m === 1 ? 0 : rho*Math.sin(m*f/2), rr*Math.sin(f)*hand]); } return out; }
function tube(pts, col, rad, closed){ const c = new T.CatmullRomCurve3(pts.map(p => V3(p[0],p[1],p[2])), !!closed);
  return new T.Mesh(new T.TubeGeometry(c, Math.min(2400, pts.length*2), rad, 8, !!closed), new T.MeshStandardMaterial({color:col, emissive:col, emissiveIntensity:0.55, roughness:0.35, metalness:0.1})); }
const alexPoly = (m, t) => { let s = 0; for(let k=0;k<m;k++) s += (k % 2 ? -1 : 1)*Math.pow(t,k); return s/Math.pow(t,(m-1)/2); };
const HANDC = h => h > 0 ? 0xff8d7c : 0x63d3ff;

/* ---- EYE 8: a knot, its mirror, and what a step can see ---- */
const eyeKnot = { id:'knot', title:'A knot, its mirror, and what a step can see', section:'Knots, Mirrors, and What the Invariants Keep (recurrence, R₇); Two Trees peel_ladder', grade:'exact; each value computed live by more than one route',
  eq:'T(2,n): two strands, n crossings\nrun side, step ratio t:  Δ = cosh(n·ln t/2) / cosh(ln t/2)\n   = t^(−(n−1)/2) · (1 − Γ₁)/(1 − Γ_n)\nturn side, angle θ:  Δ = cos(nθ/2) / cos(θ/2)\nsignature = 2 × zeros passed, sign set by the hand',
  text:'A torus knot of two strands and n crossings sits round the centre of the ball. Its Alexander polynomial can be had from the tree: take one step of ratio t along an arm, and n steps along the same arm, and compare where they land. The gold arm shows those two balls. Reverse the step, t to 1/t, and the value does not move: this number is blind to direction, and the mirror knot has the same one. The turn side is the ring. There the same expression has zeros, the white marks, and the signature counts them, two for each one passed. The signature does flip under the mirror. Each crossing change removes two crossings, and the fewest changes that untie the knot is half the full signature.',
  uses:['kn','kc','kt','ka'], view:[0.4,1.0,7.6,0],
  extra: () => `<div class="row"><button data-m="1">the knot</button><button data-m="-1">its mirror</button></div>`,
  bind(){ document.querySelectorAll('#ctl button[data-m]').forEach(bn => { bn.setAttribute('aria-pressed', +bn.dataset.m === X.mir);
    bn.addEventListener('click', () => { X.mir = +bn.dataset.m; document.querySelectorAll('#ctl button[data-m]').forEach(q => q.setAttribute('aria-pressed', q === bn)); refresh(); }); }); },
  make(g){ this.s = new T.Group(); this.d = new T.Group(); g.add(this.s, this.d); rim(this.s); this.mk = M.points(2, 0.3); g.add(this.mk); },
  enter(S){ clear(this.d); const n = S.kn, need = (n-1)/2, k = Math.min(S.kc, need), m = n - 2*k, t = S.kt, r = Math.log(t), th = S.ka*PI/180, hand = X.mir;
    this.d.add(tube(tkPts(m, 1.2, 0.42, hand), HANDC(hand), 0.045, true));
    const G1 = gam(t), Gn = gam(Math.pow(t,m)), up = y => V3(0, RB*y, 0);
    this.d.add(M.line([up(0), up(Gn)], 0xf2c14e, 0.9));
    [[G1,'one step, Γ₁'],[Gn, m + ' steps, Γ_' + m]].forEach((q,i) => { const b = new T.Mesh(new T.SphereGeometry(0.085, 20, 14), new T.MeshBasicMaterial({color:0xf2c14e})); b.position.copy(up(q[0])); this.d.add(b);
      const l = M.label(q[1], '#f2c14e', 0.22); l.position.set(0.62, RB*q[0] + (i ? 0.12 : -0.02), 0); this.d.add(l); });
    const ring = a => V3(RB*0.985*Math.cos(a), 0, -RB*0.985*Math.sin(a)*hand); let passed = 0; const zs = [];
    for(let j=0;j<m;j++){ const a = (2*j+1)*PI/m; if(Math.abs(a - PI) < 1e-9) continue; zs.push(a); }
    const zp = M.points(Math.max(1, zs.length), 0.2); zs.forEach((a,i) => { const lit = a < th + 1e-12 && a < PI; if(lit) passed++; M.setPt(zp, i, ring(a), lit ? [1,1,1] : [0.35,0.4,0.5]); }); M.flush(zp); this.d.add(zp);
    const sw = []; for(let i=0;i<=64;i++) sw.push(ring(th*i/64)); this.d.add(M.line(sw, 0xffffff, 0.9)); this.d.add(M.line([V3(0,0,0), ring(th)], 0xffffff, 0.35));
    this.pos = ring(th);
    const a1 = alexPoly(m, t), a2 = Math.cosh(m*r/2)/Math.cosh(r/2), a3 = Math.pow(t, -(m-1)/2)*(1-G1)/(1-Gn), a4 = alexPoly(m, 1/t), x = t + 1/t, tv = Math.cos(m*th/2)/Math.cos(th/2);
    const rows = [['knot shown', KNAME(m) + (m > 1 ? (hand > 0 ? '' : ', mirror') : '')], ['crossing changes made, of the ' + need + ' needed', String(k)], ['run side: t,  Γ₁,  Γ of t to the ' + m, fmt(t,2) + ',  ' + fmt(G1,4) + ',  ' + fmt(Gn,6)],
      ['Alexander value, from the polynomial', fmt(a1,6)], ['cosh(n·ln t/2)/cosh(ln t/2)', fmt(a2,6)], ['from the two balls on the arm', fmt(a3,6)], ['with the step reversed, t → 1/t', fmt(a4,6)]];
    if(m === 7) rows.push(['x³ − x² − 2x + 1 at x = t + 1/t', fmt(x*x*x - x*x - 2*x + 1, 6)]);
    rows.push(['turn side: θ', fmt(S.ka,1) + '°'], ['cos(nθ/2)/cos(θ/2)', S.ka > 179.99 ? String(m) + ' (the determinant)' : fmt(tv,5)], ['zeros passed', passed + ' of ' + (m-1)/2],
      ['signature at this angle', (passed === 0 ? '0' : (hand > 0 ? '+' : '−') + 2*passed)], ['full signature, and half of it', (m === 1 ? '0,  0' : (hand > 0 ? '+' : '−') + (m-1) + ',  ' + (m-1)/2)], ['fewest changes to untie this knot', String((m-1)/2)]);
    this.rows = rows; },
  change(S){ this.enter(S); },
  step(dt, S, t){ M.setPt(this.mk, 0, this.pos, [1,1,1]); M.flush(this.mk); return this.rows; } };

/* ---- EYE 9: knot plus mirror: five, not six ---- */
const BH = [1,-4,2,3,3,3,2,3,2,2,4,-3,-3,-3,-3,-1,-3,-2,-3,-3];
const LADDER = [['7₁ # mirror 7₁', 0], ['K14a18636', 2], ['K15n81556', 3], ['K12n412', 4], ['unknot', 5]];
function braidCurve(word, R, dy, bump){ const nC = word.length, strands = 5, pos = [], col = []; let p = 0, guard = 0; const pts = [];
  do { for(let j=0;j<nC;j++){ const g = word[j], i = Math.abs(g)-1, a0 = 2*PI*j/nC, a1 = 2*PI*(j+1)/nC; let q = p, sgn = 0;
        if(p === i){ q = i+1; sgn = g > 0 ? 1 : -1; } else if(p === i+1){ q = i; sgn = g > 0 ? -1 : 1; }
        for(let s=0;s<10;s++){ const u = s/10, e = u*u*(3-2*u), y = ((p + (q-p)*e) - 2)*dy, rr = R + (sgn ? sgn*bump*Math.sin(PI*u) : 0), a = a0 + (a1-a0)*u; pts.push([rr*Math.cos(a), y, -rr*Math.sin(a)]); }
        p = q; } guard++; } while(p !== 0 && guard < 12);
  return pts; }
const eyeSum = { id:'sum', title:'Knot plus mirror: five, not six', section:'Brittenham and Hermiller 2025, arXiv 2506.24088 (Theorem 1.2); Knots, Mirrors, and What the Invariants Keep', grade:'their result; the braid and its first two changes re-checked here; later steps as published',
  eq:'7₁ unties in 3 changes, and so does its mirror\nsignature adds:  K # K → 12,   K # mirror K → 0\nfewest changes ≥ |signature|/2\nK # K: 6 exactly      K # mirror K: at most 5',
  text:'Two copies of the knot 7₁ are joined into one loop. Each copy alone unties in three crossing changes. Joined with the same hand, the signatures add to 12, and that forces six changes: nothing is saved. Joined to its mirror, the signatures cancel to 0, and the signature no longer forbids anything. The Alexander polynomial and the determinant cannot tell the two sums apart: they are blind to the hand. Brittenham and Hermiller found five changes that untie the mirror sum, on a drawing of it with 20 crossings on five strands. The first two changes are the gold crossings of that braid, and they give the knot K14a18636. Three more changes pass through K15n81556 and K12n412 to the unknot.',
  uses:['sc'], view:[0.4,0.85,7.6,0],
  extra: () => `<div class="row"><button data-j="0">K # mirror K</button><button data-j="1">K # K</button></div><div class="row"><button data-b="0">two knots joined</button><button data-b="1">the 20-crossing braid</button></div>`,
  bind(){ const press = () => { document.querySelectorAll('#ctl button[data-j]').forEach(q => q.setAttribute('aria-pressed', +q.dataset.j === X.same)); document.querySelectorAll('#ctl button[data-b]').forEach(q => q.setAttribute('aria-pressed', +q.dataset.b === X.bv)); }; press();
    document.querySelectorAll('#ctl button[data-j]').forEach(bn => bn.addEventListener('click', () => { X.same = +bn.dataset.j; if(X.same) X.bv = 0; press(); refresh(); }));
    document.querySelectorAll('#ctl button[data-b]').forEach(bn => bn.addEventListener('click', () => { X.bv = +bn.dataset.b; if(X.bv) X.same = 0; press(); refresh(); })); },
  make(g){ this.s = new T.Group(); this.d = new T.Group(); g.add(this.s, this.d); rim(this.s); },
  enter(S){ clear(this.d); const sc = S.sc, same = X.same === 1, braid = !same && (X.bv === 1 || sc > 0); let now;
    if(!braid){ const a = same ? Math.min(3, Math.ceil(sc/2)) : 0, b = same ? Math.min(3, Math.floor(sc/2)) : 0, mA = 7 - 2*a, mB = 7 - 2*b, d = 1.16, cut = 0.17, hb = same ? 1 : -1;
      const A = tkPts(mA, 0.76, 0.27, 1, cut).map(p => [p[0]-d, p[1], p[2]]), B = tkPts(mB, 0.76, 0.27, 1, cut).map(p => same ? [d-p[0], p[1], -p[2]] : [d-p[0], p[1], p[2]]);
      this.d.add(tube(A, HANDC(1), 0.04, false)); this.d.add(tube(B, HANDC(hb), 0.04, false));
      const a0 = A[0], a1 = A[A.length-1], b0 = B[0], b1 = B[B.length-1], v = p => V3(p[0],p[1],p[2]);
      if(same){ this.d.add(M.line([v(a0), v(b1)], 0xffffff, 1)); this.d.add(M.line([v(a1), v(b0)], 0xffffff, 1)); } else { this.d.add(M.line([v(a0), v(b0)], 0xffffff, 1)); this.d.add(M.line([v(a1), v(b1)], 0xffffff, 1)); }
      if(!same){ const disc = new T.Mesh(new T.CircleGeometry(RB*0.93, 64), new T.MeshBasicMaterial({color:0x63d3ff, transparent:true, opacity:0.07, side:T.DoubleSide, depthWrite:false})); disc.rotation.y = PI/2; this.d.add(disc);
        const l = M.label('mirror plane', '#63d3ff', 0.24); l.position.set(0, RB*0.8, 0); this.d.add(l); }
      now = same ? (sc === 0 ? '7₁ # 7₁' : KNAME(mA).split(' =')[0] + ' # ' + KNAME(mB).split(' =')[0]) : '7₁ # mirror 7₁'; }
    else { const w = BH.slice(); if(sc >= 1) w[0] = -w[0]; if(sc >= 2) w[1] = -w[1]; const dim = sc > 2;
      const tb = tube(braidCurve(w, 1.5, 0.36, 0.17), dim ? 0x4a5d75 : 0x9fd8ff, 0.035, true); if(dim) tb.material.emissiveIntensity = 0.25; this.d.add(tb);
      [0,1].forEach(j => { const a = 2*PI*(j+0.5)/20, i = Math.abs(BH[j])-1, y = (i + 0.5 - 2)*0.36, done = sc > j;
        const rg = new T.Mesh(new T.TorusGeometry(0.26, 0.02, 8, 40), new T.MeshBasicMaterial({color: done ? 0xffffff : 0xf2c14e})); rg.position.set(1.5*Math.cos(a), y, -1.5*Math.sin(a)); rg.lookAt(0, y, 0); this.d.add(rg);
        const l = M.label(done ? 'changed' : 'change ' + (j+1), done ? '#ffffff' : '#f2c14e', 0.2); l.position.set(1.95*Math.cos(a), y + 0.34, -1.95*Math.sin(a)); this.d.add(l); });
      const ys = i => 1.5 - 0.75*i, lp = []; let cur = 0; LADDER.forEach((L,i) => { if(sc >= L[1]) cur = i; });
      LADDER.forEach((L,i) => { lp.push(V3(0, ys(i), 0)); const on = i === cur && (sc === L[1] || (i === 0 && sc < 2));
        const b = new T.Mesh(new T.SphereGeometry(on ? 0.11 : 0.06, 20, 14), new T.MeshBasicMaterial({color: i <= cur ? 0xffffff : 0x55657a})); b.position.set(0, ys(i), 0); this.d.add(b);
        const l = M.label(L[0], i <= cur ? '#ffffff' : '#7a8a9c', 0.22); l.position.set(0.62, ys(i), 0); l.material.depthTest = false; l.renderOrder = 20; this.d.add(l); });
      this.d.add(M.line(lp, 0xf2c14e, 0.6));
      now = sc === 1 ? 'one of the first two changes made' : LADDER[cur][0]; }
    const d7 = 43;
    this.rows = [['the sum', same ? '7₁ # 7₁ (same hand)' : '7₁ # mirror 7₁'], ['signature of each half', same ? '+6,  +6' : '+6,  −6'], ['signature of the sum (they add)', same ? '12' : '0'],
      ['fewest changes the signature allows', same ? '6' : '0: no limit from the signature'], ['Alexander polynomial of the sum at t = 2', d7 + ' × ' + d7 + ' = ' + d7*d7 + ', either sum'], ['determinant of the sum', '7 × 7 = 49, either sum'],
      ['untying each half alone', '3 + 3 = 6 changes'], ['changes made', String(sc)], ['knot now', now + (same && sc === 5 ? ': one more change needed' : '')],
      ['fewest changes known', same ? '6 exactly' : 'at most 5; the exact value is open'],
      ['re-checked here', same ? 'signature 12, determinant 49' : 'braid: signature 0, determinant 49, Alexander = (7₁)²; two changes give K14a18636']]; },
  change(S){ this.enter(S); },
  step(){ return this.rows; } };
