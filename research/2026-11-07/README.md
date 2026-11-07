# VOTKP research, 7 Nov 2026 (exploratory)

Author: Jeromie Beasley. This is a research-direction pass, not a final test: there are no kill lines. `PATH_NOTES.md` holds the running notes. Every script in `scripts/` starts with a `# SCRIPT:` header.

## Leads tested

| Lead | Script | What came out |
|---|---|---|
| Branch cut, fusion | branch_cut_01*.py | Parallel fusion doubles the signature. Opposed fusion (K # mirror) gives zero at every phase, with an exactly ±-paired spectrum. Tr(P₊Z) recovers K's signature at 400/400 phases. Even records (Alexander, determinant, metric) can't tell the two fusions apart. |
| Branch cut, fission | branch_cut_02.py | The diagonal half L is isotropic for H(ω) at every phase. P₊ sits at exactly 45° to L. |
| Flipping key (the Dzhanibekov intermediate axis) | flip_key_01/02.py | Climb rate = 0.577350, the Connection Energy formula. It is a saddle exactly when the gap product (I_k−I_a)(I_k−I_b) < 0. Bargmann phase = −½ × solid angle; Montgomery's formula reproduced to 1e-8. The memory is a lune, 4·arctan k. It hits 45° when 1/I₂ sits midway between 1/I₁ and 1/I₃. |
| The 494 silent double walls | silent_walls_01.py | Finite concordance order → 65/65 silent. g₄ ≤ 1 → 113/113 silent. 61 infinite-order silent walls are still open. |
| 45° tilt with branch mismatch | tilt_01.py | The lock breaks linearly with the mismatch. The median deviation is 0.57° away from walls, with full swings at walls. |
| P3 Schottky line | optics_01.py | Above \|Γ\|² = ½: metals 35/35, non-metals 0/6 (41 elements). |
| X02 localization integral | optics_01.py | IR slope is nonzero for metals and ~0 for C and Si. Coverage stops before the Drude regime. |
| P1 film phase | film_phase_01.py | 39 bulk-matched metal pairs. The Smith-phase gap predicts the colour split under a film: Spearman ρ = 0.64. |
| 2/3 vacuum line under pressure | pressure_line_01.py | Molecular solids: the squeeze needed to reach 2/3 ranks the measured metallization pressure, rho 0.89 (n=6). Network solids (Si, Ge, B) already sit on the line and need a flip (a structural change), not a squeeze. |
| Geometric vs dynamic turn of the Smith track | geo_phase_01.py | One handedness across all 41 elements. Free-electron metals ride the rim (the ground); there turn and climb merge. |
| Why rim pairs hide their phase under film | film_geo_link_01.py | The film under-reads pairs that both ride the rim: rho -0.52, p 0.0007. |
| Volume of the knot potential, the Jones string as light | knot_volume_01..03.py | Climb (Mahler measure) carries hyperbolic volume, rho 0.85, and adds to log det (R^2 0.71 -> 0.81). Turn (swept area) carries handedness, |signature| rho 0.83. |
| Why element tracks wind one way | handedness_01.py | Every causal model medium winds the same way, through absorption lines too. Likely causality plus passivity (Foster family). |

The optics scripts read the refractiveindex.info database (CC0), cloned locally to `/home/claude/data_ri/ri`; change the path in `ri_load.py` to match your clone.
