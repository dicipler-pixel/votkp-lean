# SCRIPT: G4_HYDROGENIC_PAIRS
import gzip,json,itertools
from fractions import Fraction as F
arc='/home/claude/votkp-lean/data/element_thresholds_20261011.json.gz'
recs=json.load(gzip.open(arc,'rt'),parse_float=str)['records']
lv=[]
for r in recs:
    z=r['Z']; t=[t for t in r['thresholds'] if t['q']==z-1]
    if t and t[0]['IE_eV'] is not None: lv.append((z,r['symbol'],float(t[0]['IE_eV'])))
print(len(lv))
L=7.576234/1.30447;H=8.15168/1.3895212;w=3+2*2**.5;c=(L+H)/2
n=0;nw=0;win=[]
for a,b in itertools.combinations(lv,2):
    n+=1; z=b[2]/a[2]
    if L<=z<H: win.append((a[1],b[1],z))
    if w<z<c: nw+=1
print('pairs',n,'in (w,c)',nw,'in full Ag-Si window',len(win)); print(win)
print((50/21)**2)
