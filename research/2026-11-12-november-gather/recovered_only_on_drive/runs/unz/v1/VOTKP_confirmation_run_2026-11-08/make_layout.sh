#!/bin/sh
# The analysis scripts read and write under .scratch/, the name of the working tree they were
# written in. This archive ships that tree as data/ so that it is visible in a file browser.
set -e
cd "$(dirname "$0")"
if [ ! -e .scratch ]; then
  ln -s data .scratch
  echo "linked .scratch -> data"
else
  echo ".scratch already exists"
fi
if [ ! -e data/stoimenow/12mut.out ]; then
  echo
  echo "NOTE: Stoimenow's tables are not in this archive. Run:"
  echo "      sh data/stoimenow/fetch_stoimenow.sh"
fi
if ! find . -name knotinfo_data_complete.csv | grep -q .; then
  echo
  echo "NOTE: the KnotInfo complete table is not in this archive. Download"
  echo "      knotinfo_data_complete.csv from knotinfo.org, then set the CSV path at the top of"
  echo "      code/shared/knotnames.py, code/shared/certificate_all.py, code/votkp/c6_jones_books.py,"
  echo "      code/votkp/c7_circuit.py, code/votkp/c8_benchmark_equal.py, code/votkp/c8_mutant_benchmark.py"
  echo "      and code/votkp/c8_verify_equal.py."
fi
echo
echo "code/ is on the path via PYTHONPATH for convenience:"
echo "      export PYTHONPATH=\"$PWD/code:$PWD/code/shared\""
