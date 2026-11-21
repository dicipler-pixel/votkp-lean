# SCRIPT: CHECK-HARDNESS-ELECTROPHILICITY-01
# The anion rung in conceptual-DFT language (Pearson convention): hardness eta = (IE - EA)/2,
# Mulliken electronegativity chi = (IE + EA)/2, electrophilicity omega = chi^2 / (2 eta).
# Gamma0 = eta/chi exactly, omega/eta = 1/(2 Gamma0^2), so the loop wall Gamma0^2 = 1/2 is omega = eta.
# Pass rule: the side of the wall from z0 = IE/EA and the side from omega vs eta agree for every bound anion.
import gzip, json, sys, math
d = json.load(gzip.open(sys.argv[1])); rec = {r['Z']: r for r in d['records']}
EA = {'H':0.754195,'Li':0.618049,'B':0.279723,'C':1.2621226,'O':1.4611136,'F':3.4011898,'Na':0.547926,
      'Al':0.43283,'Si':1.3895212,'P':0.746609,'S':2.0771042,'Cl':3.612725,'K':0.501459,'Ca':0.02455,
      'Sc':0.17938,'Ti':0.07554,'V':0.52766,'Cr':0.675928,'Fe':0.153236,'Co':0.662255,'Ni':1.157368,'Cu':1.23578,
      'Ga':0.301166,'Ge':1.2326764,'As':0.804486,'Se':2.020667,'Br':3.363588,'Rb':0.485916,'Sr':0.05206,
      'Y':0.31129,'Zr':0.433283,'Nb':0.91740,'Mo':0.74723,'Tc':0.636,'Ru':1.046270,'Rh':1.14273,
      'Pd':0.56214,'Ag':1.30447,'In':0.38392,'Sn':1.112070,'Sb':1.047401,'Te':1.970875,'I':3.0590465,'Cs':0.471626}
W = 3 + 2*math.sqrt(2); bad = 0; rows = []
for Z in range(1, 56):
    s = rec[Z]['symbol']
    if s not in EA: continue
    I = {x['q']: x['IE_eV'] for x in rec[Z]['thresholds']}[0]; A = EA[s]
    eta, chi = (I-A)/2, (I+A)/2; omega = chi*chi/(2*eta); z = I/A
    side_z = 'outside' if z > W else 'inside'; side_w = 'outside' if omega < eta else 'inside'
    bad += side_z != side_w
    rows.append((omega/eta, rec[Z]['name'], z, eta/chi, side_z))
for r in sorted(rows): print(f'{r[1]:12s} omega/eta {r[0]:8.4f}  z0 {r[2]:9.4f}  eta/chi {r[3]:.5f}  {r[4]}')
print('bound anions', len(rows), 'disagreements', bad)
