// SCRIPT: shot_iqgt_v5_phone — phone width, then the app's sandboxed preview frame
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const file = process.argv[2];
(async () => {
  const b = await chromium.launch({args:['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist','--allow-file-access-from-files']});
  const route = async p => { await p.route('https://cdn.jsdelivr.net/npm/three@0.158.0/**', r => { const rel = r.request().url().split('three@0.158.0/')[1]; r.fulfill({body: fs.readFileSync('node_modules/three/' + rel), contentType:'application/javascript', headers:{'access-control-allow-origin':'*'}}); });
    await p.route('**fonts.googleapis.com**', r => r.fulfill({body:'', contentType:'text/css'})); };
  const p = await b.newPage({viewport:{width:390,height:844}, deviceScaleFactor:2}); const errs = [];
  p.on('pageerror', e => errs.push('PAGEERR ' + e.message)); await route(p);
  await p.goto('file://' + path.resolve(file)); await p.waitForTimeout(4000); await p.screenshot({path:'ph_top.png'});
  await p.evaluate(() => { document.getElementById('ex').style.scrollBehavior = 'auto'; });
  for (const id of ['crew','ridge','split','ring']) { await p.evaluate(i => { const ex = document.getElementById('ex'), el = document.getElementById('pn-' + i); ex.scrollTop = el.getBoundingClientRect().top + ex.scrollTop - 110; }, id); await p.waitForTimeout(1500); await p.screenshot({path:`ph_ex_${id}.png`}); }
  await p.evaluate(() => window.MIXER_API.setMode('stage', 'ridge')); await p.waitForTimeout(2500); await p.screenshot({path:'ph_st_ridge.png'});
  console.log('phone overflow', await p.evaluate(() => document.documentElement.scrollWidth > window.innerWidth));
  const q = await b.newPage({viewport:{width:1200,height:800}}); q.on('pageerror', e => errs.push('SRCDOC ' + e.message)); await route(q);
  await q.route('https://host.test/', r => r.fulfill({contentType:'text/html', body:'<!doctype html><body style="margin:0;background:#fff"><iframe id="f" sandbox="allow-scripts" style="width:0;height:0;border:0"></iframe></body>'}));
  await q.goto('https://host.test/'); await q.evaluate(h => { document.getElementById('f').srcdoc = h; }, fs.readFileSync(file, 'utf8'));
  await q.waitForTimeout(2500); await q.evaluate(() => { const f = document.getElementById('f'); f.style.width = '560px'; f.style.height = '780px'; }); await q.waitForTimeout(5000);
  await q.screenshot({path:'sd_panel.png', clip:{x:0,y:0,width:560,height:780}});
  console.log(errs.join('\n') || 'no errors'); await b.close();
})();
