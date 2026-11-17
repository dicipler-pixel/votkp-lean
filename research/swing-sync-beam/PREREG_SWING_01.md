# PREREG_SWING_01 — the swing, the open end and the bigger container
Jeromie Beasley. Written 16 Nov 2026 (Central), before any run. AI-assisted.
Script: SWING_TEST_01 (swing_test_01.py). Nothing in this file is changed after the first run; results go in a separate file.

## The ideas under test (his, in his words where given)
N1. The ground state, the sea of electrons, is "like a swing", a "cosmic sync beam".
N2. Is it "a charged loop like structure that holds itself together shut, all energy conserved", or "an open container on some end",
    or "no end no background"?
N3. An open end loses a little each cycle and needs feeding, "unless it is in another even bigger container, then it may just be a
    compression of sorts".
N4. "If you want to get energy you must kick it like a photon" (in time with the swing).
N5. The open question on the beam: everywhere at once, or must the sync travel along the links like light. A third option raised in
    talk: the swing at rest is everywhere, and only changes to it travel.

## The model (stated so every line can be checked)
A line of stretches of field joined by faces. Light crosses one cell per step at speed 1. A face with step ratio z has Smith coordinate
Γ = (z − 1)/(z + 1) and scatters by the proved rule: return Γ², pass 1 − Γ² (step_matching, flux_balance). An end is a mirror (|Γ| = 1,
everything returns) or a matched load (Γ = 0, nothing returns). A swing is the light held between two faces; its period is the round
trip, 2L. No law of motion for the faces, no torque, no locking: this model is linear. MODEL CHOICE: one dimension; face signs
(+ρ seen from the left, −ρ from the right).

## Tests, why each decides its claim, and the kill line (fixed now)
T1 SEALED. Mirror, stretch L, mirror. If the loop is shut, nothing can leave, so the swing must return exactly.
   KILL: energy differs from 1 by more than 1e-12 at any step, or the state at step 2L differs from the start by more than 1e-12.
T2 OPEN END. Mirror, swing L, face Γ, stretch, matched load. Each meeting with the face keeps Γ² and passes the rest, and the load
   returns nothing. So after n meetings the swing holds exactly Γ^(2n).
   KILL: |held − Γ^(2n)| > 1e-12 for any n ≤ 20; or held + absorbed + in transit ≠ 1 to 1e-12.
T3 BIGGER CONTAINER (N3). Same swing, but the outside stretch D ends in a mirror. Derived before the run: what leaves at step L comes
   back into the swing at step L + 2D and not one step earlier, so the two runs (open end, bigger container) must agree exactly until
   then and differ from then on. Books over swing plus container stay 1.
   KILL: the two runs differ before step L + 2D; or do not differ at step L + 2D; or total ≠ 1 to 1e-12.
T3b IN TIME (N3, "a compression of sorts"). D = L, so what left meets the swing again at the face at the same instant. Derived: a
   lossless two-sided face is its own inverse on the pair (inside, outside) (a real symmetric scattering with determinant −1), so the
   swing must hold Γ² after odd meetings and exactly 1 after even meetings: the whole loss comes back. Holds for either face sign.
   KILL: held after meeting n differs from Γ² (n odd) or 1 (n even) by more than 1e-12, n ≤ 20. Run with both face signs.
T4 THE SQUEEZE DOES WORK (N3, N4). Swing between a fixed mirror and a mirror that moves, L(t) = L0(1 + a sin(Ωt + φ)); exact rays
   (each ray's meeting time with the wall is solved, nothing is imposed). Derived: one meeting with a wall moving at v multiplies the
   pulse energy by D = (1 − v)/(1 + v) (v > 0 moving away). With Ω = π/L0 the pulse meets the wall at the same phase every time.
   a = 0.01, so v0 = aπ and D0 = (1 + v0)/(1 − v0).
   T4a IN TIME, wall moving in at each meeting (φ = 0): energy after 20 meetings = D0^20.   KILL: off by more than 1%.
   T4b IN TIME, wall moving out (φ = π): energy after 5 meetings = D0^(−5) (energy handed back).   KILL: off by more than 1%.
   T4c OUT OF TIME (Ω × golden ratio): no net gain.   KILL: |mean log gain per meeting| over 200 meetings > 0.1 ln D0.
   T4d BOOKS: energy gained = work done by the wall, with wall pressure 2 × (incident energy density) × D. At v → 0 this is the
       pressure 2R with R = 1.   KILL: |gain − work| / |gain| > 1e-3 over the 20 meetings of T4a.
   Grade if it holds: REPRODUCTION (Doppler at a moving mirror and radiation pressure are textbook), shown in the face language.
T5 THE SWING'S RATE MOVES WITH THE SQUEEZE (N3). Wall moves in slowly at v = 1e-3 from L0 to 0.8 L0. Derived: energy × length is kept,
   so energy rises by 1/0.8 = 1.25, and the period falls to 0.8 of its start. A leak (T2) changes neither the period nor raises energy.
   KILL: energy ratio off 1.25 by more than 1%; period ratio off 0.8 by more than 1%.
T6 THE SEA: EVERYWHERE AT REST, CHANGES TRAVEL (N1, N5). Two swings A and B (6 cells each, faces z = 3) joined by a link of 20 cells,
   mirrors at both ends: a sealed loop. One step is a matrix V. The rest sea is the projector P onto half of V's spectrum (the half
   with negative imaginary part). MODEL CHOICE: that half; it is a rest state of V by construction, checked.
   T6a REST: V P V† = P.   KILL: differs by more than 1e-12.
   T6b TIED AT REST: the weight between A and B, X = ‖P_AB‖², is not zero though nothing is moving.   KILL: X ≤ 1e-12.
   T6c CHANGES TRAVEL: kick one cell of A (a local reflection), then step. The sea on B must not change by even 1e-12 before the
       crossing step t× = 24 (the kicked right-mover sits at cell 2; B starts at cell 26), and must change after.
       KILL: any change above 1e-12 on B before step 24; or no change above 1e-9 by step 72.
   T6d ALL AT ONCE (the Moving Matrix way), for contrast: three balls, one matrix H = D + A with direct links c0·sech(d/2), sea = levels
       below the largest gap, kick ball A, move by e^(−iHt). The far ball must already have changed at 1% of the light-crossing time.
       KILL: change on the far ball at t = 0.01·d is below 1e-8.
   What T6 would say if all hold: the third option is a consistent machine (tied at rest and causal together), and the two machines
   differ in reading 1 (when the far sea first moves). It would NOT say which one nature uses.

## Looks with no kill line (exploring, not testing)
E1. Bigger container, D/L = 1, 2, 3, 1.5, √2, golden: the most the swing gets back within 400 round trips.
E2. The weight between A and B at rest against link length 10, 20, 40, 80.

## Not in this test
Locking and gear locking (needs a law that pulls rates; this model is linear). The clock ratio z. The electron sea with interactions.
Any claim about which container the universe is.
