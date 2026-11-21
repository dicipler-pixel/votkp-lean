"""Audit the printed energy table for a complete range against the pinned archive.

Usage: python check_batch_range_v2.py ARCHIVE CSV ZFIRST ZLAST [--places 6]
Anion affinities are external inputs; compare them with the cited affinity table separately.
"""
import argparse
import csv
import gzip
import hashlib
import json
import re
import sys
from decimal import Decimal
from fractions import Fraction as F
from pathlib import Path

ARCHIVE_SHA256 = '75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
COLUMNS = {'Z', 'symbol', 'k', 'IE_k (eV)', 'z_k', 'Gamma_k', 'source'}


def check(archive_path, table_path, first, last, places):
    if hashlib.sha256(archive_path.read_bytes()).hexdigest() != ARCHIVE_SHA256:
        raise ValueError('archive SHA-256 differs from the pinned October input')
    with gzip.open(archive_path, 'rt') as inp:
        atoms = {a['Z']: a for a in json.load(inp, parse_float=Decimal)['records']}
    if first > last or any(z not in atoms for z in range(first, last+1)):
        raise ValueError('invalid element range')
    expected = {(z, k) for z in range(first, last+1) for k in range(z+1)}
    rows = {}
    with table_path.open(newline='') as inp:
        reader = csv.DictReader(inp)
        if not COLUMNS.issubset(reader.fieldnames or []):
            raise ValueError('missing printed CSV column')
        for r in reader:
            z, k = int(r['Z']), int(r['k'])
            if not first <= z <= last:
                continue
            if (z, k) in rows:
                raise ValueError(f'duplicate row at {z=} {k=}')
            rows[z, k] = r
    if rows.keys() != expected:
        raise ValueError(f'missing rows {sorted(expected-rows.keys())}, extra rows {sorted(rows.keys()-expected)}')
    if places < 1:
        raise ValueError('supply at least one decimal place')
    number = re.compile(rf'-?\d+\.\d{{{places}}}\Z')
    tolerance = F(1, 2*10**places)
    n_energy = n_ordinary = n_ea = 0
    outside = []
    errors = []
    for z, k in sorted(rows):
        atom = atoms[z]
        row = rows[z, k]
        sym = atom['symbol']
        where = f'{sym} k={k}'
        if row['symbol'] != sym:
            errors.append(f'{where}: symbol {row["symbol"]!r}')
        energy = row['IE_k (eV)'].strip()
        rz, rg = row['z_k'].strip(), row['Gamma_k'].strip()
        if k:
            threshold = atom['thresholds'][k-1]
            if threshold['q'] != k-1:
                raise ValueError(f'{where}: charge mismatch in archive')
            a = F(threshold['IE_eV'])
            n_energy += 1
            if not energy or F(energy) != a:
                errors.append(f'{where}: printed energy {energy!r} vs pinned {a}')
        elif energy:
            a = F(energy)
            n_ea += 1
            if a <= 0:
                raise ValueError(f'{where}: bound anion requires positive EA')
        else:
            if rz or rg or not row['source'].strip():
                errors.append(f'{where}: missing EA requires blank ratio fields and a status')
            continue
        if k == z:
            if rz or rg:
                errors.append(f'{where}: terminal row has a ratio')
            continue
        b = F(atom['thresholds'][k]['IE_eV'])
        ratio, gamma = b/a, (b-a)/(b+a)
        if k:
            n_ordinary += 1
        for name, printed, value in [('z', rz, ratio), ('Gamma', rg, gamma)]:
            if not number.fullmatch(printed) or abs(F(printed)-value) > tolerance:
                errors.append(f'{where}: {name} {printed!r}, exact {value}')
        if 2*(b-a)**2 > (a+b)**2:
            outside.append((sym, k))
    if errors:
        raise ValueError('\n'.join(errors))
    return n_energy, n_ordinary, n_ea, outside


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive', type=Path)
    parser.add_argument('csv', type=Path)
    parser.add_argument('first', type=int)
    parser.add_argument('last', type=int)
    parser.add_argument('--places', type=int, default=6)
    args = parser.parse_args()
    try:
        e, n, a, out = check(args.archive, args.csv, args.first, args.last, args.places)
    except (ValueError, KeyError, ZeroDivisionError) as exc:
        sys.exit(str(exc))
    print(f'{e} exact archive energies; {n} ordinary pairs; {a} anion pairs with externally supplied EA')
    print('Outside:', out)
