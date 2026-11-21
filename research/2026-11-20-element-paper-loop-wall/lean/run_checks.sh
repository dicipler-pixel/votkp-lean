#!/bin/sh
# SCRIPT: VOTKP-ELEMENTS-LOOPWALL-RUN-01
# Core Lean 4.34.1, no Mathlib. Builds LoopWall, prints the axiom audit, scans the source,
# and confirms each false control is rejected (each is also refuted inside LoopWall.lean).
set -e
cd "$(dirname "$0")"
LEAN=${LEAN:-lean}
$LEAN -o LoopWall.olean LoopWall.lean
echo "BUILD OK: $(grep -c '^theorem' LoopWall.lean) theorems"
LEAN_PATH=. $LEAN -o OpeningMap.olean OpeningMap.lean
echo "BUILD OK: OpeningMap, $(grep -c '^theorem' OpeningMap.lean) theorems"
LEAN_PATH=. $LEAN Audit.lean
LEAN_PATH=. $LEAN AuditMap.lean
if grep -n -E 'sorry|admit|native_decide|^axiom' LoopWall.lean OpeningMap.lean; then echo SCAN FAILED; exit 1; else echo "SCAN OK: no sorry, admit, native_decide or axiom"; fi
for f in controls/*.lean; do
  if LEAN_PATH=. $LEAN "$f" >/dev/null 2>&1; then echo "CONTROL ACCEPTED (bad): $f"; exit 1; else echo "control rejected: $f"; fi
done
