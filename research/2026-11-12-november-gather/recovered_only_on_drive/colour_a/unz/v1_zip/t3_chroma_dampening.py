# SCRIPT: COLOR-DAMPEN-CHROMA-01
# Data: LANL "Diminishing Returns in Perceptual Color Space – Now in Color" (Stark, Turton, Bujack, EuroVis 2025),
# raw Qualtrics exports data-run1..3.csv in github.com/lanl/color/Color_Experiment.  Two chromatic lines at L*=70:
# green -> pink (gp70) and blue -> orange (bo70); both pass through the neutral point, so each line joins a
# colour to its complement.  Per trial: s = standard image, a / b = the two tests, c = choice ('t1' or 't2').
# STEP 0 (decoding control): which of a/b is test 1 is not documented in the export.  Decide it from the data:
# for triads with |d1 - d2| > 8 dE00 the "more different" choice must agree with the larger difference far
# above chance under the correct mapping.  If neither mapping gives > 85% agreement, STOP (decoding unknown).
# MODEL: P(choose t1) = Phi(f(d1) - f(d2)), sd = 1, d = CIEDE2000 between standard and test (their bank was built
# in equal dE00 steps).  Forms as in the gray study (linear, log, poly, sine = sphere chord) plus the ledger form.
# PREDICTION being tested (from SCHRODINGER-QGT-01: the chromatic sheet of Schrödinger's metric is a sphere, and a
# chord on a sphere is the sine form): on chromatic lines the sine form should do at least as well as log.
# KILL CONDITION, written before the run: if held-out NLL(sine) > NLL(log) + 2 SE on BOTH lines, the
# sphere-chord reading of chromatic diminishing returns is not supported by these data.
import numpy as np, pandas as pd, json, colour
from scipy.optimize import minimize
from scipy.stats import norm
base = '/home/claude/colourpaper/out/ext/lanl_color/Color_Experiment/'
lab = {}
for line in ('gp70', 'bo70'):
    dic = pd.read_csv(base + 'dict-%s_to_qualtrics_name.csv' % line)
    for _, r in dic.iterrows(): lab[r.QualtricsLink] = (line, np.array([r.L, r.a, r.b], float))
recs = []
for run in (1, 2, 3):
    d = pd.read_csv(base + 'data-run%d.csv' % run)
    for _, r in d.iterrows():
        for t in range(60):
            s, a, b, c = r.get('s%d' % t), r.get('a%d' % t), r.get('b%d' % t), r.get('c%d' % t)
            if not all(isinstance(v, str) for v in (s, a, b, c)): continue
            if s not in lab or a not in lab or b not in lab: continue
            recs.append((run, lab[s][0], tuple(lab[s][1]), tuple(lab[a][1]), tuple(lab[b][1]), c.strip()))
R = pd.DataFrame(recs, columns=['run', 'line', 'S', 'A', 'B', 'c'])
print('decoded trials:', len(R), R.line.value_counts().to_dict(), R.c.value_counts().to_dict())
de = lambda u, v: float(colour.delta_E(np.array(u), np.array(v), method='CIE 2000'))
R['dA'] = [de(s, a) for s, a in zip(R.S, R.A)]; R['dB'] = [de(s, b) for s, b in zip(R.S, R.B)]
big = (R.dA - R.dB).abs() > 8
agree_aT1 = np.mean(((R.dA > R.dB) == (R.c == 't1'))[big]); agree_bT1 = np.mean(((R.dB > R.dA) == (R.c == 't1'))[big])
print('STEP 0  agreement if a=t1: %.3f   if b=t1: %.3f   (n=%d)' % (agree_aT1, agree_bT1, big.sum()))
if max(agree_aT1, agree_bT1) < 0.85: raise SystemExit('decoding unknown — stop')
if agree_aT1 >= agree_bT1: R['d1'], R['d2'] = R.dA, R.dB
else: R['d1'], R['d2'] = R.dB, R.dA
R['y'] = (R.c == 't1').astype(int)
R['key'] = R.S.astype(str) + R.A.astype(str) + R.B.astype(str)

FORMS = {
 'linear': (lambda x, a, b: a * x, 1),
 'log':    (lambda x, a, b: a * np.log10(b * x + 1) / np.log10(b + 1), 2),
 'poly':   (lambda x, a, b: a * x ** b, 2),
 'sine':   (lambda x, a, b: a * np.sin(x * np.pi / (2 * (b + 0.5))) / np.sin(np.pi / (2 * (b + 0.5))), 2),
 'ledger': (lambda x, a, b: a * np.sqrt(np.log(np.cosh(b * x))) / np.sqrt(np.log(np.cosh(b))), 2),
}
def nll(dm, y):
    p = np.clip(norm.cdf(dm), 1e-15, 1 - 1e-15); return -np.sum(np.where(y == 1, np.log(p), np.log(1 - p)))
def fit(name, T, dmax):
    f, npar = FORMS[name]; x1, x2, y = T.d1.values / dmax, T.d2.values / dmax, T.y.values
    def obj(p):
        a = abs(p[0]); b = abs(p[1]) + 1e-9
        with np.errstate(all='ignore'): v = nll(f(x1, a, b) - f(x2, a, b), y)
        return v if np.isfinite(v) else 1e18
    best = None
    for a0 in (1, 3, 8):
        for b0 in ((0.2, 1, 3, 10, 30) if npar == 2 else (1,)):
            r = minimize(obj, [a0, b0], method='Nelder-Mead', options=dict(maxiter=4000, xatol=1e-8, fatol=1e-8))
            if best is None or r.fun < best.fun: best = r
    a = abs(best.x[0]); b = abs(best.x[1]) + 1e-9
    return (lambda T2: f(T2.d1.values / dmax, a, b) - f(T2.d2.values / dmax, a, b)), (float(a), float(b))
rng = np.random.default_rng(7)
summary = {}
for line in ('gp70', 'bo70', 'both'):
    T = R if line == 'both' else R[R.line == line]
    dmax = max(T.d1.max(), T.d2.max())
    res = {k: [] for k in FORMS}; pars = {k: [] for k in FORMS}
    for split in range(20):
        test = T.groupby('key', group_keys=False).apply(lambda t: t.sample(frac=0.25, random_state=int(rng.integers(1e9))))
        train = T.drop(test.index)
        for k in FORMS:
            fn, par = fit(k, train, dmax); res[k].append(nll(fn(test), test.y.values)); pars[k].append(par)
    s = {}
    for k in FORMS:
        dd = np.array(res[k]) - np.array(res['log'])
        s[k] = dict(heldout_nll=round(float(np.mean(res[k])), 2), dNLL_vs_log=round(float(dd.mean()), 2),
                    se=round(float(dd.std(ddof=1) / np.sqrt(len(dd))), 2), par_median=np.median(pars[k], axis=0).round(4).tolist())
    summary[line] = dict(n_trials=int(len(T)), dmax=round(float(dmax), 2), forms=s)
    print(line, json.dumps(summary[line]))
json.dump(summary, open('/home/claude/colourpaper/out/t3_chroma_result.json', 'w'), indent=1)
