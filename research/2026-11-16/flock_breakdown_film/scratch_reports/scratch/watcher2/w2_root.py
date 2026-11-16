# SCRIPT: W2-ROOT (watcher phase 2). Kill: page 4.3 says Re(lambda)>0 'for any delay' for lambda=-i a (1+exp(-lambda tau)) and ~2a^2 tau small tau. Find the max-real-part root over many starts; check Re>0 for a*tau from 1e-3 to 50.
import numpy as np, mpmath as mp
mp.mp.dps=30
def roots(a,tau):
    f=lambda l: l+1j*a*(1+mp.e**(-l*tau))
    out=[]
    for re in np.linspace(-1,1.5,11):
        for im in np.linspace(-6*a-6,2*a+6,41):
            try:
                r=mp.findroot(f,mp.mpc(re,im),tol=1e-20,maxsteps=60)
                if all(abs(r-q)>1e-8 for q in out): out.append(r)
            except Exception: pass
    return out
for a,tau in [(0.5,0.0),(0.5,0.05),(0.5,2.0),(1,0.01),(1,0.1),(1,0.5),(1,1),(1,3),(1,10),(1,30),(0.01,1),(0.01,100)]:
    if tau==0: print(a,tau,'lambda=',-2j*a); continue
    R=roots(a,tau); m=max(R,key=lambda r:r.real)
    print('a',a,'tau',tau,'a*tau',a*tau,'max Re',mp.nstr(m.real,6),'2a^2tau',2*a*a*tau,'n roots',len(R))
