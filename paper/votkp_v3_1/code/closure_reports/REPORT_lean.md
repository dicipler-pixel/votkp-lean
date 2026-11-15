# REPORT: lean (Appendix B Lean library) -- 12 Nov 2026

## Outcome: NOT BUILT. Static audit only.
The build stopped at the toolchain download, as the brief says to do. I did not look for another route.
- elan itself installed (binary from github.com/leanprover/elan releases, HTTP 302, allowed).
- `elan toolchain install leanprover/lean4:v4.34.1` failed: "error during download ... CONNECT tunnel failed, response 403".
  Refused host (from the proxy status log): **release.lean-lang.org:443** (CONNECT 403, policy denial). It is the host elan uses for the toolchain archive (the exact file path is not logged; the host is what the proxy refused).
- Consequence: no Lean, no `lake exe cache get`, no `lake build`, no Mathlib cache request made. Nothing below was compiled.
- Everything below is read from the sources (my own clone, repo commit fa9f8ea on main, shallow; Appendix B says "verified at commit bd4d15a, run 38326349740", which I did not check -- I did not run `git log` history, it is a depth-1 clone).

## Versions (taken from files, not run)
lean-toolchain: leanprover/lean4:v4.34.1. lakefile.toml: mathlib rev v4.34.1; libs VOTKP (glob VOTKP.+) and Showcase (Showcase, Showcase_WithProofs). config.json: expected_theorems 140, expected_false_controls 15, 15 root modules.

## Declaration counts from the sources (script /home/claude/closure/lean/count.py, repo's own THEOREM_RE, comments stripped)
Public `theorem` per module: Smith 21, Film 12, Peel 18, Knot 1, Ordinal 5, Energy 17, Observer 7, Curvature 5, Memory 4, ThinFilm 4, WallParity 3, Scaling 6, Directed 22, Channels 8, Witnesses 7. Sum = 140. Every module matches the README table and Appendix B (Smith 21 ... Witnesses 7). Fifteen modules: confirmed by file count.
`lemma` declarations (helpers, not counted in the 140): Observer 2, Curvature 2, Memory 15, ThinFilm 11, WallParity 2, Scaling 2, Directed 4, Channels 7, Witnesses 1, others 0. (A looser grep counting theorem+lemma gives 186 in total; the "140" is theorems only.)
No `private` theorems or `example`s inside VOTKP.

## Forbidden constructs
grep -w for sorry, axiom, admit, native_decide, unsafe, opaque over VOTKP/*.lean, Showcase*.lean, FalseControls/*.lean: **no hits** (also none in comments).

## #print axioms
Not run (no build). The repo's scripts/verify.py does this after `lake build` (allowed set propext, Classical.choice, Quot.sound); its CI is claimed green in README; I did not see the run.

## FalseControls (15 files, none compiled)
Files: BindingSign, CoefficientSign, CriticalOccupation, EqualWeights, FirstThresholdTotal, FootprintValue, LadderOrder, LaterTransmission, OneRadius, OutAndBack, ShellWall, ShiftSilent, ShowcaseAltered, ThirdCumulant, ZeroEntropy = 15, matching the claim. Each is a 4-10 line `example` of a statement that reads as false by inspection (e.g. LadderOrder asserts 1/3 = 2/4; ShellWall asserts (2*2-1)/(4+1)=1/2 while it is 3/5; ZeroEntropy asserts the swapped ladder has non-zero pattern entropy flag = false; ShowcaseAltered is a type mismatch). Whether each fails to compile "for a mathematical reason" is untested here.

## Appendix B numbered results -> Lean declaration
| Paper result | Lean declaration | Found |
|---|---|---|
| Thm 3.1 (1)-(5), horizon | Observer: same_future_iff, unseen_invariant, quotient_dim, summary_kernel, quotient_is_summary, closes_iff, horizon | found (7) |
| Thm 4.1 | Curvature: eigenvalues_HM, curvature, bloch_slope, metric_and_susceptibility, critical_occupation | found (5) |
| 5.1 | Peel: peel_lowers, peel_kernel | found |
| 5.2 | Peel: form_tomography | found |
| 5.3 | Peel: schur_memory | found |
| 5.4 | Memory: memory_kernel | found |
| 5.5 | Memory: moment_horizon, transfer_silence, shift5_moments | found |
| 5.6 | Peel: four_reading, coeff_pos_below, coeff_neg_between; Channels: four_reading_matrix, _sandwich, _kernel, kernel_active | found |
| 5.7 | Peel: phase_reference_re, _im, phase_error | found |
| 5.8 | Peel: cumulant_witness | found |
| 5.9 | Peel: transmission_closed, shared_records, later_outcomes | found |
| 5.10 | Peel: snapshot_value, snapshot_slope | found |
| Thm 6.1 | Film: echo_series, echo_resum (echo_derivative) | found |
| Thm 6.2 | Film: echo_circle, circle_identity, circle_criterion, one_radius_cannot_decide (combined statement not in Lean, per LIMITATIONS) | found (two steps) |
| Thm 6.3 | ThinFilm: thin_end_top, thin_end_substrate, and the two _remainder theorems | found |
| Prop 11.1 | WallParity: det_factor, sign_prod, parity_at_wall (order of zero is a hypothesis) | found |
| Thm 15.4 | Scaling: coulomb_homogeneous, kinetic_scaling, scale_blindness, dilation_inner, dilation_norm_sq, dilation_inverse | found |
| Prop 19.1 | Directed: directed_step, directed_reverse, oplus_closed, oplus_identity_inverse, directed_composite, shrinks_iff | found |
| Prop 19.2 | Directed: cancellation_defect, no_defect_iff, out_and_back | found |
| Prop 19.3 | Directed: lift_isospectral, gap_coordinate, lift_ground, projector_deriv, lift_metric, nonunique_lift | found |
| Prop 19.4 | Directed: lifted_length_bound, sq_integral_le, spectral_weighting, route_cost (bound is a hypothesis, as Appendix B says) | found |
| 19.6 | Directed: equal_weights_iff, weights_one_four, equal_populations_no_friction | found |
| A.12 | Knot: unit_circle_ratio | found |
| Control 41 (§18) | Ordinal: zero_entropy_not_identifying (+4 supporting) | found |
| 8.1, 15.1-15.3, shell wall | Smith: smith_identity, tanh_add', block_succ/block_smith, oplus_assoc, ladders_same_composite, round_trip, shell_wall, shell_wall_values (Smith doc comments say Thm 8.1, 15.1, Cor 15.2, 15.3) | found |
| §20.1 | Energy (17 theorems) | found |
| §20.3, §20.5.1 | Channels: retained_resolvent, channel_contour, commutator_coupling, footprint_example | found |
| §20.5.2-3, 20.5.5 | Witnesses: readout, same_present, opposite_futures, U_unitary, dephased_readout, offset_schur, offset_particle_hole | found |
Not found: none among the numbered results Appendix B names. (Note: Appendix B's Smith line cites "8.7" for the stagger; LIMITATIONS says the stagger classification is data and not formalized -- consistent.) Matching is by the doc-comment tags in the sources, not by compiling.

## v3.0 Propositions 22.1, 22.2, 22.3, 24.1: NO LEAN YET
None of them exists in the repo (clone at fa9f8ea; no Lean for §§22-24). Closest existing: Channels.commutator_coupling (Tr[H,P]^2 = -2 Tr BB^dagger) covers part of 22.1; Smith.tanh_add' and Film/Smith oplus lemmas cover the ingredients of 22.3. Statements I would formalise (text only):

**22.1.** For A : Matrix p p C, B : Matrix p q C, D : Matrix q q C, H = fromBlocks A B B^H D (A, D Hermitian), P = fromBlocks 1 0 0 0, E_B := sum_{i,j} |B i j|^2 (= Tr(B B^H) as a real number). Then (a) the Frobenius norm squared of P*H*(1-P) equals E_B; (b) (1/2) * (Frobenius norm squared of H*P - P*H) = E_B; (c) E_B = Re Tr(B * exp(-i*0*D) * B^H) i.e. the K(0) reading, K(t) = B * exp(-I t D) * B^H, K 0 = B * B^H. 

**22.2.** For reals d_i, d_j > 0, E_- = (d_i-d_j)^2, E_+ = (d_i+d_j)^2, z = d_i/d_j, G = tanh(log z / 2): (d_i-d_j)/(d_i+d_j) = G; E_-/E_+ = G^2; E_-/(E_- + E_+) = G^2/(1+G^2); (E_+ - E_-)/E_+ = 1 - G^2; E_- + E_+ = 2(d_i^2 + d_j^2); E_+ - E_- = 4 d_i d_j. (Half-line corollary: G^2 = 1/2 iff E_+ = 2 E_-, and G^2 = 1/2 iff z = 3 + 2*sqrt 2 for z > 1.)

**22.3.** For z > 0 and k : N, tanh((k/2) log z) = G (+) G (+) ... (+) G (k copies, oplus left-folded, oplus u v = (u+v)/(1+u v)) with G = tanh(log z / 2); equivalently peel coordinate (z^k - 1)/(z^k + 1) = that k-fold oplus (needs z^k > 0 only). Charge form: for Zc, Zv > 0, r = (Zc - Zv)/(Zc + Zv): (Zc^2 - Zv^2)/(Zc^2 + Zv^2) = r (+) r (denominator 1 + r^2 is nonzero).

**24.1.** (Statement is a reproduction of standard module theory; a Lean version is a finite-dimensional linear-algebra statement, not the knot table.) For a field K, V finite-dimensional, h : End V, lambda in K with dim ker(h - lambda) = 1 and dim ker((h-lambda)^2) = 2: then h - lambda restricted to the generalised eigenspace ker((h-lambda)^2) is nonzero and nilpotent with square zero, and the generalised eigenspace is one Jordan block (cyclic, K[t]/((t-lambda)^2)); conversely dim ker(h-lambda) = 2 = dim ker((h-lambda)^2) iff h - lambda = 0 on that eigenspace (two independent levels). The knot facts (Alexander module summand Z[t^+-1]/(f^2), membership of f in the second Alexander polynomial, the counts 376/199, 121/77) are data and stay outside Lean.

## Files
Clone: /home/claude/closure/lean/votkp-lean (read only). Script: /home/claude/closure/lean/count.py. elan binary tree: ~/.elan (installed, unusable for this toolchain). No file added to the repo.
