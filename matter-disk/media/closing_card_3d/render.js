// SCRIPT: CARD3D-RENDER  renders card.html frame by frame to PNGs (deterministic time)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const dir = __dirname;
  const only = process.argv[2] ? process.argv[2].split(',').map(Number) : null;
  const fps = 24, dur = 14.0, n = Math.round(fps * dur);
  const browser = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  // serve via file:// with fetch allowed
  await page.goto('http://127.0.0.1:8765/card.html');
  await page.waitForFunction(() => window.READY === true, null, { timeout: 60000 });
  const frames = only || [...Array(n).keys()];
  for (const f of frames) {
    await page.evaluate(t => window.renderAt(t), f / fps);
    await page.screenshot({ path: path.join(dir, 'frames', `f_${String(f).padStart(4, '0')}.png`) });
  }
  await browser.close();
})();
