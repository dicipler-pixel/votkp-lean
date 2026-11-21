# Rubidium geometry and the boundary-twist control

**Question.** Section 5 of Jeromie Beasley's *The Loop Wall* asks for absolute link weight, shell concentration, and an independent bulk response. This control puts all three on the same bcc torus. Rubidium supplies the ambient bcc geometry and its single outer 5s electron. The orbital hopping is a model parameter. Relating this curvature to measured conductivity requires a calibrated Hamiltonian, units and a transport prescription including relaxation.

**Rejection conditions fixed by the model.** A vanishing thermodynamic half-filled-band curvature defeats its metallic control. A finite thermodynamic curvature of the completely filled isolated lower band defeats the gapped control. A closed nearest-neighbour shell test in either case would defeat this proposed demonstration of two states that both pass the shell test. The finite-size criterion in the script is a tolerance for the selected meshes. The limiting answers also follow analytically.

## Calculation

**DERIVED.** Take a conventional cubic cell of side one with two sites, spin degeneracy two, nearest-neighbour hopping t and onsite energies ±Δ. Write each component of k in [−π,π]. In an orbital-position Bloch gauge the 2 × 2 Hamiltonian has diagonal Δ, −Δ and real off-diagonal

    g(k) = −8t cos(kx/2) cos(ky/2) cos(kz/2),    E± = ±sqrt(Δ²+g²).

One electron per site occupies the lower energy at every k. At Δ=0 this is the half-filled *unfolded* bcc band. The folded bands touch on zone faces. At Δ>0 the lower band fills completely and the direct gap is 2Δ. This use of a doubled cell allows both controls to use exactly the same torus and direction.

**DERIVED.** For a given mesh define fA = ⟨(1−Δ/E+)/2⟩ and B = 2fA(1−fA). For each directed corner-to-body bond d = (±1,±1,±1)/2 evaluate its spin-summed projector weight Xd = 2|⟨−g exp(i k·d)/(2E+)⟩|². Sum all eight weights to get S₁ = Σd Xd/B. The paper's nearest-shell condition is S₁ > 1/3. The separate mean link weight is Σd Xd/8.

**DERIVED.** A boundary twist φ along x shifts kx by φ/L on an L³ conventional-cell torus. With U the total electronic energy, define K = L² U″(φ)/(2L³) evaluated at the chosen background twist. The site count 2L³ cancels spin degeneracy in the corresponding momentum average. All quoted values use t = 1. Compute the derivative at finite L first, with fixed occupations in the metallic case. Then take L to infinity. The shift of each mesh avoids all touching planes. The independent symmetric difference at φ = ±0.01 also stays on the same local branch. The analytic derivative used in the executable is

    K = ⟨g²/(4E+) − Δ²(∂x g)²/E+³⟩.

**DERIVED.** At Δ=0 the integrand reduces to |g|/4 and each one-dimensional average of cos(k/2) equals 2/π. Thus K/t = 16/π³ = 0.51602455. The thermodynamic mean link weight is 32/π⁶ and S₁ = 512/π⁶ = 0.53256267. At Δ>0 the lower energy is a smooth periodic function. Integrating its second derivative over a reciprocal period gives K = 0 exactly. At Δ=0 there is a derivative jump on the folded zone face; the order of limits matters.

## Numerical check

**DERIVED.** Python 3 with NumPy, `python bcc_twist.py`, generates `bcc_twist.csv`. We used L = 8, 16, 32, 64, 96 and three offset meshes per L and Δ. At L=96 the following ranges cover all three meshes. Across all 45 rows the largest absolute discrepancy between the analytic finite-grid curvature and its finite-difference check was 6.74 × 10⁻⁷ t. Near zero the finite difference reaches its floating-point cancellation floor. These ranges reflect mesh sensitivity and carry no experimental uncertainty.

| Δ/t | Mean nearest X at L=96 | S₁ at L=96 | Range of K/t at L=96 | Limiting K/t |
|---:|---:|---:|---:|---:|
| 0 | 0.0332941 | 0.532705 | 0.5160191 to 0.5160937 | 16/π³ |
| 1 | 0.0277012 | 0.678008 | −1.04 × 10⁻¹¹ to +1.59 × 10⁻¹¹ | 0 |
| 4 | 0.0131363 | 0.867579 | magnitude below 1 × 10⁻¹⁶ | 0 |

**RECOGNISED.** The insulating controls concentrate a larger fraction of their decreasing shareable weight on the nearest shell. The boundary response distinguishes the clean metallic model from the gapped controls. No ionization-energy or electron-affinity value was used as a hopping or a face clock. The model does not test a causal role for light or predict the conductivity of a rubidium sample.

Sources: [Beasley, element paper §5 and §7](../../VOTKP_Element_Paper_Loop_Wall_v1_20261121.html) · [Kohn, *Theory of the Insulating State* (1964)](https://doi.org/10.1103/PhysRev.133.A171) · [High-pressure diffraction studies, University of Edinburgh, section on rubidium](https://era.ed.ac.uk/server/api/core/bitstreams/50938791-38ac-4909-a74d-1568d052d0a3/content).
