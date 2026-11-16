// SCRIPT: SR-PAGE-CHECK-V1 — loads the page, runs each level, reads rows, eigen view, screenshots
const { chromium } = require('playwright');
(async () => { const b = await chromium.launch({ args:['--use-gl=swiftshader','--enable-unsafe-swiftshader'] }), p = await b.newPage({ viewport:{ width:1400, height:880 } });
  const errs = []; p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if(m.type() === 'error') errs.push(m.text()); });
  await p.goto('file://' + process.cwd() + '/The_Series_of_the_Ball_v1_20261115.html'); await p.waitForTimeout(1500);
  const out = {};
  for(const L of [1,2,3]){ const t0 = Date.now();
    await p.evaluate(l => { __LHS.CLOCK.playing = false; document.querySelector('button[data-xl="'+l+'"]').click(); for(let f=0;f<(l===3?240:360);f++) __LHS.step(1/60); }, L);
    out['L'+L+'_ms'] = Date.now() - t0; out['L'+L] = await p.evaluate(() => document.getElementById('xr').innerText);
    await p.evaluate(() => { document.getElementById('clean').click(); __LHS.S3.setView([0.7,0.32,6.0,0]); }); await p.waitForTimeout(700); await p.screenshot({ path:'shots/L'+L+'_light.png' });
    await p.evaluate(() => document.getElementById('back').click()); }
  await p.evaluate(() => { document.querySelector('button[data-xl="2"]').click(); __LHS.SX.n = 40; document.getElementById('x_mode').click(); __LHS.step(1/60); __LHS.step(1/60); document.getElementById('clean').click(); __LHS.S3.setView([0.7,0.32,6.0,0]); });
  await p.waitForTimeout(700); await p.screenshot({ path:'shots/L2_eigen40.png' }); await p.evaluate(() => document.getElementById('back').click());
  out.eig = await p.evaluate(() => document.getElementById('xr').innerText);
  await p.evaluate(() => { __LHS.CLOCK.playing = true; }); await p.waitForTimeout(2000);
  out.fps = await p.evaluate(() => new Promise(r => { let n = 0; const t = performance.now(); (function f(){ n++; if(performance.now() - t < 2000) requestAnimationFrame(f); else r(n/2); })(); }));
  out.errs = errs; require('fs').writeFileSync('check_series_v1.out.json', JSON.stringify(out, null, 1)); console.log(JSON.stringify(out, null, 1)); await b.close(); })();
