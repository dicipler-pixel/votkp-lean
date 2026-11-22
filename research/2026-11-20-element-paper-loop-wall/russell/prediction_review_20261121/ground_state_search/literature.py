"""Source-transcribed Rn–Og data, separate from the archive-ground ordinary scan."""
import csv
import gzip
import json
import sys
from decimal import Decimal as D, getcontext
from pathlib import Path

getcontext().prec = 34
records = json.load(gzip.open(sys.argv[1], 'rt'), parse_float=D)['records']
root = Path(sys.argv[2])
wall = 3 + 2 * D(2).sqrt()
rival = (D('7.576234')/D('1.30447') + D('8.15168')/D('1.3895212')) / 2
kcal_per_eV = D('23.06055')
cm_per_eV = D('8065.543937')

# One entry per neutral threshold. Qualifiers reflect the methods in the cited tables.
affinities = {
'Rn':(None,'semiempirical unbound','Ning 2022, Table 3'),
'Fr':('0.491','theory; +/- 0.005','Ning 2022, Table 3'),
'Ra':('0.17','AMS-informed estimate; no stated width','Ning 2022, Table 3 and Sec. 5'),
'Th':('0.607690','experiment; +/- 0.000060','PhysRevLett.123.203002'),
'U':('0.31497','experiment; +/- 0.00009','PhysRevA.103.L050801'),
'Am':('0.076','theory','Ning 2022, Table 2'),
'Cm':('0.321','theory','Ning 2022, Table 2'),
'Lr':('0.446','theory; +/- 0.011','PhysRevA.110.022817'),
'Rg':('1.565','theory','Ning 2022, text ref. 194'),
'Nh':('0.776','theory; +/- 0.030','10.1088/1361-6455/ac761f'),
'Fl':(None,'theory unbound','Ning 2022, text ref. 197'),
'Mc':('0.313','theory','PhysRevA.91.020501, III'),
'Lv':('0.776','theory','PhysRevA.91.020501, III'),
'Ts':('1.602','theory','PhysRevA.91.020501, III'),
'Og':('0.080','theory; +/- 0.006','10.1016/bs.aiq.2021.05.007, Table 5'),
}
# Larger binding among the treated 6d and 7p attachments in Tables II and III.
# Negative 7p values alone establish only that channel's predicted status.
for sym,energy in {'Ac':'8.24','Pa':'7.69','Np':'6.23','Pu':'0.63','Bk':'-0.93','Cf':'-1.32','Es':'-1.56','Fm':'-1.88','Md':'-2.22','No':'-2.28'}.items():
    affinities[sym] = (str(D(energy)/kcal_per_eV),'theory, most-bound reported channel' if D(energy)>0 else 'theory negative in reported 7p channel; other states unresolved','10.1063/5.0293868, Tables II–III')

cipt = {'Ds':[81933,141108,240185,328830],'Rg':[90132,171989,250503,338736,439861],'Cn':[97956,184241,260665,351903,451630,566242]}
extra_ies = {s:(D(v[0])/cm_per_eV,'theory, PhysRevA.101.012514 VIII') for s,v in cipt.items()}
extra_ies.update({'Nh':(D('7.569'),'theory, 10.1088/1361-6455/ac761f')})
pblock = {'Mc':['5.574','18.360'],'Lv':['6.855','13.550'],'Ts':['7.654','15.174'],'Og':['8.888','16.195']}
for s, vals in pblock.items():
    extra_ies[s] = (D(vals[0]), 'theory, '+('10.1016/bs.aiq.2021.05.007' if s=='Og' else 'PhysRevA.91.020501'))

def fmt(n):
    return '' if n is None else f'{n:.9f}'

with (root/'heavy_affinity_screen.csv').open('w') as f:
    wr = csv.writer(f)
    wr.writerow('Z symbol IE1_eV IE_source EA_reported_eV EA_grade EA_source target_EA_lo_eV target_EA_hi_eV z_if_positive'.split())
    for rec in records[85:]:
        s=rec['symbol']; ion=next((t for t in rec['thresholds'] if t['q']==0 and t['IE_eV'] is not None),None)
        I,source = (D(ion['IE_eV']),'archive '+ion['grade']) if ion else extra_ies.get(s,(None,'unavailable in this screen'))
        val,grade,ref=affinities.get(s,(None,'not determined in this screen',''))
        ea=None if val is None else D(val)
        wr.writerow([rec['Z'],s,fmt(I),source,fmt(ea),grade,ref,fmt(I/rival if I else None),fmt(I/wall if I else None),fmt(I/ea if I and ea and ea>0 else None)])

with (root/'additional_ordinary_theory.csv').open('w') as f:
    wr=csv.writer(f);wr.writerow('symbol earlier_k earlier_energy later_energy original_units z source'.split())
    for s,values in {**cipt,**pblock}.items():
        for k,(a,b) in enumerate(zip(values,values[1:]),1):
            wr.writerow([s,k,a,b,'cm^-1' if s in cipt else 'eV',fmt(D(b)/D(a)),extra_ies[s][1]])
