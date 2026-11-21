from playwright.sync_api import sync_playwright
import sys
f=sys.argv[1]
with sync_playwright() as p:
    b=p.chromium.launch(args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist']); pg=b.new_page(viewport={'width':1280,'height':760})
    errs=[]; pg.on('console',lambda m: errs.append(m.text) if m.type in ('error',) else None); pg.on('pageerror',lambda e: errs.append(str(e)))
    pg.goto('file://'+f); pg.wait_for_timeout(1500)
    for eid in ['ladder','wall','map','chem','screen','reach','screw','loop3','russell']:
        pg.evaluate(f"MIXER_API.show('{eid}')"); pg.wait_for_timeout(900)
        rd=pg.inner_text('#read'); pg.screenshot(path=f'/tmp/mx_{eid}.png'); print('==',eid,'|',rd.replace('\n',' ; ')[:300])
    pg.evaluate("MIXER_API.show('screw')"); pg.evaluate("MIXER_API.set('mirror',1)"); pg.wait_for_timeout(500); print('mirror', pg.inner_text('#read').replace('\n',' ; '))
    pg.evaluate("MIXER_API.set('mirror',0)"); pg.evaluate("MIXER_API.set('rev',1)"); pg.wait_for_timeout(500); print('rev', pg.inner_text('#read').replace('\n',' ; '))
    pg.evaluate("MIXER_API.set('crystal',1)"); pg.wait_for_timeout(500); print('Te', pg.inner_text('#read').replace('\n',' ; '))
    print('errors',errs[:5])
