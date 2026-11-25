# SCRIPT: TABLE-WAVE-03
# "Test the rest": the same wave tests on the other properties of the elements, Z = 1..86.
# Data: the mendeleev package (version printed below); polarizabilities there are the 2018 Schwerdtfeger-Nagle table,
# radii are Pyykko single-bond covalent radii, plus electron affinity, Pauling electronegativity, melting point.
# First ionization energy is re-run from the same package as a control against TABLE-WAVE-01/02 (other data file).
# For each property, four numbers:
#   OCT_LO  Russell's fixed octave (wavelength 8 in Z) on Z = 3..20
#   OCT_HI  the same on Z = 21..86
#   ONE     ramp of 3 harmonics, one wave per period, in the cube-root coordinate (6Z)^(1/3), wavelength searched 0.77..1.43
#   PAIR    ramp of 3 harmonics, one wave per PAIR of periods, wavelength searched 1.54..2.86
#   each of ONE and PAIR is compared with the 99th percentile of 300 shuffles given the identical search.
#   TRUE3   sorted by the true periods, 3 harmonics
# Second control added this run: the PAIR peak must also beat the best fit in two off bands (wavelengths 1.25..1.5 and 3.0..3.6);
# a smooth drift would pass a shuffle test but not this.
# Kill lines, written before the run, applied to every property:
#   P1: PAIR not above its 99 percent shuffle line                  -> "no pair wave in this property"
#   P2: PAIR not above both off bands                               -> "the pair wavelength is not special for this property"
#   P3: OCT_LO below one half, or OCT_HI above one quarter          -> "Russell's octave does not behave as it did for ionization energy"
# Prediction recorded before the run: ionization energy, electronegativity, radius and polarizability pass P1 and P2;
# melting point (a bulk property) and electron affinity (many elements bind no extra electron) are the likeliest to fail.
import numpy as np, mendeleev
from mendeleev import element
print('mendeleev version',mendeleev.__version__)
E=[element(z) for z in range(1,87)]
Z=np.arange(1,87,dtype=float)
def col(f):
    out=[]
    for e in E:
        try: v=f(e)
        except Exception: v=None
        out.append(np.nan if v is None else float(v))
    return np.array(out)
props={
 'log first ionization energy':np.log(col(lambda e:e.ionenergies[1])),
 'Pauling electronegativity':col(lambda e:e.en_pauling),
 'log covalent radius (Pyykko)':np.log(col(lambda e:e.covalent_radius_pyykko)),
 'log dipole polarizability':np.log(col(lambda e:e.dipole_polarizability)),
 'electron affinity':col(lambda e:e.electron_affinity),
 'log melting point':np.log(col(lambda e:e.melting_point)),
}
def r2(u,y,f,H):
    A0=np.c_[np.ones_like(u),u]; r0=y-A0@np.linalg.lstsq(A0,y,rcond=None)[0]
    A=np.hstack([A0]+[np.c_[np.sin(2*np.pi*h*f*u),np.cos(2*np.pi*h*f*u)] for h in range(1,H+1)])
    r=y-A@np.linalg.lstsq(A,y,rcond=None)[0]; return 1-(r@r)/(r0@r0)
def best(u,y,fs,H): 
    v=[r2(u,y,f,H) for f in fs]; k=int(np.argmax(v)); return v[k],1/fs[k]
tp=lambda z: 1 if z<=2 else 2 if z<=10 else 3 if z<=18 else 4 if z<=36 else 5 if z<=54 else 6
start={1:1,2:3,3:11,4:19,5:37,6:55}; length={1:2,2:8,3:8,4:18,5:18,6:32}
f_one=np.linspace(0.7,1.3,41); f_pair=np.linspace(0.35,0.65,41); f_offa=np.linspace(1/1.5,1/1.25,21); f_offb=np.linspace(1/3.6,1/3.0,21)
rng=np.random.default_rng(12)
print('%-30s %4s %6s %6s | %5s %5s | %5s %5s %5s | %5s %5s | %5s | verdict'%('property','n','OCT_LO','OCT_HI','ONE','99%','PAIR','wave','99%','offA','offB','TRUE3'))
for name,yy in props.items():
    m=~np.isnan(yy); z=Z[m]; y=yy[m]; uc=(6*z)**(1/3); up=np.array([tp(q)+(q-start[tp(q)])/length[tp(q)] for q in z])
    lo=(z>=3)&(z<=20); hi=z>=21
    olo=r2(z[lo],y[lo],1/8,1) if lo.sum()>8 else np.nan; ohi=r2(z[hi],y[hi],1/8,1)
    one=best(uc,y,f_one,3); pair=best(uc,y,f_pair,3); oa=best(uc,y,f_offa,3)[0]; ob=best(uc,y,f_offb,3)[0]
    s1=[];s2=[]
    for _ in range(300):
        ys=rng.permutation(y); s1.append(best(uc,ys,f_one,3)[0]); s2.append(best(uc,ys,f_pair,3)[0])
    q1=np.percentile(s1,99); q2=np.percentile(s2,99); t3=r2(up,y,1.0,3)
    v=[]
    v.append('P1 held' if pair[0]>q2 else 'P1 FIRED')
    v.append('P2 held' if pair[0]>max(oa,ob) else 'P2 FIRED')
    v.append('P3 held' if (olo>=0.5 and ohi<=0.25) else 'P3 FIRED')
    print('%-30s %4d %6.3f %6.3f | %5.3f %5.3f | %5.3f %5.2f %5.3f | %5.3f %5.3f | %5.3f | %s'%(name,m.sum(),olo,ohi,one[0],q1,pair[0],pair[1],q2,oa,ob,t3,', '.join(v)))
