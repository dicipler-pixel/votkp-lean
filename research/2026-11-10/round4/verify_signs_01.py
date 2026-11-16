# SCRIPT: VERIFY-SIGNS-01
# Independent check, by the main worker, of two claims in the second worker's SIGNS_REPORT before they are relayed:
#  (1) Chebyshev identity  tr[a,c^m] - 2 = S_(m-1)(tr c)^2 (tr[a,c] - 2)  for SL(2) (source of the m^2);
#  (2) 89/34 TURNS (it was reported "never" earlier today): a real v with v>0, tr(ab)>2, 0<k<4 solving the group relation
#      at x = ln s = 0.8, k near 0.0083.
# Method for (2) shares no code with either earlier script: the relation w a = b w is built directly from the two-bridge
# word (signs e_i = (-1)^floor(i q/p)), all four matrix entries are evaluated at 120 digits, a root of one entry is bracketed
# in v and then ALL FOUR entries are required to vanish there.  The word convention is validated first on the figure-eight
# (5/3): at v = 0 the relation must hold exactly when s^2 is a root of t^2 - 3t + 1, and must fail at another s.
# KILL: identity remainder nonzero; convention check fails; no bracketed root, or the other entries do not vanish (>1e-80).
import sympy as sp, mpmath as mp
a11,a12,a21,c11,c12,c21=sp.symbols('a11 a12 a21 c11 c12 c21')
def sl2(x,y,z): return sp.Matrix([[x,y],[z,(1+y*z)/x]])
A=sl2(a11,a12,a21); C=sl2(c11,c12,c21); S=[sp.Integer(0),sp.Integer(1)]; tc=C.trace()
for m in range(2,6): S.append(sp.expand(tc*S[-1]-S[-2]))
for m in (1,2,3,4):
    Cm=C**m; lhs=(A*Cm*A.inv()*Cm.inv()).trace()-2; rhs=S[m]**2*((A*C*A.inv()*C.inv()).trace()-2)
    print('(1) m=%d remainder:'%m,sp.simplify(lhs-rhs),'  S_(m-1) at tr c = 2:',sp.simplify(S[m].subs({c11:1,c12:0,c21:0})))
mp.mp.dps=120
def rel(p,q,s,v):
    a=mp.matrix([[s,1],[0,1/s]]); b=mp.matrix([[s,0],[-v,1/s]]); ai=a**-1; bi=b**-1
    w=mp.eye(2)
    for i in range(1,p):
        e=(-1)**((i*q)//p); g=(a if e>0 else ai) if i%2==1 else (b if e>0 else bi); w=w*g
    return w*a-b*w
phi=(3+mp.sqrt(5))/2
r1=rel(5,3,mp.sqrt(phi),mp.mpf(0)); r2=rel(5,3,mp.mpf('1.3'),mp.mpf(0))
print('(2) convention check, figure-eight 5/3 at v=0: residual at s^2 = Alexander root %s ; at s = 1.3 %s'%(mp.nstr(max(abs(x) for x in r1),3),mp.nstr(max(abs(x) for x in r2),3)))
s=mp.e**mp.mpf('0.8'); dM=2-(s**2+s**-2)
f=lambda v:rel(89,34,s,v)[0,1]
vs=[mp.mpf(i)/20000 for i in range(1,400)]; fv=[f(v) for v in vs]; hits=[]
for i in range(len(vs)-1):
    if fv[i]*fv[i+1]<0:
        r=mp.findroot(f,(vs[i],vs[i+1]),solver='anderson',tol=mp.mpf(10)**-100); R=rel(89,34,s,r)
        k=-r*(r+dM); t=s**2+s**-2-r; hits.append((r,k,t,max(abs(x) for x in R)))
for r,k,t,res in hits: print('    89/34 at x=0.8: v = %s  k = %s  tr(ab) = %s  all-entry residual %s'%(mp.nstr(r,25),mp.nstr(k,12),mp.nstr(t,10),mp.nstr(res,3)))
print('    real band points found (v>0, tr>2, 0<k<4, residual<1e-80):',sum(1 for r,k,t,res in hits if r>0 and t>2 and 0<k<4 and res<mp.mpf(10)**-80))
