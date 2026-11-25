# SCRIPT: CONNECT-ROWLAND-GHOSTS-01
# Lead L2. Fourier lines of the primes and of the twin-prime starts up to N = 10^7, at frequency a/q.
# Height = |sum over the set of exp(2 pi i n a / q)| / (size of the set).
# Predicted closed forms (written before the run):
#   primes: height at a/q (lowest terms) = |mu(q)| / phi(q)  (Ramanujan sum over Euler's totient): 1/2 -> 1, 1/3 -> 1/2,
#           1/5 -> 1/4, 1/6 -> 1/2, 1/10 -> 1/4, 1/15 -> 1/8, 1/30 -> 1/8, 1/7 -> 1/6; zero at 1/4, 1/9, 1/25.
#   twin starts: height = product over odd primes p dividing q of 2|cos(2 pi a_p / p)|/(p - 2), times 1 for p = 2,
#           where a/q = sum a_p/p mod 1; zero when q is not squarefree. So 1/3 -> 1 (full height), 1/5 and 4/5 -> 0.2060,
#           2/5 and 3/5 -> 0.5393: twin ghosts of one period are NOT of equal height, unlike the primes.
# KILL LINES: any measured height off its prediction by more than 0.01 (finite-size error ~ 1/sqrt(count) plus drift);
#   any frequency with denominator not dividing a squarefree number showing a line above 0.01; any off-grid frequency
#   (irrational, e.g. 1/sqrt(2)/10) above 0.01.
import numpy as np, math
from fractions import Fraction as F
N=10**7
s=np.ones(N+3,dtype=bool); s[:2]=False
for i in range(2,int((N+2)**.5)+1):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s[:N+1])[0]; P=P[P>30]
T=P[s[P+2]]
def fac(q):
    f={}; p=2
    while q>1:
        while q%p==0: f[p]=f.get(p,0)+1; q//=p
        p+=1
    return f
def pred_prime(a,q):
    f=fac(q); return 0.0 if any(e>1 for e in f.values()) else 1.0/np.prod([p-1 for p in f]) if f else 1.0
def pred_twin(a,q):
    f=fac(q)
    if any(e>1 for e in f.values()): return 0.0
    h=1.0
    for p in f:
        if p==2: continue
        ap=(a*pow(q//p,-1,p))%p     # a/q = sum a_p/p
        h*=2*abs(math.cos(2*math.pi*ap/p))/(p-2)
    return h
def height(S,x): return abs(np.exp(2j*np.pi*((S*x)%1.0)).sum())/len(S)
def hq(S,a,q): return abs(np.exp(2j*np.pi*((S*a)%q)/q).sum())/len(S)
print('primes above 30 up to 1e7:',len(P),'; twin starts:',len(T))
fired=0
print('%8s %10s %10s | %10s %10s'%('a/q','primes','formula','twins','formula'))
for a,q in [(1,2),(1,3),(1,5),(2,5),(1,6),(1,10),(3,10),(1,15),(2,15),(4,15),(7,15),(1,30),(7,30),(11,30),(13,30),(1,7),(2,7),(3,7),(1,210),(1,4),(1,9),(1,25),(1,8),(1,12)]:
    mp,mt=hq(P,a,q),hq(T,a,q); pp,pt=pred_prime(a,q),pred_twin(a,q)
    bad=abs(mp-pp)>0.01 or abs(mt-pt)>0.01; fired+=bad
    print('%8s %10.5f %10.5f | %10.5f %10.5f %s'%('%d/%d'%(a,q),mp,pp,mt,pt,'FIRED' if bad else ''))
for x in (0.1/math.sqrt(2),1/math.pi,0.0333):
    mp,mt=height(P.astype(float),x),height(T.astype(float),x); bad=mp>0.01 or mt>0.01; fired+=bad
    print('%8.5f %10.5f %10.5f | %10.5f %10.5f %s'%(x,mp,0,mt,0,'FIRED' if bad else ''))
print('kill lines fired:',fired)
# sum of squared heights over all a mod 30 (Parseval): equals 30 * sum of squared class shares = 30/8 for primes, 30/3 for twins
for name,S,cls in (('primes',P,8),('twins',T,3)):
    tot=sum(hq(S,a,30)**2 for a in range(30)); print('Parseval,',name,': sum over the 30 lines of height^2 = %.4f ; 30/(number of live classes) = %.4f'%(tot,30/cls))
