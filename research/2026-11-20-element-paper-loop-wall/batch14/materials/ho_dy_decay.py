"""Same-charge A=163 mass differences from the neutral PENTATRAP value and archived peels."""
import csv
from decimal import Decimal as D
from pathlib import Path

HERE = Path(__file__).resolve().parent
neutral, neutral_u = D('2863.2'), D('0.6')
# Schweiger et al., Nature Physics 20, 921 (2024), Table 1, final column.
atomic_corrections = {38:(D('37.4'),D('1.4')),39:(D('1147.3'),D('0.7')),40:(D('1115.7'),D('0.7'))}


def main():
    table = {}
    with (HERE.parent/'ladder'/'asd_states_20261121.csv').open() as f:
        for r in csv.DictReader(f):
            if r['Z'] in ('66','67'):
                table[int(r['Z']),int(r['q'])]=r
    rows=[]
    q_gap, half_width=neutral,neutral_u
    anchor_gap=anchor_width=None
    for q in range(67):
        if q:
            h, d=table[67,q-1],table[66,q-1]
            step=D(h['NIST_energy_eV'].strip('[]()'))-D(d['NIST_energy_eV'].strip('[]()'))
            width=D(h['NIST_unc_eV'])+D(d['NIST_unc_eV'])
            q_gap+=step
            half_width+=width
            if anchor_gap is not None:
                anchor_gap+=step
                anchor_width+=width
        if q==40:
            correction,unc=atomic_corrections[40]
            anchor_gap,anchor_width=neutral-correction,neutral_u+unc
        correction,unc=atomic_corrections.get(q,('',''))
        rows.append(dict(q=q,Ho_electrons=67-q,Dy_electrons=66-q,
                         Q_Ho_minus_Dy_eV=q_gap,Q_lower_eV=q_gap-half_width,
                         Q_upper_eV=q_gap+half_width,sign='Ho heavier' if q_gap>0 else 'Dy heavier',
                         cumulative_Dy_minus_Ho_peels_eV=neutral-q_gap,
                         article_binding_correction_eV=correction,article_correction_u_eV=unc,
                         archive_minus_article_binding_eV=(neutral-q_gap-correction) if correction!='' else '',
                         q40_anchor_Q_eV=anchor_gap if anchor_gap is not None else '',
                         q40_anchor_lower_eV=anchor_gap-anchor_width if anchor_gap is not None else '',
                         q40_anchor_upper_eV=anchor_gap+anchor_width if anchor_gap is not None else ''))
    assert all(r['Q_lower_eV']>0 if r['q']<57 else r['Q_upper_eV']<0 for r in rows)
    assert all(r['q40_anchor_lower_eV']>0 if r['q']<57 else r['q40_anchor_upper_eV']<0 for r in rows[40:])
    with (HERE/'ho_dy_decay.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n')
        w.writeheader()
        w.writerows(rows)
    print('67 same-charge energy differences; full-sum sign crossing 56 to 57; q40 anchor agrees.')


if __name__=='__main__':
    main()
