# SCRIPT: FLAT-LIB-01 (shared helpers: gluing data, edge-pair types, alternating-walk parity system, integer solve)
import numpy as np, snappy, warnings, itertools
from cypari import pari
from mpmath import polylog, mpc
warnings.filterwarnings('ignore')
PAIRS=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
def pair_of(i,j):
    s=frozenset((i,j))
    for k,(e1,e2) in enumerate(PAIRS):
        if s==frozenset(e1) or s==frozenset(e2): return k
def edge_classes(M):
    """union-find on (tet, edge) using gluing data; returns dict (t,(i,j))->class"""
    nb,pm=zip(*M._get_tetrahedra_gluing_data()); n=len(nb)
    par={}
    def f(x):
        while par.setdefault(x,x)!=x:
            par[x]=par[par[x]]; x=par[x]
        return x
    for t in range(n):
        for i in range(4):
            for j in range(i+1,4):
                par.setdefault((t,(i,j)),(t,(i,j)))
    for t in range(n):
        for face in range(4):
            t2=nb[t][face]; p=pm[t][face]
            for i in range(4):
                for j in range(i+1,4):
                    if face in (i,j): continue
                    a,b=sorted((p[i],p[j]))
                    par[f((t,(i,j)))]=f((t2,(a,b)))
    roots={}
    out={}
    for k in list(par):
        r=f(k); out[k]=roots.setdefault(r,len(roots))
    return out,nb,pm
def edge_matrix(M,perm):
    """edge-class x (3n) incidence with pair->slot assignment perm (perm[k]=slot of PAIRS[k])"""
    cl,nb,pm=edge_classes(M); n=len(nb); ne=max(cl.values())+1
    A=np.zeros((ne,3*n),int)
    for (t,(i,j)),c in cl.items(): A[c,3*t+perm[pair_of(i,j)]]+=1
    return A
def check_convention(M):
    E=np.array(M.gluing_equations().list(),int).reshape(-1,3*len(M.tetrahedra_shapes('rect')))
    n=E.shape[1]//3; res=[]
    for perm in itertools.permutations(range(3)):
        A=edge_matrix(M,perm)
        rowsE={tuple(r) for r in E[:A.shape[0]]}; rowsA={tuple(r) for r in A}
        if rowsE==rowsA: res.append(perm)
    return res
def parity_system(M,cost='pair'):
    """Mod-2 system for 'parity along every closed normal path is zero' (Neumann 2004 Def 4.3/4.4).
    Model: a normal path inside tetra t enters through face fin and leaves through face fout, passing the edge pair of
    {fin,fout} (= the pair of the edge fin∩fout); it pays delta(slot), delta slot0=p,slot1=q,slot2=r=1+p+q (mod 2).
    It then crosses into the glued tetra. A potential phi on half-faces (t,face) exists iff every closed directed walk pays 0
    (restricted to strongly connected components). Variables: p_j (0..n-1), q_j (n..2n-1), phi (2n..2n+4n-1).
    Returns (rows, nvars): rows = list of (set of var indices, rhs) meaning XOR of vars = rhs."""
    nb,pm=zip(*M._get_tetrahedra_gluing_data()); n=len(nb)
    V=[(t,f) for t in range(n) for f in range(4)]; idx={v:i for i,v in enumerate(V)}
    moves=[]
    for (t,fi) in V:
        for fo in range(4):
            if fo==fi: continue
            e=[v for v in range(4) if v not in (fi,fo)]
            k=pair_of(*e) if cost=='pair' else pair_of(fi,fo)
            t2=nb[t][fo]; f2=pm[t][fo][fo]
            moves.append((idx[(t,fi)],idx[(t2,f2)],t,k))
    adj=[[] for _ in V]
    for a,b,t,k in moves: adj[a].append(b)
    import sys; sys.setrecursionlimit(100000)
    index=[None]*len(V); low=[0]*len(V); on=[False]*len(V); st=[]; comp=[None]*len(V); c=[0,0]
    def sc(v):
        index[v]=low[v]=c[0]; c[0]+=1; st.append(v); on[v]=True
        for w in adj[v]:
            if index[w] is None: sc(w); low[v]=min(low[v],low[w])
            elif on[w]: low[v]=min(low[v],index[w])
        if low[v]==index[v]:
            while True:
                w=st.pop(); on[w]=False; comp[w]=c[1]
                if w==v: break
            c[1]+=1
    for v in range(len(V)):
        if index[v] is None: sc(v)
    rows=[]
    for a,b,t,k in moves:
        if comp[a]!=comp[b]: continue
        s=set(); rhs=0
        for v in (2*n+a,2*n+b): s^={v}
        if k==0: s^={t}
        elif k==1: s^={n+t}
        else: s^={t}; s^={n+t}; rhs^=1
        rows.append((s,rhs))
    return rows,6*n,c[1]
def solve_mod(A,mods,b):
    """integer solution x of A x = b mod mods (mods[i]=0: exact). returns list or None"""
    Mt=pari('['+';'.join(','.join(str(int(x)) for x in r) for r in A)+']')
    D=pari('['+','.join(str(int(x)) for x in mods)+']~'); B=pari('['+','.join(str(int(x)) for x in b)+']~')
    s=pari.matsolvemod(Mt,D,B)
    return None if s==0 else [int(s[i]) for i in range(len(A[0]))]
def parity_constraints(M):
    """eliminate phi from parity_system: returns (cons, consistent) with cons = list of (bitmask over p(0..n-1),q(n..2n-1), rhs)."""
    rows,nv,_=parity_system(M); n=nv//6
    ints=[]
    for s,r in rows:
        x=0
        for v in s: x|=1<<v
        ints.append((x,r))
    # eliminate phi columns (bits >= 2n) first
    piv_used=[]; rest=ints[:]
    for col in range(2*n,nv):
        pi=None
        for i,(x,r) in enumerate(rest):
            if (x>>col)&1: pi=i; break
        if pi is None: continue
        px,pr=rest.pop(pi)
        rest=[((x^px,r^pr) if (x>>col)&1 else (x,r)) for x,r in rest]
    # remaining rows involve only p,q ; reduce
    cons=[]; 
    for x,r in rest:
        for cx,cr in cons:
            if x&(cx&-cx): x^=cx; r^=cr
        if x==0:
            if r: return None
        else: cons.append((x,r))
    return [(x,r) for x,r in cons],True
def find_branching(M,maxsol=50):
    """ordering of vertices in every tetra so that all face gluings are order-preserving (a branching).
    returns list of solutions; each solution = list over tetra of tuple order (old labels listed from lowest to highest) or None."""
    nb,pm=zip(*M._get_tetrahedra_gluing_data()); n=len(nb)
    keys=[(t,(i,j)) for t in range(n) for i in range(4) for j in range(i+1,4)]
    par={k:(k,0) for k in keys}          # union-find with parity: par[k]=(parent, flip relative to parent)
    def find(k):
        p,f=par[k]
        if p==k: return k,0
        r,g=find(p); par[k]=(r,f^g); return r,f^g
    for t in range(n):
        for face in range(4):
            t2=nb[t][face]; g=pm[t][face]
            for i in range(4):
                for j in range(i+1,4):
                    if face in (i,j): continue
                    a,b=g[i],g[j]; flip=0
                    if a>b: a,b=b,a; flip=1
                    k1,f1=find((t,(i,j))); k2,f2=find((t2,(a,b)))
                    if k1==k2:
                        if f1^f2^flip: return []          # edge glued to itself reversed: no branching
                    else: par[k1]=(k2,f1^f2^flip)
    cls={}; off={}
    for k in keys:
        r,f=find(k); cls.setdefault(r,len(cls)); off[k]=(cls[r],f)
    nc=len(cls); sols=[]
    for mask in range(1<<nc):
        ok=True; orders=[]
        for t in range(n):
            score=[0]*4
            for i in range(4):
                for j in range(i+1,4):
                    c,f=off[(t,(i,j))]; d=((mask>>c)&1)^f      # d=0: i->j ; d=1: j->i
                    score[i if d==0 else j]+=0                  # placeholder
                    if d==0: score[j]+=1                        # score = number of edges pointing INTO the vertex
                    else: score[i]+=1
            if sorted(score)!=[0,1,2,3]: ok=False; break
            orders.append(tuple(sorted(range(4),key=lambda v:score[v])))   # lowest = source (0 incoming)
        if ok:
            sols.append(orders)
            if len(sols)>=maxsol: break
    return sols
def perm_sign(p):
    s=1; p=list(p)
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            if p[i]>p[j]: s=-s
    return s
