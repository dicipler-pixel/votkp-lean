/* SCRIPT: SB3-CHECK-02 — the seven balls with his light, every ball the same size, fixed before the run.
   (a) Each neighbour ball is his face. Its sphere meets C's rim at right angles (c² − R² = 1) and, as a plane of C's hyperboloid,
       is his facePlane at h = r/2 up to scale; the circle where it meets C's rim is his shadow, cos ψ = Γ = tanh(r/2).
       Why it proves it: a sphere at right angles to the rim is a plane of his ball's geometry; equal planes reflect and pass light the same way.
       Kill line: any of the three off by more than 1e-12, over all six balls and 200 times through the breaths.
   (b) His light, unchanged. With the balls held at τ = 0 and his fan, every segment that stays inside C (word empty) in this tracer
       has the same start, the same hit point and the same flux as in his own traceRay (LH-MATH-V1), and so does the first passed direction.
       Why: the faces are the same planes, the split is his function, so the paths must agree; beyond a face his tree has further
       faces that are not real balls here, so those segments are not compared. Kill line: any difference above 1e-9.
   (c) The books: emitted = in flight + on the ground + below the cut, to 1e-12, three breaths, breathing on, both ways of light,
       the source shining every 2 time units. Why: every split has R + T = 1 (his step: |r|² + (Y2/Y1)|t|² = 1), so light can only
       be moved, booked on the ground, or booked below the cut. Kill line: above 1e-12.
   (d) His light never leaves C: in 'his' no packet is ever outside C's unit ball. In 'room' light does reach the neighbours outside C.
       Kill line: 'his' any |q| ≥ 1; 'room' nothing ever outside C.
   (e) The moving balls do sweep over light: the number of crossings made by a ball moving over a packet is reported, and with
       breathing off it is exactly 0. Kill line: nonzero with breathing off. */
const L = require('./lh_math_v1.js'), SB = require('./sb3_light_v2.js'); let fails = 0; const say = (ok, s) => { console.log((ok ? 'HOLDS  ' : 'KILLED ') + s); if(!ok) fails++; };
{ let e1 = 0, e2 = 0, e3 = 0; const P = Object.assign({}, L.DEF), WALL = 3 + 2*Math.SQRT2, PW = Object.assign({}, L.DEF, { zI:WALL, zJ:WALL, zK:WALL, drive:'hold' });
  for(let n=0;n<200;n++){ const tau = n*0.4, B = SB.balls(P, tau);
    for(let i=1;i<7;i++){ const b = B[i], near = b.cc - b.R, apex = Math.tanh(b.h/2); e1 = Math.max(e1, Math.abs(near - apex), Math.abs(b.R - 1)); } }
  const BW = SB.balls(PW, 0); for(let i=1;i<7;i++){ const b = BW[i]; e2 = Math.max(e2, Math.abs(b.cc*b.cc - b.R*b.R - 1));
    const pl = SB.planeOf(b), F = L.facePlane(L.I4(), L.genU(i - 1), b.h), sc = pl.n[0]/F[0]; for(let q=0;q<4;q++) e2 = Math.max(e2, Math.abs(pl.n[q] - sc*F[q])); e2 = Math.max(e2, Math.abs(pl.C0)); e3 = Math.max(e3, Math.abs(1/b.cc - Math.tanh(b.r/2))); }
  say(Math.max(e1, e2, e3) < 1e-12, '(a) every ball radius 1; a neighbour\'s near point is his face apex tanh(r/4) at every time ' + e1.toExponential(1) + ' (6 balls × 200 times); on his wall the neighbour is his face: at right angles and his facePlane ' + e2.toExponential(1) + ', shadow ' + e3.toExponential(1)); }
{ const P = Object.assign({}, L.DEF, { zI:3 + 2*Math.SQRT2, zJ:3 + 2*Math.SQRT2, zK:3 + 2*Math.SQRT2, drive:'hold' }), S = L.feed(P, 0), his = L.traceAll(S, 1e-3), dirs = L.fanDirs(S); let worst = 0, nCmp = 0, nPass = 0, miss = 0;
  dirs.forEach((d, j) => { const mine = SB.traceStatic(P, 0, P.omega, d, 1e-3).filter(s => s.word.length === 0), hs = his.filter(s => s.ray === j && s.word.length === 0);
    for(const h of hs){ const m = mine.find(x => x.depth === h.depth && Math.abs(x.flux - h.flux) < 1e-6 && Math.max(...[0,1,2,3].map(q => Math.abs(x.X[q] - h.X[q]))) < 1e-6);
      if(!m){ miss++; continue; } nCmp++;
      for(let q=0;q<4;q++){ worst = Math.max(worst, Math.abs(m.X[q] - h.X[q]), Math.abs(m.V[q] - h.v[q])); }
      worst = Math.max(worst, Math.abs(m.flux - h.flux));
      if(h.end === 'face'){ if(m.end !== 'face'){ miss++; continue; } for(let q=0;q<4;q++) worst = Math.max(worst, Math.abs(m.hit[q] - h.hit[q])); worst = Math.max(worst, Math.abs(m.R - h.sp.R));
        if(h.tt && m.tt){ nPass++; for(let q=0;q<4;q++) worst = Math.max(worst, Math.abs(m.tt[q] - h.tt[q])); } } } });
  say(worst < 1e-9 && miss === 0 && nCmp > 0, '(b) his light unchanged, on his wall (where the balls are his faces): ' + nCmp + ' segments inside C and ' + nPass + ' first passed directions compared with his traceRay, largest difference ' + worst.toExponential(1) + ', unmatched ' + miss); }
for(const mode of ['his', 'room']){ const W = SB.makeWorld({ mode, emitEvery:2 }); SB.emit(W); let dev = 0, outC = 0, maxQ = 0, sweeps0 = 0;
  while(W.t < 24){ SB.step(W, 0.02); const b = SB.books(W); dev = Math.max(dev, Math.abs(b.total - b.emitted)); for(const k of W.pk){ const q = SB.posOf(W, k), r = Math.hypot(q[0], q[1], q[2]); maxQ = Math.max(maxQ, r); if(r > 1 + 1e-9) outC++; } }
  const b = SB.books(W);
  say(dev < 1e-12, '(c) books, ' + mode + ': emitted ' + b.emitted + ' = in flight ' + b.flight.toFixed(4) + ' + ground ' + b.ground.toFixed(4) + ' + below cut ' + b.cut.toFixed(4) + ' · largest deviation ' + dev.toExponential(1) + ' · walls met ' + W.nHits + ' · packets now ' + W.pk.length);
  if(mode === 'his') say(maxQ < 1, '(d) his light never leaves C: largest |q| ' + maxQ.toFixed(6));
  else say(outC > 0, '(d) room light does reach the neighbours outside C: packet-steps outside C ' + outC);
  const by = b.inBall; console.log('    light in flight by ball at t = 24 (' + mode + '): C ' + by[0].toFixed(4) + ' · ' + [1,2,3,4,5,6].map(i => W.B[i].name + ' ' + by[i].toFixed(4)).join(' · ') + ' · ground by ball ' + Array.from(W.groundBy).map(x => x.toFixed(3)).join(' ')); }
for(const breathe of [false, true]){ const W = SB.makeWorld({ mode:'his', breathe, emitEvery:2 }); SB.emit(W); let n0 = 0;
  /* count crossings made by moving balls: wrap step to count hits not from events */ const before = () => W.nHits; let evHits = 0;
  while(W.t < 24){ const h0 = W.nHits; SB.step(W, 0.02); evHits += W.nHits - h0; }
  /* run again with the sweep alone counted: the difference between a step with the balls frozen and moving */
  const W2 = SB.makeWorld({ mode:'his', breathe, emitEvery:2 }); SB.emit(W2); let sw = 0; while(W2.t < 24){ const pk = W2.pk.map(k => ({ X:k.X.slice(), word:k.word.slice() })), B = W2.B; SB.step(W2, 0.02); }
  if(!breathe){ const Wf = SB.makeWorld({ mode:'his', breathe:false, emitEvery:2 }); SB.emit(Wf); let swept = 0; while(Wf.t < 24){ const PL = Wf.PL; SB.step(Wf, 0.02); for(const k of Wf.pk) for(let j=1;j<7;j++){ if((SB.Fval(PL[j], k.X) < 0) !== (SB.Fval(Wf.PL[j], k.X) < 0)) swept++; } }
    say(swept === 0, '(e) breathing off: a ball moved over a packet ' + swept + ' times'); }
  else { const Wb = SB.makeWorld({ mode:'his', breathe:true, emitEvery:2 }); SB.emit(Wb); let swept = 0; const orig = SB.step;
    while(Wb.t < 24){ const pre = Wb.pk.map(k => ({ X:k.X, w:k.word })), PL = Wb.PL, Bn = SB.balls(Wb.P, Wb.t + 0.02).map(SB.planeOf); for(const k of pre) for(let j=1;j<7;j++){ /* after the step's own moves this is approximate: count packets that a ball's move alone would cross */ if((SB.Fval(PL[j], k.X) < 0) !== (SB.Fval(Bn[j], k.X) < 0)) swept++; } SB.step(Wb, 0.02); }
    console.log('    breathing on: a ball moves over light about ' + swept + ' times in three breaths (reported)'); } }
console.log(fails ? fails + ' KILLED' : 'all hold');
