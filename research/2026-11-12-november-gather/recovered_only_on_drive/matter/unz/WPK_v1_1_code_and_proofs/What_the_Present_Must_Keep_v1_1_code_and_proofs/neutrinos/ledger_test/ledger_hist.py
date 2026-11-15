# SCRIPT: LEDGER-HIST  kept population S(eps) on a common log grid for every full history used in K2 (and the baselines)
import json, time
from ledger import *
H = {'inst': {'base': ['inst']}, 'const1e4': {'base': ['const', 1e4]}}
for ed in (0.25, 0.5, 1, 2, 4, 8): H['n3_%g' % ed] = {'base': ['power', ed, 3]}
for ed in (1, 2, 3): H['n6_%g' % ed] = {'base': ['power', ed, 6]}
out = {'grid': GRID.tolist()}
for k, h in H.items():
    t1 = time.time(); out[k] = S_curve(h, GRID).tolist(); print(k, 'S(1.7)=%.4f S(6)=%.4f' % tuple(np.interp([1.7, 6.0], GRID, out[k])), '%.0fs' % (time.time()-t1), flush=True)
json.dump(out, open('ledger_hist.json', 'w'))
