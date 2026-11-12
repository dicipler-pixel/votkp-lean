# SCRIPT: LEDGER-RBURST  kept population S(eps) for the RAMPED coupling bursts on the instant base (exact same staircase windows as the runs)
import json
from ledger import *
H = json.load(open('rburst_hspecs.json')); out = {'grid': GRID.tolist()}
for k, h in H.items():
    out[k] = S_curve(h, GRID).tolist(); print(k, 'S(6)=%.4f' % np.interp(6, GRID, out[k]), flush=True)
json.dump(out, open('ledger_rburst.json', 'w'))
