"""Ground-mass signs from raw cyclotron ratios; dimensionless-scale counterexample."""
import csv
import gzip
import hashlib
import json
from decimal import Decimal as D
from fractions import Fraction as F
from pathlib import Path

HERE=Path(__file__).resolve().parent
ARCH=HERE.parents[3]/'data/element_thresholds_20261011.json.gz'
assert hashlib.sha256(ARCH.read_bytes()).hexdigest()=='75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
with gzip.open(ARCH,'rt') as f:
    records=json.load(f,parse_float=F)['records']
dy,ho=records[65:67]
assert (dy['symbol'],ho['symbol'])==('Dy','Ho')
states=[a['thresholds'] for a in (dy,ho)]
def inputs(level):
    return F(level['IE_eV']),F(level['unc_eV'])
# Table 2 of Schweiger et al., Nat. Phys. (2024), reported R−1 and widths.
traps={38:('0.000000018623','3.0e-12'),39:('0.000000011307','4.1e-12'),40:('0.000000011516','3.5e-12')}
def fmt(n):
    return format(D(n.numerator)/D(n.denominator),'.6f')
delta=[F(0)]
width=[F(0)]
for a,b in zip(*states):
    x,dx=inputs(a)
    y,dy_width=inputs(b)
    delta.append(delta[-1]+y-x)
    width.append(width[-1]+dx+dy_width)
q0=F('2863.2')
q0u=F('0.6')
def signs(scale):
    return [q0+scale*v>0 for v in delta]
assert signs(1)==[True]*57+[False]*10 and all(signs(F(1,100)))
for table in states:
    energies=[inputs(v)[0] for v in table]
    for a,b in zip(energies,energies[1:]):
        c=F(1,100)
        assert b/a==(c*b)/(c*a) and (b-a)/(b+a)==(c*b-c*a)/(c*b+c*a)
# Strict scale bounds for the full CENTRAL sign sequence, not just the two adjacent q.
min_scale,q_lower=max((q0/-delta[q],q) for q in range(57,67))
max_scale,q_upper=min((q0/-delta[q],q) for q in range(57) if delta[q]<0)
print('Same central signs iff scale is strictly between',fmt(min_scale),fmt(max_scale),'endpoints at q',q_lower,q_upper)
# Use wider-than-input mass and conversion bounds, deliberately for enclosure.
# For q=38..40, mDy neutral in (162.92873,162.92875)u, m_e <0.00055u,
# and 0<each of the first 40 I_Dy<511000 eV. Hence 162.89u < M_Dy(q) <162.93u.
# These very broad conversion and mass limits are sufficient and checked numerically.
assert all(inputs(t)[0]+inputs(t)[1]<510000 for t in states[0][:40])
assert F('162.92873')-40*F('.00055')>F('162.89')
rows=[]
for start,(value,err) in traps.items():
    ratio,u=F(value),F(err)
    lo=(ratio-u)*F('162.89')*931_000_000
    hi=(ratio+u)*F('162.93')*932_000_000
    for q in range(start,67):
        offset=delta[q]-delta[start]
        spread=width[q]-width[start]
        l,h=lo+offset-spread,hi+offset+spread
        assert l>0 if q<=56 else h<0
        rows.append([start,q,fmt(lo),fmt(hi),fmt(offset),fmt(spread),fmt(l),fmt(h)])
with (HERE/'direct_trap_bounds.csv').open('w') as f:
    writer=csv.writer(f,lineterminator='\n')
    writer.writerow('anchor_q q direct_anchor_lo_eV direct_anchor_hi_eV archive_increment_eV archive_increment_width_eV lower_eV upper_eV'.split())
    writer.writerows(rows)
for row in rows:
    if row[1] in (56,57):
        print(*row)
