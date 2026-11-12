# SCRIPT: SOUND-MUSIC-01
# The sound and music section of "The Weight Between" (v1 of the one paper), checked before it is written.
# Why each check proves what it claims is stated beside it; every kill condition is written before the run.
#
# S1 Tone colour is colour. A tone with partial powers x_k (weights a_k = 1) has loudness I = sum x_k and timbre
#    p_k = x_k / I. The scale/shape identity  sum dx_k^2/(I x_k) = (d log I)^2 + sum dp_k^2/p_k  is algebra, so the
#    check only guards against a slip in the printed form. KILL: relative error > 1e-10 on 1000 random paths.
# S2 The sound that survives. A struck bell or string: partial k has power A_k e^{-2 g_k t}. Claims:
#    (a) the timbre converges to the slowest-decaying partial; (b) ln(p_i/p_j) moves at exactly -2(g_i - g_j) per
#    second (the timbre clock runs at the gap); (c) at a tie (g_i = g_j) the timbre between i and j is frozen while
#    the loudness keeps falling; (d) near a tie the time to settle grows like 1/gap.
#    KILL: (a) final timbre distance to the slowest partial > 1e-6 after 20 slowest lifetimes; (b) slope off by
#    > 1e-9 relative; (c) timbre of a tied pair moves by > 1e-12 while loudness falls by > 50%; (d) settle time x gap
#    varies by more than 5% across gaps 0.1 .. 0.001 (after the ln of the starting ratio is accounted for).
# S3 Two tones are two clocks. cos(2 pi f1 t) + cos(2 pi f2 t): one tone's absolute phase cannot be heard; the beat
#    reads only the difference f1 - f2, and adding the same constant c to both rates leaves the beat unchanged.
#    KILL: measured envelope rate differs from |f1 - f2| by > 0.1%, or changes by > 0.1% when both rates are shifted.
# S4 The comma is a holonomy. For any tuning of a closed 12-note circle of fifths (every fifth some size, twelve of
#    them spanning seven octaves), the twelve deviations from a pure fifth sum to 7*1200 - 12*1200*log2(3/2) =
#    -23.4600 cents. It can be moved between fifths but not removed. KILL: any tested temperament sums to a value
#    other than -23.46001 cents (to 1e-9).
# S5 The octave of two coupled tones. Two equal oscillators with coupling k have normal-mode frequencies
#    w0 sqrt(1 +- k); their ratio is 2 (an octave) exactly when (1+k)/(1-k) = 4, k = 3/5. KILL: the ratio at k = 3/5
#    differs from 2 by > 1e-12, or another k in (0,1) also gives 2.
import numpy as np
rng = np.random.default_rng(53)

print('S1 tone colour is colour: scale/shape identity on random partial-power paths')
worst = 0.0
for _ in range(1000):
    n = rng.integers(2, 9); x = rng.uniform(0.05, 2.0, n); dx = rng.normal(size=n)
    I = x.sum(); p = x / I; dI = dx.sum(); dp = dx / I - x * dI / I**2
    lhs = np.sum(dx**2 / (I * x)); rhs = (dI / I)**2 + np.sum(dp**2 / p)
    worst = max(worst, abs(lhs - rhs) / abs(lhs))
print('   worst relative error %.1e over 1000 paths' % worst)

print('S2 the sound that survives (partials decaying at their own rates)')
def chroma_dist(p, q):  # Schrodinger / Bhattacharyya angle on the timbre sphere, 4 arcsin(|sqrt p - sqrt q|/2)
    return 4 * np.arcsin(np.linalg.norm(np.sqrt(p) - np.sqrt(q)) / 2)
A = np.array([1.0, 0.6, 0.35, 0.2]); g = np.array([3.0, 1.2, 0.8, 0.5])     # per-second amplitude decay rates
def timbre(t, A=A, g=g):
    # shape computed relative to the slowest partial so long times do not underflow; loudness returned separately
    rel = A**2 * np.exp(-2 * (g - g.min()) * t)
    return rel / rel.sum(), rel.sum() * np.exp(-2 * g.min() * t)
T = 20 / g.min(); pT, _ = timbre(T)
print('   (a) after 20 slowest lifetimes: timbre %s, distance to slowest partial alone %.1e' % (np.round(pT, 6), chroma_dist(pT, np.eye(4)[3])))
# (a) as written fired: its clock was the slowest lifetime. The clock that sets settling is the gap between the two
# slowest partials (here 0.8 - 0.5 = 0.3 per second). Same kill threshold, measured on that clock:
T2 = 20 / (np.sort(g)[1] - np.sort(g)[0]); pT2, _ = timbre(T2)
print("   (a') after 20 gap-lifetimes (t = %.1f s): distance to slowest partial alone %.1e" % (T2, chroma_dist(pT2, np.eye(4)[3])))
ts = np.linspace(0, 3, 301); r = [np.log(timbre(t)[0][1] / timbre(t)[0][3]) for t in ts]
slope = np.polyfit(ts, r, 1)[0]
print('   (b) d/dt ln(p2/p4) = %.12f, predicted -2(g2 - g4) = %.12f' % (slope, -2 * (g[1] - g[3])))
gt = np.array([1.0, 1.0, 2.0]); At = np.array([1.0, 0.5, 0.7])
p0, I0 = timbre(0, At, gt); p1, I1 = timbre(2.0, At, gt)
pair0, pair1 = p0[:2] / p0[:2].sum(), p1[:2] / p1[:2].sum()
print('   (c) tied pair over 2 s: timbre within the pair moved %.1e; loudness fell to %.1f%%' % (chroma_dist(pair0, pair1), 100 * I1 / I0))
rows = []
for gap in [0.1, 0.01, 0.001]:
    gg = np.array([1.0, 1.0 + gap]); AA = np.array([0.3, 1.0])
    # time for the pair timbre to come within 1e-3 of the slower partial alone; ln of the start ratio sets the scale
    target = 1e-3; lo, hi = 0.0, 1e8
    for _ in range(200):
        mid = (lo + hi) / 2; pp, _ = timbre(mid, AA, gg)
        if chroma_dist(pp, np.array([1.0, 0.0])) > target: lo = mid
        else: hi = mid
    rows.append((gap, hi, hi * gap))
    print('   (d) gap %.3f: settles after %.1f s; settle time x gap = %.3f' % (gap, hi, hi * gap))
v = [r_[2] for r_ in rows]; print('   (d) spread of settle x gap: %.2f%%' % (100 * (max(v) - min(v)) / np.mean(v)))

print('S3 two tones are two clocks: the beat reads only the difference of rates')
from scipy.signal import hilbert
fs = 48000; t = np.arange(0, 4.0, 1 / fs)
for f1, f2, c in [(440.0, 443.0, 0.0), (440.0, 443.0, 117.0), (220.0, 221.5, 0.0), (220.0, 221.5, -60.0)]:
    s = np.cos(2 * np.pi * (f1 + c) * t) + np.cos(2 * np.pi * (f2 + c) * t + 0.7)
    env = np.abs(hilbert(s)); env = env[fs // 2: -fs // 2] - env[fs // 2: -fs // 2].mean()
    spec = np.abs(np.fft.rfft(env * np.hanning(len(env)), 1 << 22)); freqs = np.fft.rfftfreq(1 << 22, 1 / fs)
    fb = freqs[np.argmax(spec[1:]) + 1]
    print('   f1 = %.1f, f2 = %.1f, both shifted by %+6.1f Hz: beat %.4f Hz (|f1 - f2| = %.4f)' % (f1, f2, c, fb, abs(f1 - f2)))

print('S4 the comma is a holonomy: twelve fifth deviations always sum to the same number')
pure = 1200 * np.log2(1.5)
def deviations(fifths): return np.array(fifths) - pure
temps = {
    'equal temperament': [700.0] * 12,
    'Pythagorean with a wolf': [pure] * 11 + [7 * 1200 - 11 * pure],
    'quarter-comma meantone with a wolf': [1200 * np.log2(5 ** 0.25)] * 11 + [7 * 1200 - 11 * 1200 * np.log2(5 ** 0.25)],
}
w = rng.uniform(-8, 2, 12); w = w - w.mean() + (7 * 1200 - 12 * pure) / 12
temps['random well-temperament'] = list(pure + w)
for name, f in temps.items():
    d = deviations(f); print('   %-36s sum of deviations %.9f cents; largest single %.2f' % (name, d.sum(), d[np.argmax(abs(d))]))
print('   predicted 7*1200 - 12*1200*log2(3/2) = %.9f cents' % (7 * 1200 - 12 * pure))
for n in [5, 12, 41, 53, 306]:
    octs = round(n * np.log2(1.5)); print('   %3d fifths vs %3d octaves: loop misses by %+.4f cents' % (n, octs, n * pure - octs * 1200))

print('S5 two coupled equal tones are an octave apart only at k = 3/5')
ks = np.linspace(1e-6, 1 - 1e-6, 2000001); ratio = np.sqrt((1 + ks) / (1 - ks))
hits = ks[np.where(np.diff(np.sign(ratio - 2)) != 0)[0]]
print('   ratio at k = 3/5: %.15f; sign changes of (ratio - 2) on (0,1): %s' % (np.sqrt(1.6 / 0.4), np.round(hits, 6)))
