# SCRIPT: PHOTON-MIXER-SHOTS
import asyncio, sys
from playwright.async_api import async_playwright
EYES=['core','flight','snell','slits','redshift','photoelectric','leaf','sunset']
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
        pg=await b.new_page(viewport={'width':1280,'height':760})
        errs=[]; pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('console', lambda m: errs.append('console:'+m.text) if m.type=='error' else None)
        await pg.route('**/three.min.js', lambda r: r.fulfill(path='/tmp/three158/node_modules/three/build/three.min.js', content_type='application/javascript'))
        await pg.route('https://fonts.googleapis.com/**', lambda r: r.fulfill(body='', content_type='text/css'))
        await pg.goto('file:///home/claude/work/photon_mixer/'+sys.argv[1]); await pg.wait_for_timeout(1500)
        for e in EYES:
            await pg.evaluate(f"MIXER_API.show('{e}')"); await pg.wait_for_timeout(2600 if e!='sunset' else 3500)
            await pg.screenshot(path=f'shots/{e}.png')
            rd=await pg.inner_text('#read'); print('==',e,'|',rd.replace('\n',' | ')[:400])
        await pg.evaluate("MIXER_API.clean(true)"); await pg.wait_for_timeout(800); await pg.screenshot(path='shots/sunset_clean.png')
        await pg.evaluate("MIXER_API.set('elev',20)"); await pg.wait_for_timeout(800); await pg.screenshot(path='shots/sunset_clean_h20.png')
        print('errors:',errs[:10]); await b.close()
asyncio.run(main())
