# s23_s24 rerun report (12 Nov 2026)
All 15 scripts ran. Reruns are in scripts/, round4/, elements/ as *.rerun.out; stored outputs (from the repo) as *.stored.out.
Installs: snappy 3.3.2 (installed), database_knotinfo 2026.9.1 (already present), pyyaml 6.0.3 (already present; pip name "pyyaml" ok), sympy/mpmath/scipy present. refractiveindex.info database cloned to ri/db.
Paths changed (only these): torus_roots_01.py, torus_roots_02.py: sys.path /home/claude/up/vd5/votkp_vacuum_disk_v5/scripts -> /home/claude/closure/s23_s24/vd5 (the vd5 drawing_*.py files taken from repo branch votkp-research-20261107, research/2026-11-07/scripts; the in/ package was not present). plasma_wall_01.py, phase_ladder_02.py: ROOT /home/claude/data_ri_repo/database/data/main -> /home/claude/closure/s23_s24/ri/db/database/data/main. ladder_wall_01, plasma_wall_01, phase_ladder_02: /home/claude/src/votkp-lean/data -> /home/claude/repos/votkp-lean/data. Elements scripts take paths as arguments (rows.json written in elements/). torus_roots_01 needs args 6000 5000 (as in stored run).
| Script | Rerun | Printed | Match |
|---|---|---|---|
| ladder_wall_01 | 8 steps past half line, all at closed cores (Li,Na,K,Rb,Cs + Be+,B2+,C3+ openings); no non-core ones | 8 | yes (output byte-identical to stored) |
| ladder_wall_01 counts | 5737 steps (109 elements), 694 closed-core openings | 5,714 steps, 675 openings | DIFFERENT definitions: printed 5,714/675 are from esr_check_01 (check_esr: adjacent peels 5714, set-count 675 printed OK there); ladder_wall counts elements with >=2 thresholds. The 8 agree in both. |
| iso_cross_03 | one crossing per core; He C3+ 6.080 / N4+ 5.640; Na 9.201/Mg+ 5.330; K 7.286/Ca+ 4.289; Rb 6.533/Sr+ 3.888; Cs 5.947/Ba+ 3.583; Rn line 0 crossings, Fr 5.500 | table | yes, all (Fr 5.50 vs table 5.50) (identical to stored) |
| core_open_02 | per-period past-wall valence [1-4],[1],[1],[1],[1],[] | consistent with 23.2 | yes (identical to stored) |
| element_ball_01 | K1 101/101; K2 shell median 0.4040 vs random 0.2965 (p=1.0, fails); opposite 0.296 vs 0.338 (p 0.98); K3 only Cs on wall (G2 0.5071) | 0.404 vs 0.297; 0.296 vs 0.338; Cs 0.507 | yes (0.2965 prints as 0.297). identical to stored |
| phase_ladder_02 | 1.5/2.0/2.5 eV phases Cs/Rb/K/Na/Li = 56.5/50.0/44.4/31.3/28.5; 78.6/69.1/61.2/42.5/38.4; 100.6/88.8/77.6/52.6/49.2; others max 28.6/39.5/52.0 (Ca); p=2.7e-06 each; even-reading p 0.091/0.099/0.099 | same | yes (identical to stored) |
| plasma_wall_01 | Spearman E_wall vs IE1 +0.057, vs z1 -0.279, vs valence sum +0.261 (n=30; p .77/.135/.164) | +0.06, -0.28, +0.26 | yes (identical to stored) |
| silent_walls_02 | 575 double roots; 81 jump (8+73, all nullity 2); 494 silent = 376 touches (143+233) + 118 opposed; infinite order silent: 45 (nullity 1) + 16 (nullity 2) = 61 | same | yes |
| silent_walls_03 | 376 nullity-1 none in second Alexander; 199 nullity-2 all in it; 0 disagreements | 376 / 199 | yes |
| wall_nilpotent_04 | 198 checked: 121 dims 1 then 2; 77 dims 2 then 2; 0 disagree (377 skipped: Seifert matrix singular or missing) | 198 / 121 / 77 | yes |
| torus_roots_01 | 8_19 PD 11/12 x881; braid 11/12 x579, 2/3 x106; 10_124 PD 14/15 x266, 11/15 x1; braid 14/15 x238, 11/15 x45; no root outside predicted set | same table | yes, counts also identical (seeded solver) |
| torus_roots_02 | kept 8_19 {11/12:209}; 10_124 {14/15:77}; dropped-degenerate has 2/3 x3 for 10_124 filter etc. | (stored) | identical to stored |
| join_k_01 | tr(ab)=2cos(k pi/q) matches, directions match, ALL MATCH for T(3,3..)(q=3,5,7: k=[1],[1,3],[1,3,5]) | claim | yes |
| torus_dirs_03 | arcs ends agree (0 disagreeing); 8_19: 3 arcs, 2 directions {11/12, 2/3}; 10_124: 4 arcs, 2 directions {14/15, 11/15} | predicted sets | yes |
| defect_join_01 | k_inf 1,2,3 = 4sin^2(pi/6,pi/4,pi/3); phi^-2, phi^2 (d=10); (2cos(j pi/7))^2 (d=14); 1/2, 1/4, 1/9 (and phi^2/4, phi^-2/4) no clock value d<=30 | same | yes |
| never_turn_01 | never-turners (hyperbolic) CS-fold range 0..0.132; turners 0..0.2221; verdict INSIDE | inside | yes |
Notes: wall_nilpotent_04 skipped 377 double roots (singular/missing Seifert matrix), consistent with 575-198. In S24.2 table of the paper the torus counts are identical, not merely the same set. Nothing could not run.
