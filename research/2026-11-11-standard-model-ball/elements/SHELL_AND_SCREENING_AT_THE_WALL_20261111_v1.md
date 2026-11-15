# Shell and screening at the wall — v1 (11 Nov 2026, evening)
Jeromie Beasley. Prepared with AI assistance (Claude, Anthropic).

Plan step 1 of `PLAN_FULL_TABLE_20261111_v1.md`. Script `shell_screen_04.py`, output `shell_screen_04.out`.
Data: `data/element_thresholds_20261011.json.gz`. Kill lines are in the script header, written before each run.

## 1. The plan's first kill line cannot fire
Velocity addition of two Gammas is multiplication of their ratios: z = z_sh * z_scr, with z_sh = (n/(n-1))^2.
So "Gamma_scr >= s*(n)" is "z >= 3 + 2 sqrt 2" written another way. Checked on every core-line step: the
identity holds to 2e-16. The crossing is at Gamma_scr = s*(n) by arithmetic, on any data. Corrected s*(n):
0.186, 0.443, 0.533, 0.577, 0.604, 0.621 for n = 2..7.

## 2. What the split does show (computed)
Write IE_val = Ry (Zv/n)^2 and IE_core = Ry (Zc/(n-1))^2. Then z_scr = (Zc/Zv)^2, and
Gamma_scr = r (+) r with r = (Zc - Zv)/(Zc + Zv): the step between the two effective charges, taken twice.
The wall is Zc/Zv = (1 + sqrt 2)(n-1)/n, which rises with n toward 1 + sqrt 2.

Alkali column:

| | n | Zc/Zv | wall ratio | margin |
|---|---|---|---|---|
| Na | 3 | 2.0222 | 1.6095 | +0.413 |
| K | 4 | 2.0244 | 1.8107 | +0.214 |
| Rb | 5 | 2.0448 | 1.9314 | +0.113 |
| Cs | 6 | 2.0322 | 2.0118 | +0.020 |
| Fr | 7 | 2.0102 | 2.0693 | -0.059 |

Kill line for this part: a spread over 2% among Na, K, Rb, Cs. Spread found: 1.1%. Not fired.
The screening part is the same for every alkali from Na to Cs (Gamma_scr 0.607 to 0.614). The alkalis approach
the wall down the column because the shell part falls, and for no other reason. A fixed charge ratio of
2.02 to 2.04 meets the rising wall ratio between n = 6 and n = 7 (n < 6.16 to 6.54). Caesium is the last.
Lithium is apart (1.873, wall 1.207): its core is the two-electron core.

## 3. Francium (a reading from four points, graded as such)
If francium keeps the alkali charge ratio, IE2 = IE1 (7/6)^2 (Zc/Zv)^2 = 22.67 to 23.18 eV. The wall needs
23.74 eV. Archived value 22.4 +/- 1.9 eV (semi-empirical). Reading: francium is inside the wall.
Fails this way: a measured Fr+ ionisation energy above 23.74 eV, or outside 22.7 to 23.2 eV.
Literature search (five requests): no measured Fr+ ionisation energy and no ab initio Fr2+ threshold found;
the NIST Fr II entry could not be opened, so 22.4 +/- 1.9 is unconfirmed this session.

## 4. Helium core: the 5/8 places the crossing (reproduction of the 1/Z series)
IE_core = Z^2/2 - (5/8) Z + 0.157666, IE_val = Z^2/8 - (290/729) Z + 0.250500 (Hartree). No fit.
The second-order numbers are recalled literature values, not looked up this session.
Kill line: crossing outside (6, 7), or any measured z for Z = 5..10 missed by over 2%. Not fired:
crossing at Z* = 6.538 (measured line interpolates to 6.57); worst miss 0.55% (boron).
Opposite run, core unscreened (no 5/8): crossing moves to Z* = 9.47, between fluorine and neon.
So the He-like 5/8 is what puts the wall between carbon and nitrogen.
This is standard series theory; what it adds is the location of the 5/8 in the wall picture.

## 5. Plan step 2 cannot run as written
The "2/3 vacuum-mix line" is defined only in `research/2026-11-07/scripts/pressure_line_01.py`:
E = 1 - V_own/V, a space fraction. It is not a Gamma, so Gamma = 2/3 (the ratio-5 edge) is a different object
until a map between them is written down. Its input `RECOVERED_ELEMENT_DATA_20261106.csv` is on no branch.
Vacuum disk v2 to v6 are on no branch; only v1 is in the repo.
