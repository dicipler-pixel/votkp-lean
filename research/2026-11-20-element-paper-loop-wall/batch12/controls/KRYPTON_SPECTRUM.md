# Does solid krypton's exciton band open the lower screening wall?

**HYPOTHESIS / falsifier.** Rubidium's measured screening contrast enters the lower branch near its plasma resonance. Test whether the same event occurs somewhere in the *published central fit* for the 9–11 eV exciton window of solid krypton. The criterion is $z_{\rm screen}=|\epsilon|^2<3-2\sqrt2$. A global minimum above that value rejects the proposal for that fit and interval. A dense-fluid row from the same study provides a second state. This is an additional optical comparison; neither optical spectrum supplies a free-atom peel ratio.

**MEASURED / fitted input.** Laporte, Subtil, Reininger, Saile, Bernstorff and Steinberger measured reflectivities and used a Lorentzian dielectric dispersion to reconstruct them. Table II contains central fits for crystalline krypton at 113 K, number density $20.28\times10^{21}$ cm⁻³, and fluid krypton at 122 K, $17.44\times10^{21}$ cm⁻³. We use the tabulated macroscopic oscillator strengths and dielectric background from those two rows. The local-field-corrected starred oscillator strengths belong to a different parametrization. The fourth oscillator represents transitions above the fitted spectral region. The krypton 58 K lattice used for the electronic projector is a separate experimental structure. [Laporte et al. (1987), Eq. 1, Figs. 6–8, Table II](https://doi.org/10.1103/PhysRevB.35.6270) · [Open primary-source table](https://bib-pubdb1.desy.de/record/323066/files/PhysRevB.35.6270.pdf) · [Two transcribed rows](krypton_fit_inputs.csv)

**DERIVED · reconstruction.** In energy units the macroscopic dispersion is
$$
 \epsilon(E)=\epsilon_r+A\sum_j\frac{f_j}{E_j^2-E^2-i\gamma_j E},
 \qquad A=(\hbar\omega_p)^2,\qquad \omega_p^2=\rho e^2/(\epsilon_0m_e).
$$
The SI conversion with $E$ in eV gives $A=27.9629216873$ eV² for the solid and $24.0470095773$ eV² for the fluid. All oscillator strengths and dampings are positive. Write $x=E^2$ and $D(x)=\prod_j[(E_j^2-x)^2+\gamma_j^2 x]>0$. Equation 1 has real numerator $a(x)$ and imaginary numerator $E b(x)$ over $D(x)$, so $z=(a^2+xb^2)/D^2$. Holding the central parameters fixed and rounding only $A$ to 12 decimal places, the checker isolates all real polynomial roots on $81\le x\le121$ with rational arithmetic. It tests the extrema using the derivative numerator and the two loop walls using the numerator of $z^2-6z+1$. This includes unresolved narrow model features a uniform energy grid could miss.

| State | Minimum $z_{\rm screen}$ | Energy at minimum (eV) | Upper-wall crossings | Equal-channel crossings | Lower-wall crossings |
|---|---:|---:|---:|---:|---:|
| Solid, 113 K | 0.720421 | 10.93407 | 3 | 2 | 0 |
| Fluid, 122 K | 0.299450 | 10.81231 | 3 | 2 | 0 |

**DERIVED · verdict.** Both fits reverse which response channel is larger and open the upper wall repeatedly. Neither reaches the lower branch in the observed exciton window. With the same integration limits for both states, the fitted solid yields $\int\operatorname{Im}\epsilon\,dE=4.58605$ eV and $\int\operatorname{Im}(-1/\epsilon)\,dE=0.27247$ eV. The fluid yields 3.27608 and 0.45387 eV. The ratio of these *partial integrals* depends on the energy window. Rubidium and krypton were observed at different photon energies and temperatures. These differences therefore do not define an element-by-element classifier of electrical conduction. [Root locations](krypton_screening_roots.csv) · [Extrema and partial weights](krypton_screening_scan.csv)

**DERIVED · last-place test.** Vary all density, background, oscillator energies, dampings and strengths independently by half their printed last decimal place, with a separate $10^{-7}$ relative enclosure on the SI conversion factor. Split the whole energy interval adaptively and propagate each box by interval arithmetic over rational numbers. For every such combination the solid has $z>0.22021$ and the fluid $z>0.18120$, exceeding $3-2\sqrt2\simeq0.171573$ throughout. No energy boxes remain unresolved. These tests address publication rounding; the parameter covariance and experimental systematic uncertainty are unquantified. [Complete interval counts and lower bounds](krypton_rounding.csv)

**DERIVED · reproduction.** Python requires SciPy, NumPy and SymPy.

    python3 krypton_optics.py
    python3 krypton_rounding.py
