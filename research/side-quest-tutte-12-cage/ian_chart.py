# SCRIPT: IAN-CHART-01  decode Ian Matson's notebook page "end digit totals, gaps, and codes"
# Rule read off the page: list the primes; cut the list at every gap of 2 (twin primes); in each block write each prime
# as (last digit, decade), the gaps between neighbours on top, the sum of the last digits as the block total, and under
# each prime its decade minus the block's first decade (the code). If this rule is right, it must reproduce every block on the page.
import numpy as np
P=[p for p in range(2,400) if all(p%q for q in range(2,int(p**0.5)+1))]
blocks=[[P[0]]]
for a,b in zip(P,P[1:]):
    if b-a==2: blocks.append([b])
    else: blocks[-1].append(b)
page=[5,5,8,10,21,9,22,9,32,10,27,18,30,2,10,20,21,21,9,14,25]
out=[]
for B in blocks:
    tot=sum(p%10 for p in B); gaps=[b-a for a,b in zip(B,B[1:])]; code=[p//10-B[0]//10 for p in B]
    out.append(tot); print(f"{str(B):34s} gaps {str(gaps):16s} total {tot:3d} code {code}")
print("page totals :",page)
print("rule totals :",out[:len(page)], "match:",out[:len(page)]==page)
# Hueckel reading of the 12-cage: eigenvalues are pi-orbital energies E = alpha + beta*lambda (beta<0), one electron per site
import networkx as nx
G=nx.LCF_graph(126,[17,27,-13,-59,-35,35,-11,13,-53,53,-27,21,57,11,-21,-57,59,-17],7)
ev=np.sort(np.linalg.eigvalsh(nx.to_numpy_array(G)))[::-1]   # bonding first (largest lambda = lowest energy for beta<0)
n=126; filled=ev[:n//2]; print("filled pairs reach lambda =",round(filled[-1],6)," next empty lambda =",round(ev[n//2],6),
 " zero-level states:",int(np.sum(abs(ev)<1e-8)),"electrons in the zero level:",n-2*int(np.sum(ev>1e-8)))
print("pi energy per site in units of |beta|:",round(2*np.sum(ev[ev>1e-8])/n,4))
