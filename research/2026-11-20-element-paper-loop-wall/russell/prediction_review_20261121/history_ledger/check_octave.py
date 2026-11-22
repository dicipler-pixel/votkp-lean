"""Compare the Li–Ne reflection to measured helium-core openings on the pinned archive."""
import csv
import gzip
import hashlib
import json
import sys
from decimal import Decimal as D, getcontext
from pathlib import Path

getcontext().prec = 40
path, output = map(Path, sys.argv[1:3])
records = {r['Z']: r for r in json.loads(gzip.decompress(path.read_bytes()), parse_float=D)['records']}
valences = {z:v for z,v in zip(range(3,11),(1,2,3,4,3,2,1,0))}
def reflect(z):
    return 3 + ((12-z) - 3) % 8

def opening(z):
    ions = {t['q']: t['IE_eV'] for t in records[z]['thresholds']}
    a, b = ions[z-3], ions[z-2]
    return a,b,b/a,(b-a)/(b+a),b*b-6*a*b+a*a

assert list(valences.values())[:7] == list(reversed(list(valences.values())[:7]))
assert list(valences.values()) != list(reversed(list(valences.values())))
assert all(reflect(reflect(z)) == z and valences[z] == valences[reflect(z)] for z in valences)
with output.open('w', newline='') as f:
    w=csv.writer(f); w.writerow(['Z','symbol','reflected_Z','mirror_symbol','common_normal_valence','Li_like_IE_eV','He_like_IE_eV','opening_ratio','Gamma','outside','partner_outside'])
    for z,val in valences.items():
        other = reflect(z); a,b,r,g,sign=opening(z)
        w.writerow([z, records[z]['symbol'], other, records[other]['symbol'], val, a,b,format(r,'.8f'), format(g,'.8f'), sign>0, opening(other)[-1]>0]);
for z in (3,4,5):
    assert (opening(z)[-1] > 0) != (opening(reflect(z))[-1] > 0)
print('SHA256 archive',hashlib.sha256(path.read_bytes()).hexdigest())
