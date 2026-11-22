/* SCRIPT: HEAT-SEA-02 — the sea heat put on the links only (port angle at each ball), against the heat on the balls, in the page's own engine (SEA-MATH-V2).
   Fixed before the run: same marks as HEAT-SEA-01. Also checks the balls heat at amplitude 1 against SEA-RUNS-02 (far ball leak max 1.76e-4, lifted end 2.84e-4). */
const MM = require('../mm/mm_math_v1.js'), FL = require('./fl_math_v2.js'), SEA = require('./sea_math_v2.js'), fs = require('fs');
const R = JSON.parse(fs.readFileSync('rest_seas_02.json', 'utf8'))['3|z|sealed'], u8 = Buffer.from(R.b64, 'base64'), rest = { M:R.M, rank:R.rank, margin:R.margin, h:R.h, tri:new Float32Array(u8.buffer, u8.byteOffset, u8.length/4) };
for(const on of ['balls', 'links']) for(const a of [0, 0.1, 0.3, 1.0]){ const t0 = Date.now(), E = SEA.make(FL, MM, { N:3, z:[3,5,7], clocks:'z', h:R.h, machine:'tied', ends:'sealed', feed:'squeeze_in', push:false, rest, heat:a, heatOn:on }); const mx = [0,0,0];
  while(E.t < 20 - 1e-9){ SEA.step(E); const r = SEA.read(E); for(let i=0;i<3;i++) mx[i] = Math.max(mx[i], r.leak[i]); } const r = SEA.read(E);
  console.log(on, 'heat', a, 'leak end', r.leak.map(x => x.toExponential(2)).join(' '), 'leak max', mx.map(x => x.toExponential(2)).join(' '), 'lifted', r.lifted.toExponential(2), 'tie A-C', r.tie.filter(t => t[0] === 0 && t[1] === 2)[0][2].toExponential(2), ((Date.now()-t0)/1000).toFixed(1) + ' s'); }
