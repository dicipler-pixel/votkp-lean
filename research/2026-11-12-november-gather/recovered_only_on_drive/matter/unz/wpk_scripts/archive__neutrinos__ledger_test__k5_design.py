archive/neutrinos/ledger_test/k5_design.py

\# SCRIPT: K5-DESIGN look for a collision history with a DIFFERENT kappa(eps) shape that writes (nearly) the same ledger S(eps) a s McCormick's n=3 histories. \# Candidate family: two-level step kappa/H = cap for eps \< e1, = c for e1 \<= eps \< e2, = 0 after e2 (shape unlike a power law). import json, numpy as np from scipy.optimize import minimize from ledger import S_curve LH = json.load(open('ledger_hist.json')); g = np.array(LH\['grid'\]) sel = (g \> 0.15) & (g \< 8.0); tg = g\[sel\] def hist(p):

e1, c, e2 = np.exp(p\[0\]), 10\*\*p\[1\], np.exp(p\[0\]) + np.exp(p\[2\]) return {'base': \['const', 0.0\], 'windows': \[\[0.0, e1, 5e5\], \[e1, e2, c\]\]} best = {} for key in ('n3_1', 'n3_2'):

tgt = np.array(LH\[key\])\[sel\] f = lambda p: float(np.max(np.abs(S_curve(hist(p), tg, rtol=1e-6, atol=1e-9) - tgt))) ed = float(key.split('_')\[1\]); x0 = \[np.log(0.5\*ed), np.log10(3.0), np.log(1.0\*ed)\] r = minimize(f, x0, method='Nelder-Mead', options=dict(maxfev=120, xatol=1e-3, fatol=1e-5)) h = hist(r.x); best\[key\] = dict(h=h, maxdiff=r.fun) print(key, 'history', h\['windows'\], 'max|S_B - S_A| = %.4f' % r.fun, flush=True) json.dump(best, open('k5_design.json', 'w'), indent=1)


