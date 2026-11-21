# SCRIPT: TEST-ELEMENT-MIXER-V2
import sys, time
from playwright.sync_api import sync_playwright
f = sys.argv[1]; times = [float(x) for x in sys.argv[2].split(',')]
with sync_playwright() as p:
    b = p.chromium.launch(args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist','--autoplay-policy=no-user-gesture-required'])
    pg = b.new_page(viewport={'width':1920,'height':1080})
    errs = []; pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None); pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + f); pg.wait_for_timeout(2500)
    print('errors after load', errs)
    for t in times:
        t0 = time.time(); cue = pg.evaluate(f'FILM.renderAt({t})'); pg.wait_for_timeout(60)
        pg.screenshot(path=f'/home/claude/vid/s_{int(t):03d}.png'); rd = pg.inner_text('#read').replace('\n', ' ; ')
        print(f'{t:6.1f} cue {cue} {time.time()-t0:.2f}s | {rd[:260]}')
    print('errors', errs[:8])
