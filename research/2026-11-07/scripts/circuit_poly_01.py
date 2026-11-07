# SCRIPT: CIRCUIT-POLY-01  (first attempt at our own knot polynomial)
# The knot diagram as an electrical circuit, read with light.
#  - Checkerboard-shade the diagram's regions. Shaded regions are the nodes; each crossing is a branch joining the two
#    shaded regions that meet there (the Tait graph). Kirchhoff: the number of spanning trees of this network is the
#    knot determinant for alternating diagrams (checked below on every alternating knot).
#  - Each branch's element is set by the crossing's handedness: right-handed = admittance z, left-handed = 1.
#    So Q(z) = sum over spanning trees T of z^(number of right-handed branches in T). Q(1) = tree count.
#  - Light leads: z = e^{i phi} runs once around the circle. Climb = Mahler measure of Q. Turn = swept area / size.
# Checks: (A) tree count = det on alternating knots; (B) invariance: same knot, different diagrams (snappy backtrack);
# (C) what the books carry: volume (beyond log det) and signature.
import numpy as np, database_knotinfo as d, snappy, re, warnings, random
from fractions import Fraction
from scipy.stats import spearmanr
warnings.filterwarnings('ignore')
def sign_of(X):
    i,j,k,l=X
    return +1 if (j==l+1 or l>j+1) else -1     # KnotTheory PositiveQ convention (wrap handled by l>j+1)
def tait(pd):
    darts={}                                  # edge label -> list of (crossing, position)
    for c,X in enumerate(pd):
        for p,e in enumerate(X): darts.setdefault(e,[]).append((c,p))
    def twin(c,p):
        a,b=darts[pd[c][p]]; return b if a==(c,p) else a
    seen={}; faces=[]
    for c in range(len(pd)):
        for p in range(4):
            if (c,p) in seen: continue
            f=len(faces); faces.append([]); h=(c,p)
            while h not in seen:
                seen[h]=f; c2,p2=twin(*h); faces[f].append((c2,p2)); h=(c2,(p2+1)%4)
    corner={}                                 # (crossing, corner index p = between p and p+1) -> face
    for f,cs in enumerate(faces):
        for (c,p) in cs: corner[(c,p)]=f
    n=len(pd); assert len(faces)==n+2, 'Euler check failed'
    adj={f:set() for f in range(len(faces))}
    for c in range(n):
        for p in range(4): adj[corner[(c,p)]].add(corner[(c,(p+1)%4)])
    col={0:0}; st=[0]
    while st:
        f=st.pop()
        for g in adj[f]:
            if g not in col: col[g]=1-col[f]; st.append(g)
    edges=[]
    for c in range(n):
        a,b=(corner[(c,0)],corner[(c,2)]) if col[corner[(c,0)]]==0 else (corner[(c,1)],corner[(c,3)])
        if a!=b: edges.append((a,b,sign_of(pd[c])))
    nodes=sorted({f for f in col if col[f]==0}); idx={f:i for i,f in enumerate(nodes)}
    return len(nodes),[(idx[a],idx[b],s) for a,b,s in edges]
def det_int(M):                               # Bareiss, exact integers
    M=[r[:] for r in M]; n=len(M); prev=1; sg=1
    for k in range(n-1):
        if M[k][k]==0:
            for r in range(k+1,n):
                if M[r][k]!=0: M[k],M[r]=M[r],M[k]; sg=-sg; break
            else: return 0
        for i in range(k+1,n):
            for j in range(k+1,n): M[i][j]=(M[i][j]*M[k][k]-M[i][k]*M[k][j])//prev
        prev=M[k][k]
    return sg*M[n-1][n-1] if n else 1
def tree_poly(nv,edges):                      # coefficients T_k, k = right-handed branches in the tree
    m=nv-1
    if m<=0: return [1]
    vals=[]
    for x in range(m+1):
        L=[[0]*nv for _ in range(nv)]
        for a,b,s in edges:
            w=x if s>0 else 1
            L[a][a]+=w; L[b][b]+=w; L[a][b]-=w; L[b][a]-=w
        vals.append(det_int([r[1:] for r in L[1:]]))
    xs=list(range(m+1)); coef=[Fraction(0)]*(m+1)   # Lagrange -> monomial coefficients
    for i,xi in enumerate(xs):
        num=[Fraction(1)]; den=Fraction(1)
        for j,xj in enumerate(xs):
            if j==i: continue
            num=[Fraction(0)]+num; 
            for t in range(len(num)-1): num[t]-=xj*num[t+1]
            den*=(xi-xj)
        for t in range(len(num)): coef[t]+=vals[i]*num[t]/den
    c=[int(v) for v in coef]
    while len(c)>1 and c[-1]==0: c.pop()
    while len(c)>1 and c[0]==0: c.pop(0)
    return c
TH=np.exp(1j*np.linspace(0,2*np.pi,2049)[:-1])
def books(c):
    p=np.polyval(np.array(c[::-1],float),TH); dz=np.roll(p,-1)-p
    return float(np.mean(np.log(np.abs(p)+1e-300))), float(0.5*np.sum(p.real*dz.imag-p.imag*dz.real)/np.mean(np.abs(p)**2))
def Q_of(pd): return tree_poly(*tait([list(X) for X in pd]))
def snapname(nm):
    m=re.match(r'^(\d+)([an])_(\d+)$',nm)
    return 'K%s%s%s'%m.groups() if m else nm
# (A) Kirchhoff check, (C) census
rows=[]; bad=0; alt_ok=0; alt_n=0
for r in d.link_list():
    try: vol=float(r['volume']); sig=int(r['signature']); det=int(r['determinant'])
    except (ValueError,TypeError): continue
    if vol<=0 or not r['pd_notation']: continue
    if int(re.match(r'(\d+)',r['name']).group(1))>12: continue
    pd=eval(r['pd_notation'])
    try: c=Q_of(pd)
    except AssertionError: bad+=1; continue
    if 'a' in r['name'] or int(re.match(r'(\d+)',r['name']).group(1))<=10 and r.get('alternating','')=='Y':
        pass
    if r.get('alternating')=='Y':
        alt_n+=1; alt_ok+= (sum(c)==det)
    m,t=books(c); rows.append((r['name'],vol,sig,np.log(det),m,t,len(pd),c))
print('(A) Kirchhoff: alternating knots with tree count = det: %d of %d   (diagram failures: %d)'%(alt_ok,alt_n,bad))
vol=np.array([x[1] for x in rows]); sig=np.array([x[2] for x in rows]); ld=np.array([x[3] for x in rows]); cm=np.array([x[4] for x in rows]); ct=np.array([x[5] for x in rows])
print('(C) n=%d  climb vs volume rho=%.3f | log det vs volume rho=%.3f'%(len(rows),spearmanr(cm,vol)[0],spearmanr(ld,vol)[0]))
k=np.polyfit(ld,vol,1); res=vol-np.polyval(k,ld)
print('    climb vs volume left after log det: rho=%.3f'%spearmanr(cm,res)[0])
A=np.column_stack([ld,cm,np.ones_like(vol)]); cc,*_=np.linalg.lstsq(A,vol,rcond=None); p=A@cc
print('    log det + circuit climb: R^2=%.3f (log det alone 0.708)'%(1-np.sum((vol-p)**2)/np.sum((vol-vol.mean())**2)))
print('    turn vs signature rho=%.3f ; |turn| vs |signature| rho=%.3f'%(spearmanr(ct,sig)[0],spearmanr(abs(ct),abs(sig))[0]))
print('    examples:',[(x[0],x[7]) for x in rows[:4]])
# (B) invariance on redrawn diagrams
random.seed(3); test=random.sample(rows,25); same=0; tot=0; cl_same=0
for nm,*_,c0 in test:
    try: L=snappy.Link(snapname(nm))
    except Exception: continue
    ref=Q_of(L.PD_code()); m0=books(ref)[0]
    for s in (4,8):
        L2=L.copy(); L2.backtrack(s); q=Q_of(L2.PD_code()); tot+=1
        same+= (q==ref); cl_same+= abs(books(q)[0]-m0)<1e-6
print('(B) invariance on %d redrawn diagrams: whole polynomial same %d, climb same %d'%(tot,same,cl_same))
