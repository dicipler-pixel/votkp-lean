#!/bin/sh
# Download Stoimenow's mutant tables. They are his; the report cites his URL.
set -e
cd "$(dirname "$0")"
BASE=https://stoimenov.net/stoimeno/homepage/ptab
for f in 12mut.out 13mut.out; do
  echo "fetching $f"
  curl -fsS -o "$f" "$BASE/$f"
done
ls -l 12mut.out 13mut.out
