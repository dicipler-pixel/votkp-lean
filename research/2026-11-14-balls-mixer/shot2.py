# SCRIPT: BALLS-MIXER-SHOT-02 (headless check of mixer v2: each eye, several settings, screenshots, readouts, errors)
import asyncio
from playwright.async_api import async_playwright
SH=[('f357',"MIXER_API.show('field')"),('f555',"MIXER_API.set('zI',5);MIXER_API.set('zJ',5);MIXER_API.set('zK',5)"),
 ('p55',"MIXER_API.show('pair')"),('p55rev',"document.querySelector('button[data-d=\"0\"]').click()"),
 ('p57',"document.querySelector('button[data-d=\"0\"]').click();MIXER_API.set('zJ',7)"),('p77',"MIXER_API.set('zI',7)"),
 ('p35',"MIXER_API.set('zI',3);MIXER_API.set('zJ',5)"),('c5',"MIXER_API.show('close')"),('cz5',"MIXER_API.set('zq',5)"),('cz7',"MIXER_API.set('zq',7)"),('c6',"MIXER_API.set('zq',3.7320508076)")]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'])
        pg=await b.new_page(viewport={'width':1280,'height':760}); errs=[]
        pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None); pg.on('pageerror',lambda e: errs.append(str(e)))
        await pg.goto('file:///home/claude/balls_mixer/Balls_in_One_Ball_Mixer_v2.html'); await pg.wait_for_timeout(2000)
        for name,js in SH:
            await pg.evaluate(js); await pg.wait_for_timeout(1700); await pg.screenshot(path=f'v2_{name}.png')
            print(name,'::', await pg.evaluate("[...document.querySelectorAll('#read div')].map(d=>d.innerText.replace(/\\n/g,' = ')).join(' | ')"))
        print('ERRORS:',errs[:8]); await b.close()
asyncio.run(main())
