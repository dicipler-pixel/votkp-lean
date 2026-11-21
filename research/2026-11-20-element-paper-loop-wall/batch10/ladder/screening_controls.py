"""Compare the screening zero using successively less idealised reference values."""
import argparse
import csv
import gzip
import hashlib
import json
from decimal import Decimal as D, localcontext
from pathlib import Path

from batch10_ladder import HASH, HARTREE

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive',type=Path)
    parser.add_argument('output',type=Path)
    args=parser.parse_args()
    raw=args.archive.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=HASH:
        raise ValueError('The archive hash differs from the reported pin.')
    records=json.loads(gzip.decompress(raw),parse_float=D)['records']
    with Path(__file__).with_name('hydrogen_like_components_2015.csv').open() as f:
        components={int(row['Z']):row for row in csv.DictReader(f)}
    with args.output.open('w',newline='') as f, localcontext() as ctx:
        ctx.prec=60
        writer=csv.writer(f,lineterminator='\n')
        writer.writerow(['element','atomic_number','point_Dirac_minus_bare_minus_5Zover8_eV',
                         'point_Dirac_minus_bare_minus_archive_gap_eV','archive_helium_like_minus_bare_eV',
                         'archive_hydrogen_like_minus_point_Dirac_eV','published_leading_recoil_loss_eV','published_Lamb_loss_eV','archive_residual_plus_published_losses_eV'])
        alpha=1/D('137.035999177')
        for rec in records[43:50]:
            Z=rec['Z']
            b,h=(x['IE_eV'] for x in rec['thresholds'][-2:])
            nonrel=HARTREE*Z**2/2
            point=HARTREE*Z**2/(1+(1-(Z*alpha)**2).sqrt())
            leading_gap=HARTREE*5*Z/8
            a=point-nonrel-leading_gap
            c=point-nonrel-(h-b)
            actual=b-nonrel
            residual=h-point
            assert abs(c+residual-actual)<D('1e-45')
            assert (a>0,c>0,actual>0)==(Z>=45,Z>=46,Z>=47)
            fields=[f'{v:.6f}' for v in (a,c,actual,residual)]
            if Z in components:
                tab=components[Z]
                mass=D(tab['mass_shift_Ry'])*HARTREE/2
                lamb=D(tab['Lamb_shift_Ry'])*HARTREE/2
                assert abs(residual+mass+lamb)<D('.005')
                if Z==46:
                    assert c-mass>0 and c-lamb<0
                fields.extend(f'{v:.6f}' for v in (mass,lamb,residual+mass+lamb))
            else:
                fields.extend(['','',''])
            writer.writerow([rec['name'],Z,*fields])

if __name__=='__main__':
    main()
