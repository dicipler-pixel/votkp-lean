"""Tilt the two comparison-disk axes as an explicit control on orthogonality."""
import csv
import gzip
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

from mixed_faces import ARCHIVE_SHA, gamma

def margin(first, second, cosine):
    return first**2 + second**2 - 2*first*second*cosine - 1 + cosine**2

def tangent_angles(first, second):
    spread = math.sqrt((1-first**2)*(1-second**2))
    middle = first*second
    return [math.degrees(math.acos(max(-1., min(1., v))))
            for v in (middle+spread, middle-spread)]

def main():
    archive = Path(sys.argv[1])
    if hashlib.sha256(archive.read_bytes()).hexdigest() != ARCHIVE_SHA:
        raise ValueError("Archive differs from the recorded source")
    with gzip.open(archive, 'rt') as f:
        records = json.load(f, parse_float=Fraction)['records']
    def reflection(Z, core):
        q = Z-core-1
        thresholds = records[Z-1]['thresholds']
        return gamma(Fraction(thresholds[q+1]['IE_eV']) / thresholds[q]['IE_eV'])
    # For every nonsingular test, solve the two face equations independently.
    for x, y in [(Fraction(3,5),Fraction(4,5)), (Fraction(1,3),Fraction(2,3))]:
        for c in [Fraction(-3,5), Fraction(0), Fraction(4,5)]:
            norm_sq = x*x + (y-c*x)**2/(1-c*c)
            assert (norm_sq-1)*(1-c*c) == margin(x,y,c)
    assert margin(Fraction(3,5), Fraction(4,5), 0)==0
    w = csv.writer(sys.stdout,lineterminator='\n')
    w.writerow(['element_one','element_two','core_electrons','margin_at_90_deg',
                'lower_contact_deg','upper_contact_deg','upper_contact_minus_90_deg'])
    for n,left,right in [(2,6,7),(10,11,12),(18,19,20),(36,37,38),(54,55,56)]:
        g,h = reflection(left,n),reflection(right,n)
        lo,hi = tangent_angles(float(g),float(h))
        for angle in [lo,hi]:
            assert abs(margin(float(g),float(h),math.cos(math.radians(angle)))) < 1e-14
        mid = math.radians((lo+hi)/2)
        assert margin(float(g),float(h), math.cos(mid)) < 0
        w.writerow([records[left-1]['name'],records[right-1]['name'],n,
                    f'{float(margin(g,h,0)):.9f}',f'{lo:.8f}',f'{hi:.8f}',f'{hi-90:+.8f}'])

if __name__ == '__main__':
    main()
