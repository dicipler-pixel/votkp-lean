"""Regression controls for whole-row and silent-field losses in a printed table."""
import csv
from pathlib import Path
from tempfile import TemporaryDirectory
from check_batch_range_v2 import check

here = Path(__file__).resolve().parent
archive = here.parents[2] / 'data/element_thresholds_20261011.json.gz'
reference = here.parent / 'batch12/ladder/batch12_ba_nd.csv'
with reference.open() as f:
    original = list(csv.DictReader(f))
keys = original[0].keys()
assert check(archive, reference, 56, 60, 6)[:3] == (290, 285, 5)

def control(name, change):
    rows = [dict(row) for row in original]
    change(rows)
    with TemporaryDirectory() as tmp:
        path = Path(tmp) / 'mutant.csv'
        with path.open('w', newline='') as f:
            writer = csv.DictWriter(f, keys)
            writer.writeheader()
            writer.writerows(rows)
        try:
            check(archive, path, 56, 60, 6)
        except ValueError:
            print('Rejected', name)
        else:
            raise AssertionError(f'accepted {name}')

control('removed rung', lambda r: r.pop(3))
control('duplicate rung', lambda r: r.append(dict(r[3])))
control('blank ordinary ratio', lambda r: r[3].update(z_k=''))
control('blank reflection', lambda r: r[3].update(Gamma_k=''))
control('mislabelled element', lambda r: r[3].update(symbol='La'))
control('tiny energy change', lambda r: r[3].update({'IE_k (eV)': '35.8438000001'}))
control('missing last ion', lambda r: r.pop())
control('one last-place error', lambda r: r[0].update(z_k='36.036955'))
control('terminal ratio', lambda r: r[-1].update(z_k='1.000000'))
