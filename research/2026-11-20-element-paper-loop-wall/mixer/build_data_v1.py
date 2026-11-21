# SCRIPT: ELEMENT-MIXER-DATA-V1
# Builds the data block for the element-paper mixer from the pinned threshold archive and the affinity
# table used in the paper (hydrogen to astatine). Every number shown in the mixer comes from here.
import gzip, json, math, sys
d = json.load(gzip.open(sys.argv[1])); rec = {r['Z']: r for r in d['records']}
EA = {'H':0.754195,'Li':0.618049,'B':0.279723,'C':1.2621226,'O':1.4611136,'F':3.4011898,'Na':0.547926,
 'Al':0.43283,'Si':1.3895212,'P':0.746609,'S':2.0771042,'Cl':3.612725,'K':0.501459,'Ca':0.02455,
 'Sc':0.17938,'Ti':0.07554,'V':0.52766,'Cr':0.675928,'Fe':0.153236,'Co':0.662255,'Ni':1.157368,'Cu':1.23578,
 'Ga':0.301166,'Ge':1.2326764,'As':0.804486,'Se':2.020667,'Br':3.363588,'Rb':0.485916,'Sr':0.05206,'Y':0.31129,'Zr':0.433283,
 'Nb':0.91740,'Mo':0.74723,'Tc':0.636,'Ru':1.046270,'Rh':1.14273,'Pd':0.56214,'Ag':1.30447,'In':0.38392,'Sn':1.112070,
 'Sb':1.047401,'Te':1.970875,'I':3.0590465,'Cs':0.471626,'Ba':0.14462,'La':0.557546,'Ce':0.600160,'Pr':0.10923,'Nd':0.09748,
 'Eu':0.116,'Gd':0.212,'Tb':0.13131,'Lu':0.23882,'Hf':0.1780,'Ta':0.328859,'W':0.816500,'Re':0.060396,'Os':1.077661,
 'Ir':1.564057,'Pt':2.12510,'Au':2.30861,'Tl':0.320053,'Pb':0.356721,'Bi':0.942362,'At':2.41578}
EL = []
for Z in range(1, 86):
    r = rec[Z]; t = {x['q']: x['IE_eV'] for x in r['thresholds']}
    EL.append({'Z': Z, 's': r['symbol'], 'n': r['name'], 'ie': [t[q] for q in sorted(t)], 'ea': EA.get(r['symbol'])})
def op(Z, N):
    t = EL[Z-1]['ie']; q = Z-N-1
    return t[q+1]/t[q] if 0 <= q and q+1 < len(t) else None
cores = {}
for N, nm in [(2,'helium'),(10,'neon'),(18,'argon'),(36,'krypton'),(54,'xenon')]:
    cores[nm] = [[Z, op(Z, N)] for Z in range(N+1, 86) if op(Z, N)]
Eh = 27.211386245988
scr = []
for Z in range(2, 86):
    t = EL[Z-1]['ie']; h = t[Z-1]/Eh; b = t[Z-2]/Eh
    scr.append([Z, (h-b)/Z, Z - math.sqrt(2*b)])
out = {'el': EL, 'cores': cores, 'scr': scr,
       'loc': {'Rb': [[4,5.684416],[6,7.974303],[8,10.378817],[10,12.622018]], 'Kr': [[4,0.0669244],[6,0.0669717],[8,0.0669722]],
               'share': {'Rb': 0.475015, 'Kr': 0.991270}},
       'screw': {'betaMn': 9.9306, 'Se': [4.30, 4.89, 0.218], 'Te': [4.456, 5.921, -0.2636]}}
open('element_data_v1.js', 'w').write('window.ELEMENT_DATA=' + json.dumps(out, separators=(',', ':')) + ';')
print(len(json.dumps(out)), 'bytes;', sum(1 for e in EL if e['ea']), 'anions')
