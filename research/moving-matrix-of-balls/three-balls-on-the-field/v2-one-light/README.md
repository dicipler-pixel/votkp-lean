# Three Balls on the Field — v2: one light through three balls (15 Nov 2026)

Jeromie Beasley, AI-assisted. Ball B is the same space as ball A seen from one I step out; ball C from one J step out.
The page traces its light once (its own law: step law at each face, a sin²θ conserved, total return past the critical angle) from the
centre of the kicked ball. That one light is drawn in each ball as that ball sees it: every drawn point X goes to G_b⁻¹ G_s X.
No added link strength: the energy handed between balls is the page's own flux × T at each crossing.

Checks (check_three_v2.out.json), on both the Mixer v2 ball and the Surprise v1 ball:
- placed exactly one step out, every crossing out of the kicked ball lies on the next ball's own face: worst 1.8e-15
- B and C moved off their place by 0.3: the crossings miss the face by 0.30 to 0.50
- Surprise ball, kick A: 0.05–0.08 of the light crosses into B and 0.03–0.06 into C (changes as the steps breathe); kick B → A 0.060; kick C → A 0.061, → B (through A) 0.0014
- Mixer v2 ball: its fan of rays points between +I, +J, +K, so a kick in A sends light to B and C; a kick in B or C sends none back toward A

Build: `python3 build_three_v2.py`.
