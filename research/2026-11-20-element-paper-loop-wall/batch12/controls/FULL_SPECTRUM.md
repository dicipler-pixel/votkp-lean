# What the entire optical and loss spectra can do

**DERIVED.** Screening can reverse the two intensities at a chosen photon energy. On integrating the full spectrum, passivity constrains the result. Let $T=\int_0^\infty\operatorname{Im}\epsilon(\omega)\,d\omega$ and $L=\int_0^\infty\operatorname{Im}[-1/\epsilon(\omega)]\,d\omega$. For a scalar stable passive dielectric with $\epsilon(\infty)=1$, finite $1<\epsilon_s=\epsilon(0)<\infty$, finite nonzero $T$, and the unsubtracted causal dispersion representations for both channels,
$$
1<T/L\le\sqrt{\epsilon_s}.
$$
Angular frequency can be replaced throughout by photon energy in the ratio. A metal with a free Drude pole fails the finite-static-response hypothesis. A truncated fit with a constant optical background greater than one fails the high-frequency normalization. Anisotropic tensor inversion, finite-wavevector loss and ionic versus purely electronic response require matching channels and are outside this scalar derivation. This compares two responses of the material in three dimensions. It places no restriction on the atom's ionization ladder. [Dispersion relations for the direct and inverse dielectric response, §3.2](https://www.pi1.uni-stuttgart.de/img/head_of_institute/DresselGruner.pdf) · [Onishi and Fu (2025), §§III–IV, optical and screened spectral weights](https://doi.org/10.1103/PhysRevResearch.7.023158)

## Derivation

**DERIVED.** Put $a(\xi)=\epsilon(i\xi)-1$ and $f(u)=u/(1+u)$. For positive frequencies let $b(\omega)=\operatorname{Im}\epsilon(\omega)$ and $\ell(\omega)=\operatorname{Im}[-1/\epsilon(\omega)]$. The imaginary-axis dispersion relations give
$$
a(\xi)=\frac{2}{\pi}\int_0^\infty\frac{\omega b(\omega)}{\omega^2+\xi^2}\,d\omega,\qquad
f(a(\xi))=1-\frac{1}{\epsilon(i\xi)}
=\frac{2}{\pi}\int_0^\infty\frac{\omega\ell(\omega)}{\omega^2+\xi^2}\,d\omega .
$$
Delta functions may be read as positive measures. The kernels and spectral weights are nonnegative. Interchanging integrals and integrating the kernel in $\xi$ gives $T=\int_0^\infty a(\xi)d\xi$ and $L=\int_0^\infty f(a(\xi))d\xi$. Their difference is the integral of $a^2/(1+a)$, strictly positive for a nonzero response.

**DERIVED.** Set $s=\epsilon_s-1$ and normalize the static response into a probability measure $d\mu(\omega)=2b(\omega)d\omega/(\pi s\omega)$. Then $a(\xi)$ is the $\mu$-mean of $x_\omega=s\omega^2/(\omega^2+\xi^2)$. The concavity estimate used here follows directly from
$$
 f(m)+\frac{x-m}{(1+m)^2}-f(x)
 =\frac{(x-m)^2}{(1+x)(1+m)^2}\quad(x,m\ge0).
$$
Average at $m=a(\xi)$. The linear term vanishes, so $f(a(\xi))\ge\int f(x_\omega)d\mu(\omega)$. Integrating in $\xi$ and using
$$
 \int_0^\infty\frac{s\omega^2}{(1+s)\omega^2+\xi^2}\,d\xi
 =\frac{\pi s\omega}{2\sqrt{1+s}}
$$
gives $L\ge T/\sqrt{\epsilon_s}$. The right-hand equality requires a single positive transverse resonance frequency, up to spectral sets of zero weight. The exact gap in this concavity step is the displayed nonnegative weighted variance averaged on the imaginary axis.

**DERIVED, sharpness controls.** One undamped Lorentz resonance attains the upper bound. At the same static $\epsilon_s=36$, one resonance gives $T/L=6$ outside the wall, while two separated resonances in the supplied control give $2.303230$ or $1.171965$ inside. An arbitrarily small distance from the lower limit 1 is possible at any fixed $\epsilon_s>1$: put static share $\delta$ at frequency 1 and $1-\delta$ at $\delta^2$. The high-frequency term alone contributes $L_{\rm high}=T_{\rm high}/\sqrt{1+s\delta}$. Since $f$ increases, $L\ge L_{\rm high}$, hence $T/L\le[1+(1-\delta)\delta]\sqrt{1+s\delta}\to1$. Static permittivity above threshold is necessary for an open upper wall and does not suffice to guarantee one.

**DERIVED, optional moment check.** For $-1<p<1$ let $T_p=\int\omega^p b\,d\omega$ and $L_p=\int\omega^p\ell\,d\omega$, assuming finite moments. Multiply the preceding imaginary-axis integrals by $\xi^p$. The elementary kernel integral gives the same common factor $\sec(\pi p/2)$ for both channels. Scaling $\xi$ in the concavity step now gives $1<T_p/L_p\le\epsilon_s^{(1-p)/2}$. At $p=-1$ the static dispersion relations directly give $T_{-1}/L_{-1}=\epsilon_s$. At $p=1$ the conventional finite oscillator-strength sum gives equality when the two response functions have the same high-frequency coefficient. Our finite-resonance controls test these two endpoints directly. The main experimental comparison uses $p=0$. [Source for the common frequency-weighted sum rules, §3.2](https://www.pi1.uni-stuttgart.de/img/head_of_institute/DresselGruner.pdf)

## The 122 K krypton test

**DERIVED, conditions.** The full integral is always on the forward side of match. Its reflection is bounded above by $(\sqrt{\epsilon_s}-1)/(\sqrt{\epsilon_s}+1)$. Thus an upper-wall opening requires $\epsilon_s>(3+2\sqrt2)^2=17+12\sqrt2$. The lower wall cannot open in the full forward integral. Either wall is available in a limited real-frequency window. All integrals here concern the same ground-to-high-frequency dielectric channels of the same thermodynamic state, with a scalar response.

**MEASURED / fitted inputs.** The 1987 dense-fluid krypton spectrum is for 122 K and $17.44\times10^{21}$ atoms/cm³. Use the fluid-specific static-permittivity correlation of Harvey and Lemmon, Eqs. (1), (5), (6), Table II. With molar density $d=0.02895980133$ mol/cm³ and $t=273.16/122-1$,
$$
 P=d[6.273+(6.485+13.48t)d+(-82.51-170.4t)d^{1.7}],\quad
 \epsilon_s=(1+2P)/(1-P)=1.66064970 .
$$
The source fitted static dielectric data, with more emphasis on gas-like densities. This is an estimate at the matched fluid state. Its experimental uncertainty and the far-ultraviolet fit's model uncertainty have not been converted to a joint error box. [Harvey and Lemmon (2005), Table II](https://www.nist.gov/system/files/documents/mml/acmd/fluids_modeling/Harvey-Lemmon-50062.pdf) · [Laporte et al. (1987), Tables I–II](https://doi.org/10.1103/PhysRevB.35.6270)

**DERIVED.** Conditional on those two fits, the **entire** fluid spectrum gives $1<T/L\le1.288662$ and $0<\Gamma\le0.126127$. In the **9–11 eV window**, $T_W=3.27607790$ eV and $L_W=0.45387207$ eV give $T_W/L_W=7.21806448$. Since $T\ge T_W$ and $L\ge T/\sqrt{\epsilon_s}$,
$$
 L-L_W\ge T_W/\sqrt{\epsilon_s}-L_W=2.08836006\ {\rm eV},\qquad
 (L-L_W)/L\ge1-L_W\sqrt{\epsilon_s}/T_W=0.8214671.
$$
At least **82.1% of the screened area lies outside the published window**, under the adopted inputs. Broadband spectroscopy at matched temperature and density could falsify the numerical bound or expose an incompatible static-response or window fit. A measured direct loss spectrum should approach the same long-wavelength scalar response with matched normalization. This comparison says nothing about the 58 K solid-wavefunction limit. [Numeric fluid calculation](full_spectrum_krypton.csv) · [Finite-window calculation](KRYPTON_SPECTRUM.md)

**DERIVED, test over every ellipsoidal factor.** The Rb interpolants fail the inverse-frequency sum rule for at least one macroscopic shape. For fluid krypton the same necessary check succeeds uniformly for every $0\le n\le1$. Let $b=0.673$ be the 122 K fit's background susceptibility, $d=A\sum_j f_j/E_j^2=0.47049733$ its oscillator increment, and $a=b+d=1.14349733$. These are properties of the fitted rational response; its high-frequency background is not a constant of the physical full spectrum. For its shape transform $\chi_n=\chi/(1+n\chi)$, the subtracted static dispersion relation gives a total fitted inverse moment equal to $(\pi/2)d/[(1+na)(1+nb)]$. The fitted 9–11 eV interval uses no more than that because its absorption is positive. For the physical fluid with $s=0.66064970$, the full inverse moment allowed by the static fit is $(\pi/2)s/(1+ns)$. Since $a+b\ge s$ and $ab\ge0$, the window consumes at most $d/s=0.71217369$ of the physical budget for **every** factor. Thus the numerical 82.1% conclusion survives this audit. Passing a necessary test does not establish a unique causal completion of the VUV fit or remove its experimental uncertainty. This reasoning applies at the matched 122 K fluid state; we did not substitute this static correlation into the solid.

**DERIVED, independent computation.** Run python3 full_spectrum.py. For the lossless controls the script obtains transverse poles from a diagonal matrix $D$ of squared frequencies. The longitudinal poles and their weights follow from the eigensystem of $D+vv^T$, where $v_i^2$ are the transverse oscillator strengths. The rank-one inverse identity gives $1-1/\epsilon=v^T(D+vv^T-\omega^2 I)^{-1}v$. Thus the real-frequency sums require neither density binning nor artificially broadened resonances. For $p=0$ the script checks them against separate imaginary-axis quadrature. [25 moment controls](full_spectrum_controls.csv) · [Script](full_spectrum.py)

**DERIVED · conducting extension.** Both members of a sphere-to-longitudinal comparison retain finite static dressed responses in a conductor. This gives a different bound that can be applied to Rb even though its bare transverse susceptibility diverges. [Macroscopic depolarization and rubidium](DEPOLARIZATION.md)

**DERIVED · Lean scope.** Lean 4.34.1 checks nine exact rational declarations for the tangent remainder, finite two-point concavity, wall factorization, fractional-map composition after clearing denominators, sphere/slab cap, all-shape inverse-budget inequality and one-line wall controls. The spectral integral, dispersion hypotheses and physical application are the mathematical argument above. [Lean file](ScreeningArea.lean) · [Kernel audit](ScreeningArea.audit.txt)
