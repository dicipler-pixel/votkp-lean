"""Read the exact input of PT-SHAPES-01B. No fitting to the displayed columns."""
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import numpy as np

source = Path(__file__).resolve().parents[2] / "ptable/v2/ptable_v2_data.json"
elements = [
    row for row in json.loads(source.read_bytes())["elements"]
    if not row.get("heavy") and row.get("col") and len(row["ie"]) >= 9
]
symbols = [row["sym"] for row in elements]
energies = np.array([row["ie"][:9] for row in elements])
labels = np.array([row["col"] for row in elements])
logs = np.diff(np.log(energies), axis=1)
assert np.all(logs > 0)
profiles = np.log(logs)
pairs = profiles[:, None, :] - profiles[None, :, :]
lo, hi = pairs.min(axis=2), pairs.max(axis=2)
midpoint = (hi + lo) / 2
error = np.max(np.abs(pairs - midpoint[:, :, None]), axis=2)
np.testing.assert_allclose(2 * error, hi - lo, atol=1e-14)
assert len(elements) == 77
print("Input SHA256", hashlib.sha256(source.read_bytes()).hexdigest())
print(f"{len(elements)} elements, 8 successive ratios, {len(elements)*(len(elements)-1)//2} unordered pairs")
print("method | same-column nearest / 77 (table display labels)")
scores = {}
for name, dist in {
    "log-ratio Euclidean": np.linalg.norm(logs[:, None, :] - logs[None, :, :], axis=2),
    "log-log Euclidean": np.linalg.norm(pairs, axis=2),
    "centered log-log Euclidean": np.linalg.norm(pairs - pairs.mean(axis=2, keepdims=True), axis=2),
    "unscaled log-log maximum error": np.max(np.abs(pairs), axis=2),
    "best-scaled log-log maximum error": error,
}.items():
    distances = dist.copy()
    np.fill_diagonal(distances, np.inf)
    neighbours = distances.argmin(axis=1)
    assert np.all(np.sum(distances == distances.min(axis=1, keepdims=True), axis=1) == 1)
    scores[name] = (labels == labels[neighbours])
    print(name, int(scores[name].sum()))
for family, before, after in [
    ("Euclidean", "log-log Euclidean", "centered log-log Euclidean"),
    ("maximum", "unscaled log-log maximum error", "best-scaled log-log maximum error"),
]:
    a, b = scores[before], scores[after]
    print(f"{family}, after removing scale: gained", [s for s, hit in zip(symbols, ~a & b) if hit],
          "lost", [s for s, hit in zip(symbols, a & ~b) if hit])
# Exact synthetic twin. Power two preserves its projective shape.
def outside(z):
    return (z - 1) ** 2 * 2 > (z + 1) ** 2

ratios = list(map(Fraction, [2, 3, 2, 3, 2, 3, 2, 3]))
squared = [z*z for z in ratios]
assert sum(map(outside, ratios)) == 0 and sum(map(outside, squared)) == 4
print("Exact twin: same projective shape, outside rungs 0/8 and 4/8.")
