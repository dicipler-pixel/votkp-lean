# SCRIPT: KNOT-COMM-SIGNS  — per knot, at sample x: each real Riley root v with t = tr(ab) and k = v(t-2) (60 digits)
import warnings; warnings.filterwarnings('ignore')
import mpmath as mp, sympy as sp, sys
from census_lib import riley_poly, S_, V_
mp.mp.dps = 60
for name, p, q in [('6_3',13,5),('7_5',17,5),('8_7',23,5),('8_8',25,9),('4_1',5,3),('5_2',7,3),('7_3',13,3)]:
    R = sp.Poly(riley_poly(p, q), V_); cs = [sp.lambdify(S_, c, 'mpmath') for c in R.all_coeffs()]
    print(name, 'deg', R.degree())
    for x in [0.05, 0.3, 1.0, 3.0]:
        s = mp.e ** mp.mpf(x); rts = mp.polyroots([c(s) for c in cs], maxsteps=800, extraprec=300)
        row = []
        for r in rts:
            if abs(mp.im(r)) < mp.mpf(10) ** -25:
                v = mp.re(r); t = s*s + 1/(s*s) - v
                row.append('v=%s t=%s k=%s' % (mp.nstr(v, 5), mp.nstr(t, 6), mp.nstr(v*(t-2), 4)))
        print('  x=%.2f' % x, ' | '.join(row))
