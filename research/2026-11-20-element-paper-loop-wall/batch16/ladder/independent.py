"""Third check: use published NIST rows and EA inputs directly; no ladder imports."""
from collections import Counter
import csv
from fractions import Fraction as F
from pathlib import Path

DIR=Path(__file__).resolve().parent


def read(n):
    with (DIR/n).open() as f:
        return list(csv.DictReader(f))


def canonical(v, places):
    # Compare a printed finite decimal to an exact fraction rounded to nearest, ties to even.
    return F(round(v*10**places),10**places)


def check(primary, heavy, krows):
    asd=read('asd_states_20261121.csv')
    aff={r['symbol']:r for r in read('affinities.csv')}
    frozen={r['Z']:r for r in read('../../holdouts/k_opening/predictions.csv')}
    states={(r['Z'],int(r['q'])):r for r in asd}
    displayed={(r['Z'],int(r['k'])):r for r in primary}
    assert len(displayed)==len(primary)==395
    grade=Counter()
    edges=Counter()
    for row in primary:
        n,k=int(row['Z']),int(row['k'])
        sym=row['symbol']
        r=states[str(n),max(0,k-1)]
        if k:
            actual=F(r['NIST_energy_eV'].strip('[]()'))
            grade_code={'(': 'T','[': 'S'}.get(r['NIST_energy_eV'][0],'E')
            assert row['source']==grade_code
            grade[grade_code]+=1
        else:
            assert row['source']==aff[sym]['status']
            if not aff[sym]['EA_eV']:
                assert row['IE_k (eV)']==row['z_k']==row['Gamma_k']==''
                continue
            actual=F(aff[sym]['EA_eV'])
        assert F(row['IE_k (eV)'])==actual
        if k==n:
            assert row['z_k']==row['Gamma_k']==''
            continue
        next_ie=F(states[str(n),k]['NIST_energy_eV'].strip('[]()'))
        exact_z=next_ie/actual
        exact_gamma=(next_ie-actual)/(next_ie+actual)
        assert F(row['z_k'])==canonical(exact_z,6) and F(row['Gamma_k'])==canonical(exact_gamma,6)
        edges['ordinary' if k else 'anion', 'outside' if 2*exact_gamma**2>1 else 'inside']+=1
    for r in heavy:
        n,sym=r['Z'],r['symbol']
        I=F(states[n,0]['NIST_energy_eV']); u=F(states[n,0]['NIST_unc_eV'])
        A=F(r['EA_eV']); v=F(r['unc_EA_eV'])
        eta=(I-A)/2; chi=(I+A)/2
        for col,exact in [('z',I/A),('z_low',(I-u)/(A+v)),('z_high',(I+u)/(A-v)),
                          ('Gamma',eta/chi),('eta_eV',eta),('chi_eV',chi),('omega_over_eta',(chi/eta)**2/2)]:
            assert F(r[col])==canonical(exact,12)
        def side(x,y): # equivalent loop polynomial evaluated in original energies
            score=x*x-6*x*y+y*y
            return 'outside' if score>0 else 'inside' if score<0 else 'on wall'
        assert r['central_side']==side(I,A)
        assert side(I-u,A+v)==side(I+u,A-v)==r['whole_box_side']
        assert all(r['cutoff_'+c]==('outside' if I>A*F(c) else 'inside') for c in ('5','5.8','5.82','5.83','5.85','5.9','6'))
    for r in krows:
        n=r['Z']; k=int(n)-2
        x=states[n,k-1]; y=states[n,k]
        a=F(x['NIST_energy_eV'].strip('()')); b=F(y['NIST_energy_eV'].strip('()'))
        u=F(x['NIST_unc_eV']); v=F(y['NIST_unc_eV'])
        lo=(b-v)/(a+u); hi=(b+v)/(a-u)
        for key,xkey,rkey,iskey in [('linear_from_65_70','secant_frozen','actual_minus_secant','secant_in_box'),('dirac_plus_constant_over_Z','Dirac_plus_1_over_Z_frozen','actual_minus_Dirac','Dirac_model_in_box')]:
            p=F(frozen[n][key])
            assert F(r[xkey])==p and F(r[rkey])==canonical(b/a-p,12)
            assert r[iskey]==str(lo<=p<=hi)
    return grade,edges


if __name__=='__main__':
    lists=[read('batch16_os_hg.csv'),read('heavy_anion_primary.csv')+read('heavy_anion_source_controls.csv'),read('k_opening_residuals.csv')]
    print(*check(*lists),sep='\n')
    tests=[(0,1,'IE_k (eV)','8.43'),(0,76,'source','E'),(1,0,'whole_box_side','inside'),
           (1,1,'cutoff_5','inside'),(1,2,'omega_over_eta','1.000000000000'),
           (2,3,'actual_minus_secant','-0.000067013223'),(2,4,'Dirac_model_in_box','True')]
    for i,j,col,bad in tests:
        damaged=[[x.copy() for x in data] for data in lists]
        damaged[i][j][col]=bad
        try:
            check(*damaged)
        except AssertionError:
            print('rejected:',col,bad)
        else:
            raise AssertionError('damaged value accepted: '+str((i,j,col,bad)))
