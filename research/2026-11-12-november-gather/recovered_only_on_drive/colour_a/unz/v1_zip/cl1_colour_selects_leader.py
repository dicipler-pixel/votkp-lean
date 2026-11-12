# SCRIPT: COLOUR-LEADER-01
# Idea under test (Jeromie, 2026-10-24): "colour selects the leader eigenvector/value".
# Setting: Schrodinger's 1920 colour metric:
#     ds^2 = (d ln h)^2 + 4 g_FS(sqrt p),   h = sum a_i x_i (brightness),   p_i = a_i x_i / h (chromatic share)
# so a colour splits into a RATE (log brightness) and a DIRECTION (a point on the chromatic sphere of radius 2).
# Light bouncing between surfaces, or passing through layers, is a positive linear map x -> M x on the three channels.
# Precise version tested here: under repeated passes,
#   (a) the colour (direction) converges to the leading (Perron) eigenvector of M, at a rate set by |lambda2/lambda1|;
#   (b) the log brightness grows by log(lambda1) per pass: the eigenvalue is the rate, the eigenvector is the colour;
#   (c) when the top two eigenvalues tie, no colour is selected: the final colour depends on where you started.
# Distance used: the chromatic part of Schrodinger's metric, d = 2 arccos(sum sqrt(p_i q_i)), computed in the
# equivalent form 4 arcsin(|sqrt p - sqrt q| / 2), which keeps full precision at small distances.
# KILL CONDITIONS (written before the run):
#   Ka: dies if the chromatic distance to the Perron colour does not fall like |lambda2/lambda1|^n (fitted rate within
#       2% of the ratio) on random positive M.
#   Kb: dies if the per-pass change in ln h does not approach ln lambda1 (to 1e-8 after 200 passes).
#   Kc: dies if, at an exact tie, different starting colours still converge to one common colour.
# Opposite tried before any verdict: does EVERY single pass bring two colours closer in Schrodinger's metric (a
# contraction, as Birkhoff proved for Hilbert's projective metric)? Counted, not assumed.
import numpy as np
rng = np.random.default_rng(1920)
a = np.array([43.33, 32.76, 1.0])               # Exner's luminous weights in Schrodinger's metric
def chroma(x):
    p = a * x / np.sum(a * x); return p
def dist(x, y):
    u, v = np.sqrt(chroma(x)), np.sqrt(chroma(y)); return 4 * np.arcsin(np.linalg.norm(u - v) / 2)
def hilbert(x, y):
    r = x / y; return np.log(r.max() / r.min())

rates, slopes = [], []
for trial in range(200):
    M = rng.uniform(0.05, 1.0, size=(3, 3))
    w, V = np.linalg.eig(M); o = np.argsort(-abs(w)); w, V = w[o], V[:, o]
    lead = np.abs(np.real(V[:, 0])); ratio = abs(w[1]) / abs(w[0])
    x = rng.uniform(0.1, 1.0, 3); d = []; lh = []
    for n in range(200):
        x = M @ x; s = x.sum(); lh.append(np.log(np.sum(a * x))); x = x / s; lh[-1] -= 0.0
        d.append(dist(x, lead))
    d = np.array(d)
    good = (d > 1e-12) & (np.arange(200) > 5)
    if good.sum() > 10:
        k = np.polyfit(np.arange(200)[good], np.log(d[good]), 1)[0]
        rates.append((np.exp(k), ratio))
    y = x.copy(); slopes.append((np.log(np.sum(a * (M @ y)) / np.sum(a * y)), np.log(abs(w[0]))))
rates = np.array(rates); slopes = np.array(slopes)
print('(a) colour converges to the Perron eigenvector: fitted per-pass shrink / |lambda2/lambda1|')
print('    median %.4f, 5th-95th percentile %.4f .. %.4f over %d random positive M'
      % (np.median(rates[:, 0] / rates[:, 1]), *np.percentile(rates[:, 0] / rates[:, 1], [5, 95]), len(rates)))
print('(b) brightness rate after 200 passes vs ln lambda1: worst difference %.1e' % np.abs(slopes[:, 0] - slopes[:, 1]).max())

M = np.diag([0.9, 0.9, 0.5])
ends = []
for start in [np.array([1, 0.2, 1.0]), np.array([0.2, 1, 1.0]), np.array([1, 1, 1.0])]:
    x = start.astype(float)
    for n in range(400): x = M @ x; x /= x.sum()
    ends.append(chroma(x))
print('(c) exact tie, final colours from three starts:', [np.round(e, 4) for e in ends])
print('    spread between them (Schrodinger distance): %.3f, %.3f' % (4*np.arcsin(np.linalg.norm(np.sqrt(ends[0])-np.sqrt(ends[1]))/2), 4*np.arcsin(np.linalg.norm(np.sqrt(ends[0])-np.sqrt(ends[2]))/2)))
for gap in [0.5, 0.1, 0.01, 0.001]:
    M = np.diag([0.9, 0.9 * (1 - gap), 0.5]); x = np.array([0.3, 1.0, 1.0]); n = 0
    lead = np.array([1.0, 0, 0])
    while dist(x, lead + 1e-300) > 1e-3 and n < 10**7:
        x = M @ x; x /= x.sum(); n += 1
    print('    near tie, relative gap %.3f: colour settles (distance < 1e-3) after %d passes' % (gap, n))

bad_s = bad_h = 0; worst = 0.0; N = 20000
for _ in range(N):
    M = rng.uniform(0.0, 1.0, size=(3, 3)) + 1e-3
    x, y = rng.uniform(0.01, 1, 3), rng.uniform(0.01, 1, 3)
    r_s = dist(M @ x, M @ y) / dist(x, y); r_h = hilbert(M @ x, M @ y) / hilbert(x, y)
    bad_s += r_s > 1 + 1e-12; bad_h += r_h > 1 + 1e-12; worst = max(worst, r_s)
print('Opposite: one pass makes two colours FARTHER apart in Schrodinger metric in %d of %d cases (worst stretch x%.2f);'
      ' in Hilbert projective metric in %d of %d' % (bad_s, N, worst, bad_h, N))
