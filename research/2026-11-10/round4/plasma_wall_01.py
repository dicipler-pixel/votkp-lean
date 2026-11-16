# SCRIPT: PLASMA-WALL-01
# Hole 1 (atom to knot), optical side.  |G|^2 with G = (1-N)/(1+N) is the normal-incidence reflectance R, so the half line
# on the disk is R = 1/2.  The vacuum-disk paper found mean visible |G|^2 separates metals from non-metals at 1/2.
# Question: is the photon energy E_wall at which an element's track crosses the half line (last crossing, R falling below 1/2
# for good as energy rises) readable from the same element's ionisation ladder?  If yes the optical track and the ladder are
# one record and the bridge can run through it; if no, the optical record needs something the ladder does not hold.
# Why this decides it: rank correlation over all elements with a crossing inside their tabulated range, against three ladder
# readings: first threshold IE1, first step z1 = IE2/IE1, and the sum of thresholds down to the closed core.
# KILL (written first): |Spearman rho| < 0.5 for every ladder reading -> E_wall is NOT read from the ladder.
# Opposite: correlate 1/E_wall as well (rank correlation only flips sign), and test the low-energy side: the phase of G at
# 2 eV against the same readings.
import os,re,yaml,gzip,json,numpy as np
from scipy.stats import spearmanr
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
closed=[2,10,18,28,36,46,54,60,68,78,86]
rows=[]
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
    if not best: continue
    _,lam,n,k=best; E=1.23984/lam; o=np.argsort(E); E,n,k=E[o],n[o],k[o]
    G=(1-(n+1j*k))/(1+(n+1j*k)); R=np.abs(G)**2
    cr=[i for i in range(len(E)-1) if R[i]>=.5>R[i+1]]
    Ew=np.nan
    if cr and R[cr[-1]+1:].max()<.5:
        i=cr[-1]; Ew=E[i]+(R[i]-.5)/(R[i]-R[i+1])*(E[i+1]-E[i])
    ph=np.degrees(np.angle(-np.interp(2.0,E,G.real)-1j*np.interp(2.0,E,G.imag))) if E.min()<2<E.max() else np.nan
    ie=[t['IE_eV'] for t in sorted(rec[el]['thresholds'],key=lambda t:t['q'])]; Z=rec[el]['Z']
    core=max([c for c in closed if c<Z],default=0); val=sum(ie[:Z-core]) if len(ie)>=Z-core else np.nan
    rows.append((el,Z,Ew,ph,ie[0],ie[1]/ie[0] if len(ie)>1 else np.nan,val,E.min(),E.max(),R.max()))
print('elements with a tabulated track through the visible:',len(rows))
has=[r for r in rows if not np.isnan(r[2])]
print('with a last half-line crossing inside the tabulated range:',len(has))
print(' el   Z   E_wall(eV)  phase@2eV   IE1    z1=IE2/IE1  valence sum   range eV')
for r in sorted(has,key=lambda r:r[2]): print(' %-3s %3d  %8.2f   %8.1f  %6.2f  %7.2f   %9.1f   %.2f-%.1f'%(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8]))
print('never above 1/2:',[r[0] for r in rows if r[9]<.5],'  no final crossing in range:',[r[0] for r in rows if np.isnan(r[2]) and r[9]>=.5])
A=np.array([[r[2],r[3],r[4],r[5],r[6]] for r in has])
for j,name in ((2,'IE1'),(3,'z1'),(4,'valence sum')):
    m=~np.isnan(A[:,j]); rho,p=spearmanr(A[m,0],A[m,j]); print('Spearman  E_wall vs %-12s rho = %+.3f  p = %.3g  n = %d'%(name,rho,p,m.sum()))
for j,name in ((2,'IE1'),(3,'z1'),(4,'valence sum')):
    m=~np.isnan(A[:,j])&~np.isnan(A[:,1]); rho,p=spearmanr(A[m,1],A[m,j]); print('Spearman  phase@2eV vs %-10s rho = %+.3f  p = %.3g  n = %d'%(name,rho,p,m.sum()))
