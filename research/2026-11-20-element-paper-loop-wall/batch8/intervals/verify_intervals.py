"""Build the interval certificate from pinned inputs; run Lean and a missing-data control."""
import argparse
import ast
import gzip
import hashlib
import json
import os
import subprocess
import tempfile
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARCHIVE_HASH = "75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c"


def generated(archive, ea_source):
    raw = archive.read_bytes()
    if hashlib.sha256(raw).hexdigest() != ARCHIVE_HASH:
        raise ValueError("Archive does not match pin c35b18b")
    rows = json.loads(gzip.decompress(raw), parse_float=Decimal)["records"]
    assignments = [a.value for a in ast.parse(ea_source.read_text()).body if isinstance(a, ast.Assign)
                   and any(isinstance(t, ast.Name) and t.id == "AFFINITIES" for t in a.targets)]
    if len(assignments) != 1:
        raise ValueError("Missing canonical AFFINITIES mapping")
    eas = ast.literal_eval(assignments[0])

    def input_value(energy, uncertainty):
        if energy is None:
            if uncertainty is not None:
                raise ValueError("Unbound row has an uncertainty")
            return ".unbound"
        u = "none" if uncertainty is None else f"(some {Decimal(uncertainty):f})"
        return f".energy {Decimal(energy):f} {u}"

    out = ["-- Generated from c35b18b archive bytes and batch8_ladder.py affinity data.",
           "import IntervalWall", "namespace VOTKP.Element8Intervals", ""]
    audit = ["inside_everywhere", "outside_everywhere", "box_inside_sound", "box_outside_sound"]
    prefix = {"Kr": [".noBoundAnion"], "Rb": [".outside", ".outside"],
              "Sr": [".outside"], "Y": [".outside"],
              "Zr": [".outside", ".missingUncertainty", ".missingUncertainty"]}
    for number in range(36, 41):
        r = rows[number-1]
        symbol = r["symbol"]
        if r["Z"] != number or [x["q"] for x in r["thresholds"]] != list(range(number)):
            raise ValueError(f"Missing or reordered energy at Z={number}")
        values = [input_value(*eas[symbol][:2])] + [
            input_value(q["IE_eV"], q["unc_eV"]) for q in r["thresholds"]
        ]
        groups = [", ".join(values[i:i+4]) for i in range(0, len(values), 4)]
        out.extend([f"def inputs{symbol} : List Input :=", "  [" + ",\n   ".join(groups) + "]", ""])
        head = prefix[symbol]
        name = f"intervals_{symbol}"
        out.extend([f"theorem {name} : statuses inputs{symbol} =",
                    f"    [{', '.join(head)}] ++ List.replicate {number-len(head)} .inside := by",
                    "  decide +kernel", ""])
        audit.append(name)
    out.extend(["/-- Replacing an absent error by zero changes an unknown box into a known box. -/",
                "theorem zirconium_missing_is_not_zero :",
                "    let z1 := inputsZr[1]!",
                "    let z2 := inputsZr[2]!",
                "    classify z1 z2 = .missingUncertainty ∧",
                "    classify z1 (.energy 13.13 (some 0)) = .inside ∧",
                "    classify z1 z2 ≠ classify z1 (.energy 13.13 (some 0)) := by",
                "  decide +kernel", "",
                "theorem krypton_unbound_is_not_missing :",
                "    classify .unbound (.energy 1 none) ≠ .missingUncertainty := by",
                "  decide +kernel", ""])
    audit += ["zirconium_missing_is_not_zero", "krypton_unbound_is_not_missing"]
    out.extend(f"#print axioms {name}" for name in audit)
    out.extend(["", "end VOTKP.Element8Intervals", ""])
    return "\n".join(out)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("archive", type=Path)
    p.add_argument("ea_source", type=Path, help="batch8/ladder/batch8_ladder.py")
    p.add_argument("--lean", default="lean")
    p.add_argument("--generate", action="store_true")
    args = p.parse_args()
    result = generated(args.archive, args.ea_source)
    target = HERE / "Batch8Intervals.lean"
    if args.generate:
        target.write_text(result)
    if target.read_text() != result:
        raise ValueError("Generated Lean differs from committed file")
    print(subprocess.check_output([args.lean, "--version"], text=True).strip(), flush=True)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        kernel = "IntervalWall.lean"
        (tmp / kernel).write_bytes((HERE / kernel).read_bytes())
        (tmp / target.name).write_bytes(target.read_bytes())
        env = dict(os.environ, LEAN_PATH=str(tmp))
        subprocess.run([args.lean, "-j1", "-o", "IntervalWall.olean", kernel], cwd=tmp, env=env, check=True)
        checked = subprocess.check_output([args.lean, "-j1", target.name], cwd=tmp, env=env, text=True)
        if checked.count("depends on axioms: [propext, Classical.choice, Quot.sound]") != 11:
            raise ValueError(checked)
        print(checked.rstrip())
        control = result.replace("[.outside, .missingUncertainty, .missingUncertainty]", "[.outside, .inside, .inside]")
        if control == result:
            raise ValueError("Could not inject false control")
        (tmp / "Control.lean").write_text(control)
        failed = subprocess.run([args.lean, "-j1", "Control.lean"], cwd=tmp, env=env, text=True, capture_output=True)
        if failed.returncode == 0 or "error: Tactic `decide`" not in failed.stdout or failed.stdout.count("error:") != 1:
            raise ValueError("Missing-uncertainty control failure did not match expectations")
        print("False control rejected: Zr k=1 and 2 both labeled inside despite unknown IE2 uncertainty.")
        print("187 stable boxes (182 inside, 5 outside); 2 missing Zr boxes; 1 unbound Kr placeholder.")


if __name__ == "__main__":
    main()
