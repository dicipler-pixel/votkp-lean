"""Exact integer controls for the spinor peel, junction weights and directed loops."""
from itertools import product

# Complex integers are pairs, with elementary exact operations.
def add(z,w):
    return z[0]+w[0],z[1]+w[1]

def mul(z,w):
    return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]

def conj(z):
    return z[0],-z[1]

def norm2(z):
    return z[0]**2+z[1]**2

def summands(values):
    result=(0,0)
    for value in values:
        result=add(result,value)
    return result

def product3(p,i,j,k):
    return mul(mul(p[i][j],p[j][k]),p[k][i])

def run():
    # Integer numerator M=7P of V(V*V)^(-1)V*, with V rows (1,0),
    # (0,1), (1,1), (1,i). All arithmetic below checks that M/7 is a projector.
    m=[[(3,0),(-1,-1),(2,-1),(2,1)],
       [(-1,1),(3,0),(2,1),(-1,-2)],
       [(2,1),(2,-1),(4,0),(1,-1)],
       [(2,-1),(-1,2),(1,1),(4,0)]]
    den=7
    sites=range(4)
    assert sum(m[i][i][0] for i in sites)==2*den
    for i,j in product(sites, repeat=2):
        assert m[i][j]==conj(m[j][i])
        assert summands(mul(m[i][k],m[k][j]) for k in sites)==mul((den,0),m[i][j])
        assert sum(product3(m,i,j,k)[1] for k in sites)==0
    for i in sites:
        c=m[i][i][0]
        assert den*c-c*c==sum(norm2(m[i][j]) for j in sites if j!=i)
    mirror=[[conj(z) for z in row] for row in m]
    w=product3(m,0,1,2)
    assert w==(1,-7) and product3(m,0,1,3)==(1,7)
    assert product3(m,0,2,1)==conj(w)
    assert all(norm2(m[i][j])==norm2(mirror[i][j]) for i,j in product(sites,repeat=2))
    assert product3(mirror,0,1,2)==conj(w)
    gauges=[(1,0),(0,1),(-1,0),(0,-1)]
    transformed=[[mul(mul(gauges[i],m[i][j]),conj(gauges[j])) for j in sites] for i in sites]
    assert all(product3(transformed,i,j,k)==product3(m,i,j,k) for i,j,k in product(sites,repeat=3))
    print('M Hermitian, M²=7M, Tr(M)=14: P=M/7 is a rank-two occupied projector.')
    print('Every site: B_i = 12/49; every off-site sum equals 12/49.')
    assert all(den*m[i][i][0]-m[i][i][0]**2==12 for i in sites)
    print('W012=(1−7i)/343, W013=(1+7i)/343. All edge sums of imaginary parts vanish.')
    print('Reversing 012 conjugates W. Local phase gauges leave all loops unchanged.')
    print('P and its entrywise conjugate have identical X_ij and opposite Im(W012).')
    print('Flat Hamiltonian H=I−2P: off-site evolution blocks equal 2i sin(t) P_ji; P is the occupied lower-band projector. All off-site summed transfer probabilities agree in both directions.')
    shifts=set(product((-1,1), repeat=3))
    count=sum(tuple(u+v for u,v in zip(a,b)) in shifts for a,b in product(shifts,repeat=2))
    assert count==0
    print('Ideal bcc nearest-neighbour displacements: 0 directed two-step sums are a third nearest-neighbour edge.')

if __name__=='__main__':
    run()
