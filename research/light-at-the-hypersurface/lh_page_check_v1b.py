# SCRIPT: LH-PAGE-CHECK-V1b — re-run of K14d (killed once at D, tau 7, not reproducible on three repeats) with 1200 ms waits and three repeats per eye;
# and a reference frame time for Balls in One Ball Mixer v2 on the same sandbox, to separate software rendering from this page's own cost.
import asyncio, os
from playwright.async_api import async_playwright
async def ft(pg): return await pg.evaluate("()=>new Promise(r=>{let n=0,t0=performance.now();function f(){n++;if(n<90)requestAnimationFrame(f);else r((performance.now()-t0)/90)}requestAnimationFrame(f)})")
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--use-gl=swiftshader","--enable-unsafe-swiftshader","--ignore-gpu-blocklist"])
        pg = await b.new_page(viewport={"width":1500,"height":900})
        await pg.goto("file://"+os.path.abspath("Light_at_the_Hypersurface_Mixer_v1_20261115.html")); await pg.wait_for_timeout(2500); diffs = []
        for rep in range(3):
            for tau in [0,7,40]:
                for e in "ABCDEFGHJ":
                    await pg.evaluate("([e,t])=>{window.__lh.play(false);window.__lh.set('drive','breathe');window.__lh.go(e);window.__lh.setTau(t);window.__lh.hyp(true)}", [e,tau]); await pg.wait_for_timeout(1200)
                    s = await pg.evaluate("()=>window.__lh.rows()"); await pg.evaluate("()=>window.__lh.hyp(false)"); await pg.wait_for_timeout(1200); h = await pg.evaluate("()=>window.__lh.rows()")
                    if s != h: diffs.append(f'{e}@{tau}#{rep}')
        print(('HOLDS ' if not diffs else 'KILLED') + f'  K14d  re-run, 3 repeats x 9 eyes x 3 clock values, waits 1200 ms: differences {diffs}')
        q = await b.new_page(viewport={"width":1500,"height":900}); await q.goto("file://"+os.path.abspath("balls_v2_ref.html")); await q.wait_for_timeout(2500)
        print(f'reference  Balls in One Ball Mixer v2, same sandbox and size: frame time {await ft(q):.1f} ms')
        await b.close()
asyncio.run(main())
