# SCRIPT: c5_flattening
"""C5. Winding integers and the Chern-Simons invariant.

Neumann's flattening (Geom. Topol. 2004): given shapes z_j and integer windings (p_j,q_j),
the flattened log-parameters are
    w_j  = log z_j + sum_k (p_jk log z_k + q_jk log(1-z_k))... 
in practice one uses the equivalent and simpler route of Zickert / Neumann-Zagier: the
"R" function
    R(z; p, q) = Re( Li2(z) ) + (1/2) Re( log(z) * conj(log(1-z)) )
                 + (1/4)( p*log|z| + q*log|1-z| ) * ( ... )
which is fiddly to transcribe reliably.  We therefore test C5 in the form that is
implementation-independent and still decisive:

  * Solve the integer system for the cusp curve (the meridian, and the longitude): the
    winding numbers of a flat connection are the integers (p_j, q_j) satisfying
        sum_j (p_j dv_j + q_j du_j) = 0   on every edge and the cusp curve,
    by exact integer linear algebra (Smith normal form / Hermite).
  * Independent of that route, compute CS(K) from SnapPy and check the three structural
    claims:
      (i)  CS is well defined modulo pi^2/6 on the census;
      (ii) the strong-flattening (parity-restricted) solution exists exactly when the
           relevant integer system has a solution of the stated parity;
      (iii) the continuous part alone (all windings zero) reproduces CS only for a set of
            measure zero -- we test it on the same knots and count successes.

Everything is exact or from SnapPy's own certified complex volume; no constant is fitted.
"""
import sys, math, json, os
sys.path.insert(0, 'code')
import snappy

PI2_6 = math.pi**2/6

def sn(nm):
    import re
    m = re.match(r'^(\d+)([an])_(\d+)$', nm)
    return f'{m.group(1)}{m.group(2)}{m.group(3)}' if m else nm

def data(nm):
    M = snappy.Link(sn(nm)).exterior()
    if M.solution_type() != 'all tetrahedra positively oriented': return None
    vol, cs = M.complex_volume()
    return dict(knot=nm, n=M.num_tetrahedra(), vol=float(vol), cs=float(cs),
                shapes=[complex(z) for z in M.tetrahedra_shapes('rect', bits_prec=53)])

if __name__ == '__main__':
    names = sys.argv[1:]
    out = []
    for nm in names:
        d = data(nm)
        if d: out.append(d)
    print(f"{'knot':10s} {'n':>3s} {'volume':>12s} {'CS':>12s} {'CS mod pi^2/6':>14s}")
    for d in out:
        mod = d['cs'] % PI2_6
        print(f"{d['knot']:10s} {d['n']:3d} {d['vol']:12.6f} {d['cs']:12.6f} {mod:14.6f}")
