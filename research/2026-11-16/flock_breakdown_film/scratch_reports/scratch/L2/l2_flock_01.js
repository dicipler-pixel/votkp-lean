// SCRIPT: L2-FLOCK-01
// Flock-specific geometry used in fl_math_v1.js, checked against its own functions (read-only require) and against closed forms.
const FL = require('/home/claude/balls/w/fl/fl_math_v1.js');
const MM = require('/home/claude/balls/w/mm/mm_math_v1.js');
const LH = require('/home/claude/balls/in/367c3aed-Light_at_the_Hypersurface_Mixer_v2_Source/lh_math_v1.js');
const mink = MM.mink, O = [1,0,0,0], AX = MM.AXES;
const ball = (a, r) => [Math.cosh(r), Math.sinh(r)*AX[a][0], Math.sinh(r)*AX[a][1], Math.sinh(r)*AX[a][2]];
// closed form for the crossing: <x,O> = <x,p> on x(s) = (sinh(d-s) pa + sinh(s) pb)/sinh d  =>  tanh s = A sinh d / (B + A cosh d)
function sClosed(pa, pb, d, p){ const A = mink(pa,O) - mink(pa,p), B = mink(pb,p) - mink(pb,O); return Math.atanh(A*Math.sinh(d)/(B + A*Math.cosh(d))); }
console.log('F1 (a) order of crossings on the arm-arm link, grid z_a, z_b in [1.5, 13] step 0.25 (47 x 47 = 2209 pairs), arms +I and +J');
let bad = 0, n = 0, eClosed = 0, minIn = 1e9, minInAt = null, cellBad = 0, monoBad = 0, worstStretchVsDelta = 1e9, wsAt = null;
for(let za = 1.5; za <= 13.0001; za += 0.25) for(let zb = 1.5; zb <= 13.0001; zb += 0.25){ n++;
  const ra = Math.log(za), rb = Math.log(zb), pa = ball(0, ra), pb = ball(2, rb), d = MM.linkDistance(pa, pb);
  const s1 = FL.crossAt(pa, pb, d, O, pa), s2 = FL.crossAt(pa, pb, d, O, pb);
  const c1 = sClosed(pa, pb, d, pa), c2 = d - sClosed(pb, pa, d, pb);
  eClosed = Math.max(eClosed, Math.abs(s1-c1), Math.abs(s2-c2));
  if(!(0 < s1 && s1 < s2 && s2 < d)) bad++;
  if(s2 - s1 < minIn){ minIn = s2 - s1; minInAt = [za, zb, s1, s2, d]; }
  // one sign change only of f(s) = <x,O> - <x,pa> (crossAt's bisection needs it)
  for(const [u, v] of [[O,pa],[O,pb]]){ let ch = 0, prev = null; for(let k=0;k<=400;k++){ const x = FL.geo(pa,pb,d,d*k/400), f = mink(x,u)-mink(x,v); if(prev != null && (f>0) !== (prev>0)) ch++; prev = f; } if(ch !== 1) monoBad++; }
  // between the crossings the point is nearer the centre than all six neighbours one step out (same step taken on the unused arms: use the larger of the two)
  for(let k=1;k<20;k++){ const x = FL.geo(pa,pb,d,s1 + (s2-s1)*k/20), dO = mink(x,O); if(!(dO < mink(x,pa) && dO < mink(x,pb))) cellBad++; }
  const g = Math.sinh(ra/2)*Math.sinh(rb/2); if(g > 1){ const del = Math.acosh(g), ex = (s2-s1) - del; if(ex < worstStretchVsDelta){ worstStretchVsDelta = ex; wsAt = [za,zb,s2-s1,del]; } } }
console.log('   pairs with 0 < s1 < s2 < d violated: '+bad+' of '+n+' ; bisection against closed form, largest difference: '+eClosed.toExponential(2));
console.log('   crossings that are not a single sign change: '+monoBad+' ; sample points between s1 and s2 not nearest the centre: '+cellBad);
console.log('   shortest stretch inside the centre cell: s2 - s1 = '+minIn.toFixed(4)+' at z = '+minInAt[0]+','+minInAt[1]+' (s1 = '+minInAt[2].toFixed(4)+', s2 = '+minInAt[3].toFixed(4)+', d = '+minInAt[4].toFixed(4)+')');
console.log('   where g > 1: least (s2 - s1) - delta = '+worstStretchVsDelta.toFixed(4)+' at z = '+wsAt[0]+','+wsAt[1]+' (stretch '+wsAt[2].toFixed(4)+', delta '+wsAt[3].toFixed(4)+')');
console.log('F2 the same for all 12 perpendicular arm pairs at z = (3,5,7), and the check file values');
{ const z = [3,5,7]; let b2 = 0, m = 0; for(let a=0;a<6;a++) for(let b=a+1;b<6;b++){ if((a>>1) === (b>>1)) continue; m++; const ra = Math.log(z[a>>1]), rb = Math.log(z[b>>1]), pa = ball(a,ra), pb = ball(b,rb), d = MM.linkDistance(pa,pb), s1 = FL.crossAt(pa,pb,d,O,pa), s2 = FL.crossAt(pa,pb,d,O,pb); if(!(0<s1&&s1<s2&&s2<d)) b2++; } console.log('   pairs out of order: '+b2+' of '+m); }
for(const [za,zb] of [[3,5],[5,7],[7,9],[9,13],[3+2*Math.SQRT2,3+2*Math.SQRT2],[7,7]]){ const ra = Math.log(za), rb = Math.log(zb), pa = ball(0,ra), pb = ball(2,rb), d = MM.linkDistance(pa,pb), s1 = FL.crossAt(pa,pb,d,O,pa), s2 = FL.crossAt(pa,pb,d,O,pb), g = Math.sinh(ra/2)*Math.sinh(rb/2);
  console.log('   z = '+za.toFixed(3)+','+zb.toFixed(3)+'  d = '+d.toFixed(4)+' (arccosh(cosh ra cosh rb) = '+Math.acosh(Math.cosh(ra)*Math.cosh(rb)).toFixed(4)+')  s1 = '+s1.toFixed(4)+'  s2 = '+s2.toFixed(4)+'  stretch in centre cell = '+(s2-s1).toFixed(4)+'  g = '+g.toFixed(4)+'  delta = '+(g>1?Math.acosh(g).toFixed(4):'none')); }
console.log('F3 the gap mark: Flock uses rho = tanh(k delta), passes sech^2(k delta). Against LH.tunnelGap (M3 evanescent film) at kappa_e = Y1 (return phase pi/2)');
{ let e = 0, e2 = 0; for(let i=0;i<200;i++){ const k = 0.2 + 2*Math.random(), w = 3*Math.random(), Y = 0.3 + 2*Math.random(); const t = LH.tunnelGap(Y, Y, k, w); e = Math.max(e, Math.abs(t.T - 1/Math.cosh(k*w)**2));
    const ke = 0.2 + 2*Math.random(), t2 = LH.tunnelGap(Y, ke, k, w), ph = 2*Math.atan(ke/Y)/1, sn = Math.sin(ph/1); const phi = Math.atan2(2*Y*ke, Y*Y-ke*ke); e2 = Math.max(e2, Math.abs(t2.T - Math.sin(phi)**2/(Math.sinh(k*w)**2 + Math.sin(phi)**2))); }
  console.log('   |T_film - sech^2(k w)| at kappa_e = Y1: '+e.toExponential(2)+' ; general |T_film - sin^2 phi/(sinh^2 kw + sin^2 phi)|, phi = arg of the face return: '+e2.toExponential(2));
  console.log('   example z = 7,9, delta = 0.9730, k = 1: sech^2 = '+(1/Math.cosh(0.972955075)**2).toFixed(6)+' ; film at kappa_e = Y1/2: '+LH.tunnelGap(1,0.5,1,0.972955075).T.toFixed(6)+' ; at kappa_e = 2 Y1: '+LH.tunnelGap(1,2,1,0.972955075).T.toFixed(6)); }
console.log('F4 the arm-arm link rotation in the Flock (MM.linkRotation) and the Thomas turn: holonomy round centre, ball a, ball b against 2 arctan(Ga Gb)');
{ let e = 0, e1 = 0; for(let i=0;i<200;i++){ const ra = 0.1 + 2.5*Math.random(), rb = 0.1 + 2.5*Math.random(), pa = ball(0,ra), pb = ball(2,rb);
    const Roa = MM.linkRotation(O,pa), Rab = MM.linkRotation(pa,pb), Rbo = MM.linkRotation(pb,O), H = MM.m3(Roa, MM.m3(Rab, Rbo)), ang = MM.rotAngle(H), f = 2*Math.atan(Math.tanh(ra/2)*Math.tanh(rb/2));
    e = Math.max(e, Math.abs(ang - f)); e1 = Math.max(e1, MM.rotAngle(Roa), MM.rotAngle(Rbo), Math.abs(MM.rotAngle(Rab) - f)); }
  console.log('   holonomy angle - 2 arctan(Ga Gb): '+e.toExponential(2)+' ; centre-arm link rotations are the identity and the arm-arm link rotation alone carries the angle: '+e1.toExponential(2)); }
console.log('F5 clocks: rate = exp(-r) = 1/z against (1-G)/(1+G) and against LH.doppler(-1, r)');
{ let e = 0; for(const z of [1.5,3,5,7,9,13]){ const r = Math.log(z), G = Math.tanh(r/2); e = Math.max(e, Math.abs(Math.exp(-r) - (1-G)/(1+G)), Math.abs(Math.exp(-r) - LH.doppler(-1, r)), Math.abs(z - LH.doppler(1, r))/z); } console.log('   largest residual: '+e.toExponential(2)); }
console.log('F6 LH.selftest() (the page arithmetic, run from node, nothing written)');
{ const t = LH.selftest(); console.log('   '+t.filter(x => x.pass).length+' of '+t.length+' lines hold'); for(const x of t) if(/K8|K9|K10|K11|K12|K18|K13/.test(x.id)) console.log('   '+(x.pass?'HOLDS ':'FAILS ')+x.id+'  value '+Number(x.value).toExponential(2)+'  tol '+x.tol); }
