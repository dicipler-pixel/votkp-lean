# SCRIPT: G2_WALL (count steps with Gamma^2>1/2 and closed-core opening steps in the threshold archive; solve Z* from the z_core formula)
import gzip,json,math
from fractions import Fraction
d=json.load(gzip.open('/home/claude/votkp-lean/data/element_thresholds_20261011.json.gz'))
zw=3+2*math.sqrt(2)
cross=[];pairs=[]
for r in d['records']:
    th={t['q']:t for t in r['thresholds']}
    for q in th:
        if q+1 in th:
            z=th[q+1]['IE_eV']/th[q]['IE_eV']
            G=(z-1)/(z+1)
            pairs.append((r['Z'],r['symbol'],q,z,G))
            if G*G>0.5: cross.append((r['Z'],r['symbol'],q,round(z,3),round(G*G,4)))
print('pairs',len(pairs)); print('crossing',len(cross)); [print(c) for c in cross]
counts={2,10,18,28,36,46,54,60,68,78,86}
for name,f in (('after',lambda Z,q:Z-q-1),('before',lambda Z,q:Z-q)):
    n=[p for p in pairs if f(p[0],p[2]) in counts]
    print(name,'closed-core steps',len(n),'cross',sum(1 for p in n if p[4]**2>0.5))
# z_core wall solve
def zc(Z,five=True):
    num=Z*Z/2-(5*Z/8 if five else 0)+0.157666
    den=Z*Z/8-(290/729)*Z+0.250500
    return num/den
def solve(five):
    lo,hi=3.0,60.0
    f=lambda Z:zc(Z,five)-zw
    # scan for sign change
    prev=None;roots=[]
    Z=3.0
    while Z<60:
        v=f(Z)
        if prev is not None and prev*v<0:
            a,b=Z-0.001,Z
            for _ in range(60):
                m=(a+b)/2
                if f(a)*f(m)<=0:b=m
                else:a=m
            roots.append(round(a,3))
        prev=v;Z+=0.001
    return roots
print('wall z',zw)
print('roots with 5Z/8',solve(True)); print('roots without 5Z/8',solve(False))
