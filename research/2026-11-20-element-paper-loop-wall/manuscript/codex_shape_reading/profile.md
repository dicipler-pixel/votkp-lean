### Which part of the peel survives the triangle-family comparison?

For each of eight forward peels let $x_k=\ln z_k>0$. To compare two such ladders $x,y$, the triangle-family reading uses the range of $u_k=\ln(x_k/y_k)$. If the price of a mismatch is the largest absolute log error after one common change of scale, then

$$\min_{a>0}\max_k |\ln(x_k/(a y_k))|=\frac{\max_k u_k-\min_k u_k}{2}.$$

**Derivation.** Write $t=\ln a$. The larger of the two endpoint errors is at least half the distance between the extreme values, since their sum is at least that distance. Choosing $t=(\min u+\max u)/2$ attains that bound at both ends and bounds every intermediate coordinate. The optimum rescales the step logs by $a$, equivalently raising every original ratio of the second ladder to the same power. It does not rescale the ionization energies in eV. This is the positive-cone Hilbert projective distance up to the stated factor of two. The contribution here is its interpretation and test on this table.

**An exact control.** The eight-rung vector $(2,3,2,3,2,3,2,3)$ and its coordinatewise square have distance zero by the formula. All eight original steps lie below $3+2\sqrt2$. In the squared vector, four of them equal nine and lie above the wall. A common change of scale can therefore preserve the shape perfectly while changing which rungs cross. To recover the actual ladder from its projective profile, keep one positive scale, e.g. $T=\sum x_k=\ln(IE_9/IE_1)$ and the normalized profile $p_k=x_k/T$. Then $z_k=\exp(Tp_k)$. This domain is the forward ladder, where $x_k>0$.

**What happens in the elements.** On the published v2 input, fluorine through astatine give 77 eligible rows and 2,926 unordered pairs. With one nearest neighbour per element and the table's displayed column labels, Euclidean distance on $\ln z$ gives 52 correct. Euclidean distance on $\ln(\ln z)$ gives 59 before subtracting each row's mean and 59 afterwards. Cobalt gains a hit and cerium loses one. For the maximum norm, the corresponding scores are 56 with the scale held fixed and 60 with the best scale fitted per pair. Phosphorus, cobalt, iridium and gold gain a hit and no element loses one in that comparison. These are descriptive comparisons selected after the original shape scores were known. The labels include the table's display positions for the lanthanides. They are not experimental outcomes or a universal ranking of chemical representations.

This gives the table two distinct readings of the same measured inputs. The normalized profile compares where the cost is concentrated along the ladder. Recovering the wall address also needs its scale. A good nearest-neighbour score for the profile cannot select the exact wall.

The independent replay in this folder asserts the minimax formula on every pair to floating-point tolerance, tests the synthetic wall classifications in exact rational arithmetic, and prints the input digest and changed element labels.
