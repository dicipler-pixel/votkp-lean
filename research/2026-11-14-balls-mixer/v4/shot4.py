# SCRIPT: BALLS-MIXER-SHOT-04 (headless check of mixer v3: every eye, readouts, screenshots, errors)
import asyncio
from playwright.async_api import async_playwright
SH=[('tree',"MIXER_API.show('tree')"),('k7',"MIXER_API.show('knot')"),('k7t5',"MIXER_API.set('kt',5);MIXER_API.set('ka',180)"),('k7m',"document.querySelector('button[data-m=\"-1\"]').click()"),('k7c2',"MIXER_API.set('kc',2);MIXER_API.set('ka',100)"),('k13',"MIXER_API.set('kc',0);MIXER_API.set('kn',13);MIXER_API.set('kt',1.5)"),
 ('s0',"MIXER_API.show('sum')"),('sK',"document.querySelector('button[data-j=\"1\"]').click()"),('sK5',"MIXER_API.set('sc',5)"),('sB0',"MIXER_API.set('sc',0);document.querySelector('button[data-b=\"1\"]').click()"),('sB2',"MIXER_API.set('sc',2)"),('sB5',"MIXER_API.set('sc',5)")]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'])
        pg=await b.new_page(viewport={'width':1280,'height':760}); errs=[]
        pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None); pg.on('pageerror',lambda e: errs.append(str(e)))
        await pg.goto('file:///home/claude/balls_mixer/Balls_in_One_Ball_Mixer_v4.html'); await pg.wait_for_timeout(2500)
        for name,js in SH:
            await pg.evaluate(js); await pg.wait_for_timeout(1800); await pg.screenshot(path=f'v4check/v4_{name}.png')
            print(name,'::', await pg.evaluate("[...document.querySelectorAll('#read div')].map(d=>d.innerText.replace(/\\n/g,' = ')).join(' | ')"))
        print('ERRORS:',errs[:8]); await b.close()
asyncio.run(main())
