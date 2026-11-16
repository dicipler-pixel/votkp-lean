# Solar Field — v1 (15 Nov 2026)

Jeromie Beasley, AI-assisted. The Sun and the planets out to Mars as five balls of one kind (the white Light at the Hypersurface ball).
Perfect world first (equal steps of ratio 3, circles, one plane, equal timing, equal still faces), then one dial per natural effect:
steps as measured, ellipses, tilted planes, own periods, uneven breathing faces. One light, traced from the Sun by the ball's own law,
drawn in every ball as that ball sees it. Data: NASA Planetary Fact Sheet.

Reading, not a theorem: a step is the logarithm of a ratio of distances from the Sun; the ball is the peel coordinate, not space.

Checks (t_sf1.js, check_solar_v1.out.json, check_solar_sigma.js):
- planet centres sit at their stated distance (exact); least distance from a point to a ray vs brute force 3e-8; Kepler: Mercury 0.794–1.206 a
- control: a bundle kept straight reproduces the open-ball solid-angle share at every planet (e.g. 4.94e-2 vs 4.93e-2; as measured 3.36e-5 vs 3.39e-5)
- flux balance at every face 4e-16; a sin²θ across every crossing ≤ 1e-13; the Sun's ledger sums to 1
- perfect world, share of the Sun's light through each ball, mean over one year (min–max), against the open-ball value:
  admittance falls outward:  Mercury 0.106 (0.035–0.144) vs 0.0493; Venus 6.7e-4 vs 4.2e-3; Earth 1.1e-5 vs 4.6e-4; Mars 3.6e-7 vs 5.1e-5
  admittance rises outward:  Mercury 0.0581 (0.045–0.068) vs 0.0493; Venus 4.59e-3 vs 4.24e-3; Earth 4.67e-4 vs 4.59e-4; Mars 6.2e-5 vs 5.1e-5
- as-measured steps, falls outward: 3e-7, 2e-7, 6e-8, 1e-9 against 4.8e-5, 1.4e-5, 7.2e-6, 3.1e-6

Not in v1: the Moon and Sun–Earth–Moon on the shape sphere; the Mixer v2 ball; the suns-paper interior; Kakeya direction capacity.
Build: `python3 build_solar_v1.py`.
