const { chromium } = require('playwright'); (async () => { const b = await chromium.launch({ args:['--use-gl=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] }), p = await b.newPage({ viewport:{ width:1500, height:900 } }); const errs = []; p.on('pageerror', e => errs.push(String(e)));
  await p.goto('file://' + __dirname + '/Solar_Field_v3_20261116.html'); await p.waitForTimeout(1500);
  const a = await p.evaluate(() => { const S = window.__SF3; S.setV('zoom', 80); S.setV('travel', 30); S.setV('speed', 60); return [S.jd(), S.state().rows[3].r]; }); await p.waitForTimeout(3000);
  const c = await p.evaluate(() => { const S = window.__SF3; return [S.jd(), S.state().rows[3].r, S.V.speed, document.getElementById('sf_date').textContent, document.getElementById('sf_focus').textContent]; });
  await p.evaluate(() => document.getElementById('sf_now').click()); await p.waitForTimeout(500); const d = await p.evaluate(() => [window.__SF3.jd(), window.__SF3.V.speed, document.getElementById('sf_t3').innerText.slice(0, 400)]);
  console.log(JSON.stringify({ errs, a, c, d }, null, 1)); await b.close(); })();
