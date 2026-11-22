# SCRIPT: G4_OXYGEN
import gzip,json
from decimal import Decimal as D, getcontext
getcontext().prec=40
arc='/home/claude/votkp-lean/data/element_thresholds_20261011.json.gz'
recs={r['symbol']:r for r in json.load(gzip.open(arc,'rt'),parse_float=D)['records']}
def ie(s,q): 
    return [t for t in recs[s]['thresholds'] if t['q']==q][0]
I1=D(str(ie('O',0)['IE_eV']));I2=D(str(ie('O',1)['IE_eV']))
print(I1,I2,I2/I1, 'unc',ie('O',0)['unc_eV'],ie('O',1)['unc_eV'])
K=D('8065.543937'); w=3+2*D(2).sqrt()
L=D('7.576234')/D('1.30447'); H=D('8.15168')/D('1.3895212'); mid=(L+H)/2
print('window',L,H,'mid',mid, 'H-L', H-L)
Es=[D('356736.30'),D('356844.98'),D('357117.01')]
for p,lab in ((0,'J2'),(D('158.265'),'J1'),(D('226.977'),'J0')):
    row=[]
    for E in Es:
        z=(I2+E/K)/(I1-p/K)
        row.append(f"{z:.6f} {'out' if z>w else 'in'}/{'out' if z>mid else 'in'}")
    print(lab,row)
for E in Es:
    z=(I2+E/K)/I1
    # distance in cm-1 to wall at fixed I1,I2
    d=(w*I1-I2)*K-E
    print('z',f'{z:.10f}','dist to wall cm-1 (E - Ewall)',-d)
print('nominal width ratio',(H-L)/((D('357117.01')-D('356844.98'))/K/I1))
# ground margins incl boxes
d1=D(str(ie('O',0)['unc_eV']));d2=D(str(ie('O',1)['unc_eV']))
for E in Es:
    zc=(I2+E/K)/I1
    if zc>w: m=E-K*(w*(I1+d1)-(I2-d2))
    else: m=K*(w*(I1-d1)-(I2+d2))-E
    print('margin',m)
for n,T in ((3,('267258.71','267377.11','267634.00')),(4,('356736.30','356844.98','357117.01')),(5,('391830.76','391917.80','392209.53'))):
    zs=[(I2+D(e)/K)/I1 for e in T]
    print(n,[f'{z:.6f}' for z in zs],[int(z>w) for z in zs],[int(z>mid) for z in zs])
