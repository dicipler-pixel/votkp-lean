# Two Trees in One Ball: are the boost groups free at z = 2, 4, 8?

Answer: YES for all three (and for every even integer z >= 2). Graded PROVED (elementary proof below; every step written).
Exact-computation cross-checks and the opposite-first relation search agree (no relation found).
Directory: two-trees/scripts/ (this folder).
Each script starts with `# SCRIPT: NAME` and states its kill condition in its header before the run.

| z | relation search (exact-hash meet-in-the-middle) | origin-fixing non-backtracking word | planar <B_i,B_j> | commutator [B_i,B_j] | freeness |
|---|---|---|---|---|---|
| 2 | none, all relations of length <= 22 | none, length <= 14 | none, length <= 28 (origin <= 17) | elliptic, T = 31/16, infinite order, angle not a rational multiple of pi | PROVED |
| 4 | none, length <= 20 | none, length <= 13 | none, length <= 28 | elliptic, T = 47/64, infinite order, angle irrational | PROVED |
| 8 | none, length <= 20 | none, length <= 13 | none, length <= 28 | loxodromic, T = -1889/256 (|T|>2), infinite order | PROVED |

## Step 1. Opposite first: search for a relation
relation_search.c (+ mkgens.py makes the generator files). Words are non-backtracking in the 6 letters B_u^{+-1}.
Method: all non-backtracking words of length n-1 and n are hashed (4x4 matrix times (2z)^{-len} mod 2^31-1, all 16 entries
combined into a 64-bit key; this normalisation makes words of different length comparable). Two distinct words with equal key are a
relation candidate (any relation of length <= 2n splits as w1 = w2 with lengths n, n or n, n-1). Origin search: all words of length <= dmax
are applied to e0 (mod p); a hit would be a non-backtracking word fixing the origin.
Kill condition (written in the C header before the run): any collision or origin hit = relation found; none = groups survive to the stated length.
Positive controls (the search CAN find relations): gens_ctrl.txt (contains B_i(4) = B_i(2)^2) and z = 1 both report collisions at length 2-3.
Results (files out_search_*.txt): z=2: records 70,312,500, 0 collision groups, 9.2e9 origin nodes, 0 hits (n=11, dmax=14);
z=4 and z=8: n=10 (14,062,500 records), 0 collisions, dmax=13, 0 hits; planar z=2,4,8: n=14 (8,503,056 records), 0 collisions, dmax=17, 0 hits.
No candidate arose, so no exact re-verification was needed. (Mod-p hits would have been verified exactly in Python.)

## Step 2. Commutator type (commutator_type.py, out_commutator_type.txt)
Exact 4x4 trace of [B_a^s, B_b^s'] for all 12 sign/axis pairs equals T^2 with T = 2 - 4 sinh^4(ln z/2) = 2 - (z-1)^4/(4z^2)
(checked exactly; this is the SL2 trace of the commutator, 4x4 trace = T^2 in both the elliptic and hyperbolic case).
* z=2: T = 31/16, |T|<2, elliptic. cos(phi) = T^2/2 - 1 = 449/512, phi/pi = 0.15957...
* z=4: T = 47/64, elliptic. cos(phi) = -5983/8192, phi/pi = 0.76064...
* z=8: T = -1889/256, |T| > 2: loxodromic, no rotation at all.
Finite order test: an SL2(C) element of finite order has eigenvalues that are roots of unity, so its trace is an algebraic integer.
T = 31/16 and 47/64 are rational non-integers, so the elliptic commutators have INFINITE order; e^{i phi/2} is a root of x^2 - Tx + 1,
not a root of unity; 2cos(phi) = 449/256, -5983/4096 are not algebraic integers, so phi is not a rational multiple of pi.
So no commutator gives a finite-order elliptic relation. (Thomas rotation of B_iB_j: cos = 40/41, 272/353, 2080/4481: Pythagorean-type, not roots of unity.)

## Step 3. Freeness proof (written in full)
(a) Residues mod other primes (residue_primes.py): det(2zB_u) = 16 z^4, so for every odd prime p the scaled generators have rank 4 mod p
(no rank-one reduction exists); for p | z^2+1 they become monomial (finite image), for p | z^2-1 scalar-like. Only p = 2 degenerates
(rank 1 mod 2, which is why the Lean argument is silent). The odd-divisor method is dead for powers of 2.
(b) The 2-adic route works, in elementary form: ping-pong on P^1(Q(i)) for the (1+i)-adic valuation. The structure behind it is the
Bruhat-Tits tree of PGL2(Q_2(i)) (valence 3): the three boosts are hyperbolic with translation length v(z)=2k and pairwise disjoint axes
at distance 2 from the base vertex; the proof below avoids the tree and uses only valuations.

THEOREM. Let z be an even integer >= 2 (in particular z = 2, 4, 8). Then B_i, B_j, B_k generate a free group of rank 3
(and any two of them a free group of rank 2).

Step 0 (dictionary). Pauli matrices s_x, s_y, s_z. On Hermitian 2x2 matrices X = t + x.s (quadratic form det X = t^2-x^2-y^2-z^2) put
rho(M)X = M X M*/|det M| for M in GL2(C). rho is a homomorphism to the Lorentz group. Its kernel is the scalars:
if rho(M)=I, then X=E11, E22 give columns of M parallel to e1, e2, so M=diag(a,b) with |a|^2=|b|^2=|det M|; X=[[1,1],[1,1]] gives a conj(b) = |ab|>0, hence a=b.
Let M_u = a + b s_u with a=z+1, b=z-1 (det = a^2-b^2 = 4z). Split x = x_par u + x_perp. s_u commutes with t + x_par s_u and anticommutes with x_perp.s, so
M X M* = (a+b s_u)^2 (t + x_par s_u) + (a+b s_u)(a-b s_u) x_perp.s, with (a+b s_u)^2 = (a^2+b^2) + 2ab s_u = 2(z^2+1) + 2(z^2-1) s_u.
Dividing by 4z: t' = ((z^2+1)t + (z^2-1)x_par)/(2z), x_par' = ((z^2-1)t+(z^2+1)x_par)/(2z), x_perp' = x_perp. Thus rho(M_u) = B_u (rapidity +ln z; the
other sign is the inverse). (Also verified exactly for z=2,4,8,16, pingpong_check.py CHECK 1.)
Consequence: a reduced word w in B_u^{+-1} equals the identity iff the corresponding product M_w of M_u^{+-1} is a scalar iff M_w acts as the identity on P^1(Q(i)) (Moebius action). So it suffices to show that no nonempty reduced word acts trivially on P^1.

Step 1 (valuation). For x = a+bi in Q(i)^*, v(x) := v_2(a^2+b^2) (v_2 the 2-adic valuation, extended to Q), v(0)=infinity. This is the (1+i)-adic valuation (1+i is the only prime above 2 and has norm 2): v(xy)=v(x)+v(y), v(x+y) >= min(v(x),v(y)) with equality when v(x) != v(y). Values: v(1+i)=v(1-i)=1, v(2)=2, v(unit i)=0, v(odd integer)=0. For z even: v(z) >= 2, v(z-1)=0, v(2z) >= 4.

Step 2 (six sets in P^1(Q(i)) = Q(i) u {inf}).
U_x+ = {w : v(w+1) >= 3}, U_x- = {w : v(w-1) >= 3}, U_y+ = {w : v(w-i) >= 3}, U_y- = {w : v(w+i) >= 3},
U_z+ = {w : v(w) >= 1}, U_z- = {w : v(w) <= -1} u {inf}. (Each nonempty: contains its centre.)
Pairwise disjoint: the centres 1,-1,i,-i have pairwise differences of valuation <= 2 (v(2)=v(2i)=2, v(1-i)=v(1+i)=1), so two radius-3 balls cannot share a point; points of those balls have v(w)=0, so they miss U_z+ (v>=1) and U_z- (v<=-1); and U_z+ cap U_z- is empty.

Step 3 (inclusions). Moebius maps: f_x(w) = ((z+1)w+(z-1))/((z-1)w+(z+1)) (matrix M_x), f_y(w) = ((z+1)w - i(z-1))/(i(z-1)w+(z+1)) (M_y), f_z(w) = z w (M_z ~ diag(2z,2)).
Inverses: f_x^{-1}(w) = -f_x(-w), f_y^{-1}(w) = -f_y(-w), f_z^{-1}(w) = w/z (direct substitution, inverse matrix is M with b -> -b).
Claim: f_s(P^1 \ U_{s^{-1}}) is contained in U_s for each of the six letters s.
* x: f_x(w)+1 = 2z(w+1)/D with D = (z-1)(w-1)+2z. Let w not in U_x-, i.e. v(w-1) <= 2 (or w = inf). If w=inf, f_x(w)+1 = 2z/(z-1), valuation v(2z) >= 4. Else y=w-1 != 0 with v(y)<=2: v((z-1)y)=v(y) <= 2 < 4 <= v(2z), so v(D)=v(y); and w+1 = y+2 has v >= min(v(y),2) = v(y). So v(f_x(w)+1) >= 4 + v(y) - v(y) = 4 >= 3: f_x(w) in U_x+.
 For the inverse: P^1 \ U_x+ = -(P^1 \ U_x-), f_x^{-1}(w) = -f_x(-w) lands in -U_x+ = U_x-.
* y: f_y(w) - i = 2z(w-i)/D_y with D_y = i(z-1)(w+i)+2z. For w not in U_y-, v(Y)<=2 where Y=w+i, the same computation gives v(D_y)=v(Y), v(w-i)=v(Y-2i) >= v(Y), so v(f_y(w)-i) >= 4 (w=inf: f_y(inf)-i = 2z/(i(z-1))). Inverse via -f_y(-w) as for x, with -U_y+ = U_y-.
* z: w not in U_z- means v(w) >= 0, so v(zw) >= 2 >= 1: f_z(w) in U_z+. w not in U_z+ means v(w)<=0 or inf, so v(w/z) <= -2 <= -1 (inf stays inf): f_z^{-1}(w) in U_z-.
(All checked on 100,000 exact test points, plus z = 6,10,12,20,64 pass and the NEGATIVE controls z = 1,3,5,7 fail on 80% of the points, so the test is not blind: pingpong_check.py CHECK 2, pingpong_controls.py.)

Step 4 (ping-pong). Claim: for every nonempty reduced word w = s_1...s_n and every p not in U_{s_n^{-1}}, w(p) lies in U_{s_1}.
Induction on n. n=1 is Step 3. For n>1, s_n(p) is in U_{s_n}, and U_{s_n} is disjoint from U_{s_{n-1}^{-1}} because s_n != s_{n-1}^{-1} (reduced) and distinct letters have disjoint sets; apply the claim to s_1...s_{n-1}.
Now suppose w acts as the identity. Pick a letter t with t not in {s_1, s_n^{-1}} (four or more choices) and a point p in U_t. Then p is outside U_{s_1} and U_{s_n^{-1}} (disjointness), but w(p)=p must lie in U_{s_1}: contradiction. Hence no nonempty reduced word is the identity: by Step 0 B_i,B_j,B_k generate a free group of rank 3; omitting a letter pair gives rank 2. QED.

Where the hypotheses are used: v(z) >= 2 (so v(2z)>=4 > 2 and v(z)>=2 for the z-axis) and z-1 a unit, i.e. z even. For odd z the same computation fails (negative control), and the Lean odd-divisor argument takes over. Together: every integer z >= 2 is covered (Lean: z with an odd divisor m>1; here: every even z, which includes all powers of 2).

Cross-check by an independent algebraic quantity (pingpong_check.py CHECK 3-4): 3000 random reduced words up to length 60 satisfy the ping-pong conclusion; the displacement of the base lattice, d(w) = v(det M_w) - 2 min v(entries of M_w) with entries in Z[i], is > 0 for all 4686 reduced words of length <= 5 and for 900 random reduced words up to length 40 (min 2 / 4 / 6 for z=2/4/8, attained by single z-letters, equal to the translation length 2k).

## Open / not claimed
* Not proved: that no non-backtracking word fixes the origin of the ball (as the Lean theorem does for non-powers of 2). Freeness does not imply it (G is not discrete; a word could be a rotation about the origin). Search: none up to length 14 (z=2), 13 (z=4,8), 17 (planar). Status: open, search negative.
* The proof is written and machine-spot-checked in exact arithmetic, but not formalised in Lean (needs the (1+i)-adic valuation on Z[i]/Q(i); the six-set argument is finite and could be formalised with v(x) = v_2(norm)).

## Files
mkgens.py, relation_search.c (+ binary), out_search_*.txt, commutator_type.py/out_commutator_type.txt, residue_primes.py/out_residue_primes.txt, pingpong_check.py/out_pingpong_check.txt, pingpong_controls.py/out_pingpong_controls.txt.
