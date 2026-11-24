# SCRIPT: OTES-SHOT-03  render check for v2.1: every eye in three shapes, no page errors (python3 shot3.py /full/path/One_Tree_Every_Shape_v2_1.html)
import sys
from playwright.sync_api import sync_playwright
f=sys.argv[1]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=swiftshader','--enable-unsafe-swiftshader','--no-sandbox'])
    pg=b.new_page(viewport={'width':1280,'height':800}); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None)
    pg.goto('file://'+f); pg.wait_for_timeout(1500)
    ids=['ride','whole','swCharges','swCusp','wall','faces','bCov','bDig','bZer','bShf','bFlt','bBrd']
    for sh in ['icosahedron','cube','tetrahedron']:
        pg.select_option('#gctl select >> nth=0',sh)
        for i in ids:
            pg.evaluate('(id)=>{for(let k=0;k<25;k++)window.API.frame(0.05,id,null)}',i); pg.wait_for_timeout(150)
            if sh=='icosahedron' and i in ('bZer','bDig'): pg.screenshot(path=f'/tmp/v21_{i}.jpg',type='jpeg',quality=75)
    print('byline',pg.evaluate("document.querySelector('.by').textContent"))
    print('errors',errs); b.close()
