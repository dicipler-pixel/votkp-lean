# Which 4d opening do the Nb–Rh ladders contain?

**DERIVED.** Each ratio zₖ = IEₖ₊₁/IEₖ involves three successive ground configurations. The first and second changes identify two net occupancy losses. “5s → 4d” means the first loss is 5s and the next loss is 4d. These ground-state thresholds leave the photoionization path, electron correlation and relaxation unresolved.

**Rejection conditions.** A filled 4d opening requires the middle configuration to have ten 4d electrons and then lose a 4d occupancy. A first-open-4d ratio here requires the last 5s loss to precede the first 4d loss. A strictly falling trend requires four successive decreases. A change in which two occupancies are lost and one is gained defeats a single-subshell label.

**MEASURED / EVALUATED.** The supplied ASD ground configurations and terms are spectroscopic assignments. The ASD snapshot preserves the bracketed and parenthesised ionization entries. The checker tested all 215 ASD ground-shell and energy rows for Nb–Rh, expanded each closed-core label, and matched each population to Z−q and each energy to the pin. It also checked 12 Y/Zr context rows and six Pd/Ag applicability rows. Agreement preserves the original experimental, theoretical and semiempirical grades. [NIST ASD, v5.12 (2024)](https://doi.org/10.18434/T4W30F) · [energy archive](https://github.com/dicipler-pixel/votkp-lean/blob/cae5f49/data/element_thresholds_20261011.json.gz)

**DERIVED.** Nb through Rh all give single net occupancy losses along the evaluated ground-state ladders. The fully occupied 4d column is **inapplicable for all five**. Rh has the largest neutral 4d occupancy here, eight.

| Element | Neutral state | Middle state after the last 5s loss | First open 4d (k, z, Γ) | Kr core (k, z, Γ) |
|---|---|---|---|---|
| Nb | [Kr].4d4.5s | [Kr].4d4 | 1, 2.118704, 0.358708 | 5, 2.018259, 0.337366 |
| Mo | [Kr].4d5.5s | [Kr].4d5 | 1, 2.278486, 0.389962 | 6, 1.825416, 0.292140 |
| Tc | [Kr].4d5.5s2 | [Kr].4d5 | 2, 1.936435, 0.318902 | 7, 1.704545, 0.260504 |
| Ru | [Kr].4d7.5s | [Kr].4d7 | 1, 2.277019, 0.389689 | 8, 1.621909, 0.237197 |
| Rh | [Kr].4d8.5s | [Kr].4d8 | 1, 2.423950, 0.415879 | 9, 1.537111, 0.211702 |

**RECOGNISED.** The Kr-core column falls throughout. The first-open-4d column rises, falls, rises and rises. The rank changes between Zr (first-open 4d 1.764661, Kr core 2.334452) and Nb (2.118704, 2.018259). The archive omits uncertainty on Zr IE₂ and Nb IE₂, so the rank observation applies to the central values.

**DERIVED.** The outer change is 5s → 4d, giving bare principal-shell ratio 25/16. The Kr-core opening here is 4d → 4p, giving same-principal-shell ratio 1. All ten ratios lie above their respective bare values and inside the loop wall.

**RECOGNISED.** Holding the *middle occupancy* fixed supplies a further control. Mo and Tc reach pure [Kr]4d⁵ when the last 5s occupancy goes. Ru and Rh reach the same middle occupancy after the 4d⁶ → 4d⁵ step. The latter two ratios compare one 4d removal to another, giving 1.580611 and 1.500000. Nb never passes through a pure 4d⁵ ion. Calling all four ratios a half-filled-shell energy would conflate two incoming channels. To isolate the interaction energy associated with half filling requires a charge- and configuration-controlled background model.

**DERIVED · rearrangement control.** Y in the previous batch gives [Kr]4d5s² → [Kr]5s² → [Kr]4d. The first removal loses a 4d occupancy. The second gives Δn₅ₛ = −2 and Δn₄𝒹 = +1, leaving one fewer electron overall. The checker flags the latter as a rearrangement. Forcing a removal order from the neutral atom alone misses this case. [NIST ASD, yttrium](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=on&biblio=on&e_out=0&el_name_out=on&format=1&level_out=on&seq_out=on&shells_out=on&spectra=Y&unc_out=on&units=1)

**DERIVED · where the filled-4d test starts.** Pd has neutral [Kr]4d¹⁰, so its first ordinary removal already opens that subshell. Its anion has [Kr]4d¹⁰5s, making Pd's k=0 the first 5s-to-filled-4d boundary when anion rungs are admitted. Ag gives the earliest such *ordinary* paired removal, [Kr]4d¹⁰5s → [Kr]4d¹⁰ → [Kr]4d⁹, at k=1. For a column-by-column homologous comparison with Ga–Br, use In–I, whose outer p occupancies run from one to five. Their unsampled ratios are a later test of whether the declining filled-3d series repeats. [NIST Pd](https://physics.nist.gov/cgi-bin/ASD/ie.pl?spectra=Pd&units=1&shells_out=on) · [NIST Ag](https://physics.nist.gov/cgi-bin/ASD/ie.pl?spectra=Ag&units=1&shells_out=on) · [Ning and Lu, 2022, Table 2, Pd anion](https://doi.org/10.1063/5.0080243)

## Reproduction

Run `python3 check_orbitals.py /path/to/data/element_thresholds_20261011.json.gz --csv opening_labels.csv`. The program validates the pinned archive SHA-256, computes exact rational ratios, and exports the occupancy labels for all 210 ordinary pairs. The supplementary ASD snapshot was retrieved on 21 November 2026. To retrieve the same fields, use the [niobium query](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=on&biblio=on&e_out=0&el_name_out=on&format=1&level_out=on&seq_out=on&shells_out=on&spectra=Nb&unc_out=on&units=1) and substitute the element symbol in the spectra parameter.
