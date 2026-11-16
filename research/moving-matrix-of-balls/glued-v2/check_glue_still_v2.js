// SCRIPT: MM-GLUE-STILL-V2 — same page with the faces held still (drive depth 0): who arrives first
const { chromium } = require('playwright');
(async () => { const b = await chromium.launch({ args:['--use-gl=swiftshader'] }), p = await b.newPage({ viewport:{ width:1200, height:800 } });
  await p.goto('file://' + process.cwd() + '/Moving_Matrix_of_Balls_Glued_v2_20261115.html'); await p.waitForTimeout(1000);
  const r = await p.evaluate(() => { __LHS.CLOCK.playing = false; __LHS.P.amp = 0; __LHS.mBuild(); for(let f=0;f<600;f++) __LHS.step(1/60); const s = __LHS.state; let both=0, first=0; for(let i=1;i<37;i++) if(s.MAL[i]!==null && s.MAS[i]!==null){ both++; if(s.MAL[i] < s.MAS[i]) first++; } return { first, both, books: s.MEN.E - s.ME0 - s.MS.work - s.MIN, work: s.MS.work }; });
  console.log(JSON.stringify(r)); require('fs').writeFileSync('check_glue_still_v2.out.json', JSON.stringify(r)); await b.close(); })();
