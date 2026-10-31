# SCRIPT: KNOT-COMM-BAND-HP2
# 60-digit rescan of 6_3, 7_5, 8_7, 8_8 (x in 0.02..6): for each real Riley root print v, tr(ab)=s^2+s^-2-v,
# and tr[a,b]-2 = -v(tr(ab)-2). Elliptic iff 0 < v(tr(ab)-2) < 4.
import warnings; warnings.filterwarnings('ignore')
import mpmath as mp, sympy as sp, json
from census_lib import riley_poly, S_, V_
mp.mp.dps = 60
out = {}
for name, p, q in [('6_3', 13, 5), ('7_5', 17, 5), ('8_7', 23, 5), ('8_8', 25, 9)]:
    R = sp.Poly(riley_poly(p, q), V_); cs = [sp.lambdify(S_, c, 'mpmath') for c in R.all_coeffs()]
    hits, closest = [], (None, mp.inf)
    x = mp.mpf('0.02')
    while x <= 6:
        s = mp.e ** x
        rts = mp.polyroots([c(s) for c in cs], maxsteps=500, extraprec=300)
        for r in rts:
            if abs(mp.im(r)) < mp.mpf(10) ** -25:
                v = mp.re(r); tab = s * s + 1 / (s * s) - v; k = v * (tab - 2)
                if 0 < k < 4: hits.append((float(x), float(v), float(2 - k)))
                d = min(abs(k), abs(k - 4))
                if k > 0 and d < closest[1]: closest = ((float(x), float(v), float(tab), float(k)), d)
        x += mp.mpf('0.01')
    out[name] = dict(hits=hits[:5], n_hits=len(hits), closest_positive_k=closest[0])
    print(name, 'hits', len(hits), hits[:3], 'closest k>0 (x,v,tr(ab),k):', closest[0], flush=True)
json.dump(out, open('band_hp2_out.json', 'w'), indent=1)
