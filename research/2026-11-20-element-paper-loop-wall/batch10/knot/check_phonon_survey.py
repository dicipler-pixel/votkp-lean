"""Run on Supporting_Information.pdf from https://arxiv.org/src/2412.01280 (anc/)."""
import collections
import hashlib
from pathlib import Path
import re
import subprocess
import sys

source = Path(sys.argv[1])
assert hashlib.sha256(source.read_bytes()).hexdigest() == 'd812eb4f582505a2b4a2ef8ec7137efc76938bb5946b119ea9ad49d810ec806f'
text = subprocess.check_output(['pdftotext','-layout',str(source),'-'],text=True)
block = text[text.index('Table S10: List of materials'):text.index('Table S13:')]
hits = []
for line in block.splitlines():
    if 'mp-' in line:
        m = re.search(r'(mp-\d+)\s+(.*?)\s{2,}([A-Z]{1,3})\s+',line)
        assert m, line
        chemical_elements = set(re.findall(r'[A-Z][a-z]?', m[2]))
        assert len(chemical_elements) >= 2, line
        hits.append(m[1])
counts = collections.Counter(hits)
print(f'{len(hits)} rows, {len(counts)} unique material IDs; every formula contains multiple elements.')
print('IDs appearing twice:', ', '.join(sorted(k for k,v in counts.items() if v == 2)))
