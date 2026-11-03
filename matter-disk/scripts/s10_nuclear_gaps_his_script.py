# SCRIPT: SNELL2-MASS-GAPS-ON-THE-SMITH-CHART  (exact placement; exploration)
# NUBASE2020 (via pynucastro) mass excesses. The peel ratio of Theorem 8.1, z = S(next)/S(first),
# with S a separation energy. Every bound peel has z > 0 and sits inside the disk; a negative
# separation energy gives z < 0 and |Gamma| > 1: the point leaves the disk.
import os, numpy as np, pynucastro.nucdata as nd
F = os.path.dirname(nd.__file__) + '/AtomicMassEvaluation/nubase_4.mas20.txt'
ME = {}; HL = {}
for line in open(F):
    if not line[:3].strip().isdigit(): continue
    A = int(line[0:3]); zc = line[4:8]
    if zc[3] != '0': continue
    Z = int(zc[:3]); s = line[18:31].strip()
    if not s or s.startswith('*'): continue
    ME[(A, Z)] = float(s.replace('#', '')); HL[(A, Z)] = line[69:80].strip()
n, p = 8071.31806, 7288.97061           # keV, neutron and 1H mass excesses
Sn = lambda A, Z: ME[(A - 1, Z)] + n - ME[(A, Z)]
Sp = lambda A, Z: ME[(A - 1, Z - 1)] + p - ME[(A, Z)]
Sa = lambda A, Z: ME[(A - 4, Z - 2)] + ME[(4, 2)] - ME[(A, Z)]
G = lambda z: (z - 1) / (z + 1)
cases = [('5He: remove n, then n from 4He', Sn(5, 2), Sn(4, 2), HL[(5, 2)]),
         ('5Li: remove p, then p from 4He', Sp(5, 3), Sp(4, 2), HL[(5, 3)]),
         ('8Be: remove alpha (12C ladder: 12C -> 8Be -> 4He)', Sa(8, 4), Sa(12, 6), HL[(8, 4)]),
         ('7Li (bound, for contrast): remove n, then n from 6Li', Sn(7, 3), Sn(6, 3), HL[(7, 3)]),
         ('4He (bound): remove n, then p from 3He', Sn(4, 2), Sp(3, 2), HL[(4, 2)])]
print(f'{"case":52s} {"S first (keV)":>14s} {"S next (keV)":>13s} {"|Gamma|":>8s}  half-life (NUBASE)')
for lab, s1, s2, hl in cases:
    if lab.startswith('8Be'): z = s1 / s2      # 12C ladder: first step 12C->8Be costs s2, next step 8Be->2 alpha costs s1
    else: z = s2 / s1
    print(f'{lab:52s} {s1:14.1f} {s2:13.1f} {abs(G(z)):8.3f}  {hl}')
