# SCRIPT: c5_defect
"""C5. What exactly does the continuous part miss, and is it an integer quantity?

Neumann's extended dilogarithm is
    R(z; p, q) = R(z) + (pi i/2)( p log(1-z) + q log z ) - pi^2/6,     R = Rogers dilog,
    i(vol + i cs) = sum_j R(z_j; p_j, q_j),      (p_j, q_j) in Z^2.
So with the windings dropped (p = q = 0),
    defect := i(vol + i cs) - sum_j [ R(z_j) - pi^2/6 ]
must be exactly the correction the integer windings supply.

Pre-registered rules:
  R1  CONFIRMED iff the defect is nonzero for essentially every knot (the continuous part
      alone does not determine CS).
  R2  CONFIRMED iff the defect lies on the lattice (pi i/2)(Z.log(1-z_j) + Z.log z_j) --
      tested NOT by a free lattice fit, which is meaningless in two real dimensions, but
      by checking the structural consequence: the defect is a real multiple of pi^2/6,
      defect = k.pi^2/6, with k a half-integer, for every knot.
  R3  CONFIRMED iff k is an integer (not merely a half-integer), which is the statement
      that strong flattenings exist.
Any knot breaking R2 or R3 is named.
"""
import sys, math, json, os
sys.path.insert(0, 'code')
import mpmath as mp
import snappy
mp.mp.dps = 40
pi = mp.pi

def sn(nm):
    import re
    m = re.match(r'^(\d+)([an])_(\d+)$', nm)
    return f'{m.group(1)}{m.group(2)}{m.group(3)}' if m else nm

def R(z): return mp.polylog(2, z) + mp.log(z)*mp.log(1-z)/2

def analyse(nm):
    M = snappy.Link(sn(nm)).exterior()
    if M.solution_type() != 'all tetrahedra positively oriented':
        return {'knot': nm, 'skip': 'not hyperbolic'}
    cv = M.complex_volume()
    vol, cs = mp.mpf(float(cv.real)), mp.mpf(float(cv.imag))
    sh = [mp.mpc(complex(z).real, complex(z).imag) for z in M.tetrahedra_shapes('rect', bits_prec=53)]
    n = len(sh)
    T = mp.mpc(0,1)*(vol + mp.mpc(0,1)*cs)
    S = sum(R(z) for z in sh) - n*pi**2/6
    defect = T - S
    k = defect/(pi**2/6)
    return {'knot': nm, 'n': n, 'vol': float(vol), 'cs': float(cs),
            'defect_re': float(mp.re(defect)), 'defect_im': float(mp.im(defect)),
            'k_re': float(mp.re(k)), 'k_im': float(mp.im(k)),
            'k_re_near_int': abs(mp.re(k) - mp.nint(mp.re(k))) < 1e-8,
            'k_re_near_half': abs(mp.re(k)*2 - mp.nint(mp.re(k)*2)) < 1e-8,
            'defect_real': abs(mp.im(defect)) < 1e-10,
            'cont_ok': abs(defect) < 1e-12}

if __name__ == '__main__':
    names = sys.argv[1:]
    out = '.scratch/c5_defect.jsonl'
    done = set()
    if os.path.exists(out):
        for line in open(out):
            try: done.add(json.loads(line)['knot'])
            except Exception: pass
    with open(out, 'a') as fh:
        for nm in names:
            if nm in done: continue
            r = analyse(nm)
            fh.write(json.dumps(r)+'\n'); fh.flush()
            if 'skip' in r: print(f"{nm:10s} skip ({r['skip']})"); continue
            print(f"{nm:10s} n={r['n']:2d} k={r['k_re']:+.6f}{r['k_im']:+.1e}i  "
                  f"int={r['k_re_near_int']} half={r['k_re_near_half']} real={r['defect_real']} cont_ok={r['cont_ok']}")
