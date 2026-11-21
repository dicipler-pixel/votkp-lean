"""Grade pre-existing heavy-anion calls and compare frozen rival cutoffs."""
import csv
import gzip
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
sys.path.insert(0, str(PAPER/'batch12/lean/window'))
from verify_window import ARCHIVE, ARCHIVE_SHA, affinities, csv_rows, independent_statistics

calls = {'Os':'outside','Ir':'inside','Pt':'inside','Au':'inside',
         'Pb':'outside','Bi':'outside','Po':'outside','At':'inside'}
candidates = '5 5.8 5.82 5.83 5.85 5.9 6'.split()
energy_per_cm = F('6.62607015e-34')*299792458*100/F('1.602176634e-19')
assert hashlib.sha256(ARCHIVE.read_bytes()).hexdigest() == ARCHIVE_SHA
with gzip.open(ARCHIVE, 'rt') as f:
    atoms = json.load(f,parse_float=F)['records'][:85]
assert [a['Z'] for a in atoms] == list(range(1,86))
adopted = affinities()
for n in range(13,18):
    for r in csv_rows(PAPER/f'batch{n}/ladder/affinities.csv'):
        if r['EA_eV']:
            adopted[int(r['Z'])] = F(r['EA_eV']),F(r['unc_eV'])
rows, gaps, bounds = independent_statistics(atoms,adopted)
def emit(name,header,records):
    with (HERE/name).open('w') as f:
        writer=csv.writer(f,lineterminator='\n')
        writer.writerow(header.split())
        writer.writerows(records)
def fmt(x):
    from decimal import Decimal as D
    return format(D(x.numerator)/D(x.denominator),'.10f')
def points(data):
    for atom in atoms:
        z,sym = atom['Z'],atom['symbol']
        if sym not in calls:
            continue
        ie,di = [F(atom['thresholds'][0][key]) for key in ('IE_eV','unc_eV')]
        if sym=='Po':
            ea,de = F('11905.631')*energy_per_cm,F('0.009')*energy_per_cm
            grade='preliminary-statistical-only'
        else:
            ea,de=data[z]
            grade='adopted'
        ratio=ie/ea
        lo,hi=(ie-di)/(ea+de),(ie+di)/(ea-de)
        gamma=(ie-ea)/(ie+ea)
        label='outside' if 2*gamma**2>1 else 'inside'
        assert all((2*(v-1)**2>(v+1)**2)==(label=='outside') for v in (lo,hi))
        eta,chi=(ie-ea)/2,(ie+ea)/2
        yield [z,sym,calls[sym],grade,*map(fmt,(ie,ea,ratio,gamma,lo,hi,eta,chi,1/(2*gamma**2))),label,
               'agrees' if label==calls[sym] else 'contrary',*[('outside' if ratio>F(c) else 'inside') for c in candidates]]
emit('heavy_anion_scores.csv','Z symbol frozen source_grade IE_eV EA_eV z Gamma z_low z_high eta_eV chi_eV omega_over_eta wall score '+' '.join('z_gt_'+v for v in candidates),points(adopted))
out=[]
for (ordinary,mode),(count,ins,ext) in bounds.items():
    lower=ins[2] if mode=='central' else ins[4]
    upper=ext[2] if mode=='central' else ext[3]
    out.append(['ordinary' if ordinary else 'all numeric',mode,count,atoms[ins[0]-1]['symbol'],ins[1],fmt(lower),
                atoms[ext[0]-1]['symbol'],ext[1],fmt(upper)])
emit('cutoff_window_through_At.csv','scope input count lower_element k_lower inclusive_lower upper_element k_upper exclusive_upper',out)
emit('missing_boxes_through_At.csv','Z symbol k',([z,atoms[z-1]['symbol'],k] for z,k in gaps))
print('Full primary catalogue:',len(rows),'numeric,',len(rows)-len(gaps),'complete quoted boxes.')
print('Ordinary outside:',[(atoms[r[0]-1]['symbol'],r[1]) for r in rows if r[1] and r[5]])
for v in out: print(*v)
