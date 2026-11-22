# SCRIPT: G2_BW (check Bloch-Wigner expansion D(s)=D(w)-(3sqrt3/4)|G|^2+(sqrt3/4)Re(G^3)+(3sqrt3/16)|G|^4+O(|G|^5), G=(s-w)/(s-conj w), w=exp(i pi/3))
import mpmath as mp
mp.mp.dps=40
w=mp.e**(1j*mp.pi/3)
def D(s):
    return mp.im(mp.polylog(2,s))+mp.arg(1-s)*mp.log(abs(s))
D0=D(w)
print('D(w)=',D0)
def s_of_G(G): return (w-G*mp.conj(w))/(1-G)
def pred(G):
    r3=mp.sqrt(3)
    return D0-3*r3/4*abs(G)**2+r3/4*mp.re(G**3)+3*r3/16*abs(G)**4
for rho in (mp.mpf('0.02'),mp.mpf('0.04'),mp.mpf('0.08')):
    worst=0;ratio=0
    for k in range(24):
        phi=2*mp.pi*k/24+0.1
        G=rho*mp.e**(1j*phi)
        err=abs(D(s_of_G(G))-pred(G))
        ratio=max(ratio,err/rho**5)
    print('rho',rho,'max |err|/rho^5',mp.nstr(ratio,6))
# also check coefficient of G^2 term: coefficient of Re(G^2) should vanish, and Re(G^3) coefficient
import itertools
rho=mp.mpf('0.01')
vals=[]
for k in range(8):
    phi=2*mp.pi*k/8
    G=rho*mp.e**(1j*phi); vals.append((phi,D(s_of_G(G))-D0))
# fit a|G|^2 + b Re(G^2)+ c Re(G^3) via least squares quick
A=mp.matrix(8,3);y=mp.matrix(8,1)
for i,(phi,v) in enumerate(vals):
    G=rho*mp.e**(1j*phi);A[i,0]=abs(G)**2;A[i,1]=mp.re(G**2);A[i,2]=mp.re(G**3);y[i]=v
sol=mp.lu_solve(A,y)
print('fit |G|^2,Re G^2,Re G^3:',[mp.nstr(x,8) for x in sol],' expected',mp.nstr(-3*mp.sqrt(3)/4,8),0,mp.nstr(mp.sqrt(3)/4,8))
