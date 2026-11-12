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
