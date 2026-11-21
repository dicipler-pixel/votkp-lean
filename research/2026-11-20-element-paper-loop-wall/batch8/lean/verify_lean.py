"""Check a regenerated Lean ledger and run four intentionally false controls."""
import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
CONTROLS = (
    ("Rb first ordinary rung moved inside", "checkLadder energiesRb [1]", "checkLadder energiesRb []"),
    ("Sr Kr opening moved outside", "checkLadder energiesSr []", "checkLadder energiesSr [2]"),
    ("Ni k=20 evaluated with mistyped 1750 eV", "let z := (1758.0 / 1646.0", "let z := (1750.0 / 1646.0"),
    ("Rb/Sr mixed pair moved outside", "theorem mixed_rubidium_strontium", None),
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("--lean", default="lean")
    args = parser.parse_args()
    source = HERE / "OrdinaryGaZr.lean"
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        generated = tmp / "OrdinaryGaZr.lean"
        subprocess.run([sys.executable, HERE / "generate_lean.py", args.archive, generated], check=True)
        if generated.read_bytes() != source.read_bytes():
            raise ValueError("Generated Lean differs from the version under review")
        text = source.read_text()
        print(subprocess.check_output([args.lean, "--version"], text=True).strip())
        print("Regenerated source matches byte for byte.")
        out = subprocess.check_output([args.lean, source], text=True)
        declarations = re.findall(r"^theorem (\w+)", text, flags=re.MULTILINE)
        audit = re.findall(r"'VOTKP\.ElementBatches7And8\.(\w+)' depends on axioms: \[(.*?)\]", out)
        if [name for name, _ in audit] != declarations:
            raise ValueError("Axiom printouts do not cover every theorem in source order")
        for name, axioms in audit:
            if set(axioms.split(", ")) - ALLOWED:
                raise ValueError(f"Unexpected axiom for {name}: {axioms}")
        print(out.rstrip())
        print(f"{len(audit)} declarations checked; all 345 ordinary adjacent-energy pairs covered.")
        env = dict(os.environ, NO_COLOR="1")
        for label, old, new in CONTROLS:
            if new is None:
                old = next(line for line in text.splitlines() if line.startswith(old))
                new = old.replace("< 0", "> 0")
            if text.count(old) != 1 or new == old:
                raise ValueError(f"Could not uniquely inject control: {label}")
            changed = tmp / "Control.lean"
            changed.write_text(text.replace(old, new))
            result = subprocess.run([args.lean, changed], capture_output=True, text=True, env=env)
            diagnostic = result.stdout + result.stderr
            if result.returncode == 0 or diagnostic.count("error:") != 1 or "Tactic `decide`" not in diagnostic:
                raise ValueError(f"False control did not fail as expected: {label}\n{diagnostic}")
            print(f"Rejected false control: {label}")


if __name__ == "__main__":
    main()
