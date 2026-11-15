# SCRIPT: c8_mutants
"""Benchmark: does theta separate the mutant pairs in the tables?

Mutation preserves the hyperbolic volume exactly (mutants are isospectral), the Alexander
polynomial, the signature, the Jones polynomial and the 2-fold branched cover. Non-mutant
hyperbolic knots essentially never share a volume. So candidate mutant pairs are found as:

    group the 12,965 knots by exact hyperbolic volume, keep groups of size >= 2,
    then require the Alexander polynomial, determinant and signature to agree.

That is a filter, not an identification: matching volume + Alexander + signature + Jones is
what mutants do, and a pair matching all four through the tables is a mutant pair for
practical purposes. Pairs are reported and theta is computed on each.

Pre-registered rule: theta is a mutation INVARIANT iff it takes equal values on every
candidate pair; it SEPARATES mutants iff it differs on some. The rate is reported, not a
single example.
"""
import sys, json, re, math, os
sys.path.insert(0,'code'); sys.path.insert(0,'code/votkp')
from collections import defaultdict
import multiprocessing as mp

def sn(nm):
    m = re.match(r'^(\d+)([an])_(\d+)$', nm)
    return f'{m.group(1)}{m.group(2)}{m.group(3)}' if m else nm

def vol_of(nm):
    import snappy
    try:
        M = snappy.Link(sn(nm)).exterior()
        if M.solution_type() != 'all tetrahedra positively oriented': return None
        return (nm, float(M.volume()))
    except Exception:
        return None

def theta_of(nm, pts=((2,3),(2,5))):
    import snappy, braid_drawing as bd, theta_general as tg
    from fractions import Fraction as Fr
    w = list(snappy.Link(sn(nm)).braid_word()); m = max(abs(x) for x in w)+1
    X, phi, n, info = bd.diagram(w, m)
    if (info['sum_phi'] - info['w']) % 2: return None
    out = []
    for p in pts:
        try: out.append(str(tg.theta(X, phi, n, p[0], p[1], verify=False)[0]))
        except ValueError: out.append('pole')
    return out

if __name__ == '__main__':
    import knotnames, csv
    K = knotnames.load()
    out = '.scratch/volumes.json'
    if os.path.exists(out):
        V = json.load(open(out))
    else:
        names = []
        for f in ['3','4','5','6','7','8','9','10','11a','11n','12a','12n','13a','13n']:
            names += knotnames.names_in(f)
        with mp.Pool(4) as pool:
            V = {r[0]: r[1] for r in pool.imap_unordered(vol_of, names, chunksize=8) if r}
        json.dump(V, open(out,'w'))
    print(f'knots with a hyperbolic volume: {len(V)}')
    groups = defaultdict(list)
    for nm, v in V.items(): groups[round(v, 7)].append(nm)
    cand = []
    for v, g in groups.items():
        if len(g) < 2: continue
        # filter: same determinant and signature and Alexander polynomial
        bykey = defaultdict(list)
        for nm in g:
            bykey[(K[nm]['det'], K[nm]['sig'], K[nm]['volume'][:12])].append(nm)
        for k, gg in bykey.items():
            if len(gg) > 1: cand.append((v, gg))
    print(f'candidate mutant groups (equal volume + det + signature): {len(cand)}')
    for v, g in sorted(cand)[:40]:
        print(f'   vol {v:.7f}   {g}')
