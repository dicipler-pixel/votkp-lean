# SCRIPT: c2_knotlaw_all
"""C2 (knot half) at scale, over three triangulation choices.

For every hyperbolic knot in the given families we compute the bowl-law prediction on
(a) SnapPy's triangulation, (b) the canonical retriangulation, (c) a randomized
triangulation of the same manifold, and report the error distribution for each. The
point of (c) is that the law is a per-tetrahedron identity only in the limit where each
tetrahedron is near regular; a random triangulation has shapes far from w and the law
should be much worse. That is a falsifiable prediction of the reading.
"""
import sys, json, os, math
sys.path.insert(0, 'code'); sys.path.insert(0, 'code/votkp')
import multiprocessing as mp
from c2_knotlaw import one

def job(args):
    nm, which = args
    return one(nm, which)

if __name__ == '__main__':
    import knotnames
    fams = sys.argv[1].split(',')
    out = sys.argv[2]
    names = []
    for f in fams: names += knotnames.names_in(f)
    done = {}
    if os.path.exists(out):
        for line in open(out):
            r = json.loads(line); done[(r['knot'], r.get('which'))] = r
    todo = [(n, w) for n in names for w in ('default',) if (n, w) not in done]
    print(f'{len(names)} knots, {len(todo)} to run', flush=True)
    with mp.Pool(4) as pool, open(out, 'a') as fh:
        for k, r in enumerate(pool.imap_unordered(job, todo, chunksize=8), 1):
            if r is None: r = {'knot': todo[k-1][0], 'error': 'None'}
            r['which'] = 'default'
            fh.write(json.dumps(r) + '\n'); fh.flush()
            if k % 100 == 0: print(f'  {k}/{len(todo)}', flush=True)
