// SCRIPT: SF-PAGE-CHECK-V2 — each ball its own body: sizes, field edges computed vs measured, screenshots (field and close on each body)
const { chromium } = require('playwright');
(async () => { const b = await chromium.launch({ args:['--use-gl=swiftshader','--enable-unsafe-swiftshader'] }); const p = await b.newPage({ viewport:{ width:1600, height:900 } }); const out = {}, errs = [];
  p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if(m.type() === 'error') errs.push(m.text()); });
  await p.goto('file://' + process.cwd() + '/Solar_Field_v2_20261115.html'); await p.waitForTimeout(8000);
  out.bodies = await p.evaluate(() => __sf.BODY.map((b, k) => ({ name:b.name, size:+__sf.sizeOf(b).toFixed(3), edge:+(__sf.BG[k].r0 || 0).toFixed(3), measured:b.mp })));
  await p.screenshot({ path:'shots2/field_perfect.png' });
  await p.evaluate(() => document.getElementById('sf_real').click()); await p.waitForTimeout(6000);
  out.real = await p.evaluate(() => __sf.BODY.map((b, k) => ({ name:b.name, edge:+(__sf.BG[k].r0 || 0).toFixed(3) }))); await p.screenshot({ path:'shots2/field_real.png' });
  for(const [f,n] of [[0,'sun'],[1,'mercury'],[3,'earth'],[4,'mars']]){ await p.evaluate(f => document.querySelector('#sf_zoom button[data-f="'+f+'"]').click(), f); await p.waitForTimeout(1500); await p.screenshot({ path:'shots2/close_'+n+'.png' }); }
  out.table = await p.evaluate(() => document.getElementById('sf_bod').innerText.slice(0, 700));
  out.fps = await p.evaluate(() => new Promise(r => { let n = 0; const t = performance.now(); (function f(){ n++; if(performance.now() - t < 2000) requestAnimationFrame(f); else r(n/2); })(); }));
  out.errs = errs; require('fs').writeFileSync('check_solar_v2.out.json', JSON.stringify(out, null, 1)); console.log(JSON.stringify(out, null, 1)); await b.close(); })();
