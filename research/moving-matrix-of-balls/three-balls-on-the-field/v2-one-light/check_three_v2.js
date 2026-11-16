// SCRIPT: TB-PAGE-CHECK-V2 — both pages: one light through three balls; hand-over shares, fit of the crossings, misplacement, screenshots
const { chromium } = require('playwright');
(async () => { const b = await chromium.launch({ args:['--use-gl=swiftshader','--enable-unsafe-swiftshader'] }); const out = {};
  for(const [tag, file] of [['mixer','Three_Balls_on_the_Field_Mixer_v2_20261115.html'], ['surprise','Three_Balls_on_the_Field_Surprise_v2_20261115.html']]){
    const p = await b.newPage({ viewport:{ width:1500, height:900 } }); const errs = []; p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if(m.type() === 'error') errs.push(m.text()); });
    await p.goto('file://' + process.cwd() + '/' + file); await p.waitForTimeout(6000); const o = out[tag] = { errs };
    const read = async () => p.evaluate(() => { const h = __tb.HO; return { share:h.share, gap:h.gap, nk:h.nk }; });
    for(const s of [0,1,2]){ await p.evaluate(k => document.querySelector('#tb button[data-kick="'+k+'"]').click(), s); await p.waitForTimeout(1500); o['kick'+'ABC'[s]] = await read(); await p.screenshot({ path:'shots2/' + tag + '_kick' + 'ABC'[s] + '.png' }); }
    await p.evaluate(() => { document.querySelector('#tb button[data-kick="0"]').click(); __tb.X.eps = 0.3; }); await p.waitForTimeout(1500); o.off03 = await read(); await p.screenshot({ path:'shots2/' + tag + '_off.png' });
    await p.evaluate(() => { __tb.X.eps = 0; }); await p.waitForTimeout(600);
    o.fps = await p.evaluate(() => new Promise(r => { let n = 0; const t = performance.now(); (function f(){ n++; if(performance.now() - t < 2000) requestAnimationFrame(f); else r(n/2); })(); }));
    o.rows = await p.evaluate(() => { __tb.rows(); return document.getElementById('tb_rows').innerText; }); await p.close(); }
  require('fs').writeFileSync('check_three_v2.out.json', JSON.stringify(out, null, 1)); console.log(JSON.stringify(out, null, 1)); await b.close(); })();
