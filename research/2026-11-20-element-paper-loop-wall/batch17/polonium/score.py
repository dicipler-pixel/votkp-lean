"""Score the frozen Po call from the pinned IE and primary-source input decimals."""
import csv
import gzip
import hashlib
import json
from decimal import Decimal as D, getcontext
from fractions import Fraction
from pathlib import Path

getcontext().prec = 60
HERE = Path(__file__).resolve().parent
ARCHIVE = HERE.parents[3] / "data/element_thresholds_20261011.json.gz"
assert hashlib.sha256(ARCHIVE.read_bytes()).hexdigest() == "75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c"
entries = json.loads(gzip.decompress(ARCHIVE.read_bytes()), parse_float=D)["records"]
record = next(t for a in entries if a["symbol"] == "Po" for t in a["thresholds"] if t["q"] == 0)
I, dI = record["IE_eV"], record["unc_eV"]
e = D("1.602176634e-19")
cm = D("6.62607015e-34") * 299792458 * 100 / e
kcal_mol = D(4184) / (D("6.02214076e23") * e)
# The quoted laser uncertainties exclude the experimental systematic budget.
inputs = [
    ("OPO", "fit_only", "11905.675", ".846", "cm^-1", cm),
    ("Z-cavity", "fit_only", "11905.743", ".140", "cm^-1", cm),
    ("JyvIS", "fit_only", "11905.631", ".009", "cm^-1", cm),
    ("Finney-Peterson via Ning-Lu", "theory_reported", "1.483", ".026", "eV", D(1)),
    ("Hill", "theory_central_only", "34.38", None, "kcal/mol", kcal_mol),
]
walls = D(3) - 2 * D(2).sqrt(), D(3) + 2 * D(2).sqrt()


def side(ion, affinity):
    ion, affinity = Fraction(ion), Fraction(affinity)
    diff = 2 * (ion - affinity)**2 - (ion + affinity)**2
    return "inside" if diff < 0 else "outside" if diff > 0 else "on"


def f(value):
    return "" if value is None else f"{value:.12f}"


rows = []
for name, status, value, unc, unit, scale in inputs:
    a = D(value) * scale
    da = None if unc is None else D(unc) * scale
    z = I / a
    g = (I - a) / (I + a)
    if da is not None:
        alo, ahi = a - da, a + da
        ilo, ihi = I - dI, I + dI
        # All boxes have 0 < A < I, so the endpoint z bounds are ordered.
        assert D(0) < alo <= ahi < ilo
        low, high = ilo / ahi, ihi / alo
        assert side(ilo, ahi) == side(ihi, alo) == "inside"
        box_side = "inside"
    else:
        low = high = None
        box_side = "unavailable"
    rows.append(dict(source=name, status=status, EA_native=value, quoted_error=unc or "",
                     unit=unit, IE_eV=str(I), IE_error_eV=str(dI), EA_eV=f(a), z=f(z),
                     Gamma=f(g), eta_eV=f((I-a)/2), chi_eV=f((I+a)/2),
                     omega_over_eta=f(1/(2*g*g)), central_side=side(I,a),
                     z_min=f(low), z_max=f(high), quoted_box=box_side,
                     margin_cm_inv=f((a - I*walls[0])/cm),
                     margin_lower_quoted_cm_inv=f(None if da is None else (alo - ihi*walls[0])/cm),
                     alternatives_inside="|".join(s for s in ("5","5.8","5.82","5.83","5.85","5.9","6") if z < D(s))))
with (HERE / "scores.csv").open("w",newline="") as out:
    w = csv.DictWriter(out, fieldnames=rows[0],lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("IE grade, refs:",record["grade"],record["references"])
print("EA wall eV and inverse centimetres:",f(I*walls[0]),f(I*walls[0]/cm))
print("Each value between the first and last labeled newsletter x ticks would give inside:",
      side(I+dI,11800*cm)==side(I-dI,11950*cm)=="inside")
for row in rows:
    print(row["source"],row["EA_eV"],row["Gamma"],row["quoted_box"],row["margin_lower_quoted_cm_inv"])
