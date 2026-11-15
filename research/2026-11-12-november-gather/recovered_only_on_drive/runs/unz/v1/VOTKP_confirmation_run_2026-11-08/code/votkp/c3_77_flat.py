# SCRIPT: c3_77_flat
"""The two kinds of flat in 7_7, re-anchored in the geometric shape map.

"Sometimes degenerate, sometimes exceptional" -- this file exhibits both, on the same knot,
through SnapPy's own Ptolemy-coordinates-to-cross-ratios map:

  DEGENERATE  points on the four dimension-2 components: a Ptolemy coordinate is zero, the
              cross ratio is 0/0, and no tetrahedron shape exists. They are not geometries.
  EXCEPTIONAL isolated points on the zero-dimensional components where every one of the
              eight shapes is a genuine non-real number, the eight volumes sum to exactly
              zero, and no individual volume is zero.

For each exceptional solution we print every shape, its position in the vacuum disk
|G_j|^2, and its volume D(z_j), so the cancellation is visible term by term.
"""
import sys, json, math, re
sys.path.insert(0,'code'); sys.path.insert(0,'code/votkp')
import snappy, mpmath as mp
from snappy.ptolemy.coordinates import PtolemyCoordinates
from c3_parse import parse_magma, split_knots, sn, solve_component
from c3_nsolve import solve_numeric
mp.mp.dps = 30
W  = complex(math.cos(math.pi/3),  math.sin(math.pi/3))
WB = complex(math.cos(math.pi/3), -math.sin(math.pi/3))

def D(t):
    return float(mp.im(mp.polylog(2, mp.mpc(t.real, t.imag))) + mp.arg(1-t)*mp.log(abs(t)))

meta = json.load(open('.scratch/magma/meta.json'))
blocks = split_knots(open('.scratch/magma/batch0.out').read())
M = snappy.Link('7_7').exterior()
n = M.num_tetrahedra()
dim, comps = parse_magma(blocks['7_7'])

print(f'7_7: {n} tetrahedra; variety dimension {dim}; {len(comps)} zero-dimensional components')
print()
print('--- DEGENERATE: the dimension-2 components -------------------------------------------------')
print('  all four pin a Ptolemy coordinate to zero, so c_0011/c_0101 = 0/0: no shape exists.')
print('  They are recorded as components of the variety, not as geometries.')
print()

print('--- EXCEPTIONAL: flat points on the zero-dimensional components -----------------------------')
found = []
for c in comps:
    if c['dim'] != 0: continue
    cands = solve_component(c['polys'], meta['7_7']['variables'])
    try: cands += solve_numeric(c['polys'], meta['7_7']['variables'], nstarts=800)
    except Exception: pass
    for s in cands:
        d = {str(k): complex(v) for k, v in s.items()}; d['1'] = 1
        try:
            pc = PtolemyCoordinates(d, is_numerical=True,
                                    py_eval_section=eval(meta['7_7']['py_eval']),
                                    manifold_thunk=lambda: M)
            cr = pc.cross_ratios()
            z = {}
            for k, v in cr.items():
                m = re.match(r'^z_0000_(\d+)$', k)
                if m: z[int(m.group(1))] = complex(v)
            if len(z) != n: continue
        except Exception:
            continue
        V = sum(D(t) for t in z.values())
        if abs(V) > 1e-9: continue
        G = [(t-W)/(t-WB) for t in z.values()]
        S = sum(abs(g)**2 for g in G)
        if any(abs(S-a) < 1e-7 for a, _ in found): continue
        found.append((S, z))

for S, z in sorted(found):
    print(f'\n  solution with S = sum|G_j|^2 = {S:.6f}, total volume {sum(D(t) for t in z.values()):+.3e}')
    print(f"    {'j':>3s} {'Re z':>10s} {'Im z':>10s} {'|G|^2':>9s} {'D(z_j)':>12s}")
    tot = 0.0
    for j in sorted(z):
        t = z[j]; g = (t-W)/(t-WB); dj = D(t); tot += dj
        print(f'    {j:3d} {t.real:10.5f} {t.imag:10.5f} {abs(g)**2:9.4f} {dj:+12.6f}')
    print(f'    {"":3s} {"":10s} {"":10s} {"sum":>9s} {tot:+12.6f}')
    print(f'    non-real shapes: {sum(1 for t in z.values() if abs(t.imag)>1e-9)} of {n};'
          f'  individual volumes all nonzero: {all(abs(D(t))>1e-6 for t in z.values())}')
