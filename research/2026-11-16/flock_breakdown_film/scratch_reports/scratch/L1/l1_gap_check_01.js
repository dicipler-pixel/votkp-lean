// SCRIPT: L1-GAP-CHECK-01
// Lineage 1 checks for the breakdown: the gap element of the Flock against film_is_oplus, and the face scatterer against step_matching.
// Reads FL-MATH-V1 and MM-MATH-V1 read-only (require); writes nothing.
const FL = require('/home/claude/balls/w/fl/fl_math_v1.js');
const C = { add:(a,b)=>[a[0]+b[0],a[1]+b[1]], sub:(a,b)=>[a[0]-b[0],a[1]-b[1]], mul:(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]],
  div:(a,b)=>{const d=b[0]*b[0]+b[1]*b[1];return[(a[0]*b[0]+a[1]*b[1])/d,(a[1]*b[0]-a[0]*b[1])/d];}, abs2:a=>a[0]*a[0]+a[1]*a[1], sc:(a,s)=>[a[0]*s,a[1]*s], exp:a=>[Math.exp(a[0])*Math.cos(a[1]),Math.exp(a[0])*Math.sin(a[1])] };
const oplus = (u,v) => C.div(C.add(u,v), C.add([1,0], C.mul(u,v)));
let seed = 7; const rnd = () => (seed = (seed*16807) % 2147483647)/2147483647;
let bad = 0; const line = (name, err, tol, txt) => { const ok = err <= tol; if(!ok) bad++; console.log((ok?'HOLDS  ':'FAILS  ')+name+'  worst '+err.toExponential(1)+' (tol '+tol.toExponential(0)+')'+(txt?'  '+txt:'')); };

// independent route: wave matching in the three regions (no oplus used). Medium Y1 | gap admittance i*ke, decay kp, width w | medium Y1.
// u = 1 e^{..} + r ; gap: A e^{-kp x} + B e^{kp x}; right: t. Continuity of u and of the flux Y*(forward - backward).
function filmByMatching(Y1, ke, kp, w){ const Yg = [0, ke], q = Math.exp(-kp*w);
  // unknowns r, A, B, t (complex): 1 + r = A + B ; Y1(1 - r) = Yg(A - B) ; A q + B/q = t ; Yg(A q - B/q) = Y1 t
  // from the last two: A q = t (Yg + Y1)/(2 Yg), B/q = t (Yg - Y1)/(2 Yg). Set t = 1, then scale.
  const Aq = C.div(C.add(Yg,[Y1,0]), C.sc(Yg,2)), Bq = C.div(C.sub(Yg,[Y1,0]), C.sc(Yg,2)), A = C.sc(Aq, 1/q), B = C.sc(Bq, q);
  const E = C.add(A,B), H = C.div(C.mul(Yg, C.sub(A,B)), [Y1,0]), inc = C.sc(C.add(E,H),0.5), ref = C.sc(C.sub(E,H),0.5);
  return { r:C.div(ref,inc), t:C.div([1,0],inc) }; }

// T1 film_is_oplus with |r0| = 1 against direct wave matching, and the closed form |t|^2 = sin^2 phi/(sinh^2 kd + sin^2 phi), phi = arg r0.
{ let e1 = 0, e2 = 0, e3 = 0, e4 = 0;
  for(let i=0;i<2000;i++){ const Y1 = 0.1+3*rnd(), ke = 0.1+3*rnd(), kp = 0.1+2*rnd(), w = 3*rnd();
    const r0 = C.div([Y1,-ke],[Y1,ke]), x = C.sc(C.sc(r0,-1), Math.exp(-2*kp*w)), r = oplus(r0, x), M = filmByMatching(Y1, ke, kp, w);
    const phi = Math.atan2(r0[1], r0[0]), s2 = Math.sin(phi)**2, sh2 = Math.sinh(kp*w)**2, T = s2/(sh2+s2);
    e1 = Math.max(e1, Math.hypot(r[0]-M.r[0], r[1]-M.r[1])); e2 = Math.max(e2, Math.abs(C.abs2(M.t) - T)); e3 = Math.max(e3, Math.abs(C.abs2(r) - sh2/(sh2+s2))); e4 = Math.max(e4, Math.abs(C.abs2(r0)-1)); }
  line('T1a |r0| = 1 (total_reflection)', e4, 1e-12);
  line('T1b r0 (+) (-r0 e^{-2kd}) = r from direct wave matching', e1, 1e-11);
  line('T1c |t|^2 = sin^2 phi / (sinh^2 kd + sin^2 phi)', e2, 1e-11);
  line('T1d |r|^2 = sinh^2 kd / (sinh^2 kd + sin^2 phi)', e3, 1e-11); }

// T2 at phi = pi/2 (ke = Y1): r = r0 tanh(kd), |t| = sech(kd); and tanh(kd) = (zg - 1)/(zg + 1) with zg = e^{2kd}: one peel step of length 2kd.
{ let e1 = 0, e2 = 0, e3 = 0, e4 = 0;
  for(let i=0;i<2000;i++){ const Y1 = 0.1+3*rnd(), kd = 4*rnd(), r0 = C.div([Y1,-Y1],[Y1,Y1]), r = oplus(r0, C.sc(r0, -Math.exp(-2*kd))), M = filmByMatching(Y1, Y1, 1, kd);
    const want = C.sc(r0, Math.tanh(kd)), zg = Math.exp(2*kd);
    e1 = Math.max(e1, Math.hypot(r[0]-want[0], r[1]-want[1])); e2 = Math.max(e2, Math.abs(Math.sqrt(C.abs2(M.t)) - 1/Math.cosh(kd)));
    e3 = Math.max(e3, Math.abs(Math.tanh(kd) - (zg-1)/(zg+1))); e4 = Math.max(e4, Math.abs(Math.log((1+Math.tanh(kd))/(1-Math.tanh(kd))) - 2*kd)/(1+2*kd)); }
  const r0 = C.div([1,-1],[1,1]), M = filmByMatching(1, 1, 1, 0.7);
  line('T2a phi = pi/2: r = r0 tanh(kd)', e1, 1e-12, 'r0 = ('+r0.map(v=>v.toFixed(3)).join(', ')+') = -i');
  line('T2b phi = pi/2: |t| = sech(kd)', e2, 1e-12);
  line('T2c tanh(kd) = (zg-1)/(zg+1), zg = e^{2kd}', e3, 1e-12);
  line('T2d ln((1+rho)/(1-rho)) = 2kd (relative; kd up to 4)', e4, 1e-9);
  console.log('       sample kd = 0.7: film r = ('+M.r.map(v=>v.toFixed(6)).join(', ')+'), t = ('+M.t.map(v=>v.toFixed(6)).join(', ')+'); tanh = '+Math.tanh(0.7).toFixed(6)+', sech = '+(1/Math.cosh(0.7)).toFixed(6)); }

// T3 the Flock's gap marks: rho = tanh(kgap*delta), delta = arccosh(sinh(ra/2) sinh(rb/2)); and the K4 numbers from the formula alone.
{ let e = 0, out = [];
  for(const z of [[3,5,7],[5,7,9],[7,9,11],[9,13,13]]){ const W = FL.makeWorld({ N:3, z, gamma:0 }), l = W.links[2], ra = Math.log(z[0]), rb = Math.log(z[1]);
    const g = Math.sinh(ra/2)*Math.sinh(rb/2), del = g > 1 ? Math.acosh(g) : 0, gm = l.marks.find(m => m.kind === 'gap'), fm = l.marks.filter(m => m.kind === 'face');
    e = Math.max(e, Math.abs(fm[0].rho - (z[0]-1)/(z[0]+1)), Math.abs(fm[1].rho + (z[1]-1)/(z[1]+1)), Math.abs((gm ? gm.rho : 0) - Math.tanh(del)), Math.abs(l.g - g));
    const first = (1-fm[0].rho**2)*(1-fm[1].rho**2)/Math.cosh(del)**2; out.push('z='+z[0]+','+z[1]+': g='+g.toFixed(4)+' delta='+del.toFixed(4)+' marks rho=['+l.marks.map(m => m.rho.toFixed(6)).join(', ')+'] first pass='+first.toFixed(10)); }
  line('T3 Flock marks: face rho = +(za-1)/(za+1), -(zb-1)/(zb+1); gap rho = tanh(delta)', e, 1e-12); out.forEach(s => console.log('       '+s)); }

// T4 the scatterer [[tau, -rho],[rho, tau]] is the flux-normalised form of step_matching: with Y1/Y2 = z,
//    r = (Y1-Y2)/(Y1+Y2), t = 2Y1/(Y1+Y2); rho = r, tau = sqrt(Y2/Y1) t = sqrt(1 - r^2); from the far side the reflection is -r and tau is the same.
{ let e = 0; for(let i=0;i<2000;i++){ const Y1 = 0.1+3*rnd(), Y2 = 0.1+3*rnd(), r = (Y1-Y2)/(Y1+Y2), t = 2*Y1/(Y1+Y2), r2 = (Y2-Y1)/(Y2+Y1), t2 = 2*Y2/(Y1+Y2);
    e = Math.max(e, Math.abs(Math.sqrt(Y2/Y1)*t - Math.sqrt(1-r*r)), Math.abs(Math.sqrt(Y1/Y2)*t2 - Math.sqrt(1-r*r)), Math.abs(r2 + r), Math.abs(r - Math.tanh(Math.log(Y1/Y2)/2))); }
  line('T4 flux-normalised step: tau = sqrt(Y2/Y1) t = sqrt(1-Gamma^2) both ways, Gamma21 = -Gamma12, Gamma = tanh(ln(Y1/Y2)/2)', e, 1e-12); }

// T5 cascade of real scatterers [[tau,-rho],[rho,tau]] with no phase between them: the sum of all echoes is the (+)-sum, rapidities add.
//    Time-domain: three scatterers on a line, unit pulse in from the left, open ends (no ports), run until the echoes have died.
function cascade(rhos, lens, steps){ const m = rhos.length + 1, f = lens.map(n => new Float64Array(n)), b = lens.map(n => new Float64Array(n)), hd = new Array(m).fill(0); let R = 0, T = 0, first = null;
  f[0][(hd[0]-1+lens[0])%lens[0]] = 1;
  for(let s=0;s<steps;s++){ const fo = [], bo = []; for(let k=0;k<m;k++){ fo[k] = f[k][hd[k]]; bo[k] = b[k][hd[k]]; }
    R += bo[0]; T += fo[m-1]; if(first === null && fo[m-1] !== 0) first = fo[m-1];
    const fin = new Array(m).fill(0), bin = new Array(m).fill(0);
    for(let k=1;k<m;k++){ const rho = rhos[k-1], tau = Math.sqrt(1-rho*rho); fin[k] = tau*fo[k-1] - rho*bo[k]; bin[k-1] = rho*fo[k-1] + tau*bo[k]; }
    for(let k=0;k<m;k++){ f[k][hd[k]] = fin[k]; b[k][hd[k]] = bin[k]; hd[k] = (hd[k]+1)%lens[k]; } }
  return { R, T, first }; }
{ const za = 7, zb = 9, ra = Math.log(za), rb = Math.log(zb), del = Math.acosh(Math.sinh(ra/2)*Math.sinh(rb/2)), rhos = [Math.tanh(ra/2), Math.tanh(del), -Math.tanh(rb/2)];
  const o = cascade(rhos, [40, 13, 17, 40], 400000), tot = ra/2 + del - rb/2;
  line('T5a first pass amplitude = tau_a tau_g tau_b', Math.abs(o.first - Math.sqrt((1-rhos[0]**2)*(1-rhos[1]**2)*(1-rhos[2]**2))), 1e-12, 'first '+o.first.toFixed(10)+', squared '+(o.first**2).toFixed(10));
  line('T5b sum of all echoes back = tanh(ra/2 + delta - rb/2)', Math.abs(o.R - Math.tanh(tot)), 1e-9, 'sum '+o.R.toFixed(10)+', tanh '+Math.tanh(tot).toFixed(10));
  line('T5c sum of all echoes on = sech(ra/2 + delta - rb/2)', Math.abs(o.T - 1/Math.cosh(tot)), 1e-9, 'sum '+o.T.toFixed(10)+', sech '+(1/Math.cosh(tot)).toFixed(10));
  const o2 = cascade([Math.tanh(ra/2), -Math.tanh(rb/2)], [40, 13, 40], 400000);
  line('T5d no gap: echoes back sum to (zb... ) tanh((ra-rb)/2) = (za-zb)/(za+zb) (stack_telescopes / directed_composite)', Math.abs(o2.R - (za-zb)/(za+zb)), 1e-9, 'sum '+o2.R.toFixed(10)+', (za-zb)/(za+zb) '+((za-zb)/(za+zb)).toFixed(10)); }

// T6 does the sign convention on an arm-arm link matter to the run? Same world, the three marks of the B-C link negated in memory. Compare light in each ball.
{ const run = flip => { const W = FL.makeWorld({ N:3, z:[7,9,11] }); if(flip) W.links[2].marks.forEach(m => m.rho = -m.rho); const S = FL.initState(W, { source:1 }); const out = []; for(const T of [5, 10, 20, 40]){ FL.advance(W, S, T - S.t); out.push([0,1,2].map(i => FL.ballLight(S,i))); } return { out, b:FL.books(W,S).total }; };
  const a = run(false), b = run(true); let d = 0; a.out.forEach((row,k) => row.forEach((v,i) => d = Math.max(d, Math.abs(v - b.out[k][i]))));
  console.log('NOTE   T6 arm-arm marks negated (kick B, z = 7,9,11): largest change in any ball light at t = 5,10,20,40: '+d.toExponential(2)+'; books '+a.b.toFixed(12)+' and '+b.b.toFixed(12));
  console.log('       as built   t=40: '+a.out[3].map(v => v.toFixed(6)).join(' ')+'\n       negated    t=40: '+b.out[3].map(v => v.toFixed(6)).join(' ')); }
console.log(bad ? bad+' line(s) FAIL' : 'all lines hold');
