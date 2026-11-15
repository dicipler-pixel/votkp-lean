# SCRIPT: BALLS-MIXER-LOOP-CHECK-01
# Why this decides it: the mixer draws the square of four joins as the commutator of two disk translations.
# If that matrix is the loop of the reports, its half-trace must equal 1-2q^2, q=(z-1)^2/(4z), the turn at z=5
# must be 3.70918 rad (T8 table), the centre of turn at z=5 must sit at rho^2=1/2 (T11), and the run at z=7 must be 2.955991775.
# Kill line: any of these off by more than 1e-6.
import cmath, math
def mats(z):
    d=math.log(z); c=math.cosh(d/2); s=math.sinh(d/2)
    Tx=[[c,s],[s,c]]; Ty=[[c,1j*s],[-1j*s,c]]
    inv=lambda M:[[M[1][1],-M[0][1]],[-M[1][0],M[0][0]]]
    mul=lambda A,B:[[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    return mul(mul(Tx,Ty),mul(inv(Tx),inv(Ty)))
for z in (3,5,4.6115817893,5.8284271247,7,6.26912766):
    W=mats(z); h=(W[0][0]+W[1][1]).real/2; q=(z-1)**2/(4*z)
    out=[z,h,1-2*q*q]
    if abs(h)<1:
        th=2*math.acos(h); a,b=W[0][0],W[0][1]
        # fixed point of w->(a w+b)/(conj b w+conj a)
        A=b.conjugate(); B=a.conjugate()-a; C=-b
        r=[(-B+sg*cmath.sqrt(B*B-4*A*C))/(2*A) for sg in (1,-1)]; rho=min(abs(x) for x in r)
        out+=['theta',th,'rho2',rho*rho]
    else: out+=['lambda',2*math.acosh(abs(h)), '4acosh(q)',4*math.acosh(q) if q>=1 else None]
    print(out)
