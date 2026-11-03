# Filament_Operator_Research_Revision_4 (fileId 1cHwBAlHEhBTEuVoCB5ZqnHlfi-9VBWD7) — READ IN FULL (11 pp, nothing truncated)
Title: "A Five-Dimensional Non-Normal Stability Operator with a Verified Interface Block: Transient Amplification and a Testable Filament Hypothesis". Jeromie Beasley, Operator-First Persistent Geometry Initiative, Research revision 4, 25 September 2026. (Earlier name in memory: Snake / galaxy-holes paper.)
## Evidence grades (his own legend)
[T] follows from stated mathematical assumptions; [C] claim taken from cited observational/mathematical work; [V] finite check in accompanying scripts; [H] modelling choice / proposed physical interpretation. "a mathematical deduction from a chosen matrix is not an empirical validation of that matrix."
## Sec 1 Observational motivation (all [C]/[H])
Galactic Centre Snake G359.1-0.2, ~30' ≈ 70 pc, <1 pc wide, major and minor kink; compact radio source G359.13142-0.20005 with X-ray counterpart = pulsar CANDIDATE (no radio pulses detected); proposed impact 500-1000 km/s (Chandra 2025: 450-900 km/s) is a scenario estimate. PSR J1744-2946 (confirmed MSP binary) is in the Sunfish filament, 49'' west (~1.9 pc projected), association with Snake ruled out. "the Snake an example of a forced disruption... not an observed spontaneous rupture". Z-pinch alternative cited (aspect ratio 100 needs axial field >=10x azimuthal).
## Sec 2 Operator
Coordinates (x1,x2,s1,s2,r) = two shape, two shear, one interface. K5(γ) = rows: [a 0 0 0 0; h b c1 c2 μ; 0 0 d1 q1 0; 0 0 q2 d2 0; 0 γ 0 0 b], B=[[d1,q1],[q2,d2]]; b>0. γ=0 one-way point. μ "gradient-sensitive interface-to-shape coupling" is an input [H].
- Thm 2.1 (Exact interface embedding & global spectral condition): V=span{e2,e5} invariant; K5|V = J_γ=[[b,μ],[γ,b]]; det(λI-K5(γ)) = ((λ-b)^2 - μγ)(λ-a)det(λI2-B); γ=0, μ≠0: length-two Jordan chain at b; if a>0 and σ(B) in right half-plane then Re σ(K5(0))>0 though non-normal; ||e^{-K5(0)t}|| ≥ ||e^{-Jt}||. Proof given (block upper-triangular). Equality is a restriction statement.
- Remark 2.2: "minimality" of 5 dims is by construction (2+2+1); a 4x4 family K4 carries same Jordan block; no necessity claimed. Appendix A: 5x5 pattern with defective 2x2 sub-block but simple eigenvalue in full matrix: det = λ^5-8λ^4+21λ^3-25λ^2+10λ+1, derivative -4 at 1.
## Sec 3 Resolvent/pseudospectrum [T]
||(λI-J)^-1||_2 = sqrt(4|z|^2+|μ|^2+|μ| sqrt(|μ|^2+... )) / |z|^2 form (garbled); σ_ε(J) = exact open disk |λ-b| < r_ε, r_ε = sqrt(ε|μ|+ε^2). ε_crit = sqrt(|μ|^2+4b^2) - |μ| ... = σ_min(J) (right-half-plane test on -J). At |μ|/b=2 equals (√2-1)b.
## Sec 4 Transient growth
- Thm 4.1: M(t)=||e^{-Jt}||_2 = e^{-bt}( sqrt(4+|μ|^2t^2) + |μ|t )/2; M(t)>1 for some t iff κ=|μ|/b > 2; t* = sqrt(κ^2-4)/|μ|... M_max = ((κ+√(κ^2-4))/2) exp[-√(κ^2-4)/κ]. Full system amplifies when κ>2.
- Pure interface input e5: A_r(t)=e^{-bt} sqrt(1+|μ|^2t^2); overshoots only for κ>κ_r = 2.48526751266... ; tangency x=bt satisfies 1-x=e^{-2x}, κ_r=[x(1-x)]^{-1/2}, x=0.79681213002. 2<κ<κ_r: optimal state grows, interface-only impulse does not. κ>2 sufficient not necessary for full K5.
## Sec 5 Eigenvector coalescence
- Prop 5.1: detuning J_δ: sinθ_δ = |δ|/sqrt(|μ|^2+|δ|^2) = O(|δ|/|μ|) (linear); reverse coupling J_γ (μ,γ>0): eigenvalues b±√(μγ), sinθ_γ = sqrt(γ/μ)/sqrt(1+γ/μ)=O(√(γ/μ)) (square-root). "conical rank collapse" retained only as visual name for eigenvector-frame coalescence.
## Sec 6 "model trap snapshot": max Re σ(-K5)<0 and sup_{0<t<T} E(t) > E_max.
## Sec 7 Riesz subspaces / Grassmannian lift: Π(q)=(1/2πi)∮(zI-K)^-1 dz; orthogonal range projector P=W(W†W)^-1W†; Q_ab=Tr P ∂aP ∂bP, g=ReQ, Ω=2ImQ. For model (2.1) with a,σ(B) separated, Ran Π=V constant so g=Ω=0 in these coordinates. 
## Sec 8 continuum projection (hypothesis): vorticity ω_z=dV0/dr+V0/r; K_ij=<φ_i,Lφ_j>, μ=<φ2,Lφ5>; conditions (8.4) needed for invariant block; remains [H].
## Sec 9 conditional heat trace/spectral ledger: Tr e^{-tL} ~ (4πt)^{-d/2}(a0+a1 t+...); log det_ζ L = -ζ'(0); non-self-adjoint needs admissible spectral cut; finite det K5 ≠ continuum zeta determinant.
## Sec 10 colour-shift analogy as hypothesis [H]: Bezold-Brucke-named metric shift (10.1) g~ = g + χ(I)(∂F...) + σ_EP δ (I-I_c)^{-1/2}; "not used in any proof".
## Sec 11 what Snake can decide: 700 km/s crosses 1 pc in ~1.4e3 yr (illustration only). Research program (i)-(v). Sec 12 open bridge: physical MHD/kinetic operator with (8.4) approximately; leakage bound.
## Reproduction: verify_results_v4.py (stdlib), independent_check_v4.py (NumPy/SciPy/SymPy), build_figures_v4.py, filament_operator_v4.tex.
## Flags: non-normality, exceptional point (Jordan block, γ=0), pseudospectrum, Riesz/Grassmannian (g=Ω=0), spectral ledger/log-det; no Smith disk/peel/offset/census/walls (interface = coordinate r). Memory: none. Reviewers' caution quotes: "no coupling has been measured and no astrophysical mechanism is demonstrated."
