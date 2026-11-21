# When peeling changes the accessible decay direction

**HYPOTHESIS (Jeromie Beasley).** “The vector determines the direction, that may be decay.” This is testable in the element batch without equating the sign of Γ on a single peel to a nuclear decay rate. Fix the isobars holmium-163 and dysprosium-163, compare their *ground-state masses at identical ionic charge*, and ask whether their ordering reverses along the two complete ladders. A positive gap all the way to the bare-Dy endpoint would fail to reproduce the observed reverse decay. A higher-accuracy independent mass gap of opposite sign at q=56 or q=57 would falsify the proposed bracket.

**MEASURED.** The neutral parent ¹⁶³Ho undergoes electron capture to ¹⁶³Dy. A 2024 Penning-trap study used three charge states together with atomic-structure calculations to infer a neutral mass difference corresponding to 2863.2 ± 0.6 eV in energy units. The opposite direction was actually observed in bare ions. In 1992 a storage ring accumulated hydrogen-like daughter ¹⁶³Ho⁶⁶⁺ from bare ¹⁶³Dy⁶⁶⁺ through bound-state β⁻ decay, with a half-life of about 47 days. The created electron occupies a daughter bound state. The two experiments have different electronic occupations and specify the direction at each end. [Schweiger et al., 2024](https://doi.org/10.1038/s41567-024-02461-9) · [Jung et al., 1992](https://doi.org/10.1103/PhysRevLett.69.2164) · [2026 evaluation of bare-ion decay](https://doi.org/10.1140/epja/s10050-026-01846-z).

**DERIVED.** Write Q(q) = [M(¹⁶³Ho^q+) − M(¹⁶³Dy^q+)]c². For either element, M(q)c² = M(0)c² − q mₑc² + Σₖ₌₁^q IEₖ. Equal charge cancels the missing-electron rest masses. The recurrence is therefore

$$
Q(q+1)=Q(q)+IE_{q+1}(\mathrm{Ho})-IE_{q+1}(\mathrm{Dy}).
$$

Positive Q(q) allows energy release in the Ho→Dy electron-capture direction if the necessary population, overlap and transition rules allow it. Negative Q(q) allows release for the reverse ground-mass comparison. Successive ionization energies are element-reference data, mostly theoretical in this charge range. They do not resolve isotope and hyperfine shifts for a specific stored ion. We summed *energies*, not log ratios, and added each printed uncertainty once for the entire independent-input box. It is not a confidence interval.

| Charge q | Bound electrons Ho / Dy | Q using the archive (keV) | Full input box (keV) | 2024 q=40-anchored comparison (keV) |
|---:|---:|---:|---:|---:|
| 0 | 67 / 66 | +2.8632 | [2.8626, 2.8638] | — |
| 56 | 11 / 10 | +1.9514 | [1.2802, 2.6226] | +1.9185 [1.7832, 2.0538] |
| 57 | 10 / 9 | −4.5186 | [−5.1998, −3.8374] | −4.5515 [−4.6968, −4.4062] |
| 65 | 2 / 1 | −50.4555 | [−51.2680, −49.6430] | −50.4884 [−50.7650, −50.2118] |
| 66 | 1 / 0 | −49.7563 | [−50.5690, −48.9436] | −49.7892 [−50.0661, −49.5124] |

**DERIVED.** The 67 comparisons have one sign crossing. Through q=56 every lower endpoint is positive. From q=57 through q=66 every upper endpoint is negative. At q=56 Dy already has a neon-like ten-electron core. Its next removal costs 12,081(5) eV, while Ho removes its last 3s electron at 5,611(5) eV. The same-charge energy gap therefore changes by **−6,470 eV** in that step. At q=64→65 Dy opens its helium-like core before Ho, taking the gap much farther negative. Single-atom Γ is positive on the central value of every forward ordinary Dy and Ho step here. Its sign alone cannot read the isobar crossing. [All 67 rows](ho_dy_decay.csv) · [Reproduce from the charge-keyed ASD table](ho_dy_decay.py) · [Peel and orbital assignments](../ladder/asd_states_20261121.csv).

**MEASURED / DERIVED comparison.** Table 1 in the 2024 study gives neutral-to-ion *differential binding corrections* ΔB = Q(0)−Q(q) of 37.4(1.4), 1147.3(0.7) and 1115.7(0.7) eV at q=38, 39 and 40. The raw ladder differences at these three charges are 5.394, 1113.794 and 1082.794 eV. They miss the atomic-structure determinations by −32.006, −33.506 and −32.906 eV. Their increments closely track the published increments despite that common offset. The second estimate in the table restarts at q=40 from 2863.2−1115.7 = 1747.5 eV, then applies the remaining archive steps. It avoids carrying the many low-q uncertainty widths a second time and keeps the same sign bracket. The bound includes the full 0.6 and 0.7 eV widths. This anchor and the neutral estimate share source information. [Penning-trap analysis and electronic binding components, Tables 1–2](https://doi.org/10.1038/s41567-024-02461-9).

**DERIVED / centre mapping.** Ho-163 has 67 protons, 96 neutrons, net u = 230 and d = 259. Dy-163 has 66 protons, 97 neutrons, u = 229 and d = 260. Each single electronic removal preserves its own centre's counts. Capture converts one proton to a neutron and emits an electron neutrino. Bound-state β⁻ reverses the nuclear conversion and emits an electron antineutrino. Ionization thus provides a known, quantitatively testable connection between changing the electronic wall and energetically selecting which nuclear channel is available.

**Set aside, with why.** The q=56/57 result is a ground-mass prediction using the stated energy inputs. The study does not measure either intermediate decay or predict its half-life. Daughter excitation, vacancy overlap, selection rules, recoil and initial-state preparation matter when using this sign to predict a resolved physical channel. A lifetime measurement cannot be inferred from the algebra or from the size of a single reflection.
