/* SCRIPT: SF-SHOT-V3 — opens the built page, sets views by the percent sliders, saves pictures for inspection, reports page errors. */
const { chromium } = require('playwright'); (async () => { const b = await chromium.launch({ args:['--use-gl=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] }), p = await b.newPage({ viewport:{ width:1500, height:900 } }); const errs = []; p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if(m.type() === 'error') errs.push(m.text()); });
  await p.goto('file://' + __dirname + '/Solar_Field_v3_20261116.html'); await p.waitForTimeout(2500);
  const views = JSON.parse(process.argv[2] || '[[0,0,0,0]]'); let n = 0;
  for(const v of views){ await p.evaluate(v => { const S = window.__SF3; S.setV('zoom', v[0]); S.setV('travel', v[1]); S.setV('across', v[2]); S.setV('up', v[3]); if(window.__TBHOST.S3.view){ } }, v); await p.waitForTimeout(900); await p.screenshot({ path:__dirname + '/shots/v' + (n++) + '.png' }); }
  console.log(JSON.stringify({ errs, has:await p.evaluate(() => !!window.__SF3) })); await b.close(); })();
