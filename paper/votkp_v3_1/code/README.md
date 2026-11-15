# VOTKP v3.1 — code additions (12 November 2026)

`v31/` holds what was run for Sections 22.5 and 25 of version 3.1 and the scripts that drew Figures 37 and 38 and built the page.
Each check script states, before its run, why the check decides the claim and the condition that would kill it.

- `feed_loop_01.py`, `feed_loop_02.py`, `feed_loop_03.py` with their `.out` files: the loop of two perpendicular steps, its centre of turn and obliqueness, the loop-fed signal, the push on a layer.
- `feed_math.js`, `feed_math_test.js`: the same mathematics as run by the interactive page, tested against the Python.
- `derived_algebra.py`, `h01_real_gamma.py`: the friction weight, the matter-wave step, the echo weight on a real ladder, Propositions 22.1 to 22.3.
- `figs_v31.py`, `build_v31.py`, `shot_v31.py`: figures, page build (from the complete v3.0 page), render check.

`closure_reports/` holds the reports of the reruns and checks made on 12 November: the v2.9 package replay, the rerun of the scripts behind Sections 23 and 24,
the constants of Section 23.4, the Lean source audit, the complete test ledger.

Results graded [Carried] in the paper come from the companion papers, repositories and dated runs named beside them and were not rerun for this version.
The v3.0 additions zip and the v2.9 package remain as issued.
