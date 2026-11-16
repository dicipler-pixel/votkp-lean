// SCRIPT: L2-SIGN-01
// Does the sign of the face marks on the arm-arm links matter? A patched COPY of fl_math_v1.js (original untouched) with the two face signs
// on the arm-arm link swapped (out->centre: -Gamma_a ; centre->out: +Gamma_b, the convention the centre-arm links use) is run beside the original.
const fs = require('fs');
const src = fs.readFileSync('/home/claude/balls/w/fl/fl_math_v1.js', 'utf8');
let p = src.replace("require('../mm/mm_math_v1.js')", "require('/home/claude/balls/w/mm/mm_math_v1.js')");
const a1 = "const marks = [{ s:s1, rho:Math.tanh(balls[a].r/2), kind:'face' }]", a2 = "marks.push({ s:s2, rho:-Math.tanh(balls[b].r/2), kind:'face' })";
if(!p.includes(a1) || !p.includes(a2)) throw new Error('patch anchors not found');
const orig = p; fs.writeFileSync(__dirname + '/fl_math_v1_origcopy.js', orig);
p = p.replace(a1, "const marks = [{ s:s1, rho:-Math.tanh(balls[a].r/2), kind:'face' }]").replace(a2, "marks.push({ s:s2, rho:Math.tanh(balls[b].r/2), kind:'face' })");
fs.writeFileSync(__dirname + '/fl_math_v1_signcopy.js', p);
const A = require('./fl_math_v1_origcopy.js'), B = require('./fl_math_v1_signcopy.js');
for(const [N, src_, zz] of [[3,0,[3,5,7]],[3,1,[3,5,7]],[4,1,[3,5,7]],[3,1,[7,9,13]]]){
  const WA = A.makeWorld({ N, z:zz }), WB = B.makeWorld({ N, z:zz }), SA = A.initState(WA, { source:src_ }), SB = B.initState(WB, { source:src_ });
  let out = 'N = '+N+', z = '+zz.join(',')+', kick ball '+A.NAMES[src_]+': ';
  let worst = 0, wb = 0;
  for(const T of [2, 5, 10, 20, 40]){ A.advance(WA, SA, T - SA.t); B.advance(WB, SB, T - SB.t); const la = [...Array(WA.N).keys()].map(i => A.ballLight(SA,i)), lb = [...Array(WB.N).keys()].map(i => B.ballLight(SB,i));
    const dmax = Math.max(...la.map((x,i) => Math.abs(x-lb[i]))); worst = Math.max(worst, dmax); wb = Math.max(wb, Math.abs(A.books(WA,SA).total-1), Math.abs(B.books(WB,SB).total-1));
    out += '\n   t = '+T+'  light in balls, code as written: '+la.map(x => x.toFixed(4)).join(' ')+' | signs swapped: '+lb.map(x => x.toFixed(4)).join(' ')+' | largest difference '+dmax.toExponential(2); }
  console.log(out + '\n   books residual (both): '+wb.toExponential(2)); }
