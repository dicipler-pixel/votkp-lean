# Notes: 30 October 2026 session on free-streaming neutrinos and primordial black holes (Steve McCormick's preprint)

Byline for any section built from these notes: Jeromie Beasley (AI-assisted).
Source: shared chat https://claude.ai/share/55012baa-3415-4c53-8566-4cff6d2e72e3.

COVERAGE: these notes cover only the first 50,000 of about 687,000 characters of the chat, up to the line
"The number check is back." The rest could not be read this session, because the browser request went unanswered.
Everything after that line (the number-check findings, the final Test B value, the paper's final file names
and any later decisions) is NOT recorded here yet.

Grades: [measured] = run in code or in Steve's simulation; [derived] = follows by algebra, checked numerically where noted;
[fitted] = numbers chosen after seeing data; [proposed] = untested prediction or idea.

## Steve's paper (his work)
- Preprint: free-streaming neutrinos and primordial black hole formation, apparent-horizon collapse in spherical general relativity with neutrino transport. Code and data: Zenodo 10.5281/zenodo.23808375.
- His results as quoted in the chat: the collapse threshold in the compaction measure rises about 9.7% (8.3 to 9.7% in his full model); collapse probability beta goes to about beta^1.18; a step in the mass function between 10^4 and 10^6 solar masses, near 1 MeV.
- Mass-scaling slope with and without neutrinos 0.266 against 0.268 (his Table III); the prefactor moves by x1.17 to 1.20; horizon-mass ratio about 1.19; linear scaling with neutrino fraction 0.235 R_nu.
- Gradual-decoupling shift curve G (share of the full free-streaming shift that survives), Gaussian profile: epsilon_dec 0.25, 0.5, 1, 2, 4, 8 gives G = 0.959, 0.867, 0.683, 0.431, 0.190, 0.063 (shifts 5.90, 5.33, 4.20, 2.65, 1.17, 0.39%).
- His open question (Section IV C): linear theory gives estimates of opposite sign and "does not determine which diagnostic, if any, predicts the nonlinear threshold". His missing control (Section IV D): same neutrino transport with plain radiation pressure p = e/3 against the full equation of state, horizon masses 3x10^6 to 1.6x10^7 solar masses.

## Comparison with Beyond the Event Horizon, edition 10.1
- Different objects: his apparent horizon in real spacetime against Jeromie's intrinsic metric on four-body shape space; Proposition 16 of the black-hole paper says projector data cannot supply a scale or a mass. All links are structural.
- Structural links noted: his threshold is a separatrix, a wall in a space of data (next to the "third kind", the moduli walls of section 4.5); law survives and amplitude changes (section 4); carry the invariant, do not rebuild it from near-cancelling parts (his Gamma instability); two effects of opposite sign decided by the full nonlinear run (sections 3.7, 9.7); "delay is not trapping" (section 5.5); section 9.4 (Andersson-Mars-Simon stability operator) applies directly to his marginally trapped surface.
- Abundance check [measured]: beta = erfc(C/(sqrt2 sigma)), threshold C from 0.662 to 0.726. At beta 10^-9, 10^-12, 10^-15 the ratios are 1/48, 1/189, 1/750 with exponents 1.187, 1.190, 1.192; his ranges 38-48, 140-190, 490-750. Matches the top of each range.
- Verdict asked ("who has the stronger hand"): physics Steve; mathematics and Lean Jeromie (event-horizon-lean, 40 theorems merged, CI green as of the 20 October record, not re-run that day).

## Round 1: kill test on three papers (agent, full reads)
Kill line [set before]: a result that computes something from Steve's numbers, or a new prediction his code can test. Parallels alone do not count.
- Light Keeps the Ledger 7.2: failed (its certificate tests positivity of a response function; nothing maps to a nonlinear collapse).
- The Ledger Outlives the Metric, edition 6: failed (scale invisibility, Proposition 30, cannot produce his exponent).
- Elemental Peeling v2.9: NOT a verdict; read only through section 15.10 (sections 15.11-22 and Appendices A-G unread). Its one test failed: the decoupling curve does not add like the peel rapidity; counting by optical depth fits better.
- Agent's own linear solver reproduced Steve's Appendix B (0.944 against 0.944) [measured]. Its "first maximum" estimate drops to zero by epsilon_dec about 2; the first maximum lands at epsilon about 1.7 while horizons form at epsilon about 4.0-4.5, so the threshold is decided in the window epsilon 1.7 to 4.5 [derived].

## Connection energy (Non-Normality Is Connection Energy) applied to Steve's collision operator
- Split H = D + A: transport A = -i k mu (free streaming), symmetric D = -kappa (I - P), P the projector onto the isotropic part.
- Non-normality energy = kappa^2 k^2 / 3 [derived; checked numerically on 40 angle points at three (k, kappa) pairs, exact agreement].
- The commutator [P, mu] links only the isotropic part to the flux, so all non-normality sits in the momentum channel (the kappa q drag of his Eq. 6); energy is conserved [derived].
- Two-moment truncation: exceptional point at kappa = 2k/sqrt3; below it oscillation at sound speed 1/sqrt3, above it overdamped. LATER SHOWN AN ARTIFACT: with the full angle range the slowest-damped mode turns real at kappa about 0.645 k (branch cut, not a clean exceptional point).
- Wall-crossing timing: first given as epsilon about 0.66 epsilon_dec^1.5; corrected (scaling error k/(aH) = k tau = k epsilon, not k/epsilon) to epsilon_EP = 0.811 epsilon_dec^0.75 [derived; confirmed independently by the Offset Speed Limit agent].
- Test (kill line: match G within 0.10, no fitted numbers): free-streaming average over epsilon 1 to 4, even and log weighting, both missed by 0.30 [measured, dead]. Viscosity repair: window from horizon entry all 12 versions failed (best 0.115); from Steve's start time one version passed at 0.089 (escape share k/(k+kappa), k = 2/r_m) [fitted by selection, 1 of 20]; after the scaling correction that pass vanished and a different single version passed, 1 of 32 [not counted, chance level].
- Split-rate formula [derived; verified to 10^-15]: E = k^2 kappa1^2 / 3 + (4 k^2 / 15)(kappa2 - kappa1)^2, kappa1 momentum-transfer rate, kappa2 shear-damping rate; non-normality only in the flux and shear links; flat in kappa2 at kappa2 = kappa1. Use for threshold motion [proposed, untested].

## Colour Selects the Leader agent
- Diffusive-escape law [fitted on Steve's curve, framing from the paper, physics textbook radiative diffusion]: G = 1 / (1 + sqrt15 (epsilon_dec / epsilon*)^1.5), epsilon* = 4.0 (Steve's perfect-fluid horizon time). Predicted 0.943, 0.854, 0.674, 0.422, 0.205, 0.084 against 0.959, 0.867, 0.683, 0.431, 0.190, 0.063; worst miss 0.02. Free-fit exponent 1.61. LATER KILLED by Test A (below).

## The Offset Speed Limit agent
- Scripts reproduce [measured]. Explains none of Steve's numbers: the bound measures root-mean-square speed (= 1/sqrt3 for isotropic neutrinos, bound hit to 0.99999 early); Steve's effect is the light-speed front.
- Every rate-ratio model with no fitted numbers missed (best 0.19); every linear-theory diagnostic missed [measured, dead].
- Logistic description: log-odds = 1.66 ln epsilon_dec - 0.81, worst miss 0.016 [fitted, two numbers on six points].
- Annihilation prediction [proposed]: plasma sound speed dips to 0.519 while neutrino average speed stays 1/sqrt3. Reading 1 (dip enhances): shift up about 13%, to 7.5% - fails against his 5.3-6.2%. Reading 2 (dip reduces): about -12%, 5.5-6.3% - passes weakly. Decided by his missing Section IV D control.
- Finding in Jeromie's own paper: the zip tests the offset speed limit (scripts C2-C5, Fig. 7) but the HTML text never states it.

## The Weight Between agent (closest to Steve's problem)
- The cut is Steve's collision model exactly: weight between streaming and isotropic parts = k^2/3, square root = sound speed times k [derived]. Hidden-walk formula gives Steve's exact neutrino density response to 16 decimal places [measured]. His single collision rate is the equality case of the ladder; energy-dependent rates make it strict [derived].
- Prediction [proposed]: if neutrino-neutrino collisions damp shear and higher parts but not the flux, 64% to 97.5% of the non-normality sits on the shear link, so his threshold should be far more sensitive to the shear-damping rate than to the momentum rate.
- "What the kept part retains" read at epsilon = 1.7: misses by 0.103 or 0.093 depending on wave size - near miss, not counted (within 0.02 up to epsilon_dec = 1); with a late-time weight 0.021 [fitted].
- Rung +1 candidate [proposed]: arithmetic mean of energy-group rates gives decoupling temperatures 1.62 MeV (his 1.6, electron-positron scattering alone), 1.02 MeV (his 0.93-1.0 with neutrino-neutrino scattering), mass step 2.53 (his 2.5-3). Harmonic and geometric means fail; rung +2 also passes, so a class of rungs.
- No handle anywhere on the 0.235, 0.15 and 1.19 numbers, the critical exponent, or the non-Gaussian question.

## Suns paper
- Jeromie's instinct to pull it: same transition (diffusion to free streaming at a surface), window-not-snapshot problem (transient growth, Kreiss), dynamo exceptional point from a full operator. Not read in that part of the session [proposed].

## New runs in Steve's own code (pre-registered; the check run landed inside his published bracket)
Test A, broad profile alpha = 0.3:
- epsilon_dec = 4: predicted by diffusive law tied to late collapse (epsilon about 7-9) 0.38-0.46, kill below 0.30; null "curve does not move" 0.19. MEASURED delta_c = 0.45337 +/- 0.00013, G = 0.181 +/- 0.004. Law dead; null survives.
- epsilon_dec = 8: law 0.17-0.24, kill below 0.13; null 0.063. MEASURED G = 0.045 +/- 0.004. Law dead; null survives.
- Result [measured, new beyond Steve's paper]: the clock that sets how much free streaming matters is set early; late collapse does not stretch it (if anything earlier). Candidate clocks horizon entry (epsilon = 1) or first compaction peak (epsilon about 1.7) [proposed, untested]. Opposite reading (law clock held at epsilon = 4) gives 0.205 - a fit to one curve, not a law.
Test B, Gaussian profile, collision rate kappa proportional to epsilon^-6, epsilon_dec = 2 (stiffness capped at the level his epsilon_dec = 8 runs handled; neutrinos isotropic to 2x10^-6 at the cap):
- Predictions (kill if miss by more than 0.08): diffusive escape 0.62; memory model (from The Weight Between) 0.25 (later recomputed 0.246); no-history model 0.43.
- Brackets: 0.25-0.52, then 0.25-0.38, then delta between 0.50731 and 0.50938 (G = 0.347 +/- 0.034), then after a parallel round delta between 0.50731 and 0.50800 (G 0.31-0.34). In the paper build the measured value is quoted as 0.317.
- Verdicts so far: diffusive escape dead; no-history model dead (needed G at least 0.35); memory model alive at the edge (survives only if G at or below 0.33). Steve's normal rate at the same epsilon_dec gives 0.431, so a steeper decoupling history lowers G by 0.05 to 0.12: history matters, but only partly [measured].
- The chance-pass form from the earlier search predicts 0.513 against 0.317 measured: dead.
- FINAL Test B value and verdict: in the unread part of the chat.

## Literature scan (agent; read where marked)
- No arXiv version or response to Steve's paper found (weak evidence; Zenodo page not opened).
- Yuwen et al., bulk viscosity raises the threshold, arXiv:2606.26532.
- Gonin, Escriva, Kuhnel et al., thermal-history equation of state 10 GeV to 1 keV with neutrinos in the fluid, arXiv:2608.22240.
- Papanikolaou, threshold fixed at horizon crossing following sound speed, arXiv:2205.07748 (read).
- Escriva, set by initial profile and compaction curvature at its peak, arXiv:2504.05814 (read).
- Dave et al., mu-distortion blocks Gaussian supermassive seeds, arXiv:2607.03138.
- Hu, branch cuts generic in relaxation models, arXiv:2409.05131; Romatschke, retarded correlators in kinetic theory, arXiv:1512.02641.
- Gaps nobody has filled: critical collapse of radiation plus collisionless matter; threshold against when a collision rate switches on relative to horizon entry; gradual kinetic decoupling in a full collapse simulation; a mass function with the free-streaming step. Tests A and B sit in the second and third.

## The paper (as far as the read part goes)
- Decision: write it up fully, nothing left behind, citing Steve, byline Jeromie Beasley, one PDF with paper, proofs and code (Type 1 fonts, AI-assisted line above the abstract), plus HTML and a Zenodo zip, saved to Drive "Chat Outputs".
- Suggested working title: "When the Neutrinos Leave: Decoupling History and the Threshold for Primordial Black Hole Formation" (his call; not confirmed in the read part).
- Planned structure: the question; the collision model through his operator tools (kappa^2 k^2/3, split-rate formula, exact density propagator); what does not set the threshold (truncated wall, first maximum, diffusive escape, no-history model, each with its pre-written kill line); new measurements (Tests A and B); predictions Steve can run (annihilation sound-speed control, shear-rate sensitivity, R_nu independence check); appendices with proofs and every script.
- Citations staged: Non-Normality Is Connection Energy, The Offset Belongs to the Boundary, Light Keeps the Ledger, the gravity ledger, Dirac Time, UPG and IQGT by DOI; The Weight Between, The Offset Speed Limit and Colour Selects the Leader by title and version (no DOI found); Steve's preprint.
- Build notes: five identities checked to 12 digits; figures fixed; citations fixed in HTML with numbered references; paper, HTML and code zip built; number-checker run. Its findings, the final file names and any DOI are in the unread part.

## Open, untested or still to read
- Read the rest of the chat (from "The number check is back.") and add: number-check findings, final Test B verdict, final title, file names, Zenodo record.
- Elemental Peeling v2.9 sections 15.11-22 and Appendices A-G against Steve's problem (never read in this round).
- Suns paper against the window problem.
- Which early clock (horizon entry or first compaction peak) sets the effect.
- Steve's Section IV D annihilation control; the shear-rate sensitivity; the R_nu independence check.
