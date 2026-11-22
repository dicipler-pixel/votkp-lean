"""Evaluate the selected nine NIST C III and O III levels against both frozen cutoffs."""
import csv
from decimal import Decimal as D, getcontext
import gzip
import hashlib
import json
from pathlib import Path
import sys

getcontext().prec = 45
archive = Path(sys.argv[1])
expected = '75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
assert hashlib.sha256(archive.read_bytes()).hexdigest() == expected
records = json.load(gzip.open(archive,'rt'), parse_float=D)['records']
cm_per_eV = D('8065.543937')
wall = 3 + 2*D(2).sqrt()
rival = (D('7.576234')/D('1.30447') + D('8.15168')/D('1.3895212')) / 2
rows = csv.DictReader(Path(__file__).with_name('nist_levels.csv').open())
writer = csv.writer(sys.stdout)
writer.writerow('symbol final_level J excitation_cm-1 IE1_eV IE2_eV excitation_eV photon_onset_eV z geometry rival ground_z max_symmetric_level_error_cm-1'.split())
for row in rows:
    symbol,level,J,energy = (row[k] for k in ['symbol','final_level','J','excitation_cm-1'])
    ion = next(r for r in records if r['symbol'] == symbol)
    stages = {x['q']:x for x in ion['thresholds']}
    A,I,third = [D(stages[q]['IE_eV']) for q in (0,1,2)]
    dA,dI = [D(stages[q]['unc_eV']) for q in (0,1)]
    E = D(energy)
    assert E / cm_per_eV < third
    onset = I + E/cm_per_eV
    ratio = onset / A
    margins = []
    for c in [wall,rival]:
        if ratio>c:
            margins.append(E - cm_per_eV * (c*(A+dA) - (I-dI)))
        else:
            margins.append(cm_per_eV * (c*(A-dA) - (I+dI)) - E)
    assert min(margins)>0
    writer.writerow([symbol,level,J,energy,A,I,f'{E/cm_per_eV:.12f}',f'{onset:.12f}',f'{ratio:.12f}',
                     'outside' if ratio>wall else 'inside','outside' if ratio>rival else 'inside',
                     f'{I/A:.12f}',f'{min(margins):.6f}'])
