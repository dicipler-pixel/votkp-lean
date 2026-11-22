// SCRIPT: SEA-CHECK-01
// Why this decides it: the page's sea mathematics (SEA-MATH-V1, JavaScript) and the sweep's (SEA-RUNS-01, Python) were written separately.
// If the same way, run for the same time, gives the same numbers in both, neither has a private fault.
// Kill: any of trace, lifted, tie at the end differing by more than 2e-5 relative (the stored rest sea is single precision), or first-move time differing.
const MM = require('../mm/mm_math_v1.js'), FL = require('./fl_math_v2.js'), SEA = require('./sea_math_v1.js'), fs = require('fs');
const RS = JSON.parse(fs.readFileSync('rest_seas_01.json')), REF = JSON.parse(fs.readFileSync('rest_ref_01.json')); let kills = 0;
for(const [N, clocks, ends] of [[3,'z','sealed'],[3,'equal','sealed'],[3,'dilation','sealed'],[3,'z','container'],[7,'z','sealed']]){
  const rs = RS[N + '|' + clocks + '|' + ends], buf = Buffer.from(rs.b64, 'base64'), tri = new Float32Array(buf.buffer, buf.byteOffset, buf.length/4), ref = REF[N + '|' + clocks + '|' + ends];
  const E = SEA.make(FL, MM, { N, z:[3,5,7], clocks, h:rs.h, machine:'tied', ends, feed:'kick', push:true, rest:{ M:rs.M, tri, rank:rs.rank, margin:rs.margin } });
  if(!E.ok){ console.log('KILLED', N, clocks, ends, E.why); kills++; continue; }
  const r0 = SEA.read(E), tie0 = r0.tie.filter(t => t[0] === 0 && t[1] === E.far)[0][2]; let first = null, turn = 0; const n = Math.round(30/rs.h), t0 = Date.now();
  /* the kick is applied at make(); the far change is read before each step, as the sweep does */
  for(let k=0;k<n;k++){ if(first === null && k % 1 === 0){ const M = E.M, f = E.far; let df = 0; for(let p=0;p<2;p++) for(let q=0;q<2;q++){ const i = (2*f+p)*M + 2*f+q; df += (E.Pr[i]-E.Rr[i])**2 + (E.Pi[i]-E.Ri[i])**2; } if(Math.sqrt(df) > 1e-6) first = E.t; } SEA.step(E); if(k % 20 === 0) turn = Math.max(turn, ...SEA.read(E).turn); }
  const r = SEA.read(E), tie = r.tie.filter(t => t[0] === 0 && t[1] === E.far)[0][2], rel = (a, b) => Math.abs(a - b)/Math.max(Math.abs(b), 1e-300);
  const ok = rel(r.trace, ref.trace_end) < 2e-5 && rel(r.lifted, ref.lifted_end) < 2e-3 && rel(tie, ref.tie_end) < 2e-2 && Math.abs(first - ref.first_move_time) <= 2*rs.h + 1e-9; if(!ok) kills++;
  console.log(ok ? 'HOLDS ' : 'KILLED', N, 'balls', clocks, ends, '| M', E.M, '| trace', r.trace.toFixed(6), 'vs', ref.trace_end.toFixed(6), '| lifted', r.lifted.toExponential(5), 'vs', ref.lifted_end.toExponential(5), '| tie', tie.toExponential(4), 'vs', ref.tie_end.toExponential(4), '| tie at start', tie0.toExponential(3), 'vs', ref.tie_at_start.toExponential(3), '| first move', first, 'vs', ref.first_move_time, '| ball turn', turn.toFixed(4), 'vs', ref.ball_turn_max.toFixed(4), '|', ((Date.now() - t0)/n).toFixed(1), 'ms/step');
}
console.log(kills ? kills + ' KILLED' : 'ALL HOLD');
