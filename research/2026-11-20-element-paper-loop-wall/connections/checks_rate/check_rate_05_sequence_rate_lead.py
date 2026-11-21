# SCRIPT: RATE-WEIGHT-SEQUENCE-RATE-05
# A LEAD put to a first test: does the opening map behave like the saturating trajectory of
# The Offset Speed Limit?  On trajectory (4) the wall angle theta = arcsin(Gamma) advances at the constant
# maximal rate 2 sqrt(E_B), and then the returned power Gamma^2 changes fastest exactly at the wall
# (check 02, item iv).  If an isoelectronic opening sequence (one noble core, Z rising) moved its angle
# uniformly in Z, the largest per-step change of Gamma^2 would sit on the step that crosses the wall.
# WHY THIS IS A TEST: it uses only archive ratios and the exact relation d(Gamma^2) = sin(2 theta) d theta.
# It cannot confirm a projector reading (no projector family is defined along Z); it can refute the
# "uniform angle rate" version of the lead.
# KILL CONDITION (before running): for a majority of the five wall-crossing sequences (helium, neon, argon,
# krypton, xenon cores) the largest |Delta Gamma^2| is NOT on the wall-crossing step -> the uniform-rate
# reading is refuted for the opening map.  (The speed limit itself is an upper bound and is not tested.)
import sys, gzip, json, math

d = json.load(gzip.open(sys.argv[1]))
rec = {r['Z']: r for r in d['records']}
W = 3 + 2 * math.sqrt(2)
cores = {'helium': 2, 'neon': 10, 'argon': 18, 'krypton': 36, 'xenon': 54}
fails = 0
for name, nc in cores.items():
    rows = []
    for Z in range(nc + 1, 86):
        th = {x['q']: x['IE_eV'] for x in rec[Z]['thresholds']}
        q = Z - nc - 1            # removal that leaves the core bare -> next removal opens it
        if q in th and q + 1 in th and th[q] and th[q + 1]:
            z = th[q + 1] / th[q]
            G = (z - 1) / (z + 1)
            rows.append((Z, rec[Z]['name'], z, G, math.degrees(math.asin(G))))
        if len(rows) >= 8:
            break
    steps = []
    for (Z1, n1, z1, G1, t1), (Z2, n2, z2, G2, t2) in zip(rows, rows[1:]):
        steps.append((abs(G2 * G2 - G1 * G1), t1 - t2, n1, n2, (z1 > W) != (z2 > W)))
    k = max(range(len(steps)), key=lambda i: steps[i][0])
    cross = [i for i, s in enumerate(steps) if s[4]]
    ok = cross and k == cross[0]
    fails += not ok
    print(f'{name}-core sequence:')
    for i, s in enumerate(steps):
        print(f'   {s[2]:10s} -> {s[3]:10s} |dGamma^2| = {s[0]:.5f}  dtheta = {s[1]:7.3f} deg'
              f'{"   <- crosses wall" if s[4] else ""}{"   <- largest" if i == k else ""}')
print(f'sequences where the largest change is NOT the wall step: {fails} of 5')
print('KILL', 'FIRED: uniform-angle reading refuted for the opening map' if fails >= 3 else 'not fired')
