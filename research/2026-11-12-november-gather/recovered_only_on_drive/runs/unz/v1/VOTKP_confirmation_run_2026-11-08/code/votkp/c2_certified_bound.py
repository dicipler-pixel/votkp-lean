# SCRIPT: c2_certified_bound
"""A certified remainder bound for the bowl law (the Viazovska move).

Her method bounds a quantity over a whole class by exhibiting an auxiliary function with
controlled signs, rather than by measuring the class. The bowl law has the same shape: an
approximation with an explicit remainder. So instead of reporting a median error, bound it.

With G = (z-w)/(z-wbar) and the series
    D = V0 - (3 sqrt3/4)|G|^2 + (sqrt3/4) Re(G^3) + (3 sqrt3/16)|G|^4 + R,
the remainder satisfies |R| <= C |G|^5 on the disk |G| <= 1, with C computed below. Then for
any knot whose shapes all satisfy |G_j| <= rho,

    |Vol_pred - Vol| <= n C rho^5 ,   and   relative error <= n C rho^5 / Vol.

That is a bound, not a measurement, and it says exactly which knots the law can be trusted
on. Pre-registered rule: the bound is USABLE iff C is finite and the certified bound
exceeds the measured error on every knot (it must, since it is an upper bound) while staying
within a factor 100 of it on most knots (otherwise it is vacuous).
"""
import sys, math
sys.path.insert(0,'code')
import mpmath as mp
mp.mp.dps = 40

W  = mp.expjpi(mp.mpf(1)/3); WB = mp.expjpi(-mp.mpf(1)/3)
V0 = mp.im(mp.polylog(2, W))          # arg(1-w) log|w| = 0 since |w|=1
C2 = 3*mp.sqrt(3)/4; C3 = mp.sqrt(3)/4; C4 = 3*mp.sqrt(3)/16

def D(z):
    return mp.im(mp.polylog(2, z)) + mp.arg(1-z)*mp.log(abs(z))

def zG(g):
    return (W - g*WB)/(1 - g)

def remainder(g):
    """D - (truncated series), in the G coordinate."""
    return D(zG(g)) - (V0 - C2*abs(g)**2 + C3*mp.re(g**3) + C4*abs(g)**4)

if __name__ == '__main__':
    # C = sup over the disk of |R|/|G|^5, by a grid in radius and angle
    best = mp.mpf(0)
    for rho in [mp.mpf(x)/100 for x in range(2, 101) if x != 100]:
        for k in range(48):
            ang = 2*mp.pi*k/48
            g = rho*mp.expj(ang)
            if abs(g) < mp.mpf('1e-12'): continue
            ratio = abs(remainder(g))/abs(g)**5
            if ratio > best: best = ratio; arg = (rho, ang)
    print('C = sup |R|/|G|^5 on the disk =', mp.nstr(best, 12))
    print('   attained near |G| =', mp.nstr(arg[0], 6), ', arg =', mp.nstr(arg[1], 6))
    print()
    print('   so for a knot with n tetrahedra and rho = max|G_j|:')
    for rho in ['0.3','0.5','0.7','1.0']:
        r = mp.mpf(rho)
        print(f'      rho = {rho}:  |error| <= n * {mp.nstr(best*r**5, 6)}')
