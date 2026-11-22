# Statistical planning for the encoded polarization comparison
Jeromie Beasley, 21 November 2026. Worked design with idealized counting statistics. All estimates are conditional and can be checked without an instrument.

Choose each axis Q,U,V in turn. For axis i prepare each input sign s for half the exposure, and record both analyzer output signs t. Under ideal coherent illumination with monitored mean incident photon number N_i the four counts can be modeled as independent Poisson variables with means

    μ_st = (N_i/4) (M_II + s M_Ii + t M_iI + st M_ii).

Write Y_i = sum counts / N_i and D_i = sum st counts / N_i. Then E[Y_i]=M_II, E[D_i]=M_ii. They share the same photons, so Cov(Y_i,D_i)=M_ii/N_i; their variances equal M_II/N_i. Using one third of each Y_i in the total intensity estimate, the contrast is obtained by summing Y_i/3+b_i D_i, b=(1,1,−3). Independent axis settings give Var(Lhat)=sum v_i/N_i, where v_i=(1/9+b_i²)M_II+(2/3)b_i M_ii. At fixed total exposure N, minimization with the Cauchy–Schwarz inequality gives N_i/N proportional to sqrt(v_i). This is optimal among allocations for this specified estimator. This calculation uses coherent, stationary mean illumination. Normalization errors, background subtraction, detector inefficiency, analyzer cross-talk, phase drift, uncertainty in z and departures from a coherent real return need their own independent budgets.

For the 35/6 setting and this ideal estimator, a signal-to-standard-error ratio of five requires about 1.52×10¹⁰ incident photons and 4.34×10⁸ mean detections. For Be/Rb the corresponding estimates are 3.80×10¹⁰ and 1.06×10⁹. These are group totals over both inputs, both outputs and three axes. They quantify why background and polarization calibration matter. A quoted design SNR is not an observed significance level. Raw analyzer count records must remain available to compute the measured uncertainty.

## An explicit rejection control before interpreting a positive contrast

Consider an ideal relative phase retarder with Jones matrix diag(1,exp(iφ)). It preserves intensity, Q and the circular–linear subplane up to a rotation. Its Mueller diagonal is (1,1,cosφ,cosφ); hence L=2−2cosφ, positive for every nontrivial retardance. Its two eigenvalues always have equal modulus. Thus a physical apparatus can give a strictly positive scalar and completely lack the split in eigenvalue moduli we seek. Even the V diagonal can be positive (for φ=π/3 it is 1/2 and L=1). Check phase leakage with the cross-terms of the U/V block before classifying. At φ=π, these cross-terms vanish, but the real representative diag(1,−1) reverses orientation and the V diagonal is −1. This demonstrates why checks of coherence, existence of a real representative and its positive determinant must all be part of the comparison.

With a return K already known, an ionization ratio used to set filters is a calibrated input. An optical outcome for this arrangement would test a transfer representation. Calling it validation of a natural atomic transition needs a separately specified atomic coupling and an outcome that the calibration does not encode.
