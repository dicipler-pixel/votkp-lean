"""Build or independently verify the antimony–caesium numerical packet (stdlib only).

    python3 batch11_ladder.py /path/to/element_thresholds_20261011.json.gz .
    python3 batch11_ladder.py /path/to/element_thresholds_20261011.json.gz . --verify-only
"""
import argparse
import csv
import gzip
import hashlib
import json
from decimal import Decimal as D, localcontext, ROUND_HALF_UP
from fractions import Fraction as F
from pathlib import Path

PIN = '8e5d44f1d9e36f242e6522bbe70cea18fb315c7a'
HASH = '75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
# EA22 = Ning and Lu, J. Phys. Chem. Ref. Data 51, 021502 (2022), Table 3.
AFF = {
    'Sb': (D('1.047401'), D('.000019'), 'EA22'),
    'Te': (D('1.970875'), D('.000007'), 'EA22'),
    'I': (D('3.0590465'), D('.0000036'), 'EA22'),
    'Xe': (None, None, 'no-bound-ground-anion'),
    'Cs': (D('.471626'), D('.000025'), 'EA22'),
}
HARTREE = D('27.211386245981')  # CODATA 2022, eV
CSV_HEADER = ['Z','symbol','k','IE_k (eV)','z_k','Gamma_k','source']
DETAIL_HEADER = ['Z','symbol','k','start_eV','end_eV','start_unc_eV','end_unc_eV',
                 'start_grade','end_grade','start_ref','end_ref','z','Gamma','log_z',
                 'apex','z_low','z_high','central_wall','endpoint_wall','boundary']
CORES = {54:'xenon core',46:'filled 4d10 subshell',36:'krypton core',28:'filled 3d10 subshell',18:'argon core',10:'neon core',2:'helium core'}


def load(path):
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != HASH:
        raise ValueError(f'Archive bytes differ from pin {PIN}.')
    records = json.loads(gzip.decompress(raw),parse_float=D)['records']
    r = [e for e in records if 51 <= e['Z'] <= 55]
    if [(e['Z'], e['symbol']) for e in r] != list(enumerate(AFF,51)):
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
    status=side(lo) if side(lo)==side(hi) and not (side(lo)=='outside' and lo<=1<=hi) else 'straddles'
    return (f'{D(lo.numerator)/D(lo.denominator):.9f}',
            f'{D(hi.numerator)/D(hi.denominator):.9f}',status)


def generate(path,folder):
    records=load(path)
    with (folder/'batch11_sb_cs.csv').open('w',newline='') as f, (folder/'batch11_rungs_detailed.csv').open('w',newline='') as g, localcontext() as ctx:
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
                if x is None:
                    w.writerow([Z,s,k,'','','',grade])
                    continue
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
                    boundary='measured anion'
                if k==Z-1:
                    boundary='last two'
                lo,hi,test=interval(x,y,dx,dy)
                detail.writerow([Z,s,k,x,y,dx,dy,grade,next_grade,ref,next_ref,
                                 *(format(d,'.9f') for d in [z,reflection,z.ln(),(root-1)/(root+1)]),
                                 lo,hi,side(F(y)/F(x)),test,boundary])


def summarize(path,folder):
    """Key columns are printed from the same archive and persisted full ladder."""
    records=load(path)
    with (folder/'batch11_sb_cs.csv').open(newline='') as f:
        rows={(int(r['Z']),int(r['k'])):r for r in csv.DictReader(f)}
    with (folder/'batch11_summary.csv').open('w',newline='') as f,localcontext() as c:
        c.prec=60
        w=csv.writer(f,lineterminator='\n')
        w.writerow(['element','anion_z','anion_Gamma',*CORES.values(),
                    'terminal_z','S','sigma','helium_like_minus_bare_eV','helium_like_unc_eV'])
        for rec in records:
            Z=rec['Z']
            b,h=(D(t['IE_eV']) for t in rec['thresholds'][-2:])
            screening=(h-b)/(HARTREE*Z)
            sigma=Z-(2*b/HARTREE).sqrt()
            displacement=b-HARTREE*Z*Z/2
            w.writerow([rec['name'],rows[Z,0]['z_k'],rows[Z,0]['Gamma_k'],
                        *(rows[Z,Z-core]['z_k'] if Z>core else '' for core in CORES),
                        rows[Z,Z-1]['z_k'],q6(screening),q6(sigma),
                        q6(displacement),rec['thresholds'][-2]['unc_eV']])

def verify(path,folder):
    records=load(path)
    table=folder/'batch11_sb_cs.csv'
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
                if val is None:
                    if any(row[field] for field in ('IE_k (eV)','z_k','Gamma_k')) or row['source']!=grade:
                        raise ValueError('Invalid unbound anion placeholder.')
                    continue
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
                outside.append((rec['name'],k))
            if dx is None or dy is None:
                missing.append((rec['name'],k))
            else:
                low,high=(y-F(dy))/(x+F(dx)),(y+F(dy))/(x-F(dx))
                if side(low)!=label or side(high)!=label or (label=="outside" and low<=1<=high):
                    raise ValueError(f'Central classification fails at endpoints {s}/{k}.')
                usable+=1
            if k: ordinary_pairs+=1
            else: anion_pairs+=1
        h,b=(D(t['IE_eV'])/HARTREE for t in q[-1:-3:-1])
        print(f'{rec["name"]}: S={(h-b)/Z:.9f}, sigma={Z-(2*b).sqrt():.9f}')
    print('Source pin',PIN,'archive SHA-256',HASH)
    print(f'{len(rows)} serialized rows, {ordinary_energies} archive energies, {ordinary_pairs} ordinary pairs, {anion_pairs} anion pairs, zero differences.')
    print('Outside at central inputs:',outside)
    print('Endpoint-certified arithmetic (reported input uncertainties only):',usable)
    print('Unavailable endpoints (element,k):',missing)
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
        summarize(args.archive,args.folder)
    verify(args.archive,args.folder)
