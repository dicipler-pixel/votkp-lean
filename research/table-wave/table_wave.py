# SCRIPT: TABLE-WAVE-01
# Question: is the periodic table a real wave, and in which coordinate?
# Data: first ionization energies and first peel steps for Z = 1..85 from the peel periodic table's own data file (ptable_data.json).
# Method: for a coordinate u(Z), fit one sine wave (sin + cos + constant + straight-line trend) at each trial frequency and
# record the share of the variance the wave explains. A real wave in that coordinate shows one tall peak.
# Why it can fail: if the table is not a wave in u, no frequency explains much more than shuffled data does.
# Kill lines, written before the run:
#  W1: Russell's fixed octave (wavelength 8 in Z) explains less than half the variance on Z = 3..20 (then even his home range is not a wave)
#  W2: the same fixed octave explains more than a quarter of the variance on Z = 21..85 (then it does NOT break where expected)
#  W3: the cube-root coordinate (6Z)^(1/3) has a best single wave no better than plain Z (then "real wave in the cube root" failed this way)
#  W4: the cube-root peak is not above the 99th percentile of 500 shuffles (then it is noise)
import json, numpy as np
d=json.load(open('ptable_data.json'))['elements']
Z=np.array([e['Z'] for e in d],float); ie=np.array([e['ie'][0] for e in d]); per=np.array([e['period'] for e in d])
y_ie=np.log(ie)
g=[]
for e in d:
    g.append(np.tanh(0.5*np.log(e['ie'][1]/e['ie'][0])) if len(e['ie'])>1 else np.nan)
g=np.array(g)
def r2_at(u,y,f):
    m=~np.isnan(y); u=u[m]; y=y[m]
    A0=np.c_[np.ones_like(u),u]; r0=y-A0@np.linalg.lstsq(A0,y,rcond=None)[0]
    A=np.c_[A0,np.sin(2*np.pi*f*u),np.cos(2*np.pi*f*u)]; r=y-A@np.linalg.lstsq(A,y,rcond=None)[0]
    return 1-(r@r)/(r0@r0)
def best(u,y,fs):
    v=[r2_at(u,y,f) for f in fs]; k=int(np.argmax(v)); return v[k],fs[k]
# exact period phase: period index + fraction through the period
start={1:1,2:3,3:11,4:19,5:37,6:55}; length={1:2,2:8,3:8,4:18,5:18,6:32}
def true_period(z):
    return 1 if z<=2 else 2 if z<=10 else 3 if z<=18 else 4 if z<=36 else 5 if z<=54 else 6
u_per=np.array([true_period(z)+(z-start[true_period(z)])/length[true_period(z)] for z in Z])
u_cub=(6*Z)**(1/3)
print('elements:',len(Z),' Z from',int(Z.min()),'to',int(Z.max()))
for name,y in (('log first ionization energy',y_ie),('first peel step Gamma = tanh(half log of second over first)',g)):
    print('---',name)
    lo=(Z>=3)&(Z<=20); hi=Z>=21
    print(' W1 fixed octave, wavelength 8 in Z, on Z=3..20 : variance explained %.3f'%r2_at(Z[lo],y[lo],1/8))
    print(' W2 fixed octave, wavelength 8 in Z, on Z=21..85: variance explained %.3f'%r2_at(Z[hi],y[hi],1/8))
    bz=best(Z,y,np.linspace(0.02,0.5,481)); print(' plain Z, best single wave      : %.3f at wavelength %.2f in Z'%(bz[0],1/bz[1]))
    bc=best(u_cub,y,np.linspace(0.2,2.5,461)); print(' W3 cube-root coordinate, best  : %.3f at wavelength %.3f in (6Z)^(1/3)'%(bc[0],1/bc[1]))
    bp=r2_at(u_per,y,1.0); print(' sorted by the true periods (one wave per period): %.3f'%bp)
    rng=np.random.default_rng(3); sh=[]
    for _ in range(500):
        ys=y.copy(); m=~np.isnan(ys); ys[m]=rng.permutation(ys[m]); sh.append(best(u_cub,ys,np.linspace(0.2,2.5,116))[0])
    print(' W4 shuffled data, cube-root best: median %.3f, 99th percentile %.3f'%(np.median(sh),np.percentile(sh,99)))
print('--- where the wave crests fall')
for nm,zs in (('noble gases',[2,10,18,36,54,86]),('alkaline earths',[4,12,20,38,56,88])):
    u=[(6*z)**(1/3) for z in zs]; print(' ',nm,zs,'-> (6Z)^(1/3):',np.round(u,3),' spacings:',np.round(np.diff(u),3))
