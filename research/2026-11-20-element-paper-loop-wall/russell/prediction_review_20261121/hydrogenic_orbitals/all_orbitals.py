"""Exact rational integration of scaled hydrogenic orbitals and a Jacobi cross-check."""
from fractions import Fraction as F
from math import comb, factorial

def jacobi_moment(n, l, x):
    k, p = n - l - 1, 2*l + 2
    return sum(comb(k,h)*comb(k+p-1,h)*(-x)**h*(1-x)**(k-h)
               for h in range(k+1))

def radial_moment(n,l,a):
    # In y=(alpha+beta)R/n, the Laguerre arguments are (1+a)y and (1-a)y.
    k, lam = n-l-1, 2*l+1
    terms = [F((-1)**j*comb(k+lam,k-j),factorial(j)) for j in range(k+1)]
    integral=sum(u*v*(1+a)**i*(1-a)**j*factorial(lam+i+j+1)
                 for i,u in enumerate(terms) for j,v in enumerate(terms))
    return integral/F((2*n)*factorial(k+lam),factorial(k))

def main():
    count = 0
    for n in range(1,14):
        for l in range(n):
            for a in map(F, ['-5/7','-1/3','0','1/8','1/3','3/5','9/11']):
                s = radial_moment(n,l,a)
                assert s == jacobi_moment(n,l,a*a)
                prob=(1-a*a)**(2*l+3)*s*s
                assert 0 <= prob <= 1
                count += 1
    print(f'{count} exact rational moment/Jacobi comparisons, n=1..13, every l')
    for n,l in [(1,0),(2,0),(2,1),(3,0),(3,1),(3,2)]:
        a=F(1,3)
        prob=(1-a*a)**(2*l+3)*jacobi_moment(n,l,a*a)**2
        print(f'n={n} l={l} F(z=4)={prob} ({float(prob):.9f}), local coefficient={(2*n*n-2*l*(l+1)+1)}/16')

if __name__=='__main__':
    main()
