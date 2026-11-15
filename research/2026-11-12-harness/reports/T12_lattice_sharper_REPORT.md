# T12_lattice_sharper: second probing pass on lattice, conductivity and heat (2026-11-12)

Population and sources. 84 elements with a solid reference state (T9 table); 56 are "metals" (T9's fixed list, with d_nn). Structures and lattice constants: ASE 3.29.0 (Ashcroft and Mermin). Ionization ladders: NIST via the package CSV (same table as T9). Melting point, thermal conductivity, density, atomic volume: mendeleev 1.3.0 (melting point cross-checked against pymatgen 2026.10.24: they disagree by more than 1% only for Th, 2023 against 2115 K). Electrical resistivity (room temperature): pymatgen 2026.10.24 only, because mendeleev 1.3.0 has no resistivity field. All of these are other people's published measurements, not his. Lines, definitions and kill lines were written in STATE.md before the run; scripts t12_table.py, t12_lines.py (output lines_out.txt). Shuffle control everywhere: 5,000 shuffles, seed 20261112.

## Results first

| Line | Number | Kill line | Verdict |
| :-- | :-- | :-- | :-- |
| S1 B99 split at core-opening wall (bcc without alkalis n=9 against fcc/hcp metals n=41) | AUC of G_screen = 0.593, shuffle p = 0.398. Opposites: G_shell alone 0.512 (p = 1.0), unsplit G_core 0.593 (p = 0.395) | AUC < 0.70 | NOT MET |
| S2 composition crosses the wall (82 elements: 69 conductors, 13 non-conductors) | count of crossing steps: AUC 0.533, p = 0.600. Index of first crossing step: AUC 0.748, p = 0.0056 | both < 0.70 | NOT MET in substance (the index meets the letter but is a ladder-length artefact, see below) |
| S3 conductivity and the gap (55 metals) | Spearman(ln resistivity, ln s) = +0.027, p = 0.839. Opposite Spearman(ln resistivity, ln IE1) = -0.509, p = 0.0004 | abs < 0.4 | NOT MET. The level wins |
| S4 heat forms the lattice (melting point, within class) | against L1: bcc -0.516, fcc -0.044, hcp +0.443 (1 of 3 at 0.5). Against core-opening length: bcc -0.741, fcc -0.191, hcp -0.226 (1 of 3). Opposite, against IE1: bcc +0.890, fcc +0.641, hcp +0.156 (2 of 3) | fewer than 2 classes at 0.5 | NOT MET for both lengths. The opposite (IE1) is MET, shuffle p = 0.0054 |
| S5 R2 repaired (56 metals) | partial Spearman(ln d_nn, L1 given ln IE1) = -0.461, permutation p = 0.0010 | abs < 0.3 | MET |
| A1 (mine) plain G1^2, conductor against non-conductor | AUC 0.697, p = 0.030 | < 0.70 | NOT MET (by 0.003) |
| A2 (mine) ln resistivity against L1 (55 metals) | -0.353, p = 0.0098 | abs < 0.4 | NOT MET |
| A3 (mine) melting point against ln s (56 metals) | -0.135, p = 0.317. Opposite, against ln d_nn: -0.579, p = 0.0002 | abs < 0.4 | NOT MET; absolute spacing orders melting point, dimensionless spacing does not |

Shuffle controls for S4: the chance that a shuffled melting point reaches 2 or more classes at 0.5 is 0.3 percent (L1), 0.7 percent (L_core), 0.5 percent (IE1). So the criterion is hard to reach by luck, and IE1 reaches it, the peel lengths do not.

### Plain English
- The one registered line that stands is S5. Once the level (IE1) is removed, the shape of the first step still orders the spacing: elements whose second ionization jumps more relative to the first sit closer together than their level predicts. It is a partial correlation of -0.461 over 56 metals. Not registered but worth stating: this is mathematically the same as saying ln d_nn falls with ln IE2 at fixed ln IE1, and it holds without the alkalis (-0.533) and inside each class (bcc -0.398, fcc -0.607, hcp -0.531). This repairs T9's R2, which failed because ln s contained IE1.
- S1 fails cleanly. The shell term is almost constant: for 49 of the 50 elements the opened shell is n = 2 and G_shell = 3/5 (Mg alone is n = 3, 5/13). Subtracting it only shifts G by a near-constant, so G_screen ranks the elements the same as G: AUC 0.593 both ways. After the alkalis are set aside, the core-opening step does not separate bcc from 12-coordinated metals. The bcc non-alkalis have G_screen 0.0028 (W) to 0.0436 (V); the 12-coordinated range is 0.0 to 0.41 (Mg 0.406, Be 0.358).
- S2: a shell step alone never reaches the wall, so a crossing is always screening. But only 8 elements have any crossing step in the whole ladder: Li, Na, K, Rb, Cs (step 1), Be (step 2), B (step 3), C (step 4). Six of them are conductors (the alkalis and Be), two are non-conductors (B, C). Counting crossings gives no separation (conductors 63 of 69 have zero, non-conductors 11 of 13 have zero). The first-crossing index looks good (0.748) only because "no crossing" is coded as ladder length plus 1, and ladder length itself separates the groups: Spearman(f, number of known steps) = 0.965, AUC of ladder length = 0.785 (light elements have short known ladders). In the registered opposite (steps up to 5 only) the AUC falls to 0.527 (count 0.533). So the letter is met, the substance is not.
- S3: conductivity is not tied to the dimensionless gap (+0.027). It is tied to the level: ln IE1 -0.509, and, not registered, ln IE2 -0.701 and ln IE3 -0.717. By B102 the level carries scale, and it is the level that wins here.
- S4: heat does not order the lattice through the peel lengths. The level wins (IE1 in bcc +0.890, fcc +0.641). The bcc numbers for the peel lengths are driven by the alkalis (without them, bcc n=9: L1 +0.50, L_core -0.35, IE1 +0.60).

## Seen, not registered (descriptive, best of many, nothing here is a test)

Where each line plainly fails, by family:
- S1. alkali: excluded by the rule (G_screen 0.608 median, the one family with a large value). Alkaline earth: Mg (0.406) and Be (0.358) are hcp with large G_screen, Ba (bcc) 0.012. Transition metals: bcc V 0.044, Cr 0.042, Fe 0.038 sit inside the hcp and fcc range (Ti 0.046, Sc 0.048, Ca 0.051 are hcp/fcc with higher values). Eu 0.008, Ta 0.003, W 0.003 sit below the 12-coordinated median (0.011).
- S2. Conductors with no crossing step: all 63 except the alkalis and Be. Non-conductors with a crossing: B, C. Lowest first-step G1^2 among conductors: Hg 0.081, Np 0.087, U 0.092, Cd 0.093, P 0.094 (P is listed with resistivity 1e-7 by pymatgen, likely a black-phosphorus entry; kept as the package gives it), Ir 0.096: these lie inside the non-conductor range (0.071 to 0.254).
- S3. Elements furthest from the level line (ln resistivity on ln IE1): too conductive, Al -2.09, Ag -1.99, K -1.92, Na -1.89, Cu -1.88, Ca -1.79; too resistive, Gd +1.89, Tb +1.63, Po +1.51, Dy +1.45, Er +1.45, Ho +1.36 (the heavy lanthanides). Family medians of ln resistivity: lanthanides -14.07, everything else -15.5 to -16.9.
- S4. In hcp (n=25) the sign of melting point against L1 is positive (+0.443), in bcc negative (-0.516), fcc near zero (-0.044): no common direction. The best single quantity within hcp is L2 (the second step, -0.488); within fcc IE1 (+0.641).

Which single peel quantity orders best (reported orientation-free; levels listed for comparison, they are not peel quantities):
- (a) Structure. bcc (alkalis in) against 12-coordinated: L1 (equivalently G1) 0.758, then G_screen 0.739 and L_core 0.733. bcc without alkalis against 12-coordinated: nothing passes 0.67 (dimensionless spacing ln s 0.667, L1 0.623, L_core 0.593). hcp against fcc: L3 (third step) 0.680, otherwise below 0.65.
- (b) Conductivity. Conductor against non-conductor (n=82): ln IE1 0.945 (level), ln IE2 0.853, ln IE3 0.792; among peel lengths L_core 0.750 and G_screen 0.745; ladder length / Z 0.785 is not a peel quantity but is as good. Among metals, ln resistivity is ordered best by the level, ln IE3 -0.717 and ln IE2 -0.701; the best peel length is L3 +0.500, then L1 -0.353. Thermal conductivity (pymatgen, 55 metals with values) goes the same way: ln IE2 +0.715, L3 -0.511.
- (c) Melting point. Over all 56 metals the best quantities are density +0.625 and atomic volume -0.596 (not peel), then ln IE1 +0.432; the best peel length is G_screen -0.297, L_core -0.290. Within a class: bcc G_screen -0.824 (alkali-driven), fcc L2 -0.356, hcp L2 -0.488.

Sharper lines for a later pass (at most three):
1. Does the peel shape add anything to the level? Conductor against non-conductor and ln resistivity, cross-validated: ln IE1 alone against ln IE1 plus L_core (and plus L3 for resistivity). Today the level is 0.945 and the best length 0.750 alone, and nothing says whether the shape adds. Kill: no cross-validated gain over the level.
2. Extend S5 as the working form of B102: the partial Spearman of ln d_nn on the second step, then on L2 and L3, controlling for ln IE1 within each class separately, written before the run, with alkalis excluded. Seen today: -0.40 to -0.61.
3. Melting point against L2 within hcp and fcc, controlling for atomic volume (density), since volume and density order melting point best here and L2 is the best peel length in those two classes.

## Untested
- Temperature and allotropes: untested: no allotrope table on disk. mendeleev 1.3.0 phase_transitions holds named allotrope rows only for C, P, S, As, Se, Sn, Sb, Bk, without structure labels. pymatgen holds none. So "structure at a given temperature" and "side of the wall changes with the allotrope" were not run.
- Time (his fourth factor): untested, no data column.
- Heat as formation process (heat to cold forms the lattice): only melting point against peel and level was tested, which is a static property, not the formation.
- The shell assignment is one declared rule (hydrogen-like n from the neutral configuration, removal by n then l descending). The core-opening step is the largest ratio, which is the 1s opening for 49 of 50 elements in S1; steps inside the valence block or at the d-shell boundary were not split. Another assignment was not run.
- Two samples have many missing property values: mendeleev thermal conductivity (59 of 84), mendeleev melting point (79 of 84); resistivity is missing for Ne, Ar, Kr, Xe (taken as non-conductors by fixed rule), Se, Ac (excluded).
- Lattice sample is one reference state per element; the 19 elements with no coordination formula are outside the lines.

## Files
/home/claude/harness/workers/T12_lattice_sharper/: lattice_table_ext.csv (T9 columns plus property columns, each with a source column: mp_src, mp_pmg_src, rho_src, kappa_mend_src, kappa_pmg_src, density_src, atomic_volume_src, n_electrons_removed_order_src; n_left, n_open), lattice_table_ext2.csv (adds derived G_shell, G_screen, L_core, crossing count c and index f, conductor label), t12_table.py, t12_lines.py, lines_out.txt, t12_seen.py, seen_out.txt, t12_seen2.py, seen2_out.txt, STATE.md, REPORT.md.
