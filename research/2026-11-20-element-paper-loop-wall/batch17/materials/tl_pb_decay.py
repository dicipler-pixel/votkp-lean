"""Same-charge mass gaps in the A=205 system, E*(205Pb) included.

python tl_pb_decay.py  (pinned repository thresholds loaded directly).
"""
import csv
from decimal import Decimal as D
import gzip
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
archive=HERE.parents[3]/'data/element_thresholds_20261011.json.gz'
blob=archive.read_bytes()
assert hashlib.sha256(blob).hexdigest()=='75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
elements={r['symbol']:r['thresholds'] for r in json.loads(gzip.decompress(blob),parse_float=D)['records']}
Q0, Q0u=D('50600'),D('500')
excited, exc_u=D('2329'),D('7')
gap,width=Q0,Q0u
rows=[]
for q in range(82):
    if q:
        tl,pb=elements['Tl'][q-1],elements['Pb'][q-1]
        assert tl['q']==pb['q']==q-1
        gap+=pb['IE_eV']-tl['IE_eV']
        width+=pb['unc_eV']+tl['unc_eV']
    reverse=-gap-excited
    rows.append(dict(q=q,Tl_electrons=81-q,Pb_electrons=82-q,
                     Q_ground_Pb_minus_Tl_eV=gap,ground_lo_eV=gap-width,ground_hi_eV=gap+width,
                     Q_bound_beta_to_excited_Pb_eV=reverse,
                     excited_beta_lo_eV=reverse-width-exc_u,excited_beta_hi_eV=reverse+width+exc_u))
assert all(r['ground_lo_eV']>0 and r['excited_beta_hi_eV']<0 for r in rows[:80])
assert all(r['ground_hi_eV']<0 and r['excited_beta_lo_eV']>0 for r in rows[80:])
source_ground_beta=D('101336')-D('17338')-Q0
assert -gap-source_ground_beta==D('2.5295484')
with (HERE/'tl_pb_decay.csv').open('w') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
print('82 ionic gaps and excited-state channels checked; q79/80 boundary persists in all boxes.')
