# SCRIPT: c3_parse
"""C3/C4 stage 2: parse a Magma decomposition, solve the component, read off the shapes.

Input: the Magma stdout, the variable list, and the py_eval section from c3_stage.py.
The zero-dimensional prime component's Groebner basis is solved (symbolically where sympy
can, numerically from many starts otherwise), each solution is pushed through py_eval to
recover the full Ptolemy coordinate set, and the shape parameters z_<pt>_<tet> are read off.

For each solution we record
    S      = sum over tetrahedra of |G(z)|^2,  G = (z-w)/(z-conj w)
    vol    = sum over tetrahedra of D(z)      (Bloch-Wigner)
    inside = every |G| < 1
    allreal= every z real
"""
import sys, re, json, math
sys.path.insert(0,'code')
import numpy as np
import sympy as sp
import mpmath as mp
mp.mp.dps = 40

def sn(nm):
    m = re.match(r'^(\d+)([an])_(\d+)$', nm)
    return f'{m.group(1)}{m.group(2)}{m.group(3)}' if m else nm

W  = complex(math.cos(math.pi/3),  math.sin(math.pi/3))
WB = complex(math.cos(math.pi/3), -math.sin(math.pi/3))

def split_knots(text):
    blocks = {}
    cur = None; buf = []
    for line in text.split('\n'):
        if line.strip().startswith('==KNOT=='):
            if cur is not None: blocks[cur] = '\n'.join(buf)
            cur = line.strip().split('==KNOT==')[1]; buf = []
        else:
            buf.append(line)
    if cur is not None: blocks[cur] = '\n'.join(buf)
    return {k: v for k, v in blocks.items() if k}

def parse_magma(out):
    """Return (dim, list of components), each component = (dim, [poly strings])."""
    lines = out.split('\n')
    comps = []; cur = None; dim = None
    for L in lines:
        L = L.strip()
        if L.startswith('==DIM=='):
            m = re.match(r'==DIM==\s*(-?\d+)', L)
            if m: dim = int(m.group(1))
        elif L == '==COMP==':
            cur = {'dim': None, 'polys': []}; comps.append(cur)
        elif L.startswith('==DIMC=='):
            m = re.match(r'==DIMC==\s*(-?\d+)', L)
            if m and cur is not None: cur['dim'] = int(m.group(1))
        elif L.startswith('==POLY=='):
            if cur is not None: cur['polys'].append(L[len('==POLY=='):].strip())
    return dim, comps

def solve_component(polys, var_names):
    """All complex solutions of a 0-dimensional system, numerically."""
    syms = sp.symbols(' '.join(var_names))
    if not isinstance(syms, (list, tuple)): syms = [syms]
    eqs = []
    for p in polys:
        e = sp.sympify(p.replace('^','**'), locals={v: s for v, s in zip(var_names, syms)})
        eqs.append(e)
    sols = []
    try:
        raw = sp.solve(eqs, list(syms), dict=True)
    except Exception:
        raw = []
    for d in raw:
        vals = {}
        ok = True
        for v in syms:
            if v not in d: ok = False; break
            try:
                vals[v] = complex(sp.N(d[v], 40))
            except Exception:
                ok = False; break
        if ok: sols.append(vals)
    if not sols:
        # numerical fallback: univariate factors then back-substitute
        for p in eqs:
            free = p.free_symbols
            if len(free) == 1:
                v = list(free)[0]
                P = sp.Poly(sp.expand(p), v)
                for r in np.roots([complex(c) for c in P.all_coeffs()]):
                    vals = {v: complex(r)}
                    rem = [e.subs({v: r}) for e in eqs]
                    rem = [e for e in rem if e.free_symbols]
                    sub = sp.solve(rem, list(set().union(*[e.free_symbols for e in rem])), dict=True) if rem else [{}]
                    for s2 in sub:
                        d2 = dict(vals)
                        good = True
                        for k2, v2 in s2.items():
                            try: d2[k2] = complex(sp.N(v2, 40))
                            except Exception: good = False
                        if good and len(d2) == len(syms): sols.append(d2)
    return sols

def to_shapes(sol, var_names, py_eval_src, manifold=None):
    """Shapes via SnapPy's OWN conversion, not a hand-rolled cross ratio.

    PtolemyCoordinates(dict).cross_ratios() returns z_0000_<t>, the tetrahedron shape in
    SnapPy's convention. CHECKED on 4_1: the solution with c_{0101,1}=e^{+2 pi i/3} gives
    z = w = 0.5+0.866i on both tetrahedra, matching CrossRatios.from_snappy_manifold(M)
    exactly; the other solution gives conj(w). An earlier version of this file used a
    hand-written cross ratio, which produced e^{+-2 pi i/3} (the square of the true value)
    and hence a volume of 1.353 instead of 2.030. That was the fault, and it is gone.
    """
    from snappy.ptolemy.coordinates import PtolemyCoordinates
    d = {str(k): complex(v) for k, v in sol.items()}
    d['1'] = 1
    pc = PtolemyCoordinates(d, is_numerical=True,
                            py_eval_section=eval(py_eval_src),
                            manifold_thunk=lambda: manifold)
    cr = pc.cross_ratios()
    z = {}
    for k, v in cr.items():
        m = re.match(r'^z_0000_(\d+)$', k)
        if m:
            z[int(m.group(1))] = complex(v)
    return z

def score(z):
    zs = [z[k] for k in sorted(z)]
    G = [(t - W)/(t - WB) if abs(t - WB) > 1e-14 else complex(1e15, 0) for t in zs]
    S = float(sum(abs(g)**2 for g in G))
    vol = 0.0
    for t in zs:
        if abs(t.imag) < 1e-12 or abs(t) < 1e-14:
            continue
        vol += float(mp.im(mp.polylog(2, mp.mpc(t.real, t.imag))) + mp.arg(1-t)*mp.log(abs(t)))
    return dict(S=S, vol=vol, inside=all(abs(g) < 1 for g in G),
                allreal=all(abs(t.imag) < 1e-9 for t in zs), n=len(zs))

if __name__ == '__main__':
    out_file = sys.argv[1]; knot = sys.argv[2]
    import snappy as _snappy
    meta = json.load(open('.scratch/magma/meta.json'))[knot]
    M = _snappy.Link(sn(knot)).exterior()
    dim, comps = parse_magma(open(out_file).read())
    print(f'{knot}: variety dimension {dim}, {len(comps)} prime components')
    allsol = []
    for c in comps:
        if c['dim'] != 0:
            print(f"   skipping component of dimension {c['dim']} (positive-dimensional)")
            continue
        sols = solve_component(c['polys'], meta['variables'])
        print(f"   component dim 0, {len(c['polys'])} basis polys, {len(sols)} solutions")
        for s in sols:
            try:
                z = to_shapes(s, meta['variables'], meta['py_eval'], manifold=M)
                sc = score(z)
                allsol.append(sc)
                print(f"      S={sc['S']:10.6f} vol={sc['vol']:+10.6f} inside={sc['inside']} allreal={sc['allreal']}")
            except Exception as e:
                print('      shape extraction failed:', type(e).__name__, e)
    json.dump(allsol, open('.scratch/magma/%s_sols.json' % knot.replace('_',''), 'w'), indent=1)
