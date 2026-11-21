# Screened and optical readings of the same rubidium spectrum

**DERIVED · why this belongs beside the cell test.** The finite-cell calculation moves an occupied independent-particle projector through a phase. In interacting three-dimensional Coulomb matter the experimental observable depends on the electric boundary condition. The negative-first moment of transverse optical conductivity and the longitudinal static weight involve different measured integrands. For cubic media with $\epsilon=(n+i\kappa)^2$ they are proportional respectively to $\operatorname{Im}\epsilon$ and $\operatorname{Im}(-1/\epsilon)$ when integrated over photon energy. Equations 25–28 in Onishi and Fu give the screening factor; Resta derives the boundary-condition dependence of polarization fluctuations. This is a comparison using standard electronic response in a crystal. It supplies no identification between Jeromie Beasley's intrinsic metric and an externally defined optical metric. [Onishi and Fu (2025), §§V–VI](https://doi.org/10.1103/PhysRevResearch.7.023158) · [Resta (2006)](https://arxiv.org/abs/cond-mat/0512247)

**MEASURED · material input.** N. V. Smith determined the complex optical index of rubidium from reflection measurements. The branch retains the 24 published optical-constant samples covering 0.554–3.967 eV and their source pin. Optical power, permittivity, loss, and all contrasts below are derived from those same samples. The archive gives no pointwise measurement uncertainties. [Smith (1970)](https://doi.org/10.1103/PhysRevB.2.2840) · [Input table and method](../../batch8/material_transport/rb_optics.py)

**DERIVED · test before interpretation.** Put $O=\operatorname{Im}\epsilon$ and $L=\operatorname{Im}(-1/\epsilon)$. For a passive sample with $O>0$ and nonzero $\epsilon$, write $\epsilon=u+iv$ with $v>0$:
$$
 L=\frac{v}{u^2+v^2},\qquad
 z_{\rm screen}=\frac{O}{L}=|\epsilon|^2=(n^2+\kappa^2)^2,\qquad
 \Gamma_{\rm screen}=\frac{O-L}{O+L}=\frac{z_{\rm screen}-1}{z_{\rm screen}+1}.
$$
A sample with vanishing loss has no positive two-channel ratio from the observations. For positive channels the exact loop-wall test is $z_{\rm screen}^2-6z_{\rm screen}+1>0$. Reversing which channel is in the numerator flips the directed reflection; this is an exchange of observables at fixed photon energy. Failure of either exact identity in the input table would reject the implementation. All 24 finite-decimal samples satisfy both identities in rational arithmetic. This ratio records the strength of dielectric screening at a given frequency. An atom's successive removal-energy ratio would require a separate mapping.

| Feature on the ascending photon-energy samples | Observed sample bracket (eV) | Meaning |
|---|---|---|
| Upper loop wall | 1.8730–2.0670 | Optical-to-loss ratio falls below $3+2\sqrt2$ |
| Equal-channel point | 2.4550–2.6380 | Optical-to-loss ratio passes through one |
| Lower loop wall | 2.9520–3.0640 | Ratio falls below $3-2\sqrt2$ |
| Vacuum-interface half-power | 3.2040–3.3970 | Earlier Fresnel power $\lvert(1-n-i\kappa)/(1+n+i\kappa)\rvert^2$ falls below one half |

**DERIVED · false control.** Dropping the extinction coefficient changes the wall-branch label on 19 of 24 samples. At 3.3970 eV the measured-index-derived values give a loss factor near 7.86 and an optical absorption factor near 0.127. The brackets report endpoint calls; they do not count unresolved features between measured samples. [Pointwise output](screened_optics.csv) · [Earlier Fresnel comparison](../../batch8/material_transport/README.md)

## The portion of the spectral integrals actually sampled

**DERIVED.** In this energy window, trapezoids between adjacent samples yield $\int O\,dE=1.238721$ eV and $\int L\,dE=3.841263$ eV. Three independent interpolation choices, shape-preserving interpolation of the two nonnegative channels, linear complex index, and linear complex permittivity, give 1.23415–1.24245 eV and 3.80204–3.88361 eV across the same data. The stronger pointwise loss near the plasma resonance contributes to the ordering of these partial integrals. On the branch's 5.700 Å bcc structure, multiplying by $\epsilon_0/(\pi n_e e^2)$ after converting energy to joules gives 0.20177 and 0.62569 Å² for a density convention of one electron per atom, or 0.0054532 and 0.0169105 Å² for all 37 electrons. Changing this normalization rescales the same optical data. These are finite-window contributions at the experimental temperature. The observed response includes every optically active electron and the analysis has no orbital filter. A bulk zero-temperature sum requires the unobserved spectral weight, boundary conditions and temperature assumptions. [Window and interpolation checks](screened_optics_window.csv)

**DERIVED · analytic counterexample.** Take a passive metal with finite Drude damping, $\epsilon(E)=b-p^2/[E(E+i\gamma)]$, $p,\gamma,b>0$. At $E\to0$, $O\sim p^2/(\gamma E)$ while $L\sim\gamma E/p^2$. The optical integral diverges logarithmically at its lower endpoint. The screened integral stays finite. For $0<\gamma<2p/\sqrt b$, put $A=p^2/b-\gamma^2/2$, $B=\gamma\sqrt{p^2/b-\gamma^2/4}$. Direct integration gives
$$
 \int_{E_0}^{\infty} O\,dE=\frac{p^2}{2\gamma}\ln(1+\gamma^2/E_0^2),\qquad
 \int_{E_0}^{\infty} L\,dE=\frac{p^2\gamma}{2b^2B}
 \left[\frac{\pi}{2}-\arctan\!\left(\frac{E_0^2-A}{B}\right)\right].
$$
This demonstrates in an explicit response model why unqualified transfer of the independent-particle metal divergence to the interacting longitudinal response fails. Its strictly positive dc conductivity follows from $\operatorname{Re}\sigma(0)=\epsilon_0 p^2/(\hbar\gamma)$ when the energies are in joules.

**DERIVED · held-out spectrum.** Use the archived fit to rubidium's ten infrared samples below 1.25 eV. Its tabulated parameters are $b=1.60611372$, $p=3.5869778$ eV, $\gamma=0.02957695$ eV. At the held-out sample energies 1.442–3.967 eV, the continuous fit integrated over the same band gives 0.07940 eV optical and 2.74617 eV screened; the data trapezoids give 0.54737 and 3.83559 eV. Positive dc response and low-frequency damping in the model leave much of the observed higher-energy absorption unexplained. A constant background is an effective infrared parametrization; the infinite-range analytic integrals above serve as a mathematical control. [Held-out integrated results](screened_drude.csv) · [Pointwise residual inputs](screened_drude_rows.csv) · [Archived infrared fit](../../batch8/material_transport/rb_optics.csv)

**DERIVED · reproduction.** From this directory run the two scripts below. The first verifies the input SHA-256 and computes all ratios from the published decimal inputs. The second checks both closed-form integrals against adaptive quadrature on the observed and held-out windows.

    python3 screened_optics.py
    python3 screened_drude.py

**DERIVED · independent material.** In the observed 9–11 eV exciton window, the published crystalline krypton fit crosses the equality of the two channels twice, but does not reach rubidium's lower wall. [Krypton central fits, all roots and rounding test](KRYPTON_SPECTRUM.md)
