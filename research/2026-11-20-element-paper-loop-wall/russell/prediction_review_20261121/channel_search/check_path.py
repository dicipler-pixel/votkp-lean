"""Continue a state-selected removal path before the excited ion radiates."""
import csv
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import sys

archive=Path(sys.argv[1])
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
from decimal import Decimal
records={r['symbol']:r for r in json.load(gzip.open(archive,'rt'),parse_float=Decimal)['records']}
writer=csv.writer(sys.stdout)
writer.writerow('symbol final_level J I2_exc_eV I3_from_exc_eV I4_ground_eV z1 z2 z3 Gamma2 I2_plus_I3_eV product_z'.split())
with Path(__file__).with_name('nist_levels.csv').open() as f:
    for row in csv.DictReader(f):
        entries={x['q']:Q(x['IE_eV']) for x in records[row['symbol']]['thresholds']}
        a,b,c,d=[entries[i] for i in range(4)]
        delta=Q(row['excitation_cm-1'])/Q('8065.543937')
        up,down=b+delta,c-delta
        z1,z2,z3=up/a,down/up,d/down
        assert up+down==b+c and z1*z2*z3==d/a
        assert up+c!=b+c and 0<z2<1 and z2*z2-6*z2+1>0
        vals=[up,down,d,z1,z2,z3,(z2-1)/(z2+1),b+c,z1*z2*z3]
        writer.writerow([row['symbol'],row['final_level'],row['J'],*[f'{float(x):.12f}' for x in vals]])
