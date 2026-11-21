"""Generate the Ba–Nd ladder and orbital assignments from the pinned archive and ASD snapshot."""
import argparse
import csv
import gzip
import hashlib
import json
import sys
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
from pathlib import Path

DIR = Path(__file__).resolve().parent
PREVIOUS = DIR.parents[1] / "batch11"
sys.path.insert(0, str(PREVIOUS / "ladder"))
sys.path.insert(0, str(PREVIOUS / "independent"))
from batch11_ladder import HASH, HARTREE, CSV_HEADER, exact_q6, interval, side
from assign_openings import occupation

getcontext().prec = 60
SHELLS = {54: "Xe", 46: "4d10", 36: "Kr", 28: "3d10", 18: "Ar", 10: "Ne", 2: "He"}
COMPLETE = {"Xe": "[Cd]5p^{6}", "4d10": "[Kr]4d^{10}", "Kr": "[Ar]3d^{10}4s^{2}4p^{6}",
            "3d10": "[Ar]3d^{10}", "Ar": "[Ne]3s^{2}3p^{6}",
            "Ne": "[He]2s^{2}2p^{6}", "He": "1s^{2}"}
DETAILS = ["Z", "symbol", "k", "E_start_eV", "E_end_eV", "unc_start_eV", "unc_end_eV",
           "start_grade", "end_grade", "start_ref", "end_ref", "z", "Gamma", "log_z", "face_apex",
           "z_lo", "z_hi", "wall", "box_wall", "ASD_earlier_loss", "ASD_later_loss", "boundary"]
CHEM = ["Z","symbol","EA_eV","IE1_eV","eta_eV","chi_eV","omega_eV","omega_over_eta",
        "omega_over_eta_lo","omega_over_eta_hi","wall","z0","Gamma0","neutral_valence","anion_valence"]
SCREEN = ["Z","symbol","He_like_eV","H_like_eV","terminal_z","S_Z","sigma_Z",
          "S_minus_sigma","helium_like_minus_bare_eV"]
OPEN = ["Z","symbol","k","electrons","candidate_core","ASD_matches_candidate",
        "ASD_initial_shells","ASD_middle_shells","ASD_final_shells",
        "earlier_occupation_loss","later_occupation_loss","z","Gamma","wall"]


def rows(path):
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def save(path, header, data):
    with path.open("w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(header)
        writer.writerows(data)


def archive(path):
    binary = path.read_bytes()
    if hashlib.sha256(binary).hexdigest() != HASH:
        raise ValueError("Pinned archive hash mismatch")
    data = json.loads(gzip.decompress(binary), parse_float=D)["records"]
    elements = data[55:60]
    if [e["Z"] for e in elements] != list(range(56, 61)):
        raise ValueError("Missing element")
    for e in elements:
        if [t["q"] for t in e["thresholds"]] != list(range(e["Z"])):
            raise ValueError(f"Missing charge for {e['symbol']}")
    return elements


def net_loss(initial, final):
    """Orbital occupations in the initial state minus those in the final state."""
    diff = occupation(initial)
    diff.subtract(occupation(final) if final else {})
    if sum(diff.values()) != 1:
        raise ValueError(f"Wrong charge change between {initial}, {final}")
    changed = [(orb, n) for orb, n in sorted(diff.items()) if n]
    if len(changed) == 1:
        return changed[0][0]
    return "rearranged " + " ".join(f"{orb}:{n:+d}" for orb, n in changed)


def calc(archive_path, output):
    atoms = archive(archive_path)
    affinities = {r["symbol"]: r for r in rows(DIR / "affinities.csv")}
    states = {(int(r["Z"]), int(r["q"])): r for r in rows(DIR / "asd_states_20261121.csv")}
    ladder, detailed, anion, screening, cores = [], [], [], [], []
    for atom in atoms:
        Z, sym = atom["Z"], atom["symbol"]
        thresholds = atom["thresholds"]
        a = affinities[sym]
        aff, da = D(a["EA_eV"]), D(a["unc_eV"])
        energies = [(aff, da, "EA22", a["source"])] + [
            (D(t["IE_eV"]), t["unc_eV"], t["grade"], t["references"]) for t in thresholds]
        configurations = [states[Z, q]["ground_shells"] for q in range(Z)] + [""]
        for q, cfg in enumerate(configurations[:-1]):
            if sum(occupation(cfg).values()) != Z-q:
                raise ValueError(f"Wrong electron count for {sym}/{q}")
        for k, (x, dx, grade, ref) in enumerate(energies):
            if k == Z:
                ladder.append([Z, sym, k, x, "", "", grade])
                break
            y, dy, grade_y, ref_y = energies[k+1]
            z = y/x
            gamma = (y-x)/(y+x)
            gamma_f = (F(y)-F(x))/(F(y)+F(x))
            label = side(F(y)/F(x))
            display = [exact_q6(F(y)/F(x)), exact_q6(gamma_f)]
            ladder.append([Z, sym, k, x, *display, grade])
            first = net_loss(configurations[k-1], configurations[k]) if k else "detach extra electron"
            second = net_loss(configurations[k], configurations[k+1])
            core = SHELLS.get(Z-k)
            if core:
                matches = occupation(configurations[k]) == occupation(COMPLETE[core])
                cores.append([Z, sym, k, Z-k, core, matches, *configurations[k-1:k+2],
                              first, second, *display, label])
                boundary = core+" closed (ASD)" if matches else core+" electron count only (ASD)"
            else:
                boundary = {0:"bound anion", Z-1:"He-like to H-like removal"}.get(k,"")
            apex = (z.sqrt()-1)/(z.sqrt()+1)
            lo, hi, wall_box = interval(x, y, dx, dy)
            detailed.append([Z, sym, k, x,y,dx,dy,grade,grade_y,ref,ref_y,
                             *(f"{v:.10f}" for v in (z,gamma,z.ln(),apex)),lo,hi,
                             label,wall_box,first,second,boundary])
            if k == 0:
                chi, eta = (x+y)/2, (y-x)/2
                omega = chi**2/(2*eta)
                def chem_ratio(affinity, ie):
                    return (ie+affinity)**2/(2*(ie-affinity)**2)
                # All endpoint ionization energies exceed all endpoint affinities.
                low, high = chem_ratio(x-dx,y+dy), chem_ratio(x+dx,y-dy)
                if low > high or (omega < eta) != (label == "outside"):
                    raise ValueError(f"Anion consistency failure {sym}")
                anion.append([Z,sym,x,y,eta,chi,*(f"{v:.10f}" for v in
                             (omega,omega/eta,low,high)),label,*display,
                             a["neutral_valence"],a["anion_valence"]])
        b,h = (energies[i][0] for i in (-2,-1))
        S = (h-b)/(HARTREE*Z)
        sigma = Z-(2*b/HARTREE).sqrt()
        screening.append([Z,sym,b,h,*(f"{v:.10f}" for v in
                          (h/b,S,sigma,S-sigma,b-HARTREE*Z*Z/2))])
    output.mkdir(exist_ok=True, parents=True)
    for name, header, data in [
            ("batch12_ba_nd.csv", CSV_HEADER, ladder), ("rungs_detailed.csv", DETAILS, detailed),
            ("anion_chemistry.csv", CHEM, anion), ("screening.csv", SCREEN, screening),
            ("asg_openings.csv", OPEN, cores)]:
        save(output/name, header, data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive",type=Path)
    parser.add_argument("--out",type=Path,default=DIR)
    args = parser.parse_args()
    calc(args.archive, args.out)
