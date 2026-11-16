// SCRIPT: TB-PAGE-CHECK-V1 — both pages: load, run, read the panel, screenshots
const { chromium } = require('playwright');
(async () => { const b = await chromium.launch({ args:['--use-gl=swiftshader','--enable-unsafe-swiftshader'] }); const out = {};
  for(const [tag, file] of [['mixer','Three_Balls_on_the_Field_Mixer_v1_20261115.html'], ['surprise','Three_Balls_on_the_Field_Surprise_v1_20261115.html']]){
    const p = await b.newPage({ viewport:{ width:1500, height:900 } }); const errs = []; p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if(m.type() === 'error') errs.push(m.text()); });
    await p.goto('file://' + process.cwd() + '/' + file); await p.waitForTimeout(9000);
    out[tag] = { rows: await p.evaluate(() => { __tb.rows(); return document.getElementById('tb_rows').innerText; }), books: await p.evaluate(() => __tb.books()), errs };
    await p.screenshot({ path:'shots/' + tag + '_light.png' });
    await p.evaluate(() => { document.getElementById('tb_view').click(); document.getElementById('tb_lead').click(); }); await p.waitForTimeout(1500); await p.screenshot({ path:'shots/' + tag + '_leading.png' });
    await p.evaluate(() => { document.getElementById('tb_view').click(); document.querySelector('#tb button[data-kick="2"]').click(); }); await p.waitForTimeout(2500); await p.screenshot({ path:'shots/' + tag + '_kickC.png' });
    out[tag].fps = await p.evaluate(() => new Promise(r => { let n = 0; const t = performance.now(); (function f(){ n++; if(performance.now() - t < 2000) requestAnimationFrame(f); else r(n/2); })(); }));
    await p.evaluate(() => document.getElementById('tb_one').click()); await p.waitForTimeout(800); await p.screenshot({ path:'shots/' + tag + '_one.png' }); await p.close(); }
  require('fs').writeFileSync('check_three_v1.out.json', JSON.stringify(out, null, 1)); console.log(JSON.stringify(out, null, 1)); await b.close(); })();
