# SCRIPT: BUBBLE-LADDER-01
# Jeromie's 3-6-9 bubble idea: planet = base, 3 = local (star) bubble, 6 = galactic bubble, 9 = universe bubble.
# Read as a ladder: for some natural quantity Q, log(Q_level / Q_planet) should go 1 : 2 : 3 across local, galactic,
# universe (equal steps on a log scale).  Criterion fixed before the run: a measure "fits" if both ratios
# d_gal/d_loc and d_univ/d_loc land within 15% of 2 and 3.  Look-elsewhere: 6 measures x 2 boundary choices = 12
# tries, so one fit by chance is not evidence; a fit must hold for BOTH boundary choices of the same measure.
# Values are standard approximate figures (order of magnitude is what matters here).
import math
G = 6.674e-11; c = 2.998e8; AU = 1.496e11; pc = 3.086e16; Msun = 1.989e30
H0 = 67.7e3 / (1e6 * pc); rho_c = 3 * H0**2 / (8 * math.pi * G)
lv = {  # name: (body radius, mass, boundary A (influence / pressure balance), boundary B (gravitational reach))
 'planet (Earth)':        (6.371e6, 5.972e24, 10 * 6.371e6,         1.5e9),            # magnetopause ~10 R_E ; Hill sphere
 'local (Sun)':           (6.957e8, Msun,     121.6 * AU,           230000 * AU),      # heliopause (Voyager 1) ; tidal radius in the Galaxy
 'galactic (Milky Way)':  (15e3 * pc, 1.3e12 * Msun, 200e3 * pc,    1.0e6 * pc),       # virial radius ~200 kpc ; reach to Local Group scale
 'universe':              (c / H0, rho_c * 4/3 * math.pi * (c / H0)**3, c / H0, 4.4e26)}  # Hubble radius ; particle horizon
names = list(lv)
def measures(R, M, Rb):
    return {'boundary radius': Rb, 'boundary / body radius': Rb / R, 'mass': M,
            'mean density in boundary': M / (4/3 * math.pi * Rb**3), 'dynamical time at boundary': math.sqrt(Rb**3 / (G * M)),
            'surface gravity G M / R^2 at body': G * M / R**2}
for bidx, bname in ((2, 'A: influence / pressure-balance boundary'), (3, 'B: gravitational-reach boundary')):
    print('\n== boundary choice', bname)
    tab = {n: measures(lv[n][0], lv[n][1], lv[n][bidx]) for n in names}
    for m in tab[names[0]]:
        logs = [math.log10(tab[n][m]) for n in names]
        d = [logs[i] - logs[0] for i in (1, 2, 3)]
        r2, r3 = d[1] / d[0], d[2] / d[0]
        fit = abs(r2 - 2) <= 0.3 and abs(r3 - 3) <= 0.45
        print('  %-34s log10: %s   steps from planet %6.2f %6.2f %6.2f   ratios %5.2f %5.2f  %s'
              % (m, ' '.join('%7.2f' % x for x in logs), *d, r2, r3, '<-- FITS 1:2:3' if fit else ''))

# ---- the opposite direction (base = universe, counting down), and a fragility check with Jupiter as the planet ----
print('\n== OPPOSITE: base = universe, steps down to galactic, local, planet (want 1 : 2 : 3)')
for planet in (('Earth', 6.371e6, 5.972e24, 10 * 6.371e6, 1.5e9), ('Jupiter', 6.99e7, 1.898e27, 63 * 6.99e7, 5.3e10)):
    lv2 = dict(lv); lv2['planet (Earth)'] = planet[1:]
    for bidx, bname in ((2, 'A'), (3, 'B')):
        tab = {n: measures(lv2[n][0], lv2[n][1], lv2[n][bidx]) for n in names}
        for m in tab[names[0]]:
            logs = [math.log10(tab[n][m]) for n in names][::-1]
            d = [logs[i] - logs[0] for i in (1, 2, 3)]
            if d[0] == 0: continue
            r2, r3 = d[1] / d[0], d[2] / d[0]
            fit = abs(r2 - 2) <= 0.3 and abs(r3 - 3) <= 0.45
            if fit or m == 'mass': print('  planet=%-7s boundary %s  %-34s ratios %5.2f %5.2f  %s' % (planet[0], bname, m, r2, r3, '<-- FITS' if fit else ''))
