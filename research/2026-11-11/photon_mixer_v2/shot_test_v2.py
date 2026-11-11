# SCRIPT: PHOTON-MIXER-SHOTS-V2
import asyncio, sys
from playwright.async_api import async_playwright
EYES=sys.argv[2].split(',') if len(sys.argv)>2 else ['core','flight','snell','slits','redshift','photoelectric','resonance','sky']
PFX=sys.argv[3] if len(sys.argv)>3 else 'v2_'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
        pg=await b.new_page(viewport={'width':1280,'height':760})
        errs=[]; pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('console', lambda m: errs.append('console:'+m.text) if m.type=='error' else None)
        await pg.route('**/three.min.js', lambda r: r.fulfill(path='/tmp/three158/node_modules/three/build/three.min.js', content_type='application/javascript'))
        await pg.route('https://fonts.googleapis.com/**', lambda r: r.fulfill(body='', content_type='text/css'))
        await pg.goto('file:///home/claude/work/photon_mixer/'+sys.argv[1]); await pg.wait_for_timeout(1500)
        for e in EYES:
            await pg.evaluate(f"MIXER_API.show('{e}')"); await pg.wait_for_timeout(3000)
            await pg.screenshot(path=f'shots/{PFX}{e}.png')
            rd=await pg.inner_text('#read'); print('==',e,'|',rd.replace('\n',' | ')[:400])
        print('errors:',errs[:10]); await b.close()
asyncio.run(main())
