# Work Atlas

**Jeromie Beasley**

One cross-reference of every result across my papers and Lean repos: what it says, where it is in the paper, the exact Lean theorem that proves it, and how it connects to the rest.

- **Open `ATLAS.html`** to search and filter by paper or tag. Every Lean link opens the exact line on GitHub.
- **`STATUS.md`** lists what needs attention: a cited theorem that was renamed or removed, or a link to a result not yet entered.
- **`entries/*.json`** hold the results, one file per paper or line of work.

## How it stays current

`update_atlas.py` pulls every public Lean repo named in `repos.json`, indexes every declaration under its full name, and checks that every cited theorem still exists. It counts `sorry` and `admit`, keeping open-problem statement templates separate, and lists any axioms. It then rebuilds `ATLAS.html`, `atlas.json` and `STATUS.md`.

The GitHub Actions workflow `.github/workflows/update-atlas.yml` runs it every six hours, on every change to the entries, and on demand from the Actions tab. When the Lean repos change, the atlas follows on its own.

The atlas checks that the theorems exist. Checking the proofs themselves is each Lean repo's own CI.

## Entry format

```json
{"id": "paper.short-name", "title": "...", "statement": "...",
 "paper": {"title": "...", "version": "...", "section": "..."},
 "lean": {"repo": "dicipler-pixel/<repo>", "branch": "...", "file": "path/File.lean", "theorem": "exact_name"},
 "grade": "PROVED-LEAN | DERIVED-IN-PAPER | COMPUTED | MEASURED | STATED | PREDICTION | RECOGNISED",
 "tags": ["loop-wall"],
 "links": [{"to": "other.id", "kind": "same-wall | same-formula | special-case | generalises | opposite-reading | uses | analogy-only", "note": "..."}]}
```

A `lean` of `null` means no Lean proof is cited yet, and the page says so. `controls/false_control.json` is a false entry the checker must flag.
