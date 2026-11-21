# Cerium's two optical readouts on the same specimen phases

**MEASURED.** Van der Eb, Kuz'menko and van der Marel measured ellipsometric amplitude and phase on α- and γ-cerium films between 0.8 and 2.5 eV, at 80° incidence. They associate films deposited below 4 K and at about 400 K with α and γ. The four energies below lie within the band in which both angles were measured. The plotted data are the experiment. The longitudinal loss calculated here is a reconstruction from the local scalar optical dielectric response, not a direct electron energy-loss measurement. [2001 article and Fig. 1](https://doi.org/10.1103/PhysRevLett.86.3407) · [Vector figure used in the extraction](https://pure.rug.nl/ws/portalfiles/portal/14529452/infraredandoptical.pdf)

**DERIVED.** At fixed photon energy write the optical readout as $b=\operatorname{Im}\epsilon$ and the screened readout as $s=\operatorname{Im}(-1/\epsilon)=b/|\epsilon|^2$. For positive absorption, comparing two phases at the same energy gives a reversal $b_\alpha>b_\gamma$ and $s_\alpha<s_\gamma$ exactly when

$$
1<\frac{b_\alpha}{b_\gamma}<\frac{|\epsilon_\alpha|^2}{|\epsilon_\gamma|^2}.
$$

An equal or reversed inequality kills this reversal at that energy. Separately, the intra-phase ratio $b/s=|\epsilon|^2$ tests the optical/screened wall; every central cerium row here is above the upper wall. Neither test uses a successive atomic ionization energy.

**DERIVED.** I extracted vector coordinates for the measured open symbols in Fig. 1's lowest panel and inverted its Eq. 1 with $\rho=\tan\psi\, e^{i\Delta}$ and $\epsilon=\sin^2\theta[1+\tan^2\theta((1-\rho)/(1+\rho))^2]$. A second reading uses two different panels of the same figure for $\epsilon_1$ and $\sigma_1$, with $\epsilon_2=\sigma_1/(\epsilon_0\omega)$ in SI. The source has no machine-readable spectral table in the editions checked. The curves in the two editions have the same overall shape. These two readings use the same experiment. [All central values](cerium_screening.csv)

| Photon energy (eV) | Optical α, γ from measured angles | Screened α, γ from measured angles | Ordering from both central readings |
|---:|---:|---:|---|
| 0.85 | 30.51, 25.05 | 0.02808, 0.02803 | Optical α higher. Loss ordering disagrees. |
| 1.05 | 25.42, 17.91 | 0.03299, 0.03737 | Optical α higher, loss γ higher. |
| 1.25 | 18.57, 13.56 | 0.04136, 0.04870 | Optical α higher, loss γ higher. |
| 2.00 | 9.18, 5.67 | 0.08727, 0.11553 | Optical α higher, loss γ higher. |

**DERIVED, reading resolution.** To test the stability of a printed plot, allow ±0.25 PDF points horizontally and vertically for measured-symbol centers, and ±0.56 points for the response curves (about half their drawn width). The script bounds all interpolated values in the horizontal interval before applying the vertical margin, uses interval arithmetic for the ellipsometric inversion, then extrema of (b/(a^2+b^2)) on the resulting box. These are declared figure-reading tolerances, not experimental error bars. The optical ordering survives by either method at all four energies. The three reversed loss orderings survive at symbol-center tolerance. The upper-panel scale compresses $\epsilon_1$ enough that **none of the four loss rankings is resolved by those panels at that tolerance**. At 1.05 eV the symbol-interval gap is only about 0.000069. At 2 eV the two central extractions give α losses of 0.0873 and 0.0624. Absolute loss magnitudes are sensitive to how the figure is read. The discrepancy should stay in the record until numerical spectra or a direct loss experiment resolve it. [All sensitivity ranges](cerium_reading_bounds.csv)

**RECOGNISED.** The three central reversals demonstrate how dielectric screening can change the ordering of two phases in the same element. They do not establish an ordering of frequency-integrated quantum weights, finite-wavevector loss measurements, dc transport or a universal cerium phase rule. [Longitudinal and transverse comparison](SCREENED_OPTICS.md)

Run the following commands against the linked vector PDF. The first script checks its SHA-256 and displayed tick positions.

```sh
python3 cerium_screening.py /path/to/infraredandoptical.pdf
python3 cerium_reading_bounds.py /path/to/infraredandoptical.pdf
```
