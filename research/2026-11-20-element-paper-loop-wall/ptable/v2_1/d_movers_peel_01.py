# SCRIPT: D-MOVERS-PEEL-01
import json,gzip
R=json.load(gzip.open('../../../../data/element_thresholds_20261011.json.gz'))['records']
IE={r['Z']:[t['IE_eV'] for t in r['thresholds']] for r in R}
S={r['Z']:r['symbol'] for r in R}
rows={'3d':range(21,31),'4d':range(39,49),'5d':[57]+list(range(72,80))}
movers={24,29,41,42,44,45,46,47,78,79}
W=3+2*2**0.5
for nm,zs in rows.items():
    out=[]
    for Z in zs:
        z1=IE[Z][1]/IE[Z][0]; out.append((z1,S[Z],Z in movers))
    print(nm,' '.join(f'{s}{"*" if m else ""}:{z:.3f}' for z,s,m in out))
    srt=sorted(out); best=min(sum(1 for z,s,m in srt if (z>c)!=m) for c in [x[0]-1e-9 for x in srt]+[99])
    print('   best single-cutoff errors (movers = higher z1):',best)
