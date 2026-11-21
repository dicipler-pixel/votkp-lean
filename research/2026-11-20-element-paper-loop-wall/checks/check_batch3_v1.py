# SCRIPT: CHECK-GPT-ELEMENTS-BATCH3-01
# Recompute every z and Gamma of batch 3 (Na to P) from its own energy column, check the
# wall sides, the screened series, S_Z / sigma_Z, silicon's sensitivity interval, and the
# sodium compression fraction.
import csv, math
rows=list(csv.DictReader(open('batch3.csv')))
w=3+2*math.sqrt(2); bad=0; n=0
by={}
for r in rows: by.setdefault(r['symbol'],[]).append(r)
for el,rs in by.items():
    for a,b in zip(rs,rs[1:]):
        if a['z_k']=='': continue
        x,y=float(a['IE_k (eV)']),float(b['IE_k (eV)']); z=y/x; g=(y-x)/(y+x); n+=1
        if abs(z-float(a['z_k']))>6e-6 or abs(g-float(a['Gamma_k']))>6e-6: bad+=1; print('MISMATCH',el,a['k'],z,g)
print('steps',n,'mismatches',bad)
E={el:{int(r['k']):float(r['IE_k (eV)']) for r in rs} for el,rs in by.items()}
Zs={'Na':11,'Mg':12,'Al':13,'Si':14,'P':15}
side=lambda z:'outside' if z>w else 'inside'
for el,Z in Zs.items():
    e=E[el]; L=e[Z-9]/e[Z-10]; K=e[Z-1]/e[Z-2]
    r0=(e[1]/e[0]) if 0 in e else None
    print(el,'rung0',None if r0 is None else (round(r0,5),side(r0)),'| L',round(L,5),side(L),'| K',round(K,5),side(K))
for el,Z in Zs.items():
    core=Z*Z/2-5*Z/8+0.157666; val=Z*Z/8-290*Z/729+0.2505
    print(el,'screened K ratio %.5f'%(core/val))
Eh=27.211386246
for el,Z in Zs.items():
    e=E[el]; print(el,'S_Z %.5f sigma_Z %.5f'%((e[Z]-e[Z-1])/(Z*Eh), Z-math.sqrt(2*e[Z-1]/Eh)))
g=lambda I,A:(I-A)/(I+A)
print('Si Gamma0 interval',g(8.15168-3e-5,1.3895212+7e-7),g(8.15168+3e-5,1.3895212-7e-7),'wall',1/math.sqrt(2))
print('L-opening wall charge ratio',math.sqrt(w/2.25),'Na',math.sqrt(9.20133/2.25),'Mg',math.sqrt(5.33037/2.25))
print('Na ball 1.55A',4*math.pi*1.55**3/3,'f ambient',4*math.pi*1.55**3/3/39.438,'f 310GPa',4*math.pi*1.55**3/3/6.641)
