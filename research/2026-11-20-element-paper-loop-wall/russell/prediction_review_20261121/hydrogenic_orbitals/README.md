# Face-apex survival for every hydrogenic orbital

Jeromie Beasley's face apex is a=tanh[(ln z)/4]. For a same-mass one-electron Schrödinger Coulomb Hamiltonian with scale α before and β after a sudden quench, |E'ₙ|/|Eₙ|=z=(β/α)² and a=(β−α)/(β+α). Consider the ideal probability of a projective measurement in the same n,ℓ,m eigenstate of the new Hamiltonian at the same centre, with the same spatial axes. Put x=a², k=n−ℓ−1 and p=2ℓ+2. The signed overlap in conventional real radial phase conventions and its fidelity are

    S = (1−x)^(ℓ+3/2) P_k^(0,p−1)(1−2x),       F=S².

Here P is the Jacobi polynomial with P_k^(0,b)(1)=1. The sign of one isolated overlap can be changed by rephasing either eigenvector; its zeros and the fidelity are independent of this convention. Circular states have k=0. For 2s, the polynomial is 1−3x. For each k>0 there are exactly k simple roots in 0<x<1 because the Jacobi weight has parameters 0 and p−1>−1. Both scale directions give the same x. The small-r expansion in the energy coordinate r=ln z is

    1−F = [2n²−2ℓ(ℓ+1)+1] r²/16 + O(r⁴).

This follows from the coefficient −k(k+p) of x in the Jacobi polynomial and x=r²/16+O(r⁴). This gives the local projector sensitivity for radial dilations of that particular orbital.

## Independent analytic derivation

In y=(α+β)R/n the radial overlap, after extracting its common scale factor (1−x)^(ℓ+3/2), is the normalized integral of the pair L_k^(p−1)((1+a)y), L_k^(p−1)((1−a)y), with weight y^p exp(−y). Normalize the integral by its value at a=0. The Laguerre generating function gives the generating function for the two independent polynomial indices with weight y^(p−1) exp(−y) as (p−1)! D^(−p), D=1+a(u−v)−uv. With one additional factor y, it gives p! (1−u)(1−v)D^(−p−1). At equal powers u^k v^k the two coefficients differ by the factor p+2k for all a. To see this apply the following identity involving ordinary formal derivatives:

    (1−u)(1−v)D^(−p−1)
      = [1+(u∂u+v∂v)/p+(u∂u−v∂v)/(pa)] D^(−p).

The antisymmetric derivative has zero diagonal coefficient, and a=0 follows by continuity. Hence the factor p+2k cancels on normalization. To extract the remaining coefficient factor D=(1+au)(1−av)−(1−x)uv. Binomial expansion and division by the diagonal value at a=0, binom(k+p−1,k), give

    Σ_{h=0}^k binom(k,h) binom(k+p−1,h) (−x)^h (1−x)^(k−h).

This is precisely the binomial representation of P_k^(0,p−1)(1−2x). This proof uses standard one-electron Coulomb eigenfunctions, Laguerre generating functions and ordinary integration. The exact arithmetic test independently expands both Laguerre polynomials and integrates every monomial with the factorial moment. It agrees with the Jacobi expression on all 637 tests, n=1,…,13 and every ℓ at seven scale coordinates. Run: python all_orbitals.py. [DLMF, orthogonal-polynomial definitions](https://dlmf.nist.gov/18.5) · [Generating functions](https://dlmf.nist.gov/18.12)

## What the available atomic measurements score

Couratin et al. reported a shake-off probability of 0.02339(36) for trapped one-electron ⁶He⁺ undergoing decay to lithium. The measured charge spectrum distinguishes an escaped electron from a bound electron. All electronic bound levels of the one-electron daughter contribute to its bound charge class. With the point-nucleus, zero-recoil initial 1s model, the ideal 1s→1s survival at β/α=3/2 is (24/25)³=0.884736. Its complement 0.115264 includes both shake-up to any bound state and shake-off into the continuum. Directly equating this complement to the measured 0.02339 would conflate two observables. The experiment's energy ratio is about 2.25, far below both near-5.83 cutoffs. For direct single-unit increases of positive integer Coulomb charge, (Z+1)²/Z²≤4 for every Z≥1. This class of undecorated same-n comparisons never reaches the forward wall. [Couratin et al., Physical Review Letters (2012)](https://doi.org/10.1103/PhysRevLett.108.243201)

The one-electron tritium final-state paper of Williams and Koonin computes corrections to sudden probabilities. It gives a theoretical comparison. A charge count and a term-integrated line both require a state-resolution model before scoring the same-nℓm prediction. These sources supply no measured fixed-orbital survival at a scale between the geometric and competing cutoffs. [Williams and Koonin (1983)](https://doi.org/10.1103/PhysRevC.27.1815)

## Scope of the scale map

For distinct initial and final reduced masses μ and μ′, the radial scale is proportional to μZ, whereas the binding scale is proportional to μZ². Consequently β/α=sqrt[z μ′/μ]. One must use this corrected scale in the Jacobi result; using the measured binding ratio alone silently omits the reduced-mass factor. Daughter recoil can introduce a spatial phase and couple angular channels. A relativistic Dirac Coulomb state has large and small spinor components and a charge-dependent radial exponent sqrt[κ²−(Zα_fs)²]. The simple one-parameter Schrödinger identity then needs a new integral and the appropriate energy map. An ordinary partial charge-state inventory of a many-electron atom is outside this test. Comparing an analogue simulator or another preparation at tuned scale would test the declared radial quench. Associating the wall with an independent many-electron response remains a separate scientific question.
