# SCRIPT: KNOT-CS-02
# Opposite for KNOT-CS-01. Instead of the whole swept area, read the turn at single points of light on the circle,
# t = e^{2 pi i/N}, which is where the complexified volume conjecture puts Chern-Simons (arg of the coloured Jones
# at large N). Only the uncoloured Jones is available, so this is the lowest rung of that ladder.
# Test: arg V(e^{2 pi i/N}) against CS (as an angle and |CS|), and against signature, for N = 3..10.
import numpy as np, database_knotinfo as d
from scipy.stats import spearmanr
X=[]
for r in d.link_list():
    if not r['jones_polynomial_vector']: continue
    try: vol=float(r['volume']); cs=float(r['volume_imaginary_part']); sig=int(r['signature'])
    except (ValueError,TypeError): continue
    if vol<=0: continue
    v=eval(r['jones_polynomial_vector']); X.append((v,cs,sig,vol))
def circ(x,ang):
    A=np.column_stack([np.cos(ang),np.sin(ang),np.ones_like(ang)]); c,*_=np.linalg.lstsq(A,x,rcond=None); p=A@c
    return np.sqrt(1-np.sum((x-p)**2)/np.sum((x-x.mean())**2))
cs=np.array([x[1] for x in X]); sig=np.array([x[2] for x in X]); vol=np.array([x[3] for x in X]); phi=2*np.pi*cs/np.pi**2
print(' N   arg V vs CS-angle   arg V vs |CS|   arg V vs signature   log|V| vs volume')
for N in range(3,11):
    t=np.exp(2j*np.pi/N); val=np.array([np.polyval(np.array(v[2:],float)[::-1],t)*t**v[0] for v,_,_,_ in X])
    a=np.angle(val); m=np.log(np.abs(val)+1e-12)
    print('%2d      %.3f             %+.3f            %+.3f              %+.3f'%(N,circ(a,phi),spearmanr(a,abs(cs))[0],spearmanr(a,sig)[0],spearmanr(m,vol)[0]))
