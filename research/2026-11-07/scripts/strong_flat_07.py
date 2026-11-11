# SCRIPT: STRONG-FLAT-07
# Record of the parity-model test (Neumann Prop 5.3 analogue). In each ordered reading (branching) of each knot's snappy triangulation, test which per-tetra
# parity pattern of the three ordered slots satisfies the mod-2 normal-path system of flat_lib_01.parity_system (all closed face-to-face walks pay 0):
# the patterns with exactly one odd slot, and all three odd. Neumann: l(x;0,0) (odd only in its third parameter) has zero parity along every normal path.
# Also: how many edge classes have an odd number of corners in each ordered slot (the parity around an edge).
import sys; sys.path.insert(0,'/home/claude/votkp_research')
from flat_lib_01 import *
import re, database_knotinfo as d
names=[r['name'] for r in d.link_list() if re.match(r'^\d+_\d+$',r['name'] or '') and 4<=int(r['name'].split('_')[0])<=9]
pats=[(1,0,0),(0,1,0),(0,0,1),(1,1,1)]; good={p:0 for p in pats}; tot=0; oddcls=[0,0,0]; ncls=0
for nm in names:
    M=snappy.Manifold(nm)
    if M.solution_type()!='all tetrahedra positively oriented': continue
    n=M.num_tetrahedra(); pc=parity_constraints(M)[0]; cl,nb,pm=edge_classes(M)
    Pm=np.array([[(x>>v)&1 for v in range(2*n)] for x,r in pc],int).reshape(len(pc),2*n); pb=np.array([r for x,r in pc])
    for orders in find_branching(M,maxsol=6):
        tot+=1
        for pat in pats:
            dold=np.zeros(2*n,int)
            for t in range(n):
                o=orders[t]; jk=[pair_of(o[0],o[1]),pair_of(o[0],o[2]),pair_of(o[0],o[3])]; po=[0,0,0]
                for k in range(3): po[jk[k]]=pat[k]
                dold[t]=po[0]; dold[n+t]=po[1]
            if np.all(((Pm@dold)%2)==pb): good[pat]+=1
        cnt={}
        for t in range(n):
            o=orders[t]; pos={v:i for i,v in enumerate(o)}
            for i in range(4):
                for j in range(i+1,4):
                    ni,nj=sorted((pos[i],pos[j])); cnt.setdefault(cl[(t,(i,j))],[0,0,0])[pair_of(ni,nj)]+=1
        for c,v in cnt.items():
            ncls+=1
            for k in range(3): oddcls[k]+=v[k]%2
print('runs (knot, branching):',tot)
print('parity pattern in ordered slots (slot0,slot1,slot2) satisfying the path system:',good)
print('edge classes: %d ; with an odd number of corners in ordered slot 0/1/2: %s'%(ncls,oddcls))
