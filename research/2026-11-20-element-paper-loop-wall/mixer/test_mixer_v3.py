# SCRIPT: TEST-ELEMENT-MIXER-V3
import sys, time
from playwright.sync_api import sync_playwright
f = sys.argv[1]; times = [float(x) for x in sys.argv[2].split(',')]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
    pg = b.new_page(viewport={'width':1920,'height':1080})
    errs = []; pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None); pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + f); pg.wait_for_timeout(3000)
    for t in times:
        t0 = time.time(); cue = pg.evaluate(f'FILM.renderAt({t})'); pg.screenshot(path=f'/home/claude/vid/m3_{t:06.1f}.jpg',type='jpeg',quality=90)
        print(f'{t:6.1f} cue {cue} {time.time()-t0:.2f}s')
    print('errors', errs[:8])
