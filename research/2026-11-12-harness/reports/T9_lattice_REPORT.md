# T9_lattice: can lattice type and spacing be read from the peel steps? (probing pass, 2026-11-12)

## Results first (registered lines, kill lines written in STATE.md before computing)
Population: 84 elements with a solid reference state in ASE; 65 have one of the five structures with a formula (bcc 14, fcc 20, hcp 27, diamond 3, sc 1), 56 of those are metals for R2. Ladders: NIST via the v2.9 package CSV; the installed mendeleev gives 0 disagreements above 0.5% (same NIST source, so this check is not independent).

- R1 (past the wall means bcc): MET. Past-wall elements are Li, Na, K, Rb, Cs, and all 5 are bcc (100%, kill line 80%). Inside the wall: 9 of 60 are bcc (15%). Fisher exact p = 2.4e-4. 5,000 label shuffles: p = 0.0006. The past-wall set is exactly the five alkali metals, so n = 5.
- R2 (shape carries dimensionless spacing): numbers met, flagged as artefact by my own pre-written control. Spearman(ln s, L1) = -0.543 (n = 56 metals, shuffle p < 0.0002; kill line |rho| < 0.5 not hit). But ln s and L1 share ln IE1 with opposite signs, and the registered controls do not agree: Spearman(ln d_nn, L1) = -0.196 (p = 0.15) and Spearman(ln s, ln IE2) = -0.128 (p = 0.35), both under the 0.3 floor. So per the rule written beforehand, the pass does not count. Comparison, absolute spacing against absolute level: Spearman(d_nn, IE1) = -0.789 (p = 5e-13). Level carries absolute spacing strongly, as B102 says; the ratio's share of dimensionless spacing is not separated from the shared IE1 term.
- R3 (locked step): n = 5 (the alkalis), rho(|G1 - G*|, ln s) = -0.90, p = 0.037. With n < 6 this is meaningless. G1 runs Li 0.8669, Na 0.8039, K 0.7586, Rb 0.7345, Cs 0.7121, and ln s runs 0.817, 0.961, 1.005, 1.033, 1.042, both ordered by period. G* = 0.72486 falls between Rb and Cs.
- R4 (opposite of R1): MET. Share past the wall among 8-coordinated: 5 of 14 = 35.7%. Among 12-coordinated (fcc, hcp): 0 of 47 = 0%. Fisher p = 3.4e-4. This is R1 read the other way and carries the same five elements.

## What it means in plain terms
The first step cleanly picks out one family: elements whose first ionization step is past the wall are the alkalis, and the alkalis are bcc. That is a real separation, but it rests on five elements that also share an outer-electron structure, and 9 other bcc elements sit inside the wall.

## Seen, not registered (descriptive; nothing here is a test)
1. Where the hypothesis plainly fails (bcc inside the wall, G1^2 0.099-0.175, same range as hcp and fcc): V, Cr, Fe, Nb, Mo, Ta, W, Ba, Eu. Ba and Eu have G1^2 0.099 and 0.108, as low as the hcp and fcc medians (0.106 and 0.111). The first step does not distinguish bcc from 12-coordination once the alkalis are removed: AUC of z1 for bcc against 12-coordinated is 0.774 with the alkalis and 0.648 without; z_core 0.710 and 0.556; ln s 0.237 and 0.291 (below 0.5 means bcc has the smaller s). Conversely the 12-coordinated elements with the highest first-step G1^2 are Tl 0.291, Al 0.268, Ag 0.229, Cu 0.201, Lu 0.198, all far from the wall.
2. Families. Alkali: 5 bcc, all past the wall (G1^2 0.507 to 0.752). Cs is barely past (z1 = 5.947 against the wall 5.828). Alkaline earth: G1^2 0.099-0.106 for all five (Be hcp, Mg hcp, Ca fcc, Sr fcc, Ba bcc), one bcc. Transition metals: G1^2 0.093 to 0.229, bcc 7, hcp 13, fcc 8, and the bcc ones are the groups 5 and 6 plus Fe. p-block with a formula: C, Si, Ge diamond, Al fcc, Pb fcc, Tl hcp, all inside the wall. Noble-gas solids (Ne, Ar, Kr, Xe, fcc) sit at G1^2 0.071-0.096 with ln s 2.0 to 2.24, far above every metal (~0.8 to 1.3).
3. Spacing is tight within a structure once the oddities are removed: bcc without alkalis ln s = 1.024 +/- 0.106 (n 9); bcc with alkalis 1.005 +/- 0.101 (n 14); fcc without the noble gases 1.128 +/- 0.126 (n 16, with them 1.322 +/- 0.416); hcp 1.118 +/- 0.154 (n 27). So d_nn is roughly 2.8 times r1 in bcc and 3.1 times r1 in fcc/hcp metals. Whether the gap between bcc and fcc/hcp averages is real was not tested.
4. Other peel quantities: the core-opening step is the first step for all five alkalis (k = 1), and k_core is the filled-shell index elsewhere. Median G_core is 0.625 for bcc, 0.611 fcc, 0.607 hcp, 0.646 diamond, 0.598 sc: no separation of structures. The second step z2 gives AUC 0.392 (not above chance in the useful direction).
5. Allotropes. The table holds ASE's single reference state, and his picture says it changes with temperature. As held: C diamond (graphite is the room-temperature stable form), Sn bct (white tin; grey tin is diamond), Fe bcc (fcc above 1185 K), Co hcp, Mn cubic (no CN assigned), Se and Te hcp (ASE's label for trigonal chains), Ca, Sr fcc, Ba, Eu bcc, Yb fcc, Ce fcc, Tl hcp, Po sc, Hg rhombohedral. No allotrope runs were done. 19 elements (B, P, S, Cl, Mn, Ga, As, Br, In, Sn, Sb, I, Sm, Hg, Bi, Pa, U, Np, Pu) have structures with no CN formula in the task and are in the table with empty CN, d_nn.
6. Data notes: mendeleev 1.3.0 lattice fields give the same structure and a as ASE except In (3.246 against 4.59, different axis convention) and I (7.27 against 7.72); Pu has no lattice constant in either. mendeleev has no c/a; ASE c/a was used for hcp (ideal sqrt(8/3) if absent). ASE does not reference-state He, H, N, O, F (atom or diatom), so these are not in the table. Packages: ase 3.29.0, mendeleev 1.3.0. These are other people's published measurements (ASE cites Ashcroft and Mermin; ionization energies are NIST ASD).

## Suggested sharper registered lines for a later pass (not run)
1. Within bcc and 12-coordinated metals excluding the alkalis (n = 9 and 47): does any peel quantity (z1, a loop-pass quantity, the first step of the d-block) separate them at AUC >= 0.75? Today z1 gives 0.648.
2. Remove the shared ln IE1 term: regress ln d_nn on ln IE1 first, then test whether the residual correlates with L1 within structure type (R2 repaired). Today ln d_nn against L1 is -0.196.
3. Temperature line: for the elements with a high-temperature allotrope (Fe, Ca, Sr, Ba, Ti, Zr, Tl, Sn), does the allotrope assigned by his temperature picture change the side of the wall of any step? Needs a transition-temperature table, not on disk.

## Untested
Heat, temperature, time, conductivity (his deciding factors): none of these were used. Angles from the tree: not tested. Allotrope-dependent tables: untested. The step ratio at finite ionization stages beyond the first and core step (z3 ... ): not scanned. Group-by-group peel versus structure beyond the five registered lines: untested.

## Files
/home/claude/harness/workers/T9_lattice/: lattice_table.csv (full merged table; source columns: structure_src, a_src, d_nn_src, IE1_src, with mendeleev cross-check columns mend_structure, mend_a, IE1_mend), s1_table.py, s2_registered.py, s2_out.txt, s3_seen.py, s3_out.txt, s3b_seen.py, s3b_out.txt, STATE.md, REPORT.md.

## Table (key columns, CSV)
Z,sym,structure,CN,a,d_nn,IE1,IE2,z1,G1,G1sq,side1,k_core,z_core,G_core,r1,s,ln_s
3,Li,bcc,8.0,3.49,3.0224,5.3917,75.6401,14.0289,0.8669,0.7516,past,1,14.0289,0.8669,1.3353,2.2634,0.8169
4,Be,hcp,12.0,2.29,2.2287,9.3227,18.2112,1.9534,0.3228,0.1042,inside,2,8.4507,0.7884,0.7723,2.8859,1.0598
5,B,tetragonal,,8.73,,8.298,25.1548,3.0314,0.5039,0.2539,inside,3,6.8381,0.7448,0.8677,,
6,C,diamond,4.0,3.57,1.5459,11.2603,24.3831,2.1654,0.3682,0.1355,inside,4,6.0795,0.7175,0.6394,2.4177,0.8828
10,Ne,fcc,12.0,4.43,3.1325,21.5645,40.963,1.8996,0.3102,0.0962,inside,8,5.0014,0.6667,0.3339,9.3823,2.2388
11,Na,bcc,8.0,4.23,3.6633,5.1391,47.2864,9.2013,0.8039,0.6463,past,1,9.2013,0.8039,1.401,2.6148,0.9612
12,Mg,hcp,12.0,3.21,3.1982,7.6462,15.0353,1.9664,0.3258,0.1061,inside,2,5.3304,0.6841,0.9416,3.3965,1.2228
13,Al,fcc,12.0,4.05,2.8638,5.9858,18.8286,3.1456,0.5176,0.2679,inside,11,4.7194,0.6503,1.2028,2.3809,0.8675
14,Si,diamond,4.0,5.43,2.3513,8.1517,16.3458,2.0052,0.3345,0.1119,inside,12,4.6572,0.6465,0.8832,2.6621,0.9791
15,P,cubic,,7.17,,10.4867,19.7695,1.8852,0.3068,0.0941,inside,13,4.6047,0.6432,0.6866,,
16,S,orthorhombic,,10.47,,10.36,23.3379,2.2527,0.3851,0.1483,inside,14,4.5598,0.6403,0.695,,
17,Cl,orthorhombic,,6.24,,12.9676,23.8136,1.8364,0.2949,0.087,inside,15,4.5209,0.6377,0.5552,,
18,Ar,fcc,12.0,5.26,3.7194,15.7596,27.6297,1.7532,0.2736,0.0748,inside,16,4.4869,0.6355,0.4569,8.1413,2.097
19,K,bcc,8.0,5.23,4.5293,4.3407,31.625,7.2858,0.7586,0.5755,past,1,7.2858,0.7586,1.6587,2.7307,1.0045
20,Ca,fcc,12.0,5.58,3.9457,6.1132,11.8717,1.942,0.3202,0.1025,inside,18,4.4301,0.6317,1.1778,3.3501,1.209
21,Sc,hcp,12.0,3.31,3.2575,6.5615,12.7998,1.9507,0.3222,0.1038,inside,19,4.4061,0.63,1.0973,2.9687,1.0881
22,Ti,hcp,12.0,2.95,2.8961,6.8281,13.5755,1.9882,0.3307,0.1094,inside,20,4.3845,0.6286,1.0544,2.7466,1.0103
23,V,bcc,8.0,3.02,2.6154,6.7462,14.634,2.1692,0.3689,0.1361,inside,21,4.3648,0.6272,1.0672,2.4506,0.8963
24,Cr,bcc,8.0,2.88,2.4942,6.7665,16.4863,2.4365,0.418,0.1747,inside,22,4.3469,0.626,1.064,2.344,0.8519
25,Mn,cubic,,8.89,,7.434,15.64,2.1038,0.3556,0.1265,inside,23,4.3305,0.6248,0.9685,,
26,Fe,bcc,8.0,2.87,2.4855,7.9025,16.1992,2.0499,0.3442,0.1185,inside,24,4.3154,0.6237,0.9111,2.7281,1.0036
27,Co,hcp,12.0,2.51,2.4987,7.881,17.0844,2.1678,0.3686,0.1359,inside,25,4.3014,0.6227,0.9136,2.7352,1.0062
28,Ni,fcc,12.0,3.52,2.489,7.6399,18.1688,2.3782,0.408,0.1664,inside,26,4.2884,0.6218,0.9424,2.6411,0.9712
29,Cu,fcc,12.0,3.61,2.5527,7.7264,20.2924,2.6264,0.4485,0.2011,inside,27,4.2762,0.6209,0.9318,2.7393,1.0077
30,Zn,hcp,12.0,2.66,2.66,9.3942,17.9644,1.9123,0.3133,0.0981,inside,28,4.2649,0.6201,0.7664,3.4707,1.2444
31,Ga,orthorhombic,,4.51,,5.9993,20.5151,3.4196,0.5475,0.2997,inside,29,4.2543,0.6194,1.2001,,
32,Ge,diamond,4.0,5.66,2.4509,7.8994,15.9346,2.0172,0.3371,0.1137,inside,30,4.2443,0.6186,0.9114,2.689,0.9892
33,As,rhombohedral,,4.13,,9.7886,18.5892,1.8991,0.3101,0.0962,inside,31,4.2348,0.6179,0.7355,,
34,Se,hcp,12.0,4.36,3.5312,9.7524,21.196,2.1734,0.3698,0.1367,inside,32,4.2259,0.6173,0.7383,4.7831,1.5651
35,Br,orthorhombic,,6.67,,11.8138,21.591,1.8276,0.2927,0.0857,inside,33,4.2174,0.6167,0.6094,,
36,Kr,fcc,12.0,5.72,4.0447,13.9996,24.3598,1.74,0.2701,0.0729,inside,34,4.2093,0.6161,0.5143,7.8646,2.0624
37,Rb,bcc,8.0,5.59,4.8411,4.1771,27.2895,6.5331,0.7345,0.5395,past,1,6.5331,0.7345,1.7236,2.8087,1.0327
38,Sr,fcc,12.0,6.08,4.2992,5.6949,11.0303,1.9369,0.319,0.1018,inside,36,4.1943,0.615,1.2643,3.4006,1.2239
39,Y,hcp,12.0,3.65,3.5582,6.2173,12.2236,1.9661,0.3257,0.1061,inside,37,4.1872,0.6144,1.158,3.0726,1.1225
40,Zr,hcp,12.0,3.23,3.1775,6.6341,13.13,1.9792,0.3287,0.108,inside,38,4.1804,0.6139,1.0853,2.9278,1.0743
41,Nb,bcc,8.0,3.3,2.8579,6.7588,14.32,2.1187,0.3587,0.1287,inside,39,4.1739,0.6134,1.0652,2.6828,0.9869
42,Mo,bcc,8.0,3.15,2.728,7.0924,16.16,2.2785,0.39,0.1521,inside,40,4.1677,0.613,1.0151,2.6873,0.9885
43,Tc,hcp,12.0,2.74,2.7077,7.1194,15.26,2.1434,0.3638,0.1323,inside,41,4.1616,0.6125,1.0113,2.6774,0.9849
44,Ru,hcp,12.0,2.7,2.6463,7.3605,16.76,2.277,0.3897,0.1519,inside,42,4.1557,0.6121,0.9782,2.7053,0.9952
45,Rh,fcc,12.0,3.8,2.687,7.4589,18.08,2.4239,0.4159,0.173,inside,43,4.1501,0.6117,0.9653,2.7837,1.0238
46,Pd,fcc,12.0,3.89,2.7506,8.3368,19.43,2.3306,0.3995,0.1596,inside,44,4.1446,0.6112,0.8636,3.185,1.1585
47,Ag,fcc,12.0,4.09,2.8921,7.5762,21.4844,2.8358,0.4786,0.229,inside,45,4.1392,0.6108,0.9503,3.0433,1.1129
48,Cd,hcp,12.0,2.98,2.98,8.9938,16.9083,1.88,0.3056,0.0934,inside,46,4.134,0.6104,0.8005,3.7225,1.3144
49,In,bct,,3.2456,,5.7864,18.8704,3.2612,0.5306,0.2816,inside,47,4.1289,0.6101,1.2443,,
50,Sn,bct,,5.82,,7.3439,14.6331,1.9925,0.3317,0.11,inside,48,4.1239,0.6097,0.9804,,
51,Sb,rhombohedral,,4.51,,8.6084,16.626,1.9314,0.3177,0.1009,inside,49,4.1191,0.6093,0.8364,,
52,Te,hcp,12.0,4.45,3.9189,9.0098,18.6,2.0644,0.3473,0.1207,inside,50,4.1143,0.6089,0.7991,4.9041,1.5901
53,I,orthorhombic,,7.27,,10.4512,19.1313,1.8305,0.2934,0.0861,inside,51,4.1096,0.6086,0.6889,,
54,Xe,fcc,12.0,6.2,4.3841,12.1298,20.975,1.7292,0.2672,0.0714,inside,52,4.105,0.6082,0.5936,7.386,1.9996
55,Cs,bcc,8.0,6.05,5.2395,3.8939,23.1574,5.9471,0.7121,0.5071,past,1,5.9471,0.7121,1.849,2.8337,1.0416
56,Ba,bcc,8.0,5.02,4.3474,5.2117,10.0038,1.9195,0.315,0.0992,inside,54,4.096,0.6075,1.3815,3.1469,1.1464
57,La,hcp,12.0,3.75,3.7286,5.5769,11.185,2.0056,0.3346,0.1119,inside,55,4.0917,0.6072,1.291,2.8881,1.0606
58,Ce,fcc,12.0,5.16,3.6487,5.5386,10.956,1.9781,0.3284,0.1079,inside,56,4.0873,0.6069,1.2999,2.8068,1.032
59,Pr,hcp,12.0,3.67,3.6416,5.4702,10.631,1.9434,0.3205,0.1027,inside,57,4.0831,0.6065,1.3162,2.7668,1.0177
60,Nd,hcp,12.0,3.66,3.6317,5.525,10.783,1.9517,0.3224,0.104,inside,58,4.0788,0.6062,1.3031,2.7869,1.0249
62,Sm,rhombohedral,,9.0,,5.6437,11.078,1.9629,0.325,0.1056,inside,60,4.0705,0.6056,1.2757,,
63,Eu,bcc,8.0,4.61,3.9924,5.6704,11.24,1.9822,0.3294,0.1085,inside,61,4.0664,0.6052,1.2697,3.1443,1.1456
64,Gd,hcp,12.0,3.64,3.5735,6.1498,12.076,1.9636,0.3252,0.1057,inside,62,4.0623,0.6049,1.1707,3.0523,1.1159
65,Tb,hcp,12.0,3.6,3.524,5.8638,11.513,1.9634,0.3251,0.1057,inside,63,4.0582,0.6046,1.2278,2.8701,1.0543
66,Dy,hcp,12.0,3.59,3.5026,5.9391,11.647,1.9611,0.3246,0.1053,inside,64,4.0541,0.6043,1.2123,2.8893,1.061
67,Ho,hcp,12.0,3.58,3.4885,6.0215,11.781,1.9565,0.3235,0.1047,inside,65,4.0501,0.604,1.1957,2.9176,1.0708
68,Er,hcp,12.0,3.56,3.4691,6.1077,11.916,1.951,0.3223,0.1039,inside,66,4.0461,0.6037,1.1788,2.9428,1.0794
69,Tm,hcp,12.0,3.54,3.4496,6.1844,12.065,1.9509,0.3222,0.1038,inside,67,4.0421,0.6033,1.1642,2.9631,1.0862
70,Yb,fcc,12.0,5.49,3.882,6.2542,12.1792,1.9474,0.3214,0.1033,inside,68,4.0381,0.603,1.1512,3.3721,1.2155
71,Lu,hcp,12.0,3.51,3.4416,5.4259,14.13,2.6042,0.4451,0.1981,inside,69,4.0341,0.6027,1.3269,2.5936,0.9531
72,Hf,hcp,12.0,3.2,3.1337,6.8251,14.61,2.1406,0.3632,0.1319,inside,70,4.0301,0.6024,1.0549,2.9706,1.0888
73,Ta,bcc,8.0,3.31,2.8665,7.5496,16.2,2.1458,0.3642,0.1327,inside,71,4.0261,0.6021,0.9537,3.0058,1.1005
74,W,bcc,8.0,3.16,2.7366,7.864,16.37,2.0816,0.351,0.1232,inside,72,4.0221,0.6018,0.9155,2.9891,1.095
75,Re,hcp,12.0,2.76,2.7398,7.8335,16.6,2.1191,0.3588,0.1287,inside,73,4.0181,0.6014,0.9191,2.9809,1.0922
76,Os,hcp,12.0,2.74,2.6799,8.4382,17.0,2.0146,0.3366,0.1133,inside,74,4.014,0.6011,0.8532,3.1409,1.1445
77,Ir,fcc,12.0,3.84,2.7153,8.967,17.0,1.8958,0.3094,0.0957,inside,75,4.01,0.6008,0.8029,3.3818,1.2184
78,Pt,fcc,12.0,3.92,2.7719,8.9588,18.56,2.0717,0.3489,0.1217,inside,76,4.006,0.6005,0.8037,3.4491,1.2381
79,Au,fcc,12.0,4.08,2.885,9.2256,20.203,2.1899,0.373,0.1391,inside,77,4.0019,0.6002,0.7804,3.6967,1.3074
80,Hg,rhombohedral,,2.99,,10.4375,18.7569,1.7971,0.285,0.0812,inside,78,3.9978,0.5998,0.6898,,
81,Tl,hcp,12.0,3.46,3.4122,6.1083,20.4283,3.3444,0.5396,0.2912,inside,79,3.9937,0.5995,1.1787,2.8949,1.0629
82,Pb,fcc,12.0,4.95,3.5002,7.4167,15.0325,2.0269,0.3392,0.1151,inside,80,3.9895,0.5992,0.9708,3.6056,1.2825
83,Bi,rhombohedral,,4.75,,7.2855,16.703,2.2926,0.3926,0.1541,inside,81,3.9854,0.5988,0.9882,,
84,Po,sc,6.0,3.35,3.35,8.4181,19.3,2.2927,0.3926,0.1541,inside,82,3.9812,0.5985,0.8553,3.9168,1.3653
89,Ac,fcc,12.0,5.31,3.7547,5.3802,11.75,2.1839,0.3718,0.1383,inside,87,3.9595,0.5967,1.3382,2.8058,1.0317
90,Th,fcc,12.0,5.08,3.5921,6.3067,12.1,1.9186,0.3147,0.0991,inside,88,3.955,0.5964,1.1416,3.1465,1.1463
91,Pa,tetragonal,,3.92,,5.89,11.9,2.0204,0.3378,0.1141,inside,89,3.9505,0.596,1.2224,,
92,U,orthorhombic,,2.85,,6.194,11.6,1.8728,0.3038,0.0923,inside,90,3.9459,0.5956,1.1624,,
93,Np,orthorhombic,,4.72,,6.2655,11.5,1.8354,0.2946,0.0868,inside,91,3.9414,0.5953,1.1491,,
94,Pu,monoclinic,,,,6.0258,11.5,1.9085,0.3124,0.0976,inside,92,3.9365,0.5949,1.1948,,

