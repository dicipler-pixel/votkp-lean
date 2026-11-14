# SCRIPT: CHK-01-BALL (independent ball math: Thomas, commutator, line, K/P, freeness residues, levels, strip, closing steps)
import numpy as np, math
from fractions import Fraction as F
np.set_printoptions(precision=10, suppress=True)
def boost(u, r):
    u = np.array(u, float); c, s = math.cosh(r), math.sinh(r)
    B = np.zeros((4,4)); B[0,0]=c; B[0,1:]=s*u; B[1:,0]=s*u
    B[1:,1:] = np.eye(3) + (c-1)*np.outer(u,u); return B
I = [1,0,0]; J=[0,1,0]; K=[0,0,1]
gam = lambda z: (z-1)/(z+1)
print("== A. line and Gamma")
z = 3+2*math.sqrt(2); print("Gamma^2 at 3+2sqrt2 =", gam(z)**2, " 5:", gam(5)**2, "7:", gam(7)**2)
print("== B. Thomas rotation of B_i B_j: tan(theta/2) vs Gamma^2")
def thomas(z):
    r = math.log(z); M = boost(I,r) @ boost(J,r)
    # polar: M = L R, R rotation; spatial block of M^T? use M = L R with L symmetric positive
    # R fixes time axis: L = M R^-1 ; find via polar of 3x3 after boosting: use SVD-free method
    S = M @ M.T  # = L^2
    w, V = np.linalg.eigh(S); L = V @ np.diag(np.sqrt(w)) @ V.T
    R = np.linalg.inv(L) @ M
    ang = math.acos(max(-1,min(1,(np.trace(R[1:,1:])-1)/2)))
    return R, ang
for zz in (5,7,2,3):
    R, ang = thomas(zz); G2 = gam(zz)**2
    print(zz, "theta deg", math.degrees(ang), " 2atan(Gamma^2) deg", math.degrees(2*math.atan(G2)), " cos", math.cos(ang), " (1-G4)/(1+G4)", (1-G2**2)/(1+G2**2))
print("exact cos z=5:", F(65,97), float(F(65,97)), " z=7:", F(175,337), float(F(175,337)))
print("== C. commutator [B_i,B_j]")
def comm(z, a=I, b=J):
    r=math.log(z); A=boost(a,r); B=boost(b,r); return A@B@np.linalg.inv(A)@np.linalg.inv(B)
for zz in (5,7,2,3,6):
    C = comm(zz); tr4 = np.trace(C); g = (zz-1)**2/(4*zz)  # g = sinh^2(r/2) for equal steps
    print(zz, "tr4", tr4, " (2-4g^2)^2", (2-4*g*g)**2, " 2x2 trace 2-4g^2", 2-4*g*g)
C = comm(5); print("cos phi from 4x4 trace (tr-2)/2 =", (np.trace(C)-2)/2, " vs -527/625 =", -527/625, " phi deg", math.degrees(math.acos((np.trace(C)-2)/2)))
# fixed point: vector p with C p = p, timelike
w, V = np.linalg.eig(C); idx = np.argmin(abs(w-1)); 
# eigenspace of eigenvalue 1 is 2D (p and axis); find timelike combination
N = np.linalg.svd(C-np.eye(4))[2][-2:]
best=None
for t in np.linspace(0,math.pi,2000):
    v = math.cos(t)*N[0]+math.sin(t)*N[1]; q = v[0]**2-v[1]**2-v[2]**2-v[3]**2
    if q>1e-6: best=v/math.sqrt(q); break
if best[0]<0: best=-best
print("fixed point p", best, " cosh rho", best[0], " rho", math.acosh(best[0]), " ln(3+2sqrt2)", math.log(3+2*math.sqrt(2)), " ball radius^2", (math.tanh(math.acosh(best[0])/2))**2)
# max distance over orbit n<=400
x = np.array([1.,0,0,0]); mx=0
for n in range(400):
    x = C@x; mx=max(mx, math.acosh(max(1,x[0])))
print("max d(o,C^n o) n<=400:", mx, " 2rho:", 2*math.acosh(best[0]))
C7 = comm(7); print("z=7 4x4 trace", np.trace(C7), "51076/2401=", 51076/2401, " tau", math.acosh((np.trace(C7)-2)/2), " 4*acosh(9/7)", 4*math.acosh(9/7))
print("trace at line 2x2 (2-4g^2), g=(z-1)^2/4z:", 2-4*(((z-1)**2/(4*z))**2))
print("== D. K and P (R3)")
for zz in (3,5):
    R = gam(zz)**2; print(zz, "R",R,"T",1-R,"P=2R",2*R,"K=1/(1-2R)",1/(1-2*R), " 1/(T-R)",1/((1-R)-R), " sin^2phi_k=2R", 2*R, " rho^2=(1-s)/(1+s)", (1-math.sqrt(1-2*R))/(1+math.sqrt(1-2*R)))
print("== E. freeness residues mod 5, mod 7 and no identity, depth<=6 (integer boosts)")
def Bint(z, d, sg):
    n = z*z+1; m = z*z-1  # scale 2z : cosh*2z = z^2+1, sinh*2z = z^2-1
    M = [[0]*4 for _ in range(4)]; M[0][0]=n; M[0][d+1]=sg*m; M[d+1][0]=sg*m
    for i in range(3):
        for j in range(3):
            M[i+1][j+1] = (2*z if i==j else 0) + (0 if True else 0)
    for i in range(3):
        M[i+1][i+1] = 2*z
    M[d+1][d+1] = n
    return M
def mmul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
for z in (5,7):
    gens = [(d,sg,Bint(z,d,sg)) for d in range(3) for sg in (1,-1)]
    viol=0; ident=0; cnt=0
    frontier=[(None,None,[[1 if i==j else 0 for j in range(4)] for i in range(4)])]
    for depth in range(1,7 if z==5 else 6):
        nf=[]
        for last,_,M in frontier:
            for (d,sg,G) in gens:
                if last is not None and last==(d,-sg): continue
                P = mmul(M,G); cnt+=1
                if P[0][0] % z == 0: viol+=1
                # identity up to scale?
                s=P[0][0]
                if all(P[i][j]==(s if i==j else 0) for i in range(4) for j in range(4)): ident+=1
                nf.append(((d,sg),0,P))
        frontier=nf
    print("z",z,"words checked",cnt,"a00 divisible by z:",viol," scalar matrices:",ident)
print("== F. level shells Gamma_L=(5^L-1)/(5^L+1), and straight 3-step point")
print([ (L, (5**L-1)/(5**L+1)) for L in range(1,5)], " Fraction 3-step cosh:", F(7813,125), " sinh", F(7812,125))
print("== G. strip transfer Gamma^2=(tr-2)/(tr+2), tr=4-mu")
for mu in (0,1,1.5): tr=4-mu; print("mu",mu,"Gamma^2",(tr-2)/(tr+2))
print("Gamma^2=1/2 at |tr|=",(2+2*0.5)/(1-0.5), " kappa=2ln(1+sqrt2)=", 2*math.log(1+math.sqrt(2)), " acosh(3)=", math.acosh(3))
print("strip 1xn mu_min = 4-2cos(pi/(n+1)): n=3", 4-2*math.cos(math.pi/4), " n=34", 4-2*math.cos(math.pi/35))
print("== H. closing steps q=cos(2pi/n), z=(sqrt q+sqrt(1+q))^2, Gamma^2=q/(1+q)")
for n in (5,6,8,10,12):
    q=math.cos(2*math.pi/n); zz=(math.sqrt(q)+math.sqrt(1+q))**2; print(n, zz, "q check (z-1)^2/4z", (zz-1)**2/(4*zz), "q", q, "Gamma^2", gam(zz)**2, q/(1+q))
