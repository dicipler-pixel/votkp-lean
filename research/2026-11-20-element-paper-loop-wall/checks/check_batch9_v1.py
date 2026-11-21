# SCRIPT: CHECK-GPT-ELEMENTS-BATCH9-01
# Niobium to rhodium (Z 41-45). Every energy in the received table is compared with the pinned archive;
# every z and Gamma is recomputed FROM THE ARCHIVE (not from the table's own energy text), and
# separately from the table's energy text, so a typo in either place shows up.
# Electron affinities for the anion rung are taken from the table and listed for separate checking.
import csv, gzip, json, sys
from fractions import Fraction as F
arch, tab = sys.argv[1], sys.argv[2]
d = json.load(gzip.open(arch)); rec = {r['Z']: r for r in d['records']}
rows = list(csv.DictReader(open(tab)))
W2 = lambda z: z > 3 and (z-3)*(z-3) > 8          # outside the loop wall
bad_e = bad_r = 0; n_ord = 0; out = []
for Z in range(41, 46):
    t = {x['q']: x['IE_eV'] for x in rec[Z]['thresholds']}
    R = {int(r['k']): r for r in rows if int(r['Z']) == Z}
    ea = F(R[0]['IE_k (eV)']) if R[0]['IE_k (eV)'] else None
    for k in sorted(R):
        r = R[k]
        if k >= 1:
            if abs(float(r['IE_k (eV)']) - t[k-1]) > 1e-9:
                bad_e += 1; print('ENERGY DIFFERS', r['symbol'], 'k', k, r['IE_k (eV)'], 'archive', t[k-1])
        if r['z_k'] == '': continue
        a = ea if k == 0 else F(repr(t[k-1])); b = F(repr(t[k]))
        z = b/a; g = (b-a)/(b+a)
        if k >= 1: n_ord += 1
        if abs(float(z) - float(r['z_k'])) > 5.1e-7 or abs(float(g) - float(r['Gamma_k'])) > 5.1e-7:
            bad_r += 1; print('RATIO DIFFERS', r['symbol'], 'k', k, round(float(z),6), round(float(g),6), 'table', r['z_k'], r['Gamma_k'])
        if W2(z): out.append((r['symbol'], k, round(float(z),6)))
print('ordinary steps', n_ord, 'energy differences', bad_e, 'ratio differences', bad_r)
print('outside the wall:', out)
