// SCRIPT: L3-RUN-01
// Lineage 3 runs: connection energy identity, triangle loop, speed limit, and the C4 offset reading. Reads unchanged copies only.
const MM = require('/home/claude/balls/w/mm/mm_math_v1.js'), TB = require('/home/claude/balls/w/tb/tb_math_v1.js');
const f = (x,n) => (typeof x === 'number' && isFinite(x)) ? x.toPrecision(n||12) : String(x);
let seed = 7; const rnd = () => (seed = (seed*16807) % 2147483647)/2147483647 - 0.5;
const randD = N => Array.from({length:N}, () => [2*rnd(), 2*rnd(), 2*rnd()]);
console.log('== 1. connection energy identity (1/8)||[H,H*]||^2 = sum_edges ||D_i - U D_j U^dag||^2 ==');
const r0 = [Math.log(3), Math.log(5)];
const W3 = TB.makeWorld(r0), W7 = MM.makeWorld(1);
console.log('3-ball: N', W3.N, 'links', W3.links.length, ' 7-ball: N', W7.N, 'links', W7.links.length);
for(const [name, W] of [['3-ball', W3], ['7-ball', W7]]){
  const a = MM.nnceCheck(W, W.d); console.log(name, 'own d      lhs', f(a.lhs), 'rhs', f(a.rhs), 'diff', (a.lhs-a.rhs).toExponential(2));
  let worst = 0, big = 0; for(let k=0;k<200;k++){ const d = randD(W.N), b = MM.nnceCheck(W, d); worst = Math.max(worst, Math.abs(b.lhs-b.rhs)/Math.max(1e-300, Math.abs(b.rhs))); big = Math.max(big, b.rhs); if(k===0) console.log(name, 'random d #0 lhs', f(b.lhs), 'rhs', f(b.rhs)); }
  console.log(name, '200 random d: worst relative difference', worst.toExponential(2), ' largest rhs', f(big,6));
  // control: spoil one link's U (use the identity instead of the lift of R); the identity must then fail unless R is trivial
  const Wb = Object.assign({}, W, { links:W.links.map((l,k) => k===W.links.length-1 ? Object.assign({}, l, { U:[[1,0],[0,0],[0,0],[1,0]] }) : l) }); const d = randD(W.N), c = MM.nnceCheck(Wb, d);
  console.log(name, 'control (last link U replaced by I, R kept): lhs', f(c.lhs), 'rhs', f(c.rhs), 'rel diff', (Math.abs(c.lhs-c.rhs)/c.rhs).toExponential(2), ' rotation angle of that link', f(MM.rotAngle(W.links[W.links.length-1].R),6)); }
// the matrix that moves the light (applyH) is Hermitian: its own self-commutator
for(const [name, W] of [['3-ball', W3], ['7-ball', W7]]){ const H = MM.denseH(W, randD(W.N)), n = H.n; let herm = 0; for(let i=0;i<n;i++) for(let j=0;j<n;j++) herm = Math.max(herm, Math.abs(H.Hr[i][j]-H.Hr[j][i]), Math.abs(H.Hi[i][j]+H.Hi[j][i])); console.log(name, 'dynamics matrix denseH: largest |H - H^dag| entry', herm.toExponential(2)); }
// face energy against connection energy: faceEnergy = kappa * sum |d_i - R d_j|^2 ; rhs = 2 * sum |d_i - R d_j|^2
{ const d = randD(W7.N), a = MM.nnceCheck(W7, d), F = MM.faceEnergy(W7, d); console.log('7-ball faceEnergy', f(F.E), ' (kappa/2)*rhs', f(W7.opts.kappa/2*a.rhs), ' kappa', W7.opts.kappa); }
// 7-ball triangles
{ let w = 0, n = 0; for(const t of W7.tris){ const h = MM.triangleHolonomy(W7, t); if(h){ w = Math.max(w, Math.abs(h.ang-h.area)); n++; } } console.log('7-ball: triangles', n, ' worst |turn - area|', w.toExponential(2)); }
console.log('\n== 2. loop A->B->C->A ==');
for(const r of [r0, [0.9,0.9], [0.3,2.0], [2.5,2.5]]){ const W = TB.makeWorld(r), lp = TB.loop(W, r); console.log('r =', r.map(x=>x.toFixed(4)).join(','), ' turn', lp.ang.toFixed(10), ' area', lp.area.toFixed(10), ' 2atan(G_I G_J)', lp.thomas.toFixed(10)); }
console.log('\n== 3. sea at t = 0 and the offset reading ==');
{ const W = TB.makeWorld(r0), S = MM.initState(W, { source:0 }); console.log('eigenvalues', S.gap0.toFixed(6), 'gap; rank kSea', S.kSea);
  const G = MM.groundProjector(W, W.d); console.log('levels', G.vals.map(x => x.toFixed(6)).join(' '));
  const C = MM.ballCensus(W, S); C.forEach((c,i) => console.log('ball', TB.NAMES[i], ' nu', c.nu.map(x => x.toPrecision(17)).join(', '), ' 1-nu', c.nu.map(x => (1-x).toExponential(3)).join(', '), ' tau', c.tau, ' S', c.S.toExponential(3), ' trX', c.trX.toExponential(3)));
  console.log('rest d', W.d.map(v => v.map(x => x.toFixed(6)).join(',')).join(' | ')); }
