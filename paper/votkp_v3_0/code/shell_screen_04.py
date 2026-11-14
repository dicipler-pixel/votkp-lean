# SCRIPT: SHELL-SCREEN-04
# Plan step 1: split every core-opening step as Gamma = Gamma_sh (+) Gamma_scr (velocity addition).
# WHY THE PLAN'S FIRST KILL CANNOT FIRE: velocity addition of Gammas is multiplication of ratios,
#   z = z_sh * z_scr, with z_sh = (n/(n-1))^2. So 'Gamma_scr >= s*(n)' IS 'z >= 3+2sqrt2', identically.
#   Part A shows that identity on the data (it is a check of arithmetic, not of nature).
# WHAT IS NOT CIRCULAR:
#   Part B. Write IE_val = Ry*(Zv/n)^2, IE_core = Ry*(Zc/(n-1))^2. Then z_scr = (Zc/Zv)^2, so
#           Gamma_scr = r (+) r with r = (Zc - Zv)/(Zc + Zv): the charge step taken twice.
#           Wall  <=>  Zc/Zv >= (1+sqrt2)(n-1)/n.   Table per core line.
#   Part D. Alkali column: is Zc/Zv the same for every alkali? If so the wall is met by the shell
#           part alone, and francium's second threshold follows from the ratio.
#           KILL LINE for D (before the run): fails this way if Zc/Zv for Na, K, Rb, Cs spreads
#           by more than 2%. Francium reading is then: IE2 = IE1*(7/6)^2*(Zc/Zv)^2 over that spread.
#   Part C. He core only: both charges from the 1/Z series, no fit.
#           IE_core = Z^2/2 - (5/8)Z + 0.157666   (Hartree; the 5/8 is the He-like first-order term)
#           IE_val  = Z^2/8 - (290/729)Z + 0.250500 (Li-like 2s; 290/729 = 2F0(1s,2s) - G0(1s,2s))
#           Second-order numbers are recalled literature values (not looked up this session).
#   KILL LINE for C (written before the run): fails this way if the series puts the wall crossing
#           anywhere but between Z = 6 and Z = 7, or misses any measured z for Z = 5..10 by over 2%.
#   OPPOSITE: drop the 5/8 (core unscreened, Zc = Z). If the crossing is still between 6 and 7,
#           the 5/8 is not what places the wall.
import gzip, json, math, sys
RY = 13.605693122994; HA = 2*RY; W = 3 + 2*math.sqrt(2)
d = {r['Z']: r for r in json.load(gzip.open(sys.argv[1]))['records']}
def ie(Z):
    return {t['q']: (t['IE_eV'], t.get('unc_eV') or 0.0, t.get('grade')) for t in d[Z]['thresholds'] if t.get('IE_eV')}
CORES = [(2, 2), (10, 3), (18, 4), (36, 5), (54, 6), (86, 7)]
print('PART A  identity z = z_sh*z_scr  (max relative error over all core-line steps)')
worst = 0.0; rows = []
for core, n in CORES:
    for Z in range(core + 1, min(core + 12, 119)):
        e = ie(Z); q = Z - core - 1
        if q in e and q + 1 in e:
            z = e[q+1][0] / e[q][0]; zsh = (n/(n-1))**2; zscr = z / zsh
            g = (z-1)/(z+1); gsh = (zsh-1)/(zsh+1); gscr = (zscr-1)/(zscr+1)
            worst = max(worst, abs((gsh+gscr)/(1+gsh*gscr) - g))
            Zv = n*math.sqrt(e[q][0]/RY); Zc = (n-1)*math.sqrt(e[q+1][0]/RY)
            rows.append((core, n, Z, d[Z]['symbol'], q, z, gscr, Zv, Zc, e[q+1][2], e[q+1][1], e[q][0]))
print('   max |Gsh (+) Gscr - G| = %.2e' % worst)
print()
print('PART B  effective charges; wall at Zc/Zv = (1+sqrt2)(n-1)/n')
for core, n in CORES:
    rho = (1+math.sqrt(2))*(n-1)/n
    print(' core %d  n=%d  wall ratio %.4f  s*=%.4f  charge step r*=%.4f' % (core, n, rho, (rho*rho-1)/(rho*rho+1), (rho-1)/(rho+1)))
    for r in rows:
        if r[0] == core:
            print('   %-2s q=%-2d z=%7.3f Gscr=%.4f  Zv=%6.3f Zc=%6.3f  Zc/Zv=%.4f %s  sig_v=%6.3f sig_c=%6.3f  [%s]' % (
                r[3], r[4], r[5], r[6], r[7], r[8], r[8]/r[7], 'PAST' if r[5] > W else 'in  ', r[2]-r[7], r[2]-r[8], r[9]))
print()
print('PART C  He core from the 1/Z series (no fit)')
def series(Z, s5=5/8):
    core = Z*Z/2 - s5*Z + (0.157666 if s5 else 0.0)
    val = Z*Z/8 - (290/729)*Z + 0.250500
    return core*HA, val*HA
bad = 0
for Z in range(3, 13):
    e = ie(Z); q = Z - 3
    zm = e[q+1][0]/e[q][0]; c, v = series(Z); zs = c/v; c0, v0 = series(Z, 0.0)
    err = zs/zm - 1
    if 5 <= Z <= 10 and abs(err) > 0.02: bad += 1
    print('   Z=%2d %-2s  z meas %.4f  series %.4f (%+.2f%%)  no-5/8 %.4f  %s' % (Z, d[Z]['symbol'], zm, zs, 100*err, c0/v0, 'PAST' if zm > W else 'in'))
def cross(s5):
    lo, hi = 3.5, 40.0
    f = lambda Z: series(Z, s5)[0]/series(Z, s5)[1] - W
    if f(lo)*f(hi) > 0: return None
    for _ in range(80):
        m = (lo+hi)/2
        if f(lo)*f(m) <= 0: hi = m
        else: lo = m
    return lo
zc = cross(5/8); z0 = cross(0.0)
print('   series crossing Z* = %.3f   (measured line crosses between 6 and 7, interpolated 6.57)' % zc)
print('   opposite, core unscreened: Z* = %s' % ('%.3f' % z0 if z0 else 'no crossing below Z = 40'))
print('   KILL: crossing in (6,7): %s ; misses over 2%% for Z=5..10: %d' % ('yes' if 6 < zc < 7 else 'NO', bad))
print()
print('PART D  alkali column')
alk = [r for r in rows if r[4] == 0 and r[0] >= 10]
rat = {r[3]: r[8]/r[7] for r in alk}
four = [rat[k] for k in ('Na', 'K', 'Rb', 'Cs')]
lo, hi = min(four), max(four)
for r in alk:
    rho = (1+math.sqrt(2))*(r[1]-1)/r[1]
    print('   %-2s n=%d  Zc/Zv=%.4f  wall ratio %.4f  margin %+.4f' % (r[3], r[1], r[8]/r[7], rho, r[8]/r[7]-rho))
print('   spread Na..Cs: %.4f to %.4f (%.2f%%)  KILL (over 2%%): %s' % (lo, hi, 100*(hi/lo-1), 'fired' if hi/lo-1 > 0.02 else 'not fired'))
print('   largest n with wall ratio below %.4f: n < %.2f ; below %.4f: n < %.2f' % (lo, 1/(1-lo/(1+math.sqrt(2))), hi, 1/(1-hi/(1+math.sqrt(2)))))
fr = [r for r in alk if r[3] == 'Fr'][0]; ie1 = fr[11]
print('   Fr: IE1 = %.5f eV ; wall needs IE2 > %.3f eV ; ratio reading IE2 = %.2f to %.2f eV ; archived %.1f +/- %.1f [%s]' % (
    ie1, ie1*W, ie1*(49/36)*lo*lo, ie1*(49/36)*hi*hi, ie1*fr[5], fr[10], fr[9]))
