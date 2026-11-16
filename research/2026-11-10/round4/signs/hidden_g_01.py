# SCRIPT: HIDDEN-G-01
# Q4, atom side: the sign of the hidden level g in  z(a) = kappa - g/(a - d)  (VOTKP 5.3 / 5.9 with one hidden level),
# fitted on the ionisation ladders archived in votkp-lean/data/element_thresholds_20261011.json.gz.
import gzip, json, numpy as np, collections
from scipy.optimize import least_squares
print('''WHAT IS FITTED
 Step ratio z = IE(Z, N)/IE(Z, N+1): the peel step of the element Z between the ions holding N+1 and N electrons
 (VOTKP Thm 8.1: Gamma = (z-1)/(z+1)).  FAMILY = fixed N (an isoelectronic step), parameter a = Z.
 Model H (one hidden level, 3 numbers): z(a) = kappa - g/(a - d).   Model L (no hidden level, 2 numbers): z(a) = alpha + beta a.
WHY THIS CHECK DECIDES IT
 VOTKP 5.3 with a scalar hidden level gives A + BC/(a - d), so g = -BC; a Hermitian coupling has BC = |B|^2 > 0, so g < 0.
 The sign of g is only meaningful if the pole is really in the data, i.e. if H predicts points it was not fitted on
 better than L does.
KILL CONDITION (written before the run)
 Per family (needs >= 12 points): fit on the points with index mod 4 != 2, predict the held-out points (index mod 4 == 2).
 The sign of g COUNTS for that family only if held-out RMS(H) <= 0.5 * held-out RMS(L) and the fitted pole d lies outside
 the fitted range of a.  Families failing this are reported as "no verdict".
 Claim under test: g < 0 in every family that counts.  Killed by one counted family with g > 0.
OPPOSITE (same kill): the reversed reading z -> 1/z (the step read downward), where a Hermitian level would again need g < 0.
SECOND SETUP: extrapolation instead of interleaving: fit the lower 70% of Z, predict the upper 30%.
''')
d=json.load(gzip.open('/home/claude/src/votkp-lean/data/element_thresholds_20261011.json.gz'))['records']
fam=collections.defaultdict(list)
for r in d:
    ie=[t['IE_eV'] for t in sorted(r['thresholds'],key=lambda t:t['q']) if t.get('IE_eV')]
    qs=[t['q'] for t in sorted(r['thresholds'],key=lambda t:t['q']) if t.get('IE_eV')]
    for i in range(len(ie)-1):
        if qs[i+1]!=qs[i]+1: continue
        N=r['Z']-(i+1)                       # electrons left when the larger threshold is paid
        fam[N].append((r['Z'],ie[i+1]/ie[i]))
def fitH(a,z):
    M=np.c_[a,z,np.ones_like(a)]; kap,dd,c=np.linalg.lstsq(M,z*a,rcond=None)[0]; g=-(c+kap*dd)
    f=lambda p:(p[0]-p[1]/(a-p[2]))-z
    try: s=least_squares(f,[kap,g,dd],method='lm',max_nfev=2000); return s.x
    except Exception: return np.array([kap,g,dd])
def run(split,invert=False,label=''):
    out=[]
    for N in sorted(fam):
        pts=sorted(fam[N]); a=np.array([p[0] for p in pts],float); z=np.array([p[1] for p in pts],float)
        if invert: z=1/z
        if len(a)<12: continue
        tr,te=split(len(a))
        kap,g,dd=fitH(a[tr],z[tr]); pH=kap-g/(a[te]-dd); cL=np.polyfit(a[tr],z[tr],1); pL=np.polyval(cL,a[te])
        rH=np.sqrt(np.mean((pH-z[te])**2)); rL=np.sqrt(np.mean((pL-z[te])**2))
        counts=(rH<=0.5*rL) and not (a[tr].min()<=dd<=a[tr].max())
        out.append((N,len(a),kap,g,dd,rH,rL,counts))
    cnt=[o for o in out if o[7]]
    print('\n== %s: families with >= 12 points: %d ; verdict counts in %d ; g<0 in %d, g>0 in %d ; (no verdict: %d, of which g<0 %d)'%(label,len(out),len(cnt),sum(o[3]<0 for o in cnt),sum(o[3]>0 for o in cnt),len(out)-len(cnt),sum(o[3]<0 for o in out if not o[7])))
    return out
inter=lambda n:(np.array([i for i in range(n) if i%4!=2]),np.array([i for i in range(n) if i%4==2]))
extra=lambda n:(np.arange(0,int(0.7*n)),np.arange(int(0.7*n),n))
o1=run(inter,False,'MAIN (interleaved hold-out)')
print('   N  pts    kappa        g          d     heldout RMS H   RMS L   counts')
for o in o1: print('  %3d %3d  %8.4f  %+10.4f  %8.3f   %.2e   %.2e   %s'%o)
bad=[o[0] for o in o1 if o[7] and o[3]>0]; print('   counted families with g > 0:',bad)
closed={2,10,18,28,36,46,54,60,68,78,86}
print('   counted, by kind of step: shell-opening (N a closed core) g<0 %d g>0 %d ; inside a shell g<0 %d g>0 %d'%(
      sum(o[3]<0 for o in o1 if o[7] and o[0] in closed),sum(o[3]>0 for o in o1 if o[7] and o[0] in closed),
      sum(o[3]<0 for o in o1 if o[7] and o[0] not in closed),sum(o[3]>0 for o in o1 if o[7] and o[0] not in closed)))
print('   kappa at the closed cores against the bare shell-wall ratio (n/(n-1))^2:',[(o[0],round(o[2],3)) for o in o1 if o[0] in closed and o[7]],' bare: N=2: 4, N=10: 2.25, N=28: 1.778, N=60: 1.5625')
o2=run(inter,True,'OPPOSITE (z -> 1/z, interleaved)')
print('   counted families with g > 0:',[o[0] for o in o2 if o[7] and o[3]>0][:60])
o3=run(extra,False,'SECOND SETUP (extrapolation to the top 30% of Z)')
print('   counted families with g > 0:',[o[0] for o in o3 if o[7] and o[3]>0])
both=[o[0] for o in o1 if o[7]]; s3={o[0]:o for o in o3}
print('   sign of g agrees between MAIN and SECOND SETUP in %d of %d families counted in MAIN'%(sum(np.sign(s3[o[0]][3])==np.sign(o[3]) for o in o1 if o[7]),len(both)))
