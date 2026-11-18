/* SCRIPT: SB3-SHOT-V1 — screenshots of the seven balls page. */
const { chromium } = require('playwright'); (async () => { const b = await chromium.launch({ args:['--use-gl=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] }), p = await b.newPage({ viewport:{ width:1500, height:900 } }); const errs = []; p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if(m.type() === 'error') errs.push(m.text()); });
  await p.goto('file://' + __dirname + '/Seven_Balls_v3_his_light_20261118.html'); await p.waitForTimeout(3000); const steps = JSON.parse(process.argv[2] || '[]'); let n = 0; const out = [];
  for(const s of steps){ if(s.click) for(const c of s.click) await p.click(c); await p.waitForTimeout(s.wait || 5000);
    out.push(await p.evaluate(() => ({ t:window.__SB3.W.t.toFixed(2), pk:window.__SB3.W.pk.length, num:document.getElementById('num').innerText.replace(/\n/g, ' | ').slice(0, 500) })));
    await p.screenshot({ path:__dirname + '/s' + (n++) + '.png' }); }
  console.log(JSON.stringify({ errs, out }, null, 1)); await b.close(); })();
