#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "$0")" && pwd)"
compiler="$(command -v "${LEAN:-lean}")"
tmpdir="$(mktemp -d)"
trap 'rm -rf -- "$tmpdir"' EXIT
cd "$root"
"$compiler" --version
"$compiler" -o "$tmpdir/BoundaryAgreement.olean" BoundaryAgreement.lean
if LEAN_PATH="$tmpdir" "$compiler" controls/FalseAtThird.lean > "$tmpdir/rejected.log" 2>&1; then
  echo 'Unexpected success: false control accepted'
  exit 1
fi
grep -Eq "error: .*grind.* failed" "$tmpdir/rejected.log"
cat "$tmpdir/rejected.log"
