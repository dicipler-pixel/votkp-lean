# SCRIPT: SNELL-SMITH-TREES-04
# Three exact checks behind the Snell / Smith / two-trees reading of the gap.
# (1) Strong coupling: the lowest gauge-invariant electric level on a graph is (4/3) x girth (shortest closed loop),
#     because every nontrivial support has minimum degree 2 (no dangling link) and so contains a cycle, and each
#     nontrivial link costs at least 4/3. Check against the room's graphs (two squares 16/3; cube, double cube 16/3).
# (2) Small field on the 1 x n strip: plaquette modes obey a(n+1) + a(n-1) = (4 - mu) a(n). Transfer trace 4 - mu.
#     |trace| > 2 (evanescent, the Snell 'in between') exactly for mu < 2 or mu > 6; the band is [2, 6].
#     For the 2D torus the band reaches mu = 0, so nothing is left in between.
# (3) Smith coordinate of one evanescent step: z = e^kappa with 2 cosh kappa = 4 - mu; Gamma = (z-1)/(z+1).
import numpy as np, itertools, sys
sys.path[:0]=sys.argv[1:]
import spatial_gauge as sg
def girth(edges):
    import collections
    V=sorted({x for e in edges for x in e}); adj=collections.defaultdict(list)
    for i,(a,b) in enumerate(edges): adj[a].append((b,i)); adj[b].append((a,i))
    best=10**9
    for s in V:
        dist={s:0}; par={s:-1}; q=[s]
        for x in q:
            for y,i in adj[x]:
                if i==par[x]: continue
                if y in dist: best=min(best,dist[x]+dist[y]+1)
                else: dist[y]=dist[x]+1; par[y]=i; q.append(y)
    return best
print("graph        girth  (4/3)*girth")
for n in ('two','strip','corner','cube','double_cube'):
    g=girth(sg.model(n)['edges']); print(f"{n:12s} {g:5d}  {4*g/3:.4f}")
print("\nstrip transfer: mu, trace 4-mu, evanescent?, kappa, z, Gamma, Gamma^2")
for mu in (0,0.5,1,1.5,2,3,4,6,7):
    tr=4-mu; ev=abs(tr)>2
    if ev:
        k=np.arccosh(abs(tr)/2); z=np.exp(k); G=(z-1)/(z+1)
        print(f"{mu:4.1f} {tr:6.2f}  yes  kappa={k:.6f} z={z:.6f} Gamma={G:.6f} Gamma^2={G*G:.6f}")
    else: print(f"{mu:4.1f} {tr:6.2f}  no (propagating, |trace|<=2)")
