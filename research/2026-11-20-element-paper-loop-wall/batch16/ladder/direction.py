"""Strict-reversal patterns on a chain of closed intervals; ties count as nonreverse."""
import csv
from collections import deque
from fractions import Fraction as F
from itertools import product
from pathlib import Path

DIR = Path(__file__).resolve().parent


def feasible_runs(lo, hi):
    """longest strict descending block of edges ending at each vertex."""
    limit = [0]
    for end in range(1, len(lo)):
        length = 0
        for start in range(end - 1, -1, -1):
            # Every earlier upper bound must exceed every later lower bound.
            if hi[start] <= max(lo[start + 1:end + 1]) or end - start > limit[-1] + 1:
                break
            length += 1
        limit.append(length)
    return limit


def sign_patterns(lo, hi):
    limit = feasible_runs(lo, hi)
    # For each trailing block length retain the count and a maximum-cardinality witness.
    prev = {0: (1, ())}
    for end, max_length in enumerate(limit[1:], 1):
        curr = {0: (sum(n for n,_ in prev.values()), max((r for _,r in prev.values()), key=len))}
        for length, (count, witness) in prev.items():
            if length < max_length:
                curr[length+1] = count, witness + (end,)
        prev = curr
    return sum(n for n,_ in prev.values()), max((r for _,r in prev.values()), key=len), limit


def independent_witness(lo, hi, reverse):
    """Topological propagation of lexicographic (energy, infinitesimal) lower bounds."""
    n = len(lo)
    out = [[] for _ in lo]
    order = [0]*n
    for i in range(n-1):
        strict = i+1 in reverse
        source, target = (i+1,i) if strict else (i,i+1)
        out[source].append((target, int(strict)))
        order[target] += 1
    best = [(v,0) for v in lo]
    todo = deque(i for i,d in enumerate(order) if d == 0)
    while todo:
        i = todo.popleft()
        if best[i] > (hi[i],0):
            return None
        for j, strict in out[i]:
            best[j] = max(best[j], (best[i][0],best[i][1]+strict))
            order[j] -= 1
            if order[j] == 0:
                todo.append(j)
    margins = [(upper-v)/m for upper,(v,m) in zip(hi,best) if m]
    # If leading lower bounds differ, keep their order after materializing the infinitesimal.
    energies = sorted(set(lo))
    margins.extend((b-a)/(n+1) for a,b in zip(energies,energies[1:]))
    eps = min(margins,default=F(1))/2
    vals = [v+m*eps for v,m in best]
    assert all(a <= v <= b for a,v,b in zip(lo,vals,hi))
    assert {k for k in range(1,n) if vals[k-1] > vals[k]} == set(reverse)
    return vals


def run():
    with (DIR/'asd_states_20261121.csv').open() as f:
        atoms = list(csv.DictReader(f))
    fields = ['Z','symbol','single_reverse_edges','touch_only','total_sign_patterns','max_simultaneous',
              'witness_k','adjacent_strict_reversals_possible_at','first_to_touch_k','multiplier']
    with (DIR/'joint_direction.csv').open('w', newline='') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(fields)
        for z, sym in zip(range(76,81), ('Os','Ir','Pt','Au','Hg')):
            data = [r for r in atoms if int(r['Z']) == z]
            E = [F(r['NIST_energy_eV'].strip('[]()')) for r in data]
            U = [F(r['NIST_unc_eV']) for r in data]
            assert all(a < b for a,b in zip(E,E[1:]))
            lo = [e-u for e,u in zip(E,U)]
            hi = [e+u for e,u in zip(E,U)]
            count, best, runs = sign_patterns(lo,hi)
            assert independent_witness(lo,hi,best)
            mult,k = min(((E[i]-E[i-1])/(U[i]+U[i-1]),i) for i in range(1,len(E)))
            row = [z,sym,sum(v>0 for v in runs),sum(a==b for a,b in zip(hi,lo[1:])),
                   count,len(best),' '.join(map(str,best)),' '.join(str(i-1) for i,x in enumerate(runs) if x>=2),k,str(mult)]
            w.writerow(row)
            print(*row,sep=' | ')
    # First interval paths whose two-apart bounds are respectively equal/overlapping.
    for hi in ([F(3),F(4),F(5)],[F(3,1)+F(1,100),F(4),F(5)]):
        lo = [F(1),F(2),F(3)]
        expected = [s for s in ((),(1,),(2,),(1,2)) if independent_witness(lo,hi,s)]
        count,best,_ = sign_patterns(lo,hi)
        assert count == len(expected) and len(best) == max(map(len,expected))
    # Independent solver tests all 256 sign vectors across sixteen four-edge interval chains.
    tested = 0
    for w0,w1,w2,w3 in product((0,2),repeat=4):
        lo = [F(2*i)-u for i,u in enumerate((1,w0,w1,w2,w3))]
        hi = [F(2*i)+u for i,u in enumerate((1,w0,w1,w2,w3))]
        sets = [tuple(i+1 for i,b in enumerate(bits) if b) for bits in product((0,1),repeat=4)]
        valid = [s for s in sets if independent_witness(lo,hi,s) is not None]
        n,best,_ = sign_patterns(lo,hi)
        assert n == len(valid) and len(best) == max(map(len,valid))
        tested += len(sets)
    print('Independent interval chain controls:',tested)


if __name__ == '__main__':
    run()
