# SCRIPT: LH-SHOT-V1
import asyncio, json, sys, time
from playwright.async_api import async_playwright
F = "file://" + __import__('os').path.abspath("Light_at_the_Hypersurface_Mixer_v1_20261115.html")
EYES = sys.argv[1].split(',') if len(sys.argv) > 1 else list("ABCDEFGHIJ")
TAUS = [float(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else [7.0]
DRIVE = sys.argv[3] if len(sys.argv) > 3 else 'breathe'
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--use-gl=swiftshader","--enable-unsafe-swiftshader","--ignore-gpu-blocklist"])
        pg = await b.new_page(viewport={"width":1500,"height":900}); errs = []
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None); pg.on("pageerror", lambda e: errs.append("PAGEERROR " + str(e)))
        await pg.goto(F); await pg.wait_for_timeout(2500)
        out = {}
        for tau in TAUS:
            for e in EYES:
                await pg.evaluate("([e,t,d])=>{window.__lh.play(false);window.__lh.set('drive',d);window.__lh.go(e);window.__lh.setTau(t)}", [e, tau, DRIVE])
                await pg.wait_for_timeout(1400)
                out[f"{e}@{tau}"] = await pg.evaluate("()=>window.__lh.rows()")
                await pg.screenshot(path=f"shot_{e}_{str(tau).replace('.','p')}_{DRIVE}.png")
        ft = await pg.evaluate("()=>new Promise(r=>{window.__lh.play(true);let n=0,t0=performance.now();function f(){n++;if(n<60)requestAnimationFrame(f);else r((performance.now()-t0)/60)}requestAnimationFrame(f)})")
        print(json.dumps(out, indent=1, ensure_ascii=False)); print("FRAME_MS", ft); print("ERRORS", errs)
        await b.close()
asyncio.run(main())
