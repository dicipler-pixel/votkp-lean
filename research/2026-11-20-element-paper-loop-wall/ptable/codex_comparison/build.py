"""Build the standalone comparison edition from the tracked v2.2 mixer and benchmark."""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent / "v2_2" / "Periodic_Table_of_Elemental_Peels_v2_2_Jeromie_Beasley.html"
RESULTS = HERE.parent / "fair_baseline" / "results.json"
OUTPUT = HERE / "Periodic_Table_of_Elemental_Peels_Codex_Comparison.html"


def replace_once(source, old, new):
    if source.count(old) != 1:
        raise ValueError(f"Expected exactly one insertion point at {old[:75]!r}")
    return source.replace(old, new, 1)


def build():
    source = BASE.read_text()
    result_bytes = RESULTS.read_bytes()
    results = json.loads(result_bytes)
    match = re.search(r"setTimeout\(\(\)=>\{const d=(\{[^\n]*?\});", source)
    if not match:
        raise ValueError("Missing embedded mixer data")
    mixer = {e["sym"]: e for e in json.loads(match.group(1))["elements"]}
    table = HERE.parent / "v2" / "ptable_v2_data.json"
    if hashlib.sha256(table.read_bytes()).hexdigest() != results["source_sha256"]["table"]:
        raise ValueError("Benchmark source hash differs from the v2 data file")
    source_table = {e["sym"]: e for e in json.loads(table.read_text())["elements"]}
    for e in results["primary"]["elements"]:
        sym = e["symbol"]
        if (mixer[sym]["ie"][:9] != source_table[sym]["ie"][:9]
                or mixer[sym]["col"] != e["long"] or mixer[sym]["Z"] != e["Z"]):
            raise ValueError(f"Mixer disagrees with benchmark input for {sym}")
    # Include the two interactive cohorts and their measured scores.
    display = {}
    for name in ("primary", "without_lanthanides"):
        block = results[name]
        elements = block["elements"]
        methods = block["methods"]
        symbols = [element["symbol"] for element in elements]
        if len(set(symbols)) != len(symbols):
            raise ValueError(f"Duplicate element in {name}")
        labels = {e["symbol"]: e for e in elements}
        for method, detail in methods.items():
            neighbours = detail["neighbors"]
            if len(neighbours) != len(elements):
                raise ValueError(f"Invalid neighbour list for {name}/{method}")
            for label in ("long", "short"):
                hits = sum(labels[left][label] == labels[right][label]
                           for left, right in zip(symbols, neighbours, strict=True))
                if hits != detail["hits"][label] or any(left == right for left, right in zip(symbols, neighbours)):
                    raise ValueError(f"Inconsistent score for {name}/{method}/{label}")
        display[name] = {"elements": elements, "methods": methods, "comparisons": block["comparisons"]}

    display["archiveDifferences"] = {}
    for symbol, k, plotted, reference in results["archive"]["differences"]:
        if mixer[symbol]["ie"][k - 1] != plotted:
            raise ValueError(f"Unexpected energy on {symbol} removal {k}")
        display["archiveDifferences"].setdefault(symbol, {})[str(k)] = reference

    title = "Periodic Table of Elemental Peels · Codex comparison edition"
    source = replace_once(source, "<title>Periodic Table of Elemental Peels v2.2", "<title>" + title)
    source = replace_once(source, "v2.2, 23 November 2026</div>", "v2.2 · Codex comparison edition, 23 November 2026</div>")
    source = replace_once(source, '<a href="#shapes">Shapes</a>',
                          '<a href="#shapes">Shapes</a><a href="#neighbours">Compare neighbours</a>')
    source = replace_once(source, "'moves','shapes','tests','about'];",
                          "'moves','shapes','neighbours','tests','about'];")
    source = replace_once(source, "if(v==='shapes')drawShapes();",
                          "if(v==='neighbours')drawComparison();if(v==='shapes')drawShapes();")
    source = replace_once(source, '<section class="view" id="v-shapes">',
                          (HERE / "compare.html").read_text() + '\n<section class="view" id="v-shapes">')
    source = replace_once(source, "</style>", (HERE / "compare.css").read_text() + "\n</style>")
    payload = json.dumps(display, separators=(",", ":"), ensure_ascii=False).replace("<", "\\u003c")
    script = (HERE / "compare.js").read_text()
    script = replace_once(script, "COMPARISON_RESULTS", payload)
    source = replace_once(source, "/* hash routing */", script + "\n/* hash routing */")
    source = replace_once(source, 'id="v-neighbours" ', 'id="v-neighbours" data-results-sha256="' +
                          hashlib.sha256(result_bytes).hexdigest() + '" ')
    OUTPUT.write_text(source)
    print(f"{OUTPUT.name}  sha256 {hashlib.sha256(OUTPUT.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    build()
