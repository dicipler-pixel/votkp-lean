"""Counterfactual input sensitivity with mutually exclusive published affinity assignments."""
from fractions import Fraction as F
from pathlib import Path
from generate import exact_q6, side, rows, save

DIR = Path(__file__).resolve().parent
URL_THESIS = 'https://scholarwolf.unr.edu/server/api/core/bitstreams/f41f5aac-9c22-4369-9e8a-1b2558eb8d5a/content'
variants = [
    ('Eu','2004 superseded threshold assignment','1.053','.025','https://doi.org/10.1038/srep12414'),
    ('Eu','2015 measured','.116','.013','https://doi.org/10.1038/srep12414'),
    ('Tb','2006 superseded assignment quoted in 2015 thesis','1.98','.10',URL_THESIS),
    ('Tb','2015 thesis coarse determination','.13','.07',URL_THESIS),
    ('Tb','2020 Fu et al. original determination','.13131','.00079','https://doi.org/10.1103/PhysRevA.101.022502'),
    ('Tb','2022 compilation Table 3 same central value','.13131','.00080','https://doi.org/10.1063/5.0080243'),
]
state = {r['element']:r for r in rows(DIR/'asd_states_20261121.csv') if r['q']=='0'}
def run():
    output = []
    for sym,label,ea,err,url in variants:
        s = state[{'Eu':'Europium','Tb':'Terbium'}[sym]]
        a,u = F(ea),F(err)
        i,v = F(s['NIST_energy_eV']),F(s['NIST_unc_eV'])
        z,lo,hi = i/a,(i-v)/(a+u),(i+v)/(a-u)
        sides={side(lo),side(hi)}
        output.append([sym,label,ea,err,s['NIST_energy_eV'],exact_q6(z),exact_q6((z-1)/(z+1)),
                       exact_q6(lo),exact_q6(hi),side(z),sides.pop() if len(sides)==1 else 'straddles',url])
    assert [r[10] for r in output]==['inside','outside','inside','outside','outside','outside']
    save(DIR/'source_controls.csv','symbol,scope,EA_eV,unc_eV,IE1_eV,z0,Gamma0,z_low,z_high,central_wall,box_wall,source'.split(','),output)

if __name__=='__main__':
    run()
