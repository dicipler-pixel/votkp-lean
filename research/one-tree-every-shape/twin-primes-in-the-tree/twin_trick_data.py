# SCRIPT: TWIN-TRICK-DATA-01
# Data for the three views. Kill lines (written before the run):
#  View 1: endpoint ratio d/L and frame turn of the real chain vs 50 arm-shuffled chains at 1e8; real inside both spreads -> the ball's endpoint/turn do not read order.
#  View 3: phase clock adds < 0.01 bits about the next air -> one clock suffices.
import numpy as np, math, json
rng=np.random.default_rng(7)
N=10**8
s=np.ones(N+1,dtype=bool); s[:2]=False
for i in range(2,int(N**.5)+1):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0]; tw=P[:-1][(P[1:]-P[:-1])==2]; T=tw[tw>5]
arm=np.searchsorted([1,7,9],T%10)
C2=0.6601618158468696
out={}
# ---------- view 1: chain through the ball (true ratios a'/a along arm of NEXT pair's end digit) ----------
def boost(u,r):
    B=np.eye(4); c,sh=math.cosh(r),math.sinh(r); B[0,0]=c; B[0,u+1]=B[u+1,0]=sh; B[u+1,u+1]=c; return B
def walk(arms,record_every=0):
    L=np.eye(4); pts=[]; path=0.0
    for idx in range(len(T)-1):
        r=math.log(T[idx+1]/T[idx]); path+=r
        L=L@boost(arms[idx+1],r)
        if record_every and (idx%record_every==0 or idx<400 and idx%2==0):
            v=L[:,0]; pts.append([float(v[1]/(1+v[0])),float(v[2]/(1+v[0])),float(v[3]/(1+v[0])),float(path)])
    v=L[:,0]; d=math.acosh(v[0])
    # frame turn: polar split
    gam=v[0]; n=v[1:]/math.sqrt(gam*gam-1); Bst=np.eye(4); Bst[0,0]=gam; Bst[0,1:]=Bst[1:,0]=math.sinh(d)*n; Bst[1:,1:]=np.eye(3)+(gam-1)*np.outer(n,n)
    R=(np.linalg.inv(Bst)@L)[1:,1:]; turn=math.degrees(math.acos(max(-1,min(1,(np.trace(R)-1)/2))))
    return d,path,turn,pts
d,path,turn,pts=walk(arm,record_every=600)
out['v1']={'d':d,'path':path,'ratio':d/path,'turn':turn,'pts':pts,'steps':int(len(T)-1)}
sh=[]
for _ in range(50):
    a2=arm.copy(); rng.shuffle(a2); dd,pp,tt,_=walk(a2); sh.append([dd/pp,tt])
sh=np.array(sh)
out['v1']['shuf_ratio']=[float(x) for x in np.percentile(sh[:,0],[2.5,50,97.5])]
out['v1']['shuf_turn']=[float(x) for x in np.percentile(sh[:,1],[2.5,50,97.5])]
print('V1 real ratio %.4f turn %.3f ; shuffled ratio %s turn %s'%(d/path,turn,np.round(out['v1']['shuf_ratio'],4),np.round(out['v1']['shuf_turn'],2)))
# ---------- view 2: ladder of twins: first 40 rungs + air shares by decade ----------
a=(T[1:]-T[:-1]-2)
first=[[int(T[i]),int(a[i]),int(a[i]%30)] for i in range(40)]
dec=[]
for lo,hi in [(1e3,1e4),(1e4,1e5),(1e5,1e6),(1e6,1e7),(1e7,1e8)]:
    m=(T[:-1]>=lo)&(T[:-1]<hi); dec.append([lo]+[float((a[m]%30==k).mean()) for k in (4,10,16,22,28)])
out['v2']={'first':first,'dec':dec,'limit':[1/9,2/9,2/9,1/9,3/9]}
# ---------- view 3: two clocks ----------
g=(T[1:]-T[:-1]).astype(float); lp=np.log(T[:-1].astype(float)); rr=g/(lp**2/(2*C2)); ac=(a%30)
def H(x):
    _,c=np.unique(x,return_counts=True); p=c/c.sum(); return float(-(p*np.log2(p)).sum())
m=T[:-1]>1e6
st=T[:-1]%30
mi=H(st[m])+H(ac[m])-H(st[m]*100+ac[m])
idx=rng.choice(np.nonzero(m)[0],2500,replace=False)
out['v3']={'H':H(ac[m]),'MI':mi,'mean_by_start':{int(k):float(rr[m][st[m]==k].mean()) for k in (11,17,29)},
  'cv':float(rr[m].std()/rr[m].mean()),
  'pts':[[float(lp[i]),int(st[i]),int(ac[i])] for i in idx],'tmax':float(math.log(1e8))}
print('V3 H %.3f MI %.3f cv %.3f means %s'%(out['v3']['H'],mi,out['v3']['cv'],out['v3']['mean_by_start']))
json.dump(out,open('twin_trick_data.json','w'))
print('pts v1',len(pts))
