# SCRIPT: NEVER-TURN-01
# Two Trees section 9 open question: what do the hyperbolic knots whose meridian commutator never turns (6_3, 7_5, 8_7, 8_8) share?
# Piecing-map prediction 5(a): they should stand apart in DIRECTION (Chern-Simons) from the 19 that turn.
# Why this decides 5(a): direction is read mirror-free as the distance of CS from 0 mod 1/4 (SnapPy period 1/2, mirror flips sign);
# if the four never-turners sit inside the spread of the turners, direction does not separate them.  Kill: they sit inside.
# Second part (lead-finding only, 26 knots, many fields tried): which KnotInfo fields separate never from turn.
import snappy, warnings, numpy as np
warnings.filterwarnings('ignore')
from database_knotinfo import link_list
KI={r['name']:r for r in link_list()[1:]}
never=['3_1','5_1','7_1','6_3','7_5','8_7','8_8']
turn=['4_1','5_2','6_1','6_2','7_2','7_3','8_1','7_4','8_2','8_3','8_4','7_6','7_7','8_6','8_9','8_11','8_13','8_12','8_14']
def fold(c):
    c=c%0.5; return min(c,0.5-c)
print('direction |CS| folded to [0, 1/4]  (SnapPy units)')
D={}
for grp,names in (('never',never),('turn',turn)):
    for n in names:
        M=snappy.Manifold(n)
        if M.volume()<1e-6: D[n]=None; continue
        D[n]=fold(float(M.chern_simons()))
    print(' ',grp,[(n,None if D[n] is None else round(D[n],4)) for n in names])
a=[D[n] for n in never if D[n] is not None]; b=[D[n] for n in turn]
print('  never (hyperbolic) range %.4f..%.4f ; turn range %.4f..%.4f'%(min(a),max(a),min(b),max(b)))
print('  verdict:', 'INSIDE the turners spread (no separation)' if min(b)<=min(a) and max(a)<=max(b) else 'outside')
print('\nKnotInfo fields that split never / turn exactly, or nearly (lead-finding):')
fields=[f for f in KI['6_3'] if not f.endswith('_anon')]
def num(x):
    try: return float(x)
    except Exception: return None
hits=[]
for f in fields:
    va=[KI[n][f] for n in never]; vb=[KI[n][f] for n in turn]
    na=[num(x) for x in va]; nb=[num(x) for x in vb]
    if all(x is not None for x in na+nb):
        A=np.array(na); B=np.array(nb); auc=np.mean([(x>y)+0.5*(x==y) for x in A for y in B]); hits.append((abs(auc-0.5),f,'AUC %.2f'%auc,sorted(set(na)),sorted(set(nb))))
    else:
        sa,sb=set(va),set(vb)
        if len(sa|sb)<=4 and not (sa&sb): hits.append((0.5,f,'disjoint values',sorted(sa),sorted(sb)))
hits.sort(reverse=True)
for h in hits[:8]: print('  %-38s %s  never %s  turn %s'%(h[1],h[2],str(h[3])[:60],str(h[4])[:60]))
