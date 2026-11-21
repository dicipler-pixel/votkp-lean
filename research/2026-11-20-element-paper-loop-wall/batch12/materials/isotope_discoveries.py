"""Join a SHA-pinned FRIB discovery catalogue to the local IAEA level ledger.

Usage: python isotope_discoveries.py [--catalogue IsotopeDiscoveryMap.json]
Supply --first 66 --last 70 --directory ../..//batch14/materials for Dy to Yb.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen

URL = 'https://people.frib.msu.edu/~chenj/isotope-discovery/IsotopeDiscoveryMap.json'
SHA256 = 'bae212ca9f191447a19a153cfe9d6c45450298284439c23b308ad947c1539b41'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--catalogue', type=Path)
    parser.add_argument('--directory', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--first', type=int, default=56)
    parser.add_argument('--last', type=int, default=60)
    args = parser.parse_args()
    source = args.catalogue.read_bytes() if args.catalogue else urlopen(URL, timeout=60).read()
    if hashlib.sha256(source).hexdigest() != SHA256:
        raise SystemExit('FRIB catalogue changed. Compare and explicitly version the new release.')
    with (args.directory / 'isotopes.csv').open() as f:
        ground_states = {(int(r['Z']), int(r['A'])) for r in csv.DictReader(f)}
    rows = []
    for isotope in json.loads(source).values():
        if isotope.get('status') != 'DISCOVERED':
            continue
        z = int(isotope['z'])
        if not args.first <= z <= args.last:
            continue
        a, n = int(isotope['a']), int(isotope['n'])
        assert a == z + n
        paper = isotope['reference']
        rows.append(dict(symbol=isotope['elementSymbol'], Z=z, A=a, N=n, net_up=2*z+n,
                         net_down=z+2*n, in_ground_state_snapshot=(z,a) in ground_states,
                         discovery_year=isotope['year'], publication_year=paper['year'],
                         FRIB_method=isotope.get('method',''), laboratory=isotope.get('lab',''),
                         NSR=paper.get('nsrKeynumber',''), doi=paper.get('doi','')))
    rows.sort(key=lambda r: (r['Z'],r['A']))
    ids = {(r['Z'],r['A']) for r in rows}
    if not ground_states <= ids or len(ids) != len(rows):
        raise SystemExit(f'Duplicate discovery or missing ground-state id: {ground_states - ids}')
    with (args.directory / 'isotope_discoveries.csv').open('w') as f:
        writer = csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    print(f'{len(rows)} FRIB discoveries; {len(ground_states)} IAEA ground-state rows; '
          f'{len(ids - ground_states)} additional discoveries')

if __name__ == '__main__':
    main()
