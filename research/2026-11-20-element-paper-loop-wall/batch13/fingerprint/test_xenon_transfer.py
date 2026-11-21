"""Run batch 9's frozen classifiers on the unretuned 54-electron family."""
import csv
import gzip
import hashlib
import itertools
import json
import math
import runpy
import statistics
from collections import Counter
from decimal import Decimal, localcontext
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parents[1]
ARCHIVE = PAPER.parents[1] / 'data/element_thresholds_20261011.json.gz'
old = runpy.run_path(str(PAPER/'batch9/fingerprint/test_ladder_shape.py'))
assert hashlib.sha256(ARCHIVE.read_bytes()).hexdigest() == old['DIGEST']
with gzip.open(ARCHIVE, 'rt') as f:
    atoms = {a['Z']:a for a in json.load(f, parse_float=Decimal)['records']}
MODES = ('first_two_contrast', 'endpoint', 'sorted', 'ordered', 'first_two')

def window(core, offset, q):
    z = core+offset+q
    t = atoms[z]['thresholds'][q:q+5]
    assert len(t) == 5 and [v['q'] for v in t] == list(range(q,q+5))
    span, shares = old['composition']([float(v['IE_eV']) for v in t])
    return old['Window'](core, offset, q, z, span, shares)

def fit(training, mode):
    return [tuple(map(statistics.fmean, zip(*(old['dims'](w,mode) for w in training if w.offset==c))))
            for c in range(3)]

def predict(values, centers):
    distances = [sum(abs(x-y) for x,y in zip(values,center)) for center in centers]
    return min(range(3), key=distances.__getitem__)

def dec(x):
    return Decimal(x)

def extrema(thresholds):
    """All order-chamber vertices suffice for a linear-fractional contrast in log energies."""
    if any(t['unc_eV'] is None for t in thresholds):
        return None
    bound = [(dec(t['IE_eV'])-dec(t['unc_eV']), dec(t['IE_eV'])+dec(t['unc_eV'])) for t in thresholds]
    assert min(lo for lo,_ in bound)>0 and bound[0][1]<bound[-1][0]
    ends = {e for interval in bound for e in interval}
    grids = [sorted(e for e in ends if lo<=e<=hi) for lo,hi in bound]
    # Every chamber vertex is here; extra feasible points cannot widen the true extrema.
    with localcontext() as ctx:
        ctx.prec=48
        logs = {e:e.ln() for e in ends}
        ds=[]
        for point in itertools.product(*grids):
            steps = [logs[b]-logs[a] for a,b in zip(point, point[1:])]
            ds.append((steps[0]-steps[1])/sum(map(abs,steps)))
    return min(ds),max(ds)

def main():
    training = [window(c,o,q) for c,o,q in itertools.product((10,18,36),range(3),range(8))]
    tests = [window(54,o,q) for o,q in itertools.product(range(3),range(8))]
    assert set(w.z for w in training).isdisjoint(w.z for w in tests)
    centers = {mode:fit(training,mode) for mode in MODES}
    cen = centers['first_two_contrast']
    neg,pos = (cen[2][0]+cen[0][0])/2, (cen[0][0]+cen[1][0])/2
    assert abs(neg+.1639453)<1e-7 and abs(pos-.2832956)<1e-7
    tally=Counter(); counts=Counter(); box_counts=Counter()
    print('Training D centroids for offsets 0,1,2:',*[c[0] for c in cen])
    print('Fixed D boundaries:',neg,pos)
    with (HERE/'xenon_predictions.csv').open('w',newline='') as f:
        out=csv.writer(f,lineterminator='\n')
        out.writerow(('Z','symbol','q','starting_electrons','actual_offset','input_grades','D','D_box_min','D_box_max',
                      'possible_predictions_box',*('predict_'+m for m in MODES)))
        for w in tests:
            t=atoms[w.z]['thresholds'][w.charge:w.charge+5]
            preds=[predict(old['dims'](w,m),centers[m]) for m in MODES]
            for m,p in zip(MODES,preds):
                counts[m] += p==w.offset
            tally[w.offset,preds[0]]+=1
            bounds=extrema(t)
            if bounds:
                lo,hi=map(float,bounds)
                possible=[label for label,mn,mx in [(2,-math.inf,neg),(0,neg,pos),(1,pos,math.inf)] if lo<=mx and hi>=mn]
                assert min(abs(x-y) for x in (lo,hi) for y in (neg,pos))>1e-12
                status='certain correct' if possible==[w.offset] else 'certain miss' if w.offset not in possible else 'ambiguous'
                box=[f'{lo:.10f}',f'{hi:.10f}',','.join(map(str,possible))]
            else:
                status='incomplete';box=['','','']
            box_counts[status]+=1
            out.writerow((w.z,atoms[w.z]['symbol'],w.charge,54+w.offset,w.offset,''.join(v['grade'] for v in t),
                           f'{w.shares[0]-w.shares[1]:.10f}',*box,*preds))
    print('Central confusion actual rows 0,1,2; predicted columns 0,1,2:')
    for i in range(3):
        print(*(tally[i,j] for j in range(3)))
    print('Scores / 24:',dict(counts))
    print('Primary test boxes:',dict(box_counts))

if __name__=='__main__':
    main()
