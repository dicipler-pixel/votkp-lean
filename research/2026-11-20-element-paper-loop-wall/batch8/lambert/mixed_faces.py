"""Exact two-face checks for the internal peel clocks of Kr through Zr."""
import argparse
import contextlib
import csv
import gzip
import hashlib
import io
import itertools
import json
import math
import runpy
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

ARCHIVE_SHA = '75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
CORE = {'He': 2, 'Ne': 10, 'Ar': 18, 'Kr': 36}
# Independent central-value inputs, eV. Ning & Lu 2022, Table 2,
# https://doi.org/10.1063/5.0080243 ; Y also Zhang et al. 2023,
# https://pubmed.ncbi.nlm.nih.gov/36859075/ . Kr has no bound ground anion.
AFFINITY = {'Rb': Q('0.485916'), 'Sr': Q('0.05206'), 'Y': Q('0.31129'), 'Zr': Q('0.433283')}


def gamma(z):
    if z < 1:
        raise ValueError('This script enumerates forward steps with z >= 1.')
    return (z - 1) / (z + 1)


def classify(a, b):
    displacement = gamma(a)**2 + gamma(b)**2 - 1
    if displacement == 0:
        return 'ideal'
    return 'open' if displacement > 0 else 'closes'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('repo', type=Path, help='votkp-lean checkout')
    parser.add_argument('--csv', type=Path, help='write all unordered pairs including equal pairs')
    args = parser.parse_args()
    data = args.repo / 'data/element_thresholds_20261011.json.gz'
    if hashlib.sha256(data.read_bytes()).hexdigest() != ARCHIVE_SHA:
        raise ValueError('Archive differs from the batch-8 pin.')
    with gzip.open(data, 'rt') as fh:
        elements = json.load(fh, parse_float=Q, parse_int=int)['records']
    # Reuse Claude's actual disk-circle intersection function as a separate numeric check.
    disk_path = args.repo / 'research/2026-11-20-element-paper-loop-wall/checks/lambert_jump_check_v1.py'
    with contextlib.redirect_stdout(io.StringIO()):
        disk = runpy.run_path(str(disk_path))['closes']
    for t in range(2, 21):
        a, b = Q(t*t), Q(t+1,t-1)**2
        assert classify(a,b) == classify(b,a) == 'ideal'
        assert classify(a,b-Q(1,1000)) == 'closes'
        assert classify(a,b+Q(1,1000)) == 'open'
    assert gamma(Q(9)) == Q(4,5) and gamma(Q(4)) == Q(3,5)
    assert classify(Q(9),Q(4)) != 'open'  # deliberately false strict interpretation
    # The circle model is singular for z=1; the limiting exact rule remains defined.
    assert classify(Q(1), Q(1000)) == 'closes'
    faces = {name:{} for name in [*CORE, 'anion']}
    for atom in elements:
        z, sym = atom['Z'], atom['symbol']
        if not 36 <= z <= 40:
            continue
        e = {q['q']:Q(q['IE_eV']) for q in atom['thresholds']}
        for core, n in CORE.items():
            charge = z-n-1
            if charge >= 0:
                faces[core][sym] = e[charge+1] / e[charge]
        if sym in AFFINITY:
            faces['anion'][sym] = e[0] / AFFINITY[sym]
    rows = []
    classes = Counter()
    for category, ratios in faces.items():
        for (sa, a), (sb, b) in itertools.combinations_with_replacement(ratios.items(), 2):
            ga, gb = gamma(a), gamma(b)
            result = classify(a,b)
            assert result == classify(b,a)
            assert result != 'ideal' and disk(float(a),float(b)) == (result == 'closes')
            classes[category,result] += 1
            rows.append([category,sa,sb,str(a),str(b),str(ga**2+gb**2-1),result])
    if args.csv:
        with args.csv.open('w',newline='') as f:
            w = csv.writer(f,lineterminator='\n')
            w.writerow(['face_type','element_a','element_b','exact_z_a','exact_z_b','exact_sum_gamma_sq_minus_one','classification'])
            w.writerows(rows)
    print('Exact boundary controls: 19 tangencies and 38 strict perturbations passed.')
    for category in faces:
        group = {k:classes[category,k] for k in ('closes','ideal','open')}
        print(category, group)
    print(f'Claude disk control: {len(rows)} central-value pairs, no disagreements.')
    print('Kr-core rows: element pair | gamma_a^2 + gamma_b^2 | closure')
    for cat, sa,sb, a,b,d,result in rows:
        if cat == 'Kr':
            print(f'{sa}/{sb}: {float(1+Q(d)):.8f}  {result}')
    a=faces['Kr']['Rb']
    crit=((math.sqrt(a)+1)/(math.sqrt(a)-1))**2
    print(f'Fixed Rb critical partner z: {crit:.8f}; observed Sr opening: {float(faces["Kr"]["Sr"]):.8f}.')
    print('Earlier last-outside/first-inside brackets, exact source values:')
    for num, left, right in [(2,6,7),(10,11,12),(18,19,20),(36,37,38),(54,55,56)]:
        pair = []
        for z in (left,right):
            th = elements[z-1]['thresholds']
            q = z-num-1
            e, f = th[q],th[q+1]
            assert (e['q'],f['q']) == (q,q+1)
            u, v = Q(e['IE_eV']), Q(f['IE_eV'])
            du, dv = Q(e['unc_eV']), Q(f['unc_eV'])
            pair.append((v/u, (v-dv)/(u+du), (v+dv)/(u-du)))
        (a,loA,hiA),(b,loB,hiB)=pair
        assert classify(a,a) == 'open' and classify(b,b) == 'closes'
        result=classify(a,b)
        assert classify(loA,loB)==classify(hiA,hiB)==result
        assert disk(float(a),float(b)) == (result=='closes')
        threshold=((math.sqrt(a)+1)/(math.sqrt(a)-1))**2
        print(f"{elements[left-1]['symbol']}/{elements[right-1]['symbol']}: "
              f"power sum {float(gamma(a)**2+gamma(b)**2):.8f}, {result}, "
              f"partner threshold {threshold:.8f}, observed {float(b):.8f}; "
              f"margin [{float(gamma(loA)**2+gamma(loB)**2-1):+.8f}, "
              f"{float(gamma(hiA)**2+gamma(hiB)**2-1):+.8f}]")
    closest = min(rows,key=lambda r: abs(Q(r[5])))
    print(f'Closest sampled pair: {closest[0]} {closest[1]}/{closest[2]}, signed power surplus {float(Q(closest[5])):.8f}.')


if __name__ == '__main__':
    main()
