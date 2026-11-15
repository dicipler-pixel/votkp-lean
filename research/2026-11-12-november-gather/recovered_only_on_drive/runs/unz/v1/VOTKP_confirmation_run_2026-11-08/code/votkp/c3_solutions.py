# SCRIPT: c3_solutions
"""C3/C4. All solutions of the gluing equations, and what ordering they induce.

The gluing equations come from SnapPy as an integer exponent matrix A with 3n columns
(z_j, z'_j = 1/(1-z_j), z''_j = 1-1/z_j) and one row per edge, plus meridian and
longitude rows. A solution is a complex vector z with every row product equal to 1.

We find ALL solutions numerically (damped Newton from many random starts, then
deduplicate), and for each solution record
    S   = sum_j |G_j|^2          (distance from the vacuum, G = (z-w)/(z-conj w))
    vol = Re sum_j D(z_j)        (the volume the solution would give)
    inside = every |G_j| < 1     (the tetrahedra are all geometric, not mirror)

Pre-registered rules.
  C3a  the geometric solution (SnapPy's) minimises S over all solutions.
       CONFIRMED iff it is the strict minimum for every knot; a counterexample is named.
  C3b  mirror solutions lie outside the disk. CONFIRMED iff every solution that is not
       the geometric one and not its Galois partners has some |G_j| > 1 ... stated
       precisely below as: every solution with all |G_j| < 1 is the geometric one.
  C3c  all-real solutions give S = n exactly. CONFIRMED iff it holds for every all-real
       solution found.
  C4   within each knot, volume decreases as S increases. Scored by Spearman over the
       solutions of each knot; every knot whose order breaks is named.
"""
import sys, json, itertools
sys.path.insert(0,'code')
import numpy as np
from scipy.optimize import root
import snappy, math

W  = complex(math.cos(math.pi/3),  math.sin(math.pi/3))
WB = complex(math.cos(math.pi/3), -math.sin(math.pi/3))
V0 = 1.0149416064096536

def sn(nm):
    import re
    m = re.match(r'^(\d+)([an])_(\d+)$', nm)
    return f'{m.group(1)}{m.group(2)}{m.group(3)}' if m else nm

def shapes_of(z):
    return np.array([complex(t) for t in z])

def zprime(z): return 1.0/(1.0-z)
def zsecond(z): return 1.0 - 1.0/z

def F(A, z):
    n = len(z)
    out = []
    for row in np.asarray(A):
        val = 1.0+0j
        for j in range(n):
            a, b, c = row[j], row[n+j], row[2*n+j]
            if a: val *= z[j]**a
            if b: val *= zprime(z[j])**b
            if c: val *= zsecond(z[j])**c
        out.append(val - 1.0)
    return np.array(out)

def realF(A, xr):
    z = xr[:len(xr)//2] + 1j*xr[len(xr)//2:]
    return np.concatenate([F(A, z).real, F(A, z).imag])

def deduce(nm, nstarts=400, seed=1):
    M = snappy.Link(sn(nm)).exterior()
    g = M.gluing_equations()
    A = np.array(g.list(), dtype=int).reshape(g.shape)
    n = M.num_tetrahedra()
    geo = np.array([complex(t) for t in M.tetrahedra_shapes('rect', bits_prec=53)])
    rng = np.random.default_rng(seed)
    sols = []
    for _ in range(nstarts):
        start = rng.uniform(-2, 2, 2*n) + 1j*rng.uniform(-2, 2, 2*n)
        x0 = np.concatenate([start.real, start.imag])
        try:
            r = root(realF, x0, args=(A,), method='hybr', tol=1e-13)
        except Exception:
            continue
        if not r.success: continue
        z = r.x[:n] + 1j*r.x[n:]
        if np.max(np.abs(F(A, z))) > 1e-8: continue
        if np.min(np.abs(z)) < 1e-6 or np.min(np.abs(1-z)) < 1e-6: continue
        if any(np.max(np.abs(z - s)) < 1e-6 for s in sols): continue
        sols.append(z)
    out = []
    for z in sols:
        G = (z-W)/(z-WB)
        S = float(np.sum(np.abs(G)**2))
        Ds = []
        for t in z:
            # Bloch-Wigner
            import mpmath as mp
            val = mp.im(mp.polylog(2, mp.mpc(t.real, t.imag))) + mp.arg(1-t)*mp.log(abs(t))
            Ds.append(float(val))
        out.append(dict(z=[complex(t).real + 1j*complex(t).imag for t in z],
                        S=S, vol=float(np.sum(Ds)),
                        inside=bool(np.all(np.abs(G) < 1)),
                        allreal=bool(np.all(np.abs(z.imag) < 1e-9)),
                        is_geo=bool(any(np.max(np.abs(z-g)) < 1e-6 for g in geo))))
    return dict(knot=nm, n=n, nsol=len(sols), sols=out,
                geo_S=float(np.sum(np.abs((geo-W)/(geo-WB))**2)))

if __name__ == '__main__':
    from scipy.stats import spearmanr
    for nm in sys.argv[1:]:
        r = deduce(nm)
        print(f"\n{nm}: n={r['n']}  solutions found: {r['nsol']}")
        for s in sorted(r['sols'], key=lambda s: s['S']):
            print(f"   S={s['S']:.6f}  vol={s['vol']:+.6f}  inside={s['inside']}  "
                  f"allreal={s['allreal']}  geo={s['is_geo']}")
