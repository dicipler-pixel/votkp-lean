// SCRIPT: SF-PAGE-CHECK-V1 — perfect world books, each dial, all as measured; screenshots
const { chromium } = require('playwright');
(async () => { const b = await chromium.launch({ args:['--use-gl=swiftshader','--enable-unsafe-swiftshader'] }); const p = await b.newPage({ viewport:{ width:1600, height:900 } }); const out = {}, errs = [];
  p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if(m.type() === 'error') errs.push(m.text()); });
  await p.goto('file://' + process.cwd() + '/Solar_Field_v1_20261115.html'); await p.waitForTimeout(9000);
  const snap = async () => p.evaluate(() => { const B = __sf.BOOK; return { d:__sf.PL.map(q => +q.d.toFixed(4)), share:B.share, straight:B.straight, free:B.free, sum:B.rim + B.cut + B.small, ledger:B.ledger, flux:B.flux, cons:B.cons, wob:__sf.wob }; });
  out.perfect = await snap(); await p.screenshot({ path:'shots/perfect.png' });
  await p.waitForTimeout(12000); out.perfect_later = await snap();
  for(const k of ['steps','ellipse','tilt','timing','field']){ await p.evaluate(k => { ['steps','ellipse','tilt','timing','field'].forEach(q => __sf.setDial(q, q === k ? 1 : 0)); }, k); await p.waitForTimeout(9000); out['only_' + k] = await snap(); await p.screenshot({ path:'shots/only_' + k + '.png' }); }
  await p.evaluate(() => document.getElementById('sf_real').click()); await p.waitForTimeout(12000); out.real = await snap(); await p.screenshot({ path:'shots/real.png' });
  out.fps = await p.evaluate(() => new Promise(r => { let n = 0; const t = performance.now(); (function f(){ n++; if(performance.now() - t < 2000) requestAnimationFrame(f); else r(n/2); })(); }));
  out.errs = errs; require('fs').writeFileSync('check_solar_v1.out.json', JSON.stringify(out, null, 1));
  const s = o => ({ d:o.d, share:o.share.map(x => +x.toExponential(2)), straight:o.straight.map(x => +x.toExponential(2)), free:o.free.map(x => +x.toExponential(2)), sum:o.sum, flux:o.flux, cons:o.cons, wob:o.wob && o.wob.map(w => +(w[1]-w[0]).toExponential(1)) });
  for(const k of Object.keys(out)) console.log(k, typeof out[k] === 'object' && out[k].share ? JSON.stringify(s(out[k])) : JSON.stringify(out[k])); await b.close(); })();
