# SCRIPT: BALLS-MIXER-MIX-CHECK-01
# Why: the mixer text says the smallest distance between centres keeps falling for the 14-arm set (axes 1, diagonals 1.125).
# This prints count and smallest distance per generation so the wording matches what actually happens.
import itertools, math
ax=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
dg=[tuple(1.125*s/math.sqrt(3) for s in t) for t in itertools.product((1,-1),repeat=3)]
V=ax+dg; seen={(0,0,0):(0,0,0)}; front=[(0,0,0)]
for g in range(1,6):
    nx=[]
    for p in front:
        for v in V:
            q=tuple(p[i]+v[i] for i in range(3)); k=tuple(round(c*1e5) for c in q)
            if k not in seen: seen[k]=q; nx.append(q)
    front=nx; pts=list(seen.values())
    # min separation via grid
    cell=0.35; grid={}
    for p in pts: grid.setdefault(tuple(int(math.floor(c/cell)) for c in p),[]).append(p)
    m=9
    for c,L in grid.items():
        for d in itertools.product((-1,0,1),repeat=3):
            for b in grid.get(tuple(c[i]+d[i] for i in range(3)),[]):
                for a in L:
                    if a is not b:
                        m=min(m,math.dist(a,b))
    print(g,len(pts),round(m,5))
