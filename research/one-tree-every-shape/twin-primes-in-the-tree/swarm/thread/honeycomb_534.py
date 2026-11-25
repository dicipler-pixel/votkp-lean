# SCRIPT: TWIN-HONEYCOMB-534-01
# The twin chain walked on the {5,3,4} dodecahedral honeycomb: every step one edge, cosh l = phi.
# Kill condition and prediction: HONEYCOMB_PREREG.md (written before this run).
import numpy as np, math
phi=(1+5**.5)/2; l=math.acosh(phi)
print('edge length l = %.6f, check cosh(l/2) = %.6f vs cos36/sin45 = %.6f, Gamma^2 = tanh^2(l/2) = %.6f = sqrt5-2 = %.6f'%(
    l,math.cosh(l/2),math.cos(math.pi/5)/math.sin(math.pi/4),math.tanh(l/2)**2,5**.5-2))
sg=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
def B(k,sgn=1): return math.cosh(l/2)*np.eye(2)+sgn*math.sinh(l/2)*sg[k]
def turn_and_d(L):
    W,s,Vh=np.linalg.svd(L); U=W@Vh; t=2*math.degrees(math.acos(min(1,abs(np.trace(U).real)/2)))
    return t, 2*math.log(s[0])
# K-H0: right-angled pentagon loop
Lp=B(0)@B(1)@B(0,-1)@B(1,-1)@B(0)
t,d=turn_and_d(Lp); print('K-H0 pentagon loop: leftover distance %.2e, rotation %.6f deg ->'%(d,t),'PASS' if d<1e-9 and abs(t-90)<1e-6 else 'FAIL (model wrong)')
TW=np.load('../shapes/twins_1000000000.npy').astype(np.int64); TW=TW[TW>=11]
arm={1:0,7:1,9:2}; s=np.array([arm[int(x)%10] for x in TW[1:]])
n=10**6; s=s[:n]
cnt=np.bincount(s,minlength=3)/n; rep=np.mean(s[1:]==s[:-1]); rep0=float(np.sum(cnt**2))
print('first %d twin steps end at twin start %d; arm shares %s'%(n,TW[n],np.round(cnt,5)))
print('consecutive repeat rate %.5f vs independence %.5f (se %.5f)'%(rep,rep0,math.sqrt(rep0*(1-rep0)/n)))
mats=[B(k) for k in range(3)]
def drift(seq,marks=(100,1000)):
    v=np.eye(2,dtype=complex); logs=0.0; tur={}
    for i,k in enumerate(seq):
        v=v@mats[k]; m=np.abs(v).max(); v/=m; logs+=math.log(m)
        if i+1 in marks: tur[i+1]=turn_and_d(v)[0]
    W,sv,Vh=np.linalg.svd(v); dtot=2*(logs+math.log(sv[0]))
    return dtot/len(seq), tur
real,rt=drift(s)
rng=np.random.default_rng(11); sh=[]; st=[]
for j in range(200):
    a,b=drift(rng.permutation(s)); sh.append(a); st.append(b)
sh=np.array(sh); z=(real-sh.mean())/sh.std()
print('drift per step (d/n): real %.6f; shuffles %.6f +- %.6f; z = %.1f'%(real,sh.mean(),sh.std(),z))
print('frame turn after 100 / 1000 edges: real %.3f / %.3f deg; shuffles mean %.2f / %.2f, sd %.2f / %.2f'%(
    rt[100],rt[1000],np.mean([x[100] for x in st]),np.mean([x[1000] for x in st]),np.std([x[100] for x in st]),np.std([x[1000] for x in st])))
print('KILL (no prime signal on the honeycomb)' if abs(z)<2 else 'PASS: the arm order alone carries a prime signal on the honeycomb (z=%.1f)'%z)
