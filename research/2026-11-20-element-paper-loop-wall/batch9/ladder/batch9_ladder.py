"""Build or independently verify the niobium–rhodium numerical packet (stdlib only).

    python3 batch9_ladder.py /path/to/element_thresholds_20261011.json.gz .
    python3 batch9_ladder.py /path/to/element_thresholds_20261011.json.gz . --verify-only
"""
import argparse
import csv
import gzip
import hashlib
import json
from decimal import Decimal as D, localcontext, ROUND_HALF_UP
from fractions import Fraction as F
from pathlib import Path

PIN = '182da01a14b10ce1e07e247565466d01822121c5'
HASH = '75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
# EA22 = Ning and Lu, J. Phys. Chem. Ref. Data 51, 021502 (2022), Table 3.
# Rh26 = Chen et al., Chin. Phys. B 35, 063202 (2026), DOI 10.1088/1674-1056/ae5173.
AFF = {
    'Nb': (D('.91740'), D('.00007'), 'EA22'),
    'Mo': (D('.74723'), D('.00008'), 'EA22'),
    'Tc': (D('.636'), None, 'EA22-estimate'),
    'Ru': (D('1.046270'), D('.000020'), 'EA22'),
    'Rh': (D('1.14273'), D('.00005'), 'Rh26'),
}
HARTREE = D('27.211386245981')  # CODATA 2022, eV
CSV_HEADER = ['Z','symbol','k','IE_k (eV)','z_k','Gamma_k','source']
DETAIL_HEADER = ['Z','symbol','k','start_eV','end_eV','start_unc_eV','end_unc_eV',
                 'start_grade','end_grade','start_ref','end_ref','z','Gamma','log_z',
                 'apex','z_low','z_high','central_wall','endpoint_wall','boundary']
CORES = {36:'Kr core',28:'3d10 subshell',18:'Ar core',10:'Ne core',2:'He core'}


def load(path):
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != HASH:
        raise ValueError(f'Archive bytes differ from pin {PIN}.')
    records = json.loads(gzip.decompress(raw),parse_float=D)['records']
    r = [e for e in records if 41 <= e['Z'] <= 45]
    if [(e['Z'], e['symbol']) for e in r] != list(enumerate(AFF,41)):
        raise ValueError('Missing or reordered element.')
    for e in r:
        if [t['q'] for t in e['thresholds']] != list(range(e['Z'])):
            raise ValueError(f"Missing or reordered charge on {e['symbol']}.")
    return r


def side(z):
    # Exact positive-ratio test for both branches, including equality.
    discr = z*z-6*z+1
    return 'outside' if discr>0 else 'inside' if discr<0 else 'on'


def q6(d):
    return format(d.quantize(D('0.000001'),rounding=ROUND_HALF_UP),'f')


def exact_q6(q):
    # Assert serialized ratios using integer half-up rounding, independent of Decimal.
    if q<0:
        return '-'+exact_q6(-q)
    units=(2*q.numerator*10**6+q.denominator)//(2*q.denominator)
    a,b=divmod(units,10**6)
    return f'{a}.{b:06d}'


def interval(x,y,dx,dy):
    if dx is None or dy is None:
        return ('','','unavailable')
    if x<=dx or y<=dy:
        raise ValueError('Input interval touches zero.')
    lo,hi=F(y-dy)/F(x+dx),F(y+dy)/F(x-dx)
    if lo<=1:
        raise ValueError('Revisit interval crossing the reversal point.')
    status=side(lo) if side(lo)==side(hi) else 'straddles'
    return (f'{D(lo.numerator)/D(lo.denominator):.9f}',
            f'{D(hi.numerator)/D(hi.denominator):.9f}',status)


def generate(path,folder):
    records=load(path)
    with (folder/'batch9_nb_rh.csv').open('w',newline='') as f, (folder/'batch9_rungs_detailed.csv').open('w',newline='') as g, localcontext() as ctx:
        ctx.prec=60
        w=csv.writer(f,lineterminator='\n'); w.writerow(CSV_HEADER)
        detail=csv.writer(g,lineterminator='\n'); detail.writerow(DETAIL_HEADER)
        for rec in records:
            Z,s=rec['Z'],rec['symbol']
            e,u,src=AFF[s]
            slots=[(e,u,src,src)]
            for t in rec['thresholds']:
                slots.append((D(t['IE_eV']),t['unc_eV'],t['grade'],t['references']))
            for k,(x,dx,grade,ref) in enumerate(slots):
                if k==Z:
                    w.writerow([Z,s,k,x,'','',grade])
                    continue
                y,dy,next_grade,next_ref=slots[k+1]
                z=y/x
                reflection=(y-x)/(y+x)
                w.writerow([Z,s,k,format(x,'f'),q6(z),q6(reflection),grade])
                root=z.sqrt()
                boundary=CORES.get(Z-k,'')
                if k==0:
                    boundary='estimated anion' if s=='Tc' else 'measured anion'
                if k==Z-1:
                    boundary='last two'
                lo,hi,test=interval(x,y,dx,dy)
                detail.writerow([Z,s,k,x,y,dx,dy,grade,next_grade,ref,next_ref,
                                 *(format(d,'.9f') for d in [z,reflection,z.ln(),(root-1)/(root+1)]),
                                 lo,hi,side(F(y)/F(x)),test,boundary])


def verify(path,folder):
    records=load(path)
    table=folder/'batch9_nb_rh.csv'
    with table.open(newline='') as f:
        reader=csv.DictReader(f)
        if reader.fieldnames!=CSV_HEADER:
            raise ValueError('Incorrect CSV header.')
        rows=list(reader)
    expected_keys=[(e['Z'],e['symbol'],k) for e in records for k in range(e['Z']+1)]
    if [(int(r['Z']),r['symbol'],int(r['k'])) for r in rows]!=expected_keys:
        raise ValueError('Missing, extraneous or reordered CSV row.')
    actual={(int(r['Z']),int(r['k'])):r for r in rows}
    ordinary_energies=ordinary_pairs=anion_pairs=0
    outside=[]
    missing=[]
    usable=0
    for rec in records:
        Z,s=rec['Z'],rec['symbol']
        q=rec['thresholds']
        for k in range(Z+1):
            row=actual[Z,k]
            if k:
                t=q[k-1]
                x,dx,grade=F(t['IE_eV']),t['unc_eV'],t['grade']
                ordinary_energies+=1
            else:
                val,dx,grade=AFF[s]
                x=F(val)
            if F(row['IE_k (eV)'])!=x or row['source']!=grade:
                raise ValueError(f'Energy/grade mismatch {s}/{k}.')
            if k==Z:
                if row['z_k'] or row['Gamma_k']:
                    raise ValueError(f'Unphysical outgoing terminal step {s}.')
                continue
            y=F(q[k]['IE_eV'])
            dy=q[k]['unc_eV']
            z=y/x
            g=(z-1)/(z+1)
            if (row['z_k'],row['Gamma_k'])!=(exact_q6(z),exact_q6(g)):
                raise ValueError(f'Printed pair mismatch {s}/{k}.')
            label=side(z)
            if (2*g*g>1)!=(label=='outside'):
                raise ValueError('Independent predicates disagree.')
            if label=='outside':
                outside.append((s,k))
            if dx is None or dy is None:
                missing.append((s,k))
            else:
                low,high=(y-F(dy))/(x+F(dx)),(y+F(dy))/(x-F(dx))
                if low<=1 or side(low)!=label or side(high)!=label:
                    raise ValueError(f'Central classification fails at endpoints {s}/{k}.')
                usable+=1
            if k: ordinary_pairs+=1
            else: anion_pairs+=1
        h,b=(D(t['IE_eV'])/HARTREE for t in q[-1:-3:-1])
        print(f'{rec["name"]}: S={(h-b)/Z:.9f}, sigma={Z-(2*b).sqrt():.9f}')
    print('Source pin',PIN,'archive SHA-256',HASH)
    print(f'{len(rows)} serialized rows, {ordinary_energies} archive energies, {ordinary_pairs} ordinary pairs, {anion_pairs} anion pairs (one estimated), zero differences.')
    print('Outside at central inputs:',outside)
    print('Endpoint-certified arithmetic (reported input uncertainties only):',usable)
    print('Unavailable endpoints (symbol,k):',missing)
    print('CSV SHA-256:',hashlib.sha256(table.read_bytes()).hexdigest())


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive',type=Path)
    parser.add_argument('folder',type=Path)
    parser.add_argument('--verify-only',action='store_true')
    args=parser.parse_args()
    args.folder.mkdir(exist_ok=True,parents=True)
    if not args.verify_only:
        generate(args.archive,args.folder)
    verify(args.archive,args.folder)
