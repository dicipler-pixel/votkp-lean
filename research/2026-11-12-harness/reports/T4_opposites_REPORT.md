# T4_opposites: the 33 kills never retried (ledger section C2), one natural opposite each

Results first. Of 33 items, 4 were skipped by instruction (18, 19, 33 need data that does not exist here; 28 belongs to another worker). Of the other 29: 24 were run, 5 could not be run (6, 23, 24, 31, 32).
Against the frozen kill lines (text in STATE.md, copied before any run): FIRED 13, NOT FIRED 11. "Fired" means failed in that setup only. Nothing here calls an idea dead.
Every run was done on data already on disk; every script starts with `# SCRIPT: NAME-OPP-01`; where the original reproduced in under 5 minutes it was reproduced first (outputs in items/NN/). Where the item text left a quantity open (which rule, which family, what "beat" means) the operationalisation is written in the script header before the run and repeated in RESULTS.md. Full numbers per item: RESULTS.md. Script and data paths: TRIAGE.md.

| # | item | status | verdict vs frozen line | numbers | folder |
|---|---|---|---|---|---|
| 1 | Run 02 polarizability | run | NOT FIRED | level-only ln IE1 beats peel shape in 9 of 9 settings (K=10 kNN1 0.285 vs 0.288) | items/01 |
| 2 | NUM-01 numerator | run | FIRED | ratio-to-neighbour numerator MAE 0.715 vs denominator 0.291; D-N2 = -0.424 [-0.579,-0.272] (interpretation of "K=10" stated) | items/02 |
| 3 | NUC-01 other dataset | run (shape half only) | FIRED | holdout (1214 non-even-even nuclei) SHAPE 0.661/0.697 vs NPNN 0.840/0.755 (lin/kNN) | items/03 |
| 4 | H-01 echo weight | run | NOT FIRED | leave-one-metal-out |G| 0.977 vs w 0.743; bootstrap of difference +0.234 [0.088,0.404] | items/04 |
| 5 | f-block pairing | run | NOT FIRED | shifted pairing exact 4,2,3,4 of 14 (original 2,2,3,3) | items/05 |
| 6 | Snell third rule | could not run | none | "rule from the 8-electron contained set" and "beat" undefined; the contained set is the window rule itself (6 hits, 2 false) | RESULTS |
| 7 | CAT-01 Khovanov | run | FIRED | total rank separates 0 of 21 J4-resolved pairs (reduced and unreduced) | items/07 |
| 8 | THIN-01 omitted films | run (P1 side) | NOT FIRED | same side of bulk 11 of 12 omitted cases (line scaled from 13/15) | items/08 |
| 9 | RHYTHM level reading | partly run | T16 FIRED; T13 not; T20 fired | T16: level beats peel in 1 of 3 handlings (4/4, 0.80/0.80, 3 vs 0 of 7); T13 level line already wins on both radii; T20 pair beats level on 4 of 4. T02, T04, T05, T06, T07, T09, T18, T19 have no level-vs-peel comparison: not run | items/09 |
| 10 | RUSSELL no-wave baseline | run (T3, T7) | NOT FIRED | wave/row-mean error ratio 0.340 (E_at, n=63) and 0.325 (T_m, n=60); the original neighbour baseline still beats the wave (47.5 vs 61.4; 193.7 vs 275.2) | items/10 |
| 11 | G-02 ratio test | run | FIRED | first/second ratio off 10.32% (uncorrected), 12.77% (corrected) against 5% line; same comparison as registered S1, inverted | items/11 |
| 12 | P-01 other fit family | run | NOT FIRED | knots-only ratios: 2.51, 1.31, 0.15 combined sigma (line 3) | items/12 |
| 13 | WALL-RESIDUE form 2 | run | FIRED | s-kind CV <= 8.0% in all rows; p-kind CV 22.2, 16.6, 26.0% in rows 4-6 (3 rows above 10%) | items/13 |
| 14 | TIME-01b midpoint | run | NOT FIRED | midpoint-rule charge 1.000546 and 1.000556 (|Q-1| 5.5e-4); original rule 0.998954 | items/14 |
| 15 | depth law K+1 | run | FIRED | 0 of 3 misses contained at K=11-12; forced by arithmetic (outer <= 8) | items/15 |
| 16 | Run 03 random forest | run | NOT FIRED | RF static beats peel 9/9 covalent, 9/9 atomic, 9/9 hardness (original 9, 9, 8) | items/16 |
| 17 | T-O at K=6 | run | NOT FIRED | random 18-element test sets, seeds 0-4: T1 beats S2 on 5 of 5; seeds 5-204: 200 of 200 (mean 0.667 vs 0.347) | items/17 |
| 18 | DATA-01 E-only arm | skipped | | needs data not on disk | |
| 19 | T-C, T-G | skipped | | need the NIST fetch | |
| 20 | LADDER-WALL-01 per core | run | FIRED | beyond exceeds inside in 0 of 11 cores (4/97, 1/92, 1/84, 0/75, ...) | items/20 |
| 21 | PLASMA-WALL-01 | run | FIRED | Spearman of 1/E_wall: -0.057, +0.279, -0.261 (sign flip of the original) | items/21 |
| 22 | NEVER-TURN-01 | run | FIRED | 0 of 117 KnotInfo fields separate 4 never-turners from 19 turners with <=1 error; random relabellings also give 0 | items/22 |
| 23 | golden family clock | could not run | none | no definition of the "clock reading" for 89/34 on disk | RESULTS |
| 24 | 233/89 degree 116 | could not run | none | "unit circle" has no meaning for the Riley polynomial variable; the 200-digit run is unfinished in the sources | RESULTS |
| 25 | ELEMENT-BALL-01 K2 split | run | FIRED | median |G2-1/2| real vs random: shell part 0.5000 vs 0.4216, screening 0.4152 vs 0.3844, whole 0.4040 vs 0.2965; p = 1.0 each | items/25 |
| 26 | COLOUR-PEEL-03 CIE weights | run | NOT FIRED | toward/away stretch rate: sRGB Y 0.80/0.05, 1.03/0.12, 0.95/0.10 %; CIE1931 5.92/1.95, 6.41/1.98, 6.75/2.05 % | items/26 |
| 27 | HIDDEN-G other links | run | FIRED | g negative real in 10 of 97 counted fits on 11 new links (0.103; line 0.889) | items/27 |
| 28 | CHAIN-WHOLE-03 | skipped | | other worker | |
| 29 | BOWL-HALF outer region | run | NOT FIRED (weak) | circle average: nothing at 1/2 (ratio 1.00); error hinge at 1/2 t = -4.39, but control hinges at 0.2-0.6 give t = -7.33 to -3.69, so 1/2 is not special | items/29 |
| 30 | DIELECTRICS-01 new set | run (38, not 40) | FIRED (literal reading) | 77.0% within 10 degrees of the real axis on 38 new-shelf materials (original 79.7%); line direction ambiguous | items/30 |
| 31 | SILENT-WALLS lopsidedness | could not run | none | no fresh 200 walls (all 575 KnotInfo double walls already used) and no stated rule from Smith-point position | RESULTS |
| 32 | TORUS-ROOTS homotopy | could not run | none | no homotopy solver on disk; item counts ("3 and 4 directions") do not match the registered two values | RESULTS |
| 33 | ONE-PLAQUETTE Fr row | skipped | | needs measurement not on disk | |

## Untested / cautions
- Item 6 (Snell) is deferred for ambiguity only; nothing was run for it.
- Items 2, 3, 5, 8, 12, 13, 16, 25, 26, 27, 29, 30: the family, weights, kinds, links or part-definition were my choice among several readings, written in each script header before the run.
- Item 3 covers only the shape-versus-NPNN half; the level-to-radius half was not run.
- Item 15 and 21 fire by construction (arithmetic and a sign flip) and carry no new information.
- Item 30: the frozen line "below 90%" can be read either way; both readings follow from the number.
- Item 7: full-vector differences (7 of 21) may be chirality of the listed diagrams; only total rank was used for the verdict.
