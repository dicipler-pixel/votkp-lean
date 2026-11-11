# SCRIPT: SILENT-WALLS-02
# Open problem 6 of the vacuum-disk paper / VOTKP Table 6: the silent double walls.
# Reading under test (path notes, SILENT-WALLS-01): a silent double wall is where two opposite hands cancel,
# i.e. TWO eigenvalues of H(omega) cross zero in opposite directions.
# What separates it from the alternative: KnotInfo lists, at each root, the signature left / AT / right and the nullity.
#   two opposite crossings  -> nullity 2, signature AT the root = the side value
#   one eigenvalue touching -> nullity 1, signature AT the root = side value +-1   (VOTKP Prop 11.1 allows this)
# Kill for the reading: a silent double wall with nullity 1.
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
    for e in ent:
        w=complex(sp.exp(sp.pi*sp.I*e[0]).evalf()); mult=sum(m for f,m in fac if abs(complex(f.as_expr().subs(t,w).evalf()))<1e-8)
        if mult!=2: continue
        l,a,r=e[1]; rows.append(dict(name=k['name'],jump=r-l,nul=e[2],at=a-l,aco=k['algebraic_concordance_order'],g4=k['topological_four_genus']))
print('double unit-circle roots:',len(rows))
c=collections.Counter(('silent' if r['jump']==0 else 'jump4', 'nullity %d'%r['nul'], 'at-side %+d'%r['at']) for r in rows)
for key,v in sorted(c.items()): print('  ',key,v)
print('\nsilent walls by concordance order and nullity:')
c=collections.Counter((('finite' if r['aco'] in ('1','2','4') else ('infinite' if r['aco'] else 'not listed')),r['nul']) for r in rows if r['jump']==0)
for key,v in sorted(c.items()): print('  ',key,v)
print('\nsilent with nullity 2:',[(r['name'],r['aco'],r['g4']) for r in rows if r['jump']==0 and r['nul']==2][:40])
