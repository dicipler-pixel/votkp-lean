# SCRIPT: CONJ_INVARIANTS_EXACT
import sympy as sp
from itertools import product
I=sp.I
M=sp.Matrix
def lps(u,s):
    a,b,c,d=1,0,0,0
    if u=='i': b=2*s
    if u=='j': c=2*s
    if u=='k': d=2*s
    return M([[a+b*I,c+d*I],[-c+d*I,a-b*I]])
sig={'i':M([[0,1],[1,0]]),'j':M([[0,-I],[I,0]]),'k':M([[1,0],[0,-1]])}
def boost(u,s): return 3*sp.eye(2)+2*s*sig[u]
def inv(g): return g.inv()
def ratio(g):
    t=sp.simplify(g.trace()); d=sp.simplify(g.det())
    return sp.nsimplify(sp.simplify(sp.expand(t**2/d)))
gens={}
for name,f in (('LPS',lps),('BOOST',boost)):
    gens[name]={(u,s):f(u,s) for u in 'ijk' for s in (1,-1)}
for name in gens:
    print(name)
    for (u,s),g in gens[name].items():
        print(' gen',u,s,'tr',g.trace(),'det',sp.simplify(g.det()),'tr2/det',ratio(g))
# check inverses are generators up to scalar
for name in gens:
    for (u,s),g in gens[name].items():
        h=gens[name][(u,-s)]
        assert sp.simplify(g*h-5*sp.eye(2))==sp.zeros(2,2), (name,u,s)
print('inverse check ok (g*g^-1 = 5I)')
# length-2 and commutator invariants
keys=list(gens['LPS'].keys())
res={}
for name in gens:
    G=gens[name]
    prod2={}; comm={}
    for a,b in product(keys,keys):
        if a[0]==b[0]: continue
        prod2[(a,b)]=ratio(G[a]*G[b])
        comm[(a,b)]=ratio(G[a]*G[b]*G[(a[0],-a[1])]*G[(b[0],-b[1])])
    res[name]=(prod2,comm)
for name in res:
    p,c=res[name]
    print(name,'products g_u g_v (u!=v) tr2/det distinct values:',sorted(set(p.values()),key=lambda z:(sp.re(z),sp.im(z))))
    print(name,'commutators tr2/det distinct values:',sorted(set(c.values()),key=lambda z:(sp.re(z),sp.im(z))))
    # also tr (not squared) of commutator normalised
# square invariants
for name in gens:
    print(name,'g^2 tr2/det', set(ratio(g*g) for g in gens[name].values()))
# compare sets
for k,lab in ((0,'products'),(1,'commutators')):
    A=set(res['LPS'][k].values()); B=set(res['BOOST'][k].values())
    print(lab,'common values LPS vs BOOST:',A&B)
# explicit example row
print('example i,j product LPS', res['LPS'][0][(('i',1),('j',1))], 'BOOST', res['BOOST'][0][(('i',1),('j',1))])
print('example comm [i,j] LPS', res['LPS'][1][(('i',1),('j',1))], 'BOOST', res['BOOST'][1][(('i',1),('j',1))])
# all-words-of-length<=3 : does any boost invariant equal any LPS invariant for ANY pair of words of same shape?
