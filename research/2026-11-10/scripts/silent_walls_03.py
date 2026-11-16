# SCRIPT: SILENT-WALLS-03
# Next question from SILENT-WALLS-02: what decides whether a silent double wall is a TOUCH (nullity 1) or an
# OPPOSED CROSSING (nullity 2)?
# Proposal written before the run: the knot's Alexander module at that factor f.
#   cyclic part  Z[t]/(f^2)          -> one Jordan block of size 2 -> one level touches zero        (nullity 1)
#   split part   Z[t]/(f) + Z[t]/(f) -> two independent levels                                      (nullity 2)
# KnotInfo lists the SECOND Alexander polynomial; f divides it exactly in the split case.
# Why this decides it: the two data columns are independent (signature function and nullity on one side, second Alexander
# polynomial on the other). Kill: any double root where "root of the second Alexander polynomial" disagrees with "nullity 2".
# Second question: which way do the touches go? at-side sign against the sign of the side signature.
import collections, sympy as sp
from database_knotinfo import link_list
t=sp.symbols('t'); rows=[]
for k in link_list()[1:]:
    sf=k['signature_function']
    if not sf or sf=='[0]': continue
    try: ent=eval(sf)
    except Exception: continue
    if not isinstance(ent,list) or not ent or not isinstance(ent[0],list): continue
    fac=sp.factor_list(sp.Poly(sp.sympify(k['alexander_polynomial'].replace('^','**')),t))[1]
    a2s=(k.get('second_alexander_polynomial') or '').strip()
    try: A2=sp.Poly(sp.sympify(a2s.replace('^','**')),t) if a2s else None
    except Exception: A2=None
    for e in ent:
        w=complex(sp.exp(sp.pi*sp.I*e[0]).evalf()); mult=sum(m for f,m in fac if abs(complex(f.as_expr().subs(t,w).evalf()))<1e-8)
        if mult!=2: continue
        in2=None if A2 is None else (abs(complex(A2.as_expr().subs(t,w).evalf()))<1e-8)
        l,a,r=e[1]; rows.append(dict(name=k['name'],jump=r-l,nul=e[2],at=a-l,side=l,in2=in2))
have=[r for r in rows if r['in2'] is not None]
print('double roots:',len(rows),' with a second Alexander polynomial listed:',len(have))
c=collections.Counter((r['nul'],r['in2']) for r in have)
for key,v in sorted(c.items()): print('   nullity %d, root of second Alexander polynomial: %s  -> %d'%(key[0],key[1],v))
bad=[r['name'] for r in have if (r['nul']==2)!=r['in2']]
print('   disagreements:',len(bad),bad[:10])
print('\ntouches (nullity 1): direction against the side signature')
c=collections.Counter()
for r in rows:
    if r['nul']==1:
        s=r['side']; c['side 0' if s==0 else ('toward zero' if (r['at']>0)==(s<0) else 'away from zero')]+=1
print('  ',dict(c))
c=collections.Counter((r['side'],r['at']) for r in rows if r['nul']==1 and r['side']==0); print('   at side 0, at-value:',dict(c))
