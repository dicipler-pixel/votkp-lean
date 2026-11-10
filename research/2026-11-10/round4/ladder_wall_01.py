# SCRIPT: LADDER-WALL-01
# Hole 1 (atom to knot).  The half line G^2 = 1/2 is z = 3 + 2 sqrt2 = 5.828 (DEFECT-WALL-01: meridian defect |dM| = 4).
# An atom's ladder is a word of real steps z_q = IE_{q+1}/IE_q.  Question: which ladder steps lie beyond the half line, and is
# that set a clean class of steps (the step that opens a new inner shell)?
# VOTKP Thm 8.2 gives the hydrogen-like shell wall G_sh = (2n-1)/(n^2+(n-1)^2), i.e. z -> (n/(n-1))^2: for n = 2, z = 4,
# G^2 = 9/25 < 1/2.  So in the bare limit NO shell opening reaches the half line except n = 1 -> none; any step beyond it is
# beyond because of screening.
# Why this decides it: every step of every element in the archived NIST thresholds is placed; the count beyond the line is
# split by how many electrons remain before the step (N) and by whether N is a closed-core count.
# KILL for "the half line marks shell openings": more than 10% of beyond-line steps at non-closed N, or fewer than half of
# closed-core openings beyond the line.  Opposite: steps at closed cores that stay INSIDE the line are listed by Z.
import gzip,json,numpy as np
d=json.load(gzip.open('/home/claude/src/votkp-lean/data/element_thresholds_20261011.json.gz'))['records']
Z0=3+2*np.sqrt(2); closed={2,10,18,28,36,46,54,60,68,78,86}
steps=[]
for r in d:
    ie=[t['IE_eV'] for t in sorted(r['thresholds'],key=lambda t:t['q']) if t.get('IE_eV')]
    for q in range(len(ie)-1):
        z=ie[q+1]/ie[q]; Nleft=r['Z']-(q+1)          # electrons left when the larger threshold is paid
        steps.append((r['Z'],r['symbol'],q,Nleft,z))
S=np.array([(s[0],s[2],s[3],s[4]) for s in steps])
bey=S[:,3]>Z0
print('elements with at least two thresholds:',len(set(S[:,0])),'  steps:',len(S),'  beyond the half line (z > %.3f): %d'%(Z0,bey.sum()))
cl=np.array([int(n) in closed for n in S[:,2]])
print('beyond-line steps at a closed core count N: %d of %d'%((bey&cl).sum(),bey.sum()))
print('closed-core openings beyond the line: %d of %d'%((bey&cl).sum(),cl.sum()))
for N in sorted(closed):
    m=S[:,2]==N
    if m.sum()==0: continue
    zz=S[m]; b=zz[:,3]>Z0
    print('  core N=%2d: %3d openings, %3d beyond; beyond for Z in %s; largest z %.2f (Z=%d), smallest %.3f (Z=%d)'%(N,m.sum(),b.sum(),
          sorted(int(x) for x in zz[b,0])[:12],zz[:,3].max(),int(zz[zz[:,3].argmax(),0]),zz[:,3].min(),int(zz[zz[:,3].argmin(),0])))
print('beyond-line steps NOT at a closed core:',[(s[1],'q=%d'%s[2],'N=%d'%s[3],round(s[4],2)) for s in steps if s[4]>Z0 and s[3] not in closed])
m=S[:,2]==2; zz=S[m]; o=np.argsort(zz[:,0])
print('K-shell opening (N=2) z by Z:',[(int(a),round(float(b),3)) for a,b in zz[o][:12,[0,3]]],' -> bare limit 4')
