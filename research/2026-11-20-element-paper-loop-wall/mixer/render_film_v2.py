# SCRIPT: RENDER-LOOP-WALL-FILM-V2
# Renders the mixer's song-locked film frame by frame (FILM.renderAt) at 1920x1080, 24 fps, and muxes the song.
import subprocess, sys, time
from playwright.sync_api import sync_playwright
html, mp3, out = sys.argv[1], sys.argv[2], sys.argv[3]
FPS, SONG = 24, 273.24; N = int(SONG*FPS)
ff = subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-framerate',str(FPS),'-i','-','-i',mp3,
  '-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p','-c:a','aac','-b:a','256k','-shortest','-movflags','+faststart',out], stdin=subprocess.PIPE)
with sync_playwright() as p:
    b = p.chromium.launch(args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
    pg = b.new_page(viewport={'width':1920,'height':1080})
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + html); pg.wait_for_timeout(2500)
    t0 = time.time()
    for i in range(N):
        pg.evaluate(f'FILM.renderAt({i/FPS:.5f})')
        ff.stdin.write(pg.screenshot(type='png'))
        if i % 240 == 0: print(f'frame {i}/{N}  {time.time()-t0:.0f}s  errors {len(errs)}', flush=True)
    b.close()
ff.stdin.close(); ff.wait(); print('done', out, 'errors', errs[:3], flush=True)
