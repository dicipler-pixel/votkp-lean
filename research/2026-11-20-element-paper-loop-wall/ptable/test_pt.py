# SCRIPT: TEST-PERIODIC-TABLE-V1
from playwright.sync_api import sync_playwright
three=open('/home/claude/mixer/package/build/three.min.js').read()
with sync_playwright() as p:
    b=p.chromium.launch(args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist']); pg=b.new_page(viewport={'width':1600,'height':1000})
    errs=[]; pg.on('pageerror',lambda e: errs.append(str(e))); pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None)
    pg.route('**/three.min.js',lambda r: r.fulfill(body=three,content_type='application/javascript'))
    pg.route('**/fonts.googleapis.com/**',lambda r: r.fulfill(body='',content_type='text/css'))
    for v in ['standard','signature','cores','disk','stone','colour','octaves','tests','about']:
        pg.goto(f'http://localhost:8765/index.html#{v}'); pg.wait_for_timeout(900); pg.screenshot(path=f'pt_{v}.png',full_page=(v in ('signature','standard')))
    pg.goto('http://localhost:8765/index.html#standard'); pg.wait_for_timeout(800)
    pg.click('.tile[data-z="8"]'); pg.wait_for_timeout(1200); pg.screenshot(path='pt_oxygen.png')
    print('tiles', pg.locator('#grid .tile').count()+pg.locator('#grid-f .tile').count(), 'errors', errs[:5])
