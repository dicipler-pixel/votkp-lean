# SCRIPT: BALLS-MIXER-SHOT-01  (headless check: open each eye, apply settings, screenshot, collect errors and readouts)
import asyncio, sys, json
from playwright.async_api import async_playwright
v=sys.argv[1]
SH=[('one',''),('one2',"MIXER_API.show('one');MIXER_API.set('nA',2)"),('two',"MIXER_API.set('nA',1);MIXER_API.show('two')"),('two0',"MIXER_API.show('two');MIXER_API.set('join',0)"),
    ('field',"MIXER_API.set('join',1);MIXER_API.show('field')"),('field0',"MIXER_API.show('field');MIXER_API.set('join',0.3)"),('lattice',''),('mix',"MIXER_API.show('lattice');document.querySelector('button[data-l=mix]').click()"),('tetra',"MIXER_API.show('field');document.querySelector('button[data-c=tetra]').click()"),('loop',''),('loop7',"MIXER_API.show('loop');MIXER_API.set('zL',7)")]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'])
        pg=await b.new_page(viewport={'width':1280,'height':760}); errs=[]
        pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None); pg.on('pageerror',lambda e: errs.append(str(e)))
        await pg.goto('file:///home/claude/balls_mixer/Balls_on_the_Field_Mixer_'+v+'.html'); await pg.wait_for_timeout(2000)
        for name,js in SH:
            if js: await pg.evaluate(js)
            else: await pg.evaluate(f"MIXER_API.show('{name}')")
            await pg.wait_for_timeout(1800); await pg.screenshot(path=f'shot_{name}.png')
            print(name, await pg.evaluate("[...document.querySelectorAll('#read div')].map(d=>d.innerText.replace(/\\n/g,' = ')).join(' | ')"))
        print('ERRORS:',errs[:10]); await b.close()
asyncio.run(main())
