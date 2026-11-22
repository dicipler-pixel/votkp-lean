/* SCRIPT: SEA-CHECK-03 — proves the faces can be taken out of the transport and put back live.
   (a) with live off, faces x transport must equal the sweep's one-step map on random seas, to 1e-12 (this is the step the page runs);
   (b) at rest the link signs sgn(d_i . R_ij d_j) must all be +1, or the "at rest = v2 signs" claim fails;
   (c) with live on, the tied rest sea must stay at rest (rates = 1, 1/3, 1/5, 1/7 at the page's z) and the books must hold through a kick;
   (d) the travel rule with live faces: far ball first move vs light crossing. */
const MM = require('../mm/mm_math_v1.js'), FL = require('./fl_math_v2.js'), S2 = require('./sea_math_v2.js'), S3 = require('./sea_math_v3.js'), fs = require('fs');
const RS = JSON.parse(fs.readFileSync('rest_seas_02.json', 'utf8')); const restOf = k => { const R = RS[k], u8 = Buffer.from(R.b64, 'base64'); return { M:R.M, rank:R.rank, margin:R.margin, h:R.h, tri:new Float32Array(u8.buffer, u8.byteOffset, u8.length/4) }; };
let fails = 0; const say = (ok, s) => { console.log((ok ? 'HOLDS  ' : 'KILLED ') + s); if(!ok) fails++; };
for(const [N, key] of [[3, '3|z|sealed'], [4, '4|z|sealed'], [7, '7|z|sealed']]){ const rest = restOf(key), base = { N, z:[3,5,7], clocks:'z', h:rest.h, machine:'tied', ends:'sealed', feed:'none', push:false, rest };
  const A = S2.make(FL, MM, base), B = S3.make(FL, MM, Object.assign({}, base, { live:false })), M = A.M; let seed = 7; const rnd = () => (seed = (seed*16807) % 2147483647)/2147483647 - 0.5;
  /* (a) random Hermitian sea, one step each */
  const Hr = new Float64Array(M*M), Hi = new Float64Array(M*M); for(let i=0;i<M;i++) for(let j=i;j<M;j++){ const a = rnd(), b = i === j ? 0 : rnd(); Hr[i*M+j] = a; Hr[j*M+i] = a; Hi[i*M+j] = b; Hi[j*M+i] = -b; }
  A.Pr.set(Hr); A.Pi.set(Hi); B.Pr.set(Hr); B.Pi.set(Hi); S2.step(A); S3.step(B); let dmax = 0; for(let k=0;k<M*M;k++) dmax = Math.max(dmax, Math.abs(A.Pr[k]-B.Pr[k]), Math.abs(A.Pi[k]-B.Pi[k]));
  say(dmax < 1e-12, N + ' balls (a) faces x transport = sweep map: max difference ' + dmax.toExponential(2) + ' on M = ' + M);
  /* (b) signs at rest */
  const L = S3.liveRates(B); S3.step(B); const Lb = S3.read(B).L; say(Object.values(Lb.sigma).every(s => s === 1), N + ' balls (b) link signs at rest: ' + Object.values(Lb.sigma).join(' '));
  /* (c) live on: rest stays rest, rates at the page's z */
  const C = S3.make(FL, MM, Object.assign({}, base, { live:true })); const r0 = S3.read(C); for(let k=0;k<Math.round(5/rest.h);k++) S3.step(C); const r1 = S3.read(C), Lc = r1.L;
  say(Math.max(...r1.leak) < 1e-6 && Math.abs(r1.trace - C.tr0) < 1e-9, N + ' balls (c) live, at rest for t = 5: largest ball change ' + Math.max(...r1.leak).toExponential(1) + ', books ' + (r1.trace - C.tr0).toExponential(1) + ', rates ' + Lc.rate.map(x => x.toFixed(4)).join(' ') + ' (page: ' + C.W.balls.map(b => b.rate.toFixed(4)).join(' ') + '), z ' + Lc.z.map(x => x.toFixed(3)).join(' '));
  /* (d) kick, live faces: books and travel */
  const D = S3.make(FL, MM, Object.assign({}, base, { live:true, feed:'kick' })); let first = null, trmax = 0; const T = N >= 7 ? 6 : 4; while(D.t < T - 1e-9){ S3.step(D); const r = S3.read(D); trmax = Math.max(trmax, Math.abs(r.trace - D.tr0)); if(first === null && r.farChange > 1e-6) first = D.t; }
  const rd = S3.read(D); say(trmax < 1e-8 && first !== null && first >= D.cross - D.h, N + ' balls (d) kick with live faces: books held to ' + trmax.toExponential(1) + ', far ball first moved at ' + (first === null ? '—' : first.toFixed(2)) + ' (light needs ' + D.cross.toFixed(2) + '), rates now ' + rd.L.rate.map(x => x.toFixed(4)).join(' ') + ', faces now ' + rd.faces.slice(0, 4).map(f => f.rho.toFixed(4)).join(' ') + ', signs ' + Object.values(rd.L.sigma).join(' ')); }
console.log(fails ? fails + ' KILLED' : 'all hold');
