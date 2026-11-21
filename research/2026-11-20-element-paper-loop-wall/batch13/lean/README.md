# When the direction of a peel can change inside its input box

From promethium through terbium the central archive energies increase and all 310 ordinary reflection powers stay below one half. This batch adds a separate result about **direction**. For some theoretical levels the reported widths are large enough that an admissible choice of two energies puts the next one below the preceding one. A sign change in an input rectangle is a conditional sensitivity result. These archive estimates share references; no negative experimental peel or independent-error probability is inferred.

**Falsifier for a possible reversed step.** If the maximum of the earlier energy is at most the minimum of the later energy, no choice from the box gives a strict reversal. Equality gives contact only. The input to a multistep realization is one number per level, shared by both comparisons that use it.

| Element | Individually reversible ordinary steps | Contact only | Number of jointly realizable reversal sets | Largest simultaneous set size | First common-width contact |
|---|---|---|---:|---:|---|
| Promethium | none | none | 1 | 0 | k=10 at 19/17 |
| Samarium | 13, 14 | none | 3 | 1 | k=14 at 19/26 |
| Europium | 13, 14 | 15 | 3 | 1 | k=14 at 9/14 |
| Gadolinium | 13, 14 | 15, 16 | 3 | 1 | k=14 at 20/29 |
| Terbium | 13, 14, 17 | 15, 16 | 6 | 2 | k=14 at 21/29 |

For example, samarium removals 13–15 are 237 ± 12, 257 ± 12 and 276 ± 14 eV. Step 13 permits reversal because 249 exceeds 245. Step 14 permits reversal because 269 exceeds 262. If a new measurement kept the shared $E_{14}$ central value at 257 eV, reducing its half-width strictly below 5 eV would make both steps strictly forward with the adjoining quoted widths fixed. A half-width of exactly 5 eV still permits contact in step 14. Reversing both would give $E_{13}>E_{14}>E_{15}$, even though $E_{13}\le249<262\le E_{15}$. For terbium the exact sets are ${\varnothing,\{13\},\{14\},\{17\},\{13,17\},\{14,17\}}$. Lean proves that every admissible shared vector has one of the listed sets. Conversely, it checks an explicit shared vector for every listed set.

The last column asks what happens if a common nonnegative factor $t$ multiplies every quoted width within an element. The first contact between two adjacent intervals occurs at the least $(E_{k+1}-E_k)/(u_k+u_{k+1})$. Each recorded minimizer is unique. This factor is a deterministic sensitivity scale; it does not assign confidence levels.

**How different must the two underlying errors be?** Write the shifted thresholds as $A+up$ and $B+vq$, where each signed error in units of its own quoted width lies in $[-1,1]$. If neighboring errors differ by at most $d$, with $0\le d\le 2$, the exact largest adverse energy shift is

$$\max(up-vq)=|u-v|+\min(u,v)d.$$

For $u\le v$, the maximum occurs at $p=d-1$, $q=-1$; for $u>v$, it occurs at $p=1$, $q=1-d$. Checking this formula on all 310 ordinary pairs shows that the first possible equality is at **$d=9/7$, uniquely at europium k=14**. For smaller $d$ every step remains strictly forward. At $9/7$ equality is possible but strict reversal still fails. Europium’s levels are 263 ± 14 and 281 ± 14 eV: $p=9/14$ and $q=-9/14$ bring them both to 272 eV. For every $9/7<d\le2$, choosing $p=d/2$ and $q=-d/2$ makes this step strictly negative. Gadolinium k=14 is the next contact at $19/14$. The predictor here is a bound on the actual difference of two realized standardized errors. A statistical correlation coefficient for the archive estimates has not been supplied.

**Wall and affinity scope.** The kernel checks the entire reported rectangles for all 310 ordinary inputs, including its two-sided bound for $Γ^2$ on boxes with both directions. The point-affinity inputs for europium, gadolinium and terbium keep their anion rungs outside throughout, including gadolinium's preliminary measured value and uncertainty. Promethium's theory-only affinity and samarium's one-sided lower bound supply no adopted measured point rungs. For samarium the reported lower bound by itself admits positive affinities on either side of the wall. The certificate exhibits two hypothetical values above that lower bound as witnesses to the underdetermination. The previous ordinary cutoff window from nitrogen to caesium stays sharp for all 2,080 ordinary central steps through terbium.

The branch's main proofs already include the central wall calls and the newly classified anions. The present extension proves the uncertainty and shared-direction statements. It uses Lean 4.34.1 with core and Std. The Python verifier regenerates the exact decimal literals from the pinned threshold archive and the affinity table, independently reparses all 315 new energy/uncertainty pairs, and checks the 320 printed rows and every one of the 313 displayed ratio/reflection pairs.

```sh
paper=research/2026-11-20-element-paper-loop-wall
python3 "$paper/batch13/lean/verify.py" --lean /path/to/lean
```

[Archived threshold comparison and grades](../ladder/audit.txt) · [Joint-direction experiment](../ladder/joint_direction.csv) · [Affinity sources](../ladder/affinities.csv)
