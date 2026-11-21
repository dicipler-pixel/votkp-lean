"""Regenerate, independently parse and kernel-check the batch 9 Lean certificates."""
import argparse
import gzip
import hashlib
import json
import os
import re
import subprocess
import tempfile
from decimal import Decimal
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SYMBOLS = ["Nb", "Mo", "Tc", "Ru", "Rh"]
ARCHIVE_SHA256 = "75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c"


def read_archive(path):
    if hashlib.sha256(path.read_bytes()).hexdigest() != ARCHIVE_SHA256:
        raise ValueError("Archive checksum differs from 182da01a14b10ce1e07e247565466d01822121c5")
    with gzip.open(path, "rt", encoding="utf-8") as f:
        return json.load(f, parse_float=Decimal)["records"]


def generate(path):
    records = read_archive(path)
    lines = ["-- Batch 9 from archive at 182da01: central energies in eV.",
             "import OrdinaryGaZr", "namespace VOTKP.ElementBatch9",
             "open VOTKP.ElementBatches7And8", ""]
    names = []
    for z, symbol in enumerate(SYMBOLS, 41):
        r = records[z-1]
        if r["symbol"] != symbol or [i["q"] for i in r["thresholds"]] != list(range(z)):
            raise ValueError(f"Missing, wrong or reordered data for Z={z}")
        decimals = [format(Decimal(row["IE_eV"]), "f") for row in r["thresholds"]]
        rows = [", ".join(decimals[i:i+6]) for i in range(0, len(decimals), 6)]
        lines += [f"def energies{symbol} : List Rat :=", "  [" + ",\n   ".join(rows) + "]", ""]
        name = f"ordinary_{symbol}"
        names.append(name)
        lines += [f"theorem {name} :", f"    energies{symbol}.length = {z} ∧ checkLadder energies{symbol} [] = true := by",
                  "  decide +kernel", ""]
    lines += ["/-- A neutral or positively ionized Nb–Rh atom has fewer than the 46 electrons",
              "required for a [Kr] 4d¹⁰ core. This bound uses the specified core occupancy. -/",
              "theorem below_kr_4d10_count (Z k : Nat) (h : Z ≤ 45) : Z - k < 36 + 10 := by",
              "  omega", ""]
    names.append("below_kr_4d10_count")
    lines += ["/-- Negative controls for assigning outside noble-core openings to Nb and Rh. -/",
              "theorem nb_false_outside_kr_core : checkLadder energiesNb [5] = false := by",
              "  decide +kernel", "",
              "theorem rh_false_outside_he_core : checkLadder energiesRh [43] = false := by",
              "  decide +kernel", ""]
    names += ["nb_false_outside_kr_core", "rh_false_outside_he_core"]
    lines += [f"#print axioms {name}" for name in names]
    return "\n".join(lines + ["", "end VOTKP.ElementBatch9", ""])


def reparse(source, path):
    fresh = read_archive(path)
    count = 0
    for z, symbol in enumerate(SYMBOLS, 41):
        pat = rf"def energies{symbol} : List Rat :=\s+\[(.*?)\]"
        matches = re.findall(pat, source, re.DOTALL)
        if len(matches) != 1:
            raise ValueError(f"Missing or repeated list for {symbol}")
        parsed = [Fraction(x.strip()) for x in matches[0].split(",")]
        expected = [Fraction(i["IE_eV"]) for i in fresh[z-1]["thresholds"]]
        if parsed != expected:
            raise ValueError(f"Reparsed Lean literals differ for {symbol}")
        count += len(parsed)
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("batch8_source", type=Path, help="batch8/lean/OrdinaryGaZr.lean")
    parser.add_argument("--lean", default="lean")
    parser.add_argument("--generate", action="store_true")
    args = parser.parse_args()
    source = HERE / "OrdinaryNbRh.lean"
    generated = generate(args.archive)
    if args.generate:
        source.write_text(generated)
    if source.read_text() != generated:
        raise ValueError("Regenerated Lean source differs")
    n = reparse(source.read_text(), args.archive)
    print(f"All {n} Lean energy literals independently reparsed and matched the archive.")
    print(subprocess.check_output([args.lean, "--version"], text=True).strip(), flush=True)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "OrdinaryGaZr.lean").write_bytes(args.batch8_source.read_bytes())
        (tmp / source.name).write_bytes(source.read_bytes())
        env = dict(os.environ, LEAN_PATH=str(tmp))
        lean = [args.lean, "-j1"]
        subprocess.run(lean + ["-o", "OrdinaryGaZr.olean", "OrdinaryGaZr.lean"],
                       cwd=tmp, env=env, stdout=subprocess.DEVNULL, check=True)
        audit = subprocess.check_output(lean + [source.name], cwd=tmp, env=env, text=True)
        axiom_sets = re.findall(r"depends on axioms: \[(.*?)\]", audit)
        allowed = {"propext", "Classical.choice", "Quot.sound"}
        if len(axiom_sets) != 8 or any(set(a.split(", ")) - allowed for a in axiom_sets):
            raise ValueError(audit)
        print(audit.rstrip())
        controls = [
            ("Nb Kr-core erroneously outside", "checkLadder energiesNb [] = true", "checkLadder energiesNb [5] = true"),
            ("Rh He-core erroneously outside", "checkLadder energiesRh [] = true", "checkLadder energiesRh [43] = true"),
        ]
        for label, old, new in controls:
            if generated.count(old) != 1:
                raise ValueError("Could not inject precise mutation")
            (tmp / "Control.lean").write_text(generated.replace(old, new))
            r = subprocess.run(lean + ["Control.lean"], cwd=tmp, env=env, text=True, capture_output=True)
            if r.returncode == 0 or "error: Tactic `decide`" not in r.stdout or r.stdout.count("error:") != 1:
                raise ValueError("Control did not fail at the intended step")
            print(f"Rejected false control: {label}.")
        print("210 ordinary pairs strictly inside; eight theorem audits.")


if __name__ == "__main__":
    main()
