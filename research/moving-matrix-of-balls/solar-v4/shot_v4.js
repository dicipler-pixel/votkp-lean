/* SCRIPT: SF-SHOT-V4 — opens the built page, sets views and edge dials, saves pictures, reports errors and the edge table. */
const { chromium } = require('playwright'); (async () => { const b = await chromium.launch({ args:['--use-gl=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] }), p = await b.newPage({ viewport:{ width:1500, height:900 } }); const errs = []; p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if(m.type() === 'error') errs.push(m.text()); });
  await p.goto('file://' + __dirname + '/Solar_Field_v4_20261116.html'); await p.waitForTimeout(2500);
  const views = JSON.parse(process.argv[2]); let n = 0, tab = [];
  for(const v of views){ await p.evaluate(v => { const S = window.__SF3; S.edge('flow', v[4]); S.edge('field', v[5]); S.edge('n', v[6]); S.setV('zoom', v[0]); S.setV('travel', v[1]); S.setV('across', v[2]); S.setV('up', v[3]); }, v); await p.waitForTimeout(1000); await p.screenshot({ path:__dirname + '/shots/w' + (n++) + '.png' }); tab.push(await p.evaluate(() => document.getElementById('sf_t5').innerText)); }
  console.log(JSON.stringify({ errs, tab }, null, 1)); await b.close(); })();
