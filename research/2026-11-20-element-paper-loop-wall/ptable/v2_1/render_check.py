# SCRIPT: PTABLE-V2-1-RENDER-CHECK
import asyncio, sys
from playwright.async_api import async_playwright
F='file://'+__import__('os').path.abspath('Periodic_Table_of_Elemental_Peels_v2_1_Jeromie_Beasley.html')
VIEWS=['standard','signature','cores','disk','stone','colour','octaves','spiral','heavy','decay','window','faces','corpus','moves','tests','about']
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
        pg=await b.new_page(viewport={'width':1500,'height':1000})
        errs=[]
        pg.on('console',lambda m: errs.append(m.type+': '+m.text) if m.type in('error','warning') else None)
        pg.on('pageerror',lambda e: errs.append('PAGEERROR: '+str(e)))
        await pg.goto(F); await pg.wait_for_timeout(1500)
        for v in VIEWS:
            await pg.evaluate(f"location.hash='{v}'"); await pg.wait_for_timeout(900)
            await pg.screenshot(path=f'shots/{v}.png',full_page=(v not in('spiral',)))
        for z in (6,24,46,47,67,87,103,104,113):
            await pg.evaluate("location.hash='standard'"); await pg.wait_for_timeout(300)
            await pg.evaluate(f"openEl({z})"); await pg.wait_for_timeout(900)
            await pg.screenshot(path=f'shots/drawer_{z}.png')
            await pg.evaluate("document.getElementById('close').click()")
        txt=await pg.evaluate("[document.getElementById('heavynote').textContent,document.getElementById('windownote').textContent,document.getElementById('facenote').textContent,document.getElementById('spiralnote').textContent,document.querySelectorAll('.tile').length]")
        print(txt)
        print('ERRORS:',[e for e in errs if 'deprecated' not in e] or 'none')
        await b.close()
asyncio.run(main())
