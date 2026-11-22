# Independent search for a single atomic rung

**Finding.** The October threshold archive has 5,714 adjacent pairs of ordinary ground-state removal energies. Zero central ratios lie in the open interval between the geometric wall and the frozen raw-ratio midpoint. A single source rectangle overlaps that interval, the francium first-to-second removal. Neither the reference box nor the neutral affinity literature reviewed here resolves an atomic counterclassification.

| Ordinary ground-state subset | Adjacent pairs | Central ratios in interval | Both source widths available | Rectangles intersecting interval |
|---|---:|---:|---:|---:|
| H–At | 3,570 | 0 | 3,548 | 0 |
| Rn–Og | 2,144 | 0 | 2,143 | 1 |
| Total | 5,714 | 0 | 5,691 | 1 |

The October archive includes all 118 atomic numbers but its threshold coverage is incomplete. In Rn–Og, the runner-up by distance to the interval is the Rn helium-core opening, (z=3.9725442693), composed of two theory-grade thresholds. One heavy rectangle lacks an input width (Rn, first-to-second removal). The division of positive endpoints uses the usual oppositely paired source limits, without interpreting them as simultaneous probability statements. S denotes semiempirical and T theoretical. E denotes the archive's evaluated grade. Exact rational comparisons are used for the count, with the upper branch of (z^2-6z+1>0) selected by (z>1).

**Francium.** NIST lists 4.0727411(11) eV for removing the first electron and [22.4] ± 1.9 eV for removing the next electron from the Rn-like cation. The central ratio is 5.4999813271 and the source rectangle is [5.0334636943, 5.9664992118]. For a robust test with (I_1) allowed to vary across its stated interval, the *entire* newly determined (I_2) interval must lie inside (23.73768111, 23.77348109) eV. At the window center the largest permissible symmetric half-width is strictly less than 0.01789999 eV. This is an acquisition target whether or not a future determination lands in the interval. The ratio alone cannot supply an independent observation of a physical change at either wall. [NIST ASD, Fr](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=1&biblio=1&e_out=0&ion_charge_out=1&spectra=francium&unc_out=1&units=1).

**Heavy neutral affinities.** The table `heavy_affinity_screen.csv` lists every Z=86–118, with unresolved cells explicit. Its two target columns are (I_1/c < EA < I_1/w) conditional on the stated central (I_1), and do not themselves represent observations. The availability of each rung requires a bound atomic anion. Th and U have directly measured affinities of 0.607690(60) and 0.31497(9) eV respectively, producing 10.37815 and 19.66552. The 0.17 eV Ra affinity is an AMS-informed estimate. The accelerator bounds EA(Pa), EA(Pu) > 0.05 eV cannot discriminate around their target affinities near 1 eV. A 2025 calculation gives a Pu 7p attachment of 0.63 kcal/mol (0.0273 eV), in tension with the older lower bound. The signs of calculated late-actinide 7p binding can change across models. A one-channel negative energy is insufficient to rule out every alternative anionic state. [Ning and Lu, 2022, Tables 2 and 3](https://doi.org/10.1063/5.0080243) · [Th experiment, 2019](https://doi.org/10.1103/PhysRevLett.123.203002) · [U experiment, 2021](https://doi.org/10.1103/PhysRevA.103.L050801) · [Peterson, 2025, Tables II and III](https://doi.org/10.1063/5.0293868).

**Superheavy theory.** With published paired calculations we obtain EA rungs 9.7539 for Nh, 17.8083 for Mc, 8.8338 for Lv, 4.7778 for Ts, and 111.1 for Og. For Rg, pairing an independently calculated first IE with the 1.565 eV affinity evaluated from theory gives 7.1405. The covariance and a common Hamiltonian are unavailable for this pairing. No usable numerical affinity was assigned here to Rf, Db, Sg, Bh, Hs, Mt, Ds or Cn. Across a further 16 ordinary *theoretical* pairs in Ds, Rg, Cn, Mc, Lv, Ts and Og, the calculated ratios span 1.25377–3.29386. Each pair is separately listed in its original units. A theory result can guide a future measurement; in particular these negative screens cannot rule out every missing heavy-atom threshold. [Ds/Rg/Cn, Table VIII](https://doi.org/10.1103/PhysRevA.101.012514) · [Nh](https://doi.org/10.1088/1361-6455/ac761f) · [Mc/Lv/Ts, Tables I–III](https://doi.org/10.1103/PhysRevA.91.020501) · [Og, Table 5](https://doi.org/10.1016/bs.aiq.2021.05.007) · [alternate Og affinity](https://doi.org/10.1103/PhysRevA.104.012819) · [Lr](https://doi.org/10.1103/PhysRevA.110.022817).

**Reproduction.** From this directory, supply `archive` as the path to `data/element_thresholds_20261011.json.gz`.

```sh
python scan.py "$archive" .
python literature.py "$archive" .
```

The screened bytes have SHA-256 `75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c`. The midpoint used here is exactly ((7.576234/1.30447 + 8.15168/1.3895212)/2), approximately 5.8372204179655185. The wall is (3+2\sqrt2\). `literature.py` preserves each primary input in its publication units and computes the printed ratios from those inputs. Calculated fractional digits in the CSV facilitate re-use and do not improve the scientific precision of the sources.
