# SCRIPT: SM-GEN-STEPS-01
# Generation steps z = heavier/lighter, Garrett level L = ln z / ln 5, at three scales.
# Sources: PDG 2024 low-scale values (u,d,s at 2 GeV; c,b at their own mass; t pole; lepton pole masses);
#          M_Z: quarks and lepton running factors from arXiv:0905.1425 Table A.1 / eq. A.4 (m_l(M_Z) = pole / eta_l);
#          GUT 2e16 GeV: quarks from arXiv:1206.5909 Table II (SM, this work column). Leptons at GUT not in hand: left out there.
# H1 (whole Garrett levels): KILL if any quark step's L moves by > 0.25 between scales, or mean distance to nearest integer >= 0.2 at any scale.
# H2 (past the wall z > 3+2sqrt2): KILL if any step is inside the wall at any scale.
import math
L5 = math.log(5); WALL = 3 + 2*math.sqrt(2)
S = {
 'PDG low':  dict(e=0.51099895, mu=105.6583755, tau=1776.93, u=2.16, c=1273, t=172570, d=4.70, s=93.5, b=4183),
 'M_Z':      dict(e=0.51099895/1.046, mu=105.6583755/1.027, tau=1776.93/1.0167, u=1.54, c=599, t=169600, d=3.1, s=57, b=2870),
 'GUT 2e16': dict(u=0.4565, c=222.5, t=70518.8, d=1.0773, s=20.4323, b=932.1),
}
pairs = [('e','mu'),('mu','tau'),('u','c'),('c','t'),('d','s'),('s','b')]
lev = {}
for sc, m in S.items():
    row = []; dist = []
    for a, b in pairs:
        if a in m and b in m:
            z = m[b]/m[a]; L = math.log(z)/L5; lev[(sc,a,b)] = L; dist.append(abs(L - round(L)))
            row.append(f"{a}->{b} z={z:8.2f} L={L:5.3f} {'past' if z > WALL else 'INSIDE'}")
    print(f"{sc:>9}: mean distance to whole level {sum(dist)/len(dist):.3f}  |  " + "  ".join(row))
print()
moves = []
for a, b in pairs[2:]:
    Ls = [lev[(sc,a,b)] for sc in S if (sc,a,b) in lev]; moves.append(max(Ls) - min(Ls))
    print(f"quark step {a}->{b}: levels across scales {[round(x,3) for x in Ls]}  spread {max(Ls)-min(Ls):.3f}")
mean_d = [sum(abs(lev[k]-round(lev[k])) for k in lev if k[0]==sc)/sum(1 for k in lev if k[0]==sc) for sc in S]
h1 = 'KILL FIRED' if (max(moves) > 0.25 or max(mean_d) >= 0.2) else 'survives'
h2 = 'KILL FIRED' if any(math.exp(lev[k]*L5) <= WALL for k in lev) else 'survives'
print(f"\nH1 whole Garrett levels: largest scale shift {max(moves):.3f}, mean distances {[round(x,3) for x in mean_d]} -> {h1}")
print(f"H2 every generation step past the wall at every scale -> {h2}")
