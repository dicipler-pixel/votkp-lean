# SCRIPT: LEDGER-NBURST  ledger of narrow streaming bursts (width 5%, 10%) on the coupled base, same definition as LEDGER-BURST
import json
from ledger import *
C = 1e4; out = {}
for eb in (1, 2, 3):
    for f in (1.05, 1.1):
        tg = np.array([eb, f*eb, f*eb*1.02])
        S0 = S_curve({'base': ['const', C]}, tg); Sb = S_curve({'base': ['const', C], 'windows': [[eb, f*eb, 0.0]]}, tg)
        out['%g_%g' % (eb, f)] = float(S0[2]-Sb[2]); print(eb, f, out['%g_%g' % (eb, f)], flush=True)
json.dump(out, open('ledger_nburst.json', 'w'), indent=1)
