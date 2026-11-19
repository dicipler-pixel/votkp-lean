# SCRIPT: TUTTE-12CAGE-01  Ian Matson's take: Tutte 12-cage (chromatic index 3, chromatic number 2, diameter 6)
# Check first that the LCF really builds the unique (3,12)-cage: if 126 vertices, cubic, bipartite, girth 12, diameter 6
# all hold, it is that graph (the cage is unique). Then read its shells, its intersection array and its "sound" (spectrum).
import networkx as nx, numpy as np
from collections import Counter
lcf=[17,27,-13,-59,-35,35,-11,13,-53,53,-27,21,57,11,-21,-57,59,-17]
G=nx.LCF_graph(126,lcf,7)
print("vertices",G.number_of_nodes(),"edges",G.number_of_edges(),"degrees",set(d for _,d in G.degree()),
      "bipartite",nx.is_bipartite(G),"girth",nx.girth(G),"diameter",nx.diameter(G),"radius",nx.radius(G))
# chromatic index 3: a proper 3-edge-colouring exists iff a perfect matching decomposition; check via bipartite König: cubic bipartite => class 1
print("cubic bipartite => chromatic index 3 by Konig's edge-colouring theorem")
# shells from every vertex
sh=set()
for v in G:
    d=nx.single_source_shortest_path_length(G,v); sh.add(tuple(Counter(d.values())[i] for i in range(7)))
print("shell sizes from any vertex (distance 0..6):",sh)
# intersection array b_i, c_i, a_i
v=0; d=nx.single_source_shortest_path_length(G,v)
rows=[]
for i in range(7):
    L=[u for u in G if d[u]==i]
    bs={sum(1 for w in G[u] if d[w]==i+1) for u in L}; cs={sum(1 for w in G[u] if d[w]==i-1) for u in L}; as_={sum(1 for w in G[u] if d[w]==i) for u in L}
    rows.append((i,len(L),cs,as_,bs))
print(" i  size  c_i  a_i  b_i   (c = edges back toward start, b = edges outward)")
for r in rows: print(f" {r[0]}  {r[1]:4d}  {r[2]}  {r[3]}  {r[4]}")
A=nx.to_numpy_array(G); ev=np.linalg.eigvalsh(A)
c=Counter(np.round(ev,8)); print("spectrum (eigenvalue: multiplicity):",{float(k):v for k,v in sorted(c.items())})
print("distinct eigenvalues:",len(c),"= diameter+1 =",nx.diameter(G)+1)
print("as surds: 3, sqrt6 =",round(np.sqrt(6),8),", sqrt2 =",round(np.sqrt(2),8),", 0")
print("Hamiltonian cycle given by LCF (the 126-cycle 0..125 is in the graph):",all(G.has_edge(i,(i+1)%126) for i in range(126)))
print()
for name,H in [("Tutte graph (46)",nx.tutte_graph()),("Tutte-Coxeter / Tutte 8-cage",nx.LCF_graph(30,[-13,-9,7,-7,9,13],5))]:
    print(name,"n",H.number_of_nodes(),"bipartite",nx.is_bipartite(H),"girth",nx.girth(H),"diameter",nx.diameter(H))
