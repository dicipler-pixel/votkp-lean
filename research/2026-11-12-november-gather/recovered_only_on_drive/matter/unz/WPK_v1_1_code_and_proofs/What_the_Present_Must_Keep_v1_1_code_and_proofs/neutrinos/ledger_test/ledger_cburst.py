# SCRIPT: LEDGER-CBURST  kept population S(eps) on the common grid for coupling bursts (kappa/H = cap 5e5 in [eps_b, 1.25 eps_b]) on the instant base.
# The coupling burst is not a localized ledger entry: it changes the ledger at all later eps (erases the hidden moments that would flow back,
# and restarts streaming from a pure monopole), so the full curve S_cb(eps) is stored.
import json
from ledger import *
out = {'grid': GRID.tolist()}
for eb in (0.25, 0.5, 1, 1.5, 2, 3, 4, 6):
    h = {'base': ['inst'], 'windows': [[eb, 1.25*eb, 5e5]]}
    out['cb_%g' % eb] = S_curve(h, GRID).tolist()
    print(eb, 'S(6)=%.4f S(14)=%.4f' % (np.interp(6, GRID, out['cb_%g' % eb]), out['cb_%g' % eb][-1]), flush=True)
json.dump(out, open('ledger_cburst.json', 'w'))
