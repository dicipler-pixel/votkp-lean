"""Extract nearest laboratory Fe I lines from Nave et al. (1994) Table 4 and compare to the mirror."""
import argparse
import bisect
import csv
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
for name in ('nave_pdf', 'matches_csv', 'output_csv'):
    parser.add_argument(name, type=Path)
args = parser.parse_args()
source = subprocess.check_output(['pdftotext', '-layout', args.nave_pdf, '-']).decode()
text = source.split('Finding List\n')[-1]
# Each Table 4 line has four repeated (wavelength, wavenumber, multiplet) fields.
# A physical wavelength/wavenumber consistency check rejects OCR column collisions.
triples = re.compile(r'\b(\d{4,5}\.\d{2,5})\s+(\d{4,5}\.\d{1,4})\s+(\d{1,4})(?![.\d])')
lines = defaultdict(set)
for wave_text, wn_text, multiplet in triples.findall(text):
    wave, wn = float(wave_text), float(wn_text)
    if 3400 < wave < 8100 and 99955000 < wave*wn < 99995000:
        lines[wave].add(int(multiplet))
wavelengths = sorted(lines)
scores = Counter()
max_diff = 0
with args.matches_csv.open() as matchfile, args.output_csv.open('w', newline='') as out:
    writer = csv.writer(out)
    writer.writerow(['column', 'printed_A', 'Nave_Table4_air_A', 'multiplet_numbers', 'NIST_mirror_minus_Nave_A', 'within_0.20_A'])
    for row in csv.DictReader(matchfile):
        w = float(row['printed_air_assumed_A'])
        i = bisect.bisect_left(wavelengths, w)
        near = min(wavelengths[i-1:i+1], key=lambda wl: abs(w-wl))
        difference = float(row['Fe I_nearest_A']) - near
        max_diff = max(max_diff, abs(difference))
        hit = abs(w-near) <= .2 + 1e-10
        scores[row['column']] += int(hit)
        writer.writerow([row['column'], w, near, ';'.join(map(str,sorted(lines[near]))), round(difference,6), hit])
print('Distinct air wavelengths extracted in window', len(wavelengths))
print('Largest nearest-wavelength discrepancy vs observed mirror (Å)', round(max_diff,6))
print('Hits by column', dict(scores))
