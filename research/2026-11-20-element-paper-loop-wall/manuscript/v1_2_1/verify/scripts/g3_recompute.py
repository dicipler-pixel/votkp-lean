# SCRIPT: G3-RECOMPUTE-ELEMENT-NUMBERS
import gzip,json,math,sys
from fractions import Fraction as F
sys.path.insert(0,'/home/claude/votkp-lean/research/2026-11-20-element-paper-loop-wall/batch12/lean/window')
import verify_window as vw
B='/home/claude/votkp-lean/'
raw=gzip.open(B+'data/element_thresholds_20261011.json.gz','rt')
R=json.load(raw,parse_float=F)['records']
rec={r['Z']:r for r in R}
W=3+2*math.sqrt(2)
atoms=R[:85]
# adopted affinities with uncertainty (repo loader) + batches 13-17
adopted=vw.affinities()
P=vw.PAPER
for n in range(13,18):
    for r in vw.csv_rows(P/f'batch{n}/ladder/affinities.csv'):
        if r['EA_eV']: adopted[int(r['Z'])]=(F(r['EA_eV']),F(r['unc_eV']))
print('numeric EA entries',len(adopted),[z for z in (66,69) if z in adopted])
adopted65={z:v for z,v in adopted.items() if z not in(66,69)}
print('adopted65',len(adopted65))
def stats(aff):
    rows=[]
    for a in atoms:
        z=a['Z']; th=a['thresholds']
        lv=[aff.get(z)]+[(t['IE_eV'],t['unc_eV']) for t in th]
        for k,(p,q) in enumerate(zip(lv,lv[1:])):
            if p is None: continue
            x,dx=p;y,dy=q
            lo=hi=None
            if dx is not None and dy is not None:
                lo,hi=(y-dy)/(x+dx),(y+dy)/(x-dx)
            rows.append((z,k,y/x,lo,hi,2*(y-x)**2>(y+x)**2))
    return rows
rows=stats(adopted)
print('numeric',len(rows),'with box',sum(1 for r in rows if r[3] is not None))
# stability across boxes
bad=0;crossmin0=0
for z,k,c,lo,hi,lab in rows:
    if lo is None: continue
    gl,gh=(lo-1)/(lo+1),(hi-1)/(hi+1)
    if gl<=0<=gh: crossmin0+=1
    pl=0 if gl<=0<=gh else min(gl*gl,gh*gh); ph=max(gl*gl,gh*gh)
    ok=(pl>F(1,2)) if lab else (ph<F(1,2))
    if not ok: bad+=1
print('boxes keeping side: bad=',bad,'rects crossing z=1',crossmin0)
# anion outside counts
an=[r for r in rows if r[1]==0]
ins=[(atoms[r[0]-1]['symbol']) for r in an if not r[5]]
print('anion rows',len(an),'outside',sum(r[5] for r in an),'inside',ins)
an65=[r for r in an if r[0] not in(66,69)]
print('65 adopted: outside',sum(r[5] for r in an65),len(an65),'ordinary outside',sum(1 for r in rows if r[1]>0 and r[5]))
def win(rs,mode,ordinary):
    g=[r for r in rs if (not ordinary or r[1]!=0) and (mode=='c' or r[3] is not None)]
    ins=max((r for r in g if not r[5]),key=lambda r:r[2] if mode=='c' else r[4])
    out=min((r for r in g if r[5]),key=lambda r:r[2] if mode=='c' else r[3])
    f=lambda x:float(x)
    return len(g),atoms[ins[0]-1]['symbol'],ins[1],f(ins[2] if mode=='c' else ins[4]),atoms[out[0]-1]['symbol'],out[1],f(out[2] if mode=='c' else out[3])
for o in(False,True):
    for m in('c','b'): print('window ordinary' if o else 'window all',m,win(rows,m,o))
print('width central all',5.8665387761-5.8079020598,'wall',W)
