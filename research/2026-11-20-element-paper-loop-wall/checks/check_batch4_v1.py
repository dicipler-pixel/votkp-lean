# SCRIPT: CHECK-GPT-ELEMENTS-BATCH4-01
# Recompute every z and Gamma of batch 4 (S to Ca) from its own energy column; check the
# opening sides, the S_Z / sigma_Z table and the exact identity Z(S - sigma) = D_H - sigma^2/2,
# the crossing point, and the face apices tanh(r/4) = (sqrt z - 1)/(sqrt z + 1).
import csv, math
rows=[r for r in csv.DictReader(open('batch4.csv')) if r['IE_k (eV)']!='']
w=3+2*math.sqrt(2); by={}
for r in rows: by.setdefault(r['symbol'],[]).append(r)
bad=n=0
for el,rs in by.items():
    for a,b in zip(rs,rs[1:]):
        if a['z_k']=='': continue
        x,y=float(a['IE_k (eV)']),float(b['IE_k (eV)']); z=y/x; g=(y-x)/(y+x); n+=1
        if abs(z-float(a['z_k']))>6e-6 or abs(g-float(a['Gamma_k']))>6e-6: bad+=1; print('MISMATCH',el,a['k'],round(z,6),round(g,6),a['z_k'],a['Gamma_k'])
print('steps',n,'mismatches',bad)
E={el:{int(r['k']):float(r['IE_k (eV)']) for r in rs} for el,rs in by.items()}
Zs={'S':16,'Cl':17,'Ar':18,'K':19,'Ca':20}
side=lambda z:'out' if z>w else 'in'
apex=lambda z:(math.sqrt(z)-1)/(math.sqrt(z)+1)
for el,Z in Zs.items():
    e=E[el]; out=[]
    if 0 in e: z=e[1]/e[0]; out.append('rung0 %.5f %s apex %.5f'%(z,side(z),apex(z)))
    if Z>=19: z=e[Z-17]/e[Z-18]; out.append('M %.5f %s apex %.5f'%(z,side(z),apex(z)))
    z=e[Z-9]/e[Z-10]; out.append('L %.5f %s apex %.5f'%(z,side(z),apex(z)))
    z=e[Z-1]/e[Z-2]; out.append('K %.5f %s apex %.5f'%(z,side(z),apex(z)))
    print(el,' | '.join(out))
Eh=27.211386245981
prev=None
for Z,el in [(10,None),(13,None)]+[(Z,el) for el,Z in Zs.items()]:
    pass
for el,Z in Zs.items():
    e=E[el]; h=e[Z]/Eh; b=e[Z-1]/Eh; S=(h-b)/Z; s=Z-math.sqrt(2*b); D=h-Z*Z/2
    print(el,'S %.6f sigma %.6f D_H %.6f sigma2/2 %.6f identity err %.1e'%(S,s,D,s*s/2,Z*(S-s)-(D-s*s/2)))
print('Al-Si crossing: interp Z',13+(0.190898-0.175596)/((0.237478-0.175596)-(0.188967-0.190898)))
print('Ca rung0 at EA high end',6.11315547/0.02465)
