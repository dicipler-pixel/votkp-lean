# SCRIPT: ISO-CROSS-03
# Core-opening step along isoelectronic lines: ions with N_core+1 electrons -> N_core, across Z.
# step z(Z) = IE(remove core e) / IE(remove the lone outer e). Where does each line cross the wall 3+2sqrt2?
# Hydrogenic limit (Z -> inf): ratio -> (n_out/n_core)^2: K 4, L (3/2)^2=2.25, M (4/3)^2.. all < 5.83, so every line
# that starts past the wall must cross it once. KILL LINE (before running): if any line crosses the wall more
# than once (non-monotone), the "one crossing per core" reading fails this way.
# Also: data grades for the alkali first steps (Cs, Fr).
import json, gzip, sys
d = {r['Z']: r for r in json.load(gzip.open(sys.argv[1]))['records']}
W = 3 + 8**.5
def IE(Z, q):
    for t in d[Z]['thresholds']:
        if t['q'] == q and t.get('IE_eV'): return t
for core in [2, 10, 18, 36, 54, 86]:
    out, prev, ncross = [], None, 0
    for Z in range(core+1, 119):
        q = Z - core - 1                      # ion with core+1 electrons
        a, b = IE(Z, q), IE(Z, q+1)
        if not (a and b): continue
        z = b['IE_eV']/a['IE_eV']; side = z > W
        if prev is not None and side != prev: ncross += 1; out.append(f"| WALL |")
        out.append(f"{d[Z]['symbol']}{q}+ {z:.3f}"); prev = side
    print(f"core {core:2d} ({ncross} crossing{'s' if ncross!=1 else ''}): " + "  ".join(out[:14]) + ("  ..." if len(out) > 14 else ""))
print("\nalkali first steps and data grades:")
for Z in [3, 11, 19, 37, 55, 87]:
    a, b = IE(Z, 0), IE(Z, 1)
    print(f"  {d[Z]['symbol']:2s} IE1 {a['IE_eV']:.4f} ({a['grade']}, unc {a.get('unc_eV')})  IE2 {b['IE_eV']:.3f} ({b['grade']}, unc {b.get('unc_eV')})  z {b['IE_eV']/a['IE_eV']:.3f}  z-W {b['IE_eV']/a['IE_eV']-W:+.3f}")
