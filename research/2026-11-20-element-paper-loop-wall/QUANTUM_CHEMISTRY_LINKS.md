# Quantum-chemistry links for the element paper (21 November 2026)

Three research passes (side agents), each claim checked here before it was recorded. Sources marked
"(from memory)" were not reopened during the search and must be checked before they enter the paper.
Element names and "crossing number" are written in full.

## 1. The anion rung is hardness over electronegativity

- **Derived (Lean `gam_anion_rung`, `omega_eta_wall`).** At the anion rung, Γ₀ = (IE − EA)/(IE + EA).
  This is exactly the Pearson absolute hardness η = (IE − EA)/2 divided by the Mulliken
  electronegativity χ = (IE + EA)/2.
- **Derived.** With Parr's electrophilicity ω = χ²/(2η), we get ω/η = 1/(2Γ₀²). So the loop wall
  Γ₀² = ½ is exactly **electrophilicity = hardness**, and inside the wall means ω > η. Parr's maximum
  electron uptake ΔN_max = χ/η = 1/Γ₀ equals √2 at the wall.
- **Checked** (`checks/check_hardness_electrophilicity_v1.py`): all 44 bound anions from hydrogen to
  caesium agree, with 0 disagreements. Silver has ω/η = 1.0025 (inside) and silicon 0.9954 (outside).
- **Convention check.** This paper computes η = (IE − EA)/2, χ = (IE + EA)/2 and ω = χ²/(2η).
  If a table uses full hardness H = IE − EA = 2η, specify which index accompanies H. Keeping the
  paper’s original ω gives ω/H = 1/2 at the wall. Recomputing the index as Ω = χ²/(2H) instead
  gives Ω/H = 1/4 there, because Ω = ω/2. The corresponding χ/H = 1/√2. The measured input ratio
  and Γ do not depend on these naming conventions. [Half-gap definition, Parr & Pearson (1983)](https://doi.org/10.1021/ja00364a005)
  · [full-gap and index formulas in “The nucleophilicity equalization principle”](https://www.sciencedirect.com/science/article/abs/pii/S2210271X16300287)
- **Prior art.** The quantities are standard. Sources: Parr and Pearson, Journal of the American
  Chemical Society 105, 7512 (1983); Parr, von Szentpály and Liu, Journal of the American Chemical
  Society 121, 1922 (1999); Pal and Chattaraj, Journal of Computational Chemistry 44, 278 (2023).
  No paper was found that uses ω = η, η/χ = 1/√2 or IE/EA = 3 + 2√2 as a threshold. The nearest
  published special ratio is IE/EA = 3: the validity bound in Gázquez and co-workers, and the zero
  of Ayers' nucleofugality.
- **Engineering meaning.** In transmission-line terms z is the standing-wave ratio, and Γ² = ½ is the
  half-power point (3.01 dB return loss, standing-wave ratio 5.83). At the wall, half the power is
  reflected.
- **What the split matches.** It is not metals against nonmetals, not the metalloid or Zintl line, and
  not hard against soft. It is the strong electron attachers: halogens, the chalcogens below oxygen,
  and silver.
- **Prediction for later batches** (the agent's table values, from memory, untested on the archive):
  gold (about 4.0), platinum (about 4.2), iridium (about 5.73) and astatine (about 3.9) inside;
  osmium, bismuth, polonium and lead outside. Gold and platinum form real monatomic anions (aurides,
  platinides). Iridium would sit just inside, a new near-edge case.

## 2. The junction sum rule is the delocalization-index sum rule

- **Prior art (exact mapping).** For an idempotent P:
  - Tr(C_i − C_i²) is the electron-number variance of site i: N(A) − λ(A).
  - ‖P_ij‖² is ½δ(i, j) per spin, minus the covariance of the two site numbers.
  - The sum rule Σ_{j≠i} ‖P_ij‖² = Tr(C_i − C_i²) is N(A) = λ(A) + ½ Σ_B δ(A, B).
  - Sources: Fradera, Austen and Bader (1999); Wiberg (1968); Mayer (1983) (all from memory); and
    Otero-de-la-Roza, Martín Pendás and Johnson, Journal of Chemical Theory and Computation 14, 4699
    (2018).
- **The partition matters.** The model splits orbital space into blocks, as Wiberg and Mayer do;
  quantum theory of atoms in molecules splits real space into basins. The rubidium and krypton
  fractions must state which split was used.
- **The nearest-shell fraction is a new normalisation of a known quantity.** Wuttig and co-workers'
  "electrons shared" map (Advanced Materials 31, 1806280, 2019) uses the nearest-neighbour value
  alone; no source was found that divides by the whole off-site budget.
- **Checked:** the half-filled chain gives a nearest share of 8/π² = 0.8106
  (`checks/check_chemistry_links_v1.py`).
- **Why the insulator scores higher (nearsightedness).** The density matrix decays exponentially in
  insulators and as a power law in metals (Ismail-Beigi and Arias, Physical Review Letters 82, 2127,
  1999). In a metal ‖P‖² falls as r⁻⁴, so each shell carries about r⁻² and much of the weight lies
  past the first shell.
- **The third reading, derived and checked here.**
  - Var(X) = Tr(PX(1 − P)X) = ½ Σ_ij ‖P_ij‖² (x_i − x_j)². Checked to 2e-15.
  - So the localization tensor (Resta and Sorella, Physical Review Letters 82, 370, 1999; Souza,
    Wilkens and Martin, Physical Review B 62, 1666, 2000) is the **second moment** of the same
    off-site weights whose zeroth-moment shell share is the "third".
  - It is finite in insulators and diverges in metals, and through the Souza–Wilkens–Martin sum rule
    it equals the first negative moment of the optical conductivity.
  - It is the ground-state quantum metric (Verma and Queiroz, arXiv:2403.07052): the same object as
    the IQGT.
- **Recommendation.** Report all three readings: the shell fraction, the localization tensor (both
  from P) and the Drude weight (from the Hamiltonian).
- **Eliminating a layer.** Löwdin partitioning, Feshbach projection, self-energies, embedding (density
  matrix embedding theory, dynamical mean-field theory) and the Nakajima–Zwanzig memory kernel are the
  established forms of the spinor-peel elimination. The triangle loop is the chiral quantum walk:
  Zimborás et al., Scientific Reports 3, 2361 (2013); Lu et al., Physical Review A 93, 042302 (2016).
  Odd cycles are needed for time-asymmetric transfer.

## 3. Screening, the spinor (Dirac) term, and chirality

- **All five screening events need the electron's spinor (Dirac) structure.** No spacetime metric is involved; the term comes from describing the electron as a spinor.
  - With a scalar wave alone and an infinitely heavy nucleus, S = 5/8 − 0.157666/Z and σ = 5/8 + 0.037646/Z,
    so S < 5/8 < σ for every element.
  - The crossing of S and σ follows from the leading Dirac term: Z* = (4σ²/α²)^(1/4) = 13.00 for
    σ = 0.617, between aluminium and silicon (checked).
  - σ < 0 (between palladium and silver) needs the spinor (Dirac) gain in the helium-like energy to
    beat the 5Z/8 repulsion; the estimate gives Z ≈ 46.7.
- **Caveat for the paper.** σ at neon is only 2 × 10⁻⁵ above 5/8. Removing nuclear recoil moves the
  "σ passes 5/8" event from neon–sodium to fluorine–neon, so the paper must say the event refers to
  measured, recoil-included energies.
- **Extra event.** The total two-electron binding h + b passes Z² between krypton and rubidium.
- **Chirality (Barron, Chemical Physics Letters 123, 423, 1986).**
  - The screw sign χ is a true-chirality pseudoscalar: odd under mirror, even under time reversal.
  - Γ is the opposite: odd under reversal, even under mirror.
  - Their product has the symmetry of E·B (false chirality). This classification is ours.
- **Measured handedness readouts in tellurium.**
  - Current-induced magnetisation reverses with the crystal hand (Furukawa et al., Nature
    Communications 8, 954, 2017; Physical Review Research 2021).
  - The circularly polarised Raman E1 shift is about −0.5 against +0.6 cm⁻¹ for right- and
    left-handed crystals (Spirito et al., Journal of Materials Chemistry C 12, 2544, 2024).
- **Computed only.** Spin and orbital Hall components reverse between the two hands of selenium and
  tellurium (Xiong et al., arXiv:2605.14506, 2026).
- **Not a clean handedness signal.** The tellurium circular photogalvanic current changes sign with
  wavelength (Ma et al., Nature Communications 13, 5425, 2022).
- **Selenium rings.** The crown Se₈ ring is an unknot (crossing number 0). It is achiral, with local
  χ alternating around the ring, unlike the single-signed helical chain.
- **Crystal-network topology.** Crossing number is used for crystal networks (Andriamanalina, Mahmoudi
  and Evans, arXiv:2506.15252, 2025).
