# SCRIPT: LH-PAGE-CHECK-V1
# K14d: with the hypothesis layer hidden, every law readout is bitwise identical to the run with it shown.
# K19: every self-test value computed in the browser equals the node value (relative difference > 1e-12 -> kill).
# K20: no console error in any eye at tau = 0, 7, 40; frame time under 33 ms at default density on the sandbox.
import asyncio, json, os
from playwright.async_api import async_playwright
F = "file://" + os.path.abspath("Light_at_the_Hypersurface_Mixer_v1_20261115.html")
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--use-gl=swiftshader","--enable-unsafe-swiftshader","--ignore-gpu-blocklist"])
        pg = await b.new_page(viewport={"width":1500,"height":900}); errs = []
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None); pg.on("pageerror", lambda e: errs.append("PAGEERROR " + str(e)))
        await pg.goto(F); await pg.wait_for_timeout(2500); out = []
        # K19
        page_vals = await pg.evaluate("()=>window.__lh.selftest().map(x=>({id:x.id,value:x.value}))"); node_vals = json.load(open('lh_selftest_values.json'))
        d = max(abs(a['value'] - b_['value'])/max(1e-300, abs(b_['value'])) if b_['value'] != 0 else abs(a['value']) for a, b_ in zip(page_vals, node_vals))
        same_ids = [a['id'] for a in page_vals] == [b_['id'] for b_ in node_vals]
        out.append(('HOLDS ' if (d <= 1e-12 and same_ids) else 'KILLED') + f'  K19  {d:.2e}  page self-test values against node ({len(page_vals)} lines, same ids: {same_ids})')
        # K14d and K20
        eyes = list("ABCDEFGHIJ"); diffs = []; per = {}
        for tau in [0, 7, 40]:
            for e in eyes:
                n0 = len(errs)
                await pg.evaluate("([e,t])=>{window.__lh.play(false);window.__lh.set('drive','breathe');window.__lh.go(e);window.__lh.setTau(t);window.__lh.hyp(true)}", [e, tau]); await pg.wait_for_timeout(500)
                shown = await pg.evaluate("()=>window.__lh.rows()")
                await pg.evaluate("()=>window.__lh.hyp(false)"); await pg.wait_for_timeout(500)
                hidden = await pg.evaluate("()=>window.__lh.rows()"); await pg.evaluate("()=>window.__lh.hyp(true)")
                if e != 'I' and shown != hidden: diffs.append(f'{e}@{tau}')
                per[f'{e}@{tau}'] = len(errs) - n0
        out.append(('HOLDS ' if not diffs else 'KILLED') + f'  K14d  law readouts identical with the hypothesis layer shown and hidden, eyes A-H and J at tau 0, 7, 40 (differences: {diffs})')
        out.append(('HOLDS ' if not errs else 'KILLED') + f'  K20  console errors in any eye at tau 0, 7, 40: {len(errs)} {errs[:3]}')
        js = await pg.evaluate("()=>window.__lh.bench(60)")
        ft = await pg.evaluate("()=>new Promise(r=>{window.__lh.play(true);let n=0,t0=performance.now();function f(){n++;if(n<90)requestAnimationFrame(f);else r((performance.now()-t0)/90)}requestAnimationFrame(f)})")
        out.append(('HOLDS ' if ft <= 33 else 'KILLED') + f'  K20  frame time {ft:.1f} ms at default density, software WebGL (SwiftShader) at 1500x900; JavaScript share of a frame {js:.1f} ms')
        await b.close(); print('\n'.join(out))
asyncio.run(main())
