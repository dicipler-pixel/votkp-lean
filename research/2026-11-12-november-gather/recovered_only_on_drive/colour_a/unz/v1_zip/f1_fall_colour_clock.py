# SCRIPT: FALL-COLOUR-CLOCK-01
# "Is it time for fall?" Leaves as a colour clock, run through both colour tests from COLOUR-LEADER-01.
# Leaf model (pigment amounts per area, relative units; days counted from the onset of senescence):
#   chlorophyll  c1: decays at k1 = 0.108 / day  (94% lost in ~26 days; aspen mean 3.85 %/day, Fracheboud et al. 2009;
#                    New England leaves lose 92-94%, Lee et al. 2003)
#   carotenoids  c2: decays at k2 = 0.0063 / day (85% kept over 26 days; Lee et al. 2003 report 76-94% kept)
#   anthocyanin  c3: made only in red-turning species, switched on once chlorophyll falls below 20/29 of its start
#                    (Lee et al. 2003), made at rate s3 while it is light, lost at 0.03 / day   [s3, loss: illustrative]
#   brown        c4: oxidised phenolics, made after the leaf dies (day 30) at 0.04 / day, never lost [illustrative]
# Colour: Beer-Lambert through the leaf, x_ch = exp(-A sum_i c_i eps_i,ch) for channels R, G, B (white light in), then
# Schrodinger's split: brightness h = sum x_ch, chroma p = x / h, chroma distance 4 arcsin(|sqrt p - sqrt q| / 2).
# eps (absorption per unit pigment in R, G, B) is a rough stand-in, not a measured table.
# TEST A (the colour that survives): KILL CONDITIONS written before the run
#   A1 dies if the final colour is not the colour of the last pigment standing (brown), within 1e-3.
#   A2 control: ln(c2/c1) must rise at exactly k1 - k2 per day (the gap between the two decay rates is the clock rate).
#   A3 dies if temperature (which scales k1) moves the ONSET of colour change; it may only move the speed.
# TEST B (the tie): KILL CONDITIONS
#   B1 dies if, with equal decay rates (a tie), the colour moves by more than 1e-9: a tie must give no clock.
#      (Opposite tried if it dies: the pigment mix itself, which pigment leads, instead of the visible colour.)
#   B2 dies if neither an outside drive (light making anthocyanin) nor a small rate gap restarts the clock.
import numpy as np
eps = np.array([[0.9, 0.15, 1.0], [0.0, 0.45, 3.2], [0.1, 1.8, 0.6], [0.5, 0.8, 1.2]])
A = 2.5
def colour(c):
    x = np.exp(-A * c @ eps); return x / x.sum(), np.log(x.sum())
def cdist(p, q):
    return 4 * np.arcsin(np.linalg.norm(np.sqrt(p) - np.sqrt(q)) / 2)
def leaf(days, k1=0.108, k2=0.0063, red=False, s3=0.04, death=30.0, brown_rate=0.04, dt=0.01):
    c = np.array([1.0, 0.15, 0.0, 0.0]); out = []; t = 0.0
    while t <= days + 1e-9:
        out.append((t, c.copy()))
        light = 1.0 if (t % 1.0) < 0.5 else 0.0
        made3 = s3 * light if (red and c[0] < 20 / 29 and t < death) else 0.0
        made4 = brown_rate if t >= death else 0.0
        dc = np.array([-k1 * c[0], -k2 * c[1], made3 - 0.03 * c[2], made4])
        if t >= death: dc[:3] -= 0.08 * c[:3]
        c = c + dt * dc; t += dt
    return out

print('TEST A: the colour that survives')
for red in (False, True):
    run = leaf(120, red=red)
    cs = np.array([r[1] for r in run]); P = np.array([colour(c)[0] for c in cs])
    brown_only = colour(np.array([0, 0, 0, cs[-1][3]]))[0]
    print('  %s leaf: A1 final colour vs brown alone: distance %.1e' % ('red' if red else 'yellow', cdist(P[-1], brown_only)))
run = leaf(25); ts = np.array([r[0] for r in run]); cs = np.array([r[1] for r in run])
slope = np.polyfit(ts, np.log(cs[:, 1] / cs[:, 0]), 1)[0]
print('  A2 ln(carotenoid / chlorophyll) rises %.6f per day; k1 - k2 = %.6f' % (slope, 0.108 - 0.0063))
print('TEST B: the tie')
for label, kw in [('tie, no drive', dict(k1=0.05, k2=0.05)), ('tie + light drive', dict(k1=0.05, k2=0.05, red=True, s3=0.02)),
                  ('small gap 0.005', dict(k1=0.055, k2=0.05)), ('small gap 0.0005', dict(k1=0.0505, k2=0.05))]:
    run = leaf(29, **kw); c0, c1 = run[0][1], run[-1][1]
    P0, P1 = colour(c0)[0], colour(c1)[0]
    fade = colour(c0 * (c1.sum() / c0.sum()))[0]
    q0, q1 = c0 / c0.sum(), c1 / c1.sum()
    print('  %-18s visible colour moved %.3f (thinning alone would give %.3f); pigment mix moved %.2e'
          % (label, cdist(P0, P1), cdist(P0, fade), cdist(q0, q1)))
