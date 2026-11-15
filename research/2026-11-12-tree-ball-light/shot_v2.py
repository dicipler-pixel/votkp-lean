# SCRIPT: MIXER-V2-RUNTIME-01
# WHY: the page must run without script errors and each view's readout must show the checked numbers.
# KILL LINE: any console error or page error; z=5 readouts not showing rho 0.70711, K 9.0000, sin2phi 0.88889.
import asyncio, json, sys
from playwright.async_api import async_playwright
F="file:///home/claude/mixer_v2/Tree_Ball_Light_Mixer_v2_20261112.html"
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(channel="chrome",args=["--use-gl=swiftshader","--enable-unsafe-swiftshader","--ignore-gpu-blocklist"])
        pg=await b.new_page(viewport={"width":1500,"height":900}); errs=[]
        pg.on("console",lambda m: errs.append(m.text) if m.type=="error" else None); pg.on("pageerror",lambda e: errs.append("PAGEERROR "+str(e)))
        await pg.goto(F); await pg.wait_for_timeout(1500)
        res={}
        for eye,z in [("wall",5),("wall",3),("wall",5.8284271247),("wall",8),("light",5),("light",8),("pressure",5),("pressure",3),("response",5),("end",5),("particles",5),("higgs",5)]:
            await pg.evaluate("([e,z])=>{window.__sm.setZ(z);window.__sm.go(e)}",[eye,z]); await pg.wait_for_timeout(900)
            if eye=="light": await pg.evaluate("()=>{document.getElementById('time').value=3.3;document.getElementById('time').dispatchEvent(new Event('input'))}"); await pg.wait_for_timeout(300)
            res[f"{eye}@{z}"]=await pg.evaluate("()=>window.__lightState().readout")
            await pg.screenshot(path=f"shot_{eye}_{str(z).replace('.','p')}.png")
        for d in ["i","d","f"]:
            await pg.evaluate("([d])=>{window.__sm.setZ(5);window.__sm.go('light');document.querySelector('#pd button[data-d='+d+']').click()}",[d]); await pg.wait_for_timeout(500)
            res["light dir "+d]=await pg.evaluate("()=>window.__lightState().readout")
        print(json.dumps(res,indent=1,ensure_ascii=False)); print("ERRORS",errs)
        await b.close()
asyncio.run(main())
