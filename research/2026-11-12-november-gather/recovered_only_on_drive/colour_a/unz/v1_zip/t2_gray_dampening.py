# SCRIPT: COLOR-DAMPEN-GRAY-01
# Question: along the LANL gray axis (Bujack et al., PNAS 2022, 91,896 raw 2AFC responses),
# which dampening shape f fits held-out responses best?  Adds Jeromie's ledger form
# (COLOR-LEDGER-01: Jensen-Bregman log-det divergence, sqrt(log cosh)) to their four forms.
# Model (identical to lanl/color gray_functions.R): P(choose test1) = Phi(f(d1) - f(d2)), sd = 1,
# d = |g(Ls) - g(Lt)| with g a monotone (Fritsch-Carlson) spline through 5 equally spaced points.
# CONTROL (must pass first): reproduce their ranking — log >= spline-class fits, log beats poly and sine.
# KILL CONDITION for the ledger form, written before the run:
#   supported  if  mean held-out NLL(ledger) <= mean NLL(log) + 1 SE (over 10 splits)
#   rejected   if  mean NLL(ledger) >  mean NLL(log) + 2 SE
import numpy as np, pandas as pd, json, sys
from scipy.interpolate import PchipInterpolator
from scipy.optimize import minimize
from scipy.stats import norm

rng = np.random.default_rng(20261022)
D = pd.read_csv(sys.argv[1] if len(sys.argv) > 1 else
                '/home/claude/colourpaper/out/ext/lanl_color/Gray_Experiment/data/gray_complete_data_release.csv')
D = D.dropna(subset=['R']).reset_index(drop=True)
D['R'] = D['R'].astype(int)
D['key'] = D['Ls'].astype(str) + '_' + D['Lt1'].astype(str) + '_' + D['Lt2'].astype(str)

def nll_from_dm(dm, R):
    p1 = np.clip(norm.cdf(dm), 1e-15, 1 - 1e-15)
    return -np.sum(np.where(R == 0, np.log(p1), np.log(1 - p1)))

def g_fn(par, lo, hi):
    pts = np.concatenate([[0.0], np.cumsum(np.abs(par))])
    xs = np.linspace(lo, hi, len(pts))
    return PchipInterpolator(xs, pts), pts

FORMS = {
 'linear':  (lambda x, a, b: a * x, 1),
 'log':     (lambda x, a, b: a * np.log10(b * x + 1) / np.log10(b + 1), 2),
 'poly':    (lambda x, a, b: a * x ** b, 2),
 'sine':    (lambda x, a, b: a * np.sin(x * np.pi / (2 * (b + 0.5))) / np.sin(np.pi / (2 * (b + 0.5))), 2),
 'ledger':  (lambda x, a, b: a * np.sqrt(np.log(np.cosh(b * x))) / np.sqrt(np.log(np.cosh(b))), 2),
}

def fit_form(name, d1, d2, R):
    f, npar = FORMS[name]
    dmax = max(d1.max(), d2.max())
    x1, x2 = d1 / dmax, d2 / dmax
    def obj(p):
        a = abs(p[0]); b = abs(p[1]) + 1e-9 if npar == 2 else 1.0
        with np.errstate(all='ignore'):
            v = nll_from_dm(f(x1, a, b) - f(x2, a, b), R)
        return v if np.isfinite(v) else 1e18
    best = None
    for a0 in (2, 5, 10):
        for b0 in ((0.3, 1, 3, 10, 30) if npar == 2 else (1,)):
            r = minimize(obj, [a0, b0][:max(npar, 1)] if npar == 2 else [a0, 1.0], method='Nelder-Mead',
                         options=dict(maxiter=4000, xatol=1e-7, fatol=1e-7))
            if best is None or r.fun < best.fun: best = r
    a = abs(best.x[0]); b = abs(best.x[1]) + 1e-9 if npar == 2 else 1.0
    return (lambda dd1, dd2: f(dd1 / dmax, a, b) - f(dd2 / dmax, a, b)), (a, b), best.fun

def accuracy(dm_fn, test):
    g = test.groupby('key')
    acc = []
    for k, t in g:
        n = len(t); obs2 = t['R'].sum()
        dm = dm_fn(t['d1'].values[:1], t['d2'].values[:1])[0]
        hat2 = (1 - norm.cdf(dm)) * n
        acc.append(1 - abs(obs2 - hat2) / n)
    return float(np.mean(acc))

results = {k: {'nll': [], 'acc': [], 'par': []} for k in ['g_only'] + list(FORMS)}
lo, hi = D[['Ls', 'Lt1', 'Lt2']].min().min(), D[['Ls', 'Lt1', 'Lt2']].max().max()
for split in range(10):
    test_idx = D.groupby('key', group_keys=False).apply(
        lambda t: t.sample(n=min(50, len(t)), random_state=int(rng.integers(1e9)))).index
    test = D.loc[test_idx].copy(); train = D.drop(test_idx).copy()
    # g fit (scale free, sd = 1)
    def gobj(p):
        G, _ = g_fn(p, lo, hi)
        dm = np.abs(G(train.Ls) - G(train.Lt1)) - np.abs(G(train.Ls) - G(train.Lt2))
        return nll_from_dm(dm, train.R.values)
    gb = None
    for s in range(4):
        r = minimize(gobj, rng.uniform(0, 0.25, 4) + 0.05, method='Nelder-Mead', options=dict(maxiter=6000))
        if gb is None or r.fun < gb.fun: gb = r
    G, pts = g_fn(gb.x, lo, hi)
    def apply_g(T):
        s = hi / pts[-1]
        T = T.copy()
        T['d1'] = np.abs(G(T.Ls) - G(T.Lt1)) * s; T['d2'] = np.abs(G(T.Ls) - G(T.Lt2)) * s
        return T
    train_g, test_g = apply_g(train), apply_g(test)
    # g-only held-out
    dm_g = lambda a, b: (a - b) / (hi / pts[-1])
    results['g_only']['nll'].append(nll_from_dm(dm_g(test_g.d1.values, test_g.d2.values), test_g.R.values))
    results['g_only']['acc'].append(accuracy(dm_g, test_g))
    for name in FORMS:
        dm_fn, par, _ = fit_form(name, train_g.d1.values, train_g.d2.values, train_g.R.values)
        results[name]['nll'].append(nll_from_dm(dm_fn(test_g.d1.values, test_g.d2.values), test_g.R.values))
        results[name]['acc'].append(accuracy(dm_fn, test_g))
        results[name]['par'].append([float(par[0]), float(par[1])])
    print('split', split, {k: round(results[k]['nll'][-1], 1) for k in results}, flush=True)

summary = {}
for k, v in results.items():
    n = np.array(v['nll']); a = np.array(v['acc'])
    summary[k] = dict(nll_mean=float(n.mean()), nll_se=float(n.std(ddof=1) / np.sqrt(len(n))),
                      acc_mean=float(a.mean()), acc_se=float(a.std(ddof=1) / np.sqrt(len(a))),
                      par_median=(np.median(np.array(v['par']), axis=0).tolist() if v['par'] else None))
# paired differences vs log (same splits)
for k in results:
    if k == 'log': continue
    d = np.array(results[k]['nll']) - np.array(results['log']['nll'])
    summary[k]['dNLL_vs_log_mean'] = float(d.mean()); summary[k]['dNLL_vs_log_se'] = float(d.std(ddof=1) / np.sqrt(len(d)))
print(json.dumps(summary, indent=1))
json.dump(summary, open('/home/claude/colourpaper/out/t2_gray_result.json', 'w'), indent=1)
