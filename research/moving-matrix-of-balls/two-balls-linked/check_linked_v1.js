// SCRIPT: LINKED-CHECK-V1 — the linked page (both balls, one clock/camera/kick), eyes on together, own timing, zoom; screenshots
const { chromium } = require('playwright');
(async () => { const b = await chromium.launch({ args:['--use-gl=swiftshader','--enable-unsafe-swiftshader'] }); const out = {};
  const p = await b.newPage({ viewport:{ width:1600, height:900 } }); const errs = []; p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if(m.type() === 'error') errs.push(m.text()); });
  await p.goto('file://' + process.cwd() + '/Two_Balls_Linked_v1_20261115.html'); await p.waitForTimeout(7000);
  out.ready = await p.evaluate(() => ({ mixer:__link.ready('mixer'), white:__link.ready('white') }));
  await p.screenshot({ path:'shots3/linked_mixer.png' });
  // eyes on together + own timing in the mixer ball
  out.eyes = await p.evaluate(() => { const d = __link.W('mixer').document; d.querySelector('#tb_eyes button[data-eye="C"]').click(); d.querySelector('#tb_eyes button[data-eye="G"]').click(); d.querySelector('#tb_eyes button[data-eye="H"]').click(); return [...__link.W('mixer').__tb.ON]; });
  await p.waitForTimeout(2500); out.weights = await p.evaluate(() => { const h = __link.W('mixer').__TBHOST; return { rays:h.WT.rays, loop:h.WT.loop, rimf:h.WT.rimf, cur:h.cur() }; });
  out.more = await p.evaluate(() => __link.W('mixer').document.getElementById('tb_more').innerText.slice(0, 400)); await p.screenshot({ path:'shots3/linked_mixer_eyes_CGH.png' });
  // white ball: the clock, steps and camera were carried
  await p.evaluate(() => __link.set('white')); await p.waitForTimeout(3000);
  out.white = await p.evaluate(() => { const m = __link.W('mixer'), w = __link.W('white'); return { tauM:m.__lh.CLOCK.tau, tauW:w.__LHS.CLOCK.tau, rM:m.__lh.S.r, rW:w.__LHS.state.S.r, yawM:m.__S3.view.yaw, yawW:w.__LHS.S3.view.yaw }; });
  await p.screenshot({ path:'shots3/linked_white.png' });
  // both as one
  await p.evaluate(() => __link.set('both')); await p.waitForTimeout(5000);
  out.both = await p.evaluate(() => { const m = __link.W('mixer'), w = __link.W('white'); return { dtau:m.__lh.CLOCK.tau - w.__LHS.CLOCK.tau, dr:m.__lh.S.r.map((x,i) => x - w.__LHS.state.S.r[i]), dyaw:m.__S3.view.yaw - w.__LHS.S3.view.yaw, srcM:m.__tb.X.src, srcW:w.__tb.X.src, shareM:m.__tb.HO.share, shareW:w.__tb.HO.share }; });
  await p.screenshot({ path:'shots3/linked_both_three.png' });
  await p.evaluate(() => document.querySelector('#bar button[data-zoom="1"]').click()); await p.waitForTimeout(2500); await p.screenshot({ path:'shots3/linked_both_one.png' });
  await p.evaluate(() => { document.querySelector('#bar button[data-zoom="3"]').click(); document.querySelector('#bar button[data-kick="2"]').click(); }); await p.waitForTimeout(2500);
  out.kickC = await p.evaluate(() => ({ m:__link.W('mixer').__tb.X.src, w:__link.W('white').__tb.X.src }));
  out.fps = await p.evaluate(() => new Promise(r => { let n = 0; const t = performance.now(); (function f(){ n++; if(performance.now() - t < 2000) requestAnimationFrame(f); else r(n/2); })(); }));
  out.errs = errs; require('fs').writeFileSync('check_linked_v1.out.json', JSON.stringify(out, null, 1)); console.log(JSON.stringify(out, null, 1)); await b.close(); })();
