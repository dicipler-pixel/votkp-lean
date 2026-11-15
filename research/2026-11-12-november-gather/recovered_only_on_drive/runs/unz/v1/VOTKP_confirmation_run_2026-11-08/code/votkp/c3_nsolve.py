# SCRIPT: c3_nsolve
"""C3/C4: numerical solution of a Ptolemy component, then shapes and scores.

The symbolic route (sympy.solve on the Groebner basis) missed components whose basis is
not triangular in a form sympy resolves. The method used here is the one the VOTKP paper
describes: damped Newton from many random starts on the polynomial system itself, then
deduplication. SnapPy's PtolemyCoordinates.cross_ratios() converts a solution to shapes.

Pre-registered rules (unchanged from c3_solutions.py):
  C3a the geometric solution minimises S = sum |G_j|^2.
  C3b every solution with all |G_j| < 1 is the geometric one.
  C3c every all-real solution has S = n.
  C4  within each knot, volume decreases as S increases (Spearman per knot, negative).
"""
import sys, json, math
sys.path.insert(0,'code'); sys.path.insert(0,'code/votkp')
import numpy as np
from scipy.optimize import least_squares
import sympy as sp
import snappy
from snappy.ptolemy.coordinates import PtolemyCoordinates
from c3_parse import parse_magma, split_knots, score, sn, solve_component

def solve_numeric(polys, var_names, nstarts=3000, seed=7):
    syms = sp.symbols(var_names)
    if not isinstance(syms, (list, tuple)): syms = [syms]
    eqs = [sp.sympify(p.replace('^','**'), locals={v: s for v, s in zip(var_names, syms)})
           for p in polys]
    f = sp.lambdify(syms, eqs, 'numpy')
    n = len(syms)
    rng = np.random.default_rng(seed)
    sols = []
    def resid(x):
        z = x[:n] + 1j*x[n:]
        out = f(*z)
        out = [complex(o) for o in np.atleast_1d(out)]
        return np.array([o.real for o in out] + [o.imag for o in out])
    for _ in range(nstarts):
        x0 = np.concatenate([rng.normal(0, 1.5, n), rng.normal(0, 1.5, n)])
        try:
            r = least_squares(resid, x0, xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=400)
        except Exception:
            continue
        if np.max(np.abs(r.fun)) > 1e-9: continue
        z = r.x[:n] + 1j*r.x[n:]
        if any(np.max(np.abs(np.concatenate([z.real-a.real, z.imag-a.imag]))) < 1e-6 for a in sols):
            continue
        sols.append(z)
    return [dict(zip(var_names, s)) for s in sols]

def analyse(knot, block, meta, nstarts=3000):
    M = snappy.Link(sn(knot)).exterior()
    V = M.ptolemy_variety(2, obstruction_class=1 if len(M.ptolemy_obstruction_classes()) > 1 else None)
    dim, comps = parse_magma(block)
    out = []
    for c in comps:
        if c['dim'] != 0: continue
        cands = solve_component(c['polys'], meta['variables'])
        try:
            cands = cands + solve_numeric(c['polys'], meta['variables'], nstarts=nstarts)
        except Exception:
            pass
        for s in cands:
            d = {str(k): complex(v) for k, v in s.items()}; d['1'] = 1
            try:
                pc = PtolemyCoordinates(d, is_numerical=True,
                                        py_eval_section=eval(meta['py_eval']),
                                        manifold_thunk=lambda: M)
                cr = pc.cross_ratios()
                z = {}
                import re
                for k, v in cr.items():
                    m = re.match(r'^z_0000_(\d+)$', k)
                    if m: z[int(m.group(1))] = complex(v)
                if len(z) != M.num_tetrahedra(): continue
                sc = score(z); sc['z'] = [str(t) for t in z.values()]
                out.append(sc)
            except Exception:
                pass
    # dedupe on S
    ded = []
    for r in sorted(out, key=lambda r: r['S']):
        if not any(abs(r['S']-q['S']) < 1e-7 and abs(r['vol']-q['vol']) < 1e-7 for q in ded):
            ded.append(r)
    return ded, M.num_tetrahedra()

if __name__ == '__main__':
    from scipy.stats import spearmanr
    meta = json.load(open('.scratch/magma/meta.json'))
    blocks = split_knots(open('.scratch/magma/batch0.out').read()) | {'4_1': open('.scratch/magma/41.out').read()}
    knots = sys.argv[1:] or ['4_1','5_2','6_1','6_2','6_3','7_2','7_4']
    results = {}
    for kn in knots:
        if kn not in blocks: print(f'{kn}: no Magma block'); continue
        rows, n = analyse(kn, blocks[kn], meta[kn])
        results[kn] = rows
        print(f"\n{kn}  (n={n})   {len(rows)} solutions")
        for r in rows:
            print(f"    S={r['S']:12.6f}  vol={r['vol']:+10.6f}  inside={r['inside']}  allreal={r['allreal']}")
        if len(rows) >= 3:
            S = [r['S'] for r in rows]; Vv = [r['vol'] for r in rows]
            rho = spearmanr(S, Vv).statistic
            print(f"    C3a nearest-vacuum inside: {rows[0]['inside']}")
            print(f"    C3c all-real S=n: " + ", ".join(f"{r['S']:.6f}" for r in rows if r['allreal']) if any(r['allreal'] for r in rows) else "    C3c no all-real solutions")
            print(f"    C4 Spearman(S, vol) = {rho:+.4f}")
    json.dump({k: v for k, v in results.items()}, open('.scratch/c3_results.json','w'), indent=1)
