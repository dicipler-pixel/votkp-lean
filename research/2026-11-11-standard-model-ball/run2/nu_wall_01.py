# SCRIPT: SM-NU-WALL-01
# Neutrino generation steps against the wall z = 3+2sqrt2 (= (1+sqrt2)^2, Gamma^2 = 1/2). Inputs NuFIT 6.0 (2024), IC24 with SK:
#   dm21 = 7.49 +- 0.19 e-5 eV^2;  NO: dm31 = +2.534 (+0.025 -0.023) e-3;  IO: dm32 = -2.510 (+0.024 -0.025) e-3.
# H3: with m1 = 0 (normal ordering), z = m3/m2 = sqrt(dm31/dm21) sits on the wall.  KILL: |z - wall| > 2 sigma.
# OPPOSITE: inverted ordering with m3 = 0 (step m2/m1), and normal ordering with m1 > 0.
import math
W = 3 + 2*math.sqrt(2); dm21, s21 = 7.49e-5, 0.19e-5; dm31, s31 = 2.534e-3, 0.024e-3
z = math.sqrt(dm31/dm21); sz = 0.5*z*math.sqrt((s21/dm21)**2 + (s31/dm31)**2)
print(f"NO, m1 = 0: m2 = {math.sqrt(dm21)*1e3:.3f} meV, m3 = {math.sqrt(dm31)*1e3:.2f} meV, z = m3/m2 = {z:.4f} +- {sz:.4f}; wall {W:.4f}; off by {(z-W)/sz:+.2f} sigma -> {'KILL FIRED' if abs(z-W) > 2*sz else 'survives'}")
print(f"   same in splittings: dm31/dm21 = {dm31/dm21:.2f} against (1+sqrt2)^4 = {W*W:.2f}")
for m1 in [0.0, 0.5e-3, 1e-3, 2e-3, 5e-3, 1e-2]:
    m2 = math.sqrt(m1*m1 + dm21); m3 = math.sqrt(m1*m1 + dm31); zz = m3/m2
    print(f"   NO, m1 = {m1*1e3:4.1f} meV: m3/m2 = {zz:.4f} ({(zz-W)/sz:+.2f} sigma from the wall), m2/m1 = {('inf' if m1==0 else f'{m2/m1:.2f}')}")
dm32 = 2.510e-3; m1 = math.sqrt(dm32 - dm21); m2 = math.sqrt(dm32)
print(f"IO, m3 = 0: m2/m1 = {m2/m1:.5f} (deep inside the wall; the two heavy states are almost one)")
