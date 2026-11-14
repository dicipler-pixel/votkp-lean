# SCRIPT: BALLFILM-RECORD-01 (live recording of each eye of Balls in One Ball Mixer v3 with its real sliders and readouts on screen; actions timed to the narration beats)
import asyncio, json, sys, os, shutil, time
from playwright.async_api import async_playwright
from narration import SEGMENTS
T=json.load(open('times.json'))
STEP={'zI':(0.01,70),'zJ':(0.01,70),'zK':(0.01,70),'np':(1,90),'zq':(0.01,420),'zt':(0.01,260),'zl':(0.001,90),'nc':(1,90)}
CSS="""#eyes,#what,.by,#panel>.row,#panel>.ctl:not(#ctl),.filmbar,.hint,.cleanexit{display:none!important}
#read div{line-height:1.3!important} .ctl label{margin-top:5px!important}
.panel{width:350px!important;max-height:700px!important;overflow:hidden!important} #eq{font-size:12.5px!important} #read{font-size:12px!important} #tag{font-size:10.5px!important}
#card{position:fixed;left:44px;top:70px;width:470px;color:#dfe7ef;font-family:"Inter Tight",system-ui,sans-serif;pointer-events:none;z-index:9}
#card h2{font-family:"Chakra Petch","Segoe UI",system-ui,sans-serif;font-size:40px;font-weight:600;letter-spacing:.03em;line-height:1.12;margin:0 0 16px;text-transform:uppercase}
#card div{font-size:17px;color:#8a9aab;line-height:1.55;white-space:pre-wrap} #card b{color:#f2c14e;font-weight:500} #card i{color:#63d3ff;font-style:normal}"""
CARDS={'intro':("Balls in One Ball","<i>Mixer v3 · seven eyes</i>\n\nJeromie Beasley\n\nOne tree of peel steps in one hyperbolic ball\n<b>Γ = (z − 1)/(z + 1)     step length ln z</b>\n\nBuilt on Two Trees in One Ball\ndoi.org/10.5281/zenodo.23847114"),
 'outro':("Balls in One Ball","Jeromie Beasley\nNarration voice: Kokoro am_michael\ngithub.com/dicipler-pixel/votkp-lean\n\n<i>Atlas Memoriae</i>\nEx memoria lux, ex luce materia\n\nAI-assisted\n\n<b>CC | https://doi.org/10.5281/zenodo.23847114</b>")}
RUN="""(acts)=>{ const t0=performance.now(), done=new Set(), last={};
 function tick(){ const t=(performance.now()-t0)/1000;
  acts.forEach((a,i)=>{ if(a.k==='tw'){ if(t>=a.t0 && !done.has(i)){ const u=Math.min(1,(t-a.t0)/(a.t1-a.t0)), e=u*u*(3-2*u); let v=+(Math.round((a.v0+(a.v1-a.v0)*e)/a.step)*a.step).toFixed(4);
      if(u>=1){ done.add(i); v=a.v1; } const now=performance.now(); if(u>=1 || !(last[a.p] && now-last[a.p]<a.thr)){ if(MIXER_API.P[a.p]!==v) MIXER_API.set(a.p,v); last[a.p]=now; } } }
    else if(!done.has(i) && t>=a.t){ done.add(i); if(a.k==='js') (0,eval)(a.c); else { const b=document.querySelector(a.c); if(b) b.click(); } } });
  requestAnimationFrame(tick); } tick(); }"""
def acts_of(name,beats):
    out=[]
    for (text,acts,cues),(t0,d) in zip(beats,T[name]['marks']):
        for a in acts:
            if a[0]=='tw': st,thr=STEP[a[1]]; out.append(dict(k='tw',p=a[1],v0=a[2],v1=a[3],t0=t0+a[4]*d,t1=t0+a[5]*d,step=st,thr=thr))
            else: out.append(dict(k=a[0],c=a[1],t=t0+a[2]*d))
    return out
async def main(names):
    os.makedirs('rec',exist_ok=True); lead=json.load(open('lead.json')) if os.path.exists('lead.json') else {}
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'])
        for name,eye,beats in SEGMENTS:
            if names and name not in names: continue
            ctx=await b.new_context(viewport={'width':1280,'height':720},record_video_dir='rec/tmp',record_video_size={'width':1280,'height':720})
            pg=await ctx.new_page(); tc=time.time(); errs=[]; pg.on('pageerror',lambda e: errs.append(str(e)))
            await pg.goto('file:///home/claude/balls_mixer/Balls_in_One_Ball_Mixer_v3.html'); await pg.wait_for_timeout(1500)
            await pg.add_style_tag(content=CSS); await pg.evaluate("id=>MIXER_API.show(id)", eye)
            if name in CARDS:
                await pg.evaluate("c=>{document.getElementById('panel').style.visibility='hidden'; const d=document.createElement('div'); d.id='card'; d.innerHTML='<h2>'+c[0]+'</h2><div>'+c[1]+'</div>'; document.body.append(d);}", list(CARDS[name]))
            await pg.wait_for_timeout(700)
            lead[name]=time.time()-tc; await pg.evaluate(RUN, acts_of(name,beats))
            await pg.wait_for_timeout(int((T[name]['total']+0.9)*1000))
            v=pg.video; await ctx.close(); src=await v.path(); shutil.move(src,f'rec/{name}.webm'); print('recorded',name,round(lead[name],2),errs[:2],flush=True)
            json.dump(lead,open('lead.json','w'))
        await b.close()
asyncio.run(main(sys.argv[1:]))
