#!/usr/bin/env python3
"""The prime-knot list and symmetry types, from the KnotInfo database.

Source: the KnotInfo complete data table (Livingston & Moore), obtained as the
`database_knotinfo` snapshot of 2026-11-01, file knotinfo_data_complete.csv.

symmetry_type is KnotInfo's field: 'chiral' (no symmetry), 'reversible' (only
reversibility), 'negative amphicheiral' / 'positive amphicheiral' (amphichiral,
not reversible), 'fully amphicheiral' (all three).  A knot is AMphichiral iff
it is reachable from its mirror, i.e. iff one of the three amphicheiral labels.
"""
import csv, re, os, functools
CSV = '.scratch/venv/lib/python3.12/site-packages/database_knotinfo/csv_data/knotinfo_data_complete.csv'
AMPH = {'negative amphicheiral', 'positive amphicheiral', 'fully amphicheiral'}

@functools.lru_cache(maxsize=1)
def load():
    csv.field_size_limit(10**9)
    with open(CSV, newline='') as fh:
        rows = list(csv.DictReader(fh, delimiter='|'))
    out = {}
    for r in rows:
        nm = r['name']
        if nm == 'Name':
            continue
        st = (r['symmetry_type'] or '').strip()
        out[nm] = {'cross': int(r['crossing_number']) if r['crossing_number'] else None,
                   'symmetry': st, 'amphichiral': st in AMPH,
                   'det': r['determinant'], 'sig': r['signature'],
                   'volume': r['volume']}
    return out

def family(nm):
    m = re.match(r'^(\d+)([an]?)', nm)
    return m.group(1) + m.group(2)

def names_in(fam):
    d = load()
    sel = [nm for nm in d if family(nm) == fam]
    key = lambda s: tuple(int(x) for x in re.findall(r'\d+', s))
    return sorted(sel, key=key)

def names_upto(c):
    return [nm for nm in names_in('3')+names_in('4')+names_in('5')+names_in('6')+names_in('7')
            +names_in('8')+names_in('9')+names_in('10') if load()[nm]['cross'] <= c]

if __name__ == '__main__':
    d = load()
    print('knots in KnotInfo:', len(d))
    for f in ['3','4','5','6','7','8','9','10','11a','11n','12a','12n','13a','13n']:
        L = names_in(f)
        print(f'{f:5s} {len(L):5d}   amphichiral {sum(d[n]["amphichiral"] for n in L):4d}')
    print('<=10 crossings:', len(names_upto(10)))
