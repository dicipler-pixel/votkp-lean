"""Replay all experimental Yb cells in Storm & McMahon (2026), DOI 10.7488/ds/8146.

python yb_structure.py [--zip storm_yb_data_2026.zip]
A changed archive must be reviewed. No calculated cell enters the inputs.
"""
import argparse
from collections import Counter, defaultdict
import csv
from functools import cache
import hashlib
import io
from math import sqrt
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile

from yb_neighbour_graph import BASES, displacements

HERE = Path(__file__).resolve().parent
URL = 'https://datashare.ed.ac.uk/server/api/core/bitstreams/8b6b116d-7dcc-44d6-a26d-3bd131121863/content'
SHA = 'c72e320645e54017d1c994c7781b56273498a72c9ca3a50b41279a953b66a54f'


@cache
def shells(phase):
    counts = Counter((b,l) for _, _, b, l in displacements(phase))
    return [(float(b), float(l), n) for (b,l),n in counts.items()]


def geom(phase, a, c):
    if phase.startswith('c'):
        d, n = (a*sqrt(3)/2, 8) if phase=='cI2' else (a/sqrt(2), 12)
        return a**3/len(BASES[phase]), d, n, a
    # Enumerate all sites. A translated site beyond the +/-2 range has a
    # basal component or height too large to be one of these first shells.
    ordered = sorted((a*a*b+c*c*l, n) for b,l,n in shells(phase))
    v = sqrt(3)/2*a*a*c/len(BASES[phase])
    return v, sqrt(ordered[0][0]), ordered[0][1], sqrt(ordered[1][0])


def write(name, rows):
    with (HERE/name).open('w') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--zip',type=Path)
    args=parser.parse_args()
    archive=args.zip.read_bytes() if args.zip else urlopen(URL,timeout=60).read()
    if hashlib.sha256(archive).hexdigest()!=SHA:
        raise SystemExit('Source fingerprint changed')
    table=ZipFile(io.BytesIO(archive)).read('yb_exp_data_table.csv').decode()
    groups=defaultdict(list)
    rows=[]
    for r in csv.DictReader(io.StringIO(table)):
        raw=r['phase']
        phase='cF4-II' if raw=='cF2-II' else raw
        a,c=float(r['a (A)']),float(r['c (A)'])
        ua,uc=float(r['a_err (A)']),float(r['c_err (A)'])
        v,d,n,d2=geom(phase,a,c)
        corners=[geom(phase,a+i*3*ua,c+j*3*uc) for i in (-1,1) for j in (-1,1)]
        expect={'hP3':4,'hP2':6,'cI2':8,'cF4-II':12}[phase]
        assert n==expect and all(k[2]==n for k in corners)
        key=(r['cell'],r['P (GPa)'])
        entry=dict(DAC=key[0],P_GPa=key[1],uP_GPa=r['P_err (GPa)'],raw_phase=raw,phase=phase,
                   a_A=a,c_A=c,ua_A=ua,uc_A=uc,
                   V_atom_A3=v,d1_A=d,n1=n,d2_A=d2,
                   V_3u_lo=min(k[0] for k in corners),V_3u_hi=max(k[0] for k in corners),
                   d1_3u_lo=min(k[1] for k in corners),d1_3u_hi=max(k[1] for k in corners))
        groups[key].append(entry)
        rows.append(entry)
    assert len(rows)==119 and Counter(r['phase'] for r in rows)=={'cI2':16,'hP2':15,'cF4-II':15,'hP3':73}
    pairs=[]
    for key, sample in groups.items():
        if len(sample)==1:
            continue
        x,y=sample
        pairs.append(dict(DAC=key[0],P_GPa=key[1],phase1=x['phase'],phase2=y['phase'],
                          V1_A3=x['V_atom_A3'],V2_A3=y['V_atom_A3'],
                          d1_A=x['d1_A'],d2_A=y['d1_A'],
                          dV_percent=100*(y['V_atom_A3']/x['V_atom_A3']-1),
                          delta_d_percent=100*(y['d1_A']/x['d1_A']-1),
                          dV_3u_box_lo=y['V_3u_lo']-x['V_3u_hi'],
                          dV_3u_box_hi=y['V_3u_hi']-x['V_3u_lo'],
                          delta_d_3u_box_lo=y['d1_3u_lo']-x['d1_3u_hi'],
                          delta_d_3u_box_hi=y['d1_3u_hi']-x['d1_3u_lo']))
    assert len(pairs)==5
    assert all(r['dV_3u_box_hi']<0<r['delta_d_3u_box_lo'] for r in pairs if r['phase1']=='cI2')
    write('yb_pressure_cells.csv',rows)
    write('yb_coexisting_contacts.csv',pairs)
    print(f'{len(rows)} raw cells in two DACs reviewed. All 73 hP3 geometries retain four '
          'nearest links over the individual 3u box. Five dual-phase pressure samples.')


if __name__=='__main__':
    main()
