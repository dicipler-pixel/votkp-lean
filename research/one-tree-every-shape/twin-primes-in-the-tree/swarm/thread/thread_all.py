# SCRIPT: TWIN-THREAD-ALLPRIMES-01
# The screw cut by ALL primes at once (Hardy-Littlewood local factors), mean-field first-arrival.
# Given a twin start x in end class j (11, 17, 29 mod 30), the chance that x-h is also a twin start:
#   lam_j(h) = rho * F30_j(h) * prod_{7<=p<=Pmax} f_p(h)
#   F30_j(h) = 10 if (j-h) mod 30 is a twin class, else 0
#   f_p(h) = p(p - nu_p(h)) / (p-2)^2, where nu_p(h) = size of {0, -2, h, h-2} mod p
# Gap back to the previous twin start, mean-field: P(gap = h | j) = lam_j(h) exp(-sum_{m<h} lam_j(m)).
# dev_j*G = (E[gap|j]/sum_i E[gap|i] - 1/3) * G, with G = mean of E[gap|j].
# STEP A, validation. KILL (written before the run): the method is unusable if, with primes <= 19 and the
#   matching density, it misses the exact screw values (-0.971, 0.867, 0.104) by more than 0.06 on any digit.
# STEP B, prediction with all primes <= 1e5. KILL: the full-product screw does not explain the tilt if
#   digits 1 or 7 fall more than 2 se from the real 1e8-1e9 values (-0.924 +- 0.041, 0.839 +- 0.034).
import numpy as np, math
def primes(n):
    s=np.ones(n+1,bool); s[:2]=False
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i]=False
    return np.nonzero(s)[0]
def run(Pmax, rho, H):
    h=np.arange(1,H+1)
    logF=np.zeros(H)
    for p in primes(Pmax):
        if p<7: continue
        r=np.stack([np.zeros(H,int),np.full(H,p-2),h%p,(h-2)%p],1)
        r.sort(1); nu=1+(np.diff(r,axis=1)!=0).sum(1)
        logF+=np.log(p*(p-nu)/(p-2)**2)
    F=np.exp(logF); E=[]
    for j in (11,17,29):
        lam=rho*F*np.isin((j-h)%30,(11,17,29))*10.0
        surv=np.exp(-np.concatenate([[0],np.cumsum(lam)[:-1]]))
        P=lam*surv; E.append((h*P).sum()/P.sum())
    E=np.array(E); G=E.mean()
    return (E/E.sum()-1/3)*G, G
N=math.sqrt(1e8*1e9)
# Step A: same density as the exact P<=19 screw
ps=[2,3,5,7,11,13,17,19]; W=math.prod(ps)
q=(W/np.prod([p-1 for p in ps]))/math.log(N)
slots_per_int=np.prod([p-2 for p in ps if p>2])/W
rhoA=q*q*slots_per_int
dA,GA=run(19,rhoA,8000)
errA=np.abs(dA-np.array([-0.971,0.867,0.104]))
print('A  primes<=19  dev*G',np.round(dA,3),' G %.1f'%GA,' max miss %.3f'%errA.max(),' PASS' if errA.max()<=0.06 else ' KILL')
# Step B: all primes up to 1e5, Hardy-Littlewood density 2*C2/ln^2 N
C2=0.6601618158
for Pm in (19,23,100,1000,10000,100000):
    d,G=run(Pm,2*C2/math.log(N)**2,8000)
    z=(np.array([-0.924,0.839])-d[:2])/np.array([0.041,0.034])
    print('B  primes<=%6d  dev*G (1,7,9) %s  G %.1f  z(1,7) %s'%(Pm,np.round(d,3),G,np.round(z,1)))
