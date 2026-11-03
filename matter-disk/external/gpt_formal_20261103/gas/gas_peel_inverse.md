# Reverse recovery: a gas carries the peel under a specified closure

Supplement G8–G9 to `formal_gas_response.md`, 3 November 2026. The newly supplied `matter-disk` branch, commit `881386a0ab00d917af6334a01423fb8b22469f5e`, adds an inverse construction in §8. It is consistent with the forward insufficiency result: the inverse uses population and specimen information that the atomic record alone does not supply. This section retains that construction and proves its exact general form.

Let $\beta=1/(k_BT)$, with energies in the matching units. Suppose all populations are positive and satisfy the Saha ratios at the sampled temperatures. Electron density, nucleus density and temperature can vary between samples; every state-dependent correction must use its own sample's values.

**Theorem G8 — population combinations recover the threshold record.** For $0\leq q<Z-1$,
\[
L_q=\log\frac{n_qn_{q+2}}{n_{q+1}^2}
=\log\frac{U_qU_{q+2}}{U_{q+1}^2}
-\beta(I_{q+1}-I_q).
\]
The full-ladder combination satisfies
\[
L_B=\log\frac{n_0}{n_Z\,(n_e\lambda_e^3)^Z}
=\log\frac{U_0}{2^ZU_Z}+\beta B,
\qquad B=\sum_{q=0}^{Z-1}I_q.
\]
The $L_q$ are population-only ratios and cancel electron density and thermal wavelength algebraically. $L_B$ is a **corrected** ratio: evaluating it requires the sample's $n_e\lambda_e^3$. Its right side has no remaining explicit density factor, but it is not an observable constructed from charge fractions alone.

*Proof.* Dividing two adjacent Saha relations gives
$n_qn_{q+2}/n_{q+1}^2=S_{q+1}/S_q$. Their common electron-density and wavelength factors cancel. Multiplying all $Z$ Saha relations gives
\[
\frac{n_Z}{n_0}=
\frac{2^Z}{(n_e\lambda_e^3)^Z}\frac{U_Z}{U_0}e^{-\beta B}.
\]
Taking logarithms proves both identities. Since $n_q=Np_q$, the common nucleus density also cancels from the displayed ratios. No charge-neutrality assumption is needed for these identities themselves; it is needed only if $n_e$ is inferred from pure-species populations rather than supplied independently. ∎

If the partition weights and thresholds are independent of temperature, take two distinct inverse temperatures. The slopes give
\[
D_q=-\frac{\Delta L_q}{\Delta\beta}=I_{q+1}-I_q,
\qquad B=\frac{\Delta L_B}{\Delta\beta}.
\]
The complete threshold ladder follows from
\[
I_0=\frac1Z\left[B-\sum_{r=0}^{Z-2}(Z-1-r)D_r\right],
\qquad
I_q=I_0+\sum_{r<q}D_r.
\]
Indeed, summing $I_q=I_0+\sum_{r<q}D_r$ counts each $D_r$ exactly $Z-1-r$ times. This reconstruction includes the absolute scale; the Cayley vector follows by Theorem G1. With known partition functions and known $n_e\lambda_e^3$, one temperature already gives the individual thresholds directly from each adjacent Saha relation. The two-temperature construction instead removes constant partition intercepts.

For helium with $U=(1,2,1)$, write $D=I_1-I_0$. Then
\[
\log\frac{n_0n_2}{n_1^2}=-\beta D-\log4,
\qquad
\log\frac{n_0}{n_2n_e^2\lambda_e^6}=\beta B-\log4,
\qquad \Gamma_0=D/B.
\]
These are precisely the incoming §8 identities. Generating Saha populations from an input ladder and reading that ladder back verifies a model identity and the code, not an independent experimental determination of atomic thresholds.

**Theorem G9 — partition correction and the excited-state opposite.** If positive $U_q(T)$ vary with temperature but are known, define
\[
\widetilde L_q=L_q-\log\frac{U_qU_{q+2}}{U_{q+1}^2},
\qquad
\widetilde L_B=L_B-\log\frac{U_0}{2^ZU_Z}.
\]
For temperature-independent thresholds, their two-temperature slopes recover $D_q$ and $B$ exactly. Omitting the correction gives biases
\[
\widehat D_q=D_q-
\frac{\Delta\log(U_qU_{q+2}/U_{q+1}^2)}{\Delta\beta},
\qquad
\widehat B=B+
\frac{\Delta\log(U_0/(2^ZU_Z))}{\Delta\beta}.
\]

*Proof.* Subtract the known partition terms in Theorem G8 and take finite differences in $\beta$. ∎

For finite electronic excitation partitions
$U_q(\beta)=\sum_jg_{qj}e^{-\beta\epsilon_{qj}}$, with fixed positive weights $g_{qj}$ and fixed nonnegative excitation energies, let $\overline\epsilon_q$ be their normalized thermal mean. Differentiation gives $d\log U_q/d\beta=-\overline\epsilon_q$. Thus the **local**, uncorrected slope readings for helium are
\[
D_{\rm app}=D+\overline\epsilon_0+\overline\epsilon_2-2\overline\epsilon_1,
\qquad
B_{\rm app}=B-\overline\epsilon_0+\overline\epsilon_2.
\]
For a finite temperature interval these terms are interval averages in inverse temperature, not evaluations at an arbitrary midpoint. Consequently the naive quotient $D_{\rm app}/B_{\rm app}$ generally differs from the atomic $\Gamma_0$.

The registered opposite uses $U_0=U_2=1$ and the synthetic excited partition $U_1(T)=2+4e^{-10\,\mathrm{eV}/(k_BT)}$. It is not an asserted helium level scheme. Its purpose is to demonstrate a controlled failure of the constant-partition inference and exact recovery after the known partition correction. Actual helium excited-state partitions, continuum lowering, non-LTE populations and experimental uncertainty remain separate physical validation tasks.

**Stability of slope inversion.** If each corrected logarithmic combination has endpoint errors bounded by $\eta_1,\eta_2$, its two-temperature slope error is at most $(\eta_1+\eta_2)/|\Delta\beta|$. Thus close temperatures amplify observational errors even though the exact identity holds. For helium, suppose $|\widehat D-D|\leq\eta_D$, $|\widehat B-B|\leq\eta_B<B$, and $B>0$. Then
\[
\left|\frac{\widehat D}{\widehat B}-\frac DB\right|
\leq\frac{\eta_D+|D/B|\eta_B}{B-\eta_B}.
\]
This follows by writing the numerator as $B(\widehat D-D)-D(\widehat B-B)$ and using $|\widehat B|\geq B-\eta_B$. No statistical independence is assumed in this deterministic error bound. Vanishing or unmeasurably rare populations make the logarithmic inversion undefined or poorly conditioned; numerical closure tests do not remove that measurement limitation.

## Machine and numerical coverage

Theorem G8 and G9 have explicit analytic proofs above. The prospective numerical checks are in `PREREGISTRATION_ADDENDUM_GAS_PEEL.md`, with separate status in `formal_gas_results.json`. Lean coverage is only what the final theorem manifest lists. The original §8 reproduction remains a retrospective verification of supplied results; the synthetic partition opposite was specified before executing the new control.
