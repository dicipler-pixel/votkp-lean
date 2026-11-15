// SCRIPT: MM-PAGE-CHECK-V1 — loads the page, visits every eye at levels 1/2/3, reads rows, checks kill lines, screenshots.
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ args:['--use-gl=swiftshader','--enable-unsafe-swiftshader'] }); const p = await b.newPage({ viewport:{ width:1400, height:860 } });
  const errs = []; p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if(m.type() === 'error') errs.push(m.text()); });
  await p.goto('file://' + process.cwd() + '/Moving_Matrix_of_Balls_Mixer_v1_20261115.html'); await p.waitForTimeout(2500);
  const out = {};
  for(const L of [1,2,3]){
    await p.evaluate(l => { __mm.play(false); __mm.level(l); }, L);
    const t0 = Date.now(); await p.evaluate(l => __mm.run(l === 3 ? 3 : 4), L); const ms = Date.now() - t0;
    for(const id of 'ABCDEFGHIJ'){ await p.evaluate(i => __mm.go(i), id); await p.waitForTimeout(L === 3 ? 1200 : 400); out[L + id] = await p.evaluate(() => __mm.rows());
      if((L === 2) || (L === 3 && 'ABI'.includes(id)) || (L === 1 && id === 'J')) await p.screenshot({ path:`shots/L${L}_${id}.png` }); }
    out[L + '_ms'] = ms;
  }
  await p.evaluate(() => { __mm.level(2); __mm.play(true); }); await p.waitForTimeout(3000);
  const fps = await p.evaluate(() => new Promise(r => { let n = 0; const t = performance.now(); (function f(){ n++; if(performance.now() - t < 2000) requestAnimationFrame(f); else r(n/2); })(); }));
  out.fps_L2 = fps; out.errs = errs;
  await p.setViewportSize({ width:390, height:844 }); await p.waitForTimeout(800); await p.screenshot({ path:'shots/phone_L2.png' });
  require('fs').writeFileSync('mm_page_check_v1.out.json', JSON.stringify(out, null, 1)); console.log(JSON.stringify(out, null, 1).slice(0, 9000));
  await b.close();
})();
