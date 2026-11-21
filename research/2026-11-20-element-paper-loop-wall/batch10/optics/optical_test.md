# Five bulk optical responses and a cadmium polarization control

**HYPOTHESIS — test before comparison.** If a single scalar atomic peel ladder fixes the entire optical response of an elemental wall, a fixed single crystal must have identical principal optical responses at the same wavelength. A reproducible polarization splitting at fixed composition, wavelength and temperature falsifies that scalar prediction. The broader ball model permits directional ports. A comparison of its predicted splitting needs an optical response assigned to each direction before fitting the data.

**MEASURED inputs; DERIVED last two columns.** The complex optical constants are reported for experimental samples. For a principal polarization at a flat, semi-infinite, nonmagnetic surface adjoining vacuum, put N = n + iκ. The vacuum reflectance is R = ((1−n)²+κ²)/((1+n)²+κ²). Bulk intensity decays to 1/e over ℓ = λ₀/(4πκ). The palladium and silver optical constants were inferred from films. Using them here in the semi-infinite expression removes film interference from the calculation. The displayed digits in the derived column describe arithmetic and do not establish the experimental uncertainty.

| Element, sample | Vacuum wavelength (nm) | n | κ | R | ℓ (nm) |
|---|---:|---:|---:|---:|---:|
| Palladium, Johnson–Christy | 582.0 | 1.68 | 4.02 | 0.712117 | 11.520918 |
| Silver, Johnson–Christy | 582.1 | 0.05 | 3.858 | 0.987490 | 12.006751 |
| Cadmium, basal plane | 580 | 1.6193 | 4.5080 | 0.761717 | 10.238450 |
| Cadmium, optic axis | 580 | 1.5736 | 3.7049 | 0.690688 | 12.457808 |
| Indium, 295 K | 600 | 0.795 | 5.02 | 0.888117 | 9.511252 |
| Metallic white tin, 293 K | 730 | 2.16 | 6.35 | 0.828258 | 9.148276 |

**DERIVED.** The two cadmium channels differ by 0.071029 in surface reflectance and 2.21936 nm in attenuation length. They share the same free-atom peel ladder. Their polarization dependence gives a directly checkable target for a directional wall model. A single unpolarized response would discard this information. The diagonal tensor components remain unchanged when the sign convention of either axis is reversed, so this experiment supplies no signed chirality observable.

**DERIVED — matched interface.** For two regions with the same complex index in the same orientation and eigenpolarization, (N−N)/(N+N) = 0 even when κ is positive and the intensity attenuation length is finite. In the table the boundary is vacuum–metal. In the matched control both sides are the same material. A bulk penetration distance requires a propagation law in addition to any junction clock. No grey-tin spectrum or arbitrary-orientation tensor fit has been substituted.

**Reproduction.** Run `python optics.py` in this directory. Both principal polarizations have 17 paired cadmium wavelengths. The other 39 measured input rows give a total of 73. Tin begins at 730 nm in this source. The wavelength sets differ by paper.

Sources: [palladium, Johnson & Christy 1974](https://doi.org/10.1103/PhysRevB.9.5056), [silver, Johnson & Christy 1972](https://doi.org/10.1103/PhysRevB.6.4370), [cadmium tabulation, AIP Handbook, Table 6g-1](https://web.mit.edu/8.13/8.13c/references-fall/aip/aip-handbook-section6g.pdf), [single-crystal cadmium polarization experiment](https://doi.org/10.1088/0370-1328/83/6/320), [indium, 1967](https://www.jetp.ras.ru/cgi-bin/dn/e_024_06_1093.pdf), [tin, 1964](https://www.jetp.ras.ru/cgi-bin/dn/e_019_02_0310.pdf). Numerical transcriptions for palladium, silver, indium and tin can also be checked in the [Polyanskiy optical constants database](https://github.com/polyanskiy/refractiveindex.info-database/tree/master/database/data/main).
