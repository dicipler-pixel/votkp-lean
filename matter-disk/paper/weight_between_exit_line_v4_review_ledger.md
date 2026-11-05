# Ledger: The Weight Between and the Exit Line, v3 -> v4

Files: LaTeX `paper/weight_between_exit_line_v4.tex` (from `_v3.tex`); HTML template `exit_line_template_v4.html` (from `_v3.html`), built by `build_html_v4.py` into `weight_between_exit_line_v4.html`; zip folder `zen4/weight_between_exit_line_v4_code_and_proofs/`.

## Finding 1: Qualify "pure state"

**weight_between_exit_line_v4.tex**, Abstract, paragraph 1

Old:

```
It lies below the local defect $C_A-C_A^2$, and equals it on a pure state.
```

New:

```
It lies below the local defect $C_A-C_A^2$. For a pure Gaussian (Slater) state, $C$ is an orthogonal projector and $X_A=A_C-A_C^2$.
```

**weight_between_exit_line_v4.tex**, Section 3, paragraph "The boundary coordinate"

Old:

```
On a pure state $\lambda=\nu(1-\nu)$, so $\Gamma_b=|1-2\nu|$
```

New:

```
For a pure Gaussian (Slater) state, $C$ is an orthogonal projector, $X_A=A_C-A_C^2$ and $\lambda=\nu(1-\nu)$, so $\Gamma_b=|1-2\nu|$
```

**weight_between_exit_line_v4.tex**, Appendix B.2

Old:

```
\subsection*{B.2 \texttt{s16\_weight\_between\_checks.py}}
\lstinputlisting[language=Python]{../scripts/s16_weight_between_checks.py}
\lstinputlisting{../outputs/s16_weight_between_checks.txt}
```

New:

```
\subsection*{B.2 \texttt{s16\_weight\_between\_checks\_v2.py}}
\lstinputlisting[language=Python]{../scripts/s16_weight_between_checks_v2.py}
\lstinputlisting{../outputs/s16_weight_between_checks_v2.txt}
```

**exit_line_template_v4.html**, Abstract, paragraph 1

Old:

```
It lies below the local defect $C_A-C_A^2$, and equals it on a pure state.
```

New:

```
It lies below the local defect $C_A-C_A^2$. For a pure Gaussian (Slater) state, $C$ is an orthogonal projector and $X_A=A_C-A_C^2$.
```

**exit_line_template_v4.html**, Figure 1 caption

Old:

```
On a pure state $T_A=0$ and the census reads the boundary alone.
```

New:

```
For a pure Gaussian (Slater) state, $C$ is an orthogonal projector, $T_A=0$ and the census reads the boundary alone.
```

**exit_line_template_v4.html**, Figure 1 drawing code, bar label

Old:

```
['pure state  (C² = C)',0,1]
```

New:

```
['pure Slater state  (C² = C)',0,1]
```

**exit_line_template_v4.html**, Section 3, "The boundary coordinate"

Old:

```
On a pure state $\lambda=\nu(1-\nu)$, so $\Gamma_b=|1-2\nu|$
```

New:

```
For a pure Gaussian (Slater) state, $C$ is an orthogonal projector, $X_A=A_C-A_C^2$ and $\lambda=\nu(1-\nu)$, so $\Gamma_b=|1-2\nu|$
```

**exit_line_template_v4.html**, Evidence panel s16

Old:

```
<summary>s16_weight_between_checks.py · controls for §3</summary>
```

New:

```
<summary>s16_weight_between_checks_v2.py · controls for §3</summary>
```

- Script copy `scripts/s16_weight_between_checks_v2.py` (from `s16_weight_between_checks.py`): first line `# SCRIPT: s16_weight_between_checks_v2`; label `pure states (100)` -> `orthogonal projectors (pure Slater states) (100)`; comment `# pure states: census recovery` -> `# orthogonal projectors (pure Slater states): census recovery`; output path `../outputs/s16_weight_between_checks.txt` -> `../outputs/s16_weight_between_checks_v2.txt`. New output `outputs/s16_weight_between_checks_v2.txt`.
- Zenodo description: no Zenodo description file for this paper was found in the repo or scratchpad, so none was edited.

## Finding 2: Keep the spectral exit law conditional

**weight_between_exit_line_v4.tex**, Abstract, paragraph 3

Old:

```
We construct an operator $T_R=\tfrac12\{X+\tfrac12,H\}_R$ that commutes exactly with the half-chain correlation block. The proof uses only $H(k)^2=E(k)^2I$, so it holds without Hermiticity. On its eigenvectors the entanglement levels form a ladder $\varepsilon_j=j\Delta+i\theta$. The spacing is $\Delta=2\pi K'(k)/K(k)$, with modulus $k=v'/w'$ taken from the Hermitian band hidden in the opened one. The single shared phase is $\theta=\pi F(\arcsin s\,|\,k)/K(k)$, with $s=uw/(w^2-v'^2)$. We prove that a ladder of this form crosses the unit circle of the Cayley chart all at once, and that its phase reaches $\pi/2$ exactly on the Petermann line. Both directions are proved, the converse through an explicit factorisation. The ladder form and the phase formula are verified at 200 random parameter points: commutation to $8\times10^{-12}$, spacing to $2\times10^{-8}$, phase to $4\times10^{-7}$, and the inside/outside verdict 200 of 200. They are proved in the dimer limit. Deriving them analytically from the commuting operator is the one step left open, and it is stated as such.
```

New:

```
We construct a linearly weighted operator $T_R=\tfrac12\{X+\tfrac12,H\}_R$ that commutes entrywise with the half-chain correlation block. The proof uses only $H(k)^2=E(k)^2I$, so it holds without Hermiticity. At 200 sampled gapped parameter points, its tested low-index edge eigenvectors exhibit an equally spaced entanglement ladder $\varepsilon_j=j\Delta+i\theta$ with a shared phase described by an elliptic integral. The spacing is $\Delta=2\pi K'(k)/K(k)$, with modulus $k=v'/w'$ taken from the Hermitian band hidden in the opened one. The phase is $\theta=\pi F(\arcsin s\,|\,k)/K(k)$, with $s=uw/(w^2-v'^2)$. On the tested levels the eigenvector residual is below $8\times10^{-12}$, the spacing agrees to $2\times10^{-8}$, the phase to $4\times10^{-7}$, and the inside/outside verdict holds at 200 of 200 points. For this proposed ladder, we prove simultaneous crossing of the Cayley unit circle and show that its phase reaches $\pi/2$ exactly on the band-averaged Petermann line $\langle K\rangle=2$, in both directions, the converse through an explicit factorisation. The dimer limit is proved exactly. An analytic derivation of the ladder for the coupled chain remains open.
```

**weight_between_exit_line_v4.tex**, Section 1, paragraph 4 (mechanism narrative)

Old:

```
An operator commutes exactly with the half-chain block, and its eigenvectors organise the levels into a ladder with one shared phase.
```

New:

```
An operator commutes exactly with the half-chain block, and numerically, the tested edge levels follow a ladder with one shared phase.
```

**weight_between_exit_line_v4.tex**, Section 5.5, paragraph "The open step"

Old:

```
\paragraph{The open step.} Theorem~\ref{thm:commute} fixes the eigenvectors.
```

New:

```
\paragraph{The open step.} Theorem~\ref{thm:commute} supplies invariant eigenspaces of $T_R$ for $C_R$; completeness or diagonalizability of $T_R$ is not claimed.
```

**weight_between_exit_line_v4.tex**, Status table, ladder-crossing row

Old:

```
Ladder crosses the rim all at once; its phase is $\pi/2$ exactly on the Petermann line (both directions); dimer limit & \grade{T}\\
```

New:

```
Conditional ladder crossing (any ladder of the stated form) and exact crossing of the proposed phase on the Petermann line & \grade{T}\\
Dimer limit, exact & \grade{T}\\
```

**exit_line_template_v4.html**, Abstract, paragraph 3

Old:

```
<p>We construct an operator $T_R=\tfrac12\{X+\tfrac12,H\}_R$ that commutes exactly with the half-chain correlation block. The proof uses only $H(k)^2=E(k)^2I$, so it holds without Hermiticity. On its eigenvectors the entanglement levels form a ladder $\varepsilon_j=j\Delta+i\theta$. The spacing is $\Delta=2\pi K'(k)/K(k)$, with modulus $k=v'/w'$ taken from the Hermitian band hidden in the opened one. The single shared phase is $\theta=\pi F(\arcsin s\,|\,k)/K(k)$, with $s=uw/(w^2-v'^2)$. We prove that a ladder of this form crosses the unit circle of the Cayley chart all at once, and that its phase reaches $\pi/2$ exactly on the Petermann line. Both directions are proved, the converse through an explicit factorisation. The ladder form and the phase formula are verified at 200 random parameter points: commutation to $8\times10^{-12}$, spacing to $2\times10^{-8}$, phase to $4\times10^{-7}$, and the inside/outside verdict 200 of 200. They are proved in the dimer limit. Deriving them analytically from the commuting operator is the one step left open, and it is stated as such.</p>
```

New:

```
<p>We construct a linearly weighted operator $T_R=\tfrac12\{X+\tfrac12,H\}_R$ that commutes entrywise with the half-chain correlation block. The proof uses only $H(k)^2=E(k)^2I$, so it holds without Hermiticity. At 200 sampled gapped parameter points, its tested low-index edge eigenvectors exhibit an equally spaced entanglement ladder $\varepsilon_j=j\Delta+i\theta$ with a shared phase described by an elliptic integral. The spacing is $\Delta=2\pi K'(k)/K(k)$, with modulus $k=v'/w'$ taken from the Hermitian band hidden in the opened one. The phase is $\theta=\pi F(\arcsin s\,|\,k)/K(k)$, with $s=uw/(w^2-v'^2)$. On the tested levels the eigenvector residual is below $8\times10^{-12}$, the spacing agrees to $2\times10^{-8}$, the phase to $4\times10^{-7}$, and the inside/outside verdict holds at 200 of 200 points. For this proposed ladder, we prove simultaneous crossing of the Cayley unit circle and show that its phase reaches $\pi/2$ exactly on the band-averaged Petermann line $\langle K\rangle=2$, in both directions, the converse through an explicit factorisation. The dimer limit is proved exactly. An analytic derivation of the ladder for the coupled chain remains open.</p>
```

**exit_line_template_v4.html**, Section 1, paragraph 4

Old:

```
An operator commutes exactly with the half-chain block, and its eigenvectors organise the levels into a ladder with one shared phase.
```

New:

```
An operator commutes exactly with the half-chain block, and numerically, the tested edge levels follow a ladder with one shared phase.
```

**exit_line_template_v4.html**, Open step

Old:

```
The open step.</strong> Theorem 5.2 fixes the eigenvectors.
```

New:

```
The open step.</strong> Theorem 5.2 supplies invariant eigenspaces of $T_R$ for $C_R$; completeness or diagonalizability of $T_R$ is not claimed.
```

**exit_line_template_v4.html**, Status, ladder-crossing row

Old:

```
<tr><td>Ladder crosses the rim all at once; its phase is $\pi/2$ exactly on the Petermann line (both directions); dimer limit</td><td><span class="g">T</span></td></tr>
```

New:

```
<tr><td>Conditional ladder crossing (any ladder of the stated form) and exact crossing of the proposed phase on the Petermann line</td><td><span class="g">T</span></td></tr>
<tr><td>Dimer limit, exact</td><td><span class="g">T</span></td></tr>
```

- The 200-point figures quoted in the abstract are kept as rounded upper bounds (8e-12, 2e-8, 4e-7); the word "commutation" before 8e-12 is replaced by "eigenvector residual" (also finding 4).

## Finding 3: Numerical provenance and reproducibility

**weight_between_exit_line_v4.tex**, Section 4, paragraph after Proposition 4.2

Old:

```
differences $4\times10^{-8}$ and below \grade{V}
```

New:

```
differences of about $5\times10^{-8}$ or less in these runs \grade{V}
```

**exit_line_template_v4.html**, Section 4, paragraph after Proposition 4.2

Old:

```
differences $4\times10^{-8}$ and below <span class="g v">V</span>
```

New:

```
differences of about $5\times10^{-8}$ or less in these runs <span class="g v">V</span>
```

- README (zip `README.md`): title `(v3)` -> `(v4)`; `weight_between_exit_line_v3.tex` -> `weight_between_exit_line_v4.tex`; `outputs/` row `exactly as quoted` -> `from the reference run quoted in the paper`.
- README: old sentence `Rerunning `s15`, `s16`, `s17` and `s18` reproduces their output files byte for byte. The outputs of `s05b`, `s06`, `s11` and the filter audit are the reruns of 4 November 2026, saved as `*_rerun_20261104.txt`.` replaced by three paragraphs: reference-run and tolerance statement (with the independent rerun values 1.43e-8, 3.69e-7, 5.84e-7, +3.97e-8/−5.06e-10/−4.19e-8 as an example), the list of v2 outputs and retained v3 scripts, and the reference environment: Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1, SymPy 1.14.0, mpmath 1.3.0, Matplotlib 3.11.2, Linux x86_64 (glibc 2.39), scipy-openblas (OpenBLAS 0.3.34), `OPENBLAS_NUM_THREADS=1`.
- The 400×400-grid sentence on max s is removed from the Statement 5.3 evidence (see finding 4 entries, PDF and HTML), replaced by a citation of the domain lemma (finding 6).

## Finding 4: Describe exactly what the tests measure

**weight_between_exit_line_v4.tex**, Section 3, evidence paragraph after Proposition 3.9

Old:

```
Script \texttt{s16} checks the saturation to $5.9\times10^{-15}$. It also checks every inequality of this section on 400 random contractions and 64 interior covariances. All bounds hold, the sharp ratio runs $4.00027$, $4.0000027$, $4.00000002$, and the pure-state recovery holds to $6.8\times10^{-16}$ \grade{V}.
```

New:

```
Script \texttt{s16\_weight\_between\_checks\_v2} checks the saturation to $5.9\times10^{-15}$. On 400 random contractions it checks the defect identity, the two order diagnostics, the positive-spectrum agreement, the ordered-eigenvalue comparison and the norm-stability estimate. On 64 interior covariances it checks the two information inequalities. It also checks the sharp family, whose ratio runs $4.00027$, $4.0000027$, $4.00000002$, and 100 orthogonal projectors (pure Slater states), on which $X_A=A_C-A_C^2$ holds to $6.8\times10^{-16}$. All checked bounds hold \grade{V}.
```

**weight_between_exit_line_v4.tex**, Statement 5.3, evidence paragraph

Old:

```
\noindent\emph{Evidence} (script \texttt{s15}).
```

New:

```
\noindent\emph{Evidence} (script \texttt{s15\_exit\_ladder\_v2}).
```

**weight_between_exit_line_v4.tex**, Statement 5.3, evidence list

Old:

```
\item the eigen-residual of $C_R$ on the edge eigenvectors of $T_R$ is at most $8.4\times10^{-12}$;
\item the relative spacing error is at most $1.7\times10^{-8}$;
\item the phase error is at most $4.2\times10^{-7}$ on the levels $j=0,\pm1$;
\item the domain condition $s<1$ holds, with maximum $0.913$ at the test points and $1-4\times10^{-8}$ on a $400\times400$ grid of the whole gapped region, where $s\to1$ only at the critical line.
```

New:

```
\item the eigenvector residual $\|C_Rr-\nu r\|$ is at most $8.4\times10^{-12}$ over 600 selected levels, three per point ($j=0,\pm1$); every point contributes all three, and the residual filter removes none. This is a residual on selected eigenvectors, not an operator norm of $[C_R,T_R]$;
\item the relative spacing error is at most $1.7\times10^{-8}$ over 400 spacing pairs, none skipped by the script's $\Delta\ge40$ rule;
\item the phase error is at most $4.2\times10^{-7}$ on the levels $j=0,\pm1$;
\item the domain condition $0<s<1$ holds on the whole gapped region by the domain lemma; at the test points the maximum is $0.913$.
```

**weight_between_exit_line_v4.tex**, Section 5.4, evidence after the proof of Theorem 5.4

Old:

```
Script \texttt{s15} returns $|\theta-\pi/2|
```

New:

```
Script \texttt{s15\_exit\_ladder\_v2} returns $|\theta-\pi/2|
```

**weight_between_exit_line_v4.tex**, Section 5.5 item 2, s11 reference

Old:

```
independent of block size (script \texttt{s11}).
```

New:

```
independent of block size (script \texttt{s11\_exit\_quarter\_turn\_v2}).
```

**weight_between_exit_line_v4.tex**, Appendix B.1

Old:

```
\subsection*{B.1 \texttt{s15\_exit\_ladder.py}}
\lstinputlisting[language=Python]{../scripts/s15_exit_ladder.py}
\lstinputlisting{../outputs/s15_exit_ladder.txt}
```

New:

```
\subsection*{B.1 \texttt{s15\_exit\_ladder\_v2.py}}
\lstinputlisting[language=Python]{../scripts/s15_exit_ladder_v2.py}
\lstinputlisting{../outputs/s15_exit_ladder_v2.txt}
```

**weight_between_exit_line_v4.tex**, Appendix B.8

Old:

```
\subsection*{B.8 \texttt{s11\_exit\_quarter\_turn.py}}
```

New:

```
\subsection*{B.8 \texttt{s11\_exit\_quarter\_turn\_v2.py}}
```

**weight_between_exit_line_v4.tex**, Appendix B.8 listings

Old:

```
\lstinputlisting[language=Python]{../scripts/s11_exit_quarter_turn.py}
\lstinputlisting{../outputs/s11_exit_quarter_turn_rerun_20261104.txt}
```

New:

```
\lstinputlisting[language=Python]{../scripts/s11_exit_quarter_turn_v2.py}
\lstinputlisting{../outputs/s11_exit_quarter_turn_v2.txt}
```

**exit_line_template_v4.html**, Section 3, evidence after Proposition 3.9

Old:

```
Script <code>s16</code> checks the saturation to <span class="num">5.9e-15</span>. It also checks every inequality of this section on 400 random contractions and 64 interior covariances. All bounds hold, the sharp ratio runs <span class="num">4.00027</span>, <span class="num">4.0000027</span>, <span class="num">4.00000002</span>, and the pure-state recovery holds to <span class="num">6.8e-16</span> <span class="g v">V</span>.
```

New:

```
Script <code>s16_weight_between_checks_v2</code> checks the saturation to <span class="num">5.9e-15</span>. On 400 random contractions it checks the defect identity, the two order diagnostics, the positive-spectrum agreement, the ordered-eigenvalue comparison and the norm-stability estimate. On 64 interior covariances it checks the two information inequalities. It also checks the sharp family, whose ratio runs <span class="num">4.00027</span>, <span class="num">4.0000027</span>, <span class="num">4.00000002</span>, and 100 orthogonal projectors (pure Slater states), on which $X_A=A_C-A_C^2$ holds to <span class="num">6.8e-16</span>. All checked bounds hold <span class="g v">V</span>.
```

**exit_line_template_v4.html**, Figure 2 caption

Old:

```
The 200 points of the ladder test (script <code>s15</code>)
```

New:

```
The 200 points of the ladder test (script <code>s15_exit_ladder_v2</code>)
```

**exit_line_template_v4.html**, Statement 5.3 evidence

Old:

```
<p class="evidence"><em>Evidence</em> (script <code>s15</code>).
```

New:

```
<p class="evidence"><em>Evidence</em> (script <code>s15_exit_ladder_v2</code>).
```

**exit_line_template_v4.html**, Checks band, residual tile

Old:

```
<span>largest eigen-residual of $C_R$ on the edge eigenvectors of $T_R$</span>
```

New:

```
<span>largest eigenvector residual $\|C_Rr-\nu r\|$ over 600 selected levels, three per point; not an operator norm of $[C_R,T_R]$</span>
```

**exit_line_template_v4.html**, Checks band, spacing tile

Old:

```
<span>largest relative error of the spacing $\Delta=2\pi K'/K$</span>
```

New:

```
<span>largest relative error of the spacing $\Delta=2\pi K'/K$, over 400 spacing pairs</span>
```

**exit_line_template_v4.html**, Evidence paragraph after checks band

Old:

```
<p class="evidence">The domain condition $s&lt;1$ holds, with maximum <span class="num">0.913</span> at the test points and <span class="num">1 − 4e-8</span> on a 400×400 grid of the whole gapped region, where $s\to1$ only at the critical line.
```

New:

```
<p class="evidence">Every point contributes all three selected levels ($j=0,\pm1$), and the residual filter removes none; no spacing pair is skipped by the script's $\Delta\ge40$ rule. The domain condition $0&lt;s&lt;1$ holds on the whole gapped region by the domain lemma; at the test points the maximum is <span class="num">0.913</span>.
```

**exit_line_template_v4.html**, Section 5.4 evidence

Old:

```
Script <code>s15</code> returns
```

New:

```
Script <code>s15_exit_ladder_v2</code> returns
```

**exit_line_template_v4.html**, Section 5.5 item 2

Old:

```
independent of block size (script <code>s11</code>).
```

New:

```
independent of block size (script <code>s11_exit_quarter_turn_v2</code>).
```

**exit_line_template_v4.html**, Evidence panel s15

Old:

```
<summary>s15_exit_ladder.py · the 200-point ladder test</summary>
```

New:

```
<summary>s15_exit_ladder_v2.py · the 200-point ladder test</summary>
```

**exit_line_template_v4.html**, Evidence panel s11

Old:

```
<summary>s11_exit_quarter_turn.py · census rotation
```

New:

```
<summary>s11_exit_quarter_turn_v2.py · census rotation
```

- New script `scripts/s15_exit_ladder_v2.py` (from `s15_exit_ladder.py`): first line `# SCRIPT: s15_exit_ladder_v2`; docstring adds a v2 note; `if not lv: print(...); continue` -> `assert lv`; candidates `cand` (|Re ε| < 1.5Δ) separated from `use` (residual < 1e-6); asserts `len(cand)==len(use)` and `len(use)==3` per point; counts per-point levels, levels removed by the residual filter, spacing pairs used and pairs skipped by the Δ≥40 rule; three new printed lines; output path -> `../outputs/s15_exit_ladder_v2.txt`. The `out=[]` split marker is unchanged, so `fig09` exec still works.
- New script `scripts/s11_exit_quarter_turn_v2.py` (from `s11_exit_quarter_turn.py`): first line `# SCRIPT: MATTER-DISK-S11-V2 ...`; KILL comment `the gap at block 160 is not smaller than at block 20, or exceeds 2e-3 at block 160.` -> `the gap at block 160 exceeds the gap at block 20 by more than 1e-9, or exceeds 2e-3 at block 160.` plus a two-line v2 note; code `good=(g[-1]<g[0]) and g[-1]<2e-3` -> `good=(g[-1]<=g[0]+1e-9) and g[-1]<2e-3`. Output saved to `outputs/s11_exit_quarter_turn_v2.txt` (stdout via tee).
- README script table: rows for `s15`, `s16`, `s11` replaced by rows for the v2 scripts; `s16` row no longer says `Every inequality of Section 3` and lists the checks exactly.

## Finding 5: Lean coverage and audit evidence

**weight_between_exit_line_v4.tex**, Status table, weight-between row

Old:

```
Weight between: split, order, two-sidedness, comparison, trace, local unitaries & \grade{T}\grade{L}\\
```

New:

```
Weight between: split, order, two-sidedness, comparison, trace, local unitaries & \grade{T}\grade{L} (Lean: algebraic subclaim)\\
```

**weight_between_exit_line_v4.tex**, Status table, radial census row

Old:

```
Radial census survives opening; positivity does not & \grade{T}\grade{L}\\
```

New:

```
Radial census survives opening; positivity does not & \grade{T}\grade{L} (Lean: algebraic subclaim)\\
```

**weight_between_exit_line_v4.tex**, Status table, Petermann row

Old:

```
Petermann line $\langle K\rangle=2\iff(w^2-v^2)^2=2u^2(w^2+v^2)$ & \grade{T}\grade{L}\\
```

New:

```
Petermann line $\langle K\rangle=2\iff(w^2-v^2)^2=2u^2(w^2+v^2)$ & \grade{T}\grade{L} (Lean: algebraic subclaim)\\
```

**exit_line_template_v4.html**, Status, weight-between row

Old:

```
<tr><td>Weight between: split, order, two-sidedness, comparison, trace, local unitaries</td><td><span class="g">T</span><span class="g">L</span></td></tr>
```

New:

```
<tr><td>Weight between: split, order, two-sidedness, comparison, trace, local unitaries</td><td><span class="g">T</span><span class="g">L</span> (Lean: algebraic subclaim)</td></tr>
```

**exit_line_template_v4.html**, Status, radial census row

Old:

```
<tr><td>Radial census survives opening; positivity does not</td><td><span class="g">T</span><span class="g">L</span></td></tr>
```

New:

```
<tr><td>Radial census survives opening; positivity does not</td><td><span class="g">T</span><span class="g">L</span> (Lean: algebraic subclaim)</td></tr>
```

**exit_line_template_v4.html**, Status, Petermann row

Old:

```
<tr><td>Petermann line $\langle K\rangle=2\iff(w^2-v^2)^2=2u^2(w^2+v^2)$</td><td><span class="g">T</span><span class="g">L</span></td></tr>
```

New:

```
<tr><td>Petermann line $\langle K\rangle=2\iff(w^2-v^2)^2=2u^2(w^2+v^2)$</td><td><span class="g">T</span><span class="g">L</span> (Lean: algebraic subclaim)</td></tr>
```

- New file `lean/formal_suite/AUDIT_ARTIFACTS_NOT_INCLUDED.md` in the zip (text as specified). README `lean/formal_suite/` layout row and the Lean paragraph each gain one sentence pointing to it. `formalization_status.md` unchanged.

## Finding 6: Domain and operator qualifications

**weight_between_exit_line_v4.tex**, Section 5.2, paragraph after Theorem 5.2 (with finding 9 citations)

Old:

```
That relation survives the non-Hermitian opening, so the commuting operator survives with it. Since $C_R$ is bounded and $T_R$ is banded, $C_R$ maps each eigenspace of $T_R$ into itself. A simple eigenvector of $T_R$ is therefore an eigenvector of $C_R$, and the levels of $C_R$ can be indexed by those of $T_R$.
```

New:

```
That relation survives the non-Hermitian opening, so the commuting operator survives with it. On the same PT-symmetric SSH model, Rottoli, Fossati and Calabrese find numerically a linearly weighted lattice entanglement Hamiltonian in a gapped setting~\cite{rottoli24}; their hopping and cut conventions differ from those used here and must be translated before sectors are compared. Biorthogonal entanglement spectra of non-Hermitian free fermions are developed in~\cite{chang20,herviou19}. This paper adds the exact entrywise commutation proof, valid without Hermiticity, the elliptic (Abel) phase tested against the edge levels, and its exact crossing on the Petermann line.

To pass from the entrywise identity to eigenvectors, take $T_R$ as its maximal operator on $\ell^2$, with domain $\{r\in\ell^2: T_Rr\in\ell^2\}$. For an eigenvector $r\in\ell^2$ of $T_R$, the kernel of $C_R$ decays exponentially and the entries of $T_R$ grow only linearly, so the sums defining $T_RC_Rr$ and $C_RT_Rr$ converge absolutely and agree. Hence $C_R$ maps each eigenspace of $T_R$ into itself, and a simple eigenvector of $T_R$ is an eigenvector of $C_R$. No completeness or diagonalizability of $T_R$ is claimed.
```

**weight_between_exit_line_v4.tex**, Section 5.3, new unnumbered lemma before Statement 5.3

Old:

```
\subsection{The ladder}
\begin{statement}[the edge ladder]
```

New:

```
\subsection{The ladder}
\begin{lemma*}[the domain of the phase]
For $0\le v<w$ and $0<u<w-v$, with $v'$ as in Lemma~\ref{lem:band}, the number $s=uw/(w^2-v'^2)$ satisfies $0<s<1$, and $s\to1$ at the critical boundary $u\to w-v$. \grade{T}
\end{lemma*}
\begin{proof}
At $v=0$, $E_0=E_\pi$, so $v'=0$ and $s=u/w<1$. For fixed $0<v<w$, write $v'(u)=(E_0-E_\pi)/2$. Then
\[
\frac{dv'}{du}=\frac u2\Big(\frac1{E_\pi}-\frac1{E_0}\Big)>0,
\]
since $E_\pi<E_0$. As $u$ increases to $w-v$, $E_\pi\to0$ and $E_0\to2\sqrt{vw}$, so $v'\to\sqrt{vw}$. Therefore $v'^2<vw$ in the open gapped region, and
\[
w^2-v'^2>w(w-v)>wu>0,\qquad 0<s=\frac{uw}{w^2-v'^2}<1.
\]
At the critical boundary $w^2-v'^2\to w(w-v)$ and $s\to1$.
\end{proof}
\begin{statement}[the edge ladder]
```

**weight_between_exit_line_v4.tex**, Statement 5.3, definition of s

Old:

```
s=\frac{uw}{w^2-v'^2}\in(0,1),\qquad
```

New:

```
s=\frac{uw}{w^2-v'^2}\in(0,1)\ \text{(by the domain lemma)},\qquad
```

**weight_between_exit_line_v4.tex**, Preamble, unnumbered lemma environment

Old:

```
\newtheorem{lemma}[theorem]{Lemma}
```

New:

```
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem*{lemma*}{Lemma}
```

**exit_line_template_v4.html**, Section 5.2, paragraph after Theorem 5.2 (with finding 9 citations)

Old:

```
That relation survives the non-Hermitian opening, so the commuting operator survives with it. Since $C_R$ is bounded and $T_R$ is banded, $C_R$ maps each eigenspace of $T_R$ into itself. A simple eigenvector of $T_R$ is therefore an eigenvector of $C_R$, and the levels of $C_R$ can be indexed by those of $T_R$.</p>
```

New:

```
That relation survives the non-Hermitian opening, so the commuting operator survives with it. On the same PT-symmetric SSH model, Rottoli, Fossati and Calabrese find numerically a linearly weighted lattice entanglement Hamiltonian in a gapped setting [5]; their hopping and cut conventions differ from those used here and must be translated before sectors are compared. Biorthogonal entanglement spectra of non-Hermitian free fermions are developed in [6,7]. This paper adds the exact entrywise commutation proof, valid without Hermiticity, the elliptic (Abel) phase tested against the edge levels, and its exact crossing on the Petermann line.</p>
<p>To pass from the entrywise identity to eigenvectors, take $T_R$ as its maximal operator on $\ell^2$, with domain $\{r\in\ell^2: T_Rr\in\ell^2\}$. For an eigenvector $r\in\ell^2$ of $T_R$, the kernel of $C_R$ decays exponentially and the entries of $T_R$ grow only linearly, so the sums defining $T_RC_Rr$ and $C_RT_Rr$ converge absolutely and agree. Hence $C_R$ maps each eigenspace of $T_R$ into itself, and a simple eigenvector of $T_R$ is an eigenvector of $C_R$. No completeness or diagonalizability of $T_R$ is claimed.</p>
```

**exit_line_template_v4.html**, Section 5.3, new lemma before Statement 5.3

Old:

```
<h3>5.3 The ladder</h3>
<div class="thm"><span class="tag">MEASURED STATEMENT 5.3
```

New:

```
<h3>5.3 The ladder</h3>
<div class="thm"><span class="tag">LEMMA · THE DOMAIN OF THE PHASE</span>
For $0\le v&lt;w$ and $0&lt;u&lt;w-v$, with $v'$ as in Lemma 5.1, the number $s=uw/(w^2-v'^2)$ satisfies $0&lt;s&lt;1$, and $s\to1$ at the critical boundary $u\to w-v$. <span class="g">T</span></div>
<div class="proof">
<p>At $v=0$, $E_0=E_\pi$, so $v'=0$ and $s=u/w&lt;1$. For fixed $0&lt;v&lt;w$, write $v'(u)=(E_0-E_\pi)/2$. Then</p>
<div class="math-d">$$\frac{dv'}{du}=\frac u2\Big(\frac1{E_\pi}-\frac1{E_0}\Big)&gt;0,$$</div>
<p>since $E_\pi&lt;E_0$. As $u$ increases to $w-v$, $E_\pi\to0$ and $E_0\to2\sqrt{vw}$, so $v'\to\sqrt{vw}$. Therefore $v'^2&lt;vw$ in the open gapped region, and</p>
<div class="math-d">$$w^2-v'^2&gt;w(w-v)&gt;wu&gt;0,\qquad 0&lt;s=\frac{uw}{w^2-v'^2}&lt;1.$$</div>
<p>At the critical boundary $w^2-v'^2\to w(w-v)$ and $s\to1$. <span class="qed">∎</span></p>
</div>
<div class="thm"><span class="tag">MEASURED STATEMENT 5.3
```

**exit_line_template_v4.html**, Statement 5.3, definition of s

Old:

```
$$s=\frac{uw}{w^2-v'^2}\in(0,1),\qquad
```

New:

```
$$s=\frac{uw}{w^2-v'^2}\in(0,1)\ \text{(by the domain lemma)},\qquad
```


## Finding 7: Interactive dimer and near-rim states

**exit_line_template_v4.html**, Hero instrument, label (d)

Old:

```
<div class="instrument" aria-label="Live ladder on the Cayley disk">
    <canvas
```

New:

```
<div class="instrument" aria-label="Proposed ladder model (Statement 5.3) on the Cayley disk">
    <div class="model-tag">PROPOSED LADDER MODEL (STATEMENT 5.3)</div>
    <canvas
```

**exit_line_template_v4.html**, CSS for model tag

Old:

```
.legend-line{font-size:13px;
```

New:

```
.model-tag{font-family:var(--display);letter-spacing:.2em;font-size:11px;color:var(--gold);text-align:center;margin-bottom:8px}
.legend-line{font-size:13px;
```

**exit_line_template_v4.html**, Hero legend line

Old:

```
<p class="legend-line">Points are the ladder $\Gamma_j=\tanh\big((j\Delta+i\theta)/2\big)$, $j=-3,\dots,3$, with $w=1$, computed live from the elliptic formulas of §5.
```

New:

```
<p class="legend-line">Proposed ladder model, not an independent spectrum calculation. Points are the ladder $\Gamma_j=\tanh\big((j\Delta+i\theta)/2\big)$, $j=-3,\dots,3$, with $w=1$, computed live from the elliptic formulas of §5; at the dimer $v=0$ only the centre level $j=0$ exists and only it is drawn. When the apex $i\tan(\theta/2)$ is large the drawing is rescaled to fit, and an arrow with its value marks it if it still cannot fit.
```

**exit_line_template_v4.html**, Hero instrument, drawDisk() body (a)(b)(c)

Old:

```
  clampV();const v=+vs.value,u=+us.value,m=model(v,u);
  document.getElementById('vo').textContent=v.toFixed(3);document.getElementById('uo').textContent=u.toFixed(3);
  const W=cv.width,H=cv.height,R=W*0.36,ox=W/2,oy=H*0.6;cx.clearRect(0,0,W,H);
  const P=(x,y)=>[ox+R*x,oy-R*y];
  /* grid: Smith-like constant-modulus rings */
  cx.lineWidth=1.2;for(const r of [0.25,0.5,0.75]){cx.strokeStyle='rgba(111,166,255,0.12)';cx.beginPath();cx.arc(ox,oy,R*r,0,2*Math.PI);cx.stroke();}
  cx.strokeStyle='rgba(227,173,85,0.12)';cx.beginPath();cx.moveTo(ox-R*1.25,oy);cx.lineTo(ox+R*1.25,oy);cx.moveTo(ox,oy+R*1.05);cx.lineTo(ox,oy-R*1.5);cx.stroke();
  /* rim */
  cx.save();cx.shadowColor=BLUE;cx.shadowBlur=26;cx.strokeStyle='rgba(169,203,255,0.85)';cx.lineWidth=2.4;cx.beginPath();cx.arc(ox,oy,R,0,2*Math.PI);cx.stroke();cx.restore();
  cx.fillStyle=MUT;cx.font='26px JetBrains Mono, monospace';cx.fillText('|Γ| = 1',ox+R*0.74,oy+R*0.86);
  cx.fillText('Re Γ',ox+R*1.02,oy-12);cx.fillText('Im Γ',ox+10,oy-R*1.42);
  if(!m){return;}
  const th=m.theta;
  /* arc tanh((x+i th)/2) */
  const pts=[];for(let i=0;i<=600;i++){const x=-14+28*i/600;const a=x/2,b=th/2;const den=Math.cosh(2*a)+Math.cos(2*b);pts.push([Math.sinh(2*a)/den,Math.sin(2*b)/den]);}
  const col=Math.abs(th-Math.PI/2)<0.004?'#ffffff':(th<Math.PI/2?BLUEHI:GOLDHI);
  cx.save();cx.shadowColor=th<Math.PI/2?BLUE:GOLD;cx.shadowBlur=30;cx.strokeStyle=col;cx.lineWidth=3;cx.beginPath();pts.forEach((p,i)=>{const q=P(p[0],p[1]);i?cx.lineTo(q[0],q[1]):cx.moveTo(q[0],q[1]);});cx.stroke();cx.restore();
  /* ladder points */
  const D=isFinite(m.Delta)?m.Delta:1e9;
  for(let j=-3;j<=3;j++){const a=j*D/2,b=th/2;const den=Math.cosh(2*a)+Math.cos(2*b);const g=[Math.sinh(2*a)/den,Math.sin(2*b)/den];const q=P(g[0],g[1]);
    cx.save();cx.shadowColor=GOLD;cx.shadowBlur=40;cx.fillStyle=j===0?'#fff7e0':GOLDHI;cx.beginPath();cx.arc(q[0],q[1],j===0?15:10,0,2*Math.PI);cx.fill();cx.restore();}
  /* apex label */
  const ap=P(0,Math.tan(th/2));cx.fillStyle=TXT;cx.font='italic 28px Spectral, Georgia, serif';cx.fillText('i tan(θ/2)',ap[0]+22,ap[1]-14);
  cx.fillStyle=MUT;cx.font='24px JetBrains Mono, monospace';cx.fillText('−1',ox-R-46,oy+34);cx.fillText('+1',ox+R+12,oy+34);
  /* readouts */
  const ex=m.E0*m.Ep-u*u;
  document.getElementById('r-th').textContent=(th/Math.PI).toFixed(4);
  document.getElementById('r-de').textContent=isFinite(m.Delta)&&m.Delta<1e6?m.Delta.toFixed(3):'∞ (dimer)';
  document.getElementById('r-ex').textContent=(ex>=0?'+':'')+ex.toFixed(4);
  document.getElementById('r-k').textContent=m.Kav.toFixed(4);
  const vd=document.getElementById('verdict');
  if(Math.abs(th-Math.PI/2)<0.004){vd.className='verdict on';vd.textContent='ON THE RIM · THE EXIT LINE';}
  else if(th<Math.PI/2){vd.className='verdict in';vd.textContent='EVERY LEVEL INSIDE THE DISK';}
  else{vd.className='verdict out';vd.textContent='EVERY LEVEL PAST THE RIM';}
}
```

New:

```
  clampV();const v=+vs.value,u=+us.value,m=model(v,u);
  document.getElementById('vo').textContent=v.toFixed(3);document.getElementById('uo').textContent=u.toFixed(3);
  const W=cv.width,H=cv.height,ox=W/2,oy=H*0.6;cx.clearRect(0,0,W,H);
  const fin=(...a)=>a.every(Number.isFinite);
  /* scale: fit the arc and its apex i tan(theta/2); keep a floor, and mark an apex that still cannot fit */
  let R=W*0.36,tA=0,offTop=false;
  if(m&&Number.isFinite(m.theta)){tA=Math.tan(m.theta/2);const half=tA>1?(tA*tA+1)/(2*tA):1;
    const Rfit=Math.min((oy-80)/Math.max(1.5,tA+0.12),(W/2-60)/Math.max(1.3,half+0.05));
    if(Number.isFinite(Rfit))R=Math.max(W*0.1,Math.min(R,Rfit));offTop=!(oy-R*tA>=30);}
  const P=(x,y)=>[ox+R*x,oy-R*y];
  /* grid: Smith-like constant-modulus rings */
  cx.lineWidth=1.2;for(const r of [0.25,0.5,0.75]){cx.strokeStyle='rgba(111,166,255,0.12)';cx.beginPath();cx.arc(ox,oy,R*r,0,2*Math.PI);cx.stroke();}
  cx.strokeStyle='rgba(227,173,85,0.12)';cx.beginPath();cx.moveTo(ox-R*1.25,oy);cx.lineTo(ox+R*1.25,oy);cx.moveTo(ox,oy+R*1.05);cx.lineTo(ox,oy-R*1.5);cx.stroke();
  /* rim */
  cx.save();cx.shadowColor=BLUE;cx.shadowBlur=26;cx.strokeStyle='rgba(169,203,255,0.85)';cx.lineWidth=2.4;cx.beginPath();cx.arc(ox,oy,R,0,2*Math.PI);cx.stroke();cx.restore();
  cx.fillStyle=MUT;cx.font='26px JetBrains Mono, monospace';cx.fillText('|Γ| = 1',ox+R*0.74,oy+R*0.86);
  cx.fillText('Re Γ',ox+R*1.02,oy-12);cx.fillText('Im Γ',ox+10,oy-R*1.42);
  if(!m){return;}
  const th=m.theta;
  /* arc tanh((x+i th)/2) */
  const pts=[];for(let i=0;i<=600;i++){const x=-14+28*i/600;const a=x/2,b=th/2;const den=Math.cosh(2*a)+Math.cos(2*b);const p=[Math.sinh(2*a)/den,Math.sin(2*b)/den];if(fin(p[0],p[1]))pts.push(p);}
  const col=Math.abs(th-Math.PI/2)<0.004?'#ffffff':(th<Math.PI/2?BLUEHI:GOLDHI);
  cx.save();cx.shadowColor=th<Math.PI/2?BLUE:GOLD;cx.shadowBlur=30;cx.strokeStyle=col;cx.lineWidth=3;cx.beginPath();pts.forEach((p,i)=>{const q=P(p[0],p[1]);i?cx.lineTo(q[0],q[1]):cx.moveTo(q[0],q[1]);});cx.stroke();cx.restore();
  /* ladder points: at the dimer (Delta infinite) only the centre level j=0 exists */
  const js=Number.isFinite(m.Delta)?[-3,-2,-1,0,1,2,3]:[0];
  for(const j of js){const a=j*(j?m.Delta:0)/2,b=th/2;const den=Math.cosh(2*a)+Math.cos(2*b);const g=[Math.sinh(2*a)/den,Math.sin(2*b)/den];if(!fin(g[0],g[1]))continue;const q=P(g[0],g[1]);
    if(j===0&&offTop)continue;
    cx.save();cx.shadowColor=GOLD;cx.shadowBlur=40;cx.fillStyle=j===0?'#fff7e0':GOLDHI;cx.beginPath();cx.arc(q[0],q[1],j===0?15:10,0,2*Math.PI);cx.fill();cx.restore();}
  /* apex label, or an off-canvas arrow carrying its value */
  if(!offTop){const ap=P(0,tA);cx.fillStyle=TXT;cx.font='italic 28px Spectral, Georgia, serif';cx.fillText('i tan(θ/2)',ap[0]+22,ap[1]-14);}
  else{cx.save();cx.fillStyle='#fff7e0';cx.strokeStyle='#fff7e0';cx.lineWidth=3;cx.beginPath();cx.moveTo(ox,70);cx.lineTo(ox,22);cx.stroke();cx.beginPath();cx.moveTo(ox,8);cx.lineTo(ox-12,30);cx.lineTo(ox+12,30);cx.closePath();cx.fill();
    cx.font='24px JetBrains Mono, monospace';cx.textAlign='left';cx.fillText('centre level above: i tan(θ/2) = '+tA.toFixed(2)+' i',ox+22,44);cx.restore();}
  cx.fillStyle=MUT;cx.font='24px JetBrains Mono, monospace';cx.fillText('−1',ox-R-46,oy+34);cx.fillText('+1',ox+R+12,oy+34);
  /* readouts */
  const ex=m.E0*m.Ep-u*u;
  document.getElementById('r-th').textContent=(th/Math.PI).toFixed(4);
  document.getElementById('r-de').textContent=Number.isFinite(m.Delta)&&m.Delta<1e6?m.Delta.toFixed(3):'∞ (dimer)';
  document.getElementById('r-ex').textContent=(ex>=0?'+':'')+ex.toFixed(4);
  document.getElementById('r-k').textContent=m.Kav.toFixed(4);
  const vd=document.getElementById('verdict');
  if(Math.abs(ex)<1e-12){vd.className='verdict on';vd.textContent='ON THE RIM · THE EXIT LINE';}
  else if(Math.abs(th-Math.PI/2)<0.004){vd.className='verdict on';vd.textContent='NEAR THE EXIT LINE';}
  else if(th<Math.PI/2){vd.className='verdict in';vd.textContent='EVERY LEVEL INSIDE THE DISK';}
  else{vd.className='verdict out';vd.textContent='EVERY LEVEL PAST THE RIM';}
}
```

- HTML template only (no LaTeX counterpart). Instrument tests: see the Playwright results below.
- Hero instrument `drawDisk()`: (a) when Δ is not finite only j=0 is drawn, and every arc/line point is checked finite before drawing; (b) verdict `ON THE RIM · THE EXIT LINE` only when |E0·Eπ − u²| < 1e-12, `NEAR THE EXIT LINE` when |θ − π/2| < 0.004, otherwise inside/past as before; (c) R = max(0.1W, min(0.36W, fit)) where the fit keeps the apex i·tan(θ/2) and the arc half-width (t²+1)/(2t) on the canvas; if the apex still cannot fit, an upward arrow with the value of tan(θ/2) is drawn in place of the centre level; (d) a `PROPOSED LADDER MODEL (STATEMENT 5.3)` tag above the canvas, aria-label and legend text, plus a `.model-tag` CSS rule.

## Finding 8: Smaller scope statements

**weight_between_exit_line_v4.tex**, Proposition 2.1

Old:

```
The window $\nu\in[\delta,1-\delta]$ is the disk $|\Gamma|\le1-2\delta$.
```

New:

```
For real $\nu$ the window $\nu\in[\delta,1-\delta]$ maps to the real diameter segment $[-1+2\delta,1-2\delta]$, equivalently $|\Gamma|\le1-2\delta$ for real $\nu$.
```

**weight_between_exit_line_v4.tex**, Section 3, list after Proposition 3.5, item 1

Old:

```
\item $C=pI$ has full raw census and zero boundary census.
```

New:

```
\item $C=pI$ has full raw census for $p\in[\varepsilon,1-\varepsilon]$, and zero boundary census for every $p$.
```

**weight_between_exit_line_v4.tex**, Section 3, sentence after the list

Old:

```
The census reads correlation faithfully inside the quasi-free class, and only there.
```

New:

```
A one-body record does not in general determine correlations outside the quasi-free class.
```

**weight_between_exit_line_v4.tex**, Proposition 3.9

Old:

```
both saturate $\dot\tau^2=4gS$ at all times, in opposite directions.
```

New:

```
both saturate $\dot\tau^2=4gS$ wherever $0<\nu(t)<1$, that is away from $\sin2\omega t=\pm1$, in opposite directions.
```

**weight_between_exit_line_v4.tex**, Figure 5.1 (fig:ladder) include

Old:

```
{../figures/fig09_exit_ladder.png}
```

New:

```
{../figures/fig09_exit_ladder_v2.png}
```

**weight_between_exit_line_v4.tex**, Section 5.5 item 1

Old:

```
A filter that discards them does not move the crossing until it begins to discard ill-conditioned levels it should keep.
```

New:

```
A filter that discards them does not move the crossing until the cutoff is lowered enough to retain numerically ill-conditioned near-endpoint levels.
```

**weight_between_exit_line_v4.tex**, Section 5.5 item 1, last sentence

Old:

```
where the filter keeps levels within $10^{-10}$ of the endpoints, whose eigenvalues are ill-conditioned \grade{V}
```

New:

```
where the cutoff is lowered enough to retain numerically ill-conditioned near-endpoint levels \grade{V}
```

**weight_between_exit_line_v4.tex**, Appendix B.3

Old:

```
\subsection*{B.3 \texttt{fig09\_exit\_ladder.py}}
\lstinputlisting[language=Python]{../scripts/fig09_exit_ladder.py}
```

New:

```
\subsection*{B.3 \texttt{fig09\_exit\_ladder\_v2.py}}
\lstinputlisting[language=Python]{../scripts/fig09_exit_ladder_v2.py}
```

**exit_line_template_v4.html**, Proposition 2.1

Old:

```
The window $\nu\in[\delta,1-\delta]$ is the disk $|\Gamma|\le1-2\delta$.
```

New:

```
For real $\nu$ the window $\nu\in[\delta,1-\delta]$ maps to the real diameter segment $[-1+2\delta,1-2\delta]$, equivalently $|\Gamma|\le1-2\delta$ for real $\nu$.
```

**exit_line_template_v4.html**, Section 3, list item 1

Old:

```
<li>$C=pI$ has full raw census and zero boundary census.</li>
```

New:

```
<li>$C=pI$ has full raw census for $p\in[\varepsilon,1-\varepsilon]$, and zero boundary census for every $p$.</li>
```

**exit_line_template_v4.html**, Section 3, sentence after the list

Old:

```
<p>The census reads correlation faithfully inside the quasi-free class, and only there.</p>
```

New:

```
<p>A one-body record does not in general determine correlations outside the quasi-free class.</p>
```

**exit_line_template_v4.html**, Proposition 3.9

Old:

```
both saturate $\dot\tau^2=4gS$ at all times, in opposite directions.
```

New:

```
both saturate $\dot\tau^2=4gS$ wherever $0&lt;\nu(t)&lt;1$, that is away from $\sin2\omega t=\pm1$, in opposite directions.
```

**exit_line_template_v4.html**, Section 5.5 item 1

Old:

```
A filter that discards them does not move the crossing until it begins to discard ill-conditioned levels it should keep.
```

New:

```
A filter that discards them does not move the crossing until the cutoff is lowered enough to retain numerically ill-conditioned near-endpoint levels.
```

**exit_line_template_v4.html**, Section 5.5 item 1, last sentence

Old:

```
where the filter keeps levels within $10^{-10}$ of the endpoints, whose eigenvalues are ill-conditioned <span class="g v">V</span>
```

New:

```
where the cutoff is lowered enough to retain numerically ill-conditioned near-endpoint levels <span class="g v">V</span>
```

**exit_line_template_v4.html**, Evidence panel fig09

Old:

```
<summary>fig09_exit_ladder.py · the paper
```

New:

```
<summary>fig09_exit_ladder_v2.py · the paper
```

- New script `scripts/fig09_exit_ladder_v2.py` (from `fig09_exit_ladder.py`): first line `# SCRIPT: fig09_exit_ladder_v2`; exec reads `s15_exit_ladder_v2.py`; adds `v_exit=float(mp.findroot(lambda x:(1-x*x)/mp.sqrt(2*(1+x*x))-u,0.47))`; trace `(0.4682,cols[1],'$v=0.468$: on the rim')` -> `(v_exit,cols[1],f'$v=v_{{\\rm exit}}={v_exit:.8f}$: on the rim\n(exact root of $E(0)E(\\pi)=u^2$)')`; saves `../figures/fig09_exit_ladder_v2.png/.pdf`. v_exit = 0.46821319.
- README: `figures/` row and `fig09` script row updated to the v2 figure and script.

## Finding 9: Non-Hermitian literature

**weight_between_exit_line_v4.tex**, Section 5.5, paragraph "The open step", after the Wiener--Hopf sentence

Old:

```
That derivation is open \grade{C}.
```

New:

```
The numerical entanglement Hamiltonian of~\cite{rottoli24} and the biorthogonal framework of~\cite{chang20,herviou19} are the natural points of comparison for that derivation. That derivation is open \grade{C}.
```

**weight_between_exit_line_v4.tex**, Bibliography

Old:

```
\bibitem{byrd}
```

New:

```
\bibitem{rottoli24} M.~Rottoli, M.~Fossati and P.~Calabrese, Entanglement Hamiltonian in the non-Hermitian SSH model, \emph{J. Stat. Mech.} (2024) 063102, arXiv:2402.04776.
\bibitem{chang20} P.-Y.~Chang, J.-S.~You, X.~Wen and S.~Ryu, Entanglement spectrum and entropy in topological non-Hermitian systems and nonunitary conformal field theory, \emph{Phys. Rev. Research} \textbf{2} (2020) 033069.
\bibitem{herviou19} L.~Herviou, N.~Regnault and J.~H.~Bardarson, Entanglement spectrum and symmetries in non-Hermitian fermionic non-interacting models, \emph{SciPost Phys.} \textbf{7} (2019) 069, arXiv:1908.09852.
\bibitem{byrd}
```

**exit_line_template_v4.html**, Theorem 5.4(b) proof, Byrd citation renumbered

Old:

```
$\operatorname{sn}(K/2\,|\,k)^2=1/(1+k')$ [5].
```

New:

```
$\operatorname{sn}(K/2\,|\,k)^2=1/(1+k')$ [8].
```

**exit_line_template_v4.html**, Open step, comparison sentence

Old:

```
That derivation is open <span class="g c">C</span>.
```

New:

```
The numerical entanglement Hamiltonian of [5] and the biorthogonal framework of [6,7] are the natural points of comparison for that derivation. That derivation is open <span class="g c">C</span>.
```

**exit_line_template_v4.html**, References list

Old:

```
<li>P. F. Byrd and M. D. Friedman,
```

New:

```
<li>M. Rottoli, M. Fossati and P. Calabrese, Entanglement Hamiltonian in the non-Hermitian SSH model, <em>J. Stat. Mech.</em> (2024) 063102, arXiv:2402.04776.</li>
<li>P.-Y. Chang, J.-S. You, X. Wen and S. Ryu, Entanglement spectrum and entropy in topological non-Hermitian systems and nonunitary conformal field theory, <em>Phys. Rev. Research</em> 2 (2020) 033069.</li>
<li>L. Herviou, N. Regnault and J. H. Bardarson, Entanglement spectrum and symmetries in non-Hermitian fermionic non-interacting models, <em>SciPost Phys.</em> 7 (2019) 069, arXiv:1908.09852.</li>
<li>P. F. Byrd and M. D. Friedman,
```

- Not applied: the "Bibliographic cleanup" sentence (swap author order of the 2009 review). Reason: arXiv author order is Peschel, Eisler (arXiv:0906.1663), which is what the paper has.
- HTML reference renumbering: [1]-[4] unchanged; new [5] Rottoli et al., [6] Chang et al., [7] Herviou et al.; Byrd and Friedman [5] -> [8] (citation in the proof of Theorem 5.4(b) updated). In the LaTeX the three new entries are placed before `byrd` in the bibliography.

## Numbers changed by reruns

Reruns of s15_exit_ladder_v2, s16_weight_between_checks_v2 and s11_exit_quarter_turn_v2 in the reference environment reproduce every number printed by the v3 scripts (s15: 8.37e-12, 1.67e-08, 4.21e-07, 200/200, 2.22e-16, 6.66e-16, 0.9131; s16: all lines identical, projector recovery 6.80e-16; s11: all gaps identical).
No number quoted in the paper changed because of a rerun.
New printed numbers (s15_exit_ladder_v2): 3 selected levels at each of 200 points, 600 in total; 0 removed by the residual filter; 400 spacing pairs used, 0 skipped by the Δ≥40 rule. These are quoted in the Statement 5.3 evidence.
s11_exit_quarter_turn_v2 per-point flags: the three u = 0.7 points change from FAIL to PASS under the 1e-9 slack rule; the six u = 0.3 and u = 0.5 points remain FAIL; VERDICT unchanged (KILLED at the stated bar); OPPOSITE unchanged.
Wording-only change to a quoted number: s05b "differences 4×10⁻⁸ and below" -> "differences of about 5×10⁻⁸ or less in these runs" (finding 3).

## Item 7 test results (Playwright, Chromium, local MathJax 3.2.2)

| v | u | verdict | non-finite canvas values | centre level (canvas px) | other levels drawn |
|---|---|---|---|---|---|
| 0 | 0.5 | EVERY LEVEL INSIDE THE DISK | 0 | (450, 366.8) | 0 |
| 0.468 | 0.5 | NEAR THE EXIT LINE | 0 | (450, 240.4) | 6 |
| 0.4682131924 | 0.5 | NEAR THE EXIT LINE | 0 | (450, 240) | 6 |
| 0 | 0.9 | EVERY LEVEL PAST THE RIM | 0 | (450, 105.3) | 0 |
| 0.098 | 0.9 | EVERY LEVEL PAST THE RIM | 0 | (450, 95) | 6 |

Page width at a 400 px viewport: scrollWidth 400, clientWidth 400. Same results at 1200 px. No page errors.
At v = 0.4682131924, |E0·Eπ − u²| = 2.4e-10, so the verdict is NEAR THE EXIT LINE by the rule; at the exact root v = 0.46821319246213563 the verdict is ON THE RIM · THE EXIT LINE (extra check).

## Other files

- `build_html_v4.py` (from `build_html_v3.py`): reads `exit_line_template_v4.html`; S15, S16, FIG09, S11 placeholders and their outputs point to the v2 scripts and outputs; writes `weight_between_exit_line_v4.html`. No `@@` remains in the built page.
- Zip folder: v3 tex removed, v4 tex added; v2 scripts, v2 outputs and the v2 figure added; v3 scripts, outputs and figure kept; `AUDIT_ARTIFACTS_NOT_INCLUDED.md` added; README updated as above.

## Final pass (applied after the agent's build, same findings)
- Finding 3: status table row (PDF and HTML) "Finite-block census exit on the line, to $4\times10^{-8}$; filter audit" → "Finite-block census exit on the line, about $5\times10^{-8}$ in these runs; filter audit".
- Finding 2: zip README "Status of the claims" now states the crossing as conditional (any ladder of the stated form), the exact crossing of the proposed phase, the domain lemma, and the ladder as measured on 600 selected low-index edge levels.
- Finding 1: Theorem 3.7 proof (PDF and HTML) "pure states with an occupation tending to 0" → "pure Slater states with an occupation tending to 0".
- Not changed (outside the review): the hero slider in the HTML clamps v when u is raised, and keeps the clamped value when u is lowered.
