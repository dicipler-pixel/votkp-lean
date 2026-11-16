# The Series of the Ball — v1 (15 Nov 2026)

Jeromie Beasley, AI-assisted. Built on Light at the Hypersurface, Surprise v1 (z̄ = 3, 5, 7, breathing A = 0.35, the same ball as Mixer v2 Eye A).
Every face of the ball is the end of a ball (a sphere meeting the rim at right angles). The generators carry each end into the next:
6 → 36 → 186 ends, all of one kind. Two ends are joined when they bound the same cell, with strength c₀ sech δ
(δ = 0 crossing or kissing, arccosh(sinh h₁ sinh h₂) apart, r for the two ends of one arm). The moving matrix (MM-MATH-V1) runs on the ends:
light, electron sea (levels 1–2), each end's field, faces; the ends breathe on the page clock and their work is recorded. Eigenvectors shown live.

Checks: t_sr1.js (δ from the drawn spheres vs formula ≤ 5e-13; holonomy = area ≤ 1e-13), t_sr2.js, check_series_v1.out.json:
books ≤ 2e-7 with breathing; light norm ≤ 3e-8; each end in − out ≤ 2e-16; light before sea 5/5 (level 1), 35/35 (level 2).
Model choices: c₀ = 0.5, ω = 2, κ = 0.25, sech δ as the join. Build: `python3 mk_series.py && node build_series.js`.
