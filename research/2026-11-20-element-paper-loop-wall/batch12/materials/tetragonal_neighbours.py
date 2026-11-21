"""Contact count in the elemental I4/mmm refinements with the 2a site at zero.

All membership tests use exact rational squared distances. The square roots in
the CSV are for display only. Output uses the smallest observed nonzero distance
as its reference, and includes the radius exactly when equal to the cutoff.
"""
import csv
import itertools
import math
from fractions import Fraction
from pathlib import Path

SOURCES = (
    ("La", 224, "2.6378", "0.0004", "3.8867", "0.0011", "10.1103/PhysRevB.110.024107"),
    ("Pr", 205, "2.383", "0.004", "4.209", "0.011", "10.1103/PhysRevB.105.174104"),
)
TOLERANCES = (0, 2, 5, 10, 15)


def enumerate_shells(a, c):
    shells = {}
    # A body-centred lattice point has either three integer or three
    # half-integer fractional coordinates. Translations not visited have
    # at least one coordinate of magnitude >=2, beyond the largest cutoff.
    for h, k, l in itertools.product(range(-3, 4), repeat=3):
        if (h, k, l) == (0, 0, 0) or not (h % 2 == k % 2 == l % 2):
            continue
        d2 = ((h*h + k*k)*a*a + l*l*c*c) / 4
        shells[d2] = shells.get(d2, 0) + 1
    return shells


def main():
    rows = []
    for s, pressure, a0, da0, c0, dc0, doi in SOURCES:
        a, da, c, dc = map(Fraction, (a0, da0, c0, dc0))
        shells = enumerate_shells(a, c)
        extremes = [enumerate_shells(aa, cc) for aa in (a-da, a+da) for cc in (c-dc, c+dc)]
        first, second = sorted(shells)[:2]
        assert first == a*a and second == (2*a*a + c*c)/4
        assert (shells[first], shells[second]) == (4, 8)
        ratio2lo = (2+((c-dc)/(a+da))**2)/4
        ratio2hi = (2+((c+dc)/(a-da))**2)/4
        for percent in TOLERANCES:
            cutoff2 = (1+Fraction(percent,100))**2
            def count(sh):
                return sum(n for d2,n in sh.items() if d2 <= min(sh)*cutoff2)
            n = count(shells)
            corner_counts = [count(sh) for sh in extremes]
            assert len(set(corner_counts+[n])) == 1
            # These c/a ranges put all other lattice shells outside 1.15a;
            # test that the extreme ratio interval is strictly on one side.
            assert ratio2hi < cutoff2 or ratio2lo > cutoff2
            assert n == (12 if ratio2hi < cutoff2 else 4)
            rows.append([s,pressure,a0,da0,c0,dc0,percent,format(math.sqrt(first),".6f"),
                         format(math.sqrt(second),".6f"),format(math.sqrt(second/first),".7f"),
                         format(math.sqrt(ratio2lo),".7f"),format(math.sqrt(ratio2hi),".7f"),
                         n,f"1/{3*n}",f"https://doi.org/{doi}"])
    path=Path(__file__).with_name("tetragonal_neighbours.csv")
    with path.open("w",newline="") as out:
        w=csv.writer(out,lineterminator="\n")
        w.writerow(("symbol","P_GPa","a_A","a_su_A","c_A","c_su_A","distance_tolerance_pct",
                    "first_A","second_A","second_over_first","ratio_box_lo","ratio_box_hi",
                    "n_within_tolerance","budget_multiplier_1_over_3n","source"))
        w.writerows(rows)
    assert [r[12] for r in rows if r[6]==5] == [12,4]
    print(f"{len(rows)} element/tolerance combinations, all 1-s.u. box decisions stable")


if __name__ == "__main__":
    main()
