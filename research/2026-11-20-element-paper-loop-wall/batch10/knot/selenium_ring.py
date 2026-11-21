"""Project the published beta-Se8 ring along fractional x; standard library only."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import re
import sys


def product(a, b):
    endpoints = [x*y for x in a for y in b]
    return min(endpoints), max(endpoints)


def difference(a, b):
    return a[0] - b[1], a[1] - b[0]


def number(s):
    central, su = re.fullmatch(r'(\d+\.\d+)\((\d+)\)', s).groups()
    value = F(central)
    uncertainty = F(int(su), 10**len(central.split('.')[1]))
    return value - uncertainty, value + uncertainty


def orientations(p):
    """Each projected edge must have each of the other six vertices on its left."""
    margins = []
    for i, a in enumerate(p):
        b = p[(i + 1) % len(p)]
        for j, c in enumerate(p):
            if j in (i, (i+1) % len(p)):
                continue
            by, bz = (difference(u,v) for u,v in zip(b,a))
            cy, cz = (difference(u,v) for u,v in zip(c,a))
            margins.append(difference(product(by,cz),product(bz,cy))[0])
    return margins


path = Path(sys.argv[1])
raw = path.read_bytes()
assert hashlib.sha256(raw).hexdigest() == 'ac27d99b1c3c9e1d9997917fa41086702ed451ea2e80392132ae3b75dd31eb89'
lines = raw.decode().splitlines()
sites = {}
bonds = set()
for line in lines:
    words = line.split()
    if len(words) == 9 and words[5] == 'Uani' and words[0].startswith('Se'):
        sites[int(words[0][2:])] = tuple(number(s) for s in words[2:4])
    if re.fullmatch(r'Se[1-8] Se[1-8] \d+\.\d+\(\d+\)', line):
        bonds.add(frozenset(int(s[2:]) for s in words[:2]))
assert set(sites) == set(range(1,9))
assert bonds == {frozenset([i,i%8+1]) for i in sites}
ring = [sites[i] for i in sorted(sites)]
with_box = orientations(ring)
central = [tuple(((a+b)/2, (a+b)/2) for a,b in t) for t in ring]
nominal = orientations(central)
assert len(with_box) == 48 and min(with_box) > 0
bad = ring.copy()
bad[2],bad[5] = bad[5],bad[2]
assert min(orientations(bad)) < 0
print(f'8 sites, 8 published bonds, {len(nominal)} strict half-plane checks')
print(f'minimum central oriented determinant = {float(min(nominal)):.12f}')
print(f'minimum one-standard-uncertainty-box lower bound = {float(min(with_box)):.12f}')
print('Swapping vertices 3 and 6 fails the convexity certificate.')
