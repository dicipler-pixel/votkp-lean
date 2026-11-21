"""Distance to the real/complex eigenvalue boundary for a reconstructed two-port map."""
from math import sqrt, hypot
from fractions import Fraction as Q
from itertools import product

def multiply(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def inverse(A):
    return [[A[1][1],-A[0][1]],[-A[1][0],A[0][0]]]

def commutator(a,b):
    # The irrational normalization of the second matrix cancels from W.
    A=[[a,0],[0,1]]
    B=[[b+1,b-1],[b-1,b+1]]
    den=4*a*b
    P=multiply(multiply(multiply(A,B),inverse(A)),inverse(B))
    return [[x/den for x in row] for row in P]

def inspect(A):
    a,b=A[0]
    c,d=A[1]
    t=(a+d)/2; u=(a-d)/2; v=(b+c)/2; w=(b-c)/2
    r=hypot(u,v)
    radius=r-abs(w)
    tr=a+d
    delta=(a-d)**2+4*b*c
    assert abs(4*radius*(r+abs(w))-float(delta))<1e-9
    return float(tr),float(delta),radius
if __name__=='__main__':
    z=Q(35,6)
    W=commutator(z,z)
    tr=W[0][0]+W[1][1]
    assert tr==-Q(441,400)-Q(400,441)
    assert W[0][0]*W[1][1]-W[0][1]*W[1][0]==1
    print('35/6 map:',W,'exact eigenvalues −441/400 and −400/441')
    for name,a,b in [('equal',z,z),('Be–Rb',Q('153.896205')/Q('18.21115'),Q('18305.886')/Q('4356.865')),('Si–Ag',Q('8.15168')/Q('1.3895212'),Q('7.576234')/Q('1.30447')),('inside control',Q(4),Q(4))]:
        M=commutator(a,b); tr,delta,r=inspect(M)
        print(name,'trace, discriminant, signed Frobenius clearance, sufficient uniform entrywise tolerance:',*(f'{s:.10f}' for s in (tr,delta,r,abs(r)/2)))
        x,y=M[0];v,w=M[1];t=(x+w)/2;U=float((x-w)/2);V=float((y+v)/2);K=float((y-v)/2)
        R=hypot(U,V); target=(R+abs(K))/2
        for mult in (.99,1.01):
            # Move toward and then through the nearest repeated-eigenvalue matrix.
            P=1+mult*(target/R-1); S=1+mult*(target/abs(K)-1)
            N=[[float(t)+P*U,P*V+S*K],[P*V-S*K,float(t)-P*U]]
            distance=sqrt(sum((float(M[i][j])-N[i][j])**2 for i,j in product(range(2),repeat=2)))
            assert abs(distance-mult*abs(r))<1e-13
            assert (inspect(N)[1]*delta>0)==(mult<1)
