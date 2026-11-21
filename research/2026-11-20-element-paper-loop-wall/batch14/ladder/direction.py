"""Find sharp simultaneous reversal sets on the Dy–Yb interval chains."""
import csv
import gzip
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

DIR=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('reversals',DIR.parents[1]/'batch13/ladder/direction.py')
core=importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
assert hashlib.sha256(core.ARCHIVE.read_bytes()).hexdigest()==core.HASH
with gzip.open(core.ARCHIVE,'rt') as f:
    atoms=json.load(f,parse_float=Fraction)['records'][65:70]
with (DIR/'joint_direction.csv').open('w',newline='') as file:
    writer=csv.writer(file,lineterminator='\n')
    writer.writerow(('symbol','reversible_k','touch_only_k','possible_strict_reversal_sets',
                     'max_simultaneous','example_k','first_to_touch_k',
                     'common_width_multiplier_to_touch','common_energy_at_touch_eV'))
    for atom in atoms:
        result=core.study(atom)
        writer.writerow(result)
        print(*result,sep=' | ')
