# Three Balls on the Field — v1 (15 Nov 2026)

Jeromie Beasley, AI-assisted. Three whole Light at the Hypersurface balls on one field: A at the centre, B one peel step out along A's I arm,
C one peel step out along A's J arm. Each ball is the finished page's own ball, unchanged, drawn three times; each is lit by the share of the
energy it holds. One matrix H = D + A (MM-MATH-V1) between the three balls moves the light, the electron sea and each ball's field.
Two pages: on the Mixer v2 ball and on the Surprise v1 ball.

Checks (t_tb1.js, check_three_v1.out.json):
- B–C is the third side of the right triangle: cosh d = cosh r_I cosh r_J (exact)
- loop A→B→C→A: frame turn = triangle area = Thomas turn 2 arctan(Γ_I Γ_J) = 0.7110545751 at τ = 0 (10 digits)
- rest: nothing held on any face; no light and steps held → no ball turns (1e-10)
- kick any ball: light reaches the other two (t ≈ 0.08–0.12) before the sea answers (t ≈ 0.96–1.12); energy drift ≤ 6e-9
- breathing steps: books (change − work − light put in) ≤ 6e-9 in node, 5e-10 on the pages; each ball in − out ≤ 1e-16
- eigenvalues at τ = 0: −1.462 −1.231 −0.307 0.538 0.769 1.693; leading eigenvector shares A 0.381, B 0.345, C 0.274; margin 0.864

Model choices: c₀ = 0.5, ω = 2, κ = 0.25. Drawing convention: ball centres are placed so each ball's rim passes through the cap vertex on the shared arm.
Build: `python3 build_three_v1.py`.
