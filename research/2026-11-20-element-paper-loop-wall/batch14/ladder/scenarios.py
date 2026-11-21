"""Evaluate the closed 4f opening and the Tm/Dy affinity-source sensitivity."""
from fractions import Fraction as F
from pathlib import Path
import sys

DIR=Path(__file__).resolve().parent
sys.path.insert(0,str(DIR.parents[1]/'batch12/ladder'))
from batch12_ladder import exact_q6, side, occupation, rows, save

def run():
    states={(int(r['Z']),int(r['q'])):r for r in rows(DIR/'asd_states_20261121.csv')}
    terms={(r['symbol'],int(r['k'])):r for r in rows(DIR/'rungs_detailed.csv')}
    scenarios=[
        (66,'Dy','1994 electric dissociation fit: p1/2','0.0155','0.0025'),
        (66,'Dy','2022 Table 3 recommended rounding','0.015','0.003'),
        (69,'Tm','2022 Table 3 / 1997 AMS estimate','0.032','0.007'),
        (69,'Tm','2002 competing photodetachment assignment','1.029','0.022'),
        (70,'Yb','withdrawn AMS attribution; counterfactual only','0.010','0.003'),
    ]
    alt=[]
    for z,s,f,ea,unc in scenarios:
        r=states[z,0]
        i,di,a,da=map(F,(r['NIST_energy_eV'],r['NIST_unc_eV'],ea,unc))
        value,lo,hi=i/a,(i-di)/(a+da),(i+di)/(a-da)
        assert side(value)==side(lo)==side(hi)=='outside'
        alt.append([s,f,ea,unc,*map(exact_q6,(value,lo,hi,(value-1)/(value+1))),
                    side(value),'straddles six' if lo<6<hi else 'above six'])
    save(DIR/'source_controls.csv','symbol,input_scope,EA_eV,unc_eV,z0,z_low,z_high,Gamma0,central_wall,interval_vs_6'.split(','),alt)
    fs=[]
    intervals=[]
    for z,sym in enumerate(('Dy','Ho','Er','Tm','Yb'),66):
        row=terms[sym,2]
        assert row['ASD_earlier_loss']=='6s' and row['ASD_later_loss']=='4f'
        given=occupation(states[z,2]['ground_shells'])
        count=given['4f']
        assert count==z-56
        x,y,dx,dy=map(F,(row['E_start_eV'],row['E_end_eV'],row['unc_start_eV'],row['unc_end_eV']))
        lo,hi=(y-dy)/(x+dx),(y+dy)/(x-dx)
        intervals.append((lo,hi))
        fs.append([sym,2,states[z,2]['ground_shells'],count,14,count==14,row['z'],
                   row['Gamma'],row['z_lo'],row['z_hi'],row['box_wall']])
    assert intervals[-1][0]>max(hi for lo,hi in intervals[:-1])
    save(DIR/'four_f_opening.csv','symbol,k,ASD_middle_ground_shells,occupation_4f,capacity_4f,full,z,Gamma,z_lower,z_upper,wall_box'.split(','),fs)

if __name__=='__main__':
    run()
