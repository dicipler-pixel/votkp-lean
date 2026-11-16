/* SCRIPT: SF-CHECK-V3 — checks of the raw data and the chart, run before the page is built. */
const SFH = require('./sf_helio_v3.js'), D = require('./sf_raw_data_v3.json'), H = SFH(D), jd = Date.UTC(2026, 10, 16, 12)/86400000 + 2440587.5, S = H.state(jd), out = { date:H.dateOf(jd), jd };
/* 1. two independent sources against each other: each planet's distance from the JPL elements must lie between the fact sheet's perihelion and aphelion, all the way round the orbit */
out.range = H.PLANETS.map(p => { let lo = 1e99, hi = 0; for(let k=0;k<3600;k++){ const r = H.norm(H.posOf(p, jd, 2*Math.PI*k/3600))/1e6; lo = Math.min(lo, r); hi = Math.max(hi, r); } return { name:p.name, jplMin:+lo.toFixed(1), sheetPeri:p.peri_1e6km, jplMax:+hi.toFixed(1), sheetAph:p.aph_1e6km, ok:Math.abs(lo - p.peri_1e6km)/p.peri_1e6km < 0.003 && Math.abs(hi - p.aph_1e6km)/p.aph_1e6km < 0.003 }; });
/* 2. poles (IAU) against obliquities (fact sheet), through the orbit normals (JPL) */
out.obliquity = H.obliquityCheck(jd).map(o => ({ name:o.name, fromPole:+o.fromPole.toFixed(2), sheet:o.sheet, diff:+o.diff.toFixed(2) }));
/* 3. the ball's own share formula against flat space: must agree, because the chart keeps true shapes */
out.share = S.rows.slice(1).map(r => ({ name:r.name, flat:r.light, ball:r.lightBall, rel:Math.abs(r.light/r.lightBall - 1) }));
/* 4. a known number: sunlight the Earth takes, share x luminosity; and at the Earth's distance per square metre */
const e = S.rows[3]; out.earth = { rAU:e.r/H.AU, watts:e.watts, perM2:D.constants.sun_luminosity_W/(4*Math.PI*Math.pow(e.r*1000, 2)) };
/* 5. the books close */
out.books = { lightSum:S.lightSum, rimLight:1 - S.lightSum, windSum:S.windSum, rimWind:1 - S.windSum };
out.edges = S.rows.slice(1).map(r => ({ name:r.name, edgeR:r.edge ? +r.edge.toFixed(2) : null, measured:H.PLANETS.find(p => p.name === r.name).edge_measured_R || null }));
out.leader = { sunMassShare:S.sunMassShare, baryInSunRadii:S.baryR, lead:S.lead.map(x => +x.toFixed(6)), gram:S.gram };
out.now = S.rows.slice(1).map(r => ({ name:r.name, AU:+(r.r/H.AU).toFixed(4), gamma:+r.gamma.toFixed(6), step:+r.step.toFixed(6), T:+r.T.toFixed(8), lightMin:+(r.lightSec/60).toFixed(2), lonDeg:+((Math.atan2(r.pos[1], r.pos[0])*180/Math.PI + 360) % 360).toFixed(2) }));
require('fs').writeFileSync('check_helio_v3.out.json', JSON.stringify(out, null, 1)); console.log(JSON.stringify(out, null, 1));
