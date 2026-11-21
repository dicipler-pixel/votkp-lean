"""What one independent inequality could resolve in each incomplete three-step chain."""
import csv
import gzip
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

archive = Path(sys.argv[1])
if hashlib.sha256(archive.read_bytes()).hexdigest() != '75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c':
    raise ValueError("Unexpected archive checksum")
with gzip.open(archive, 'rt') as f:
    elements = json.load(f, parse_float=Q)['records']
# Largest inside ratio under the reported endpoint boxes.
cutoff = Q(7576259, 1304450)
writer = csv.writer(sys.stdout, lineterminator='\n')
writer.writerow(['element','IE1_lower_eV','IE4_upper_eV','interior_threshold_min_eV',
                 'interior_threshold_max_eV','counterexample_last_z','example_inside_max_z'])
for Z in (43,45):
    element = elements[Z-1]
    t = element['thresholds']
    a = Q(t[0]['IE_eV']) - t[0]['unc_eV']
    d = Q(t[3]['IE_eV']) + t[3]['unc_eV']
    assert t[1]['unc_eV'] is None and t[2]['unc_eV'] is None
    lo,hi = d/cutoff, cutoff*a
    # Strictly increasing counterexample compatible with both reported endpoints;
    # these constructed intermediates illustrate the information gap only.
    witness = [a,a+Q(1,100),a+Q(1,50),d]
    assert max(v/u for u,v in zip(witness,witness[1:])) == d/witness[2]
    assert 2*(d-witness[2])**2 > (d+witness[2])**2
    # Another admissible chain, taking the encoded central intermediate values.
    encoded = [a,Q(t[1]['IE_eV']),Q(t[2]['IE_eV']),d]
    assert all(lo < e < hi for e in encoded[1:3])
    max_ratio = max(v/u for u,v in zip(encoded, encoded[1:]))
    assert max_ratio < cutoff
    writer.writerow([element['name'],*(f'{float(v):.9f}' for v in (a,d,lo,hi,d/witness[2],max_ratio))])
