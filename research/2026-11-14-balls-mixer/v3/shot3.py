# SCRIPT: BALLS-MIXER-SHOT-03 (headless check of mixer v3: every eye, readouts, screenshots, errors)
import asyncio
from playwright.async_api import async_playwright
SH=[('field',"MIXER_API.show('field')"),('pair',"MIXER_API.show('pair')"),('close',"MIXER_API.show('close')"),
 ('tree5',"MIXER_API.show('tree')"),('tree5i',"document.querySelector('button[data-s=\"0\"]').click()"),('tree7k',"MIXER_API.set('zt',7);document.querySelector('button[data-s=\"2\"]').click()"),
 ('th35',"MIXER_API.show('thomas')"),('th55',"MIXER_API.set('zI',5)"),('th55r',"document.querySelector('button[data-o=\"1\"]').click()"),('th57',"MIXER_API.set('zJ',7)"),
 ('ln5',"MIXER_API.show('line')"),('ln3',"MIXER_API.set('zl',3)"),('ln55',"MIXER_API.set('zl',5.5)"),('lnL',"document.querySelector('button[data-l=\"3\"]').click()"),('ln7',"MIXER_API.set('zl',7)"),
 ('ch400',"MIXER_API.show('chain')"),('ch10',"MIXER_API.set('nc',10)"),('ch100',"MIXER_API.set('nc',100)"),('ch1000',"MIXER_API.set('nc',1000)"),('ch2400',"MIXER_API.set('nc',2400)")]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'])
        pg=await b.new_page(viewport={'width':1280,'height':760}); errs=[]
        pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None); pg.on('pageerror',lambda e: errs.append(str(e)))
        await pg.goto('file:///home/claude/balls_mixer/Balls_in_One_Ball_Mixer_v3.html'); await pg.wait_for_timeout(2500)
        for name,js in SH:
            await pg.evaluate(js); await pg.wait_for_timeout(1800); await pg.screenshot(path=f'v3check/v3_{name}.png')
            print(name,'::', await pg.evaluate("[...document.querySelectorAll('#read div')].map(d=>d.innerText.replace(/\\n/g,' = ')).join(' | ')"))
        print('ERRORS:',errs[:8]); await b.close()
asyncio.run(main())
