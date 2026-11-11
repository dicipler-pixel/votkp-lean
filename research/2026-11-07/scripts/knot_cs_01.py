# SCRIPT: KNOT-CS-01
# Does the turn book carry the imaginary half of complex volume (Chern-Simons, KnotInfo 'volume_imaginary_part',
# defined modulo pi^2)? Friedl-Jackson (2011) left open whether the arguments of Alexander zeros relate to Chern-Simons.
# Why this checks it: the climb (Mahler measure) already tracks the real half (volume). If the two books really are
# the two halves of Vol + i CS, the turn should track CS. CS is an angle (mod pi^2), so it is also tested as an angle.
import numpy as np, database_knotinfo as d
from scipy.stats import spearmanr
th=np.linspace(0,2*np.pi,4097)[:-1]; t=np.exp(1j*th)
X=[]
for r in d.link_list():
    if not r['jones_polynomial_vector'] or not r['alexander_polynomial_vector']: continue
    try: vol=float(r['volume']); cs=float(r['volume_imaginary_part']); sig=int(r['signature'])
    except (ValueError,TypeError): continue
    if vol<=0: continue
    v=eval(r['jones_polynomial_vector']); c=np.array(v[2:],float); p=np.polyval(c[::-1],t)*t**v[0]
    dz=np.roll(p,-1)-p; turn=0.5*np.sum(p.real*dz.imag-p.imag*dz.real)/np.mean(np.abs(p)**2)
    a=eval(r['alexander_polynomial_vector']); ra=np.roots(np.array(a[2:],float)[::-1])
    unit=ra[np.abs(np.abs(ra)-1)<1e-6]; up=unit[unit.imag>1e-9]
    alex_arg=np.mean(np.angle(up)) if len(up) else np.nan       # mean argument of unit-circle zeros, upper half
    jr=np.roots(c[::-1]); jarg=np.mean(np.angle(jr[jr.imag>1e-9])) if np.any(jr.imag>1e-9) else np.nan
    X.append((vol,cs,sig,turn,alex_arg,jarg))
vol,cs,sig,turn,aarg,jarg=np.array(X).T
print('n =',len(vol))
print('signed turn vs signed CS:      rho=%.3f'%spearmanr(turn,cs)[0])
print('|turn| vs |CS|:                rho=%.3f'%spearmanr(abs(turn),abs(cs))[0])
print('signature vs signed CS:        rho=%.3f   (sign convention check)'%spearmanr(sig,cs)[0])
phi=2*np.pi*cs/np.pi**2
def circ(x,ang):   # correlation of a line variable with an angle (Mardia): sqrt of R^2 from regressing x on cos, sin
    A=np.column_stack([np.cos(ang),np.sin(ang),np.ones_like(ang)]); c,*_=np.linalg.lstsq(A,x,rcond=None); p=A@c
    return np.sqrt(1-np.sum((x-p)**2)/np.sum((x-x.mean())**2))
print('turn vs CS as an angle:        r=%.3f'%circ(turn,phi))
ok=~np.isnan(aarg); print('Alexander zero angle vs CS angle (n=%d): r=%.3f ; vs |CS| rho=%.3f'%(ok.sum(),circ(aarg[ok],phi[ok]),spearmanr(aarg[ok],abs(cs[ok]))[0]))
ok=~np.isnan(jarg); print('Jones zero angle vs CS angle:  r=%.3f ; vs |CS| rho=%.3f'%(circ(jarg[ok],phi[ok]),spearmanr(jarg[ok],abs(cs[ok]))[0]))
rng=np.random.default_rng(1); print('null (shuffled CS) for the angle test: r=%.3f'%np.mean([circ(turn,rng.permutation(phi)) for _ in range(50)]))
