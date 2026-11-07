# SCRIPT: DRAWING-POLY-02
# Read the knot potential off ANY drawing (KnotInfo PD code). PD crossing X[i,j,k,l]: i incoming under strand, then
# counter-clockwise; opposite pairs (i,k) under, (j,l) over. The Cho-Kim-Kim crossing term pairs (b,d) and (a,c) as
# opposite sides. The paper's corner placement is in a figure we do not have, so every placement is tested: which pair
# is (b,d), and the order within each pair, separately for positive and negative crossings (8 x 8 = 64 rules).
# A rule is accepted only if, on several different knots, the solution with the largest Im V0 reproduces SnapPy's
# complex volume (vol, and cs mod pi^2) exactly. No fitting: either a rule reproduces it or it does not.
import numpy as np, snappy, warnings, itertools, database_knotinfo as d
warnings.filterwarnings('ignore')
from drawing_poly_01 import build, solve, V0
def sign_of(X):
    i,j,k,l=X; return +1 if (j==l+1 or l>j+1) else -1
PLACE=[]
for pair in ('under','over'):
    for s1 in (0,1):
        for s2 in (0,1): PLACE.append((pair,s1,s2))
def place(X,rule):
    i,j,k,l=X; pair,s1,s2=rule
    bd=(i,k) if pair=='under' else (j,l); ac=(j,l) if pair=='under' else (i,k)
    b,dd=bd if s1==0 else bd[::-1]; a,c=ac if s2==0 else ac[::-1]
    return (a,b,c,dd)
KI={r['name']:r for r in d.link_list()}
def crossings_from(name,rp,rn):
    pd=eval(KI[name]['pd_notation']); labels=sorted({e for X in pd for e in X}); idx={e:t for t,e in enumerate(labels)}
    cr=[]
    for X in pd:
        a,b,c,dd=place(X,rp if sign_of(X)>0 else rn); cr.append((idx[a],idx[b],idx[c],idx[dd]))
    return cr,len(labels)
def score(name,rp,rn,starts=40):
    cr,n=crossings_from(name,rp,rn); T=build(cr); sols=solve(T,n,starts=starts)
    if not sols: return None
    vals=[V0(T,z,n) for z in sols]; best=max(vals,key=lambda v:v.imag)
    cv=complex(snappy.Manifold(name).complex_volume())
    dcs=((-best.real-cv.imag)+np.pi**2/2)%np.pi**2-np.pi**2/2
    return abs(best.imag-cv.real),abs(dcs)
if __name__=='__main__':
  hits=[]
  for rp in PLACE:
    for rn in PLACE:
        s=score('4_1',rp,rn)
        if s and s[0]<1e-6 and s[1]<1e-5:
            s2=score('5_2',rp,rn)
            if s2 and s2[0]<1e-6 and s2[1]<1e-5: hits.append((rp,rn))
  print('rules reproducing 4_1 and 5_2 exactly:',len(hits))
  for h in hits[:8]: print('  positive:',h[0],' negative:',h[1])
  import json; json.dump(hits,open('drawing_rules.json','w'))
