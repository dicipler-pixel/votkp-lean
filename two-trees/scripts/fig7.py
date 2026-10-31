# SCRIPT: PEEL-TREES-FIG7
# Figure 7: the knot commutator band. Left: real Riley branches in the plane (x, u), u = v / (4 sinh^2 x)
# (u in (0,1) <=> the meridian axes cross); shaded: the rotation band 0 < A^2 u(1-u) < 4, A = 4 sinh^2 x.
# Right: first entry x for each knot (80-digit check, firstx_out.json); knots that never enter marked.
import json, warnings; warnings.filterwarnings('ignore')
import numpy as np, mpmath as mp, sympy as sp, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from census_lib import riley_poly, S_, V_
BG='#070c18'; INK='#e3ebff'; DIM='#8fa2c4'; LINE='#2a3a5c'
C1='#4fe3c1'; C2='#ffb547'; C3='#ff6f91'; C4='#7aa8ff'; C5='#c08bff'
plt.rcParams.update({'font.family':'DejaVu Sans','text.color':INK,'axes.edgecolor':LINE,'axes.labelcolor':INK,
                     'xtick.color':DIM,'ytick.color':DIM,'savefig.facecolor':BG,'figure.facecolor':BG,'axes.facecolor':BG})
mp.mp.dps = 50
fig, (a1, a2) = plt.subplots(1, 2, figsize=(12.5, 5.6), gridspec_kw=dict(width_ratios=[1.25, 1]))
X = np.linspace(0.01, 2.6, 400); A = 4*np.sinh(X)**2
# band: 0<u<1 and A^2 u(1-u) < 4
U = np.linspace(-0.6, 1.6, 600); XX, UU = np.meshgrid(X, U); AA = 4*np.sinh(XX)**2; K = AA**2*UU*(1-UU)
a1.contourf(XX, UU, ((K > 0) & (K < 4)).astype(float), levels=[0.5, 1.5], colors=['#1c3b4a'])
a1.axhline(0, color=LINE, lw=1); a1.axhline(1, color=LINE, lw=1)
a1.axvline(np.log(1+np.sqrt(2)), color=DIM, lw=1, ls='--'); a1.text(np.log(1+np.sqrt(2))+0.03, 1.5, 'x = ln(1+√2)\n(Γ² = 1/2)', color=DIM, fontsize=9, va='top')
for name, p, q, col in [('3₁', 3, 1, C3), ('4₁', 5, 3, C1), ('5₂', 7, 3, C2), ('6₃', 13, 5, C5)]:
    R = sp.Poly(riley_poly(p, q), V_); cs = [sp.lambdify(S_, c, 'mpmath') for c in R.all_coeffs()]
    xs, us = [], []
    for x in np.linspace(0.01, 2.6, 260):
        s = mp.e ** mp.mpf(x); Ax = (s - 1/s)**2
        for r in mp.polyroots([c(s) for c in cs], maxsteps=600, extraprec=300):
            if abs(mp.im(r)) < mp.mpf(10)**-20:
                u = float(mp.re(r)/Ax)
                if -0.6 < u < 1.6: xs.append(x); us.append(u)
    a1.scatter(xs, us, s=3, color=col, label=name)
a1.set_xlim(0, 2.6); a1.set_ylim(-0.6, 1.6); a1.set_xlabel('x  (meridian length 2x)'); a1.set_ylabel('u = v / 4 sinh²x')
a1.text(0.05, 0.47, 'axes cross', color=DIM, fontsize=9); a1.text(0.05, 1.08, 'axes disjoint', color=DIM, fontsize=9); a1.text(0.05, -0.12, 'axes disjoint (v < 0)', color=DIM, fontsize=9)
lg = a1.legend(loc='upper right', markerscale=4, frameon=True, facecolor=BG, edgecolor=LINE, fontsize=9)
a1.set_title('Real branches against the rotation band (shaded)', fontsize=12)
d = json.load(open('firstx_out.json'))
names = list(d.keys()); ent = [(n, d[n]['x1']) for n in names if d[n]['enters']]; nev = [n for n in names if not d[n]['enters']]
ent.sort(key=lambda z: z[1]); order = ent + [(n, None) for n in nev]
for i, (n, x1) in enumerate(order):
    if x1 is None: a2.text(0.02, i, 'never (k < 0 on every real branch)', color=C3, fontsize=8.5, va='center')
    else: a2.barh(i, x1, color=C1, height=0.6)
a2.set_yticks(range(len(order))); SUB=str.maketrans('0123456789','₀₁₂₃₄₅₆₇₈₉'); a2.set_yticklabels([n if n.startswith('T') else n.split('_')[0]+n.split('_')[1].translate(SUB) for n, _ in order], fontsize=9); a2.set_ylim(len(order)-0.4, -0.6); 
a2.axvline(np.log(1+np.sqrt(2)), color=DIM, lw=1, ls='--'); a2.set_xlim(0, 1.0); a2.set_xlabel('first x with an elliptic commutator')
a2.set_title('First entry into the band, 26 knots', fontsize=12)
plt.tight_layout(); plt.savefig('fig7_band.png', dpi=150); print('ok', len(ent), 'enter,', len(nev), 'never')
