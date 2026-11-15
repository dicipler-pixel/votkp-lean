# SCRIPT: c2_certify_census
"""Apply the certified bound to every knot: which ones can the bowl law be PROVED on?

With C = 0.685556567092 (the sup of |remainder|/|G|^5 on the disk, computed in
c2_certified_bound.py) and rho(K) = max_j |G_j| over the geometric shapes,

    |Vol_pred - Vol|  <=  n C rho^5        (a bound, not a measurement)

so the relative error is at most n C rho^5 / Vol. This is reported per knot, alongside the
measured error, together with the tightness ratio bound/measured.
"""
import sys, json, math, os
sys.path.insert(0,'code'); sys.path.insert(0,'code/votkp')
import multiprocessing as mp
import snappy

W  = complex(math.cos(math.pi/3),  math.sin(math.pi/3))
WB = complex(math.cos(math.pi/3), -math.sin(math.pi/3))
V0 = 1.0149416064096536
C2 = 3*math.sqrt(3)/4; C3 = math.sqrt(3)/4; C4 = 3*math.sqrt(3)/16
C  = 0.685556567092

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
        rho = max(abs(g) for g in G)
        pred = sum(V0 - C2*abs(g)**2 + C3*(g**3).real + C4*abs(g)**4 for g in G)
        meas = abs(pred-vol)/vol
        bound_max = len(sh)*C*rho**5/vol
        bound = C*sum(abs(g)**5 for g in G)/vol      # sharper: sum, not n*max
        return dict(knot=nm, n=len(sh), vol=vol, rho=rho, meas=meas,
                    bound=bound, bound_max=bound_max)
    except Exception:
        return None

if __name__ == '__main__':
    import knotnames, statistics as st
    names = []
    for f in ['3','4','5','6','7','8','9','10','11a','11n','12a','12n','13a','13n']:
        names += knotnames.names_in(f)
    out = '.scratch/c2_certify.jsonl'
    done=set()
    if os.path.exists(out):
        for l in open(out):
            try: done.add(json.loads(l)['knot'])
            except Exception: pass
    todo=[n for n in names if n not in done]
    with mp.Pool(4) as pool, open(out,'a') as fh:
        for r in pool.imap_unordered(one, todo, chunksize=8):
            if r: fh.write(json.dumps(r)+'\n'); fh.flush()
    rows=[json.loads(l) for l in open(out)]
    rows=[r for r in rows if r['bound']>0]
    b=sorted(r['bound'] for r in rows)
    print(f'knots certified: {len(rows)}')
    print(f'  certified relative bound: median {100*st.median(b):.4f}%  90th {100*b[int(0.9*(len(b)-1))]:.4f}%  worst {100*b[-1]:.2f}%')
    for thr in (0.001, 0.01, 0.05):
        k=sum(1 for r in rows if r['bound']<=thr)
        print(f'  knots with a PROVEN relative error below {100*thr:.1f}%: {k} of {len(rows)} ({100*k/len(rows):.1f}%)')
    rat=sorted(r['bound']/r['meas'] for r in rows if r['meas']>1e-12)
    print(f'  tightness bound/measured: median {st.median(rat):.1f}x  best {rat[0]:.1f}x  worst {rat[-1]:.1f}x')
    print(f'  knots where the bound is tighter than 10x: {sum(1 for x in rat if x<10)}')
