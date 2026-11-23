# SCRIPT: LEAVE-THE-SIGN-VIDEO-01
# Music video of the Periodic Table of Elemental Peels v2.1, cut to "Leave the Sign".
# Every label value is read from the table data or the captured page; nothing is typed in by hand
# except the words of the labels.
import json, os, sys, subprocess, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1920, 1080, 30
CAP = '/home/claude/vid/cap'
OUT = '/home/claude/vid/scenes'
os.makedirs(OUT, exist_ok=True)
meta = json.load(open(f'{CAP}/meta.json'))
beats = json.load(open('/home/claude/vid/beats.json'))['beats']
DATA = {e['sym']: e for e in json.load(open('/home/claude/votkp-lean/research/2026-11-20-element-paper-loop-wall/ptable/ptable_data.json'))['elements']}
SONG = 259.464

F_BIG = ImageFont.truetype('/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf', 86)
F_SUB = ImageFont.truetype('/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf', 34)
F_LAB = ImageFont.truetype('/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf', 38)
F_SMALL = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 24)
GOLD = (242, 193, 78); ICE = (99, 211, 255); INK = (230, 237, 244); DIM = (143, 160, 178)

def snap(t):
    return min(beats, key=lambda b: abs(b - t)) if t > 1 else t

# ---------- sources ----------
_img = {}
def img(name):
    if name not in _img:
        im = Image.open(name).convert('RGB')
        _img[name] = im
    return _img[name]

def content_box(name, thr=40):
    a = np.asarray(img(name).convert('L'))
    ys, xs = np.where(a > thr)
    return xs.min(), ys.min(), xs.max(), ys.max()

def full_cam(name, margin=0.04):
    x0, y0, x1, y1 = content_box(name)
    w, h = x1 - x0, y1 - y0
    w = max(w, h * 16 / 9) * (1 + margin)
    return ((x0 + x1) / 2, (y0 + y1) / 2, w)

def tile(z):
    x, y, w, h = meta['tiles'][str(z)]
    return ((x + w / 2) * 2, (y + h / 2) * 2)

def pt(view, startswith):
    for t, x, y in meta['pts_' + view]:
        if t.startswith(startswith):
            return (x * 2, y * 2)
    raise KeyError(startswith)

def crop(im, cx, cy, w):
    h = w * 9 / 16
    box = (int(cx - w / 2), int(cy - h / 2), int(cx + w / 2), int(cy + h / 2))
    return im.crop(box).resize((W, H), Image.BILINEAR)   # PIL pads outside with black

def ease(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)

def lerp(a, b, u):
    return tuple(x + (y - x) * u for x, y in zip(a, b))

# ---------- overlays ----------
def label_layer(title, sub=None):
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    tw = d.textlength(title, font=F_LAB); sw = d.textlength(sub, font=F_SMALL) if sub else 0
    bw = max(tw, sw) + 56
    d.rectangle((60, H - 190, 60 + bw, H - 70 if sub else H - 112), fill=(0, 0, 0, 185))
    d.rectangle((60, H - 190, 66, H - 70 if sub else H - 112), fill=GOLD + (255,))
    d.text((88, H - 178), title, font=F_LAB, fill=INK)
    if sub:
        d.text((88, H - 122), sub, font=F_SMALL, fill=GOLD)
    return L

def bug_layer():
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    t = 'Periodic Table of Elemental Peels  ·  Jeromie Beasley'
    d.text((W - 60 - d.textlength(t, font=F_SMALL), 40), t, font=F_SMALL, fill=DIM + (200,))
    return L
BUG = bug_layer()

# ---------- shot renderer ----------
class Shot:
    def __init__(self, t0, t1, src, cam0, cam1=None, label=None, seq=None, seq_speed=1.0, flash=True, fade_in=0, fade_out=0, card=None):
        self.t0, self.t1, self.src, self.cam0 = t0, t1, src, cam0
        self.cam1 = cam1 or cam0; self.seq = seq; self.seq_speed = seq_speed
        self.label = label_layer(*label) if label else None
        self.flash, self.fade_in, self.fade_out, self.card = flash, fade_in, fade_out, card
        if seq:
            self.frames = sorted(os.listdir(seq))

    def frame(self, t):
        u = ease((t - self.t0) / max(self.t1 - self.t0, 1e-6))
        if self.card is not None:
            base = self.card.copy()
        else:
            if self.seq:
                k = int((t - self.t0) * FPS * self.seq_speed) % len(self.frames)
                im = img(os.path.join(self.seq, self.frames[k]))
                if len(_img) > 40: _img.clear()
            else:
                im = img(self.src)
            base = crop(im, *lerp(self.cam0, self.cam1, u))
        base = base.convert('RGBA')
        base.alpha_composite(BUG)
        if self.label is not None:
            a = min(1.0, (t - self.t0) / 0.35, (self.t1 - t) / 0.35)
            if a > 0:
                lab = self.label if a >= 1 else Image.blend(Image.new('RGBA', (W, H), (0, 0, 0, 0)), self.label, a)
                base.alpha_composite(lab)
        out = base.convert('RGB')
        g = 1.0
        if self.flash and t - self.t0 < 0.13:
            out = Image.blend(out, Image.new('RGB', (W, H), (255, 255, 255)), 0.35 * (1 - (t - self.t0) / 0.13))
        if self.fade_in: g = min(g, (t - self.t0) / self.fade_in)
        if self.fade_out: g = min(g, (self.t1 - t) / self.fade_out)
        if g < 1:
            out = Image.blend(Image.new('RGB', (W, H)), out, max(g, 0))
        return out

def title_card(lines):
    C = Image.new('RGB', (W, H), (0, 0, 0)); d = ImageDraw.Draw(C)
    y = H / 2 - 90
    for text, font, col in lines:
        d.text(((W - d.textlength(text, font=font)) / 2, y), text, font=font, fill=col); y += font.size + 30
    return C

# ---------- shot list ----------
S = f'{CAP}/standard.jpg'
FULL = full_cam(S, 0.02)
def tcam(z, w=700): x, y = tile(z); return (x, y, w)

def fmt(x, n): return f'{x:.{n}f}'
C_, N_, O_, AU = DATA['C'], DATA['N'], DATA['O'], DATA['Au']
c_ratio = C_['ie'][4] / C_['ie'][3]
n_core = N_['cores'][0]['z']; o_core = O_['cores'][0]
cn = C_['cores'][0]['g2'] + N_['cores'][0]['g2']

B = [0, 22.8, 57.6, 84.7, 124.3, 155.9, 180.7, 206.6, 223.7, 250.4, SONG]
B = [B[0]] + [snap(x) for x in B[1:-1]] + [SONG]

VIEWS_FAST = ['disk', 'cores', 'signature', 'heavy', 'moves', 'octaves', 'decay', 'colour', 'stone', 'window', 'faces']
VIEW_LABEL = {'disk': ('The disk', 'every step as a reflection · gold circle = the wall'),
              'cores': ('Core strands', 'each noble-gas core opening, element by element'),
              'signature': ('Signatures', 'anion rung and first core opening, side by side'),
              'heavy': ('Radon onward', '2,144 more steps · none outside the wall'),
              'moves': ('Where the electron moves', 'the twenty atoms that break the filling order'),
              'octaves': ('Russell octaves', '1+ 2+ 3+ 4 3- 2- 1-'),
              'decay': ('Decay', 'strip the electrons and the heavier isobar can change'),
              'colour': ('Colour line', 'all 35 metals above half power · none of the 6 non-metals'),
              'stone': ('Stone and wanting', 'hardness against electronegativity'),
              'window': ('The window', 'every cutoff from silver to silicon sorts alike'),
              'faces': ('Two faces', 'the loop closes below the line, opens above')}

def beat_cuts(t0, t1, every, views, start=0, labels=True):
    shots = []; bs = [b for b in beats if t0 <= b < t1]
    cuts = [t0] + bs[every::every]
    cuts = [c for c in cuts if c < t1 - 0.4] + [t1]
    for i in range(len(cuts) - 1):
        v = views[(start + i) % len(views)]; src = f'{CAP}/{v}.jpg'
        fc = full_cam(src)
        z = 0.82 if i % 2 else 1.0
        shots.append(Shot(cuts[i], cuts[i + 1], src, (fc[0], fc[1], fc[2] * z), (fc[0], fc[1], fc[2] * (0.9 if i % 2 else 0.86)),
                          label=VIEW_LABEL[v] if labels else None))
    return shots

shots = []
# Intro
card = title_card([('Leave the Sign', F_BIG, INK), ('Periodic Table of Elemental Peels', F_SUB, GOLD), ('Jeromie Beasley', F_SUB, DIM)])
shots.append(Shot(0, 6.0, None, None, card=card, flash=False, fade_in=1.5, fade_out=1.0))
shots.append(Shot(6.0, B[1], S, (FULL[0], FULL[1], FULL[2] * 1.06), (FULL[0], FULL[1] * 0.98, FULL[2] * 0.8), flash=False, fade_in=1.2,
                  label=('The table hung beside the window', 'each tile is a chain of its own removal energies')))
# Verse 1: carbon, then nitrogen
t = B[1]; d = B[2] - B[1]
shots += [Shot(t, t + d * 0.22, S, FULL, tcam(6, 640), label=('Carbon', f'fifth removal costs {fmt(c_ratio, 2)}× the fourth · outside the wall')),
          Shot(t + d * 0.22, t + d * 0.48, None, (519, 300, 1066), seq=f'{CAP}/ch6', seq_speed=0.5,
               label=('Carbon’s chain', 'the gold link is the step that crosses the wall')),
          Shot(t + d * 0.48, t + d * 0.70, S, tcam(6, 640), tcam(7, 640), label=('Nitrogen · one square east', f'same helium core, z = {fmt(n_core, 2)} · inside')),
          Shot(t + d * 0.70, B[2], None, (519, 300, 1066), seq=f'{CAP}/ch7', seq_speed=0.5, label=('Nitrogen’s chain', 'the same deep door, a shorter climb'))]
# Chorus 1
shots += beat_cuts(B[2], B[3], 8, VIEWS_FAST, 0)
# Verse 2: oxygen
t = B[3]; d = B[4] - B[3]
so = f'{CAP}/stone.jpg'; ox = pt('stone', 'Oxygen')
shots += [Shot(t, t + d * 0.25, S, FULL, tcam(8, 640), label=('Oxygen', f'anion rung outside the wall · z₀ = {fmt(O_["anion"]["z0"], 2)}')),
          Shot(t + d * 0.25, t + d * 0.55, None, (519, 300, 1066), seq=f'{CAP}/ch8', seq_speed=0.5,
               label=('Oxygen’s chain', f'the helium-core pair opens inside · z = {fmt(o_core["z"], 2)}')),
          Shot(t + d * 0.55, t + d * 0.8, so, (*ox, 2400), (*ox, 1500), label=('Both marks belong', 'outside at the anion rung, inside at the core')),
          Shot(t + d * 0.8, B[4], S, tcam(8, 520), tcam(8, 900), label=('Oxygen stands on both sides at once', 'proved in Lean: oxygen_two_sides'))]
# Verse 3: two faces, carbon with nitrogen
t = B[4]; d = B[5] - B[4]
fa = f'{CAP}/faces.jpg'; cnp = pt('faces', 'C then N')
ffc = full_cam(fa)
shots += [Shot(t, t + d * 0.3, fa, ffc, (ffc[0], ffc[1], ffc[2] * 0.75), label=('Two faces', 'below the line the loop closes; above it, it opens')),
          Shot(t + d * 0.3, t + d * 0.65, fa, (*cnp, 1800), (*cnp, 700), label=('Carbon with nitrogen', f'Γa² + Γb² = {fmt(cn, 4)} · just over one')),
          Shot(t + d * 0.65, B[5], f'{CAP}/cores.jpg', full_cam(f'{CAP}/cores.jpg'), None, label=('A little daylight through', 'the helium-core strand crosses inward after carbon'))]
# Chorus 2
shots += beat_cuts(B[5], B[6], 8, VIEWS_FAST, 4)
# Bridge: Russell octaves, then the spiral
t = B[6]; d = B[7] - B[6]
oc = f'{CAP}/octaves.jpg'; occ = full_cam(oc)
sp0 = sorted(os.listdir(f'{CAP}/spiral3'))[0]; spw = img(f'{CAP}/spiral3/{sp0}').size
shots += [Shot(t, t + d * 0.4, oc, occ, (occ[0], occ[1], occ[2] * 0.8), label=('Russell’s octaves', 'up to four and down the far side')),
          Shot(t + d * 0.4, B[7], None, (spw[0] / 2, spw[1] / 2, spw[1] * 16 / 9 * 0.95), seq=f'{CAP}/spiral3', seq_speed=0.4,
               label=('After Russell’s spiral', 'one turn per period · the wall is the gold cylinder'))]
# Verse 4: the window, oxygen's three lines
t = B[7]; d = B[8] - B[7]
wi = f'{CAP}/window.jpg'; wc = full_cam(wi)
shots += [Shot(t, B[8], wi, wc, (wc[0], wc[1], wc[2] * 0.8), label=('The window', 'silver 5.8079 · the wall 5.8284 · silicon 5.8665'))]
# Final chorus: everything, faster
fin = beat_cuts(B[8], B[9] - 3.34, 4, VIEWS_FAST + ['standard'], 2, labels=False)
au_t = fin[-1].t1
shots += fin
shots.append(Shot(au_t, B[9], None, (519, 300, 1066), seq=f'{CAP}/ch79', seq_speed=0.8, label=('Gold', 'every chain is a stair the old chart never drew')))
# Outro
t = B[9]
shots += [Shot(t, SONG, S, tcam(8, 520), FULL, flash=False, fade_out=2.5, label=('Oxygen still has one square', 'both words are there'))]

# ---------- render one file per shot group ----------
def render(idx, sh):
    path = f'{OUT}/s{idx:03d}.mp4'
    if os.path.exists(path): return path
    n = int(round(sh.t1 * FPS)) - int(round(sh.t0 * FPS))
    tmp = f'{OUT}/tmp_s{idx:03d}.mp4'
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-crf', '18', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', tmp], stdin=subprocess.PIPE)
    f0 = int(round(sh.t0 * FPS))
    for k in range(n):
        p.stdin.write(sh.frame((f0 + k) / FPS).tobytes())
    p.stdin.close(); p.wait()
    if p.returncode == 0: os.replace(tmp, path)
    return path

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if mode == 'preview':
        for tt in [float(x) for x in sys.argv[2:]]:
            sh = [s for s in shots if s.t0 <= tt < s.t1][0]
            sh.frame(tt).save(f'/tmp/prev_{tt:.1f}.jpg', quality=88)
        print('shots', len(shots))
    else:
        files = [render(i, s) for i, s in enumerate(shots)]
        open(f'{OUT}/list.txt', 'w').write(''.join(f"file '{f}'\n" for f in files))
        print('rendered', len(files))
