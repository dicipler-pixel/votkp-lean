/* SCRIPT: ST3D-SHOT-V1 — screenshots of the page at chosen times. */
const { chromium } = require('playwright'); (async () => { const b = await chromium.launch({ args:['--use-gl=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] }), p = await b.newPage({ viewport:{ width:1500, height:900 } }); const errs = []; p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if(m.type() === 'error') errs.push(m.text()); });
  await p.goto('file://' + __dirname + '/The_Step_3D_v1_20261118.html'); await p.waitForTimeout(2500); const steps = JSON.parse(process.argv[2] || '[]'); let n = 0;
  for(const s of steps){ if(s.click) for(const c of s.click) await p.click(c); await p.waitForTimeout(s.wait || 1500); await p.screenshot({ path:__dirname + '/n' + (n++) + '.png' }); }
  console.log(JSON.stringify({ errs })); await b.close(); })();
