# SCRIPT: WTK-LOOPWALL-RAIL-REFLECTION-01
"""
Connection: WTK's rail (lambda_pm = sec psi +- tan psi, t = log lambda_+, Proposition 11)
and the element paper's reflection Gamma = (z-1)/(z+1) = tanh(r/2).

Why this check proves what it claims:
 1. If a step ratio z is put on the rail as lambda_+ = z, then Gamma(z) = tan(psi/2) is an
    algebraic identity: lambda_+ = (1 + sin psi)/cos psi = tan(pi/4 + psi/2), and
    (tan(pi/4+x) - 1)/(tan(pi/4+x) + 1) = tan x. Sympy must reduce the difference to 0.
    Then Gamma^2 = 1/2 fixes sec psi = (1 + Gamma^2)/(1 - Gamma^2) = 3: the loop wall sits
    on the rail where sec psi = 3, i.e. cos psi = 1/3.
 2. Exact arithmetic: (3 + 2 sqrt2)^2 = 17 + 12 sqrt2. Sympy must expand it. Then the
    Catalan rail root of WTK section 3 is the square of the loop-wall ratio, and its
    rapidity is twice the wall's.
 3. WTK Proposition 11: G = (1/2) int_0^{pi/2} log lambda_+(psi) dpsi. With the
    substitution psi = 2 arctan Gamma (from 1) and log lambda_+ = 2 artanh Gamma, this is
    G = int_0^1 2 artanh(Gamma)/(1 + Gamma^2) dGamma. If mpmath's quadrature equals
    Catalan's constant to 40 digits, the reflection form is confirmed numerically;
    the substitution itself is exact. The split of that integral at the wall
    Gamma = 1/sqrt2 is printed only as a number (a LEAD, no meaning claimed).
"""
import sympy as sp, mpmath as mp
psi = sp.symbols('psi', positive=True)
T = sp.symbols('T', positive=True)        # T = tan(psi/2); exact half-angle forms
lamT = (1 + T**2)/(1 - T**2) + 2*T/(1 - T**2)  # sec psi + tan psi
d = sp.simplify((lamT - 1)/(lamT + 1) - T)
print('1. with T = tan(psi/2): (lambda_+ - 1)/(lambda_+ + 1) - T =', d)
print('   numeric spot check at psi = 0.9:', sp.N(((sp.sec(0.9)+sp.tan(0.9))-1)/((sp.sec(0.9)+sp.tan(0.9))+1) - sp.tan(0.45), 15))
g = sp.symbols('g', positive=True)
secpsi = sp.simplify((1 + g**2)/(1 - g**2))
print('   sec psi at Gamma^2 = 1/2:', secpsi.subs(g, 1/sp.sqrt(2)), '; check sec(2 arctan g) =', sp.simplify(sp.sec(2*sp.atan(g)) - secpsi))
print('   psi at the wall = arccos(1/3) =', sp.N(sp.acos(sp.Rational(1,3))*180/sp.pi, 12), 'degrees')
print('   lambda_pm at sec psi = 3:', sp.simplify(3 + sp.sqrt(8)), 'and', sp.simplify(3 - sp.sqrt(8)))
print('2. (3+2sqrt2)^2 =', sp.expand((3 + 2*sp.sqrt(2))**2), '; (1+sqrt2)^4 =', sp.expand((1+sp.sqrt(2))**4))
print('   Gamma of the Catalan rail root 17+12sqrt2 =', sp.nsimplify(sp.simplify((16 + 12*sp.sqrt(2))/(18 + 12*sp.sqrt(2)))),
      ' (= tanh(2 h*), h* = arsinh 1)')
mp.mp.dps = 45
f = lambda x: 2*mp.atanh(x)/(1 + x*x)
I = mp.quad(f, [0, 1/mp.sqrt(2), 1])
print('3. int_0^1 2 artanh(G)/(1+G^2) dG =', mp.nstr(I, 40))
print('   Catalan G                      =', mp.nstr(mp.catalan, 40))
print('   difference                     =', mp.nstr(I - mp.catalan, 5))
inner = mp.quad(f, [0, 1/mp.sqrt(2)]); outer = mp.quad(f, [1/mp.sqrt(2), 1])
print('   LEAD only: inside-wall part', mp.nstr(inner, 15), ' outside-wall part', mp.nstr(outer, 15),
      ' fraction inside', mp.nstr(inner/mp.catalan, 12))
print('4. Second map: the loop holonomy W (equal faces) outside the wall has eigenvalues -lambda_pm with')
s2 = sp.symbols('s2', positive=True)   # s2 = sinh^2 h
print('   lambda_+ + lambda_- = |tr W| = 4 s2^2 - 2, lambda_+ lambda_- = 1, so sec psi_W = 2 s2^2 - 1')
sol = sp.solve(sp.Eq(2*s2**2 - 1, 17), s2)
print('   sec psi_W = 17 (the Catalan rail) needs sinh^2 h =', sol, '-> Gamma^2 = s2/(1+s2) =', [sp.nsimplify(x/(1+x)) for x in sol],
      '; sec psi_W = 1 (rail start) needs sinh^2 h =', sp.solve(sp.Eq(2*s2**2 - 1, 1), s2), '(the wall)')
