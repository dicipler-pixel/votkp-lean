# SCRIPT: VIDEO-CAPTURE-01
import asyncio, json, os
from playwright.async_api import async_playwright
F='file:///home/claude/votkp-lean/research/2026-11-20-element-paper-loop-wall/ptable/v2_1/Periodic_Table_of_Elemental_Peels_v2_1_Jeromie_Beasley.html'
VIEWS=['standard','signature','cores','disk','stone','colour','octaves','heavy','decay','window','faces','moves']
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
        pg=await b.new_page(viewport={'width':1920,'height':1080},device_scale_factor=2)
        await pg.goto(F); await pg.wait_for_timeout(1500)
        # hide header and nav so the content fills the frame
        await pg.add_style_tag(content='header,nav,.legend{display:none!important} main{padding-top:24px!important}')
        meta={}
        for v in VIEWS:
            await pg.evaluate(f"location.hash='{v}'"); await pg.wait_for_timeout(800)
            el=await pg.query_selector(f'#v-{v}')
            await el.screenshot(path=f'cap/{v}.jpg',type='jpeg',quality=92)
            meta[v]=await el.bounding_box()
        # tile rectangles in the standard view, relative to the section
        await pg.evaluate("location.hash='standard'"); await pg.wait_for_timeout(500)
        meta['tiles']=await pg.evaluate("""(()=>{const s=document.getElementById('v-standard').getBoundingClientRect();const o={};document.querySelectorAll('#v-standard .tile').forEach(t=>{const r=t.getBoundingClientRect();o[t.dataset.z]=[r.x-s.x,r.y-s.y,r.width,r.height];});return o;})()""")
        # point positions in stone, faces, octaves views (svg circles with titles)
        for v in ['stone','faces','octaves','window','cores']:
            await pg.evaluate(f"location.hash='{v}'"); await pg.wait_for_timeout(500)
            meta['pts_'+v]=await pg.evaluate(f"""(()=>{{const s=document.getElementById('v-{v}').getBoundingClientRect();const o=[];document.querySelectorAll('#v-{v} circle').forEach(c=>{{const t=c.querySelector('title');if(!t)return;const r=c.getBoundingClientRect();o.push([t.textContent.slice(0,40),r.x+r.width/2-s.x,r.y+r.height/2-s.y]);}});return o;}})()""")
        # spiral: rotating frames
        await pg.evaluate("location.hash='spiral'"); await pg.wait_for_timeout(1500)
        el=await pg.query_selector('#v-spiral canvas')
        os.makedirs('cap/spiral',exist_ok=True)
        for i in range(70):
            await el.screenshot(path=f'cap/spiral/{i:03d}.jpg',type='jpeg',quality=92)
        # drawers with the 3D chain
        await pg.evaluate("location.hash='standard'")
        for z in (6,7,8,79):
            await pg.evaluate(f"openEl({z})"); await pg.wait_for_timeout(1200)
            d=await pg.query_selector('#drawer'); os.makedirs(f'cap/dr{z}',exist_ok=True)
            await d.screenshot(path=f'cap/drawer_{z}.jpg',type='jpeg',quality=92)
            cv=await pg.query_selector('#chain3d')
            for i in range(40):
                await cv.screenshot(path=f'cap/dr{z}/{i:03d}.jpg',type='jpeg',quality=92)
            await pg.evaluate("document.getElementById('close').click()"); await pg.wait_for_timeout(400)
        json.dump(meta,open('cap/meta.json','w'))
        await b.close()
asyncio.run(main())
