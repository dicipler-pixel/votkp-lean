"""Build an offline rotatable comparison of the first twelve neighbours in COD 9008526."""
import csv
import hashlib
import json
import sys
from pathlib import Path
import gemmi
from check_cages import HERE, SCALE, cage, inverted, site_basis

src = Path(sys.argv[1])/'9008526.cif'
with (HERE/'source_models.csv').open() as f:
    expected = next(r['sha256'] for r in csv.DictReader(f) if r['COD']=='9008526')
assert hashlib.sha256(src.read_bytes()).hexdigest()==expected
structure=gemmi.make_small_structure_from_block(gemmi.cif.read(str(src)).sole_block())
sites=site_basis(structure)
records={}
for site in sites:
    neighbors=cage(structure,sites,site,2)[:12]
    vs=[v for _,v,_ in neighbors]
    pair_count=sum(inverted(v) in vs for v in vs)//2
    if pair_count in records:
        continue
    records[pair_count]=[]
    for v in vs:
        p=structure.cell.orthogonalize(gemmi.Fractional(*(e/SCALE for e in v)))
        records[pair_count].append(dict(xyz=[p.x,p.y,p.z],paired=inverted(v) in vs))
assert sorted(records)==[3,6]
template=(HERE/'site_comparison.template.html').read_text()
(HERE/'neodymium_sites.html').write_text(template.replace('/*CAGES*/null',json.dumps(records,separators=(',',':'))))
