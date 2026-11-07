# SCRIPT: VOTKP-FILM-RECORD-02  (live recording of each mixer eye, clean view, title and equation overlay; length = its narration)
import asyncio, json, sys, os, shutil
from playwright.async_api import async_playwright
from narration import SEGMENTS
dur=json.load(open('durations.json'))
OV = """(function(t,e,big){ let o=document.getElementById('ov'); if(!o){ o=document.createElement('div'); o.id='ov'; document.body.append(o); }
 o.style.cssText='position:fixed;left:48px;top:40px;max-width:760px;font-family:Inter Tight,system-ui,sans-serif;color:#dfe7ef;pointer-events:none;z-index:9';
 o.innerHTML = big ? '<div style=\"font-size:44px;font-weight:600;letter-spacing:.02em;line-height:1.15\">'+t+'</div><div style=\"margin-top:14px;font-size:20px;color:#8a9aab;white-space:pre-wrap\">'+e+'</div>'
   : '<div style=\"font-size:15px;letter-spacing:.14em;text-transform:uppercase;color:#63d3ff\">'+t+'</div><div style=\"margin-top:8px;font-family:JetBrains Mono,monospace;font-size:19px;color:#f2c14e;white-space:pre-wrap;line-height:1.5\">'+e+'</div>'; })"""
CARDS={'intro':('The Volume of the Knot Potential','Decay and Direction on the Vacuum Disk\n\nJeromie Beasley\n\nVOTKP  ·  doi.org/10.5281/zenodo.24040319'),
       'outro':('VOTKP','Jeromie Beasley\nNarration voice: Kokoro am_michael\ngithub.com/dicipler-pixel/votkp-lean\n\nAtlas Memoriae — Ex memoria lux, ex luce materia\n\nCC | https://doi.org/10.5281/zenodo.24040319')}
async def main(names):
    os.makedirs('rec',exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'])
        for name,eye,_ in SEGMENTS:
            if names and name not in names: continue
            ctx=await b.new_context(viewport={'width':1280,'height':720},record_video_dir='rec/tmp',record_video_size={'width':1280,'height':720})
            pg=await ctx.new_page(); await pg.goto('file:///home/claude/mixer/VOTKP_Mixer_v1.html'); await pg.wait_for_timeout(1200)
            e = eye or ('disk' if name=='intro' else 'self')
            info=await pg.evaluate("id=>{MIXER_API.show(id); MIXER_API.clean(true); const b=document.querySelector('#eyes button.on'); return [b?b.innerText.replace(/^\\d+\\s*/,''):'', document.getElementById('eq').textContent];}", e)
            if eye: await pg.evaluate(OV+"(arguments[0],arguments[1],false)" if False else f"({OV})({json.dumps(info[0])},{json.dumps(info[1])},false)")
            else: await pg.evaluate(f"({OV})({json.dumps(CARDS[name][0])},{json.dumps(CARDS[name][1])},true)")
            await pg.evaluate("document.querySelector('.cleanexit').style.display='none'")
            await pg.wait_for_timeout(int((dur[name]+1.6)*1000))
            v=pg.video; await ctx.close(); src=await v.path(); shutil.move(src,f'rec/{name}.webm'); print('recorded',name,flush=True)
        await b.close()
asyncio.run(main(sys.argv[1:]))
