# Which oxygen channels discriminate the wall?

**Prospective design for Jeromie Beasley.** The known O III \(4s\,{}^3P^\circ_J\) levels supply three experimental settings. Geometry predicts **inside, inside, outside** in order \(J=0,1,2\). Every one of the six registered midpoint rules predicts **inside, inside, inside**. A separately specified physical observable at \(J=2\) could distinguish them. No independent wall response has been recorded here.

## Positions, calibration and the surviving interval

Set \(z_J=(I_2+E_J/K)/I_1\), using the pinned \(I_1=13.618055(7)\) eV, \(I_2=35.12112(6)\) eV and the shared conversion convention \(K=8065.543937\ {\rm cm}^{-1}/{\rm eV}\). \(E_J\) is the O III excitation above its ground state in inverse centimetres. These channel-conditioned ratios extend the original ground-state peel ledger.

| \(J\) | \(E_J\) (cm⁻¹) | Ratio | Lower edge from \(I_1,I_2\) | Upper edge from \(I_1,I_2\) |
|---:|---:|---:|---:|---:|
| 0 | 356736.30 | 5.826880873182 | 5.826873472117 | 5.826888274255 |
| 1 | 356844.98 | 5.827870339202 | 5.827862937628 | **5.827877740784** |
| 2 | 357117.01 | 5.830347008705 | **5.830339605858** | 5.830354411559 |

North's level check found blank per-level uncertainty fields for these three settings in NIST ASD. The table holds their positions fixed. Given a separately justified symmetric excitation half-width \(d_J\), the edge expressions are

$$
z_J^-=\frac{I_2-\delta I_2+(E_J-d_J)/K}{I_1+\delta I_1},\qquad
z_J^+=\frac{I_2+\delta I_2+(E_J+d_J)/K}{I_1-\delta I_1}.
$$

We recomputed the six frozen cutoffs from the Ag and Si endpoints \(L=7.576234/1.30447\) and \(H=8.15168/1.3895212\). Write \(g(z)=(z-1)/(z+1)\) and \(u(z)=(z-1)/(2\sqrt z)\). For a transformed-coordinate rule, take the named mean in that coordinate and invert back to \(z\).

| Frozen cutoff | \(c\) | \(J=0,1,2\) |
|---|---:|---|
| Geometry \(3+2\sqrt2\) | 5.828427124746 | 001 |
| Arithmetic mean of \(z\) | 5.837220417966 | 000 |
| Geometric mean of \(z\) | 5.837146789467 | 000 |
| Harmonic mean of \(z\) | 5.837073161898 | 000 |
| Arithmetic mean in \(g\) | 5.837094699315 | 000 |
| Arithmetic mean in \(g^2\) | 5.837120689445 | 000 |
| Geometric mean in \(u\) | 5.837120799099 | 000 |

Here 1 means strictly above cutoff. All six cutoffs remain within [5.837006362245…, 5.837286797096…] over the calibrated Ag and Si input rectangles. All exceed the \(J=2\) upper bound at fixed excitation. On the three channels they constitute one alternative prediction pattern.

**What an independent 001 outcome could buy.** Let the physical endpoint and its mapping to the binary class be declared in advance. Every monotone cutoff \(c\) in \([z_1,z_2)\) produces 001. \(J=0\) supplies a control and leaves the bracket unchanged. The left endpoint belongs to the permitted interval under the rule \(z>c\). The following are rounded displays of the exact expressions above.

| Conditional interpretation | Compatible cutoffs | Width |
|---|---|---:|
| Central ratios | [5.827870339202, 5.830347008705) | 0.002476669502 |
| Gives 001 for **every** allowed ground-input setting, fixed levels | [5.827877740784, 5.830339605858) | 0.002461865074 |
| Gives 001 for **some** allowed ground-input setting, fixed levels | [5.827862937628, 5.830354411559) | 0.002491473931 |

The central width \(272.03/(K I_1)\) is **23.6756 times smaller** than the width of the central Ag–Si reference gap. The middle row is an intersection that checks the robustness of a proposed cutoff. If the ground inputs are unknown in their boxes, the last row gives the full possible-threshold set. The two ground energies vary jointly across the whole triplet. The feasible ground rectangle is connected and the conditional intervals overlap. Both the geometry and nearby alternatives remain observationally equivalent inside the interval. Deriving 001 from the tabulated energies alone provides no empirical tightening.

The other three possible deterministic patterns for sorted inputs are 111 when the cutoff lies below the first channel, 011 between the first and second, and 000 at or above the third. The four remaining binary patterns reject every noiseless one-sided monotone cutoff on this ordered triplet. For noisy outcomes, assess these failures with the registered response likelihood. An independent 000 outcome would favour the six midpoint rules over the geometry under that mapping, while leaving the six tied.

Holding the ground widths fixed, the geometric labels survive if each independently established excitation half-width is smaller than its margin: \(169.02266675,\ 60.34266675,\ 210.06133589\ {\rm cm}^{-1}\) respectively (rounded). The script passes the sensitivity test at a common \(60.34\ {\rm cm}^{-1}\). A \(60.35\ {\rm cm}^{-1}\) half-width permits \(J=1\) to cross the wall.

## Preregistering the observable and its likelihood

Choose the same physically justified response for the three channels. Specify preparation, matched excess energy above each channel threshold, spectral tags, their confusion matrix, backgrounds, efficiencies, blinded scoring, acceptance limits and stopping before examining an outcome. Feasibility and calibration data belong in a separate sample. An unresolved multiplet cannot establish three distinct readouts.

For three ordered response categories \(r\in\{\mathrm{low},\mathrm{middle},\mathrm{high}\}\), register an independently calibrated response matrix \(p_{r|b}\) for the proposed binary class \(b\). Require ordered distributions, for example a larger high-bin probability and a smaller low-bin probability when \(b=1\). With conditioned counts \(N_{Jr}\), independent runs and resolved channel labels, the planned log likelihood is

$$
\ell(c)=\sum_{J,r}N_{Jr}\log p_{r|\mathbf1[z_J>c]}+\mathrm{constant}.
$$

Keep the middle category in the likelihood. If “unresolved” denotes instrumental failure, freeze its missingness model separately. When misclassification is material, fold the independently measured tag confusion and differential efficiencies into the likelihood. Correlated acquisition blocks need block-level analysis. Allowing unconstrained \(p_{r|b,J}\) on these same test data erases identifiability. With the common calibrated matrix, only \(J=2\) contributes to the log likelihood ratio between geometry and any midpoint rival. Increasing exposure alone cannot separate the six rivals from each other or determine an exact real-valued cutoff.

**A false positive that passes every pair of the original triplet.** “Outside iff \(J=2\)” gives 001, as does a degeneracy cutoff \(2J+1>3\). Thus its pairwise differences for \((0,1),(0,2),(1,2)\) are \(0,1,1\), exactly the geometry's three contrasts on \(4s\). The known \(4s\,{}^1P^\circ_1\) singlet gives \(z=5.844476033570\), above all seven cutoffs despite \(J=1\). Using the singlet as a control introduces a spin-multiplicity difference.

**Same-spin control.** Use all three \(J\) values of the O III \(3s\), \(4s\) and \(5s\) \({}^3P^\circ\) terms. All nine levels are in the same NBS table.

| \(n\) | \(z_0,z_1,z_2\) | Geometry | Each midpoint rival | \(J=2\) proxy |
|---|---|---|---|---|
| 3 | 5.012241, 5.013319, 5.015658 | 000 | 000 | 001 |
| 4 | 5.826881, 5.827870, 5.830347 | 001 | 000 | 001 |
| 5 | 6.146395, 6.147187, 6.149843 | 111 | 111 | 001 |

Let \(D_n(i,j)=b_{nj}-b_{ni}\). The table enumerates **every** pairwise \(J\) contrast and every pairwise radial comparison. Pure \(J\), pure shell and additive shell-plus-\(J\) effects give zero differences of differences on the chosen additive analysis scale.

| Radial comparison | \(D(0,1)\) | \(D(0,2)\) | \(D(1,2)\) |
|---|---:|---:|---:|
| \(D_4-D_3\), geometry | 0 | +1 | +1 |
| \(D_5-D_4\), geometry | 0 | −1 | −1 |
| \(D_5-D_3\), geometry | 0 | 0 | 0 |
| Any comparison, six rivals or pure \(J\) proxy | 0 | 0 | 0 |

These are differences of model class indicators. For intensities or measured probabilities their sign and scale require a calibrated response-to-class mapping. The nine comparisons reuse cells and are dependent. An angular-momentum effect specific to the \(4s\) shell can still mimic the geometry. Another independently chosen setting or an experimentally justified bound on this interaction is needed to exclude it.

**A kinematic false control that passes all nine states.** At a fixed photon energy \(T\), the answer “channel is still inaccessible” is exactly \(\mathbf1[I_2+E_J/K>T]\). Choosing \(T=I_1w\) returns the geometric classes on every setting by construction. Thus line identity, onset energy and access at one common photon energy cannot distinguish geometry from kinematics. Match the **excess** energy for each channel and score an independently defined endpoint. If that physical endpoint fails its preregistered prediction, retain the failure.

## Reproduction and sources

Run the neighbouring Python file with the pinned October gzip path as its sole required argument. The optional argument --level-width takes a hypothetical excitation half-width in inverse centimetres. It uses exact fractions for energies and ratio limits, 55-digit decimal arithmetic for transformed midpoints, and rejects any input gzip whose SHA-256 differs from 75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c. No lifetime outcomes were consulted.

- [NBS O III energy levels and multiplets, 1985](https://doi.org/10.6028/NBS.NSRDS.3sec11) and [Pettersson's O III spectroscopy, 1982](https://doi.org/10.1088/0031-8949/26/4/007).
- [NIST ASD level-uncertainty guidance](https://physics.nist.gov/PhysRefData/ASD/Html/levelshelp.html) and [oxygen ionization energies](https://physics.nist.gov/cgi-bin/ASD/ie.pl?spectra=O&units=1&unc_out=1).
- [Electron-affinity reference for the Ag and Si calibration endpoints, 2022](https://doi.org/10.1063/5.0080243).
