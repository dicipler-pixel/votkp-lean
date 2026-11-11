# SCRIPT: SM-BALL-CHECKS-01
# Exact and numeric checks for placing Standard Model particles in the ball tree.
# Why each check proves what it says is printed beside it.
from mpmath import mp, mpf, log, sqrt, cosh, sinh, tanh, acosh
mp.dps = 40
L5 = log(5)
print("1. One tree edge is a boost of rapidity ln 5.  gamma = cosh(ln5) =", cosh(L5), " (13/5 =", mpf(13)/5, ")  v/c = tanh(ln5) =", tanh(L5), " (12/13 =", mpf(12)/13, ")")
print("   ball radius of one step tanh(ln5/2) =", tanh(L5/2), " = Gamma(5) = (5-1)/(5+1) = 2/3")
# 2. Lepton masses (PDG 2024 central values, MeV): Koide's ratio and the angle to (1,1,1)
me, mmu, mtau = mpf('0.51099895000'), mpf('105.6583755'), mpf('1776.93')
Q = (me+mmu+mtau)/(sqrt(me)+sqrt(mmu)+sqrt(mtau))**2
c2 = 1/(3*Q)
print("2. Koide Q =", mp.nstr(Q,12), "  (2/3 = 0.666666666667)   cos^2 of the angle between (sqrt m) and (1,1,1) = 1/(3Q) =", mp.nstr(c2,12), " (the half line is 1/2)")
# error on Q from the tau mass uncertainty 0.09 MeV
dQ = abs(((me+mmu+mtau+mpf('0.09'))/(sqrt(me)+sqrt(mmu)+sqrt(mtau+mpf('0.09')))**2) - Q)
print("   change in Q from one sigma of the tau mass:", mp.nstr(dQ,3), "  distance of Q from 2/3:", mp.nstr(abs(Q-mpf(2)/3),3))
# 3. Generation steps as peel steps: z = heavier/lighter, Gamma = tanh(ln z /2); the wall is z = 3+2 sqrt2
wall = 3+2*sqrt(2)
masses = {'e':me,'mu':mmu,'tau':mtau,'u':mpf('2.16'),'c':mpf('1273'),'t':mpf('172570'),'d':mpf('4.70'),'s':mpf('93.5'),'b':mpf('4183')}
for a,b in [('e','mu'),('mu','tau'),('u','c'),('c','t'),('d','s'),('s','b')]:
    z = masses[b]/masses[a]; print(f"3. {a}->{b}: z = {mp.nstr(z,6):>9}  Gamma = {mp.nstr(tanh(log(z)/2),6)}  Garrett levels ln z/ln5 = {mp.nstr(log(z)/L5,4)}  beyond the wall z>5.828: {z>wall}")
# 4. Where a light particle sits in the ball: radius r = tanh(eta/2), eta = acosh(E/m)
for name, m, E in [('electron neutrino (m ~ 0.05 eV) at 1 MeV', mpf('0.05e-6'), mpf(1)), ('electron at 1 MeV total energy', me, mpf(1)), ('muon from a pion decay (E=109.8 MeV)', mmu, mpf('109.78'))]:
    eta = acosh(E/m); print(f"4. {name}: rapidity {mp.nstr(eta,6)} = {mp.nstr(eta/L5,4)} tree levels, ball radius 1 - {mp.nstr(1-tanh(eta/2),4)}")
# 5. Counting: Lipschitz quaternions of norm 5 (Jacobi four-square r4(5) = 8*(1+5))
from itertools import product
n5 = sum(1 for a,b,c,d in product(range(-3,4),repeat=4) if a*a+b*b+c*c+d*d==5)
print("5. Lipschitz quaternions of norm 5:", n5, " = 6 tree arms x 8 units;  Weyl fermion states per Standard Model with right-handed neutrinos: 3 x 16 =", 3*16, "; without them 3 x 15 =", 45)
# 6. The wall as Wigner's classification: a Lorentz/SL(2,C) element is elliptic (|tr|<2, pure turn), parabolic (tr = 2, the wall), hyperbolic/loxodromic (climb)
# perpendicular commutator of two equal boosts: tr = 2 - 4 sinh^4(r/2) (BallJoins J4); parabolic (tr=-2) when sinh^4(r/2)=1, i.e. r = 2 asinh(1) = ln(3+2sqrt2)
from mpmath import asinh
r = 2*asinh(1); print("6. commutator of two equal perpendicular boosts reaches the wall at rapidity", mp.nstr(r,15), " = ln(3+2sqrt2) =", mp.nstr(log(wall),15), "; boost speed there v/c =", mp.nstr(tanh(r),12), "(= 2sqrt2/3)", mp.nstr(2*sqrt(2)/3,12))
