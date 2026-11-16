# SCRIPT: TIME-WALL-01
# Hole 3 (time).  Dirac Time 9.4 and Colour 12 prove a rate cannot come from projector geometry (blind to sH + cI); VOTKP 13.7
# leaves "no Hamiltonian drives the meridian phase" open.  What CAN be read without a calibrated rate?
# Join under test: Colour eq. (7) (two decaying parts: ln ratio = gap * t) is a peel step tau = gap * t, and Colour eq. (8)
# (bend of log brightness = squared Fisher speed) then reads, for two parts,
#       (ln I)'' = (gap/2)^2 * (1 - G^2),   G = tanh(tau/2) the Smith point of the ratio.
# 1 - G^2 is the transmitted fraction of the step.  Consequence: starting from equal parts, the bend has fallen to exactly
# HALF its starting value when the ratio is 3 + 2 sqrt2, i.e. on the half line G^2 = 1/2, at t * gap = ln(3 + 2 sqrt2) = 1.7627.
# The ratio "bend now / largest bend" needs no knowledge of the gap, so the wall is detectable without a calibrated clock.
# Why this decides it: I(t) is differentiated at 50 digits and compared with the formula; the half-bend time is solved directly.
# KILL: formula off by more than 1e-20 relative on random two-part fades, or half-bend ratio differing from 3 + 2 sqrt2.
# Opposite: three parts - does "bend = half of maximum" still mark one fixed ratio?  (Expected to fail; counted.)
import mpmath as mp, random
mp.mp.dps=50; random.seed(5); worst=0
for _ in range(200):
    g1,g2=mp.mpf(random.uniform(.1,3)),mp.mpf(random.uniform(.1,3)); a,b=mp.mpf(random.uniform(.1,5)),mp.mpf(random.uniform(.1,5)); t=mp.mpf(random.uniform(0,3))
    I=lambda s:a*mp.e**(-g1*s)+b*mp.e**(-g2*s)
    bend=mp.diff(lambda s:mp.log(I(s)),t,2)
    z=(a*mp.e**(-g1*t))/(b*mp.e**(-g2*t)); G=(z-1)/(z+1)
    worst=max(worst,abs(bend-((g1-g2)/2)**2*(1-G**2))/bend)
print('two parts: (ln I)\'\' against (gap/2)^2 (1-G^2), worst relative error over 200 fades: %s'%mp.nstr(worst,3))
gap=mp.mpf('0.37'); I=lambda s:mp.e**(-s)+mp.e**(-(1+gap)*s)
b0=mp.diff(lambda s:mp.log(I(s)),0,2); th=mp.findroot(lambda s:mp.diff(lambda u:mp.log(I(u)),s,2)-b0/2,4)
print('equal start, gap %s: bend halves at t*gap = %s  (ln(3+2sqrt2) = %s);  ratio there = %s  (3+2sqrt2 = %s)'%(gap,mp.nstr(th*gap,20),mp.nstr(mp.log(3+2*mp.sqrt(2)),20),mp.nstr(mp.e**(gap*th),20),mp.nstr(3+2*mp.sqrt(2),20)))
# opposite: three parts
vals=[]
for _ in range(6):
    r=[mp.mpf(random.uniform(.2,2)) for _ in range(3)]; I3=lambda s:sum(mp.e**(-x*s) for x in r)
    f=lambda s:mp.diff(lambda u:mp.log(I3(u)),s,2); b0=f(0)
    try:
        th=mp.findroot(lambda s:f(s)-b0/2,2/ (max(r)-min(r))); sh=sorted([mp.e**(-x*th) for x in r]); vals.append(float(sh[-1]/sh[0]))
    except Exception: vals.append(float('nan'))
print('three parts, largest/smallest part when the bend has halved:',[round(v,3) for v in vals],' (no single ratio)')
