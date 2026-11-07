# SCRIPT: MIXER-SHOT-01  (headless check: open each eye, wait, screenshot, collect console errors)
import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'])
        pg=await b.new_page(viewport={'width':1280,'height':720}); errs=[]
        pg.on('console',lambda m: errs.append(m.text) if m.type in ('error','warning') else None); pg.on('pageerror',lambda e: errs.append(str(e)))
        await pg.goto('file:///home/claude/mixer/VOTKP_Mixer_v1.html'); await pg.wait_for_timeout(2500)
        for eid in sys.argv[1:]:
            await pg.evaluate(f"MIXER_API.show('{eid}')"); await pg.wait_for_timeout(2500)
            await pg.screenshot(path=f'/tmp/eye_{eid}.png')
        print('\n'.join(errs[:10])); await b.close()
asyncio.run(main())
