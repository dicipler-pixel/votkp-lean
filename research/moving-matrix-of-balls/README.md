# The Moving Matrix of Balls — Mixer v1 (15 Nov 2026)

Jeromie Beasley, AI-assisted. A live matrix of balls in one ball (series 7 → 49 → 343, VOTKP peel steps),
where one Hermitian matrix H = D + A moves the light (iψ̇ = Hψ), the electron sea (Ṗ = −i[H,P], gapped ground projector),
and the balls (ḋᵢ = Fᵢ × dᵢ), with the energy held on the faces halfway along each link (Non-Normality Is Connection Energy).

Checked on the page (mm_page_check_v1.out.json):
- conserved energy drift ≤ 1.2e-9 after t = 4 (levels 1, 2) and t = 3 (level 3)
- light continuity per ball ≤ 2.2e-16; each ball passes on what it takes (in − out ≤ 4.4e-16)
- NNCE identity at rest: 1.9594443454 = 1.9594443454 (level 1), 26.6433899546 = 26.6433899546 (level 2)
- holonomy = area on every loop (20, 140, 980 loops; worst 1.1e-11)
- clock speed limit τ̇² ≤ 4gS: largest ratio 0.0007
- light arrives before the sea answers at every ball where both arrive: 6/6 (level 1), 42/42 (level 2)

Model choices (not derived): c₀ = 0.5, ball quantum ω = 2, face stiffness κ = 0.25, steps [0.9, 2.7, 6.0].
The sea is not run live at level 3 (686 × 686 projector). Build: `python3 mm_build_v1.py`; check: `node mm_page_check_v1.js`.
