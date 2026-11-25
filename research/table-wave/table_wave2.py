# SCRIPT: TABLE-WAVE-02
# The single smooth wave failed its noise line in TABLE-WAVE-01. Same data, same noise line, a different wave SHAPE:
# a repeating ramp (sawtooth), built from the first three harmonics of one fundamental. Same test for the shuffles.
# Kill lines, written before the run:
#  S1: in the cube-root coordinate the three-harmonic wave is not above the 99th percentile of 500 shuffles given the same fit
#  S2: sorted by the true periods, a three-harmonic wave explains less than 60 percent of the variance
#  S3: a wave with wavelength one period PAIR (two periods per wave, three harmonics) does no better in the cube-root coordinate than wavelength one
import json, numpy as np
d=json.load(open('ptable_data.json'))['elements']
Z=np.array([e['Z'] for e in d],float); y=np.log(np.array([e['ie'][0] for e in d]))
def r2(u,y,f,H):
    A0=np.c_[np.ones_like(u),u]; r0=y-A0@np.linalg.lstsq(A0,y,rcond=None)[0]
    cols=[A0]+[np.c_[np.sin(2*np.pi*h*f*u),np.cos(2*np.pi*h*f*u)] for h in range(1,H+1)]
    A=np.hstack(cols); r=y-A@np.linalg.lstsq(A,y,rcond=None)[0]; return 1-(r@r)/(r0@r0)
def best(u,y,fs,H):
    v=[r2(u,y,f,H) for f in fs]; k=int(np.argmax(v)); return v[k],fs[k]
tp=lambda z: 1 if z<=2 else 2 if z<=10 else 3 if z<=18 else 4 if z<=36 else 5 if z<=54 else 6
start={1:1,2:3,3:11,4:19,5:37,6:55}; length={1:2,2:8,3:8,4:18,5:18,6:32}
u_per=np.array([tp(z)+(z-start[tp(z)])/length[tp(z)] for z in Z]); u_cub=(6*Z)**(1/3)
fs1=np.linspace(0.7,1.3,61); fs2=np.linspace(0.35,0.65,61)
b1=best(u_cub,y,fs1,3); b2=best(u_cub,y,fs2,3)
rng=np.random.default_rng(4); sh=[best(u_cub,rng.permutation(y),fs1,3)[0] for _ in range(500)]
print('S1 cube-root, ramp of 3 harmonics, wavelength near 1 : %.3f at wavelength %.3f ; shuffles median %.3f, 99th percentile %.3f'%(b1[0],1/b1[1],np.median(sh),np.percentile(sh,99)))
print('S3 cube-root, ramp of 3 harmonics, wavelength near 2 : %.3f at wavelength %.3f'%(b2[0],1/b2[1]))
for H in (1,2,3,5): print('S2 sorted by true periods, %d harmonic(s): %.3f'%(H,r2(u_per,y,1.0,H)))
print('plain Z, ramp of 3 harmonics, best over wavelengths 4..40: %.3f at wavelength %.2f'%((lambda b:(b[0],1/b[1]))(best(Z,y,np.linspace(1/40,1/4,200),3))))
# Russell's octave as a valence triangle: +1 +2 +3 4 -3 -2 -1 0 against the most common valences of periods 2 and 3
val={3:1,4:2,5:3,6:4,7:-3,8:-2,9:-1,10:0,11:1,12:2,13:3,14:4,15:-3,16:-2,17:-1,18:0}
tri=lambda k:[1,2,3,4,-3,-2,-1,0][k]
print('Russell octave as valence, periods 2 and 3: matches',sum(1 for z in val if val[z]==tri((z-3)%8)),'of',len(val))
