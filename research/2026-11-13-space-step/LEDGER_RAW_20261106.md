# Raw results ledger, 6 Nov 2026 (numbers only; each test's pass/kill line is in its PREREG_*.md file)

Data: optical n,k from refractiveindex.info (41 elements with full visible coverage; 60 further absorbing materials);
current-data sheets /home/claude/research/current_data/A_41.csv, B_40.csv, C_edges.csv (sources and years per value).
E = 1 - (r_cov/r_room)^3, r_room = (3V/4pi)^(1/3), V = M/(rho N_A), r_cov = Pyykko 2009 covalent radius.
E2 = 1 - (4pi/3) alpha / V (Herzfeld form, alpha = static dipole polarizability). Gamma = (1-N)/(1+N). arg N = phase of N.

1. SHEET-AREA-01: signed hyperbolic area of each element's Smith track (violet->red, closed by geodesic). Controls passed.
   Best single-threshold split of metals vs B,C,Si,Ge,Se,Te: 35-36/41, shuffle p 0.28-1.0. Partial Spearman(area, key strength | chroma) = -0.394, p 0.0115.
   Spearman(area, Gamma1 of peel ladder) = -0.416, p 0.007; with lnIE1 +0.370, p 0.018. 39/41 areas negative (clockwise).
   |area| order of coinage metals: Ag 24.5 > Au 8.9 > Cu 6.5.
2. QWALL-01: q = (ln|N|)^2 - (arg N)^2, visible mean. Fixed wall q<0 = metal: 25/41 wrong. Elements with q<0: K Rb Na Cs Li Ca Ag Au Bi Cu.
   Best threshold on arg N alone: 41/41 at 0.661 rad (fitted), shuffle p 0.001; nearest: W 0.66 (metal), Te 0.62 (non-metal). ln|N| alone: 35/41.
3. TURNBOOK-OOS-01/02: Spearman(arg N, log10 DC conductivity) +0.544 (n 40, p 0.0005); metals only +0.320.
   Frozen arg-N line vs Herzfeld R/V>=1: 6 disagreements (B Bi Ge Hg Pb Si). ln|N| vs conductivity +0.196; red-end arg N +0.521.
4. SPACE-BETWEEN-01 (35 metals): Spearman(E, log10 DC conductivity) +0.072 (p 0.69); Spearman(E, arg N) +0.783 (p 0.0005); E2 vs arg N +0.515.
   Every metal E <= 0.604 (Na highest); every non-metal E >= 0.665 (B lowest).
5. SPACE-LINES-02 (40 further elements, old packaged data): E<0.63: 3 wrong (P As Po); E<2/3: 1 wrong (P, label later found wrong); Herzfeld: 4 wrong (P As Sb Po).
6. RERUN-CURRENT-02 (81 rows, current data): E<0.63: 2 wrong (As, Po); E<2/3: 1 wrong (B, E=0.665); Herzfeld: 9 wrong (B Si Ge Hg Pb Bi Sb As Po).
   Staircase band: Sb 0.619, As 0.658, Po 0.662, Sn-grey 0.664, B 0.665, Ge 0.672, Si 0.673, C-diamond 0.689, Te 0.690, P-red 0.759, Se 0.760.
7. Crossing cases (densities g/cm3; measured from C_edges.csv):
   case          | 2/3-line predicts | Herzfeld predicts | measured switch
   Hg expanding  | 11.27 | 15.83 | between 10.7 (metal) and 8.3 (non-metal)
   Si melting    | 2.38  | 2.01  | solid 2.311 non-metal, liquid 2.580 metal
   Ge melting    | 5.42  | 4.86  | solid 5.32 non-metal, liquid 5.585 metal
   I squeezed    | 7.13  | 10.32 | metal about 7.7-8.1 (14-24 GPa)
   H fluid       | 4.07  | 0.60  | metal 0.60-0.64
   Xe squeezed   | 7.72  | 12.86 | metal about 12.3-12.8 (about 130 GPa)
   Cs, Rb, K expanding | 1.41, 1.22, 0.69 | 0.89, 0.72, 0.36 | still metal near critical densities 0.38, 0.29, 0.18
   He: E 0.991 liquid, 0.988 solid (never conducts). Sn white 0.574 metal, grey 0.664 (semimetal/0.08 eV gap source conflict).
8. P4 handedness, 60 absorbing materials not used before: 56 clockwise, 3 counter-clockwise (As2Se3 +0.346, TiC +0.0034, VC +0.0006), 1 flat.
9. P3 on current data: Spearman(E, arg N) in 35 metals = +0.785, p 0.0005. Largest rank breakers: Pb -19, Ag +15, Ta +14, Hg -11, Be -9, Rh +9, Zn -8, Al +8, Ca +7, Bi -6.
10. OUTLIERS-ALL-01: outlier = wrong side or right side by < 0.1 of the test's spread. Outlier rate by family (pooled):
   Zn-Cd-Hg 0.44 (n16), p non/metalloid 0.34 (38), p metal 0.32 (34), s2 0.22 (27), open d 0.21 (131), s1 0.17 (35), coinage 0.10 (21), f/La-Lu 0.02 (47).
   Family-label shuffle p = 0.003. Per-test outlier lists are printed by scripts/OUTLIERS_ALL_01.py.
11. RELATIVITY-01: Delta_s = 1 - r_rel/r_nonrel of outer s orbital (ROHF, uncontracted ANO-RCC, sfX2C vs nonrel). Na 0.0012, Au 0.169.
   Hg 0.143, Tl 0.128, Pb 0.120, Bi 0.114, Po 0.111, Ra 0.093, Ag 0.054, In 0.041, Sn 0.039, Sb 0.038, Te 0.037, I 0.037, Cs 0.034, Ba 0.032, Pd 0.029, Zr 0.023, Cu 0.020, Zn 0.016, light elements < 0.005.
   R1 Spearman(Delta_s, Herzfeld margin), Z>=37: -0.616 p 0.0075 n 19. R2 (metals, rank residual): -0.466 p 0.026 n 23. R3 (pooled outlier rate): +0.087 p 0.58 n 43.
   Opposite Delta_d: R1 -0.446 p 0.052; R2 -0.263; R3 +0.211. Spearman(Delta_s, Z) 0.753; partial (Delta_s, margin | Z) -0.481.
   Not converged (excluded): Ir Pt Os Re W Ta Hf Lu La Rh Tc Ru Nb Mo Y Ni Fe Mn Cd.
12. Literature numbers gathered: Bruggeman symmetric EMA threshold conductor fill 1/3 (mean field); random sphere percolation about 0.16-0.29.
   Diamond-cubic packing fraction 0.340. Lindemann melting ratio about 0.07-0.11. Metallization pressures (Wikipedia table, unreferenced): Te 4, black P 4.8, Ge 11, Si 12, I 16, Se 23, Br 25, S 83, O 96, Xe 130, B 160, Cl 200 GPa.
