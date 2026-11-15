# constants check, Sec 23.4 (12 Nov 2026)
Scripts (all in this folder, each with WHY and KILL LINE): part1.py (+part1.out), part34.py (+part34.out), part4b.py (+part4b.out). Web requests used: 6 of 6 (3 searches, 3 fetches), no page twice.

## 1. Exact arithmetic and integrals: CONFIRMED (computed here, sympy, exact)
- 5965/5832 - 5/8 = 290/729; 2*17/81 - 16/729 = 290/729 (both exact, True).
- Hydrogenic 1s, 2s radial functions (normalised, charge Z): F0(1s,2s) = 17Z/81, G0(1s,2s) = 16Z/729, 2F0-G0 = 290Z/729. F0(1s,1s) = 5Z/8 also confirmed.

## 2. Second-order constants at source
He-like, e2:
- NOT read at primary source (Hylleraas, Scherr-Knight, Midtdal not reached; Baker, Freund, Hill, Morgan, Phys. Rev. A 41, 1247 (1990) paywalled, not reached).
- Confirmed in a secondary source that quotes Baker et al. (1990): J.C. Lopez Vieyra and A.V. Turbiner, "On 1/Z expansion for two-electron systems", arXiv:1309.2707 (2013), https://arxiv.org/pdf/1309.2707 . Table I prints e2 = -0.157 666 429 469 15 (attributed to Schwartz 2013, private communication, 25 digits -0.1576664294691509410566793); the caption says Baker et al. differ only in the 14th digit (4 for 5). Paper's -0.157666 agrees.
- Also printed in Turbiner, Lopez Vieyra, Olivares-Pilon, "Helium-like and Lithium-like ions: Ground state energy", arXiv:1707.07547, https://arxiv.org/pdf/1707.07547 : E2(He-like) = -0.15766642946915 (same).
Li-like 1s^2 2s, e2:
- NOT read at primary source. Yan, Tambasco, Drake, Phys. Rev. A 57, 1652 (1998) ("Energies and oscillator strengths for lithiumlike ions"): only the abstract was reachable (https://data.zhenzhi.com/details/1/914984016); it prints no coefficient.
- Secondary: arXiv:1707.07547 (URL above) prints E2(Li-like) = -0.40816616526115 and attributes it to Yan, Tambasco, Drake PRA 57, 1652 (1998), ref [7]. Same paper prints E0 = -9/8, E1 = 5965/5832 and for He-like -1, 5/8. Paper's -0.408166 agrees. Difference e2(Li)-e2(He) = -0.250499736 so 0.250500 agrees.
- Hylleraas 1930, Scherr-Knight 1963, Midtdal 1965, Horak, Seung-Wilson 1967: NOT confirmed (not reached). Do not cite as read.

## 3. Data-only fit (computed here from element_thresholds_20261011.json.gz)
IE_core = threshold q=Z-2 (all grade T); IE_val = threshold q=Z-3 (E/S for Z=6-10, T for Z>=11). Hartree = eV/27.211386246. Residual R = IE - (two leading terms) for Z=6..20, no other subtraction:
- Core R rises 0.159 (Z=6) to 0.982 (Z=20): the Z^4 relativistic trend dominates. Val R 0.257 to 0.502.
- Constant-only or a+b/Z fits are poor (rms 0.07-0.25 Ha). Adding alpha^2 Z^4 term: core a = 0.108 (Z 6-20), 0.141 (Z 6-12), 0.079 (Z 9-20); with a 1/Z^2 term 0.116 (Z 6-12) to -0.043; fitted Z^4 coefficient ~0.09-0.105.
- Val with Z^4 term: a = 0.232 (6-20), 0.244 (6-12), 0.222 (9-20); with 1/Z^2 term 0.18-0.24; Z^4 coefficient ~0.026-0.032.
- Verdict: data constrain the constants only loosely (spread ~0.1 Ha core, ~0.03 Ha val, set by model choice). Val constant is consistent with 0.2505 within ~0.01-0.03 for the best Z=6-12 fit; core constant is not pinned (0.04 to 0.14 vs 0.1577); the data neither confirm nor exclude 0.157666. The literature values are not testable at the 1e-3 level with Z>=6 data and a free Z^4 term. By the kill line (>0.005 Ha) the data fits do NOT independently support the constants to that accuracy. Opposite setups (no Z^4 term) fail badly, as expected.

## 4. Crossing Z* (z = 3+2sqrt2 = 5.8284), computed here
- Confirmed constants (0.157666, 0.250500): Z* = 6.5385 (paper 6.538 OK). With printed-digit constants 6.5385.
- First-order terms only: 7.4100 (paper 7.41 OK).
- 5/8 removed with BOTH constants kept: 9.5478. Paper's 9.47 is reproduced only by the variant in shell_screen_04.py that drops 5/8 AND the core constant 0.157666 but keeps the val constant 0.250500 (9.4700). Paper text says only "5/8 removed": a MISMATCH of definition (9.548 vs 9.47). Also 5/8 and both constants removed: 10.145.
- Crossing with data-fitted constants (0.108, 0.232): 6.583. Measured linear interpolation: 6.571 (paper 6.57 OK).
