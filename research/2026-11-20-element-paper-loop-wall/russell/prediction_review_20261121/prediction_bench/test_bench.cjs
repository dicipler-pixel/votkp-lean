/* Run with Playwright and a locally installed Chromium; CHROMIUM selects its executable. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { chromium } = require('playwright');

async function main() {
  const source = path.resolve(__dirname, 'Prediction_Bench_v1.html');
  const browser = await chromium.launch({
    executablePath: process.env.CHROMIUM || '/usr/bin/chromium',
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--disable-gpu'],
  });
  try {
    const page = await browser.newPage({ viewport: { width: 1280, height: 950 } });
    const errors = [];
    const network = [];
    page.on('pageerror', (error) => errors.push(error.message));
    page.on('request', (request) => {
      if (request.url().startsWith('http')) network.push(request.url());
    });
    await page.goto(pathToFileURL(source).href);
    const expectations = {
      diag: ['Open', 'Closed', 'Closed', 'Closed', '−2.009529'],
      comp: ['Open', 'Closed', 'Open', 'Open', '−2.020493'],
      berb: ['Open', 'Closed', 'Closed', 'Open', '−2.006465'],
      siag: ['Open', 'Closed', 'Closed', 'Open', '−2.016894'],
      null: ['Ideal', 'Closed', 'Closed', 'Ideal', '−2.000000'],
    };
    let comparisons = 0;
    for (const [preset, [native, sum, product, warp, trace]] of Object.entries(expectations)) {
      await page.locator('[data-id="' + preset + '"]').click();
      assert.equal(await page.locator('#nativeCall').innerText(), native);
      assert.equal(await page.locator('#trace').innerText(), trace);
      for (const [rival, expected] of Object.entries({ sum, product, warp })) {
        await page.selectOption('#rival', rival);
        assert.equal(await page.locator('#rivalCall').innerText(), expected);
        assert.equal(await page.locator('#partners tr').count(), 2);
        comparisons++;
      }
    }
    await page.selectOption('#rival', 'sum');
    await page.locator('[data-id="diag"]').click();
    await page.selectOption('#planeZoom', 'full');
    await page.selectOption('#planeZoom', 'local');
    const plane = page.locator('#plane');
    const slice = page.locator('#slice');
    const priorPlane = await page.locator('#planeTip').innerText();
    let rect = await plane.boundingBox();
    await page.mouse.move(rect.x + rect.width * 0.52, rect.y + rect.height * 0.45);
    assert.notEqual(await page.locator('#planeTip').innerText(), priorPlane);
    await plane.focus();
    await page.keyboard.press('ArrowRight');
    await page.keyboard.press('ArrowUp');
    await page.keyboard.press('Enter');
    assert.equal(await page.locator('[aria-pressed="true"]').count(), 0);
    for (const zoom of ['wide', 'interval', 'close']) await page.selectOption('#sliceZoom', zoom);
    await slice.scrollIntoViewIfNeeded();
    rect = await slice.boundingBox();
    await page.mouse.click(rect.x + rect.width * 0.63, rect.y + rect.height * 0.62);
    assert.equal(await page.locator('#a').inputValue(), await page.locator('#b').inputValue());
    await slice.focus();
    const prior = await page.locator('#sliceTip').innerText();
    await page.keyboard.press('ArrowRight');
    assert.notEqual(await page.locator('#sliceTip').innerText(), prior);
    await page.keyboard.press('Enter');

    await page.fill('#a', '1');
    await page.click('#apply');
    assert.ok(await page.locator('#inputError').isVisible());
    await page.fill('#a', '3');
    await page.fill('#b', '13.99');
    await page.locator('#b').press('Enter');
    assert.equal(await page.locator('#rivalCall').innerText(), 'Closed');
    assert.ok(await page.locator('#inputError').isHidden());

    await page.locator('[data-id="diag"]').click();
    if (process.env.BENCH_QA_DIR) {
      await page.evaluate(() => scrollTo(0, 0));
      fs.mkdirSync(process.env.BENCH_QA_DIR, { recursive: true });
      await page.screenshot({
        path: path.join(process.env.BENCH_QA_DIR, 'desktop.png'),
        fullPage: true,
      });
    }
    for (const width of [320, 390, 768, 1024]) {
      await page.setViewportSize({ width, height: 844 });
      await page.waitForTimeout(130);
      const screen = await page.evaluate(() => ({
        viewport: document.documentElement.clientWidth,
        content: document.documentElement.scrollWidth,
        canvases: Array.from(document.querySelectorAll('canvas'), (c) => [c.width, c.height]),
        missingLabels: Array.from(document.querySelectorAll('input,select')).filter(
          (el) =>
            !el.getAttribute('aria-label') && !document.querySelector('label[for="' + el.id + '"]'),
        ).length,
      }));
      assert.equal(screen.viewport, screen.content, 'horizontal overflow at ' + width);
      assert.ok(screen.canvases.every(([w, h]) => w > 200 && h > 180));
      assert.equal(screen.missingLabels, 0);
      if (width === 390 && process.env.BENCH_QA_DIR) {
        await page.screenshot({
          path: path.join(process.env.BENCH_QA_DIR, 'mobile.png'),
          fullPage: true,
        });
      }
    }
    const mobile = await browser.newPage({
      viewport: { width: 390, height: 844 },
      isMobile: true,
      hasTouch: true,
      deviceScaleFactor: 2,
    });
    await mobile.goto(pathToFileURL(source).href);
    await mobile.locator('[data-id="null"]').tap();
    assert.equal(await mobile.locator('#nativeCall').innerText(), 'Ideal');
    await mobile.locator('#slice').tap();
    assert.equal(await mobile.locator('#a').inputValue(), await mobile.locator('#b').inputValue());
    assert.equal(await mobile.locator('[aria-pressed="true"]').count(), 0);
    await mobile.close();
    assert.equal(errors.length, 0);
    assert.equal(network.length, 0);
    console.log(
      'PASS: 5 presets, ' +
        comparisons +
        ' rival comparisons, 5 exact/archived return traces, 5 zoom settings.',
    );
    console.log(
      'PASS: mobile tap, pointer inspection/click and keyboard commit on plots; invalid manual entry and recovery.',
    );
    console.log(
      'PASS: 320, 390, 768, 1024, 1280 px layouts, labelled inputs, zero page exceptions or network requests.',
    );
  } finally {
    await browser.close();
  }
}
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
