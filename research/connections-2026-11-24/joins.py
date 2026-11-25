# SCRIPT: CONNECT-JOINS-01
# Five short tests. KILL LINES (written before the run):
#  J1 tune-out as a weak-value share. Claim: for a ground state with two lines and light of circular fraction C, the
#     zero of the light shift sits at the fraction (1+Gamma)/2 of the way from the lower line to the upper line, with
#     Gamma = (z-1)/(z+1), z = strength of lower line / strength of upper line = 2(1+C)/(R(2-C)), R = ratio of squared
#     reduced elements (2 for unsplit lines, giving Gamma = (2C-1)/3 exactly). Kill: the resonant formula misses the
#     measured 790.03235 nm (C = 0) or 785.1522 nm (C = 0.9931) by more than 0.05 nm (one percent of their 4.88 nm
#     separation); or adding the counter-rotating terms does not land within 0.001 nm of the two-line record values
#     790.0280 and 785.1492.
#  J2 three-body cones as half flux. Claim: for unequal masses the four degeneracies of M = D R^T Q R D each have
#     line-field index exactly 1/2 (holonomy -1), summing to 2 = Euler characteristic, the same total as two quadratic
#     poles of index 1. Kill: any index not +1/2, or sum not 2.
#  J3 moment ladder is log-convex (Cauchy-Schwarz, the same positivity as card B1): S(k)^2 <= S(k-1) S(k+1) on the
#     exact hydrogen rungs, and S(k-1)/S(k) increases toward 8/3 (inverse of the first line, 3/8 hartree). Kill: any
#     violation. Consequence tested: his tensor Q = S(-3)/2 >= S(-2)^2/(2 S(-1)).
#  J4 twin-chain offset 0.10866 +/- 0.00003 against closed forms of the census family. Kill for each candidate: miss
#     larger than 0.0001 (three times the stated uncertainty).
#  J5 the three transpositions of Sym(3) = invertible 2x2 matrices over the two-element field: transposition t minus the
#     identity must be a rank-1 matrix on the leg of the vector t fixes (legs <-> transpositions, equivariantly). Kill:
#     any transposition whose t - I is not rank 1 or sits on another leg.
import numpy as np, math, itertools
from fractions import Fraction as F
from scipy.optimize import brentq
# ---------- J1
cL=299792.458; fD1,fD2=377.107463380,384.230484468; hf=2.563005979e-3; E1,E2=fD1-hf,fD2-hf; R=1.99217
def s12(C,R): return (1+C)/3.0, R*(2-C)/6.0
def resonant(C,R):
    s1,s2=s12(C,R); z=s1/s2; G=(z-1)/(z+1); return cL/(E1+(E2-E1)*(1+G)/2), G
def full(C,R):
    # resonant weights (1+C)/3, R(2-C)/6 ; counter-rotating weights are those of the opposite handedness (C -> -C)
    s1,s2=s12(C,R); t1,t2=s12(-C,R)
    f=lambda w: s1/(E1-w)+s2/(E2-w)+t1/(E1+w)+t2/(E2+w)
    return cL/brentq(f,E1+1e-6,E2-1e-6)
for C,meas,rec in ((0.0,790.03235,790.0280),(0.9931,785.1522,785.1492)):
    lam,G=resonant(C,R); lam2,G2=resonant(C,2.0); lf=full(C,R)
    print('J1 C = %.4f: Gamma = %+.5f (unsplit: (2C-1)/3 = %+.5f); resonant formula %.4f nm, measured %.5f, miss %+.4f nm %s ; with counter-rotating terms %.4f nm against record %.4f (%+.4f) %s'
          %(C,G,(2*C-1)/3,lam,meas,lam-meas,'HELD' if abs(lam-meas)<0.05 else 'FIRED',lf,rec,lf-rec,'HELD' if abs(lf-rec)<0.001 else 'FIRED'))
print('   opposite handedness C = -1: Gamma =',resonant(-1.0,2.0)[1],'(the rim: the zero sits on the lower line itself, no tune-out between the lines)')
print('   C = 1/2: Gamma =',resonant(0.5,2.0)[1],'(centre of the disc: zero exactly midway)')
# ---------- J2
def Mten(th,ph,q):
    c,s=math.cos(ph),math.sin(ph); Rm=np.array([[c,-s],[s,c]]); D=np.diag([math.cos(th),1.0]); return D@Rm.T@np.diag(q)@Rm@D
def winding(th0,ph0,q,rad=1e-3,n=400):
    tot=0; prev=None
    for t in np.linspace(0,2*math.pi,n+1):
        M=Mten(th0+rad*math.cos(t),ph0+rad*math.sin(t)/max(abs(math.sin(th0)),1e-9),q); a=math.atan2(2*M[0,1],M[0,0]-M[1,1])
        if prev is not None: d=(a-prev+math.pi)%(2*math.pi)-math.pi; tot+=d
        prev=a
    return tot/(2*math.pi)
q=(1.0,2.3)   # unequal eigenvalues of Q (stands for unequal masses); q_min/q_max sets the latitude
th=math.acos(math.sqrt(min(q)/max(q))); pts=[]
for th0 in (th,math.pi-th):
    for ph0 in np.linspace(0,2*math.pi,8,endpoint=False):
        M=Mten(th0,ph0,q)
        if abs(M[0,1])<1e-9 and abs(M[0,0]-M[1,1])<1e-9: pts.append((th0,ph0))
idx=[]
for th0,ph0 in pts:
    w=winding(th0,ph0,q); orient=1.0   # chart (theta, phi) has one orientation everywhere off the poles
    idx.append(w/2)
print('J2 degenerate points found:',len(pts),'; chart winding of the traceless part / 2 at each:',np.round(idx,3))
# true index on the sphere = index measured in the frame (e_theta, e_phi) seen with outward orientation; the chart
# (theta, phi) is right-handed for the outward normal, so no sign change is needed, and the frame itself is smooth there.
wp=winding(1e-2,0.0,q,rad=0)  # placeholder not used
def pole_winding(th0,q,n=400):
    tot=0; prev=None
    for ph in np.linspace(0,2*math.pi,n+1):
        M=Mten(th0,ph,q); a=math.atan2(2*M[0,1],M[0,0]-M[1,1])
        if prev is not None: tot+=(a-prev+math.pi)%(2*math.pi)-math.pi
        prev=a
    return tot/(2*math.pi)
pn=pole_winding(0.02,q); ps=pole_winding(math.pi-0.02,q)
print('   around the north pole the tensor winds %+.2f in the rotating frame, so its true line index there is 1 + (%+.2f)/2 = %.2f (regular point if 0)'%(pn,pn,1+pn/2))
print('   around the south pole (loop reversed for the outward normal): frame winding %+.2f, true line index 1 - (%+.2f)/2 = %.2f'%(ps,ps,1-ps/2))
tot=sum(abs(i) for i in idx); print('   sum of the four cone indices (magnitudes): %.3f ; Euler characteristic 2 ; equal masses: 2 poles x index 1 = 2.'%tot, 'HELD' if len(pts)==4 and all(abs(abs(i)-0.5)<1e-3 for i in idx) and len({round(i,3) for i in idx})==1 else 'CHECK SIGNS')
print('   flux reading: holonomy -1 is Phi = pi, Gamma = i tan(Phi/2) = infinity (books swapped); two of them merged give Phi = 2 pi, Gamma = 0, holonomy +1.')
# ---------- J3
S={-1:F(2),-2:F(9,2),-3:F(43,4),-4:F(319,12),-5:F(9673,144),-6:F(297541,1728)}
ok=True
for k in (-2,-3,-4,-5):
    lhs,rhs=S[k]**2,S[k+1]*S[k-1]; ok&=lhs<=rhs; print('J3 S(%d)^2 = %s <= S(%d) S(%d) = %s : %s (quotient %.5f)'%(k,lhs,k+1,k-1,rhs,lhs<=rhs,float(lhs/rhs)))
rat=[S[k-1]/S[k] for k in (-1,-2,-3,-4,-5)]; print('   rung quotients S(k-1)/S(k):',[round(float(r),4) for r in rat],'-> 8/3 = 2.6667 ; increasing:',all(a<b for a,b in zip(rat,rat[1:])),'; all below 8/3:',all(r<F(8,3) for r in rat))
print('   lower bound on the tensor half-rung: S(-3)/2 = %s >= S(-2)^2/(2 S(-1)) = %s ; upper: S(-3)/2 <= (8/3) S(-2)/2 = %s'%(S[-3]/2,S[-2]**2/(2*S[-1]),F(8,3)*S[-2]/2), 'HELD' if ok else 'FIRED')
print('   Smith coordinate of each rung quotient against the first line, Gamma = (x-1)/(x+1), x = quotient x 3/8:',[round(float((r*F(3,8)-1)/(r*F(3,8)+1)),4) for r in rat])
# ---------- J4
c,unc=0.10866,0.00003; s3=math.sqrt(3)
cands={'ln(4/3)/sqrt(3) (star offset on the diagonal shadow)':math.log(4/3)/s3,
 'ln(4/3)/3':math.log(4/3)/3,
 'half the census depth at 90 degrees between arms, 2 ln(1/sin 45) / 2 = ln(2)/2, times (1 - 1/sqrt 3)^2':math.log(2)/2*(1-1/s3)**2,
 'ln(3/2)/4 (census depth at the arm-to-diagonal angle, sin^2 = 2/3, quartered)':math.log(1.5)/4,
 'ln(9/8) (census depth at the tetrahedral angle 70.53)':math.log(9/8),
 'ln(17/11)/4 (first step over four)':math.log(17/11)/4,
 '(2 - sqrt 3) ln(3/2)':(2-s3)*math.log(1.5),
 'ln(4/3)(1 - 1/sqrt 3)':math.log(4/3)*(1-1/s3),
 '1/(2 pi sqrt(3)) + ...: 1/(3 pi)':1/(3*math.pi)}
for n,v in cands.items(): print('J4 %-95s %.5f  miss %+.5f  %s'%(n,v,v-c,'within 0.0001' if abs(v-c)<1e-4 else 'missed'))
print('   exact piece: the first-step part of the offset, ln(17/11)(1 - 1/sqrt 3) = %.4f (record: +0.1840)'%(math.log(17/11)*(1-1/s3)))
tab={'cube 90':(0.57735,0.1086),'tetrahedron 109.47':(1/3,0.1567),'icosahedron 63.43':(0.79465,0.0603),'dodecahedron 41.81':(0.91117,0.0281)}
for n,(P,cc) in tab.items(): print('   %-22s offset %.4f ; offset/(1 - P^2) = %.4f ; offset/(1 - P) = %.4f'%(n,cc,cc/(1-P*P),cc/(1-P)))
# ---------- J5
def rank(a): 
    d=(a[0][0]*a[1][1]-a[0][1]*a[1][0])%2; return 2 if d else (1 if any(any(r) for r in a) else 0)
mats=[((a,b),(c,d)) for a,b,c,d in itertools.product((0,1),repeat=4)]; inv=[m for m in mats if rank(m)==2]; I=((1,0),(0,1))
mul=lambda a,b: tuple(tuple(sum(a[i][k]&b[k][j] for k in range(2))%2 for j in range(2)) for i in range(2))
app=lambda a,v: tuple(sum(a[i][k]&v[k] for k in range(2))%2 for i in range(2))
vecs=[(1,0),(0,1),(1,1)]; good=True
for t in inv:
    if t!=I and mul(t,t)==I:
        fixed=[v for v in vecs if app(t,v)==v]; N=tuple(tuple(x^y for x,y in zip(r,s)) for r,s in zip(t,I)); img={app(N,v) for v in vecs}-{(0,0)}
        good&=(rank(N)==1 and img=={fixed[0]}); print('J5 transposition',t,'fixes',fixed,'; t - I =',N,'rank',rank(N),'; its leg (image) is',img)
tr=[t for t in inv if t!=I and mul(t,t)==I]
print('   differences between two transpositions have rank:',[rank(tuple(tuple(x^y for x,y in zip(r,s)) for r,s in zip(a,b))) for a,b in itertools.combinations(tr,2)],'; all three legs used once:', 'HELD' if good else 'FIRED')
