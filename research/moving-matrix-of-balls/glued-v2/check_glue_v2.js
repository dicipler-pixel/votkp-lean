// SCRIPT: MM-GLUE-PAGE-CHECK-V2 — loads the page, runs the clock, reads the matrix rows, screenshots
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ args:['--use-gl=swiftshader','--enable-unsafe-swiftshader'] }); const p = await b.newPage({ viewport:{ width:1400, height:880 } });
  const errs = []; p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if(m.type() === 'error') errs.push(m.text()); });
  await p.goto('file://' + process.cwd() + '/Moving_Matrix_of_Balls_Glued_v2_20261115.html'); await p.waitForTimeout(1500);
  // run the page clock by hand: 600 frames of 1/60 (tau = 10)
  const t0 = Date.now(); await p.evaluate(() => { __LHS.CLOCK.playing = false; for(let f=0;f<600;f++) __LHS.step(1/60); }); const ms = Date.now() - t0;
  const rows = await p.evaluate(() => document.getElementById('mm').innerText);
  const st = await p.evaluate(() => { const s = __LHS.state; return { books: s.MEN.E - s.ME0 - s.MS.work - s.MIN, work: s.MS.work, faces: s.MEN.EF, nn: s.MNN }; });
  await p.screenshot({ path:'shots/whole.png' });
  await p.evaluate(() => { __LHS.S3.setView([0.55,0.28,3.4,0]); }); await p.waitForTimeout(500); await p.screenshot({ path:'shots/centre.png' });
  await p.evaluate(() => { document.getElementById('clean').click(); __LHS.S3.setView([0.7,0.32,6.2,0]); }); await p.waitForTimeout(600); await p.screenshot({ path:'shots/clean.png' });
  await p.evaluate(() => { document.getElementById('back').click(); __LHS.CLOCK.playing = true; }); await p.waitForTimeout(2500);
  const fps = await p.evaluate(() => new Promise(r => { let n = 0; const t = performance.now(); (function f(){ n++; if(performance.now() - t < 2000) requestAnimationFrame(f); else r(n/2); })(); }));
  await p.setViewportSize({ width:390, height:844 }); await p.waitForTimeout(800); await p.screenshot({ path:'shots/phone.png' });
  const out = { ms_600_frames:ms, fps, st, rows, errs }; require('fs').writeFileSync('check_glue_v2.out.json', JSON.stringify(out, null, 1)); console.log(JSON.stringify(out, null, 1));
  await b.close();
})();
