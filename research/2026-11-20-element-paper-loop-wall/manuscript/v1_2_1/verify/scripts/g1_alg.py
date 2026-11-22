# SCRIPT: G1_ALGEBRA_RECOMPUTE
# Independent recomputation of the algebraic identities and numbers in 00_front, 01_opening, 02_wall, 03_criterion, 07_ledgers.
import sympy as sp, mpmath as mp, numpy as np, gzip, json, math
mp.mp.dps = 50
z, G, h, a, b = sp.symbols('z G h a b', positive=True)
# 1 Smith identity and inverse
print('1 Gamma=tanh(h/..)', sp.simplify(((z-1)/(z+1)) - sp.tanh(sp.log(z)/2).rewrite(sp.exp)))
print('1 inverse z=(1+G)/(1-G)', sp.simplify((1+(z-1)/(z+1))/(1-(z-1)/(z+1)) - z))
# 2 wall quadratic
print('2 G^2=1/2 <=> z^2-6z+1=0:', sp.factor(sp.together(((z-1)/(z+1))**2 - sp.Rational(1,2))))
print('2 roots', sp.solve(z**2-6*z+1, z), float(3+2*sp.sqrt(2)))
# 3 commutator trace of two perpendicular boosts, mixed and equal
def boost(h, ax):
    s = {'x': np.array([[0,1],[1,0]]), 'z': np.array([[1,0],[0,-1]])}[ax]
    w, v = np.linalg.eigh(s); return v @ np.diag(np.exp(h*w)) @ v.T
worst = 0
for ha, hb in [(0.3,0.9),(1.1,0.4),(0.8814,0.8814),(1.5,1.5)]:
    A, B = boost(ha,'z'), boost(hb,'x')
    W = A@B@np.linalg.inv(A)@np.linalg.inv(B)
    worst = max(worst, abs(np.trace(W) - (2-4*np.sinh(ha)**2*np.sinh(hb)**2)))
print('3 trW=2-4 sinh^2 ha sinh^2 hb, worst', worst)
# equal faces tr W = 2-4 sinh^4(r/2) = 2-4 (R/T)^2, and Jordan at wall
r = mp.log(3+2*mp.sqrt(2)); hh = r/2
A = np.array(boost(float(hh),'z')); B = np.array(boost(float(hh),'x'))
W = A@B@np.linalg.inv(A)@np.linalg.inv(B); I2 = np.eye(2)
print('3 wall: trW', np.trace(W), ' (W+1)^2 norm', np.linalg.norm((W+I2)@(W+I2)), ' W+1 norm', np.linalg.norm(W+I2))
for zz in [3.0, 5.0, 7.0]:
    Gm = (zz-1)/(zz+1); R = Gm**2; T = 1-R
    A = np.array(boost(math.log(zz)/2,'z')); B = np.array(boost(math.log(zz)/2,'x'))
    W = A@B@np.linalg.inv(A)@np.linalg.inv(B)
    print('   z=%g trW %.9f  2-4(R/T)^2 %.9f  K=1/(1-2G^2)=%.6f' % (zz, np.trace(W), 2-4*(R/T)**2, 1/(1-2*R)))
# 4 sum/product forms
x, y, t = sp.symbols('x y t', positive=True)
print('4 (1-x)(1-y)-xy = 1-(x+y):', sp.simplify((1-x)*(1-y)-x*y-(1-(x+y))))
tt = sp.Rational(5005,10000); xx = sp.Rational(9999,10000); yy = sp.Rational(5,10000)
print('4 t=.5005 x=.9999 y=.0005: sum form closed?', xx+yy < 2*tt, ' product form closed?', xx*yy*(1-tt)**2 < tt**2*(1-xx)*(1-yy))
# 5 apex
L = mp.log(3+2*mp.sqrt(2)); ap = mp.tanh(L/4)
print('5 apex at wall', ap, mp.sqrt(2)-1, ' 1-a^2', 1-ap**2, 2*(mp.sqrt(2)-1))
print('5 G=2a/(1+a^2) at wall', 2*ap/(1+ap**2), mp.sqrt(2)/2)
# 6 numbers
print('6 ln(3+2sqrt2)=', L, ' 2 ln(1+sqrt2)=', 2*mp.log(1+mp.sqrt(2)), ' 2 asinh 1=', 2*mp.asinh(1))
print('6 3+2sqrt2=', 3+2*mp.sqrt(2))
print('6 5,7: G=', mp.mpf(4)/6, mp.mpf(6)/8, ' product', mp.mpf(4)/6*mp.mpf(6)/8)
print('6 midpoint example 3,7: mid 5 halfgap 2 Gamma', (7-3)/(7+3), 2/5)
# 7 Catalan
Gint = mp.quad(lambda g: 2*mp.atanh(g)/(1+g**2), [0,1])
print('7 integral', Gint, ' Catalan', mp.catalan, ' diff', Gint-mp.catalan)
rt = 17+12*mp.sqrt(2)
print('7 (3+2sqrt2)^2', (3+2*mp.sqrt(2))**2, rt, ' Gamma(root)', (rt-1)/(rt+1), 2*mp.sqrt(2)/3, ' tanh(2 asinh1)', mp.tanh(2*mp.asinh(1)))
print('7 psi: Gamma=tan(psi/2), wall cos psi', (1-0.5)/(1+0.5), ' sec', (1+0.5)/(1-0.5))
# 8 speed limit trajectory
Om = 1.3
print('8 pi/(8 Om)=', math.pi/(8*Om), ' 2 sqrt(Om^2)=', 2*math.sqrt(Om**2))
# 9 Offset algebra
nu = sp.symbols('nu', positive=True)
zz = (1-nu)/nu; Gm = (zz-1)/(zz+1)
print('9 Gamma=1-2nu', sp.simplify(Gm-(1-2*nu)), ' nu(1-nu)-(1-G^2)/4', sp.simplify(nu*(1-nu)-(1-Gm**2)/4), ' S-4/(1-G^2)', sp.simplify(1/(nu*(1-nu))-4/(1-Gm**2)))
print('9 wall: nu(1-nu)=', sp.Rational(1,8), ' S=', 4/(1-sp.Rational(1,2)))
# Rice-Mele
t1,t2,v = sp.symbols('t1 t2 v', positive=True)
Emin2 = v**2+(t1-t2)**2; Emax2 = v**2+(t1+t2)**2
print('9 RM: 2Emin2-Emax2 =', sp.expand(2*Emin2-Emax2), ' (= t1^2+t2^2+v^2-6 t1 t2?)', sp.expand(2*Emin2-Emax2-(t1**2+t2**2+v**2-6*t1*t2)))
tt_=1; vv=sp.symbols('vv', positive=True)
sol = sp.solve(sp.Eq(2*(vv**2) , vv**2+4*tt_**2), vv)  # equal hopping t: 2 Emin^2 = Emax^2 -> k_e^2=1/2
print('9 RM equal hopping, k_e^2=1/2 at v=', sol, ' 2/sqrt3=', 2/math.sqrt(3))
print('9 gamma^2=1/2 (equal hopping gamma^2=k_e=Emin/Emax) => Emax=2Emin: v^2+4t^2=4v^2 -> v=', math.sqrt(4/3))
print('9 K(1/2)/K(1/2) spacing: 4*pi=', 4*mp.pi, ' via ellipk:', 4*mp.pi*mp.ellipk(mp.mpf(1)/2)/mp.ellipk(1-mp.mpf(1)/2))
# 10 anion S0 etc
d = json.load(gzip.open('/home/claude/votkp-lean/data/element_thresholds_20261011.json.gz')); rec = {r['Z']: r for r in d['records']}
def I0(sym):
    for r in rec.values():
        if r['symbol']==sym: return [x['IE_eV'] for x in sorted(r['thresholds'], key=lambda x:x['q'])][0]
for sym, EA in [('Ag',1.30447),('Si',1.3895212)]:
    I = I0(sym); S0 = (I+EA)**2/(I*EA); G0 = (I-EA)/(I+EA)
    print('10', sym, 'S0=%.4f 4/(1-G0^2)=%.4f z0=I/EA=%.5f' % (S0, 4/(1-G0**2), I/EA))
print('10 francium threshold', 4.072741*(3+2*math.sqrt(2)))
# 11 IQGT: Tr(Pi V W) = g - (i/2) Omega with g=1/2 Tr(VW), Omega = i Tr(Pi[V,W]) on random tangents
rng = np.random.default_rng(1)
n,k = 5,2
M = rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); H = M+M.conj().T
w,U = np.linalg.eigh(H); P = U[:,:k]@U[:,:k].conj().T
def tang():
    X = rng.normal(size=(k,n-k))+1j*rng.normal(size=(k,n-k))
    Uo, Un = U[:,:k], U[:,k:]
    return Uo@X@Un.conj().T + Un@X.conj().T@Uo.conj().T
V, Wt = tang(), tang()
Q = np.trace(P@V@Wt); g = 0.5*np.trace(V@Wt); Om = 1j*np.trace(P@(V@Wt-Wt@V))
print('11 Q - (g - i/2 Omega) =', abs(Q-(g-0.5j*Om)))
gVV = 0.5*np.trace(V@V).real; gWW = 0.5*np.trace(Wt@Wt).real
print('11 |Omega| <= 2 sqrt(gVV gWW - gVW^2):', abs(Om), 2*math.sqrt(gVV*gWW-g.real**2))
# 12 criterion: J^dag A^2 J - (J^dag A J)^2 = (QAJ)^dag QAJ
A = rng.normal(size=(5,5))+1j*rng.normal(size=(5,5)); A = A+A.conj().T
J = np.linalg.qr(rng.normal(size=(5,2))+1j*rng.normal(size=(5,2)))[0]; Qm = np.eye(5)-J@J.conj().T
lhs = J.conj().T@A@A@J-(J.conj().T@A@J)@(J.conj().T@A@J); rhs = (Qm@A@J).conj().T@(Qm@A@J)
print('12 defect identity residual', np.linalg.norm(lhs-rhs))
S = np.array([[0,1],[1,0]]); J1 = np.array([[1],[0]])
print('12 swap: retained A', (J1.T@S@J1)[0,0], ' retained A^2', (J1.T@S@S@J1)[0,0])
# 13 observability: autonomous iff L kerR in kerR; unobservable = ker of stacked R L^j
L = rng.normal(size=(4,4)); R = rng.normal(size=(2,4))
Ob = np.vstack([R@np.linalg.matrix_power(L,j) for j in range(4)])
ns = np.linalg.svd(Ob)[2][np.linalg.matrix_rank(Ob):]
print('13 generic: unobservable dim', ns.shape[0])
# make non-generic: R kills an invariant subspace
ev, V4 = np.linalg.eig(L); v1 = V4[:,0].real if abs(ev[0].imag)<1e-12 else None
# 14 Hidden block Laplace correction: check numerically  u'=Au+Bv, v'=Cu+Dv  via transfer function
A_=rng.normal(size=(2,2)); B_=rng.normal(size=(2,2)); C_=rng.normal(size=(2,2)); D_=rng.normal(size=(2,2))
Hf = np.block([[A_,B_],[C_,D_]]); zeta = 2.7+0.3j
full = np.linalg.inv(zeta*np.eye(4)-Hf)[:2,:2]
red = np.linalg.inv(zeta*np.eye(2)-A_-B_@np.linalg.inv(zeta*np.eye(2)-D_)@C_)
print('14 resolvent: (zeta-A-B(zeta-D)^-1 C)^-1 equals block of full resolvent:', np.linalg.norm(full-red))
# 15 time-domain integral eq via expm numerical check
from scipy.linalg import expm
u0=rng.normal(size=2); v0=rng.normal(size=2); tT=0.8
def sol(t): 
    return expm(Hf*t)@np.concatenate([u0,v0])
tgrid=np.linspace(0,tT,2001); us=np.array([sol(t)[:2] for t in tgrid])
integrand=np.array([B_@expm(D_*(tT-s))@C_@us[i] for i,s in enumerate(tgrid)])
integ=np.trapezoid(integrand,tgrid,axis=0)
du_formula = A_@us[-1]+B_@expm(D_*tT)@v0 if False else A_@us[-1]+B_@expm(D_*tT)@v0+integ
du_true = (Hf@sol(tT))[:2]
print('15 u-dot integral formula error', np.linalg.norm(du_formula-du_true))
# 16 E_B vs connection energy E- on one edge
di, dj, bb = 5.0, 2.0, 0.7
Hh = np.array([[di,bb],[bb,dj]]); Pp = np.array([[1,0],[0,0]])
EB = np.linalg.norm(Pp@Hh@(np.eye(2)-Pp))**2; comm = Hh@Pp-Pp@Hh
print('16 E_B=||PH(1-P)||^2 =', EB, ' (1/2)||[H,P]||^2 =', 0.5*np.linalg.norm(comm)**2, ' vs connection book (di-dj)^2 =', (di-dj)**2)
# 17 literal shift of every IONISATION energy vs shift of charge-state energies (Matter at a Scale sentence)
rec6 = rec[6]; E6 = [x['IE_eV'] for x in sorted(rec6['thresholds'], key=lambda x:x['q'])]
a_, b_ = E6[3], E6[4]; c_ = 5.0
print('17 carbon step 4 Gamma', (b_-a_)/(b_+a_), ' after IE->IE+5 for every IE:', ((b_+c_)-(a_+c_))/((b_+c_)+(a_+c_)), ' G^2', ((b_-a_)/(b_+a_))**2, (((b_+c_)-(a_+c_))/((b_+c_)+(a_+c_)))**2)
# 18 count anions Z<=55 in the source EA list (44 claim)
import re
src = open('/home/claude/votkp-lean/research/2026-11-20-element-paper-loop-wall/connections/checks_rate/check_rate_01_logodds_peel.py').read()
m = re.search(r"EA = \{(.*?)\}", src, re.S); n = len(re.findall(r"'[A-Z][a-z]?'\s*:", m.group(1)))
print('18 anions in rate_01 EA table (H..Cs):', n)
pt = json.load(open('/home/claude/votkp-lean/research/2026-11-20-element-paper-loop-wall/ptable/ptable_data.json'))['elements']
print('18 ptable anions with Z<=55:', sum(1 for e in pt if e.get('anion') and e['Z']<=55))
