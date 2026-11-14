# SCRIPT: c2_bowl_orders
"""C2b, four orders of the bowl law compared on the same knots.

For the geometric solution, with G_j = (z_j-w)/(z_j-wbar):
  order 0   Vol ~ sum_j V0                                        (pieces at full volume)
  order 2   Vol ~ sum_j [V0 - (3 sqrt3/4)|G_j|^2]                 (quadratic bowl)
  order 3   ...        + (sqrt3/4) Re(G_j^3)                      (the racket term)
  order 4   ...        + (3 sqrt3/16)|G_j|^4                      (quartic)
The series is D = V0 - (3 sqrt3/4)|G|^2 + (sqrt3/8)(G^3+conj G^3) + (3 sqrt3/16)|G|^4
+ O(|G|^5), and (sqrt3/8)(G^3+conj G^3) = (sqrt3/4) Re(G^3).

Pre-registered rule: CONFIRMED that the quartic term helps iff the median relative error
at order 4 is below that at order 2 and below that at order 3. Reported per knot and over
the whole census.
"""
import sys, json, math
sys.path.insert(0,'code'); sys.path.insert(0,'code/votkp')
import multiprocessing as mp
import snappy

W  = complex(math.cos(math.pi/3),  math.sin(math.pi/3))
WB = complex(math.cos(math.pi/3), -math.sin(math.pi/3))
V0 = 1.0149416064096536
C2 = 3*math.sqrt(3)/4
C3 = math.sqrt(3)/4
C4 = 3*math.sqrt(3)/16

def sn(nm):
    import re
    m = re.match(r'^(\d+)([an])_(\d+)$', nm)
    return f'{m.group(1)}{m.group(2)}{m.group(3)}' if m else nm

def one(nm):
    try:
        M = snappy.Link(sn(nm)).exterior()
        if M.solution_type() != 'all tetrahedra positively oriented': return None
        vol = float(M.volume())
        sh = [complex(z) for z in M.tetrahedra_shapes('rect', bits_prec=53)]
        G = [(z-W)/(z-WB) for z in sh]
        p = [0.0, 0.0, 0.0]                    # orders 2, 3, 4
        for g in G:
            q = abs(g)**2
            p[0] += V0 - C2*q
            p[1] += V0 - C2*q + C3*(g**3).real
            p[2] += V0 - C2*q + C3*(g**3).real + C4*q*q
        return dict(knot=nm, n=len(sh), vol=vol,
                    e0=abs(len(sh)*V0 - vol)/vol,
                    e2=abs(p[0]-vol)/vol, e3=abs(p[1]-vol)/vol, e4=abs(p[2]-vol)/vol)
    except Exception:
        return None

if __name__ == '__main__':
    import knotnames, statistics as st, os
    names = []
    fams = sys.argv[1:] or ['3','4','5','6','7','8','9','10','11a','11n','12a','12n','13a','13n']
    for f in fams: names += knotnames.names_in(f)
    out = '.scratch/c2_orders.jsonl'
    done = set()
    if os.path.exists(out):
        for l in open(out):
            try: done.add(json.loads(l)['knot'])
            except Exception: pass
    todo = [n for n in names if n not in done]
    print(f'{len(names)} knots, {len(todo)} to run', flush=True)
    with mp.Pool(4) as pool, open(out,'a') as fh:
        for r in pool.imap_unordered(one, todo, chunksize=8):
            if r: fh.write(json.dumps(r)+'\n'); fh.flush()
    rows = [json.loads(l) for l in open(out)]
    for lbl, key in [('order 0 (full volume)','e0'), ('order 2 (quadratic)','e2'),
                     ('order 3 (+ cubic)','e3'), ('order 4 (+ quartic)','e4')]:
        v = sorted(r[key] for r in rows)
        print(f"{lbl:24s} n={len(v):6d}  median {100*st.median(v):7.3f}%  "
              f"90th {100*v[int(0.9*(len(v)-1))]:7.3f}%  worst {100*v[-1]:14.3f}%  "
              f"({max(rows, key=lambda r: r[key])['knot']})")
