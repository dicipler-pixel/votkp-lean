# An exact gas-transport witness with matching density, flow and stress

Prepared for Jeromie Beasley's matter–gas–VOTKP programme, 3 November 2026. These are fully specified analytic models and proofs, not new laboratory observations. The finite-difference moment-null identity is developed more generally in the manuscript's M1; the construction below specializes it to a positive velocity distribution and a physical transport equation.

## K1. Two positive preparations with the same first three moments — proved here

Let \(x\) be periodic with period \(L\), choose \(k=2\pi m/L\) for an integer \(m\ge1\), and fix

\[
\rho_*>0,\quad 0<\eta<1,\quad v_0>0,\quad 0<a<1/12,\quad \sigma\ge0.
\]

Put

\[
u=(-3,-1,1,3),\qquad d=(-1,3,-3,1),\qquad
\rho(x)=\rho_*[1+\eta\cos(kx)].
\]

For \(\sigma>0\), let \(g_\sigma\) be the centered normalized Gaussian of variance \(\sigma^2\). At \(\sigma=0\), interpret \(g_0(v-v_j)\,dv\) as the point mass at \(v_j\). Define

\[
p_\pm(v)=\sum_{j=0}^3(\tfrac14\pm ad_j)g_\sigma(v-v_0u_j),
\qquad f_\pm(x,v,0)=\rho(x)p_\pm(v).
\]

Both are nonnegative normalized conditional velocity distributions, strictly positive for \(\sigma>0\). Their pointwise initial moments are

\[
M_\ell^\pm(x,0)=\int_\mathbb R v^\ell f_\pm(x,v,0)\,dv,
\]

\[
M_0^+=M_0^-=\rho(x),\qquad
M_1^+=M_1^-=0,\qquad
M_2^+=M_2^-=(5v_0^2+\sigma^2)\rho(x).
\]

Their third moments differ:

\[
M_3^\pm(x,0)=\pm48av_0^3\rho(x),\qquad
\Delta M_3(x,0)=96av_0^3\rho(x),
\]

where \(\Delta=({+})-({-})\).

**Proof.** The four weights sum to one because \(\sum_jd_j=0\). Their smallest possible value is \(1/4-3a>0\). Direct exact sums give

\[
\sum_j d_j u_j^\ell=0\quad(\ell=0,1,2),\qquad
\sum_j d_j u_j^3=48,
\]

while \(\frac14\sum_ju_j=0\), \(\frac14\sum_ju_j^2=5\), and \(\sum_ju_j^3=0\). Convolution with the centered Gaussian adds \(\sigma^2\) to each second moment and \(3\sigma^2v_0u_j\) to each third moment. The corresponding perturbation sums still vanish at orders at most two and the additional third-moment term vanishes because \(\sum_jd_ju_j=0\). ∎

Thus number density, mean velocity and kinetic stress are equal **pointwise**, not merely after spatial averaging. With particle mass \(m_p\), the kinetic-energy density is also equal, \(m_pM_2/2\). This is a one-dimensional illustration, so it is not by itself a claim about every component of a three-dimensional stress tensor.

## K2. Same transport law, different later density — proved here

Evolve both preparations by the same force-free collisionless Boltzmann equation,

\[
\partial_t f+v\partial_x f=0,
\qquad f_\pm(x,v,t)=f_\pm(x-vt,v,0).
\]

Let \(n_\pm(x,t)=\int f_\pm(x,v,t)\,dv\). With \(q=kv_0t\), the exact densities are

\[
n_\pm(x,t)=\rho_*\left[1+\eta e^{-\sigma^2k^2t^2/2}
\left(\tfrac12[\cos q+\cos(3q)]\cos(kx)
\mp8a\sin^3q\sin(kx)\right)\right].
\]

In particular,

\[
\boxed{\Delta n(x,t)=-16a\eta\rho_*e^{-\sigma^2k^2t^2/2}
\sin(kx)\sin^3(kv_0t).}
\]

**Proof.** Along a characteristic, \(x-vt\) is constant, proving the solution formula. The Gaussian Fourier transform gives

\[
\int g_\sigma(v-v_0u_j)e^{-ikvt}\,dv
=e^{-iku_jv_0t}e^{-\sigma^2k^2t^2/2}.
\]

The unperturbed symmetric weights contribute \([\cos q+\cos(3q)]/2\). For the perturbation,

\[
\sum_jd_j\cos(q u_j)=0,\qquad
\sum_jd_j\sin(q u_j)=2\sin(3q)-6\sin q=-8\sin^3q.
\]

Expanding \(\cos(kx-kvt)\) and combining these identities proves both formulas. ∎

For the exact discrete-velocity instance

\[
a=1/24,\quad \eta=1/2,\quad \rho_*=v_0=k=1,\quad\sigma=0,
\quad x=t=\pi/2,
\]

the two later densities are

\[
n_+=5/6,\qquad n_-=7/6,\qquad \Delta n=-1/3.
\]

For \(\sigma>0\), the distributions are smooth and positive and the separation remains nonzero at the same event, reduced by \(e^{-\sigma^2\pi^2/8}\). The discrete case is therefore not essential to the qualitative separation.

## K3. What the missing moment does — proved here

The transport equation implies the hierarchy

\[
\partial_tM_\ell+\partial_xM_{\ell+1}=0.
\]

For the two preparations in K1,

\[
\Delta n(x,0)=\partial_t\Delta n(x,0)
=\partial_t^2\Delta n(x,0)=0,
\]

but

\[
\partial_t^3\Delta n(x,0)
=-\partial_x^3\Delta M_3(x,0)
=-96a\eta\rho_*k^3v_0^3\sin(kx).
\]

**Proof.** Integrate the kinetic equation against \(v^\ell\); the finite mixture with Gaussian tails justifies differentiation and integration. The discrete measure case is the same finite sum. Iterate the hierarchy three times and use K1. Equivalently, differentiate the exact formula in K2. ∎

The stress separates first through its derivative, the flow next, and the density at third order. The full kinetic state obeys a Markovian evolution. The history dependence appears only after retaining the three lower moments and discarding the higher velocity structure. These are matching **specified present measurements**, not the same complete physical state. No contradiction with deterministic dynamics is involved.

## K4. A precise erasure intervention before release — proved here

Define the common symmetric velocity target

\[
p_0(v)=\tfrac14\sum_{j=0}^3g_\sigma(v-v_0u_j).
\]

During an explicitly separate preparation interval of duration \(s\), hold the spatial profile fixed and apply the velocity-reset map

\[
\mathcal E_s[f](x,v)=e^{-\nu s}f(x,v)
+(1-e^{-\nu s})\rho(x)p_0(v),\qquad \nu\ge0.
\]

For the K1 preparations this map preserves their common density, flow and stress, preserves positivity, and multiplies their difference by \(e^{-\nu s}\). If free streaming starts **after** this preparation interval, then the density contrast in K2 is multiplied by exactly \(e^{-\nu s}\).

**Proof.** The map is a convex combination of positive distributions with the same first three moments. Its difference on the two preparations is \(e^{-\nu s}(f_+-f_-)\). Free streaming and integration in velocity are linear, so this factor carries through to the later density contrast. ∎

The map can be implemented mathematically as a Poisson reset to a prescribed common velocity distribution while the spatial profile is held. It is not asserted to be the self-consistent collision operator of an isolated gas. If collisions and streaming act simultaneously with a moment-dependent local equilibrium, the two targets need not stay equal once the lower moments separate; the simple exponential factor has then **not** been proved. The separation of preparation and release is an essential hypothesis.

An early perturbation exposed to the reset for longer has a smaller later signal; a perturbation inserted immediately before release has less time to be erased. This gives a controlled mathematical version of the early/late distinction in the song without making a universal dense-gas claim.

## Null tests and limitations

| Control | Exact prediction | Interpretation |
|---|---|---|
| \(a=0\) | \(f_+=f_-\), hence \(\Delta n=0\) | Remove the hidden distinction |
| \(\eta=0\) | \(\Delta n=0\) for all times | Homogeneous density is insensitive to the different velocity record |
| \(\sin(kx)=0\) | Density contrast zero at that readout | Spatial placement matters |
| \(kv_0t\in\pi\mathbb Z\) | Density contrast zero at that time | A null readout is not evidence that the complete distributions agree |
| Pre-release reset \(s\to\infty\), \(\nu>0\) | \(\Delta n\to0\) | An intervention erases the prepared distinction |
| Include \(M_3\) among retained observations | Preparations differ already initially | The original three-moment match is no longer the stated experiment |
| \(\sigma>0\) | Exact Gaussian dephasing envelope | Smooth velocity spread reduces this density readout without making the full states identical |

No gas pressure law, collision cross section, VOTKP ionization threshold, quantum memory kernel or laboratory calibration is inferred from this construction. It establishes a bounded mathematical claim: a density–flow–stress record alone does not determine later force-free transport for arbitrary positive velocity distributions. Testing whether an actual gas can prepare and retain this distinction requires a separate physical model and experiment.
