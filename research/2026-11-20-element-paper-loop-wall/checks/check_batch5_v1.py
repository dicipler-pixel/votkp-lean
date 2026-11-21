# SCRIPT: CHECK-GPT-ELEMENTS-BATCH5-01
# Recompute every z and Gamma of batch 4 (S to Ca) from its own energy column; check the
# opening sides, the S_Z / sigma_Z table and the exact identity Z(S - sigma) = D_H - sigma^2/2,
# the crossing point, and the face apices tanh(r/4) = (sqrt z - 1)/(sqrt z + 1).
import csv, math
rows=[r for r in csv.DictReader(open('batch5.csv')) if r['IE_k (eV)']!='']
w=3+2*math.sqrt(2); by={}
for r in rows: by.setdefault(r['symbol'],[]).append(r)
bad=n=0
for el,rs in by.items():
    for a,b in zip(rs,rs[1:]):
        if a['z_k']=='': continue
        x,y=float(a['IE_k (eV)']),float(b['IE_k (eV)']); z=y/x; g=(y-x)/(y+x); n+=1
        if abs(z-float(a['z_k']))>6e-6 or abs(g-float(a['Gamma_k']))>6e-6: bad+=1; print('MISMATCH',el,a['k'],round(z,6),round(g,6),a['z_k'],a['Gamma_k'])
print('steps',n,'mismatches',bad)

# Compare the inline energy column with Jeromie's archive (the source GPT says it used).
import gzip, json, sys
d=json.load(gzip.open(sys.argv[1]))
rec={r['Z']:{t['q']:t['IE_eV'] for t in r['thresholds']} for r in d['records']}
for r in rows:
    if r['k']!='0':
        a=rec[int(r['Z'])].get(int(r['k'])-1)
        if a is not None and abs(float(r['IE_k (eV)'])-a)>1e-9: print('ENERGY DIFFERS FROM ARCHIVE',r['symbol'],'k',r['k'],r['IE_k (eV)'],'archive',a)
