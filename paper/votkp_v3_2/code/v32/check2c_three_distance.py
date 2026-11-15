# SCRIPT: LOOP2-CHECK2C-IRRATIONALITY-AND-THREE-DISTANCE
# WHY THIS DECIDES IT: (1) cos(theta) is rational at every rational z; by Niven's theorem a rational multiple of pi with rational cosine
# has cos in {0,+-1/2,+-1}; -527/625 is not, so theta/2pi is irrational (independent of the Two Trees citation). (2) three-gap theorem
# (Steinhaus): for k*alpha mod 1, k=1..n, the circular gaps take at most 3 distinct values, the largest being the sum of the other two.
# gaps computed at 50 digits so that equal gaps are recognised exactly.
# KILL LINE (before the run): cos(theta) at z=5 != -527/625 (residual>1e-45), or any n with >3 distinct gap values, or (3 values and
# largest != sum of the other two within 1e-40) -> kill.
import mpmath as mp
mp.mp.dps=60
def theta(z):
    z=mp.mpf(z); s2=(z-1)**2/(4*z); ch=1-2*s2**2   # cos(theta/2)
    return 2*mp.acos(ch)
th=theta(5); print('cos(theta) z=5:',mp.nstr(mp.cos(th),20),' residual vs -527/625:',mp.nstr(abs(mp.cos(th)+mp.mpf(527)/625),3))
a=th/(2*mp.pi); print('theta/2pi =',mp.nstr(a,25))
# continued fraction
x=a; cf=[]; 
for _ in range(14):
    q=int(mp.floor(x)); cf.append(q); x=1/(x-q)
print('continued fraction [a0;a1..]:',cf)
num,den=1,0; h0,k0=1,0; h1,k1=cf[0],1; conv=[(h1,k1)]
for q in cf[1:]:
    h0,h1=h1,q*h1+h0; k0,k1=k1,q*k1+k0; conv.append((h1,k1))
print('convergent denominators:',[c[1] for c in conv])
import math
for z in ['2','3','4','5','5.5','5.8']:
    zz=mp.mpf(z); c=mp.cos(theta(zz)); print('z',z,'cos(theta)=',mp.nstr(c,12),'rational candidates; theta/2pi=',mp.nstr(theta(zz)/(2*mp.pi),12))
alpha=a
for n in [5,8,13,21,34,55,100,200,500,1000,2000]:
    pts=sorted([(k*alpha)%1 for k in range(1,n+1)])
    gaps=[pts[i+1]-pts[i] for i in range(n-1)]+[pts[0]+1-pts[-1]]
    vals=[]
    for g in gaps:
        if not any(abs(g-v)<mp.mpf('1e-40') for v in vals): vals.append(g)
    vals.sort()
    ok = len(vals)<=3 and (len(vals)<3 or abs(vals[2]-vals[0]-vals[1])<mp.mpf('1e-40'))
    cnt=[sum(1 for g in gaps if abs(g-v)<mp.mpf('1e-40')) for v in vals]
    print('n=%d distinct gaps=%d values(x2pi)=%s counts=%s  largest=sum of other two: %s'%(n,len(vals),[mp.nstr(v*2*mp.pi,6) for v in vals],cnt,ok))
