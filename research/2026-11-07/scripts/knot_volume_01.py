# SCRIPT: KNOT-VOLUME-01
# Exploratory. The first meaning of VOTKP (volume of the knot potential), run through the two books.
# Each knot's Jones polynomial is a string of light: let t = e^{i theta} run once around the circle, the way colour runs
# violet to red, and follow V(t) as a track in the plane. Since V(1) = 1, every track leaves the same point and comes back to it.
#   climb book = Mahler measure m(V) = mean of log|V| around the circle (how far out the string climbs)
#   turn book  = how many times the track winds around 0 (the vacuum the closed string encloses)
#                = number of Jones roots inside the unit circle (argument principle, after removing the t^k factor)
# Target: hyperbolic volume of the knot complement (KnotInfo), every hyperbolic knot with 3-12 crossings.
# Baselines: crossing number, and log|det| (Dunfield's observation that log det tracks volume).
import numpy as np, database_knotinfo as d, re
from scipy.stats import spearmanr
th=np.linspace(0,2*np.pi,4097)[:-1]; t=np.exp(1j*th)
rows=[]
for r in d.link_list():
    if not r['volume'] or not r['jones_polynomial_vector']: continue
    try: vol=float(r['volume'])
    except ValueError: continue
    if vol<=0: continue
    v=eval(r['jones_polynomial_vector']); lo,hi,c=v[0],v[1],np.array(v[2:],float)
    p=np.polyval(c[::-1],t)                         # V(t)/t^lo, same |V|, no t^k winding
    mahler=np.mean(np.log(np.abs(p)))
    roots=np.roots(c[::-1]); inside=int(np.sum(np.abs(roots)<1-1e-9)); onc=int(np.sum(np.abs(np.abs(roots)-1)<1e-9))
    cr=int(re.match(r'(\d+)',r['name']).group(1))
    rows.append((r['name'],cr,vol,mahler,inside,len(c)-1,np.log(int(r['determinant'])),onc))
R=np.array([x[1:] for x in rows],float); cr,vol,mah,ins,span,ldet,onc=R.T
print('hyperbolic knots, 3-12 crossings:',len(rows))
for nm,x in [('crossing number',cr),('Jones span',span),('log det  [Dunfield baseline]',ldet),('climb: Mahler measure of V',mah),('turn: roots inside (vacuum enclosed)',ins),('turn share: inside / span',ins/span)]:
    print('  %-40s rho=%.3f'%(nm,spearmanr(x,vol)[0]))
print('\nwithin each crossing number (removes the size effect): mean rho over 8..12')
for nm,x in [('log det',ldet),('Mahler (climb)',mah),('inside share (turn)',ins/span)]:
    print('  %-22s'%nm,' '.join('%d:%.2f'%(c,spearmanr(x[cr==c],vol[cr==c])[0]) for c in range(8,13)))
# volume left over after log det: does either book carry it?
k=np.polyfit(ldet,vol,1); res=vol-np.polyval(k,ldet)
print('\nafter log det is taken out: climb rho=%.3f  turn share rho=%.3f'%(spearmanr(mah,res)[0],spearmanr(ins/span,res)[0]))
print('Jones roots sitting on the circle: %d knots of %d'%(np.sum(onc>0),len(rows)))
