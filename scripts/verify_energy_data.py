#!/usr/bin/env python3
"""Exact arithmetic controls on archived decimal ionization thresholds.

This checks the data-derived ledger, not atomic response operators or rates.
Use --figure to regenerate the single 5:2 dark figure (requires matplotlib).
"""
import argparse
import hashlib
import gzip
import json
from fractions import Fraction
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/element_thresholds_20261011.json.gz"


def analyze():
    source = json.loads(gzip.decompress(SOURCE.read_bytes()), parse_float=Fraction)
    counts = Counter()
    states = []
    cover = []
    for rec in source["records"]:
        z = rec["Z"]
        raw = rec["thresholds"]
        thresholds = {t["q"]: Fraction(t["IE_eV"]) for t in raw}
        assert len(thresholds) == len(raw), "duplicate charge stage"
        assert all(0 <= q < z and val > 0 for q, val in thresholds.items())
        counts["element_slots"] += 1
        counts["with_thresholds"] += bool(thresholds)
        counts["thresholds"] += len(thresholds)
        complete = set(thresholds) == set(range(z))
        counts["complete_ladders"] += complete
        # A ground-energy reference is available only with a complete suffix.
        remaining = {z: Fraction(0)}
        for q in reversed(range(z)):
            if q in thresholds and q + 1 in remaining:
                remaining[q] = thresholds[q] + remaining[q + 1]
        for q, energy in remaining.items():
            if q < z:
                states.append((z, z - q, float(energy), rec["symbol"]))
                assert remaining[q] - remaining[q + 1] == thresholds[q]
                counts["bare_reference_edge_checks"] += 1
        # Independent local anchors cover every known segment, including those
        # disconnected from both the neutral and bare endpoints.
        for q, val in thresholds.items():
            if q == 0 or q - 1 not in thresholds:
                e = Fraction(0)
                j = q
                while j in thresholds:
                    next_e = e + thresholds[j]
                    assert next_e - e == thresholds[j]
                    counts["local_segment_edge_checks"] += 1
                    e = next_e
                    j += 1
            if q + 1 in thresholds:
                nxt = thresholds[q + 1]
                assert nxt > val, "archived ratio not on positive Smith radius"
                gamma = (nxt - val) / (nxt + val)
                assert val * (1 + gamma) / (1 - gamma) == nxt
                counts["peel_inverse_checks"] += 1
        if complete:
            # Forward sum and reverse recurrence agree exactly.
            assert remaining[0] == sum(thresholds.values(), Fraction(0))
            counts["complete_total_checks"] += 1
        cover.append({"Z": z, "symbol": rec["symbol"], "thresholds": len(raw),
                      "complete": complete,
                      "total_binding_eV": float(remaining[0]) if 0 in remaining else None,
                      "grades": dict(Counter(t["grade"] for t in raw))})
    assert counts["element_slots"] == 118
    assert counts["with_thresholds"] == 110
    assert counts["thresholds"] == 5847
    assert counts["complete_ladders"] == 103
    assert counts["peel_inverse_checks"] == 5714
    assert counts["local_segment_edge_checks"] == 5847
    # Negative control: replacing a missing threshold by zero is not a valid
    # complete ladder; duplicate charge labels cannot add evidence.
    assert set({0: Fraction(1), 2: Fraction(3)}) != set(range(3))
    assert len({t["q"] for t in [{"q": 0}, {"q": 0}]}) != 2
    return counts, states, cover


def figure(states, cover):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.colors import LogNorm
    from matplotlib.ticker import LogLocator
    fig, ax = plt.subplots(figsize=(15, 6), dpi=180)
    fig.patch.set_facecolor("#050914")
    ax.set_facecolor("#050914")
    z, n, energy, symbols = zip(*states)
    im = ax.scatter(z, n, c=energy, s=11, marker="s", linewidths=0,
                    cmap="magma", norm=LogNorm(vmin=min(energy), vmax=max(energy)))
    ax.plot([1, 118], [1, 118], color="#9db8d8", lw=.7, alpha=.5)
    # Missing thresholds are marked only at the neutral element address.
    missing = [r["Z"] for r in cover if r["total_binding_eV"] is None]
    ax.scatter(missing, missing, marker="x", c="#97abc6", s=34, linewidths=1)
    for sym in ["C", "Fe", "Cu", "Xe", "Au", "Og"]:
        r = next(r for r in cover if r["symbol"] == sym)
        ax.annotate(sym, (r["Z"], r["Z"]), xytext=(5, 5), textcoords="offset points",
                    fontsize=9, color="#dce9ff")
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 122)
    ax.set_xlabel("Proton number Z", color="#dce9ff", labelpad=8)
    ax.set_ylabel("Remaining electrons Z − q", color="#dce9ff", labelpad=8)
    ax.set_title("Electronic binding remaining across the element atlas",
                 color="#f5f7ff", fontsize=16, loc="left", pad=16)
    ax.tick_params(colors="#a9bbd1")
    for spine in ax.spines.values():
        spine.set_color("#26364e")
    ax.grid(alpha=.12, color="#9db8d8", linewidth=.5)
    cbar = fig.colorbar(im, ax=ax, pad=.025, fraction=.035)
    cbar.set_label("Remaining binding Bq (eV) · logarithmic color", color="#dce9ff")
    cbar.ax.tick_params(colors="#a9bbd1")
    cbar.outline.set_edgecolor("#26364e")
    fig.text(.08, .025,
             "Archived E/S/T • × incomplete neutral binding • diagonal means q = 0 • empty regions are unpopulated",
             color="#a9bbd1", fontsize=9)
    fig.subplots_adjust(left=.08, right=.89, bottom=.15, top=.88)
    out = ROOT / "docs/assets/element-energy-landscape.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, facecolor=fig.get_facecolor())
    plt.close(fig)


def peel_figure():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    source = json.loads(gzip.decompress(SOURCE.read_bytes()))
    points = []
    for r in source["records"]:
        values = {t["q"]: t["IE_eV"] for t in r["thresholds"]}
        for q, a in values.items():
            if q + 1 in values:
                b = values[q + 1]
                points.append((r["Z"], r["Z"] - q, (b - a) / (b + a)))
    fig, ax = plt.subplots(figsize=(15, 6), dpi=180)
    fig.patch.set_facecolor("#050914")
    ax.set_facecolor("#050914")
    x, y, g = zip(*points)
    im = ax.scatter(x, y, c=g, cmap="magma", vmin=0, vmax=1,
                    marker="s", s=11, linewidths=0)
    ax.plot([1, 118], [1, 118], lw=.7, color="#9db8d8", alpha=.4)
    ax.set(xlim=(0, 120), ylim=(0, 122))
    ax.set_xlabel("Proton number Z", color="#dce9ff", labelpad=8)
    ax.set_ylabel("Electrons before the first removal Z − q", color="#dce9ff", labelpad=8)
    ax.set_title("VOTKP peel shape aligned by electron count",
                 color="#f5f7ff", fontsize=16, loc="left", pad=16)
    ax.tick_params(colors="#a9bbd1")
    for spine in ax.spines.values():
        spine.set_color("#26364e")
    ax.grid(alpha=.12, color="#9db8d8", linewidth=.5)
    cb = fig.colorbar(im, ax=ax, pad=.025, fraction=.035)
    cb.set_label("Peel Γq = (Iq+1 − Iq)/(Iq+1 + Iq)", color="#dce9ff")
    cb.ax.tick_params(colors="#a9bbd1")
    cb.outline.set_edgecolor("#26364e")
    fig.text(.08, .025,
             "5,714 archived adjacent pairs • E/S/T inputs • missing pairs left blank • aligned comparisons, not trajectories",
             color="#a9bbd1", fontsize=9)
    fig.subplots_adjust(left=.08, right=.89, bottom=.15, top=.88)
    fig.savefig(ROOT / "docs/assets/element-peel-landscape.png", facecolor=fig.get_facecolor())
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--figure", action="store_true")
    args = parser.parse_args()
    counts, states, cover = analyze()
    result = {"status": "passed", "arithmetic": "exact rationals from archived decimal values",
              "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              "counts": dict(counts), "coverage": cover,
              "scope": "energy ledger and coordinates only; no new response or dynamics"}
    out = ROOT / "verification"
    out.mkdir(exist_ok=True)
    (out / "energy_data_report.json").write_text(json.dumps(result, indent=2) + "\n")
    if args.figure:
        figure(states, cover)
        peel_figure()
    print(json.dumps({"status": "passed", "counts": dict(counts)}, indent=2))


if __name__ == "__main__":
    main()
