"""Independent exact audit. Usage: python3 verify_batch8.py archive.json.gz [batch8.csv]."""
import argparse
import csv
import gzip
import hashlib
import json
from collections import Counter
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

# Ning & Lu (2022), Table 3, doi:10.1063/5.0080243; Y primary update
# Zhang et al. (2023), doi:10.1063/5.0124882; Kr has no bound ground-state anion.
AFFINITIES = {
    'Kr': None, 'Rb': ('0.485916', '0.000021'), 'Sr': ('0.05206', '0.00006'),
    'Y': ('0.31129', '0.00022'), 'Zr': ('0.433283', '0.000089'),
}
ARCHIVE_SHA256 = '75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'


def energy_pair(value, uncertainty):
    return Fraction(value), None if uncertainty is None else Fraction(uncertainty)


def call(z):
    value = z*z - 6*z + 1
    return 'outside' if value > 0 else 'inside' if value < 0 else 'on'


def show(x, digits=6):
    # Round once half-up from exact rational, without converting to binary float.
    scale = 10**digits
    rounded = (2*x.numerator*scale + x.denominator) // (2*x.denominator)
    return f'{rounded//scale}.{rounded%scale:0{digits}d}'


def verify(archive, product):
    data = archive.read_bytes()
    if hashlib.sha256(data).hexdigest() != ARCHIVE_SHA256:
        raise ValueError('Archive SHA-256 differs from cae5f49.')
    records = json.loads(gzip.decompress(data), parse_float=Decimal)['records']
    expected = {}
    n_checked = Counter()
    for Z, symbol in enumerate(AFFINITIES,36):
        record = records[Z-1]
        assert (record['Z'],record['symbol']) == (Z,symbol)
        shells = sorted(record['thresholds'], key=lambda t:t['q'])
        assert [t['q'] for t in shells] == list(range(Z))
        energies = {i+1:energy_pair(t['IE_eV'],t['unc_eV']) for i,t in enumerate(shells)}
        if AFFINITIES[symbol] is not None:
            energies[0] = energy_pair(*AFFINITIES[symbol])
        histogram = Counter()
        missing_bounds = []
        sides = []
        for k,(a,da) in sorted(energies.items()):
            n_checked['ordinary energies' if k else 'affinities'] += 1
            if k == Z:
                expected[(Z,k)] = symbol,a,'',''
                continue
            b,db = energies[k+1]
            z = b/a
            reflection = (b-a)/(b+a)
            side = call(z)
            assert (2*reflection**2 > 1) == (side == 'outside')
            expected[(Z,k)] = symbol,a,show(z),show(reflection)
            n_checked['ordinary pairs' if k else 'anion pairs'] += 1
            histogram[side] += 1
            if side == 'outside':
                sides.append(k)
            if None in (da,db):
                missing_bounds.append(k)
            else:
                lo,hi = (b-db)/(a+da), (b+db)/(a-da)
                assert 1 < lo <= z <= hi and call(lo) == side == call(hi)
                n_checked['pairs robust at archive/EA endpoints'] += 1
                if k == Z-36 and k > 0:
                    print(f'{symbol} Kr core  k={k}  z={show(z,9)}  Γ={show(reflection,9)}  z endpoints=[{show(lo,9)}, {show(hi,9)}]  {side}')
        print(f'{symbol}: classified={sum(histogram.values())} outside k={sides}; missing combined uncertainty k={missing_bounds}')
    print(dict(n_checked))
    if product is None:
        return
    with product.open(newline='') as f:
        actual = list(csv.DictReader(f))
    # Accept a blank explanatory k=0 placeholder for unbound Kr; no finite numerical row exists.
    keys = set()
    records_by_z = {r['Z']:r for r in records}
    for row in actual:
        Z,k = int(row['Z']),int(row['k'])
        key = Z,k
        assert key not in keys, ('duplicate key', key)
        keys.add(key)
        if key == (36,0):
            assert row['symbol'] == 'Kr' and all(row[h]=='' for h in ('IE_k (eV)','z_k','Gamma_k'))
            continue
        symbol,a,z,g = expected[key]
        if k:
            assert row['source'] == records_by_z[Z]['thresholds'][k-1]['grade'], ('source grade',key)
        fields = (row['symbol'], Fraction(row['IE_k (eV)']), row['z_k'], row['Gamma_k'])
        assert fields == (symbol,a,z,g), (key, fields, (symbol,a,z,g))
    assert keys-{(36,0)} == set(expected), 'dropped or extra rows'
    print(f'CSV SHA-256: {hashlib.sha256(product.read_bytes()).hexdigest()}')
    print(f'CSV pass: {len(expected)} physical energy rows, 189 displayed pairs, {len(actual)-len(expected)} blank Kr placeholder.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive',type=Path)
    parser.add_argument('product',type=Path,nargs='?')
    args = parser.parse_args()
    verify(args.archive,args.product)
