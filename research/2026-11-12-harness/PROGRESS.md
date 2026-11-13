2026-11-12 09:10 lead: board opened, 6 tasks; T1 running
2026-11-12 09:20 lead: T2-T6 workers started
2026-11-12 T3_cap_fill: kill lines and derivation written in STATE.md before runs
2026-11-12 T4 triage done, starting item 1
2026-11-12 T5_band_mean: read done, kill lines written, running S1
2026-11-12 T5_band_mean: S1 k(z) PASS (8e-25)
2026-11-12 T5_band_mean: DONE. REPORT.md written (k(z) PASS; exit identity G0^2+G1^2=1/2)
2026-11-12 09:27 lead: T5 done - band mean 2 <=> G0^2+G1^2=1/2 at the band ends; k(z) closed form
2026-11-12 T3_cap_fill: A and B killed (K-A,K-B), K-0 holds; law E kill line written in STATE before run
2026-11-12 T3_cap_fill: REPORT.md written; A, B, E killed; zero-slack class holds
2026-11-12 09:38 lead: T3 done - laws A,B,E killed; proven bound and never-reach class hold; T3b started on the three-gap word
2026-11-12 T3b_cap_word: kill line F1 (necessary-window lower envelope) written; about to run
2026-11-12 T3b_cap_word: done; F1 lower envelope proven but killed 110/330; F5,F6 killed; REPORT.md written
2026-11-12 09:45 lead: T3b done - lower bound F1 proven (0/330 violations), F1/F5/F6 killed as exact laws; fill law parked as open with two-sided bounds
2026-11-12 T4: items 1-5,2,17,15,16,14,13,12,11,3,10 run; continuing with 9
2026-11-12 T4: items 9,20,21,25,26,30,22 done; next 23
2026-11-12 14:45 lead: 5-hour limit stopped T1,T4,T6 at ~09:50; reset passed; all three resumed from state files; T2 resumed
2026-11-12 T4: items 23,24 not runnable; 27,29 done; next 31
2026-11-12 T4 done: 24 run (13 fired, 11 not fired), 5 could not run, 4 skipped; REPORT.md written
2026-11-12 14:55 lead: T4 done - 24 opposites run, 13 fired, 11 not fired
2026-11-12 knot_v29: all 28 scripts rerun; 11/12-crossing scan matches stored rows; pair count 353 vs paper 354 (see REPORT.md)
2026-11-12 15:12 lead: T1 done - knot side reproduces; pair count 353/251 vs printed 354/253
2026-11-12 T6_lean: toolchain from GitHub OK; cache.mathlib.org 403; narrow closure built; NewProps.lean compiles (43 theorems, no sorry)
2026-11-12 15:40 lead: T6 done - NewProps.lean 43 theorems compile; T7 started on full build
2026-11-12T21:55Z T7: Mathlib build 4253/8884 jobs, ~1h in, no errors
2026-11-12T22:41Z T7: Mathlib build 6199/8918, ~2h in, no errors
2026-11-12T23:32Z T7: Mathlib 7708/8923, cut off, restarted
2026-11-12 T2: done, 1e9 reached, 12.2695 deg, kill line fired (0.197>0.1)
2026-11-12 18:25 lead: T2 done - twin-chain turn 12.2695 deg at 1e9, not settled; axis settled
2026-11-13T01:07Z T7: Mathlib FULL built (8923 jobs, EXIT 0). next: lake build project
DONE 2026-11-13T01:26Z: Mathlib 8923 jobs, project 8942 jobs OK, verify 140 thm/15 controls OK, two-trees 159 thm OK. REPORT.md written.
2026-11-12 19:30 lead: T7 done - full Lean build passes: 140 theorems + 15 false controls, two-trees 159; all board tasks done
2026-11-12 T8 step1 done: lambda closed in chi (tanh(lambda/8)=sinh chi), not proportional; real arm angle past wall pinned at pi/2. next: step 2-3
2026-11-12 T8 steps 2-3 done: gap/depth rates equal at exactly one z*=6.2691276608523 (cubic: y^3-4y-2=0, y=z^(1/4)+z^(-1/4)); next: step 4 length reading
2026-11-12 T8 step4 done: in length both decay as e^-2L (e-fold 1/2); per-pass lengths equal only at z*. next: step 5 data search
2026-11-12 20:05 lead: v3.3 built and pushed (paper/votkp_v3_3); T8 running
2026-11-12 T8 step5 done: no lattice/nn table on disk; metallic-radius proxy only passes the wall filter for 6 elements (<25 registered) -> untested. next: REPORT.md
2026-11-12 T8 DONE: REPORT.md written
2026-11-12 20:15 lead: T8 done - gap and decay share the law e^(-2L); steps equal only at z*=6.26913 (y^3-4y-2=0)
2026-11-12 20:25 lead: T9 (lattice data) and T10 (tree arms, two-ball joins) started
2026-11-12 T9_lattice: registered R1-R4 written in STATE.md before computing
2026-11-12 T10_arms: conventions read (PeelTrees.lean:45,88,235; paper l.167: ln7 uses 6 axes, not LPS-8); step 1 kill lines written
2026-11-12 T9_lattice: table built (84 elements, 65 with CN); IE cross-check 0 disagreements (same NIST source)
2026-11-12 T9_lattice: R1-R4 run (s2_out.txt)
2026-11-12 T9_lattice: REPORT.md done (R1 met, R2 artefact-flagged, R3 meaningless n=5, R4 met)
2026-11-12 20:32 lead: T9 done - past the wall = the five alkalis, all bcc; R2 artefact; level carries absolute spacing (-0.789)
2026-11-12 T10_arms: DONE - REPORT.md (arms: 5 oct/6, 7 cube/8 only in LPS-8 not his six-axis ln7, 11 NOT cuboctahedron in parity form (a=3 shell only), 13 = 6+14; depth-2 no lattice shells; (5,7) join impossible; B99 triple in paper s8.7)
2026-11-12 20:45 lead: T10 done - arms: 5 octahedron, 13 = 6+8, 11 not cuboctahedron in his form; integer pairs across wall only (5,7),(4,11)
2026-11-12 20:55 lead: T11 (many-ball assembly, exploration) and T12 (sharper data lines) started
2026-11-12 T11_many_balls: step1 done - 6 axes->sc, 8 diag->bcc, 12 face->fcc close under every rule; 14-set (axes+diagonals) rank 4 no lattice unless d_diag/d_axis=sqrt3/2
2026-11-12 T12_lattice_sharper: table built (lattice_table_ext.csv), lines S1-S5 + A1-A3 registered in STATE.md before running
2026-11-12 T11_many_balls: step2 done - rule b contacts reproduce rock-salt/CsCl/ZnS closing ratios sqrt2-1, sqrt3-1, sqrt6/2-1 (classical numbers, structural); no rational pair hits exactly
2026-11-12 T12_lattice_sharper DONE: S5 met (-0.461); S1-S4 not met (level IE1 beats peel shape on resistivity/melting); REPORT.md in workers/T12_lattice_sharper
2026-11-12 21:05 lead: T12 done - S5 met (shape adds to spacing beyond level, -0.461); S1-S4 not met in this setup
2026-11-12 T11_many_balls: step3 closed forms (z for theta=60,72,90,120,180 ...), C1 element test not met; step4: omega=90 at golden-ratio z, W^m=I at crystal-angle z, wall changes kind of holonomy not size
2026-11-12 T11_many_balls: step5 done - pressure balance P1+P2=1 has one integer solution: z=3,n=m=1 (K=2); pushes-equal trivial only
2026-11-12 T11_many_balls: DONE - REPORT.md (sc/bcc/fcc close per arm set, 13-set rank 4; rock-salt/CsCl/ZnS closing ratios; special z for theta=60..180; omega=90 at golden z; pressure balance only z=3 n=m=1)
2026-11-12 21:20 lead: T11 done - assemblies, special turn steps (wall = full turn), square defect changes kind at the wall, P1+P2=1 only at z=3
