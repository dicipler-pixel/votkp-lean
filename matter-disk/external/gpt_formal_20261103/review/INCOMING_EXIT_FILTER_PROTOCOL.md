# Endpoint-filter sensitivity audit

Written before execution on 3 November 2026. This audit asks whether the incoming
`matter-disk` finite-census exit is independent of its endpoint filter. The shipped
filter is `abs(nu)>1e-9` and `abs(1-nu)>1e-9`; the retained maximum principal
logarithm angle reaches pi/2 at the reported exit.

Use the same antiperiodic ring N=2000 and region L=40, with the same lower band
of h(k)=(0.5+cos k)sigma_x+sin k sigma_y+(m+i gamma)sigma_z. Compute its projector
independently as (I-h/E)/2 for principal E=sqrt(d.d), check this against eigensolver
biorthogonal projectors at representative k. Test m=0.4 and m=0, with endpoint
filters 1e-6, 1e-8, 1e-9, 1e-10 and 1e-12. Locate the first sampled threshold
crossing by the source scan then 26 bisections. Record results, not a pass/fail
criterion chosen to support an exit interpretation. Significant filter dependence
means a numerical instrument-dependent exit must be distinguished from a
filter-independent spectral law. Complex eigenvalues are not physical occupation
probabilities.

Also evaluate the exact oblique projector [[2,1],[-2,-1]], whose boundary product
is -2, to falsify unconditional positive-census transfer to biorthogonal projectors.
