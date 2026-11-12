# SCRIPT: c2_knotlaw
"""C2 (knot half). The bowl law, tested with nothing fitted.

Pre-registered rule: for a hyperbolic knot with a triangulation of n ideal tetrahedra of
shapes z_j, predict
    Vol_pred = sum_j [ V0 - (3 sqrt(3)/4)|G_j|^2 ],   G_j = (z_j-w)/(z_j-conj w),
and compare with SnapPy's volume. CONFIRMED as a knot-level law iff the median relative
error is below 1 percent and no hyperbolicity of the construction depends on fitting a
constant. We report median, 90th percentile and worst, and list the worst by name.
"""
import sys, math
import snappy

W  = complex(math.cos(math.pi/3), math.sin(math.pi/3))
WB = complex(math.cos(math.pi/3), -math.sin(math.pi/3))
V0 = 1.0149416064096536
C  = 3*math.sqrt(3)/4

def shape_G(z):
    return (z - W)/(z - WB)

def predict(shapes):
    tot = 0.0; n = 0
    for z in shapes:
        if abs(z.imag) < 1e-12:       # real shape: flat, contributes V0 - c|G|^2 = V0 - c
            pass
        tot += V0 - C*abs(shape_G(z))**2
        n += 1
    return tot, n

def sn(nm):
    import re
    m = re.match(r'^(\d+)([an])_(\d+)$', nm)
    return f'{m.group(1)}{m.group(2)}{m.group(3)}' if m else nm

def one(name, which='default'):
    try:
        M = snappy.Link(sn(name)).exterior()
        if M.solution_type() != 'all tetrahedra positively oriented': return None
        vol = float(M.volume())
        if which == 'default':
            sh = M.tetrahedra_shapes('rect', bits_prec=53)
        elif which == 'canonical':
            Mc = M.canonical_retriangulation()
            if Mc is None: return None
            sh = Mc.tetrahedra_shapes('rect', bits_prec=53)
        else:
            Mr = M.copy(); Mr.randomize()
            sh = Mr.tetrahedra_shapes('rect', bits_prec=53)
        sh = [complex(s) for s in sh]
        pred, n = predict(sh)
        Gs = [abs(shape_G(s))**2 for s in sh]
        return dict(knot=name, n=n, vol=vol, pred=pred, rel=abs(pred-vol)/vol,
                    meanG2=sum(Gs)/len(Gs), maxG2=max(Gs),
                    n_upper=sum(1 for s in sh if s.imag > 0), n_lower=sum(1 for s in sh if s.imag < 0))
    except Exception as ex:
        return dict(knot=name, error=f'{type(ex).__name__}: {ex}')

if __name__ == '__main__':
    names = sys.argv[1:]
    res = [one(nm) for nm in names]
    ok = [r for r in res if r and 'rel' in r]
    bad = [r for r in res if r and 'error' in r]
    print(f"{'knot':10s} {'n':>3s} {'+':>2s} {'-':>2s} {'volume':>12s} {'predicted':>12s} {'rel err':>10s}")
    for r in ok:
        print(f"{r['knot']:10s} {r['n']:3d} {r['n_upper']:2d} {r['n_lower']:2d} "
              f"{r['vol']:12.6f} {r['pred']:12.6f} {100*r['rel']:9.3f}%")
    if bad:
        print("errors:", [(b['knot'], b['error']) for b in bad][:5])
    if ok:
        import statistics as st
        rs = sorted(r['rel'] for r in ok)
        print()
        print(f"n = {len(ok)}   median {100*st.median(rs):.3f}%   "
              f"90th pct {100*rs[int(0.9*(len(rs)-1))]:.3f}%   worst {100*rs[-1]:.3f}% "
              f"({max(ok, key=lambda r: r['rel'])['knot']})")
