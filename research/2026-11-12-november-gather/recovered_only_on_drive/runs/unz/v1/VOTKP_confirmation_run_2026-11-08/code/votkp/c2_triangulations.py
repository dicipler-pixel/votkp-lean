# SCRIPT: c2_triangulations
"""C2. Does the bowl-law error depend on the choice of triangulation?

Pre-registered rule: CONFIRMED as a triangulation-dependence statement iff
  (i)  the canonical (Epstein-Penner) triangulation gives SMALLER error than SnapPy's
       default on the majority of knots, and
  (ii) a randomized triangulation gives much larger error.
If (i) fails or (ii) fails, the reading "the law is about the tetrahedra being near
regular" is not supported by the data.
"""
import sys, json, os
sys.path.insert(0,'code'); sys.path.insert(0,'code/votkp')
import multiprocessing as mp
from c2_knotlaw import one

def job(a):
    nm, w = a
    r = one(nm, w)
    if r: r['which'] = w
    return r

if __name__ == '__main__':
    import knotnames
    names = knotnames.names_in('8')+knotnames.names_in('9')
    todo = [(n, w) for n in names for w in ('default','canonical','random')]
    out = '.scratch/c2_tri.jsonl'
    done=set()
    if os.path.exists(out):
        for l in open(out):
            r=json.loads(l); done.add((r['knot'], r.get('which')))
    todo=[t for t in todo if t not in done]
    print(f'{len(names)} knots x 3 triangulations, {len(todo)} to run', flush=True)
    with mp.Pool(4) as pool, open(out,'a') as fh:
        for r in pool.imap_unordered(job, todo, chunksize=1):
            if r is None: continue
            fh.write(json.dumps(r)+'\n'); fh.flush()
    print('done')
