# SCRIPT: WALL-NILPOTENT-04
# Makes the headline exact. Claim: at a TOUCH wall (double root, nullity 1) the knot's monodromy h = V^-1 V^T has a
# single Jordan block of size 2 at that root, so (h - lambda) is a NONZERO NILPOTENT on the root space;
# at a split wall (nullity 2) it is zero there (two independent eigenvectors).
# Why this decides it: the Seifert matrix is a third column of KnotInfo, independent of the signature function and of
# the second Alexander polynomial. dim ker(h - lambda) = 1 with dim ker(h - lambda)^2 = 2 is exactly one Jordan block.
# Kill: any double root (with invertible V) where dim ker(h - lambda) differs from the listed nullity.
import numpy as np, sympy as sp, collections
from database_knotinfo import link_list
t=sp.symbols('t'); ok=bad=skip=0; shape=collections.Counter(); ex=[]
for k in link_list()[1:]:
    sf=k['signature_function']
    if not sf or sf=='[0]': continue
    try: ent=eval(sf)
    except Exception: continue
    if not isinstance(ent,list) or not ent or not isinstance(ent[0],list): continue
    fac=sp.factor_list(sp.Poly(sp.sympify(k['alexander_polynomial'].replace('^','**')),t))[1]
    dbl=[e for e in ent if sum(m for f,m in fac if abs(complex(f.as_expr().subs(t,complex(sp.exp(sp.pi*sp.I*e[0]).evalf())).evalf()))<1e-8)==2]
    if not dbl: continue
    try: V=np.array(eval(k['seifert_matrix']),float)
    except Exception: skip+=len(dbl); continue
    if abs(np.linalg.det(V))<1e-9: skip+=len(dbl); continue
    h=np.linalg.solve(V,V.T)
    for e in dbl:
        lam=np.exp(1j*np.pi*e[0]); A=h-lam*np.eye(len(V))
        s1=np.linalg.svd(A,compute_uv=False); s2=np.linalg.svd(A@A,compute_uv=False)
        k1=int((s1<1e-6).sum()); k2=int((s2<1e-6).sum())
        if k1==0 and k2==0:      # root may sit at the conjugate convention
            A=h-np.conj(lam)*np.eye(len(V)); s1=np.linalg.svd(A,compute_uv=False); s2=np.linalg.svd(A@A,compute_uv=False); k1=int((s1<1e-6).sum()); k2=int((s2<1e-6).sum())
        shape[(e[2],k1,k2)]+=1
        if k1==e[2]: ok+=1
        else: bad+=1
        if e[2]==1 and len(ex)<3: ex.append((k['name'],round(e[0],4),k1,k2))
print('double roots checked:',ok+bad,' skipped (Seifert matrix singular or missing):',skip)
for key,v in sorted(shape.items()): print('   listed nullity %d : dim ker(h-lam) = %d, dim ker(h-lam)^2 = %d   -> %d'%(key[0],key[1],key[2],v))
print('agree:',ok,' disagree:',bad,' examples of touch walls:',ex)
