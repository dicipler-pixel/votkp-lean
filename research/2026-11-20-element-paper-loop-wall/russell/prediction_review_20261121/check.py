"""Compare the VOTKP equal-face wall with a maximum-margin cutoff, then scan mixed faces."""
import csv,sys,itertools,math
from fractions import Fraction as F
from pathlib import Path
rows=list(csv.DictReader(Path(sys.argv[1]).open()))
def g(z):return (z-1)/(z+1)
def s(z):return g(z)**2
def ratio(r):return F(r['next_energy_eV'])/F(r['energy_eV'])
lo=max(ratio(r) for r in rows if r['central_wall']=='inside')
hi=min(ratio(r) for r in rows if r['central_wall']=='outside')
c=(lo+hi)/2
t=2*s(c)
print('edges, rival, excess power',*[float(v) for v in (lo,hi,c,t-1)])
a=[r for r in rows if r['z']]
print('ordinary and adopted anion pairs, rival disagreements',len(a),sum((ratio(r)>c)!=(r['central_wall']=='outside') for r in a))
print('Fr boundaries',4.0727411*(3+2*math.sqrt(2)),4.0727411*float(c))
m=[]
for n in [0,2,10,18,36,54]:
 group=[r for r in a if (int(r['k'])==0 if not n else int(r['k'])>0 and int(r['Z'])-int(r['k'])==n)]
 for r,b in itertools.combinations(group,2):
    power=s(ratio(r))+s(ratio(b))
    if 1<power<t:
      boxed=all(x['z_lower'] and F(x['z_lower'])>1 and x['z_upper'] for x in (r,b))
      left=sum(s(F(x['z_lower'])-F(1,10**12)) for x in (r,b)) if boxed else None
      right=sum(s(F(x['z_upper'])+F(1,10**12)) for x in (r,b)) if boxed else None
      robust=boxed and left>1 and right<t
      m.append([n,r['symbol'],r['k'],b['symbol'],b['k'],float(power),float(left) if boxed else '',float(right) if boxed else '',robust])
print('mixed central and box-stable',len(m),sum(x[-1] for x in m));print(*[x for x in m if x[-1]][:15],sep='\n')
with (Path(sys.argv[2])/'mixed.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['core_electrons_or_zero_for_anions','symbol_a','k_a','symbol_b','k_b','power','lower','upper','robust']);w.writerows(m)
# Independent implementation: compare the two geometric circles, and multiply
# the four transfer matrices directly without using the mixed-power formula.
def mul(a,b):
 return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def inv(a):
 return [[a[1][1],-a[0][1]],[-a[1][0],a[0][0]]]
def circle(x):
 u=math.tanh(math.log(x)/4)
 return (1+u*u)/(2*u),(1-u*u)/(2*u)
for n,u,k,v,j,*_ in m:
 x,y=[float(ratio(next(r for r in a if r['symbol']==sym and r['k']==idx))) for sym,idx in [(u,k),(v,j)]]
 p,q=map(circle,[x,y])
 assert math.hypot(p[0],q[0])>p[1]+q[1]
 f,h=map(math.sqrt,[x,y])
 M=[[f,0.],[0.,1/f]]
 N=[[(h+1/h)/2,(h-1/h)/2],[(h-1/h)/2,(h+1/h)/2]]
 R=mul(mul(mul(M,N),inv(M)),inv(N)); tr=R[0][0]+R[1][1]
 assert tr < -2 and abs(R[0][0]*R[1][1]-R[0][1]*R[1][0]-1)<1e-12
 print(u,v,'circle open; matrix trace',f'{tr:.10f}')
print('unordered distinct pairs examined:',sum(math.comb(sum(1 for r in a if (int(r['k'])==0 if not n else int(r['k'])>0 and int(r['Z'])-int(r['k'])==n)),2) for n in [0,2,10,18,36,54]))
