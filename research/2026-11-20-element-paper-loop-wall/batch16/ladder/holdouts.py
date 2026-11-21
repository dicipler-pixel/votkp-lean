"""Score two recorded forecasts from independent exact-decimal source inputs."""
import csv
import gzip
import hashlib
import json
from decimal import Decimal, localcontext
from fractions import Fraction as F
from pathlib import Path

DIR = Path(__file__).resolve().parent
ARCHIVE = DIR.parents[3]/'data/element_thresholds_20261011.json.gz'
HASH = '75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
CUTOFFS = ['5','5.8','5.82','5.83','5.85','5.9','6']
PRIOR = {'Os':'outside','Ir':'inside','Pt':'inside','Au':'inside'}


def read(path):
    with path.open() as f:
        return list(csv.DictReader(f))


def write(path, fields, data):
    with path.open('w',newline='') as f:
        w=csv.writer(f,lineterminator='\n')
        w.writerow(fields)
        w.writerows(data)


def shown(value):
    with localcontext() as ctx:
        ctx.prec=40
        return f'{Decimal(value.numerator)/Decimal(value.denominator):.12f}'


def where(z):
    c = 2*(z-1)**2-(z+1)**2
    return 'outside' if c>0 else 'inside' if c<0 else 'on wall'


def score():
    assert hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()==HASH
    with gzip.open(ARCHIVE,'rt') as f:
        atoms=json.load(f,parse_float=F)['records'][75:80]
    frozen={int(r['Z']):r for r in read(DIR.parents[1]/'holdouts/k_opening/predictions.csv')}
    aff={r['symbol']:r for r in read(DIR/'affinities.csv')}
    live={r['element']:r for r in read(DIR/'asd_states_20261121.csv') if r['q']=='0'}
    alternatives=read(DIR/'alternative_affinities.csv')
    primary,secondary,kr=[],[],[]
    # Read the actual earlier Ag and Si inputs; rounded cutoffs would corrupt endpoint tests.
    with gzip.open(ARCHIVE,'rt') as f:
        records=json.load(f,parse_float=F)['records']
    si_row=next(r for r in read(DIR.parents[1]/'checks/batch3.csv') if r['symbol']=='Si' and r['k']=='0')
    si=records[13]['thresholds'][0]['IE_eV']/F(si_row['IE_k (eV)'])
    ag_row=next(r for r in read(DIR.parents[1]/'batch10/ladder/batch10_pd_sn.csv') if r['symbol']=='Ag' and r['k']=='0')
    ag=records[46]['thresholds'][0]['IE_eV']/F(ag_row['IE_k (eV)'])
    assert (ag,si)==(F(3788117,652235),F(20379200,3473803))
    for a in atoms:
        n,s,t=a['Z'],a['symbol'],a['thresholds']
        entries=[('evaluated primary',aff[s])] if s in PRIOR else []
        entries += [(r['assignment'],r) for r in alternatives if r['symbol']==s]
        for scope,r in entries:
            ie,ui=t[0]['IE_eV'],t[0]['unc_eV']
            name=a['name'] if 'name' in a else {'Os':'Osmium','Ir':'Iridium','Pt':'Platinum','Au':'Gold'}[s]
            assert F(live[name]['NIST_energy_eV'])==ie and F(live[name]['NIST_unc_eV'])==ui
            ea,ua=F(r['EA_eV']),F(r['unc_eV'])
            z,lo,hi=ie/ea,(ie-ui)/(ea+ua),(ie+ui)/(ea-ua)
            gamma=(ie-ea)/(ie+ea)
            eta,chi=(ie-ea)/2,(ie+ea)/2
            assert lo>1 and where(lo)==where(z)==where(hi)
            answers=['outside' if z>F(x) else 'inside' for x in CUTOFFS]
            assert all((lo>F(c)) or (hi<F(c)) for c in CUTOFFS)
            tightens=(where(z)=='outside' and z<si) or (where(z)=='inside' and z>ag)
            row=[n,s,scope,r['EA_eV'],r['unc_eV'],*map(shown,[z,lo,hi,gamma,eta,chi,1/(2*gamma**2)]),
                 PRIOR[s],where(z),where(lo),'supported' if where(z)==PRIOR[s] else 'contrary',
                 *answers,str(tightens)]
            (primary if scope=='evaluated primary' else secondary).append(row)
        # Li-like = three-electron starting ion, adjacent to the helium-like threshold.
        k=n-2
        x,dx=t[k-1]['IE_eV'],t[k-1]['unc_eV']
        y,dy=t[k]['IE_eV'],t[k]['unc_eV']
        z,lo,hi=y/x,(y-dy)/(x+dx),(y+dy)/(x-dx)
        row=[n,s,k,t[k-1]['grade'],t[k]['grade'],*map(shown,[z,lo,hi]),'above 4' if lo>4 else 'below 4' if hi<4 else 'straddles 4']
        for key in ('linear_from_65_70','dirac_plus_constant_over_Z'):
            p=F(frozen[n][key])
            row += [str(frozen[n][key]),shown(z-p),str(lo<=p<=hi)]
        kr.append(row)
    fields=['Z','symbol','scope','EA_eV','unc_EA_eV','z','z_low','z_high','Gamma','eta_eV','chi_eV','omega_over_eta','prediction','central_side','whole_box_side','grade',*['cutoff_'+x for x in CUTOFFS],'tightens_H_Cs_central_cutoff_interval']
    write(DIR/'heavy_anion_primary.csv',fields,primary)
    write(DIR/'heavy_anion_source_controls.csv',fields,secondary)
    write(DIR/'k_opening_residuals.csv',['Z','symbol','k','Li_like_grade','He_like_grade','actual','lower','upper','box_vs_four','secant_frozen','actual_minus_secant','secant_in_box','Dirac_plus_1_over_Z_frozen','actual_minus_Dirac','Dirac_model_in_box'],kr)
    assert [r[15] for r in primary]==['supported']*4
    assert all(r[-1]=='False' for r in primary+secondary)
    assert [r[8] for r in kr]==['above 4']*4+['below 4']
    # Preserve opposite readings as explicit controls instead of upgrading them after seeing the answer.
    assert where(F(5))=='inside' and F(primary[1][5])>5 and primary[1][13]=='inside'
    assert F(kr[-2][5])>4 and F(kr[-1][7])<4
    assert kr[-2][-1]=='False' and kr[-1][-1]=='False'
    print('Primary heavy signs:', [(r[1],r[13]) for r in primary])
    print('Source alternatives:',len(secondary),'with unchanged whole-box side')
    print('Comparator disagreements:',list(zip(CUTOFFS,[sum(r[13]!=r[16+i] for r in primary) for i in range(len(CUTOFFS))])))
    print('Prior cutoff interval:',shown(ag),shown(si),'unchanged')
    for r in kr:
        print('K',*[r[i] for i in (1,5,8,10,11,13,14)])


if __name__=='__main__':
    score()
