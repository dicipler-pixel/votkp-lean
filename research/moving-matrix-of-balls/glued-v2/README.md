# The Moving Matrix of Balls, glued at the hypersurface (v2, 15 Nov 2026)

Jeromie Beasley, AI-assisted. Built on Light at the Hypersurface, Surprise v1: the same ball, rays, faces and clock, with the moving matrix
(MM-MATH-V1) put on its cells. 37 balls (centre, 6 neighbours, their 30), glued where they share a face; 36 links, one per shared face.
One matrix H = D + A moves the light, the electron sea and the balls. The faces breathe on the page clock and the work they do is recorded.

Checks (t_glue1.js, check_glue_v2.out.json, check_glue_still_v2.out.json):
- each link's midpoint lies on its shared face: worst 1.4e-14
- glued rest holds zero on every face; connection energy ⅛‖[H,H*]‖² = Σ faces = 0 (1e-28)
- no light, faces still: no ball turns (4e-14)
- books (energy change − work by breathing faces − photons): 7e-10 over τ = 10 with breathing; 4e-9 with faces still
- ball in − out ≤ 1e-16; clock limit τ̇² ≤ 4gS: largest ratio 0.0011
- faces still: light reaches all 36 outer balls before the sea answers (36/36)
- faces breathing (drive depth 0.35): 28/36 — the breathing faces move the sea directly at some balls before the light gets there

Model choices: c₀ = 0.5, ω = 2, κ = 0.25. Build: `python3 mk_app.py && node build_v2.js`.
