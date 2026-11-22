"""Run with paths to LoC 1926 PDF, NIST handbook iron HTML, pinned mirror root and output directory."""
import argparse
import bisect
import csv
import hashlib
import re
import statistics
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
for name in ('book', 'handbook', 'mirror', 'output'):
    parser.add_argument(name, type=Path)
args = parser.parse_args()
root = ET.fromstring(subprocess.check_output(['pdftotext', '-f', '224', '-l', '224', '-bbox', args.book, '-']))
columns = {'iron': [], 'recent': [], 'remote': []}
for word in root.iter('{http://www.w3.org/1999/xhtml}word'):
    label = re.fullmatch(r'(\d{4}\.\d)(\**)', word.text or '')
    if label and 125 <= float(word.attrib['yMin']) <= 394:
        x = float(word.attrib['xMin'])
        column = 'iron' if 155 < x < 181 else 'recent' if 227 < x < 249 else 'remote' if 296 < x < 317 else None
        if column:
            columns[column].append((float(label[1]), label[2]))
assert all(len(v) == 23 and v == sorted(v, reverse=True) for v in columns.values())
columns['iron prose'], columns['recent prose'], columns['remote prose'] = [[(v, '')] for v in (7817.2, 7392.3, 6944.8)]

spectra = {}
for species in ('Fe I', 'Fe II', 'Ni I', 'Ti I'):
    element, ion = species.split()
    path = args.mirror / 'nist_library/NIST_ELEMENTS' / element / f'{element}_{ion}.dat'
    with path.open() as source:
        next(source)
        lines = {float(row[3]) for row in csv.reader(source, delimiter='\t')}
    spectra[species] = sorted(w for w in lines if 3400 < w < 8100)
handbook_pattern = r'<td>(?:&nbsp;)*(\d+\.\d+)</td>\s*<td>Fe I</td>'
spectra['Strong Fe I'] = sorted({float(w) for w in re.findall(handbook_pattern, args.handbook.read_text()) if 3400 < float(w) < 8100})
assert spectra['Strong Fe I']

def nearest(values, wavelength):
    i = bisect.bisect_left(values, wavelength)
    return min(values[max(0, i - 1):i + 1], key=lambda wi:abs(wi-wavelength))

def write_csv(filename, rows):
    with (args.output / filename).open('w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

rows = [['column', 'printed_air_assumed_A', 'original_stars'] + [s + '_nearest_A' for s in spectra] + ['FeI_printed_minus_nearest_A']]
for name, values in columns.items():
    for w, stars in values:
        matches = [nearest(lines, w) for lines in spectra.values()]
        rows.append([name, w, stars, *matches, round(w - matches[0], 5)])
write_csv('iron_wavelengths_v1.csv', rows)
rows = [['reference', 'lines_3400_to_8100_A', 'column', 'max_delta_A', 'subtracted_calibration_A', 'hits_of_23', 'control_median', 'control_min', 'control_max', 'num_controls_at_least_observed', 'num_controls']]
for species, lab in spectra.items():
    for kind in ('iron', 'recent', 'remote'):
        waves = [w for w, stars in columns[kind]]
        for tolerance in (.05, .1, .2, .3, .5):
            for adjust in (0.0, .16, .19):
                def score(offset):
                    adjusted = [w - adjust + offset for w in waves]
                    return sum(abs(nearest(lab, w) - w) <= tolerance + 1e-10 for w in adjusted)
                actual = score(0)
                shifted = [score(d) for d in range(-50, 51) if abs(d) >= 5]
                rows.append([species, len(lab), kind, tolerance, adjust, actual, statistics.median(shifted), min(shifted), max(shifted), sum(n >= actual for n in shifted), len(shifted)])
write_csv('iron_controls_v1.csv', rows)
for row in rows[1:]:
    if row[3:5] == [.2, 0.0]:
        print(*row)
