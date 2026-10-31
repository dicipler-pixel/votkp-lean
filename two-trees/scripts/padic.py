# SCRIPT: CONJ_PADIC_TREE
from itertools import product
K=24
P=5
MOD=P**K
# Hensel: i5 with i5^2=-1, i5 = 2 mod 5
x=2
for _ in range(10):
    x=(x-(x*x+1)*pow(2*x,-1,MOD))%MOD
assert (x*x+1)%MOD==0 and x%5==2
i5=x
def mm(A,B):
    return [[(A[0][0]*B[0][0]+A[0][1]*B[1][0])%MOD,(A[0][0]*B[0][1]+A[0][1]*B[1][1])%MOD],
            [(A[1][0]*B[0][0]+A[1][1]*B[1][0])%MOD,(A[1][0]*B[0][1]+A[1][1]*B[1][1])%MOD]]
def lps(u,s):
    a,b,c,d=1,0,0,0
    if u=='i': b=2*s
    if u=='j': c=2*s
    if u=='k': d=2*s
    return [[(a+b*i5)%MOD,(c+d*i5)%MOD],[(-c+d*i5)%MOD,(a-b*i5)%MOD]]
def boost(u,s):
    I=1;
    sg={'i':[[0,1],[1,0]],'j':[[0,-i5],[i5,0]],'k':[[1,0],[0,-1]]}[u]
    return [[(3*(r==c)+2*s*sg[r][c])%MOD for c in range(2)] for r in range(2)]
def val(n):
    n%=MOD
    if n==0: return K
    v=0
    while n%5==0: n//=5; v+=1
    return v
def canon(g):
    # lattice spanned by columns, up to scalar. returns (n, canonical data)
    m=min(val(g[r][c]) for r in range(2) for c in range(2))
    g=[[ (g[r][c]//P**m) for c in range(2)] for r in range(2)]
    M2=P**(K-m)
    cols=[(g[0][0]%M2,g[1][0]%M2),(g[0][1]%M2,g[1][1]%M2)]
    def v2(n):
        n%=M2
        if n==0: return 99
        v=0
        while n%5==0: n//=5; v+=1
        return v
    cols.sort(key=lambda c:v2(c[1]))
    w1,w2=cols
    # make w2 second coord zero
    if v2(w2[1])<99:
        q=(w2[1]//P**v2(w1[1]))*pow((w1[1]//P**v2(w1[1])),-1,M2)%M2
        w2=((w2[0]-q*w1[0])%M2,0)
    e=v2(w2[0]); q2=v2(w1[1])
    u=pow(w1[1]//P**q2,-1,M2)
    f=(w1[0]*u)%M2
    f%=P**e
    return (e,q2,f)
# generators as dict
def gens(f): return {(u,s):f(u,s) for u in 'ijk' for s in (1,-1)}
def neigh_line(g):
    # image of g mod 5: column space as point of P1(F5)
    a,b,c,d=[g[r][cc]%5 for r in range(2) for cc in range(2)]
    col=(a,c) if (a,c)!=(0,0) else (b,d)
    # normalise
    if col[0]%5!=0:
        inv=pow(col[0],-1,5); return ('1',(col[1]*inv)%5)
    return ('inf',0)
for name,f in (('LPS',lps),('BOOST',boost)):
    G=gens(f)
    lines={k:neigh_line(g) for k,g in G.items()}
    print(name,'det valuations',{k:val((g[0][0]*g[1][1]-g[0][1]*g[1][0])) for k,g in G.items()})
    print(name,'image lines mod 5 (point of P1(F5))',lines)
    print(name,'six lines distinct:',len(set(lines.values()))==6)
    # reduced words up to depth 4
    keys=list(G.keys())
    level={():[[1,0],[0,1]]}
    seen={}
    total=0
    cur=[((),[[1,0],[0,1]])]
    verts={canon([[1,0],[0,1]]):()}
    ok=True
    for depth in range(1,5):
        nxt=[]
        for w,g in cur:
            for k in keys:
                if w and w[-1][0]==k[0] and w[-1][1]==-k[1]: continue
                h=mm(g,G[k]); w2=w+(k,)
                c=canon(h)
                n=val(h[0][0]*h[1][1]-h[0][1]*h[1][0])-2*min(val(h[r][cc]) for r in range(2) for cc in range(2))
                if n!=depth: ok=False
                if c in verts: ok=False
                verts[c]=w2
                nxt.append((w2,h))
        cur=nxt
        print(name,'depth',depth,'words',len(cur),'distinct vertices so far',len(verts),'expected',sum(6*5**(d-1) if d else 1 for d in range(depth+1)))
    print(name,'all reduced words up to depth 4: det-valuation=depth and vertices distinct:',ok)
# eigenvalue ratios in Q_5
# LPS: (1+2 i5)/(1-2 i5);  valuation
a=(1+2*i5)%MOD; b=(1-2*i5)%MOD
print('LPS eigenvalues 1+2i5 valuation',val(a),' 1-2i5 valuation',val(b))
# is ratio 5 or 1/5 ? check a == 5*b or b==5*a mod 5^k
print('LPS ratio == 5 ?',(a-5*b)%MOD==0,'  ratio == 1/5 ?',(b-5*a)%MOD==0)
print('5-adic digits of valuation of (a-5b), (b-5a):',val(a-5*b),val(b-5*a))
# also with lambda scaling: eigenvalue ratio invariant. rho_LPS*5 vs: rho=(-3+4i)/5
rho_num=(-3+4*i5)%MOD
print('v(-3+4 i5)=',val(rho_num),' v(-3-4 i5)=',val((-3-4*i5)))
# tr^2/det equality test 4/5 vs 36/5 in Q_5: difference 32/5, valuation -1 (nonzero)
print('v_5(36/5-4/5) = v(32)-1 =',val(32)-1)
