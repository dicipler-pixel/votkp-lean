# SCRIPT: KNOT-COMM-BAND-HP
# High-precision check (mpmath, 60 digits) of the entries into the rotation band for 6_3, 7_5, 8_7, 8_8,
# and of the torus knots' ab trace and v sign.
import warnings; warnings.filterwarnings('ignore')
import mpmath as mp, sympy as sp
from census_lib import riley_poly, S_, V_
mp.mp.dps = 60
def real_roots(p, q, x):
    R = sp.Poly(riley_poly(p, q), V_); s = mp.e ** mp.mpf(x)
    co = [mp.mpf(str(sp.N(c.subs(S_, sp.Float(str(s), 70)), 70))) for c in R.all_coeffs()]
    rts = mp.polyroots(co, maxsteps=400, extraprec=200)
    return s, [mp.re(r) for r in rts if abs(mp.im(r)) < mp.mpf(10) ** -30]
for name, p, q, xs in [('6_3', 13, 5, [2.6, 2.865, 3.2, 4.0, 5.0]), ('7_5', 17, 5, [2.0, 2.055, 2.5, 3.5]),
                        ('8_7', 23, 5, [1.4, 1.42, 1.8, 3.0]), ('8_8', 25, 9, [1.3, 1.335, 1.8, 3.0])]:
    for x in xs:
        s, vs = real_roots(p, q, x); A = (s - 1 / s) ** 2
        trs = [2 - v * (A - v) for v in vs]
        ins = [mp.nstr(t, 12) for t in trs if abs(t) < 2]
        print(name, 'x=%.3f' % x, 'real roots', len(vs), ' tr[a,b] in (-2,2):', ins)
for name, p, q in [('T(2,3)', 3, 1), ('T(2,5)', 5, 1), ('T(2,7)', 7, 1)]:
    for x in [0.3, 1.0, 2.5]:
        s, vs = real_roots(p, q, x)
        print(name, 'x=%.1f' % x, [('v=' + mp.nstr(v, 8), 'tr(ab)=' + mp.nstr(s * s + 1 / (s * s) - v, 10)) for v in vs])
