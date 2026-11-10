# SCRIPT: DIELECTRICS-01
# Open problem 4 of the vacuum-disk paper: "Colour inside the disk: dielectrics and the bowl."
# Statement under test (v1.2 section 9): clear materials live inside the disk and would fill the bowl region,
# where the knot pieces live and the 41 elements barely reach.
# Why this decides it: every tabulated-nk compound of the refractiveindex.info main shelf (not single elements) covering
# the visible is placed by G = (1-N)/(1+N). "Fill the bowl" needs two things: radius inside (|G|^2 < 1/2, most < 1/4),
# and ANGLE spread, because knot pieces fill the disk in two dimensions. A transparent material has real N, so G is real
# and negative: it can only draw a diameter.  Kill for "fill": more than 90% of points within 10 degrees of the real axis.
import os, re, yaml, numpy as np, warnings
warnings.filterwarnings('ignore')
ROOT='/home/claude/data_ri_repo/database/data/main'
def load(path):
    try: d=yaml.safe_load(open(path))
    except Exception: return None
    for blk in d.get('DATA',[]):
        if blk.get('type')=='tabulated nk':
            try: arr=np.array([[float(x) for x in ln.split()] for ln in blk['data'].strip().split('\n') if ln.strip()])
            except Exception: return None
            if arr.ndim==2 and arr.shape[1]>=3: return arr[:,0],arr[:,1],arr[:,2]
    return None
rows=[]
for mat in sorted(os.listdir(ROOT)):
    if re.fullmatch(r'[A-Z][a-z]?',mat): continue          # single elements were done in OPTICS-01
    best=None
    for dp,dn,fn in os.walk(os.path.join(ROOT,mat)):
        for f in fn:
            if not f.endswith('.yml'): continue
            r=load(os.path.join(dp,f))
            if r is None: continue
            lam,n,k=r
            if lam.min()>0.40 or lam.max()<0.70: continue
            m=(lam>=0.38)&(lam<=0.78)
            if m.sum()<3: continue
            if best is None or m.sum()>best[0]: best=(m.sum(),n[m]+1j*k[m])
    if best: rows.append((mat,best[1]))
print('compounds with tabulated n,k across the visible:',len(rows))
allG=np.concatenate([(1-N)/(1+N) for _,N in rows]); g2=np.abs(allG)**2
ang=np.degrees(np.abs(np.angle(-allG)))                    # angle away from the negative real axis
print('points:',len(allG))
print('  |G|^2 < 1/4: %.3f   < 1/2: %.3f   >= 1/2: %.3f'%(np.mean(g2<.25),np.mean(g2<.5),np.mean(g2>=.5)))
print('  within 10 deg of the real axis: %.3f   within 30 deg: %.3f'%(np.mean(ang<10),np.mean(ang<30)))
per=[(m,float(np.mean(np.abs((1-N)/(1+N))**2)),float(np.median(np.degrees(np.abs(np.angle(-(1-N)/(1+N))))))) for m,N in rows]
inside=[p for p in per if p[1]<.5]; print('  compounds with mean |G|^2 < 1/2: %d of %d'%(len(inside),len(per)))
off=[p for p in inside if p[2]>10]; print('  of those, median angle off the axis > 10 deg: %d'%len(off))
print('  the ones off the axis and inside (these are the ones that enter the bowl in two dimensions):')
for m,a,b in sorted(off,key=lambda p:-p[2])[:25]: print('     %-14s mean |G|^2 %.3f  angle %.1f deg'%(m,a,b))
print('  outside the line (mean |G|^2 >= 1/2):',[p[0] for p in per if p[1]>=.5][:30])
