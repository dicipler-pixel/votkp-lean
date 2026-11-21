"""Compare free and neon-hosted Ba optical transition frequencies, Lippi et al. Table I.

The input uses the wavenumber columns of arXiv:2512.11140v1; the journal
publication is J. Chem. Phys. 164 (2026) 144303. Gamma here is a signed
comparison of a line with *itself* in two environments. This is not IE or EA.
"""
import csv
from fractions import Fraction as F
from pathlib import Path

DIR = Path(__file__).resolve().parent


def main():
    with (DIR/"barium_neon_lines.csv").open() as f:
        rows=list(csv.DictReader(f))
    out=[]
    for r in rows:
        m, v, reported = (int(r[k]) for k in ("matrix_cm-1","free_cm-1","source_shift_cm-1"))
        z, gamma = F(m,v), F(m-v,m+v)
        assert (z-1)/(z+1)==gamma and (1/z-1)/(1/z+1)==-gamma
        # This interval covers rounding of the printed whole-number
        # wavenumbers. It is explicitly *not* a line-centre error bar.
        zlo, zhi = F(2*m-1,2*v+1), F(2*m+1,2*v-1)
        out.append(dict(label=r["label"],grade=r["assignment"],center_difference_cm_1=m-v,
                        printed_shift_cm_1=reported,center_minus_printed_cm_1=m-v-reported,
                        host_over_free=f"{float(z):.9f}",Gamma_host_free=f"{float(gamma):.9f}",
                        display_z_lo=f"{float(zlo):.9f}",display_z_hi=f"{float(zhi):.9f}"))
    with (DIR/"barium_neon_clock_check.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=tuple(out[0]),lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    # Common lower level removes an additive shift of all energies.
    d={r["label"]:r for r in rows}
    assert d["C"]["lower"]==d["G"]["lower"]==d["H"]["lower"]
    assert d["E"]["upper"]==d["F"]["upper"]
    def splitting(left,right):
        return tuple(int(d[left][k])-int(d[right][k]) for k in ("matrix_cm-1","free_cm-1"))
    assert splitting("C","G")== (5369,5426)
    assert splitting("E","F")== (173,182)
    z=[r for r in out if r["label"] in ("C","H")]
    assert float(z[0]["display_z_hi"])<1<float(z[1]["display_z_lo"])
    differences=[r["label"] for r in out if r["center_minus_printed_cm_1"]!=0]
    assert differences==["E","F","G"]
    print("8 transitions; 5 identified; C and H have opposite signed shifts.")
    print("Shared ground: C-G is 5369 vs 5426 cm^-1 (Ne vs free), shift -57.")
    print("Shared upper: E-F is 173 vs 182 cm^-1, shift -9.")
    print("Printed whole-number subtractions differ from listed shifts by -1 cm^-1 on E,F,G.")


if __name__=="__main__":
    main()
