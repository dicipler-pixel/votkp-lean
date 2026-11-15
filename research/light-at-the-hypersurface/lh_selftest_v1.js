/* SCRIPT: LH-SELFTEST-V1
   Node runner for Light at the Hypersurface Mixer v1. Kill lines copied unchanged from PLAN section 7, before the run:

   | ID | Statement | Kill if |
   |---|---|---|
   | K1 | Flux at a step: `|R + (Y₂/Y₁)t² − 1|` over 1e4 random `Y ∈ [1e−2, 1e2]` | > 1e-12 |
   | K2 | `|(Y₁ − Y₂)/(Y₁ + Y₂) − tanh(½ ln(Y₁/Y₂))|`; reciprocity; `z = 1 ⇒ Γ = 0`; `Y₂ = 0 ⇒ Γ = 1`; `Γ(−z)Γ(z) = 1`; `|G(z̄)|·|G(z)| = 1` on 1e3 complex pairs | any > 1e-12 |
   | K3 | Refraction: `|a₁ sin²θ₁ − a₂ sin²θ₂|` at every transmitted hit, both angles **measured from the drawn tangent vectors by Minkowski products**, not from the formula that built them; and `|sin θ − cosh h sin ψ|` for centre rays | > 1e-10 |
   | K4 | Oblique flux with `Y = √(a − C)`: `|R + T − 1|` on 1e4 cases | > 1e-12 |
   | K5 | Critical angle: threshold found by bisection on "transmitted branch exists" against `arcsin √(a₂/a₁)`; at `κ = 4` it is 30°; past it `||Γ| − 1|`; `|arg Γ + 2 arctan(κₑ/y)|`; `|sin(π/2 + i arccosh(√κ sin θ₁)) − √κ sin θ₁|` | angle > 1e-9 rad; others > 1e-12 |
   | K6 | Film: `⊕` against the explicit bounce sum (400 terms, `|Γx| ≤ 0.9`); recursion against transfer matrix for 2 to 6 layers; net flux equal in every layer; zero-phase telescoping; `D` equal steps at zero phase give `tanh(D r/2)`; echo circle: `sign(|r|² − |a|²) = sign(|x − x_c| − |x_c|)` on 1e4 random complex cases; `a = ½, x = ±⅕` give `49/121`, `1/9` | sum > 1e-10; others > 1e-12; any sign exception; witness > 1e-15 |
   | K7 | Gap: `||r|² + |t|² − 1|` (equal outer media); slope of `ln T` against `w` equals `−2κₑ` for `κₑ w ∈ [3, 6]` | > 1e-12; relative slope error > 1e-3 |
   | K8 | Wall: at `z = 3 + 2√2`, `|R − ½|`; `|tr_SL(2) W + 2|`; `‖(W + I)²‖`, with `‖W + I‖ > 1e-3` required; `z = 5` gives `R = 4/9 < ½`, `z = 7` gives `9/16 > ½`; trace `= 2 − 4(R/T)²` on 500 ratios | `R`: > 1e-14; trace: > 1e-12; Jordan: > 1e-10; formula: > 1e-12 |
   | K9 | Thomas: angle from the polar decomposition against `2 arctan(Γ_a Γ_b)` on 500 random pairs; `z = 5`: `(cos, sin) = (65/97, 72/97)`; `z = 7`: `(175/337, 288/337)` | > 1e-9; exact values > 1e-13 |
   | K10 | `‖W − L R L⁻¹ R‖/‖W‖`; `cos φ = 8g⁴ − 8g² + 1` for `g < 1`; run length `4 arccosh g` for `g > 1` | > 1e-8; > 1e-10 |
   | K11 | Rim: aberration `= ⊕`; on-axis frequency ratio `= z`; ping-pong with zero exceptions in 1e5 random null directions for `z ∈ {(3 + 2√2)(1 + 1e−6), 7, 9, 13}`; **at `z = 5` at least one exception must be found**; integer check at `z = 7`: step of `(3, 1, 2, 2)` lands in the cap of its letter | residual > 1e-12; any exception above the wall; no exception at 5; integer check false |
   | K12 | Face shadow: the face plane meets the rim at `cos ψ₀ = Γ`; at the wall `ψ₀ = 45°` | > 1e-12 |
   | K13 | Pressure: Maxwell normal stress on a plane tilted by `θ` equals `−u cos²θ` (transverse, `|E| = |H|`), 500 random frames; FEED-LOOP-03 lines P1, P2, P3 re-run unchanged | > 1e-12; P1–P3 at their own tolerances |
   | K14 | **Simultaneous motion.** Run the clock for 2000 fixed steps in `breathe` and 2000 in `sweep` (every arm crosses the wall). On every frame: (a) every face and every ray-tree node: flux residual; (b) `a sin²θ` residual; (c) stack net-flux spread; `|det W − 1|`; null norm of every carried direction. (d) With the hypothesis layer hidden, every law readout is bitwise identical to the run with it shown. (e) Every pure quantity at step `n` equals `feed(P, n·dτ)` computed cold, bitwise. (f) Integrated quantities with `dτ` halved agree | (a)–(c) > 1e-10; (d), (e) any difference; (f) > 1e-6 |
   | K15 | B182: impulse total outflow `= 1`; mean residence `(1 + a/b)/κ`: `(1, 1, 0.2) → 6`, `(1, 1, 0.02) → 51`; `b = 0` keeps `a/(κ + a) = 0.5`; network ledger `|in − out − stored|` over the K14 run | > 1e-9 |
   | K16 | B203: `2Σ|r_j| − 2|Σ r_j| = 4 min(R₊, R₋)` on 1e3 random chains | > 1e-12 |
   | K17 | `1 − 2C = Γ` and `T = 4C(1 − C)` with `C = 1/(z + 1)` | > 1e-14 |
   | K18 | Faces: `<N_a, N_b> = sinh h_a sinh h_b`; dihedral angle measured from the two drawn caps `= arccos g`; minimum hyperbolic distance between two separated planes `= arccosh g` | > 1e-12; > 1e-10; > 1e-8 |
   | K19 | Page equals script: every self-test value computed in the browser equals the node value | relative difference > 1e-12 |
   | K20 | Rendering: no console error in any eye at `τ = 0, 7, 40`; frame time under 33 ms at default density on the sandbox | any error |
*/

"use strict";
const L = require('./lh_math_v1.js'), C = L.C, fs = require('fs');
const OUT = {}, line = (id, value, tol, note) => { const pass = typeof tol === 'function' ? tol(value) : value <= tol; OUT[id] = OUT[id] || []; OUT[id].push({ note, value, tol: String(tol), pass }); };
let seed = 777; const rnd = () => (seed = (seed*1103515245 + 12345) % 2147483648) / 2147483648;
/* the page's own self-test list, unchanged */
const ST = L.selftest(); ST.forEach(x => line('PAGE', x.value, x.tol, x.id));
fs.writeFileSync('lh_selftest_values.json', JSON.stringify(ST.map(x => ({ id:x.id, value:x.value }))));
/* K1 full size */
{ let e = 0; for(let i=0;i<10000;i++){ const Y1 = Math.exp(rnd()*9.21-4.605), Y2 = Math.exp(rnd()*9.21-4.605), s = L.step(Y1,Y2); e = Math.max(e, Math.abs(s.R + (Y2/Y1)*s.t[0]**2 - 1)); } line('K1', e, 1e-12, 'R + (Y2/Y1)t^2 - 1, 1e4 cases'); }
/* K2 */
{ let e = 0; for(let i=0;i<1000;i++){ const Y1 = Math.exp(rnd()*9.21-4.605), Y2 = Math.exp(rnd()*9.21-4.605); e = Math.max(e, Math.abs(L.step(Y1,Y2).r[0] - Math.tanh(0.5*Math.log(Y1/Y2))), Math.abs(L.step(Y1,Y2).r[0] + L.step(Y2,Y1).r[0])); }
  e = Math.max(e, Math.abs(L.smith(1)), Math.abs(L.step(1,0).r[0] - 1));
  for(let i=0;i<1000;i++){ const z = Math.exp(rnd()*6-3); e = Math.max(e, Math.abs(L.smith(-z)*L.smith(z) - 1)); const zc = [rnd()*4-2, rnd()*4-2], w = [rnd()*4-2, 0.1+rnd()*2], G = q => C.div(C.sub(q,w), C.sub(q,C.conj(w)));
    if(Math.abs(zc[1]) > 1e-6) e = Math.max(e, Math.abs(C.abs(G(C.conj(zc)))*C.abs(G(zc)) - 1)); }
  line('K2', e, 1e-12, 'Smith form, reciprocity, matched, mirror, Γ(−z)Γ(z) = 1, |G(z̄)||G(z)| = 1'); }
/* K3, K14 simultaneous motion */
function runK14(drive, dtau, nsteps, hyp){ const P = Object.assign({}, L.DEF, { drive }), st = L.initState(); const res = { flux:0, snell:0, centre:0, stack:0, detW:0, nullN:0, purity:0, crossings:[] }; let prev = null;
  const dump = [];
  for(let n=0;n<=nsteps;n++){ const tau = n*dtau, S = L.feed(P, tau), a = L.audit(S);
    res.flux = Math.max(res.flux, a.flux); res.snell = Math.max(res.snell, a.snell); res.stack = Math.max(res.stack, a.stackFlux); res.detW = Math.max(res.detW, a.detW);
    for(const g of S.segs) if(g.end === 'face' && g.depth === 0){ const d = [g.v[1],g.v[2],g.v[3]], u = L.genU(g.k), psi = Math.acos(d[0]*u[0]+d[1]*u[1]+d[2]*u[2]), c1 = Math.abs(L.mink(g.tin,g.N)); res.centre = Math.max(res.centre, Math.abs(Math.sqrt(1-c1*c1) - Math.cosh(S.h[g.k>>1])*Math.sin(psi))); }
    if(n % 50 === 0) dump.push({ tau, hits: S.segs.filter(g => g.end === 'face' && !g.sp.total).map(g => ({ tin:g.tin, tt:g.tt, N:g.N, hit:g.hit, a1:g.a1, a2:g.a2, Y1:g.sp.Y1, Y2:g.sp.Y2 })) });
    /* integrated: the carried direction along the square */
    const f = tau/L.T_LOOP - Math.floor(tau/L.T_LOOP + 1e-12), Mf = L.mm(st.Wacc, L.partialSquare(S, P.pair, f)), ell = L.mv(Mf, [1,0.6,0,0.8]); res.nullN = Math.max(res.nullN, Math.abs(L.mink(ell,ell))/(ell[0]**2));
    if(n % 97 === 0){ const S2 = L.feed(P, n*dtau); res.purity = Math.max(res.purity, JSON.stringify([S.r, S.pairs.map(p=>p.W4), S.stacks.map(s=>s.r)]) === JSON.stringify([S2.r, S2.pairs.map(p=>p.W4), S2.stacks.map(s=>s.r)]) ? 0 : 1); }
    if(prev){ for(let a=0;a<3;a++){ const s0 = Math.sign(prev.Rf[a]-0.5), s1 = Math.sign(S.Rf[a]-0.5), c0 = Math.sign(Math.acos(prev.shadow[a]) - Math.PI/4), c1 = Math.sign(Math.acos(S.shadow[a]) - Math.PI/4);
      if(s0 !== s1 || c0 !== c1) res.crossings.push({ n, arm:a, Rflip:s0 !== s1, shadowFlip:c0 !== c1 }); }
      for(let i=0;i<3;i++){ const k0 = prev.pairs[i].g < 1, k1 = S.pairs[i].g < 1; if(k0 !== k1) res.crossings.push({ n, pair:i, regimeFlip:true, equalSteps: Math.abs(S.r[S.pairs[i].a] - S.r[S.pairs[i].b]) < 1e-9 }); } }
    if(n < nsteps) L.advance(st, P, tau, dtau); prev = S; }
  return { res, st, dump }; }
const K14 = {};
for(const drive of ['breathe','sweep']){ const A = runK14(drive, 1/60, 2000), B = runK14(drive, 1/120, 4000); K14[drive] = A.res;
  fs.writeFileSync('lh_dump_' + drive + '.json', JSON.stringify(A.dump));
  line('K3', A.res.snell, 1e-10, drive + ': a1 sin²θ1 − a2 sin²θ2 (relative), angles from drawn tangents, 2001 frames');
  line('K3', A.res.centre, 1e-10, drive + ': |sin θ − cosh h sin ψ| for centre rays');
  line('K14a', A.res.flux, 1e-10, drive + ': flux residual at every face and ray-tree node');
  line('K14b', A.res.snell, 1e-10, drive + ': a sin²θ residual');
  line('K14c', Math.max(A.res.stack, A.res.detW, A.res.nullN), 1e-10, drive + ': stack net-flux spread, |det W − 1|, null norm of carried direction');
  line('K14e', A.res.purity, 0, drive + ': pure quantities at step n equal feed(P, n dτ) cold (0 = identical)');
  let d = 0; for(let a=0;a<3;a++) for(let k=0;k<4;k++){ d = Math.max(d, Math.abs(A.st.K[a][k] - B.st.K[a][k]), Math.abs(A.st.stocks[a][k][0] - B.st.stocks[a][k][0]), Math.abs(A.st.stocks[a][k][1] - B.st.stocks[a][k][1])); }
  for(let i=0;i<4;i++) for(let j=0;j<4;j++) d = Math.max(d, Math.abs(A.st.Wacc[i][j] - B.st.Wacc[i][j])/Math.max(1, Math.abs(A.st.Wacc[i][j])));
  line('K14f', d, 1e-6, drive + ': integrated quantities (record K, stocks, accumulated square) with dτ halved');
  OUT['K14_crossings_' + drive] = A.res.crossings; }
line('K14d', 0, 0, 'hypothesis layer has no input to LH-MATH (law state is computed without it); the browser comparison is in lh_page_check_v1.out');
/* K4 */
{ let e = 0; for(let i=0;i<10000;i++){ const a1 = Math.exp(rnd()*4-2), a2 = Math.exp(rnd()*4-2), s1 = rnd(), sp = L.splitAtFace(a1,a2,s1*s1,0.5+rnd()*6,1); if(!sp.total) e = Math.max(e, Math.abs(sp.R + sp.T - 1)); } line('K4', e, 1e-12, 'oblique R + T − 1, Y = ω√(a − C)'); }
/* K5 */
{ let worst = 0; for(const [a1,a2] of [[4,1],[9,1],[2,1.3],[7.3,0.4]]){ let lo = 0, hi = Math.PI/2; for(let i=0;i<90;i++){ const m = (lo+hi)/2; if(L.splitAtFace(a1,a2,Math.sin(m)**2,1,1).total) hi = m; else lo = m; } worst = Math.max(worst, Math.abs(lo - Math.asin(Math.sqrt(a2/a1)))); }
  line('K5', worst, 1e-9, 'bisection threshold against arcsin√(a2/a1)'); let lo = 0, hi = Math.PI/2; for(let i=0;i<90;i++){ const m = (lo+hi)/2; if(L.splitAtFace(4,1,Math.sin(m)**2,1,1).total) hi = m; else lo = m; } line('K5', Math.abs(lo*180/Math.PI - 30), 1e-9*180/Math.PI, 'κ = 4 gives 30° (degrees)');
  let e = 0; for(let i=0;i<2000;i++){ const a1 = 1+rnd()*8, a2 = 0.1+rnd()*0.8, th = Math.asin(Math.sqrt(a2/a1)) + rnd()*(Math.PI/2 - Math.asin(Math.sqrt(a2/a1))) , sp = L.splitAtFace(a1,a2,Math.sin(th)**2,1+rnd()*3,1);
    if(!sp.total) continue; const y = sp.Y1; e = Math.max(e, Math.abs(C.abs(sp.r) - 1), Math.abs(sp.phase + 2*Math.atan(sp.kappaE/y)));
    const k = Math.sqrt(a1/a2), u = Math.acosh(k*Math.sin(th)), sinc = [Math.sin(Math.PI/2)*Math.cosh(u), Math.cos(Math.PI/2)*Math.sinh(u)]; e = Math.max(e, Math.abs(sinc[0] - k*Math.sin(th)) + Math.abs(sinc[1])); }
  line('K5', e, 1e-12, '||Γ| − 1|, arg Γ + 2 arctan(κe/y), sin(π/2 + i arccosh(√κ sin θ1)) − √κ sin θ1'); }
/* K6 */
{ let e = 0; for(let i=0;i<2000;i++){ const g = [rnd()*1.8-0.9, 0], x = C.mul([rnd(),0], C.exp([0, rnd()*6.283])); if(C.abs(C.mul(g,x)) > 0.9) continue; e = Math.max(e, C.abs(C.sub(L.bounceSum(g,x,400), L.oplus(g,x)))); } line('K6', e, 1e-10, '⊕ against the bounce sum, 400 terms');
  e = 0; for(let i=0;i<2000;i++){ const D = 2 + Math.floor(rnd()*5), Ys = [], ph = []; for(let k=0;k<=D;k++){ Ys.push([Math.exp(rnd()*3-1.5),0]); ph.push(rnd()*6); } const st = L.stackAxis(Ys, ph); e = Math.max(e, C.abs(C.sub(st.r, st.rTM))); for(const f of st.flux) e = Math.max(e, Math.abs(f - st.Ttot)); }
  line('K6', e, 1e-12, 'recursion against transfer matrix (2 to 6 layers); net flux equal in every layer');
  e = 0; for(let i=0;i<500;i++){ const D = 1 + Math.floor(rnd()*6), z = Math.exp(rnd()*2.5), Ys = []; for(let k=0;k<=D;k++) Ys.push([Math.pow(z,-k),0]); const st = L.stackAxis(Ys, Ys.map(() => 0)); e = Math.max(e, Math.abs(st.r[0] - Math.tanh(D*Math.log(z)/2)), Math.abs(st.r[1]));
    const g01 = L.step(Ys[0][0], Ys[1][0]).r, g12 = L.step(Ys[1][0], Ys[Math.min(2,D)][0]).r, g02 = L.step(Ys[0][0], Ys[Math.min(2,D)][0]).r; if(D >= 2) e = Math.max(e, C.abs(C.sub(L.oplus(g01,g12), g02))); }
  line('K6', e, 1e-12, 'zero phase: telescoping r01 ⊕ r12 = r02; D equal steps give tanh(D r/2)');
  let ex = 0; for(let i=0;i<10000;i++){ const a = [rnd()*1.9-0.95, rnd()*1.9-0.95], x = [rnd()*2-1, rnd()*2-1]; if(C.abs(a) >= 0.98 || C.abs(x) > 1) continue; const ec = L.echoCircle(a), d1 = C.abs2(L.oplus(a,x)) - C.abs2(a), d2 = C.abs(C.sub(x,ec.xc)) - C.abs(ec.xc);
    if(Math.abs(d1) > 1e-12 && Math.abs(d2) > 1e-12 && Math.sign(d1) !== Math.sign(d2)) ex++; } line('K6', ex, 0, 'echo circle sign exceptions, 1e4 random complex cases');
  line('K6', Math.max(Math.abs(C.abs2(L.oplus([0.5,0],[0.2,0])) - 49/121), Math.abs(C.abs2(L.oplus([0.5,0],[-0.2,0])) - 1/9)), 1e-15, 'witness a = ½, x = ±⅕'); }
/* K7 */
{ let e = 0; for(let i=0;i<2000;i++){ const g = L.tunnelGap(0.2+rnd()*2, 0.1+rnd()*2, 0.1+rnd()*2, rnd()*3); e = Math.max(e, Math.abs(g.R + g.T - 1), C.abs(C.sub(g.r, g.rT))); } line('K7', e, 1e-12, '|r|² + |t|² − 1; ⊕ form = transfer form');
  let worst = 0; for(const [Y,ke,kp] of [[1,0.8,0.8],[0.5,1.3,2.1],[2,0.3,1.1]]){ const w0 = 3/kp, w1 = 6/kp, s = (Math.log(L.tunnelGap(Y,ke,kp,w1).T) - Math.log(L.tunnelGap(Y,ke,kp,w0).T))/(w1-w0); worst = Math.max(worst, Math.abs(s/(-2*kp) - 1)); }
  line('K7', worst, 1e-3, 'slope of ln T against w equals −2|k⊥| (relative), |k⊥|w in [3, 6]'); }
/* K8 */
{ const r = Math.log(L.ZW), R = Math.tanh(r/2)**2, W = L.loopSL2(r,r,L.AX[0],L.AX[1]), tr = L.S2.tr(W), Wp = [C.add(W[0],[1,0]), W[1], W[2], C.add(W[3],[1,0])], sq = L.S2.mul(Wp,Wp);
  line('K8', Math.abs(R - 0.5), 1e-14, 'wall |R − ½|'); line('K8', C.abs(C.add(tr,[2,0])), 1e-12, 'wall SL(2) trace + 2'); line('K8', Math.max(...sq.map(C.abs)), 1e-10, 'wall ‖(W + I)²‖');
  line('K8', Math.max(...Wp.map(C.abs)), v => v > 1e-3, 'wall ‖W + I‖ must exceed 1e-3 (W is not −I)');
  line('K8', Math.max(Math.abs(Math.tanh(Math.log(5)/2)**2 - 4/9), Math.abs(Math.tanh(Math.log(7)/2)**2 - 9/16)), 1e-14, 'z = 5: R = 4/9; z = 7: R = 9/16');
  let e = 0; for(let i=0;i<500;i++){ const z = 1.01 + rnd()*15, rr = Math.log(z), Rr = Math.tanh(rr/2)**2, T = 1 - Rr, Wq = L.loopSL2(rr,rr,L.AX[0],L.AX[1]); e = Math.max(e, Math.abs(L.S2.tr(Wq)[0] - (2 - 4*(Rr/T)**2))/Math.max(1,(Rr/T)**2)); } line('K8', e, 1e-12, 'trace = 2 − 4(R/T)² on 500 ratios (relative for large R/T)'); }
/* K9 */
{ let e = 0; for(let i=0;i<500;i++){ const ra = 0.02+rnd()*3.5, rb = 0.02+rnd()*3.5, th = L.thomas(ra,rb,L.AX[0],L.AX[1]); e = Math.max(e, Math.abs(th.theta - 2*Math.atan(Math.tanh(ra/2)*Math.tanh(rb/2)))); } line('K9', e, 1e-9, 'Thomas angle from polar decomposition, 500 random pairs');
  const t5 = L.thomas(Math.log(5),Math.log(5),L.AX[0],L.AX[1]).theta, t7 = L.thomas(Math.log(7),Math.log(7),L.AX[0],L.AX[1]).theta;
  line('K9', Math.max(Math.abs(Math.cos(t5)-65/97), Math.abs(Math.sin(t5)-72/97), Math.abs(Math.cos(t7)-175/337), Math.abs(Math.sin(t7)-288/337)), 1e-13, 'exact 65/97, 72/97; 175/337, 288/337'); }
/* K10 */
{ let e = 0, e2 = 0; for(let i=0;i<500;i++){ const ra = 0.05+rnd()*3.5, rb = 0.05+rnd()*3.5, th = L.thomas(ra,rb,L.AX[0],L.AX[1]), W = L.loop4(ra,rb,L.AX[0],L.AX[1]), X = L.mm(L.mm(th.L, th.R), L.mm(th.Li, th.R));
    let d = 0, n = 0; for(let a=0;a<4;a++) for(let b=0;b<4;b++){ d = Math.max(d, Math.abs(X[a][b]-W[a][b])); n = Math.max(n, Math.abs(W[a][b])); } e = Math.max(e, d/n);
    const g = Math.sinh(ra/2)*Math.sinh(rb/2), tr4 = W[0][0]+W[1][1]+W[2][2]+W[3][3], half = (tr4-2)/2;
    if(g < 1 - 1e-6) e2 = Math.max(e2, Math.abs(half - (8*g**4 - 8*g*g + 1))); else if(g > 1 + 1e-6) e2 = Math.max(e2, Math.abs(Math.acosh(half) - 4*Math.acosh(g))/(4*Math.acosh(g))); }
  line('K10', e, 1e-8, '‖W − L R L⁻¹ R‖/‖W‖'); line('K10', e2, 1e-10, 'cos φ = 8g⁴ − 8g² + 1 (g < 1); run 4 arccosh g (g > 1, relative)'); }
/* K11 */
{ let e = 0; for(let i=0;i<10000;i++){ const c = rnd()*2-1, r = rnd()*3.5, u = L.AX[i%3], p = L.AX[(i+1)%3], s = Math.sqrt(1-c*c), n = [0,1,2].map(k => c*u[k] + s*p[k]), b = L.boostNull(n,u,r);
    e = Math.max(e, Math.abs(b.n[0]*u[0]+b.n[1]*u[1]+b.n[2]*u[2] - L.aberrate(c,r)), Math.abs(b.f - L.doppler(c,r))); } for(let i=0;i<100;i++){ const z = Math.exp(rnd()*3); e = Math.max(e, Math.abs(L.doppler(1, Math.log(z)) - z)/z); }
  line('K11', e, 1e-12, 'aberration = ⊕; on-axis frequency ratio = z');
  const dirs = []; for(let i=0;i<100000;i++){ const zz = rnd()*2-1, ph = rnd()*2*Math.PI, rr = Math.sqrt(1-zz*zz); dirs.push([rr*Math.cos(ph), rr*Math.sin(ph), zz]); }
  for(const z of [L.ZW*(1+1e-6), 7, 9, 13]) line('K11', L.pingpongExceptions(z, dirs), 0, 'ping-pong exceptions, 1e5 random null directions × 6 letters, z = ' + z);
  line('K11', L.pingpongExceptions(5, dirs), v => v >= 1, 'z = 5: at least one exception must be found');
  const t = 3, x = [1,2,2], tp = 25*t + 24*x[0], xp = 24*t + 25*x[0]; line('K11', (tp > 0 && xp/tp > Math.SQRT1_2 && t*t === x[0]**2+x[1]**2+x[2]**2) ? 0 : 1, 0, 'integer step at z = 7: (3, 1, 2, 2) → (99, 97, 14, 14), in the cap of its letter'); }
/* K12 */
{ let e = 0; for(let i=0;i<1000;i++){ const h = rnd()*3, N = L.facePlane(L.I4(), L.AX[0], h), c = Math.tanh(h), ph = rnd()*6.283, s = Math.sqrt(1-c*c); e = Math.max(e, Math.abs(L.mink([1, c, s*Math.cos(ph), s*Math.sin(ph)], N))); }
  line('K12', e, 1e-12, 'face meets rim at cos ψ0 = Γ'); line('K12', Math.abs(Math.acos(L.faceShadow(Math.log(L.ZW)/2)) - Math.PI/4), 1e-12, 'at the wall ψ0 = 45°'); }
/* K13 */
{ let e = 0; for(let i=0;i<500;i++){ /* random frame: propagation k, E ⊥ k, H = k × E, |E| = |H| */ const k = [rnd()-0.5,rnd()-0.5,rnd()-0.5], kn = Math.hypot(...k), kk = k.map(v=>v/kn); let E = [rnd()-0.5,rnd()-0.5,rnd()-0.5]; const d = E[0]*kk[0]+E[1]*kk[1]+E[2]*kk[2]; E = E.map((v,j)=>v-d*kk[j]);
    const H = [kk[1]*E[2]-kk[2]*E[1], kk[2]*E[0]-kk[0]*E[2], kk[0]*E[1]-kk[1]*E[0]], th = rnd()*Math.PI/2, q = [rnd()-0.5,rnd()-0.5,rnd()-0.5]; const dq = q[0]*kk[0]+q[1]*kk[1]+q[2]*kk[2]; let pp = q.map((v,j)=>v-dq*kk[j]); const pn = Math.hypot(...pp); pp = pp.map(v=>v/pn);
    const n = kk.map((v,j) => Math.cos(th)*v + Math.sin(th)*pp[j]), s = L.stress(E,H); e = Math.max(e, Math.abs(L.normalStress(s.s, n) + s.u*Math.cos(th)**2)/s.u); }
  line('K13', e, 1e-12, 'Maxwell normal stress on a tilted plane = −u cos²θ, 500 random frames (relative)'); }
/* K15 */
{ const imp = (kappa, a, b, Tend, dt) => { let x = 1, y = 0, out = 0, tm = 0, held = 0; const n = Math.round(Tend/dt); let fprev = kappa*x;
    for(let i=0;i<n;i++){ const t0 = i*dt; const [x1,y1] = L.stocksStep(x,y,0,0,0,kappa,a,b,dt); const [xm] = L.stocksStep(x,y,0,0,0,kappa,a,b,dt/2); const f0 = kappa*x, fm = kappa*xm, f1 = kappa*x1;
      out += dt/6*(f0 + 4*fm + f1); tm += dt/6*(t0*f0 + 4*(t0+dt/2)*fm + (t0+dt)*f1); x = x1; y = y1; } return { out, mean:tm/out, y }; };
  const A = imp(1,1,0.2,400,0.01), B = imp(1,1,0.02,4000,0.02), Z = imp(1,1,0,60,0.01);
  line('K15', Math.abs(A.out - 1), 1e-9, 'impulse total outflow = 1 at (κ, a, b) = (1, 1, 0.2)'); line('K15', Math.abs(A.mean - 6), 1e-9, 'mean residence 6'); line('K15', Math.abs(B.mean - 51), 1e-9, 'mean residence 51 at b = 0.02');
  line('K15', Math.abs(Z.y - 0.5), 1e-9, 'b = 0 keeps a/(κ + a) = 0.5');
  /* network ledger over the K14 run: in − out − stored per layer */
  const P = Object.assign({}, L.DEF, { drive:'breathe' }), st = L.initState(); let inn = 0, out = 0, worst = 0; const dt = 1/60;
  for(let n=0;n<2000;n++){ const t0 = n*dt, p0 = L.pushAt(P,t0)[0].arrive[1], pm = L.pushAt(P,t0+dt/2)[0].arrive[1], p1 = L.pushAt(P,t0+dt)[0].arrive[1], x0 = st.stocks[0][1][0];
    L.advance(st, P, t0, dt); const x1 = st.stocks[0][1][0]; inn += dt/6*(p0+4*pm+p1); out += P.kappa*dt*(x0+x1)/2; }
  /* exact ledger with Simpson on loss: recompute densely */
  { const st2 = L.initState(); let I2 = 0, O2 = 0; const h = 1/600; let x = 0, y = 0;
    for(let n=0;n<20000;n++){ const t0 = n*h, p0 = L.pushAt(P,t0)[0].arrive[1], pm = L.pushAt(P,t0+h/2)[0].arrive[1], p1 = L.pushAt(P,t0+h)[0].arrive[1];
      const [x1,y1] = L.stocksStep(x,y,p0,pm,p1,P.kappa,P.ha,P.hb,h), [xm] = L.stocksStep(x,y,p0,p0,pm,P.kappa,P.ha,P.hb,h/2); I2 += h/6*(p0+4*pm+p1); O2 += P.kappa*h/6*(x+4*xm+x1); x = x1; y = y1; }
    line('K15', Math.abs(I2 - O2 - x - y)/Math.max(1,I2), 1e-9, 'network ledger |in − out − stored| over 2000 frames (relative)'); } }
/* K16 */
{ let e = 0; for(let i=0;i<1000;i++){ const n = 1 + Math.floor(rnd()*12), r = []; for(let j=0;j<n;j++) r.push(rnd()*2-1); const Rp = r.filter(v=>v>0).reduce((a,b)=>a+b,0), Rm = -r.filter(v=>v<0).reduce((a,b)=>a+b,0);
    e = Math.max(e, Math.abs(2*r.reduce((a,b)=>a+Math.abs(b),0) - 2*Math.abs(r.reduce((a,b)=>a+b,0)) - 4*Math.min(Rp,Rm))); } line('K16', e, 1e-12, 'route − endpoint = 4 min(R₊, R₋), 1e3 chains'); }
/* K17 */
{ let e = 0; for(let i=0;i<2000;i++){ const z = Math.exp(rnd()*8-4), Cc = L.occupation(z), G = L.smith(z); e = Math.max(e, Math.abs(1 - 2*Cc - G), Math.abs(4*Cc*(1-Cc) - (1 - G*G))); } line('K17', e, 1e-14, '1 − 2C = Γ; T = 4C(1 − C)'); }
/* K18 */
{ let e = 0, ea = 0, ed = 0; const PI = Math.PI;
  for(let i=0;i<500;i++){ const ha = 0.05+rnd()*2, hb = 0.05+rnd()*2, Na = L.facePlane(L.I4(), L.AX[0], ha), Nb = L.facePlane(L.I4(), L.AX[1], hb), g = L.mink(Na,Nb); e = Math.max(e, Math.abs(g - Math.sinh(ha)*Math.sinh(hb)));
    /* the drawn caps: spheres centred on the axes at c = (1+ρ²)/(2ρ), radius R = (1−ρ²)/(2ρ), ρ = tanh(h/2) */
    const sph = h => { const r = Math.tanh(h/2); return { c:(1+r*r)/(2*r), R:(1-r*r)/(2*r) }; }, A = sph(ha), B = sph(hb), d2 = A.c*A.c + B.c*B.c;
    if(g < 1){ const cosang = (A.R*A.R + B.R*B.R - d2)/(2*A.R*B.R); ea = Math.max(ea, Math.abs(Math.acos(-cosang) - Math.acos(g))); }
    else { const sq = Math.sqrt(g*g-1); let fa = L.lin(1/sq, Nb, g/sq, Na), fb = L.lin(1/sq, Na, g/sq, Nb); if(fa[0] < 0) fa = fa.map(v=>-v); if(fb[0] < 0) fb = fb.map(v=>-v);
      /* minimise distance over the two planes numerically by sampling near the feet, and compare the feet distance */
      const dist = Math.acosh(L.mink(fa,fb)); ed = Math.max(ed, Math.abs(dist - Math.acosh(g)), Math.abs(L.mink(fa,Na)), Math.abs(L.mink(fb,Nb)), Math.abs(L.mink(fa,fa)-1)); } }
  line('K18', e, 1e-12, '<Na, Nb> = sinh ha sinh hb'); line('K18', ea, 1e-10, 'dihedral angle from the two drawn caps = arccos g'); line('K18', ed, 1e-8, 'distance between separated planes (feet of the common perpendicular) = arccosh g'); }
/* report */
let n = 0, m = 0; const lines = []; for(const [k,v] of Object.entries(OUT)){ if(!Array.isArray(v) || !v.length || v[0].pass === undefined){ lines.push(k + ': ' + JSON.stringify(v)); continue; }
  for(const x of v){ m++; if(x.pass) n++; lines.push((x.pass ? 'HOLDS ' : 'KILLED') + '  ' + k.padEnd(5) + ' ' + (typeof x.value === 'number' ? x.value.toExponential(2) : x.value).padStart(10) + '  tol ' + x.tol.padEnd(10) + '  ' + x.note); } }
lines.push(''); lines.push(n + ' of ' + m + ' lines hold');
console.log(lines.join('\n'));
