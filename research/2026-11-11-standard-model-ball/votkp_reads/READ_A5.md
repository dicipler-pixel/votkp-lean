# READ_A5: VOTKP / Elemental Peeling, four Drive versions

Label: A5. Source texts: /home/claude/sm/votkp_reads/src/A5/ (decoded from Drive).

## 1. Coverage

| File | Drive id | Bytes (wc -c, .txt) | Read in full? | Notes |
|---|---|---|---|---|
| v1.0 | 1Fro0QPS7f0CqWqB36ENlx3yKmOb5kXsz | 175,456 | Yes, by chunks | Read in offset-checked chunks after tool output truncation; the gap at ~111,000–116,100 (§15.3) was re-read and is contiguous. |
| v1.1 | 1-qVXMtUUHOhlsdhe9NU3BWdSLHwvLt4x | 193,973 | Yes | Full read. Notes in src/A5/scratch_v11.txt. |
| v1.1.1 | 163Mxsrqltibi162BOtvDfvrlgcSNZzzt | 194,032 | By diff only | Sentence-level diff against v1.1 (difflib on sentence splits). Text otherwise identical. Three changed passages (below). |
| v1.2 | 1zzyVXaZWtGpdpP2fMeInORvVAbxRNo2Q | 199,978 | Chars 0–~77,000 read; rest by diff | Sentence-level diff against v1.1 (/tmp/diff11_12.txt, 18 non-equal opcodes). Every changed passage read in full. Unchanged text after ~77,000 was not read by eye; it matches v1.1 by diff. |

v1.1.1 differences from v1.1 (the only differences found): (a) title "Version 1.1" to "Version 1.1.1"; (b) §6.4 stack example adds "With gold at N=0.4+2.3i and titania at N=2.4" and changes 0.433 to 0.432; (c) closing "Version 1.1." to "Version 1.1.1.".

## 2. What each version defines and claims

**v1.0.** Peel ratio as a Smith-chart reflection, Γ_k = (z_k−1)/(z_k+1) = tanh(½ ln z_k), with z_k = IE_{k+1}/IE_k (Thm 8.1). Shell-wall split Γ^sh = (2n−1)/(n²+(n−1)²) with Pythagorean triples (Thm 8.2). Thin-film echo r(d) = (Γ+x)/(1+Γx) (Thm 6.2). Gold metamer, knot layers, nuclear onion, glueball test P-01, Test H-01 (relativistic echo weight, killed). §15 casts peeling as Einstein velocity addition. Quote from Thm 8.1: "Because every z_k>1, each Γ_k lies on the positive real radius, so the atomic reflection chart has no phase."

**v1.1.** Adds Thm 6.3 (thin-end shunt admittance Y = n_b + y), Cor 15.2 (hyperbolic distance d(0,w) = ln(IE_l/IE_k)), §15.2 composition ("Successive peel steps compose as successive boosts."), §15.7 loop states of SU(2)/SU(3) lattice gauge theory and a hydrogen SO(4,2) map. Run G-02 (glueball registered sector) appears here; v1.0 said it was not run. Quote from §15.2: "Each peel ratio is the frequency ratio of a radar echo from a mirror moving at Γ_k c."

**v1.1.1.** Only the three changes above.

**v1.2.** Replaces the Lean checkpoint (49 declarations, commit 6955e48, Lean 4.33.0) with 57 theorems (commit b25c968, Lean v4.34.1). Adds the permutation-entropy paragraph (checked by hand). Redefines data grades A–D and evidence levels 0–4. Quote from §16: "Only the phase makes order matter."

Section-level checks done in v1.0 and carried to later versions: §6.4 "The phase of the echo decides."; §5.9 "T_s(0)=T_s(√2)=1/2"; §15.3 Thm 15.4 (scale blindness): "every energy scales by λ and every ratio IE_{k+1}/IE_k is unchanged."

## 3. Element-specific results

| Element / system | Z | Quantity | Number | Section |
|---|---|---|---|---|
| Lithium | 3 | Γ from τ1 | 0.867 | §15.3 / Table scratch_v10 |
| Sodium | 11 | Γ from τ1 | 0.804 | same |
| Potassium | 19 | Γ from τ1 | 0.759 | same |
| Rubidium | 37 | Γ from τ1 | 0.735 | same |
| Caesium | 55 | Γ from τ1 | 0.712 | same |
| Francium | 87 | Γ from τ1 | 0.692 | same |
| Hydrogen (H⁻) | 1 | τ = ln(IE/EA), measured | 2.89206(2), Γ 0.89491 | §15.3 mass-ratio table |
| Positronium (Ps⁻) | — | τ measured / theory | 3.0355(4) / 3.0361; Γ 0.9083 / 0.9084 | §15.3 |
| Helium | 2 | τ | 0.7945 | §15.3 Statistics |
| Lithium | 3 | τ1 = ln(75.64/5.39) | 2.641 | §15.3 Statistics |
| Nucleus, N=8 | — | ridge prominence | 0.188 | §15.4 |
| Nucleus, N=20 | — | ridge prominence | 0.110 | §15.4 |
| Nucleus, N=28 | — | ridge prominence | 0.141 | §15.4 |
| Nucleus, N=50 | — | ridge prominence | 0.209 | §15.4 |
| Nucleus, N=82 | — | ridge prominence | 0.244 | §15.4 |
| Nucleus, N=126 | — | ridge prominence | 0.221 | §15.4 |
| Non-magic N | — | 90th percentile prominence | 0.000 | §15.4 |
| Nucleus, N=40, 70 | — | ridge (oscillator closures) | −0.021, −0.002 | §15.4 |

Nuclear rows: "The six canonical magic numbers are the six strongest ridges." The Lithium Γ rows are from the scratch file; the paper's Table in §15 is the source. Mass-ratio table (§15.3): "Replacing an infinitely heavy positive particle by a positron moves τ by +0.145 (theory to theory)." Isotope residual H⁻ D⁻: 1.55(62) cm⁻¹.

## 4. Bold moves

1. **Associator for reduced products (§15.2).** For x⋆y = P(xy), the associator is P[x(I−P)(yz) − (I−P)(xy)z]. Checked on random matrices to 10⁻¹⁵. The paper says: "The associator is not small for a generic projection." Present in v1.0 (read in full); I did not verify by eye whether later versions keep it.
2. **Scale blindness (Thm 15.4).** Multiplying all masses by λ gives a unitary equivalence to λH, so IE ratios are invariant. Used to argue the peel coordinate is blind to which particle carries the charge.
3. **Statistics makes the ridges.** Lithium's τ1 = ln(75.64/5.39) = 2.641 exists because exclusion forbids 1s³. The paper calls this "The coordinate needs an absolute threshold."

## 5. Connections to today's frame

- Γ² = ½ wall: not defined in any version. The paper's alkali Γ values past 1/√2 agree numerically with the frame's listed alkali steps; the paper never names the wall.
- z ≈ 5.83, 3+2√2, √2, 1/√2: √2 appears only in T_s(√2) = 1/2 (§5.9). 1/√2 is not defined. 5.83 and 3+2√2 do not appear.
- Phase at a wall: conflict. Thm 8.1 says the atomic chart has no phase. The frame needs phase at a wall. The films use phase ("The phase of the echo decides."). The paper's own statement (§15.2 Thomas rotation) puts phase between additions, which is the nearest match.
- Cancel / lock / convert: not used in any version.
- Two books, tree/ball, neutrinos, Koide, spin: none appear in any version.
- Lorentz / rapidity: strong match. "Successive peel steps compose as successive boosts." (§15.2 v1.1+). "An atom's peel is a walk along one diameter, which is a geodesic." (Cor 15.2).
- Counts: frame count 5,737 steps vs the paper's 3,655 (to Z=86) and 5,714 (to Z=110). Flag this discrepancy.

## 6. Contradictions with the frame

1. Phase: Thm 8.1 says the atomic reflection chart has no phase; the frame requires phase at the wall.
2. Step count: 5,737 (frame) vs 3,655 / 5,714 (paper). Not reconciled in any version.
3. Internal inconsistency (v1.1 and v1.2): §15.5 cites "two agreeing transcriptions" of Athenodorou–Teper Table 17, while Appendix E says "a transcription ... in an external review".
4. Test H-01 killed: the echo weight |1−Γ²| is a worse separator (0.778 in sample) than |Γ| (0.994). This is a result against the Γ² reading, not a confirmation.
5. Version changes: v1.1 changes G-02 from not run to run; v1.2 changes the Lean checkpoint and data grades.

## 7. Notes on method

Byte counts are from wc -c on the .txt files; the earlier character counts in the working notes differ slightly because of encoding. The v1.1.1 and v1.2 differences were found by sentence-level difflib, not by eye; this is stated in the coverage table.
