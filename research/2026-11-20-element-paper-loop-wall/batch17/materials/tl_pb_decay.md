# The A=205 charge-state test

**HYPOTHESIS / falsifier.** In batch 14, comparing two electronic removal *sums* gave the observed switch of decay direction between the neutral and highly ionized Ho/Dy isobars. Apply exactly that mass comparison to the next pair with an observed reverse decay, ²⁰⁵Pb/²⁰⁵Tl. A positive Pb−Tl ground mass gap up to q=81 or a lack of energy to reach the *observed excited daughter* would invalidate the proposed mapping for this pair.

**MEASURED.** Ground-state neutral ²⁰⁵Pb undergoes electron capture toward ²⁰⁵Tl with an approximately 17-million-year half-life. At GSI in 2024, bare ²⁰⁵Tl⁸¹⁺ ions decayed by bound-state β⁻ emission to ²⁰⁵Pb⁸¹⁺. The half-life extracted from daughter production was 291⁺³³₋₂₇ days. The weak transition overwhelmingly populates the first nuclear excited state of Pb, 2.329(7) keV above ground. The neutral mass-difference energy was evaluated at 50.6(5) keV. [Measured storage-ring decay](https://doi.org/10.1103/PhysRevLett.133.232701) · [2024 analysis, Fig. 1 and Methods Eq. 3](https://doi.org/10.1038/s41586-024-08130-4).

**DERIVED.** With Q(q) = [M(Pb^q+)−M(Tl^q+)]c², start with Q(0) = 50,600 ± 500 eV. For each successive charge append IE(Pb) − IE(Tl), directly from the pinned element archive. The available energy to the excited daughter in the reverse direction is −Q(q)−2,329 eV. Add each quoted threshold width, the baseline width, and when appropriate the 7 eV excitation width to bound the two rectangular comparisons.

| q | Bound electrons Tl / Pb | Q(q), keV | Energy available to excited Pb in reverse direction, keV |
|---:|---:|---:|---:|
| 0 | 81 / 82 | +50.600 ± 0.500 | −52.929 ± 0.507 |
| 79 | 2 / 3 | +37.545 ± 4.549 | −39.874 ± 4.556 |
| 80 | 1 / 2 | −34.300 ± 4.550 | +31.971 ± 4.557 |
| 81 | 0 / 1 | −33.401 ± 4.550 | +31.072 ± 4.557 |

**DERIVED.** Through q=79 every sign box keeps Pb above Tl in ground mass. At q=80 and 81 each box keeps Tl above even the excited Pb daughter in mass. The step at q=79 takes helium-like Tl down to its K-shell vacancy while lithium-like Pb loses its outer electron. It is also precisely at these final two Tl charges that a K shell vacancy is available for bound-state β⁻ decay. All atomic IEs are element-reference thresholds and many are theoretical, so these brackets are sensitivity ranges, not isotope-specific experimental uncertainties. [82 rows](tl_pb_decay.csv) · [Recompute from the pinned archive](tl_pb_decay.py).

**DERIVED / control.** The experimental paper's Methods gives a component-based transition-energy evaluation, using B_K = 101.336(1) keV and the total-binding difference ΔBₑ = 17.338(1) keV. Its electronic contribution is 83.998 keV. Subtracting the neutral energy 50.6 keV and the nuclear excitation 2.329 keV gives 31.069 keV, reported as 31.1(5) keV. The archived electronic contribution is 84.000530 keV, **2.53 eV higher**. Both reconstructions share the neutral energy and nuclear excitation. Their close central energies cannot count as independent mass measurements. The measured daughter accumulation and half-life supply independent evidence for that channel. The wide archive box does not claim few-eV accuracy. Replacing the excited final level by the ground state would overstate the actual channel energy by 2.329 keV.

**DERIVED / centre mapping.** ²⁰⁵Tl has 81 protons and 124 neutrons, net u = 286, d = 329. ²⁰⁵Pb has 82 protons and 123 neutrons, u = 287, d = 328. At fixed isotope a peel preserves the centre; a bound β⁻ transition changes it by (+1,−1) net up/down, emits an electron antineutrino and leaves the newly produced electron in the daughter ion. The mass ordering describes energetic allowance. The rate also depends on nuclear matrix elements, occupation and electronic overlap. [Reference to the matched Ho/Dy test](../../batch14/materials/holmium_dysprosium_decay.md).
