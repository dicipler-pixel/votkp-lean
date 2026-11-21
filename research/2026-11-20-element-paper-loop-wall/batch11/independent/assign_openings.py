"""Find the orbitals of the two removals from three successive ASD ground states."""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

CORES = {
    "He": "1s^{2}", "Ne": "[He]2s^{2}2p^{6}", "Ar": "[Ne]3s^{2}3p^{6}",
    "Kr": "[Ar]3d^{10}4s^{2}4p^{6}", "Cd": "[Kr]4d^{10}5s^{2}",
    "Xe": "[Cd]5p^{6}",
}
NAMES = {2:"He core", 10:"Ne core", 18:"Ar core", 28:"filled 3d10",
         36:"Kr core", 46:"filled 4d10", 54:"Xe core"}


def occupation(shells):
    match = re.match(r"\[([A-Za-z]+)\]", shells)
    if match:
        result = occupation(CORES[match[1]])
        shells = shells[match.end():]
    else:
        result = Counter()
    while shells:
        term = re.match(r"(\d[spdf])(?:\^\{(\d+)\})?", shells)
        if not term:
            raise ValueError(f"unparsed shell {shells!r}")
        result[term[1]] += int(term[2] or "1")
        shells = shells[term.end():]
    return result


def removed(before, after):
    diff = before.copy()
    diff.subtract(after)
    changes = [(name, count) for name, count in diff.items() if count]
    if len(changes) != 1 or changes[0][1] != 1:
        raise ValueError(f"several occupations change: {changes}")
    return changes[0][0]


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python assign_openings.py asd_configurations.csv")
    with Path(sys.argv[1]).open() as f:
        cfgs = {(int(row["Z"]),int(row["q"])):row["ground_shells"] for row in csv.DictReader(f)}
    out = csv.writer(sys.stdout, lineterminator="\n")
    out.writerow(["Z","k","intermediate_electrons","opening","earlier_loss","later_loss",
                  "initial_configuration","intermediate_configuration","final_configuration"])
    for z in sorted({z for z,q in cfgs}):
        for n in sorted(NAMES, reverse=True):
            k = z-n
            if k < 1:
                continue
            text = [cfgs[z,q] for q in (k-1,k,k+1)]
            occ = [occupation(t) for t in text]
            if [sum(x.values()) for x in occ] != [n+1,n,n-1]:
                raise ValueError(f"wrong electron count for {z},{n}")
            out.writerow([z,k,n,NAMES[n],removed(*occ[:2]),removed(*occ[1:]),*text])


if __name__ == "__main__":
    main()
