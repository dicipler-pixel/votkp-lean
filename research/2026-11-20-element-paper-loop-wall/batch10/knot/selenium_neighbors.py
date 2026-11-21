"""Exhaust periodic copies and exhibit strict convex-hull separation in fractional coordinates."""
from fractions import Fraction as F
from itertools import product
from math import floor, ceil
import re
from selenium_ring import number, raw

text = raw.decode()
symmetry = re.search(r"_symmetry_equiv_pos_as_xyz\n(.*?)\nloop_",text,re.S)[1].splitlines()
assert symmetry == ["'x, y, z'", "'-x, y+1/2, -z+1/2'", "'-x, -y, -z'", "'x, -y-1/2, z-1/2'"]
assert '_space_group_IT_number           14' in text
assert '_cell_formula_units_Z            4' in text
cells = {k: float(re.search(rf'_cell_{k}\s+([\d.]+)', text)[1]) for k in
         ('length_a','length_b','length_c','angle_alpha','angle_beta','angle_gamma')}
assert min(cells[k] for k in ('length_a','length_b','length_c')) > 0
assert cells['angle_alpha'] == cells['angle_gamma'] == 90 and 0 < cells['angle_beta'] < 180
# A nonsingular affine coordinate change preserves half-space separation and linking.
sites = [tuple(number(s) for s in line.split()[1:4]) for line in text.splitlines()
         if re.match(r'Se[1-8] ',line) and ' Uani ' in line]
ops = [((1,1,1),(0,0,0)), ((-1,1,-1),(0,F(1,2),F(1,2))),
       ((-1,-1,-1),(0,0,0)), ((1,-1,1),(0,F(-1,2),F(-1,2)))]
def transform(site, signs, offsets):
    return [tuple(sorted(s*x+t for x in coord)) for coord,s,t in zip(site, signs, offsets)]

def projections(obj, normal):
    ranges = [transform(vertex,normal,(0,0,0)) for vertex in obj]
    return min(sum(x[0] for x in v) for v in ranges),max(sum(x[1] for x in v) for v in ranges)

basis = [(1,0,0),(0,1,0),(0,0,1)]
box = [projections(sites,n) for n in basis]
axes_checks = []
for k,(s,t) in enumerate(ops):
    obj = [transform(v,s,t) for v in sites]
    other = [projections(obj,n) for n in basis]
    # Every shift outside these exact inclusive integer bounds separates along a coordinate axis.
    shifts = [(ceil(a-d),floor(b-c)) for (a,b),(c,d) in zip(box, other)]
    print(f'operation {k+1}, potentially overlapping integer shifts {shifts}')
    for shift in product(*(range(a,b+1) for a,b in shifts)):
        if k == 0 and shift == (0,0,0): continue
        axes_checks.append((k,shift))
assert len(axes_checks)==0, f'Candidates requiring closer checks: {axes_checks}'
print('Zero distinct candidate boxes. All distinct rings have disjoint convex hulls, including coordinate error boxes.')
