# SCRIPT: BOWL-HALF-01
# Piecing-map question: does the vacuum-disk bowl have a feature at |G|^2 = 1/2, the line that appears in Two Trees,
# the knot commutator band, the elements and the alkali steps?
# Why this would show it: (1) the exact volume D averaged round the circle |G| = r is a smooth function of r^2; a feature
# would be a special value or a change of behaviour at r^2 = 1/2; (2) on real knot tetrahedra the error of the bowl law
# would change character across the line.  Kill: neither shows anything at 1/2.
import numpy as np, mpmath as mp, snappy, warnings
warnings.filterwarnings('ignore')
from database_knotinfo import link_list
w=np.exp(1j*np.pi/3); V0=float(mp.im(mp.polylog(2,mp.e**(1j*mp.pi/3)))); k2=3*np.sqrt(3)/4
def D(z):
    z=complex(z); return float(mp.im(mp.polylog(2,z))+mp.arg(1-z)*mp.log(abs(z)))
def zofG(G): return (w-np.conj(w)*G)/(1-G)
print('circle average of the exact volume, and its share of V0:')
for r2 in (0.1,0.25,0.4,0.5,0.6,0.75,0.9):
    r=np.sqrt(r2); th=np.linspace(0,2*np.pi,721)[:-1]; a=np.mean([D(zofG(r*np.exp(1j*t))) for t in th])
    print('  |G|^2 = %.2f  mean D = %.6f  share %.4f  quadratic bowl %.6f  bowl+quartic %.6f'%(r2,a,a/V0,V0-k2*r2,V0-k2*r2+3*np.sqrt(3)/16*r2*r2))
G2=[];err=[]
for k in link_list()[1:]:
    if int(k['crossing_number'])>10: continue
    try: M=snappy.Manifold(k['name'])
    except Exception: continue
    if M.volume()<1e-6: continue
    for z in M.tetrahedra_shapes('rect'):
        z=complex(z); G=(z-w)/(z-np.conj(w)); g2=abs(G)**2; d=D(z)
        q=V0-k2*g2+np.sqrt(3)/8*2*(G**3).real+3*np.sqrt(3)/16*g2*g2
        G2.append(g2); err.append(q-d)
G2=np.array(G2); err=np.array(err)
print('\ntetrahedra (knots to 10 crossings):',len(G2),' share with |G|^2 < 1/2: %.3f'%np.mean(G2<0.5))
for lo,hi in ((0,.1),(.1,.25),(.25,.4),(.4,.5),(.5,.6),(.6,.8),(.8,1.0),(1.0,99)):
    m=(G2>=lo)&(G2<hi)
    if m.sum(): print('  |G|^2 in [%.2f,%.2f): n=%5d  median |bowl error| %.5f  mean signed %.5f'%(lo,hi,m.sum(),np.median(abs(err[m])),err[m].mean()))
