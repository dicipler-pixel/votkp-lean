# SCRIPT: PHASE-LADDER-02
# Follow-up to PLASMA-WALL-01 (its kill fired for E_wall; its opposite, the phase of G at 2 eV, gave rho = +0.545 with z1).
# Sharper question: the ladder has exactly 5 neutral atoms whose first step lies beyond the half line (Li, Na, K, Rb, Cs;
# LADDER-WALL-01).  Do those same atoms carry the largest optical phase (angle of the reflection away from the real axis)?
# Why this decides it: the phase at a fixed visible energy is read for every element with a track; a rank-sum test compares the
# beyond-line atoms with the rest.  With 5 against ~36 the smallest possible one-sided p is about 1e-6.
# KILL: one-sided Mann-Whitney p > 0.01, or any two energies (1.5, 2.0, 2.5 eV) disagreeing in direction.
# Opposite: the same test on |G|^2 (the even reading) - if the even reading separates them equally well, phase adds nothing.
import os,re,yaml,gzip,json,numpy as np
from scipy.stats import mannwhitneyu
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
rec={r['symbol']:r for r in json.load(gzip.open('/home/claude/src/votkp-lean/data/element_thresholds_20261011.json.gz'))['records']}
T={}
for el in sorted(os.listdir(ROOT)):
    if not re.fullmatch(r'[A-Z][a-z]?',el) or el not in rec: continue
    best=None
    for dp,dn,fn in os.walk(os.path.join(ROOT,el)):
        for f in fn:
            if f.endswith('.yml'):
                r=load(os.path.join(dp,f))
                if r is None: continue
                lam,n,k=r
                if lam.min()>0.38 or lam.max()<0.78: continue
                span=np.log(lam.max()/lam.min())
                if best is None or span>best[0]: best=(span,lam,n,k)
    if best:
        _,lam,n,k=best; E=1.23984/lam; o=np.argsort(E); T[el]=(E[o],(1-(n[o]+1j*k[o]))/(1+(n[o]+1j*k[o])))
Z0=3+2*np.sqrt(2)
for Eq in (1.5,2.0,2.5):
    rows=[]
    for el,(E,G) in T.items():
        if not (E.min()<=Eq<=E.max()): continue
        g=np.interp(Eq,E,G.real)+1j*np.interp(Eq,E,G.imag); ie=[t['IE_eV'] for t in sorted(rec[el]['thresholds'],key=lambda t:t['q'])]
        rows.append((el,abs(np.degrees(np.angle(-g))),abs(g)**2,ie[1]/ie[0]>Z0))
    a=[r[1] for r in rows if r[3]]; b=[r[1] for r in rows if not r[3]]
    a2=[r[2] for r in rows if r[3]]; b2=[r[2] for r in rows if not r[3]]
    p=mannwhitneyu(a,b,alternative='greater').pvalue; p2=mannwhitneyu(a2,b2,alternative='two-sided').pvalue
    top=sorted(rows,key=lambda r:-r[1])[:7]
    print('E = %.1f eV: %d elements; beyond-line atoms present: %s'%(Eq,len(rows),[r[0] for r in rows if r[3]]))
    print('   phase: beyond-line %s   rest median %.1f max %.1f   one-sided p = %.2g'%([round(x,1) for x in a],np.median(b),max(b),p))
    print('   top seven phases:',[(r[0],round(r[1],1)) for r in top])
    print('   even reading |G|^2: beyond-line %s   rest median %.3f   two-sided p = %.2g'%([round(x,3) for x in a2],np.median(b2),p2))
