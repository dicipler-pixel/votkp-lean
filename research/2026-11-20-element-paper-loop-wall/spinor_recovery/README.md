# Recovered spinor-peel and SARNS-coupling math (checked)

Source: Jeromie Beasley's December, October and March drafts (UFSKO / EFRO / SARNS / CRFZD), as recovered with
ChatGPT on 21 November 2026 (`recovered_spinor_peel_notes_from_gpt.md`). Every runnable statement was checked
numerically in `check_spinor_recovery_v1.py` (output beside it). All checks pass.

| Statement | Check | Result |
|---|---|---|
| Peel identity ι†A²ι − (ι†Aι)² = (QAι)†(QAι) | random 6×6 Hermitian, 2-dim layer | error 1e-14 |
| Three-mode loop: spectrum depends only on cos Φ | Φ = ±0.7 | identical eigenvalues; characteristic polynomial λ³ − 3J²λ − 2J³cos Φ |
| Direction sees Im(W): P(1→2) − P(2→1) ≈ 2 Im(W) τ³ | τ = 0.01, 0.05 | agrees to leading order, sign flips with Φ |
| Perfect cycling at Φ = ±π/2, τ = 2π/(3√3 J) | evolution matrix | +π/2 sends 1→2→3→1 with probability 1; −π/2 reverses |
| Eliminating mode 3: J_eff(E) = J + J² e^(−iΦ)/E, diagonal shift J²/E | Schur complement | exact; true eigenvalues solve the reduced equation |
| Memory form of the peel | full evolution vs the integral equation | residual 5e-7 (finite-difference) |
| Torus Dirac operator: D² = (2π)²[(m+α)² + (n+β)²], ± pairing, η = 0 | σ₃ anticommutes with D | holds; smallest level π at shifts (½, 0) |

Prior art: perfect directional transfer on a triangle with a loop phase is the known chiral quantum walk
(Zimborás et al., Scientific Reports 3, 2361, 2013). What is new here is its use as a control for the peel.

How it joins the element paper: the energy ledger sees Re(W) = J³ cos Φ, which is even under reversal, like Γ².
The directional test sees Im(W) = J³ sin Φ, which is odd, like the sign of Γ and the screw sign χ. Eliminating a
mode keeps its phase only if the elimination is done properly (Schur complement, or the memory integral); plain
deletion loses it. That is the same distinction as PR #16's side-coupled orbital in operator-first.
