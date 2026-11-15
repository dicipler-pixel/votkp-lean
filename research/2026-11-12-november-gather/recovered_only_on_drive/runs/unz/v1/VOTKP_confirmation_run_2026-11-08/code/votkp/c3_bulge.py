# SCRIPT: c3_bulge
"""Is the flat locus in 7_7 a curve (a "pseudospectral bulge") or a set of points?

A pseudospectrum, in the sense the corpus uses the word, is what a non-normal object has
instead of isolated eigenvalues: a positive-dimensional region whose boundary bulges away
from the spectrum. The knot-side analogue is exact and testable:

  * the ISOLATED (zero-dimensional) components of the Ptolemy variety are the discrete
    geometries -- a spectrum;
  * the POSITIVE-DIMENSIONAL components are families -- a bulge.

If the flat (volume-zero) solutions lie on positive-dimensional components, then "flat"
is a curve, and a single flat point says nothing about its neighbours. Pre-registered
rule: CONFIRMED as a bulge iff some positive-dimensional component exists and its points
have volume identically zero while S = sum|G_j|^2 varies continuously along it.
"""
import sys, json, math, re
sys.path.insert(0,'code'); sys.path.insert(0,'code/votkp')
import numpy as np, sympy as sp
import snappy
from snappy.ptolemy.coordinates import PtolemyCoordinates
from c3_parse import parse_magma, split_knots, sn, score
import mpmath as mp

def sample_component(polys, var_names, free, n=12, seed=3):
    """Set the free variables to random values, solve the rest by least squares."""
    syms = sp.symbols(var_names)
    if not isinstance(syms, (list, tuple)): syms = [syms]
    eqs = [sp.sympify(p.replace('^','**'), locals={v: s for v, s in zip(var_names, syms)}) for p in polys]
    f = sp.lambdify(syms, eqs, 'numpy')
    idx = {v: i for i, v in enumerate(var_names)}
    fixed = [v for v in var_names if v not in free]
    rng = np.random.default_rng(seed)
    out = []
    from scipy.optimize import least_squares
    for _ in range(n):
        base = {v: 0j for v in var_names}
        for v in free:
            base[v] = complex(rng.normal(0, 1.2), rng.normal(0, 1.2))
        def resid(x):
            d = dict(base)
            for j, v in enumerate(fixed): d[v] = x[j] + 1j*x[len(fixed)+j]
            vals = [complex(o) for o in np.atleast_1d(f(*[d[v] for v in var_names]))]
            return np.array([o.real for o in vals] + [o.imag for o in vals])
        x0 = np.concatenate([rng.normal(0,1,len(fixed)), rng.normal(0,1,len(fixed))])
        try:
            r = least_squares(resid, x0, xtol=1e-13, ftol=1e-13, max_nfev=300)
        except Exception:
            continue
        if np.max(np.abs(r.fun)) > 1e-8: continue
        d = dict(base)
        for j, v in enumerate(fixed): d[v] = complex(r.x[j], r.x[len(fixed)+j])
        out.append(d)
    return out

if __name__ == '__main__':
    meta = json.load(open('.scratch/magma/meta.json'))
    blocks = split_knots(open('.scratch/magma/batch0.out').read())
    kn = '7_7'
    M = snappy.Link('7_7').exterior()
    dim, comps = parse_magma(blocks[kn])
    print(f'{kn}: variety dimension {dim}, {len(comps)} components')
    for i, c in enumerate(comps):
        print(f'  component {i}: dimension {c["dim"]}, {len(c["polys"])} basis polynomials')
    pos = [c for c in comps if c['dim'] > 0]
    print(f'\npositive-dimensional components: {len(pos)}')
    if not pos:
        print('  -> no bulge: the flat locus is discrete'); raise SystemExit
    dep = []
    for c in pos:
        eqs = c['polys']
        mentioned = set()
        for p in eqs:
            mentioned |= set(re.findall(r'c_\d{4}_\d+', p))
        free = [v for v in meta[kn]['variables'] if v not in
                {v for v in meta[kn]['variables'] if any(v + ' ' in p or v+'*' in p or v+'^' in p or p.strip().endswith(v) or p.strip()==v for p in eqs)}]
        pts = sample_component(eqs, meta[kn]['variables'], free)
        print(f'\n  dim-{c["dim"]} component: free vars {free}; {len(pts)} points solved')
        for d in pts[:6]:
            d2 = {k: v for k, v in d.items()}; d2['1'] = 1
            try:
                pc = PtolemyCoordinates(d2, is_numerical=True,
                                        py_eval_section=eval(meta[kn]['py_eval']),
                                        manifold_thunk=lambda: M)
                cr = pc.cross_ratios(); z = {}
                for k, v in cr.items():
                    m = re.match(r'^z_0000_(\d+)$', k)
                    if m: z[int(m.group(1))] = complex(v)
                if len(z) != M.num_tetrahedra():
                    print('     shapes degenerate'); continue
                sc = score(z)
                dep.append((sc['S'], sc['vol']))
                print(f"     S={sc['S']:14.6f}   vol={sc['vol']:+14.6f}")
            except Exception as e:
                print('     degenerate:', type(e).__name__)
    if dep:
        S = [a for a, b in dep]; V = [b for a, b in dep]
        print(f'\n  along the positive-dimensional components: S ranges over '
              f'[{min(S):.4f}, {max(S):.4f}], volume over [{min(V):+.6f}, {max(V):+.6f}]')
