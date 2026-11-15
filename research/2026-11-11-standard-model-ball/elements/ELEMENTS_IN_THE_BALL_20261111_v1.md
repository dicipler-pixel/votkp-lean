# How each element plays out in the ball — v1 (11 Nov 2026)
Jeromie Beasley

Data: `data/element_thresholds_20261011.json.gz` (118 elements, 103 full ladders, 5,328 steps).
One peel step z = IE_{q+1}/IE_q → Γ = tanh(½ ln z); wall Γ² = ½ at z = 3+2√2 = 5.828.
Scripts: `element_ball_01.py`, `core_open_02.py`, `iso_cross_03.py` (each with its .out). Kill lines are written in each header before the run.

## Results
**K1: the biggest step sits at a closed core. Passes.**
- 101 of 101 elements with two or more shells of data.
- Every element's largest step opens a noble-gas core. There are no exceptions.

**K2: a whole shell, peeled as one boost, sits at the wall. Fails this way.**
- The median |Γ²_block − ½| is 0.404, against 0.297 for random blocks of the same length (p = 1.0).
- The opposite (a whole shell past the wall, "converted" as a unit) fails too: 0.296 against 0.338 for random blocks.
- Block Γ² depends on block length and little else.
- So the wall is a property of single steps, not of whole shells.

**Each core-opening crosses the wall exactly once along its isoelectronic line.**
- The kill line was "more than one crossing on any line". No line crossed more than once.
- In the hydrogenic limit every core-opening ratio tends to (n_out/n_core)² (4 for K, 2.25 for L, and so on), and all of these are inside the wall. So every line that starts past the wall has to cross it.
- Where each line crosses:

| Core | Line | Last past the wall | First inside |
|---|---|---|---|
| K (He core) | Li-like | C³⁺, z = 6.080 | N⁴⁺, z = 5.640 (interpolated crossing at Z ≈ 6.57) |
| L (Ne core) | Na-like | Na, 9.20 | Mg⁺, 5.33 |
| M (Ar core) | K-like | K, 7.29 | Ca⁺, 4.29 |
| Kr core | Rb-like | Rb, 6.53 | Sr⁺, 3.89 |
| Xe core | Cs-like | Cs, 5.95 | Ba⁺, 3.58 |
| Rn core | Fr-like | none | Fr, 5.50 |

- Neutral elements, by period: period 2 is past the wall for 1–4 valence electrons (Li, Be, B, C) and inside it from N onward. Periods 3–6 have only the alkali past the wall. Period 7 has none.

**Francium is undecided by the data. This is a prediction.**
- Fr IE2 = 22.4 ± 1.9 eV (grade S, semi-empirical), so z = 5.50, anywhere from about 5.0 to 6.0. The wall is inside that range.
- The ball says francium is past the wall only if a measured Fr⁺ ionisation energy exceeds W·IE1 = 23.74 eV.
- The alkali sequence approaching the wall: Γ² = 0.752, 0.646, 0.576, 0.539, 0.507, then 0.479 for Fr on the semi-empirical value. Cs is past by just 2%.
- Relativistic 7s contraction raises Fr's IE1 above Cs's (4.07 against 3.89 eV), and that is what pulls Fr back inside.

**K3: steps on the wall to 2%.**
- Only Cs (Γ² = 0.5071).

## What it means in the frame
- The wall separates "a lone electron over a closed core" from everything else.
- Past the wall, the two equal perpendicular peel loops do not close. The outer electron and the core cannot be peeled as one turning step, so only the phase is carried across (the alkali optical phase found on 10 Nov).
- As Z rises along any core line, the step falls back inside the wall. Period 2 is the only period where the crossing lands in the middle of the row, between carbon and nitrogen. Everywhere else it lands right after the alkali.
- This is a statement about where the crossing falls, not about chemistry. No claim is made that carbon is special because of it.

## Already in the old builds (from the readers so far)
- v0.3/v0.4 (§8.6, Theorem 8.1) already read IE ratios as Smith reflections, τ = 2 artanh Γ, with the alkali τ₁ = 2.641 … 1.705.
- Γ² = ½ is not named there, but its own numbers put Li–Cs above 1/√2 and Fr below.
- Line 268 of that version says the atomic chart "carries no phase". Today's frame says the phase is what survives at the wall, so this is an open contradiction to keep.
