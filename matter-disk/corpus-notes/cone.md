# "A Measured Lorentzian Cone in Non-Hermitian Quantum Geometry" — v8 (FULL READ of prose; scripts A.1-A.7 read via comments/verdict lines only)

Author: Jeromie Beasley, August 2026, 27 pp. Source: Drive fileId 1ujBiHFtmKGd5xLmiAOz8gkbWPw_HJj9S ("cone_paper_v8 (2).pdf"), read with pdftotext -layout. Nothing truncated. Caveat: the script appendices were skimmed (comments and verdict lines), not line-by-line.

## Model and round-trip form Q
- H = d·σ, d = (kx, ky, m + iγ), m = 0.4, γ = 0.6.
- Eq (1): Q(θ) = M+−(θ) M−+(θ) / (E+ − E−)², M_mn(θ) = ⟨L_m|V(θ)|R_n⟩, V(θ) = cos θ σx + sin θ σy. Q(θ) = a cos²θ + 2b sinθ cosθ + c sin²θ.
- Re Q is the non-Hermitian quantum metric in the biorthogonal convention; the one-way |M−+|² cannot carry a signature.

## Theorem 1 (No metric cone at a Hermitian point)
At any Hermitian point Re Q(θ) = Q(θ) ≥ 0 for all θ. Proof: left and right eigenvectors coincide, so M−+ = M+−*, Q = |M+−|²/(E+−E−)² ≥ 0. Radial scan: (−,−) at small r, (+,+) at intermediate r, Lorentzian (−,+) beyond r ≈ 2, separated by degeneracy walls [V].

## Theorem 2 (Factorization) [T]+[V]
δE+(θ,ω) = (ε²/4) M+− M−+ χ(ω), χ = 1/(Δ−ω) + 1/(Δ+ω); diagonal drive components give no shift. Protocol phase: raw arg[Δ²χ], χ-deconvolved arg[Δ²], full (metric convention) zero.

## Gate GEOWALL-CONE-01
- Points: Lorentzian d=(2.0, 0, 0.4+0.6i); definite non-Hermitian control d=(1.2, 0, 0.4+0.6i); Hermitian control d=(2.0, 0, 0.4). ω = 0.37, 0.61; ε = 2e-3; 4000 steps/period.
- P1: Hermitian formula agreement < 1e-4, positive. P2: Re δE+ spans +5.8e-8 to +8.7e-7, one sign.
- P3: (a,b,c) = (−0.0013, 0.0000, +0.0648); zero pairs predicted and measured: raw 9.452°/170.548°, χ-deconvolved 10.758°/169.242°, metric 7.963°/172.037°, all within 0.5°.
- Factorization at two frequencies agrees at 1e-4; zeros independent of ε over 1e-3 to 4e-3.
- Quote: "Non-Hermiticity is necessary for indefiniteness; indefiniteness, not openness per se, is what carries the cone."

## 4.1 Persistence (GEOWALL-CONE-02)
C(Δ,θ) = Tr[Π(k)Π(k+Δu(θ))], Π = |R+⟩⟨L+|; C = 1 − QΔ² + O(Δ³). Persistence nulls 7.964°/172.038° vs form 7.963°/172.037°. Hermitian match 7e-6. Supra-unity Re C = 1.00000314 at Δ=0.05, θ=0 (timelike).

## 4.2 (GEOWALL-CONE-03)
Random-operator factorization worst error 2e-4 vs bar 1e-3 within |Im Δ|T ≤ 3. Tilted point d=(1.6, 1.2, 0.4+0.6i): (a,b,c) = (+0.0225, −0.0317, +0.0410), nulls 28.907°/44.833°, persistence nulls 28.906°/44.834°, supra-unity Re C = 1.00000314 at θ = 37°. Fourth (decay-rate) quadrature zeros 55.261°/124.739° and 92.131°/161.608°.

## 4.3 Interferometric register [T]+[V]
I+ − I− = |A+C|² − |A−C|² = 4 Re[A e^{−iϕ} B] (2e-15). Plain conjugate mixer (ϕ=0): nulls 10.758°/169.242°; ϕ = arg[(E+−E−)²] = 7.199°: 7.963°/172.037°. A design condition, not a demonstrated device.

## Sec 5 Assembly, as graded
- Horizons force openness: cited [1].
- Openness carries a cone: [V]; absent at Hermitian points [T].
- Restricted dynamics generates a cone: [H].
- Arrow and cone from one skew sector: [C].
- Printed relation QΠ = gΠ + (i/2)ΩΠ (sign "+"), differing from IQGT's g − (i/2)Ω; the paper says "the exact correspondence is deliberately not asserted until derived".
- Three manifestations of persistence, "not one theorem".
- Scope boundary: momentum-space two-band, not spacetime.

## Sec 6 Horizon generator (hyperboloidal Pöschl–Teller)
QNM ladder ω_n = ±sqrt(V0 − 1/4) − i(n + 1/2) to 2e-11; biorthonormality 1e-12. Mirror pair fails the Hermitian control [V]; skew-probe indefiniteness is an artifact class [V]; overtone pair definite at V0=1 with Hermitian probes, "unconverged" [V]/open.

## Open problems (1-5)
Arrow and cone from one construction; real-space reading; many-band; interferometric hardware; the horizon operator (entropy production vs sign of Re Q).

## Claims-and-grades table: 19 rows with [T], [V], [H], [C], cited, [V]/open.
Scripts: GEOWALL-CONE-01/02/03, optical readout, HRZN-02/03, PANELS-CONE. 14 references.
