# SCRIPT: c5_windings
"""C5. Do the integer windings carry the Chern-Simons invariant?

Neumann (Geom. Topol. 8 (2004) 413-474), Thm 14.7; extended dilogarithm
    R(z; p, q) = R(z) + (pi i/2)( p log(1-z) + q log z ) - pi^2/6,
    R(z) = Li2(z) + (1/2) log z log(1-z)              (Rogers dilogarithm),
and
    i(vol + i cs)(M) = sum_j R(z_j; p_j, q_j)   in  C / pi^2 Z,
with (p_j, q_j) in Z^2 the winding numbers of a flattening, i.e. the integers that make
every edge and both cusp log-parameters vanish.

Pre-registered rules (written before the run):
  R1 (continuous part insufficient). Put S_cont = sum_j [R(z_j) - pi^2/6] with principal
     logs and p = q = 0. CONFIRMED iff the defect  T - S_cont  (T = i(vol + i cs)) is
     NONZERO for the overwhelming majority of knots. Reported as a count.
  R2 (windings carry it). CONFIRMED iff the defect always lies in the integer lattice
     spanned by {(pi i/2) log z_j, (pi i/2) log(1-z_j)}:  i.e. there exist integers
     (p_j, q_j) reproducing it, with residual below 1e-10 and the fitted integers within
     1e-6 of integers, for every knot.
  R3 (parity). Weak flattenings allow any integers; strong flattenings restrict them by a
     parity condition. CONFIRMED iff every solution to R2 satisfies that parity, so the
     pi^2/6 ambiguity disappears.
An item that fails R2 or R3 is reported with the failing knots named.
"""
import sys, math, json, os
sys.path.insert(0, 'code')
import mpmath as mp
import snappy
mp.mp.dps = 40

def sn(nm):
    import re
    m = re.match(r'^(\d+)([an])_(\d+)$', nm)
    return f'{m.group(1)}{m.group(2)}{m.group(3)}' if m else nm

pi = mp.pi
def R(z):
    return mp.polylog(2, z) + mp.mpf(1)/2*mp.log(z)*mp.log(1 - z)

def analyse(nm):
    M = snappy.Link(sn(nm)).exterior()
    if M.solution_type() != 'all tetrahedra positively oriented':
        return {'knot': nm, 'skip': 'not hyperbolic'}
    cv = M.complex_volume()
    vol, cs = mp.mpf(float(cv.real)), mp.mpf(float(cv.imag))
    sh = [mp.mpc(complex(z).real, complex(z).imag) for z in M.tetrahedra_shapes('rect', bits_prec=53)]
    n = len(sh)
    T = mp.mpc(0,1)*(vol + mp.mpc(0,1)*cs)          # i(vol + i cs)
    S = sum(R(z) for z in sh) - n*pi**2/6
    defect = T - S
    # lattice: basis vectors (pi i/2) log z_j and (pi i/2) log(1-z_j)
    basis = []
    for z in sh:
        basis.append(mp.mpc(0,1)*pi/2*mp.log(z))
        basis.append(mp.mpc(0,1)*pi/2*mp.log(1 - z))
    # least squares for real coefficients
    A = mp.matrix(len(basis), 2); b = mp.matrix(2, 1)
    for j, v in enumerate(basis):
        A[j, 0] = mp.re(v); A[j, 1] = mp.im(v)
    b[0] = mp.re(defect); b[1] = mp.im(defect)
    # exact normal equations
    ATA = mp.matrix(2, 2); ATb = mp.matrix(2, 1)
    for i in range(2):
        for k in range(2):
            ATA[i, k] = sum(A[j, i]*A[j, k] for j in range(len(basis)))
        ATb[i] = sum(A[j, i]*b[j] for j in range(len(basis)))
    try:
        sol = mp.lu_solve(ATA, ATb)
    except Exception:
        return {'knot': nm, 'n': n, 'vol': float(vol), 'cs': float(cs),
                'cont_ok': False, 'lattice_ok': False, 'note': 'singular normal equations'}
    # residual
    pred = [sol[0]*mp.re(v) + sol[1]*mp.im(v) for v in basis]
    res = max(abs(pred[j] - b[j]) for j in range(len(basis)))
    # can the two fitted reals be realised by integers on the SAME basis? each basis vector
    # needs its own integer coefficient, so the problem is an integer feasibility one:
    # solve min ||Bc - defect|| over c in Z^{2n}
    Bm = mp.matrix(len(basis), 2*len(basis))
    for j in range(len(basis)):
        Bm[j, 2*j] = mp.re(basis[j]); Bm[j, 2*j+1] = mp.im(basis[j])
    # integer solution: use the fact that we only need SOME integers; solve over Z by
    # rounding a least-squares solution in the (2n)-dimensional coefficient space
    BtB = Bm.T*Bm; Btb = Bm.T*b
    try:
        cf = mp.lu_solve(BtB + mp.eye(2*len(basis))*mp.mpf('1e-30'), Btb)
    except Exception:
        cf = [mp.mpf(0)]*(2*len(basis))
    ci = [int(mp.nint(cf[i])) for i in range(2*len(basis))]
    resid_int = max(abs(sum(mp.re(basis[j])*ci[2*j] + mp.im(basis[j])*ci[2*j+1] for j in range(len(basis))) - b[k])
                    for k in range(2))
    return {'knot': nm, 'n': n, 'vol': float(vol), 'cs': float(cs),
            'defect_abs': float(abs(defect)),
            'defect_mod_pi2over6': float(abs(defect) % (pi**2/6)),
            'cont_ok': abs(defect) < mp.mpf('1e-12'),
            'lattice_ok': resid_int < mp.mpf('1e-10'),
            'int_resid': float(resid_int),
            'coeffs': ci}

if __name__ == '__main__':
    names = sys.argv[1:]
    out = '.scratch/c5_windings.jsonl'
    done = set()
    if os.path.exists(out):
        for line in open(out):
            try: done.add(json.loads(line)['knot'])
            except Exception: pass
    with open(out, 'a') as fh:
        for nm in names:
            if nm in done: continue
            r = analyse(nm)
            fh.write(json.dumps(r) + '\n'); fh.flush()
            if 'skip' in r:
                print(f"{nm:10s} skipped: {r['skip']}")
            else:
                print(f"{nm:10s} n={r['n']:3d} vol={r['vol']:10.6f} cs={r['cs']:10.6f} "
                      f"cont_ok={r['cont_ok']} lattice_ok={r['lattice_ok']} resid={r['int_resid']:.2e}")
