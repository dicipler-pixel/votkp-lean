# SCRIPT: MIRROR-CHECK-01
# For knots where SnapPy Manifold(name) disagrees with the KnotInfo PD drawing: is Manifold(name) exactly the mirror (cs -> -cs mod pi^2)?
import snappy, warnings, numpy as np, database_knotinfo as d, json
warnings.filterwarnings('ignore')
P2=np.pi**2
KI={r['name']:r for r in d.link_list()}
mir=[];same=[];other=[]
for nm in KI:
    if nm.count('_')!=1 or nm.startswith('L') or KI[nm]['crossing_number'] not in list('456789'): continue
    M=snappy.Manifold(nm)
    if M.volume()<0.5: continue
    a=complex(snappy.Link(eval(KI[nm]['pd_notation'])).exterior().complex_volume()); b=complex(M.complex_volume())
    dd=lambda x,y:abs(((x-y)+P2/2)%P2-P2/2)
    if abs(a.real-b.real)>1e-6: other.append(nm)
    elif dd(a.imag,b.imag)<1e-5: same.append(nm)
    elif dd(a.imag,-b.imag)<1e-5: mir.append(nm)
    else: other.append(nm)
print('same chirality:',len(same),' exact mirror:',len(mir),' other:',other)
