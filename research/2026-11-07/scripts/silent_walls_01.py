# SCRIPT: SILENT-WALLS-01
# Exploratory. VOTKP Table 6: double unit-circle Alexander roots that change the signature by 0 (silent) or by +/-4.
# Question: are the silent double walls where two opposite hands meet inside one knot?
# The algebraic shadow of "opposite hands that cancel" is a metabolic Seifert form (a fixed half where the form vanishes,
# the cut L of BRANCH-CUT-02): KnotInfo's algebraic concordance order 1. Cross-tabulate silent vs +/-4 walls
# against algebraic concordance order, ribbon and topological 4-genus. Also: is the Alexander factor that carries
# the double root itself repeated (f^2)?
import collections, sympy as sp
from database_knotinfo import link_list
t=sp.symbols('t')
L=link_list()[1:]
rows=[]
for k in L:
    sf=k['signature_function']
    if not sf or sf=='[0]': continue
    try: ent=eval(sf)
    except Exception: continue
    if not isinstance(ent,list) or not ent or not isinstance(ent[0],list): continue
    # multiplicity from the factored Alexander polynomial at each root
    A=sp.sympify(k['alexander_polynomial'].replace('^','**'))
    fac=sp.factor_list(sp.Poly(A,t))[1]
    for e in ent:
        r=e[0]; left,at,right=e[1]; nul=e[2]
        w=complex(sp.exp(sp.pi*sp.I*r).evalf())
        mult=0; carriers=[]
        for f,m in fac:
            if abs(complex(f.as_expr().subs(t,w).evalf()))<1e-8: mult+=m; carriers.append((str(f.as_expr()),m))
        if mult!=2: continue
        rows.append(dict(name=k['name'],root=r,jump=right-left,aco=k['algebraic_concordance_order'],
                         ribbon=k['ribbon'],g4=k['topological_four_genus'],square=any(m==2 for f,m in carriers)))
print('double unit-circle roots found:',len(rows),' (VOTKP Table 6 lists 575 entries at multiplicity 2)')
cnt=collections.Counter('silent' if r['jump']==0 else 'jump4' for r in rows); print(cnt)
def tab(key,lab):
    c=collections.defaultdict(collections.Counter)
    for r in rows: c[r[key]]['silent' if r['jump']==0 else 'jump4']+=1
    print('\nby',lab)
    for v,cc in sorted(c.items(),key=lambda x:str(x[0])): 
        tot=cc['silent']+cc['jump4']; print(f'   {str(v):>10}: silent {cc["silent"]:4d}  +/-4 {cc["jump4"]:4d}   silent share {cc["silent"]/tot:.2f}')
tab('aco','algebraic concordance order (1 = form has a cut)')
tab('square','double root carried by a squared factor f^2 (vs two different factors)')
tab('g4','topological 4-genus')
ex=[r['name'] for r in rows if r['jump']==0 and r['aco']=='1'][:12]
print('\nexamples silent & algebraically slice:',ex)
ex2=[(r['name'],r['aco']) for r in rows if r['jump']==0 and r['aco']!='1'][:12]
print('silent but NOT algebraically slice:',ex2)
