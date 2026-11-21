# Rhenium gives a direct test of the proposed connection with decay

**HYPOTHESIS, Jeromie's wording.** “The vector determines the direction, that may be decay.” The bare and neutral ions of the *same isotope* supply a comparison, and a second isotope tests what an element-wide vector omits. A nuclear decay rate was not used to fit any ionization energy. [Endpoint protocol](TESTS.md) · [pinned electronic data](../../../../data/element_thresholds_20261011.json.gz)

**MEASURED.** Bosch et al. stored fully stripped ¹⁸⁷Re and observed the growth of hydrogen-like ¹⁸⁷Os by two independent methods. The bare-parent half-life was 32.9(2.0) years. Their neutral reference was about 42 billion years. The 2025 geochemical review uses approximately 41.6 billion years and discusses calibration uncertainty. IAEA's historical ENSDF ground-state value is 4.33×10¹⁰ yr. Each gives the same orders-of-magnitude separation. The emitted electron can occupy an empty bound state of the daughter in this process. [1996 storage-ring measurement](https://doi.org/10.1103/PhysRevLett.77.5190) · [authors' numerical summary](https://wwwmpa.mpa-garching.mpg.de/mpa/publications/proceedings/nucast_1998.pdf) · [2025 review](https://doi.org/10.1093/nsr/nwaf300) · [IAEA](https://nds.iaea.org/relnsd/v1/data?fields=ground_states&nuclides=187re)

**DERIVED / first falsifier.** The neutral-to-bare decay acceleration λ_bare/λ_neutral equals t½,neutral/t½,bare. Bosch's historical comparison gives 42×10⁹/32.9 = **1.2766×10⁹**. Holding that rounded neutral benchmark fixed while varying the bare half-life gives [1.2034,1.3592]×10⁹. For the electronic readout the 74 successive step ratios telescope to IE₇₅/IE₁ = 83162.41/7.83352 = **10616.225**, in the pinned box [10616.045,10616.405]. The rate acceleration exceeds the electronic span by a factor of about **120,250** at the central values. The same scalar cannot be both endpoint readings in this example. There are 75 removal energies and 74 successive ratios; there is no measured removal threshold beyond the bare ion. This tests one literal equality, not every possible vector-based mechanism.

## What the electronic thresholds actually predict

**DERIVED.** Write positive B(Z)=Σₖ IEₖ for the entire binding of the neutral electrons. With nuclear ground states and the same mass units, M_atom c²=M_nuc c²+Zmₑc²−B(Z). The neutral ground-state β⁻ Q is the neutral atomic mass difference. A bare nucleus emitting a *free* electron has Q_free=Q_neutral+B(Re)−B(Os). If the emitted electron instead enters the otherwise bare daughter K shell, add B₁s(Os). An excited daughter nucleus consumes its excitation energy. Rate calculations also require the nuclear matrix element, selection rules, the electron wavefunction and phase space.

```math
Q_K=Q_{\rm neutral}+B(\mathrm{Re})-B(\mathrm{Os})+B_{1s}(\mathrm{Os})
=Q_{\rm neutral}+\sum_{k=1}^{75}IE_k(\mathrm{Re})-\sum_{k=1}^{75}IE_k(\mathrm{Os}).
```

**DERIVED.** In eV the two archived totals are 454144.43352 and 469448.05823. The one-electron Os threshold is 85614.42 eV. The more favorable bound final state adds a *net* 70310.79529 eV to the neutral Q, with rectangular electronic width 2263.71031 eV. The identical last Os binding cancels symbolically before summing errors. A rectangle over quoted inputs is an enclosure under those input ranges, not an experimental confidence interval. Electronic thresholds are element-wide reference values; no isotope-specific electronic correction was introduced.

| Isotope, source of neutral mass difference | Neutral Q, keV | Bare parent, bound electron Q, keV [input box] | Bare parent, free electron Q, keV [input box] |
|---|---:|---:|---:|
| ¹⁸⁵Re, AME2020 | −1013.1393(4190) | −942.829 [−945.512,−940.145] | −1028.443 [−1031.126,−1025.760] |
| ¹⁸⁷Re, AME2020 | +2.4667(16) | +72.777 [70.512,75.043] | −12.837 [−15.103,−10.571] |
| ¹⁸⁷Re, PENTATRAP 2021 | +2.4709(13) | +72.782 [70.516,75.047] | −12.833 [−15.098,−10.567] |

**DERIVED / isotope control.** The identical archive permits the bound-electron ground-state channel for bare ¹⁸⁷Re but closes it even in the most favorable box for bare ¹⁸⁵Re. An electron in any less-bound daughter orbital cannot rescue the latter channel. For ¹⁸⁷Re, neutral continuum β decay is allowed, bare continuum β decay is energetically closed, and a bound channel opens. An element-wide ladder alone gives the same electronic correction to both isotopes; the nuclear mass difference decides their different signs. These are kinematic ground-state limits; we do not identify a measured branching fraction from the sign or equate a Q with an inverse lifetime. [AME2020](https://doi.org/10.1088/1674-1137/abddaf) · [2021 direct mass measurement](https://doi.org/10.1103/PhysRevLett.127.072502) · [nuclear inputs](rhenium_nuclear_inputs.csv) · [every computed box](rhenium_channels.csv)

## A tighter bridge using an ion in the middle of the ladder

**MEASURED and DERIVED.** PENTATRAP measured the charge-29 mass difference with a positive energy release of 2417.4(9) eV in the Re→Os direction. Their neutral mass result adds a multiconfiguration correction of +53.5(1.0) eV for the 29 removed electrons. Define S_q(Z)=Σₖ₌₁ᵠ IEₖ(Z) using positive removal costs. Then Q_neutral = Q_29 + S₂₉(Os)−S₂₉(Re). The pinned central *difference* S₂₉(Os)−S₂₉(Re) is only +32.81471 eV, with a broad rectangular box [−1047.10560,1112.73502] eV. It cannot independently match the 1 eV accuracy of the published correlated calculation.

**DERIVED.** Insert the ionic mass directly instead of first reconstructing the neutral mass. The shared 29-electron correction now cancels exactly. The bridge uses only 46 remaining pairs of removal energies:

```math
Q_K = Q_{29}
 + \sum_{k=30}^{75}\left[IE_k(\mathrm{Re})-IE_k(\mathrm{Os})\right].
```

**DERIVED.** This gives **+72.76101 ± 1.18469 keV** for the K channel, a rectangular span [71.57632,73.94570]. For the continuum the result is **−12.85341 ± 1.18484 keV** after subtracting the 85.61442 keV H-like Os threshold. The width is almost halved because the uncertain 29 outer steps on *both* atoms have been replaced by an independent measured ionic mass difference. Counting the same theoretical 53.5 eV correction twice would hide that improvement. [Direct source, equations and Table I](https://pure.mpg.de/rest/items/item_3336134_1/component/file_3336135/content) · [archive-hash-checked exact-decimal script](isotope_decay.py) · [audit](isotope_decay_audit.txt)

**DERIVED / formal scope.** The Lean file proves the shared endpoint cancellation algebra and selected scaled-integer sign predicates, including exact endpoints from the encoded constants. The Python check constructs the sums from the source-pinned archive and evaluates the hybrid ionic-mass route. The written mass formula states the physical assumptions outside the formal proof. [ReEnergyChecks.lean](ReEnergyChecks.lean) · [Lean 4.34.1 axiom output](re_lean_output.txt)

**MEASURED and DERIVED / the branch that dominates the experiment.** The storage-ring authors explain that most of the bare-ion rate goes to the *first excited nuclear state*, which has a much larger nuclear matrix element than the ground-state transition. IAEA gives ¹⁸⁷Os 1/2⁻ at 0 and 3/2⁻ at 9.756(19) keV. The neutral continuum cannot reach that first excited state: 2.4709−9.756=−7.2851 ±0.0203 keV using the PENTATRAP neutral mass and the rectangular widths. The bare-parent bound-electron route can: 72.76101−9.756=**+63.00501 ±1.20369 keV** using the direct charge-29 bridge. This is why a nuclear channel absent in the neutral atom can dominate in the stripped ion; the larger nuclear matrix element matters as well as the open energy budget. [Storage-ring authors' discussion of the first excited state](https://wwwmpa.mpa-garching.mpg.de/mpa/publications/proceedings/nucast_1998.pdf) · [IAEA levels](https://nds.iaea.org/relnsd/v1/data?fields=levels&nuclides=187os) · [two source rows](osmium_first_levels.csv)

**Historical energy check.** The storage-ring team quoted a K-shell ground-to-ground endpoint of **72.97 keV**, inside the independently reconstructed [71.57632, 73.94570] keV input box. Their L-shell endpoint of **9.07 keV** lies below the 9.756(19)-keV daughter nuclear excitation. Thus their ground-state L channel could open while their first excited-state L channel could not. These are historical electron-shell kinematics, separate from the directly observed half-life. [Storage-ring proceedings, decay scheme and quoted Q values](https://wwwmpa.mpa-garching.mpg.de/mpa/publications/proceedings/nucast_1998.pdf)
