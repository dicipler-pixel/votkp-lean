# Can the integral over a sphere and the integral over a slab open the wall?

**DERIVED.** In a stable, local, macroscopically isotropic dielectric, let $\chi=\epsilon-1$. For one principal axis of a quasistatic ellipsoid surrounded by vacuum, its response to the external field is proportional to $\chi_n=\chi/(1+n\chi)$, where $n$ is the depolarization factor. Write $M_n=\int_0^\infty\operatorname{Im}\chi_n\,d\omega$. Transverse slab, sphere, and longitudinal slab have $n=0,1/3,1$ respectively. Resta's Eq. (13) relates these areas to clamped-nuclei electronic polarization fluctuations under the corresponding macroscopic boundary conditions. [Resta (2006), Eqs. 8–14](https://arxiv.org/pdf/cond-mat/0512247)

**DERIVED.** Fix $0\le n_1<n_2\le1$ and $d=n_2-n_1$. The identity $\chi_{n_2}=\chi_{n_1}/(1+d\chi_{n_1})$ lets us apply the [passive full-spectrum bound](FULL_SPECTRUM.md) to the auxiliary scalar response $1+d\chi_{n_1}$. Its numerator and loss areas equal $dM_{n_1}$ and $dM_{n_2}$, respectively. Its high-frequency limit is one, and its static value for bare static susceptibility $s=\epsilon_s-1$ equals $(1+n_2s)/(1+n_1s)$. Assume this dressed response and its inverse are causal with the stated dispersion representations and finite nonzero areas. Under these hypotheses,
$$
1<\frac{M_{n_1}}{M_{n_2}}\le
\sqrt{\frac{1+n_2s}{1+n_1s}}.
$$
Even if $\chi(i\xi)\to+\infty$ as $\xi\downarrow0$, each $n_1>0$ gives $\chi_{n_1}(0)=1/n_1$. Thus the same comparison for two positive factors has upper bound $\sqrt{n_2/n_1}$ in a conductor. This argument does not require the bare transverse area to be finite. A single undamped Drude pole attains the conducting upper bound, since the two depolarization resonances are at $\sqrt{n_i}\,\omega_p$. A damped resonance gives a spread of frequencies.

**DERIVED.** For the sphere and longitudinal slab at any finite $s>0$ the squared upper bound $(1+s)/(1+s/3)$ is less than 3. For the conductor limit it is 3. Hence the full sphere/slab ratio never exceeds $\sqrt{3}$ under these hypotheses. Its forward reflection cannot exceed $(\sqrt3-1)/(\sqrt3+1)=2-\sqrt3$, well below the wall reflection $1/\sqrt2$. A genuine ratio above the bound would rule out at least one premise, such as matched states, scalar quasistatic response, common volume normalization, correct sample geometry, or full spectral coverage.

**DERIVED · mainstream-blend watch.** The third here is a classical depolarization factor for an externally driven homogeneous sphere. A spherical depolarization factor is fixed by equal axes and the sum of their three factors being one. Jeromie's projector link cutoff and a Bruggeman mixture's percolation threshold involve separate definitions. None enters this derivation. The comparison here is between boundary responses of the same material. It cannot be identified with transport between two atomic balls without a further physical bridge.

## Four rubidium interpolations fail a necessary passivity check

**MEASURED / DERIVED.** Starting with Smith's 24 measured rubidium index pairs, use $\chi=(n_{\rm opt}+i\kappa)^2-1$ and $\operatorname{Im}\chi_N=\operatorname{Im}\chi/|1+N\chi|^2$ at each frequency. The sphere response is reconstructed from bulk optical data, not directly measured on spheres. Integrate over the observed 0.554–3.967 eV using four declared interpolations because narrow resonances can fall between samples. [Underlying rubidium optical constants and provenance](../../batch8/material_transport/README.md) · [All four reconstructions](depolarization_rb.csv)

**DERIVED, falsifier.** A passive conducting dielectric obeys
$$
  \int_0^\infty\frac{\operatorname{Im}\chi_n(E)}{E}\,dE=\frac{\pi}{2n},\qquad n>0.
$$
This is the zero-frequency dispersion relation with $\chi_n(0)=1/n$ and $\chi_n(\infty)=0$. A positive partial integral above the complete allowance rules out that interpolated response. Positive strength at missing frequencies only increases the discrepancy. An ellipsoidal axis with $n=0.132$ is physically allowed. I selected it after scanning $n$ to look for a counterexample; no prior prediction of the witness value is claimed.

| Interpolation | Sphere / longitudinal window area | Fraction of inverse-moment budget at sphere | Fraction at $n=0.132$ | Verdict |
|---|---:|---:|---:|---|
| Linear response channels | 2.5914 | 1.02189 | 1.04062 | Reject |
| Shape-preserving cubic responses | 2.5594 | 1.01802 | 1.04534 | Reject |
| Linear complex index | 2.4954 | 0.97670 | 1.11327 | Reject |
| Linear complex permittivity | 2.4972 | 0.97256 | 1.12884 | Reject |

**DERIVED.** The same witness rejects all four ways of interpolating across the measured points. None of the four numbers in the ratio column supplies a defensible full-spectrum missing-area estimate for Rb. Combining them mechanically with the $\sqrt3$ cap would give nominal minimum missing fractions of 30.6–33.2%. Those scenario outputs are retained in the CSV with an explicit failed-audit flag; they are not a measurement. Pointwise evaluations at Smith's measured frequencies remain meaningful. A causal fit to the complex data with experimental errors and a sufficiently resolved resonance region would be needed to recover a quantitative missing fraction. [Inverse-moment passivity tests](depolarization_passivity.csv) · [Rejected scenarios](depolarization_rb.csv) · [Reproduction script](depolarization.py)

**MEASURED, independent context.** An earlier electron-loss experiment reported volume-plasmon energy 3.45 eV and additional loss features at 25 and 55 eV in Rb. That establishes spectral features beyond Smith's window; those energies alone give no absolute integrated area. [1966 electron-loss measurement](https://doi.org/10.1103/PhysRev.144.295)
