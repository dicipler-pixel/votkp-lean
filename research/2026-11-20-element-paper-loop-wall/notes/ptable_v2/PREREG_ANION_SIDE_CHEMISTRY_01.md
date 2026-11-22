# PREREG: ANION-SIDE-CHEMISTRY-01
Written 2026-11-22, before any compound data is collected.

## Question
The anion rung puts every element with a bound anion on one side of the wall:
inside when electrophilicity exceeds hardness (omega/eta > 1), outside when hardness wins.
Inside (12): Ag, Ir, F, S, Se, Te, Pt, Au, At, Cl, Br, I.
Outside (53): the rest of the 65 adopted anion rungs.
This side is built from two numbers only: first ionisation energy and electron affinity.
Does it predict chemistry that is NOT built from those two numbers?

## Observable (independent of ionisation energy and electron affinity)
For each of the 65 elements: does a characterised binary solid with an alkali metal
(lithium, sodium, potassium, rubidium or caesium) exist in which the element sits as an
isolated single-atom anion, bonded to no atom of its own kind?
Scored YES / NO from crystal-structure literature, with one source per YES.
Cluster, chain and dimer anions (Si4, P7, C2, Sn9, ...) score NO for that compound.

## Why this check would prove what it claims
The side of the wall uses gas-phase single-atom energies. Whether a solid with an isolated
anion forms depends on lattice energy, size and competing cluster phases, none of which enter
the rung. If the inside set still forms isolated anions at a clearly higher rate than the
outside set, the wall is carrying chemical information beyond its two inputs.

## Kill condition (fixed now)
Let p_in = YES fraction among the 12 inside, p_out = YES fraction among the 53 outside.
- PASS if p_in - p_out >= 0.40 and a one-sided Fisher exact test gives p < 0.01.
- KILL if p_in - p_out < 0.20.
- In between: WEAK, reported as such.

## Known risk, stated before the run
Lithium- and sodium-rich Zintl phases put isolated anions of many outside elements
(oxide, hydride, nitride, phosphide, silicide, stannide ...) into crystals. That would push
p_out up and could kill this test. If it dies, the opposite direction is run next with the
same budget: does the outside side predict cluster/chain formation?
