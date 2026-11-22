# SCRIPT: G4_BENCH
import gzip,json
from fractions import Fraction as F
from math import sqrt
arc='/home/claude/votkp-lean/data/element_thresholds_20261011.json.gz'
recs={r['symbol']:r for r in json.load(gzip.open(arc,'rt'),parse_float=str)['records']}
def th(s,q): return [t for t in recs[s]['thresholds'] if t['q']==q][0]
print('Rb q=34,35',th('Rb',34)['IE_eV'],th('Rb',35)['IE_eV'],'Be q1,2',th('Be',1)['IE_eV'],th('Be',2)['IE_eV'])
g=lambda z:(z-1)/(z+1); u=lambda z:(z-1)/(2*sqrt(z))
L=7.576234/1.30447; H=8.15168/1.3895212; c=(L+H)/2
q=lambda z:g(z)**2
def warp(t):
    qL,qH,qc=q(L),q(H),q(c)
    if t<=qL or t>=qH: return t
    if t<=qc: return qL+(0.5-qL)*(t-qL)/(qc-qL)
    return 0.5+(qH-0.5)*(t-qc)/(qH-qc)
def calls(a,b):
    geo=q(a)+q(b)-1
    return dict(geo=geo, sum=q(a)+q(b)-2*q(c), prod=u(a)*u(b)-u(c)**2, warp=warp(q(a))+warp(q(b))-1,trace=2-4*u(a)**2*u(b)**2, sp=u(a)*u(b))
for name,a,b in [('35/6',35/6,35/6),('3,13.99',3,13.99),('Be,Rb',153.896205/18.21115,18305.886/4356.865),('Si,Ag',8.15168/1.3895212,7.576234/1.30447),('9,4',9,4)]:
    r=calls(a,b); print(name,{k:round(v,9) for k,v in r.items()})
print('35/6 G',g(35/6),29/41,'2G^2-1',2*g(35/6)**2-1, 1/1681)
print(F(-354481,176400), float(F(-354481,176400)))
