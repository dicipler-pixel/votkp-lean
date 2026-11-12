// SCRIPT: shot_iqgt_v5b — explainer page, stage eyes, self-test, errors
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const file = process.argv[2], tag = process.argv[3] || 'd', stageIds = (process.argv[4] || '').split(',').filter(Boolean);
const fsrc = p => 'file://' + path.resolve('node_modules/@fontsource/' + p);
const css = `@font-face{font-family:"Instrument Sans";font-weight:400;src:url(${fsrc('instrument-sans/files/instrument-sans-latin-400-normal.woff2')})}
@font-face{font-family:"Instrument Sans";font-weight:500;src:url(${fsrc('instrument-sans/files/instrument-sans-latin-500-normal.woff2')})}
@font-face{font-family:"Instrument Sans";font-weight:600;src:url(${fsrc('instrument-sans/files/instrument-sans-latin-600-normal.woff2')})}
@font-face{font-family:"STIX Two Text";font-style:normal;src:url(${fsrc('stix-two-text/files/stix-two-text-latin-400-normal.woff2')})}
@font-face{font-family:"STIX Two Text";font-style:italic;src:url(${fsrc('stix-two-text/files/stix-two-text-latin-400-italic.woff2')})}`;
(async () => {
  const b = await chromium.launch({args:['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist','--allow-file-access-from-files']});
  const p = await b.newPage({viewport:{width:1440,height:900}}); const errs = [];
  p.on('pageerror', e => errs.push('PAGEERR ' + e.message)); p.on('console', m => { if(m.type()==='error') errs.push('CONSOLE ' + m.text()); });
  await p.route('https://cdn.jsdelivr.net/npm/three@0.158.0/**', r => { const rel = r.request().url().split('three@0.158.0/')[1]; r.fulfill({body: fs.readFileSync('node_modules/three/' + rel), contentType:'application/javascript'}); });
  await p.route('**fonts.googleapis.com**', r => r.fulfill({body: css, contentType:'text/css'}));
  await p.goto('file://' + path.resolve(file)); await p.waitForTimeout(4000);
  await p.screenshot({path:`${tag}_top.png`});
  const ids = await p.evaluate(() => Object.keys(window.MIXER_API.eyes));
  await p.evaluate(() => { document.getElementById('ex').style.scrollBehavior = 'auto'; });
  for (const id of ids) { await p.evaluate(i => { const ex = document.getElementById('ex'), el = document.getElementById('pn-' + i); ex.scrollTop = el.getBoundingClientRect().top + ex.scrollTop - 130; }, id); await p.waitForTimeout(1600);
    await p.screenshot({path:`${tag}_ex_${id}.png`}); }
  await p.evaluate(() => window.MIXER_API.selfTest()); await p.waitForTimeout(4000);
  console.log('SELFTEST ' + await p.evaluate(() => document.getElementById('sheet_sum').innerText));
  console.log(await p.evaluate(() => [...document.querySelectorAll('#sheet_body tr')].filter(r => r.querySelector('td.no')).map(r => r.innerText.replace(/\t/g,' | ')).join('\n')) || 'no misses');
  await p.screenshot({path:`${tag}_selftest.png`});
  await p.evaluate(() => document.getElementById('sheet').classList.remove('on'));
  for (const id of stageIds) { await p.evaluate(i => window.MIXER_API.setMode('stage', i), id); await p.waitForTimeout(2500); await p.screenshot({path:`${tag}_st_${id}.png`}); }
  console.log(errs.join('\n') || 'no errors'); await b.close();
})();
