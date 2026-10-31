# SCRIPT: COMMUTATOR_TYPE
# KILL CONDITION (written before the run): the claim "T = 2 - 4 sinh^4(ln z/2) is the SL2 trace of [B_i,B_j]" is dead if
# the exact 4x4 trace of the commutator differs from T^2 (trace of the Hermitian-matrix representation of an SL2 element
# with real trace T is T^2 in the hyperbolic case and 2+2cos(2 theta)=T^2 also in the elliptic case, since 2+2cos2th=4cos^2 th).
# Finite order is DECIDED by: SL2 trace T is an algebraic integer if the element has finite order (eigenvalue a root of unity);
# T rational and not an integer therefore => infinite order.  Rotation angle phi: cos(phi)=T^2/2-1; by Niven, rational cos of a
# rational multiple of pi lies in {0,+-1/2,+-1}.
from fractions import Fraction as Fr
import itertools
def boost(z,a,sg):
    c=Fr(z*z+1,2*z); s=sg*Fr(z*z-1,2*z)
    B=[[Fr(int(i==j)) for j in range(4)] for i in range(4)]
    B[0][0]=c;B[a][a]=c;B[0][a]=s;B[a][0]=s
    return B
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def tr(A): return sum(A[i][i] for i in range(4))
def inv(z,a,sg): return boost(z,a,-sg)
for z in (2,4,8,16):
    print("=== z =",z)
    T=2-Fr((z-1)**4,4*z*z)      # 2 - 4 sinh^4(ln z /2),  sinh(ln z/2)=(z-1)/(2 sqrt z)
    print(" claimed SL2 trace of commutator T =",T,"=",float(T))
    seen={}
    for (a,sa,b,sb) in itertools.product((1,2,3),(1,-1),(1,2,3),(1,-1)):
        if a>=b: continue
        A=boost(z,a,sa);B=boost(z,b,sb)
        C=mm(mm(A,B),mm(inv(z,a,sa),inv(z,b,sb)))
        t4=tr(C)
        seen.setdefault(t4,[]).append((a,sa,b,sb))
    for t4,l in seen.items():
        print("  4x4 trace of [B_a^sa,B_b^sb] =",t4,"=",float(t4),"  (#pairs with this value:",len(l),") equals T^2?",t4==T*T)
    t4=list(seen.keys())[0]
    # decide type using the T of the standard commutator [B_i,B_j]
    A=boost(z,1,1);B=boost(z,2,1);C=mm(mm(A,B),mm(inv(z,1,1),inv(z,2,1)))
    t4=tr(C); print(" [B_i,B_j] 4x4 trace =",t4,"T^2 =",T*T,"match:",t4==T*T)
    if abs(T)<2:
        cphi=T*T/2-1
        print(" ELLIPTIC (|T|<2): rotation angle phi with cos(phi) = T^2/2-1 =",cphi,"=",float(cphi))
        import math
        print("  phi (rad) =",math.acos(float(cphi)),"  phi/pi =",math.acos(float(cphi))/math.pi)
        print("  T =",T,"is rational, denominator",T.denominator,"=> not an algebraic integer => eigenvalue e^{i phi/2} is not a root of unity => INFINITE order")
        print("  2cos(phi) =",2*cphi,"denominator",(2*cphi).denominator,": not an integer, so phi is not a rational multiple of pi (Niven / algebraic-integer test)")
        print("  e^{i phi/2} is root of x^2 - T x + 1 =",T.numerator,"/",T.denominator,": x^2-(%s)x+1"%T)
        # also: 2cos(phi/2)=T must be algebraic integer for finite order
    else:
        import math
        lam=(float(T)+math.sqrt(float(T)**2-4))/2
        print(" HYPERBOLIC/LOXODROMIC (|T|>2), real trace; |eigenvalue| =",abs(lam),", translation length 2 |ln|lambda|| =",2*abs(math.log(abs(lam)))," -> infinite order")
    # other commutator traces (sign variants) summarized above
    # Thomas rotation of B_i B_j
    A=boost(z,1,1);B=boost(z,2,1);P=mm(A,B)
    print(" tr(B_i B_j) (4x4) =",tr(P)," Thomas rotation cos(theta)=4z(z^2+1)/(z^4+6z^2+1)=",Fr(4*z*(z*z+1),z**4+6*z*z+1))
