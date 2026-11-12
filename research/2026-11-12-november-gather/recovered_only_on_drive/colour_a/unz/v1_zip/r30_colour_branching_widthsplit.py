# SCRIPT: R30_COLOUR_BRANCHING_WIDTHSPLIT
# Same soft-colour model, cross-fitted by WIDTH instead of by phase: fit on widths 12-26, score on 28-40, and the reverse.
import json, numpy as np
from math import lgamma, log
rows = json.load(open('colour_branching.json'))['rows']
def ll(k, N, p):
    p = min(max(p, 1e-6), 1 - 1e-6)
    return lgamma(N + 1) - lgamma(k + 1) - lgamma(N - k + 1) + k * log(p) + (N - k) * log(1 - p)
bands = [('FINAL', lambda x: x['N'] <= 16), ('MIDDLE', lambda x: 16 < x['N'] < 512), ('EARLY', lambda x: x['N'] >= 512)]
grid = np.linspace(-1, 1, 81)
for name, sel in bands:
    r = [x for x in rows if sel(x)]
    out = []; tot = 0
    for fit_lo in (True, False):
        rf = [x for x in r if (x['n'] <= 26) == fit_lo]; rt = [x for x in r if (x['n'] <= 26) != fit_lo]
        if not rf or not rt: continue
        best = max(grid, key=lambda L: sum(ll(x['k'], x['N'], .5 + L * (x['prevE'] - .5)) for x in rf))
        gain = sum(ll(x['k'], x['N'], .5 + best * (x['prevE'] - .5)) - ll(x['k'], x['N'], .5) for x in rt)
        out.append((round(float(best), 3), round(gain, 2), len(rt))); tot += gain
    print(name, 'fits (lam, held-out gain, steps):', out, ' total held-out gain over coin:', round(tot, 2))
