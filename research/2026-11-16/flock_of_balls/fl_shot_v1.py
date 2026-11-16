# SCRIPT: FL-SHOT-V1 — opens a built page headless (software WebGL), runs steps, prints the layer's own readouts and page errors, saves screenshots.
import asyncio, sys, json
from playwright.async_api import async_playwright
async def main():
    page, pfx = sys.argv[1], sys.argv[2]
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
        pg = await b.new_page(viewport={'width':1600,'height':900}); errs = []
        pg.on('pageerror', lambda e: errs.append('ERR '+str(e)[:300])); pg.on('console', lambda m: errs.append(m.text[:200]) if m.type == 'error' else None)
        await pg.route('https://fonts.googleapis.com/**', lambda r: r.fulfill(body='', content_type='text/css'))
        await pg.goto('file://'+page); await pg.wait_for_timeout(6000)
        async def shot(name, js=None, wait=5000):
            if js: await pg.evaluate(js)
            await pg.wait_for_timeout(wait); await pg.screenshot(path=f'shots/{pfx}{name}.png')
            r = await pg.evaluate("(() => { const F = window.__FL; if(!F) return null; const b = F.books(); return { N:F.W.N, t:F.St.t, total:b.total, balls:b.balls, gaps:b.gaps, r:F.order().r, arrive:F.arrive(), zoom:F.X.zoom, st:document.getElementById('fl_st').textContent }; })()")
            print(name, json.dumps(r))
        await shot('n4')
        await shot('n7', "document.querySelector('#fl button[data-n=\"7\"]').click()", 9000)
        await shot('n7_goB', "window.__FL.goTo(1)", 4000)
        await shot('n3_numbers', "document.querySelector('#fl button[data-n=\"3\"]').click(); document.getElementById('fl_numb').click()", 7000)
        await shot('n4_sync_pan', "document.getElementById('fl_numb').click(); document.querySelector('#fl button[data-n=\"4\"]').click(); document.querySelector('#fl button[data-view=\"sync\"]').click(); window.__FL.setZoom(160); window.__FL.panBy(2,1)", 6000)
        print('errors:', errs[:8]); await b.close()
asyncio.run(main())
