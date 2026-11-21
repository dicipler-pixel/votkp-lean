"""Tabulate the openings and two-face disk control, from the same pinned archive."""
import argparse
import csv
from decimal import Decimal as D
from fractions import Fraction
from pathlib import Path

from batch8_ladder import AFFINITIES, read_input

E_H = D("27.211386245981")  # eV, CODATA 2022
COLUMNS = ["element", "k", "start_eV", "end_eV", "start_unc_eV", "end_unc_eV", "start_grade",
           "end_grade", "start_ref", "end_ref", "z", "Gamma", "r", "apex", "z_low", "z_high",
           "wall_central", "wall_at_endpoints", "boundary"]


def wall(z):
    z = Fraction(z)
    discriminant = z*z - 6*z + 1
    if discriminant == 0:
        return "on"
    return "outside" if discriminant > 0 else "inside"


def detail_row(symbol, k, start, end, marker):
    x, u, grade, ref = start
    y, v, next_grade, next_ref = end
    ratio = y/x
    reflect = (y-x)/(y+x)
    root = ratio.sqrt()
    apex = (root-1)/(root+1)
    low = high = ""
    interval_call = "unavailable"
    if u is not None and v is not None:
        lo = Fraction(y-v) / Fraction(x+u)
        hi = Fraction(y+v) / Fraction(x-u)
        # Every uncertainty rectangle in this batch lies entirely on the forward branch.
        if lo < 1:
            raise ValueError("an uncertainty interval crosses the reversal point")
        interval_call = wall(lo) if wall(lo) == wall(hi) else "straddles"
        low, high = (format(D(r.numerator)/D(r.denominator), ".9f") for r in (lo, hi))
    return [symbol,k,x,y,u,v,grade,next_grade,ref,next_ref,
            *(format(n,".9f") for n in (ratio,reflect,ratio.ln(),apex)),
            low,high,wall(Fraction(y)/Fraction(x)),interval_call,marker]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("archive", type=Path)
    p.add_argument("detail_csv", type=Path)
    args = p.parse_args()
    faces = {}
    summaries = []
    with args.detail_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(COLUMNS)
        for record in read_input(args.archive):
            z, symbol = record["Z"], record["symbol"]
            slots = [(D(t["IE_eV"]), None if t["unc_eV"] is None else D(t["unc_eV"]),
                      t["grade"], t["references"]) for t in record["thresholds"]]
            ea, ea_unc, ea_source = AFFINITIES[symbol]
            slots.insert(0, (D(ea), D(ea_unc), ea_source, ea_source) if ea else None)
            # Core electron count m leaves the m-electron ion after ionization k=Z-m.
            # Krypton starts at its own core; it has no ordinary step opening that core.
            markers = {z-m: f"{name} opening" for m,name in [(36,"Kr core"), (28,"3d10"),
                                                               (18,"Ar core"),(10,"Ne core"),
                                                               (2,"He core")] if z>m}
            markers.update({0: "bound anion", z-1: "last two"})
            strongest = (D(0), None)
            for k, (start,end) in enumerate(zip(slots,slots[1:])):
                if start is None:
                    continue
                row = detail_row(symbol,k,start,end,markers.get(k,""))
                w.writerow(row)
                value = end[0]/start[0]
                if k>0 and value>strongest[0]:
                    strongest = (value,k)
                if markers.get(k) == "Kr core opening":
                    faces[symbol] = Fraction(end[0])/Fraction(start[0])
                if markers.get(k):
                    print(f"{symbol:3s} {k:2d} {row[-1]:18s} z={row[10]} G={row[11]} [{row[14]}, {row[15]}] {row[17]}")
            h, b = slots[-1][0]/E_H, slots[-2][0]/E_H
            screening = D(z)-(2*b).sqrt()
            gap = (h-b)/z
            summaries.append((symbol,strongest[1],strongest[0],gap,screening))
    print("\nLargest ordinary ratio, last-two S and sigma (CODATA 2022 Hartree)")
    for symbol,k,value,s,sigma in summaries:
        print(f"{symbol:3s} k={k:2d} z={value:.9f} S={s:.9f} sigma={sigma:.9f}")
    print("\nKr-core faces in Claude's perpendicular disk model, pin c35b18b:")
    for left,right in [("Rb","Rb"),("Rb","Sr"),("Sr","Sr")]:
        a,b = faces[left],faces[right]
        squared_product = ((a-1)*(b-1))**2/(16*a*b)
        state = "open" if squared_product>1 else "closes" if squared_product<1 else "tangent"
        print(f"{left}/{right} (sinh(h_a) sinh(h_b))^2={float(squared_product):.9f}, {state}")
    a = D(faces["Rb"].numerator)/D(faces["Rb"].denominator)
    critical = ((a.sqrt()+1)/(a.sqrt()-1))**2
    print(f"Rb held fixed: second-face critical z={critical:.9f}")


if __name__ == "__main__":
    main()
