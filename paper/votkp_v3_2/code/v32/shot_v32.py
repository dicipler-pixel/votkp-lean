# SCRIPT: SHOT-V31-01  (render check of the new sections; screenshots are for checking only)
import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        pg = await b.new_page(viewport={'width': 1500, 'height': 1000})
        await pg.route('**/mathjax@3/es5/**', lambda r: r.fulfill(path='/home/claude/build/node_modules/mathjax/es5/' + r.request.url.split('/es5/')[1].split('?')[0]))
        await pg.goto('file:///home/claude/build32/VOTKP_ELEMENTAL_PEELING_PAPER_v3_2_20261112.html', wait_until='load', timeout=180000)
        await pg.wait_for_timeout(9000)
        print('math errors:', await pg.evaluate("document.querySelectorAll('mjx-merror').length"), 'containers:', await pg.evaluate("document.querySelectorAll('mjx-container').length"),
              'figures:', await pg.evaluate("document.querySelectorAll('figure').length"), 'overflow:', await pg.evaluate("document.body.scrollWidth>window.innerWidth+4"))
        print('raw tex left:', await pg.evaluate("(document.querySelector('main')||document.body).innerText.split(String.fromCharCode(92)+'[').length-1"), await pg.evaluate("(document.body.innerText.match(/operatorname|tfrac|lvert/g)||[]).length"))
        for i, sel in enumerate(['#bounds-on-the-weight-between', '#the-loop', '#the-loop-drives-the-signal', '#the-exit-line', '#where-the-atlas-holds-the-parts']):
            await pg.evaluate("s => document.querySelector(s).scrollIntoView()", sel); await pg.wait_for_timeout(700); await pg.screenshot(path='s32_%d.png' % i)
        await b.close()
asyncio.run(main())
