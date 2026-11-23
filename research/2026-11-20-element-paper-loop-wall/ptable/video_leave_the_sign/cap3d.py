# SCRIPT: VIDEO-CAPTURE-3D-03
import asyncio, os, math
from playwright.async_api import async_playwright
F='file:///home/claude/vid/table_capture_copy.html'
async def shoot(pg,sel,folder,n,y0,turn):
    os.makedirs(folder,exist_ok=True)
    el=await pg.query_selector(sel)
    for i in range(n):
        await pg.evaluate(f'window.__Y={y0+turn*i/n}'); await pg.wait_for_timeout(60)
        await el.screenshot(path=f'{folder}/{i:03d}.jpg',type='jpeg',quality=92)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
        pg=await b.new_page(viewport={'width':1920,'height':1080},device_scale_factor=2)
        await pg.goto(F+'#spiral'); await pg.wait_for_timeout(1500)
        await pg.add_style_tag(content='header,nav,.legend{display:none!important}'); await pg.wait_for_timeout(500)
        await shoot(pg,'#v-spiral canvas','cap/spiral3',180,0.5,2*math.pi)
        await pg.evaluate("location.hash='standard'"); await pg.wait_for_timeout(500)
        for z in (6,7,8,79):
            await pg.evaluate(f"openEl({z})"); await pg.wait_for_timeout(1000)
            await shoot(pg,'#chain3d',f'cap/ch{z}',120,0.6,2*math.pi)
            await pg.evaluate("document.getElementById('close').click()"); await pg.wait_for_timeout(300)
        await b.close()
asyncio.run(main())
