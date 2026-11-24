# SCRIPT: MOMENT-LADDER-CARD-SHOT-01  render check: no page errors, numbers against MOMENT-LADDER-01, screenshots
import sys
from playwright.sync_api import sync_playwright
f=sys.argv[1]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=swiftshader','--enable-unsafe-swiftshader','--no-sandbox'])
    pg=b.new_page(viewport={'width':1280,'height':900}); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None)
    pg.goto('file://'+f); pg.wait_for_timeout(1800)
    st=pg.evaluate('window.API.state()'); print('y=0:',{k:(round(v,6) if not isinstance(v,dict) else {a:round(b_,4) for a,b_ in v.items()}) for k,v in st.items()})
    pg.evaluate('window.API.still(0.0)')
    el=pg.query_selector('#stage'); el.scroll_into_view_if_needed(); pg.wait_for_timeout(500); el.screenshot(path='/tmp/card_y0.jpg',type='jpeg',quality=80)
    pg.click('#b1'); pg.wait_for_timeout(600); st=pg.evaluate('window.API.state()'); print('tune-out: y',round(st['y'],6),'alpha',round(st['alpha'],9),'Q',st['Q'])
    el.screenshot(path='/tmp/card_tune.jpg',type='jpeg',quality=80)
    pg.evaluate('window.API.set({y:0.5})'); pg.wait_for_timeout(500); print('y=0.5 alpha',round(pg.evaluate('window.API.state().alpha'),6)); el.screenshot(path='/tmp/card_y05.jpg',type='jpeg',quality=80)
    pg.evaluate('window.scrollTo(0,0)'); pg.wait_for_timeout(300); pg.screenshot(path='/tmp/card_top.jpg',type='jpeg',quality=70)
    pg.set_viewport_size({'width':390,'height':800}); pg.wait_for_timeout(600); pg.evaluate('window.scrollTo(0,0)'); pg.screenshot(path='/tmp/card_phone.jpg',type='jpeg',quality=70,full_page=True)
    print('read:',pg.inner_text('#read')[:260]); print('errors',errs); b.close()
