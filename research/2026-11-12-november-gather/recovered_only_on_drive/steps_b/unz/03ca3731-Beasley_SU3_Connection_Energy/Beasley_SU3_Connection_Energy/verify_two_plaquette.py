from fractions import Fraction
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "upstream"))
from two_plaquette_19 import retained, psd_check

gram, _, coupling = retained(Fraction(4))
rank = sum(pivot != 0 for pivot in psd_check(coupling))
speed_squared = sum(coupling[i][i] / gram[i][i] for i in range(len(gram)))
print(f"rank = {rank}, squared speed = {speed_squared}")
if (rank, speed_squared) != (14, 208):
    raise SystemExit("Result differs from the recorded run.")
