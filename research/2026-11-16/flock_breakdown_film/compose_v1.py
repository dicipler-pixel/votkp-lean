# SCRIPT: COMPOSE_V1 (Flock film, five scenes; derived from COMPOSE_P)
# Puts the captured Flock page frames (lossless PNGs from capture_p.py) into the narrator kit's 1920x1080 frame:
#   page in the kit's panel box, narrator figure (hologram, arm gestures, cane TAPS, one mirror MIRRORS turn, eye arc) screen-blended over it
#   (screen blend: black adds nothing, so there is no background rectangle), a lower band with the spoken line, then a credits card.
# The kit is imported from a copy (film/work/kit/code); its cue lists are overwritten here, nothing in the kit is edited.
# Usage: python3 compose_p.py narration.wav times.json frames_dir out.mp4 [main_seconds credits_seconds]
import sys, json, os, math, subprocess, time, glob
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
wav, times_json, fdir, outp = sys.argv[1:5]
MAIN = float(sys.argv[5]) if len(sys.argv) > 5 else 121.12
CRED = float(sys.argv[6]) if len(sys.argv) > 6 else 8.0
KIT = '/home/claude/balls/film/work/kit/code'
SCENES = [('s12', 0.0), ('s3', 43.97), ('s4', 65.38), ('s5', 84.10), ('s6', 100.0)]; CAPFPS = 15
DOI = '10.5281/zenodo.24040319'
sys.argv = ['narrator_v2.py', wav, outp, str(MAIN)]
sys.path.insert(0, KIT)
import narrator_v2 as N
T = json.load(open(times_json))
# ---- cues, placed on the spoken sentences (times.json) ----
N.TAPS = [21.3, 64.4]                   # on 'exactly one' twice: the two shares make one (Lean flux_balance); balls plus gaps make one (K2, 1e-12)
N.MIRRORS = [65.6]                      # the one mirror turn, at the start of the clocks scene
N.ARCS = [(47.1, 0.5, 0.45), (86.4, 0.5, 0.45)]   # eyes shine and the arc strikes ball A as it is kicked (kick cues in s3 and s5)
N.GESTURES = [(t['start'] + 0.1, t['end'] - 0.2, 62) for i, t in enumerate(T) if not (65.5 < t['start'] < 69.5)]
N.PANEL_ON = 1e9                        # the kit's demo books are not drawn; the page is the panel
W, H, FPS = N.W, N.H, N.FPS
x0, y0, x1, y1 = N.PBOX
NMAIN, NALL = int(round(MAIN * FPS)), int(round((MAIN + CRED) * FPS))
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; FONTB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

def text_layer(w, h, items):
    """items: (text, y_center, size, bold, rgb); every line is auto-shrunk to fit w-120 so no word is cropped; returns float layer and ink boxes"""
    im = Image.new('RGB', (w, h), (0, 0, 0)); d = ImageDraw.Draw(im); boxes = []
    for txt, yc, size, bold, rgb in items:
        while True:
            f = ImageFont.truetype(FONTB if bold else FONT, size); l, t, r, b = d.textbbox((0, 0), txt, font=f)
            if r - l <= w - 120 or size <= 18: break
            size -= 1
        assert r - l <= w - 120, ('line too wide', txt)
        px, py = (w - (r - l)) // 2 - l, int(yc - (b + t) / 2)
        d.text((px, py), txt, font=f, fill=rgb); boxes.append((px + l, py + t, px + r, py + b))
    return np.asarray(im, np.float32) / 255, boxes

# lower band under the page: dark, translucent, one line of the spoken sentence, shown from just before it is spoken to just after
BX0, BX1, BY0, BY1 = x0, x1, 950, 1034
def cap_items(txt):
    f = ImageFont.truetype(FONT, 30); d = ImageDraw.Draw(Image.new('RGB', (10, 10)))
    if d.textlength(txt, font=f) <= BX1 - BX0 - 120: return [(txt, (BY1 - BY0) / 2, 30, False, (214, 228, 242))]
    w = txt.split(' '); best = min(range(1, len(w)), key=lambda i: abs(len(' '.join(w[:i])) - len(' '.join(w[i:]))))
    return [(' '.join(w[:best]), (BY1 - BY0) * 0.30, 28, False, (214, 228, 242)), (' '.join(w[best:]), (BY1 - BY0) * 0.70, 28, False, (214, 228, 242))]
CAPS = [(s['start'] - 0.15, s['end'] + 0.45, text_layer(BX1 - BX0, BY1 - BY0, cap_items(s['text']))[0]) for s in T]
# credits card
CARD, CARDBOXES = text_layer(W, H, [('Flock of Balls on the Field', 250, 72, True, (226, 238, 250)),
    ('Jeromie Beasley', 365, 52, False, (150, 205, 255)),
    ('AI-assisted. Mixer, mathematics and narration script: Jeromie Beasley with Claude.', 460, 28, False, (170, 186, 204)),
    ('Narration voice: Kokoro am_michael', 530, 28, False, (170, 186, 204)),
    ('github.com/dicipler-pixel/votkp-lean', 600, 28, False, (170, 186, 204)),
    ('Atlas Memoriae', 710, 44, True, (242, 193, 78)),
    ('Ex memoria lux, ex luce materia', 770, 30, False, (242, 193, 78)),
    ('CC | https://doi.org/' + DOI, 880, 30, False, (170, 186, 204))])
NOTICE, _nb = text_layer(W, 80, [('The papers and proofs behind this film: doi.org/' + DOI, 40, 26, False, (150, 175, 205))])
card_margin = min(min(b[0], b[1], W - b[2], H - b[3]) for b in CARDBOXES)

def grab(f):
    t = f / FPS; nm, t0 = [x for x in SCENES if x[1] <= t + 1e-9][-1]
    nxt = [x[1] for x in SCENES if x[1] > t0]; tend = nxt[0] if nxt else MAIN
    k = min(int((t - t0) * CAPFPS), len(glob.glob(os.path.join(fdir, nm + 'f', 'f*.png'))) - 1)
    p = os.path.join(fdir, nm + 'f', f'f{k:05d}.png')
    im = cv2.cvtColor(cv2.imread(p), cv2.COLOR_BGR2RGB); assert im.shape[:2] == (y1 - y0, x1 - x0), im.shape
    return im.astype(np.float32) / 255
PAGES = [None]
R = N.Renderer(); stats = []
cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-i', wav,
       '-t', f'{MAIN + CRED:.3f}', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', outp]
p = subprocess.Popen(cmd, stdin=subprocess.PIPE); t0 = time.time()
for f in range(NALL):
    t = f / FPS
    if f < NMAIN or t < MAIN + 0.4:
        figs = R.figs(min(f, NMAIN - 1), min(t, MAIN - 1 / FPS), {'full'})
        fr = N.BG.copy(); fr[y0:y1, x0:x1] = grab(min(f, NMAIN - 1))
        c = np.array([0.15, 0.23, 0.34], np.float32)       # panel outline (kit style)
        fr[y0, x0:x1] = c; fr[y1, x0:x1] = c; fr[y0:y1, x0] = c; fr[y0:y1, x1] = c
        N.ripple(fr, t)
        if t < 5.0:
            kk = min(1, t / 0.5, (5.0 - t) / 0.5); fr[10:90, :] = 1 - (1 - fr[10:90, :]) * (1 - np.clip(NOTICE * kk, 0, 1))
        for a, b, lay in CAPS:                              # lower band
            if a <= t <= b:
                k = min(1, (t - a) / 0.25, (b - t) / 0.25)
                fr[BY0:BY1, BX0:BX1] = fr[BY0:BY1, BX0:BX1] * (1 - 0.82 * k) + 0.015 * k
                fr[BY0:BY1, BX0:BX1] = 1 - (1 - fr[BY0:BY1, BX0:BX1]) * (1 - np.clip(lay * k, 0, 1))
        N.screen(fr, figs['full'], N.FULL_POS[0], N.FULL_POS[1] + figs['dy']); N.draw_arc(fr, t, figs.get('eyes'))
    if t >= MAIN:                                           # credits card dissolves in over 0.4 s, holds
        k = min(1.0, (t - MAIN) / 0.4); k = k * k * (3 - 2 * k)
        fr = fr * (1 - k) + (N.BG * 0.6 + CARD) * k if t < MAIN + 0.4 else N.BG * 0.6 + CARD
    out = (np.clip(fr, 0, 1) * 255 + 0.5).astype(np.uint8); p.stdin.write(out.tobytes())
    lum = out.max(axis=2); stats.append((f, float(lum.mean()), float((lum > 204).mean())))
    if f % 60 == 0: print(f'frame {f}/{NALL} wall {time.time() - t0:.1f}s', flush=True)
p.stdin.close(); p.wait()
print(f'wrote {outp} in {time.time() - t0:.1f}s; credits card smallest ink margin {card_margin}px; '
      f'max mean-brightness {max(s[1] for s in stats):.1f}/255; max fraction of near-white pixels in any frame {max(s[2] for s in stats) * 100:.3f}%')
