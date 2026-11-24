# SCRIPT: TWIN-THREAD-ALLPRIMES-02
# The full-product screw (primes <= 1000, which has converged) against every decade 1e5..1e9,
# plus predictions for 1e9..1e12.
# KILL (written before the run): fails if digits 1 or 7 leave 2 se of the real value in any decade 1e5..1e9.
import numpy as np, math, importlib.util
spec=importlib.util.spec_from_file_location('t','thread_all.py')
src=open('thread_all.py').read().split('N=math.sqrt')[0]; ns={}; exec(src,ns)
real={(1e5,1e6):([-1.344,0.654,0.691],[0.625,0.955,0.654]),(1e6,1e7):([-1.05,0.429,0.621],[0.246,0.422,0.461]),
      (1e7,1e8):([-0.83,0.725,0.105],[0.168,0.303,0.233]),(1e8,1e9):([-0.924,0.839,0.085],[0.041,0.034,0.054])}
C2=0.6601618158; ok=True
for lo,hi in [(1e5,1e6),(1e6,1e7),(1e7,1e8),(1e8,1e9),(1e9,1e10),(1e10,1e11),(1e11,1e12)]:
    N=math.sqrt(lo*hi); d,G=ns['run'](1000,2*C2/math.log(N)**2,int(30*math.log(N)**2))
    if (lo,hi) in real:
        m,se=map(np.array,real[(lo,hi)]); z=(m-d)/se; ok&=bool(np.all(abs(z[:2])<2))
        print('%.0e-%.0e predicted %s  real %s  z(1,7) %s'%(lo,hi,np.round(d,3),m,np.round(z[:2],1)))
    else:
        print('%.0e-%.0e predicted %s  (beyond the cache)  G %.0f'%(lo,hi,np.round(d,3),G))
print('ALL DECADES PASS' if ok else 'KILL')
