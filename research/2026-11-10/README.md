# VOTKP research, 10 Nov 2026

Author: Jeromie Beasley. Prepared with AI assistance (Claude, Anthropic). Continues `research/2026-11-07`.

The session read the papers in full (IQGT, Dirac Time v3.1, vacuum disk v1.2 and v5, VOTKP v2.0, Two Trees v4, Non-Normality v15 with the v16 corrections, What the Present Must Keep v1.1, One Tree One Ball, Two Trees One Scale, BallJoins), then tested the open questions. Every script starts with a `# SCRIPT:` header and states its kill line before the result.

## Start here
- `Recoveries_20261110_v1.html` — results already in one paper that answer an open question in another.
- `OPEN_QUESTIONS_TESTS_VOTKP_20261110_v3.md` — every test, its kill line and its numbers.
- `PIECING_MAP_VOTKP_DIRAC_TREES_DISK_COLOUR_20261110_v2.md` — how VOTKP, Dirac Time, Two Trees, the vacuum disk and colour join.

## What came out

| Question | Script | Result |
|---|---|---|
| Missing torus roots (vacuum disk open 1) | torus_roots_01/02 | Predicted from Dirac Time arcs, direction -k^2/(pq): 8_19 {11/12, 2/3}, 10_124 {14/15, 11/15}. Both new roots found; none outside the sets. |
| Silent double walls (VOTKP Table 6, open 6) | silent_walls_02/03, wall_nilpotent_04 | Two kinds: 376 touches (one Jordan block) and 118 opposed crossings. 575/575 by the second Alexander polynomial, 198/198 on Seifert matrices. |
| One k in three papers | join_k_01, torus_dirs_03 | tr(ab) = 2cos(k pi/q), direction -k^2/(pq), arc end k/(2pq). |
| Commutator limit values (Two Trees open 4) | defect_join_01 | k = 2 - tr[a,b] is the UPG defect; the m = 1 limits are clock-and-shift defects, d = 3, 4, 6, 10, 14. m > 1 open. |
| Never-turning knots (Two Trees open 3) | never_turn_01..05 | Census extended to 9 crossings; three families held on new knots; no single rule. Direction does not separate them. |
| Bowl at one half | bowl_half_01 | No feature in the bowl; 99.7% of knot tetrahedra inside the line. |
| Dielectrics on the disk (open 4) | dielectrics_01 | 91 of 94 inside; mostly on the real diameter; 17 absorbing compounds enter in two dimensions. |
| Twin chain turning (Two Trees, One Scale) | chain_turn_01/02, chain_whole_03 | No order beyond one step; a one-step hand in the signed turn. |

## Folders
- `records/` read records 01-09, handoff notes, coverage record.
- `scripts/`, `outputs/` every script and the long-run outputs.
- `equation-file-entries/` what failed, with its failure condition, for the master equation file.
- `BallJoins.lean` as attached on 10 Nov (J1-J8).

Needs: snappy, database_knotinfo, sympy, mpmath, scipy; `dielectrics_01.py` reads a local clone of the refractiveindex.info database; the torus scripts import the vacuum-disk v5 scripts.
