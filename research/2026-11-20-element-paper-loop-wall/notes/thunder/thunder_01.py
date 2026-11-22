# SCRIPT: THUNDER-WALL-01
# Straw man: a trace that hits the peel wall with nowhere to go turns into a burst (thunder)
# and then locks (synchronizes) so different traces come out equal.
import numpy as np
sx=np.array([[0,1],[1,0]],float); sy=np.array([[0,-1j],[1j,0]])
def B(r,a):  # peel step as a boost of rapidity r along a
    A=a[0]*sx+a[1]*sy
    return np.cosh(r/2)*np.eye(2)+np.sinh(r/2)*A
def loop(G2):
    G=np.sqrt(G2); r=np.log((1+G)/(1-G))
    Bi=B(r,(1,0)); Bj=B(r,(0,1))
    return Bi@Bj@np.linalg.inv(Bi)@np.linalg.inv(Bj)
rng=np.random.default_rng(1)
print('Gamma^2   tr W        peak |W^n v| (n<=4000)  step of peak   angle between two traces after n=50,500,4000')
for G2 in [0.40,0.45,0.48,0.49,0.495,0.499,0.4999,0.5,0.5001,0.501,0.51,0.55]:
    W=loop(G2); t=np.trace(W).real
    v=rng.normal(size=2)+1j*rng.normal(size=2); v/=np.linalg.norm(v)
    u=rng.normal(size=2)+1j*rng.normal(size=2); u/=np.linalg.norm(u)
    x,y=v.copy(),u.copy(); peak=1; npk=0; ang={}
    for n in range(1,4001):
        x=W@x; y=W@y
        nx=np.linalg.norm(x)
        if nx>peak: peak,npk=nx,n
        if n in (50,500,4000):
            c=abs(np.vdot(x,y))/np.linalg.norm(x)/np.linalg.norm(y)
            ang[n]=np.degrees(np.arccos(min(1,c)))
        if nx>1e200: break
    print(f'{G2:<8} {t:+.6f}  {peak:12.4e}  {npk:6d}   ' + '  '.join(f'{ang.get(k,float("nan")):9.4f}' for k in (50,500,4000)))
# scaling of the burst below the wall: predicted beat period ~ pi/delta, delta = pi - theta/2
print()
print('distance d=1/2-Gamma^2   beat period (steps)   pi/delta   peak gain   peak*sqrt(d)')
for d in [1e-2,1e-3,1e-4,1e-5]:
    G2=0.5-d; W=loop(G2); t=np.trace(W).real
    half=np.arccos(t/2); delta=np.pi-half
    x=np.array([1,0],complex); norms=[]
    for n in range(int(4*np.pi/delta)+10):
        x=W@x; norms.append(np.linalg.norm(x))
    norms=np.array(norms)
    pk=[i for i in range(1,len(norms)-1) if norms[i]>=norms[i-1] and norms[i]>=norms[i+1] and norms[i]>0.5*norms.max()]
    per=np.diff(pk).mean() if len(pk)>1 else float('nan')
    print(f'{d:<22} {per:12.1f}       {np.pi/delta:10.1f}   {norms.max():10.3f}   {norms.max()*np.sqrt(d):.4f}')
