# SCRIPT: RENDER-LEAVE-THE-SIGN-FILM-V3
# Renders the mixer's song-locked film frame by frame (FILM.renderAt), 1920x1080, 30 fps, frames a..b.
import subprocess, sys, time, os
from playwright.sync_api import sync_playwright
html, a, b, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
FPS = 30; tmp = out.replace('.mp4', '.part.mp4')
ff = subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-framerate',str(FPS),'-i','-',
  '-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p',tmp], stdin=subprocess.PIPE)
with sync_playwright() as p:
    br = p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
    pg = br.new_page(viewport={'width':1920,'height':1080})
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + html); pg.wait_for_timeout(3000)
    t0 = time.time()
    for i in range(a, b):
        pg.evaluate(f'FILM.renderAt({i/FPS:.5f})')
        ff.stdin.write(pg.screenshot(type='jpeg', quality=93))
        if (i - a) % 300 == 0: print(f'frame {i} ({i-a}/{b-a})  {time.time()-t0:.0f}s  errors {len(errs)}', flush=True)
    br.close()
ff.stdin.close(); ff.wait()
if ff.returncode == 0: os.replace(tmp, out)
print('done', out, ff.returncode, 'errors', errs[:3], flush=True)
