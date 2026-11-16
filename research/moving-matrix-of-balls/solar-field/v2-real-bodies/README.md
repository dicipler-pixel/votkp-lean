# Solar Field — v2: each ball its own body (15 Nov 2026)

Jeromie Beasley, AI-assisted. v1 drew one ball five times. In v2 each ball is its own body: measured radius (logarithmic size scale),
flattening, rotation axis, and its magnetic field where it has one. Planet balls show their rim, their own body and field, and the Sun's
light as they see it; the copy of the Sun's faces is no longer drawn in them.

Sources (fetched 15 Nov 2026): NASA NSSDC fact sheets (Sun, Mercury, Venus, Earth, Mars); Winslow et al., Mercury's magnetopause and bow
shock from MESSENGER Magnetometer observations (standoff 1.45 R_M at 14.3 nPa, flaring 0.5); Wikipedia "Magnetopause" (Earth typical 10 R_E).
Not fetched that night (standard values): Earth's obliquity 23.44° and sidereal day; the Sun's radius and the speed of light in v1.

Real math in v2: dipole field lines r = L cos²(latitude) about the measured dipole axis; outer edge of the field from pressure balance,
r₀/R = (2B²/(μ₀P))^(1/6), with the ram pressure MESSENGER measured at Mercury scaled by the inverse square of distance.
Computed vs measured: Mercury 1.28 R vs 1.45 R (MESSENGER); Earth 9.41 R vs 10 R (typical). Mercury over its orbit: 1.19 to 1.37 R
computed vs 1.35 to 1.55 R measured range. Venus and Mars: NASA lists no magnetic field; none drawn.

Not modelled: squeezing of field lines on the sunward side, the tail, Earth's dipole offset direction, the phase of each dipole axis about
its rotation axis, induced fields at Venus and Mars, Mars's crustal fields, the Sun's field beyond a dipole (no spiral, no cycle).
Build: `python3 build_solar_v2.py`.
