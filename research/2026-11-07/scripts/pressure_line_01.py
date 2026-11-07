# SCRIPT: PRESSURE-LINE-01
# Exploratory. The 2/3 vacuum-mix line under pressure.
# Space between E = 1 - V_own/V. Squeezing shrinks the room V and leaves the atom's own size (covalent radius, Pyykko) alone,
# so the element crosses E = 2/3 at V/V0 = 3(1 - E0). Measured metallization pressures: Wikipedia "Metallization pressure"
# table (experimental rows only), fetched 2026-11-07. Bulk moduli B0: pymatgen element data (rough; flagged).
import csv, numpy as np, warnings; warnings.filterwarnings('ignore')
from scipy.stats import spearmanr
from pymatgen.core import Element as El
R={r['element']:r for r in csv.DictReader(open('/home/claude/recover/RECOVERED_ELEMENT_DATA_20261106.csv',encoding='utf-8-sig'))}
Pm={'B':160,'Si':12,'P':4.8,'S':83,'Ge':11,'Se':23,'Br':25,'Te':4,'I':16}   # GPa, experimental
rows=[]
for s,p in Pm.items():
    E0=float(R[s]['space_between_E']); vr=3*(1-E0); comp=max(0.0,1-vr)
    B=El(s).bulk_modulus; B=float(str(B).split()[0]) if B else np.nan
    Ppred=B/4*((1/min(vr,1))**4-1)
    rows.append((s,E0,vr,comp,B,Ppred,p))
print(' el   E0     V/V0 at 2/3   squeeze needed   B0(GPa)   P_pred(B0p=4)   P_measured')
for r in sorted(rows,key=lambda r:r[6]): print(' %-3s %.3f    %.3f          %.3f          %6.1f      %6.1f          %6.1f'%r)
c=[r[3] for r in rows]; m=[r[6] for r in rows]; pp=[r[5] for r in rows]
print('\nrank link squeeze needed -> measured pressure: rho=%.2f p=%.3f'%spearmanr(c,m))
ok=[i for i in range(len(rows)) if not np.isnan(pp[i])]
print('rank link EOS pressure -> measured pressure:   rho=%.2f p=%.3f  (n=%d)'%(*spearmanr([pp[i] for i in ok],[m[i] for i in ok]),len(ok)))
lo=[r for r in rows if r[0] not in ('B',)]
print('without B (stiff cage):                         rho=%.2f p=%.3f'%spearmanr([r[5] for r in lo],[r[6] for r in lo]))
mol=[r for r in rows if r[0] in ('Te','P','I','Se','Br','S')]
print('\nmolecular/chain solids only (Te P I Se Br S): squeeze -> P_m rho=%.2f p=%.3f ; EOS -> P_m rho=%.2f p=%.3f'%(*spearmanr([r[3] for r in mol],[r[6] for r in mol]),*spearmanr([r[5] for r in mol],[r[6] for r in mol])))
net=[r for r in rows if r[0] in ('Si','Ge','B')]
print('network solids (Si Ge B): E0 =',[round(r[1],3) for r in net],' all within 0.01 of 2/3, P_m =',[r[6] for r in net])
