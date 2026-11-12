# SCRIPT: DERIVED-ALGEBRA (claims 1, 3, 4 and Prop 22.1: exact sympy algebra plus numeric spot checks)
# WHY: each claim is an identity; sympy simplify(lhs-rhs)==0 decides it exactly. Numbers are only spot checks.
# KILL LINE: any identity whose simplified difference is not 0, or any numeric residual above 1e-12, means the claim fails as stated.
import sympy as sp, numpy as np
ok=[]
def chk(name,expr):
    e=sp.simplify(expr); ok.append((name,e==0)); print(('PASS ' if e==0 else 'FAIL ')+name+('' if e==0 else '  residual: '+str(e)))
x=sp.symbols('x',real=True); z,u,k1,k2,E,V1,V2=sp.symbols('z u k1 k2 E V1 V2',positive=True)
# ---- Claim 1: step reflection from continuity of psi and psi'
r,t=sp.symbols('r t')
sol=sp.solve([sp.Eq(1+r,t),sp.Eq(sp.I*k1*(1-r),sp.I*k2*t)],[r,t],dict=True)[0]
print('step: r =',sp.simplify(sol[r]),' t =',sp.simplify(sol[t]))
chk('r=(k1-k2)/(k1+k2)',sol[r]-(k1-k2)/(k1+k2))
# k ~ sqrt(E-V) (hbar=2m=1): energy ratio zE=(E-V2)/(E-V1)
kk1=sp.sqrt(E-V1); kk2=sp.sqrt(E-V2)
zE=sp.symbols('zE',positive=True)
# r in terms of zE: k2/k1=sqrt(zE)
rE=sp.simplify(((1-sp.sqrt(zE))/(1+sp.sqrt(zE))))
chk('r(zE) = -tanh((1/4) ln zE)', (rE+sp.tanh(sp.log(zE)/4)).rewrite(sp.exp))
chk('r(kratio w) = -tanh((1/2) ln w)', ((1-z)/(1+z)+sp.tanh(sp.log(z)/2)).rewrite(sp.exp))
# step in energy ratio has tanh(1/2 ln zE)= (zE-1)/(zE+1): different function
print('z=14.03: tanh(1/2 ln z)=%.6f  tanh(1/4 ln z)=%.6f  (1/2 form = (z-1)/(z+1) = %.6f)'%(np.tanh(np.log(14.03)/2),np.tanh(np.log(14.03)/4),(14.03-1)/(14.03+1)))
# impedance: probability current j=(hbar k/m)|psi|^2 -> Z_Q ~ 1/k or k; light: Z=Z0/n
Z0,n1,n2=sp.symbols('Z0 n1 n2',positive=True)
chk('light: (n1-n2)/(n1+n2) = (Z2-Z1)/(Z2+Z1) with Z=Z0/n', (n1-n2)/(n1+n2)-((Z0/n2-Z0/n1)/(Z0/n2+Z0/n1)))
# Doppler/radar: nu'/nu=(1+b)/(1-b) -> b=(zf-1)/(zf+1) in FREQUENCY (photon energy) ratio, linear dispersion omega=ck so k ratio = energy ratio
b=sp.symbols('b',positive=True)
chk('radar: b=(zf-1)/(zf+1) at zf=(1+b)/(1-b)', ((1+b)/(1-b)-1)/((1+b)/(1-b)+1)-b)
# slab 0<x<d: closed Airy form check done numerically in the package; here the single step only.
# ---- Claim 3: friction weight
tau,chi,D=sp.symbols('tau chi Delta',positive=True)
c=tau/(1+chi**2*tau**2*D**2); w=2*c*D
uu=chi*tau*D; G=(uu-1)/(uu+1)
chk('w = (2/chi) u/(1+u^2), u=chi tau Delta', w-(2/chi)*uu/(1+uu**2))
chk('w = (1/chi)(1-G_u^2)/(1+G_u^2), G_u=(u-1)/(u+1), u LINEAR', w-(1/chi)*(1-G**2)/(1+G**2))
Gq=(uu**2-1)/(uu**2+1)
print('with u squared (G=(u^2-1)/(u^2+1)): (1-G^2)/(1+G^2)-2u/(1+u^2) =',sp.simplify((1-Gq**2)/(1+Gq**2)-2*uu/(1+uu**2)),' (nonzero: the squared variable does NOT give w)')
chk('c/tau = (1-Gamma(u^2))/2  (the k=2 rung)', c/tau-(1-Gq)/2)
chk('w = (1/chi) sech(ln u)', (w-(1/chi)/sp.cosh(sp.log(uu))).rewrite(sp.exp))
chk('mirror: w(u)=w(1/u)', (2*uu/(1+uu**2))-(2*(1/uu)/(1+(1/uu)**2)))
for tb,dd in ((0.5,1),(0.5,4),(0.5,3)):
    uv=tb*dd; print('tau=%.1f Delta=%d: w=%.8f u=%.2f Gamma_u=%.6f'%(tb,dd,2*uv/(1+uv*uv),uv,(uv-1)/(uv+1)))
# ---- Claim 4: Prop 22.2 / 22.3
di,dj=sp.symbols('d_i d_j',positive=True)
Em=(di-dj)**2; Ep=(di+dj)**2; Gm=(di-dj)/(di+dj); zz=di/dj
chk('Gamma=(z-1)/(z+1)=tanh(1/2 ln z)', (Gm-(zz-1)/(zz+1)))
chk('Gamma=tanh(1/2 ln z)', (Gm-sp.tanh(sp.log(zz)/2)).rewrite(sp.exp))
chk('E-/E+ = G^2', Em/Ep-Gm**2)
chk('E-+E+ = 2(di^2+dj^2)', Em+Ep-2*(di**2+dj**2))
chk('E+-E- = 4 di dj', Ep-Em-4*di*dj)
chk('E-/(E-+E+) = G^2/(1+G^2)', Em/(Em+Ep)-Gm**2/(1+Gm**2))
chk('(E+-E-)/E+ = 1-G^2', (Ep-Em)/Ep-(1-Gm**2))
print('half line: solve G^2=1/2, z>1:',[sp.nsimplify(s) for s in sp.solve(sp.Eq(((z-1)/(z+1))**2,sp.Rational(1,2)),z)])
zh=3+2*sp.sqrt(2); Gh=(zh-1)/(zh+1)
chk('z=3+2sqrt2 -> G^2=1/2', Gh**2-sp.Rational(1,2))
chk('z=3+2sqrt2 -> E+=2E-  (E-/E+=1/2)', Gh**2-sp.Rational(1,2))
chk('at G^2=1/2: E-/(E-+E+) = 1/3', (Gh**2)/(1+Gh**2)-sp.Rational(1,3))
print('rim: E-/E+ = G^2 ->1 only as z->inf: limit',sp.limit(((z-1)/(z+1))**2,z,sp.oo),'; for finite positive d, E+-E-=4didj>0 so never exactly equal')
chk('G^2=1/2 <=> 1-G^2=G^2 (echo weight = reflection)', (1-Gh**2)-Gh**2)
chk('G^2=1/2 <=> sinh(tau/2)=1 (tau=ln z)', (sp.sinh(sp.log(zh)/2)-1).rewrite(sp.exp))
# Prop 22.3
Dl1,Dl2,kp=sp.symbols('Delta1 Delta2 k',positive=True)
chk('(D2^k-D1^k)/(D2^k+D1^k)=tanh((k/2) ln z), z=D2/D1', ((Dl2**kp-Dl1**kp)/(Dl2**kp+Dl1**kp)-sp.tanh(kp/2*sp.log(Dl2/Dl1))).rewrite(sp.exp))
oplus=lambda a,bb:(a+bb)/(1+a*bb)
Gs=sp.symbols('G',real=True)
chk('k=2: G(+)G = tanh(ln z)=2G/(1+G^2)', oplus(Gs,Gs)-2*Gs/(1+Gs**2))
Gz=(z-1)/(z+1)
chk('Gamma(z^2)= G(+)G', (z**2-1)/(z**2+1)-oplus(Gz,Gz))
Gz3=(z**3-1)/(z**3+1)
chk('Gamma(z^3)= G(+)G(+)G', Gz3-oplus(oplus(Gz,Gz),Gz))
chk('Gamma(z^-1) = -Gamma(z)', (1/z-1)/(1/z+1)+Gz)
chk('Gamma(z^-2) = (-G)(+)(-G) = -G(+)G', (z**-2-1)/(z**-2+1)-oplus(-Gz,-Gz))
chk('Gamma(z^-2) = -tanh(ln z)', (z**-2-1)/(z**-2+1)+(z**2-1)/(z**2+1))
# general integer k by composition identity tanh(k a)= k-fold (+) of tanh(a): induction step
a=sp.symbols('a',real=True)
chk('induction: tanh((k+1)a)=tanh(ka)(+)tanh(a)', (sp.tanh(3*a)-oplus(sp.tanh(2*a),sp.tanh(a))).rewrite(sp.exp))
# screening: IE ~ Z^2: z=(Zc/Zv)^2, r=(Zc-Zv)/(Zc+Zv)
Zc,Zv=sp.symbols('Zc Zv',positive=True); rr=(Zc-Zv)/(Zc+Zv)
chk('Gamma((Zc/Zv)^2) = r(+)r', ((Zc**2-Zv**2)/(Zc**2+Zv**2))-oplus(rr,rr))
# ---- Prop 22.1 numerics
rng=np.random.default_rng(12)
worst=0
for trial in range(2000):
    n=rng.integers(2,9); kk=rng.integers(1,n)
    X=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); H=(X+X.conj().T)/2
    P=np.zeros((n,n),complex); P[:kk,:kk]=np.eye(kk)
    # random basis change so P is a generic projector
    Q,_=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))); P=Q@P@Q.conj().T
    I=np.eye(n); Bm=P@H@(I-P); com=H@P-P@H
    f=lambda M:np.linalg.norm(M,'fro')**2
    e1=f(Bm); e2=0.5*f(com)
    # block B in the adapted basis: columns of Q
    Hb=Q.conj().T@H@Q; B=Hb[:kk,kk:]; D=Hb[kk:,kk:]; e3=np.trace(B@B.conj().T).real
    # K(0) = B e^{-iD0} B^dagger
    e4=np.trace(B@B.conj().T).real
    worst=max(worst,abs(e1-e2)/e1,abs(e1-e3)/e1,abs(e1-e4)/e1)
print('Prop 22.1: 2000 random Hermitian H (n=2..8, rank k=1..n-1, complex, generic projector): worst relative deviation = %.2e'%worst)
ok.append(('prop22.1 numeric',worst<1e-12))
# block symbolic: [H,P] for P=diag(1,0)
A,Bs,Dm=sp.symbols('A B D',commutative=False)
print('ALL SYMBOLIC/NUMERIC PASS:',all(v for _,v in ok), ' n=',len(ok))
