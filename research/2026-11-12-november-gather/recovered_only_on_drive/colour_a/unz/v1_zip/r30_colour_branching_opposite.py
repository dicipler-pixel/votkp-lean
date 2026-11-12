# SCRIPT: R30_COLOUR_BRANCHING_OPPOSITE
# Opposite runs and a fair version of the colour model, on the same steps as R30_COLOUR_BRANCHING.
# (1) OPPOSITE: p = 1 - E+_(j-1) (the books swap).
# (2) SOFT COLOUR: p = 1/2 + lam*(E+_(j-1) - 1/2); lam fitted on phase A widths, scored on phase B (and the reverse).
# (3) DISPERSION: how far the pass counts scatter compared with fair coins (1.0 = coin-like, >1 = clumped).
import json, numpy as np
from math import lgamma, log
rows = json.load(open('colour_branching.json'))['rows']
def ll(k, N, p):
    p = min(max(p, 1e-6), 1 - 1e-6)
    return lgamma(N + 1) - lgamma(k + 1) - lgamma(N - k + 1) + k * log(p) + (N - k) * log(1 - p)
bands = [('FINAL', lambda x: x['N'] <= 16), ('MIDDLE', lambda x: 16 < x['N'] < 512), ('EARLY', lambda x: x['N'] >= 512)]
for name, sel in bands:
    r = [x for x in rows if sel(x)]
    coin = sum(ll(x['k'], x['N'], .5) for x in r)
    opp = sum(ll(x['k'], x['N'], min(max(1 - x['prevE'], .05), .95)) for x in r)
    # soft colour, cross-fitted between phases
    tot = 0
    lams = {}
    for fit, test in (('A', 'B'), ('B', 'A')):
        rf = [x for x in r if x['ph'] == fit]; rt = [x for x in r if x['ph'] == test]
        grid = np.linspace(-1, 1, 81)
        best = max(grid, key=lambda L: sum(ll(x['k'], x['N'], .5 + L * (x['prevE'] - .5)) for x in rf))
        lams[fit] = round(float(best), 3)
        tot += sum(ll(x['k'], x['N'], .5 + best * (x['prevE'] - .5)) for x in rt) - sum(ll(x['k'], x['N'], .5) for x in rt)
    z = np.array([(x['k'] - x['N'] / 2) / np.sqrt(x['N'] / 4) for x in r])
    print(f"{name}: steps={len(r)}  opposite-coin={opp - coin:.2f}  soft-colour(held out)-coin={tot:.2f}  lam fitted A,B={lams['A']},{lams['B']}  dispersion={np.mean(z**2):.2f}")
