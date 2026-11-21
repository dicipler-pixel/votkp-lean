"""Read sparse observables from the vector paths of van der Eb et al., Fig. 1."""
import argparse
import math
from pathlib import Path
import pymupdf as pdf

URL = 'https://pure.rug.nl/ws/portalfiles/portal/14529452/infraredandoptical.pdf'
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('pdf', type=Path, help=URL)
args = p.parse_args()
doc = pdf.open(args.pdf)
page, = [p for p in doc if 'FIG. 1.' in p.get_text() and len(p.get_drawings()) > 700]
paths = page.get_drawings()
# Tick centers in page points. Confirm against the axis strokes in this rendering.
x0, x25 = 324.481, 536.596
y0, y8 = 421.923, 327.649
horiz = [item for d in paths for item in d['items'] if item[0]=='l' and item[1].y==item[2].y]
vert = [item for d in paths for item in d['items'] if item[0]=='l' and item[1].x==item[2].x]
for y in (y0,y8):
    assert any(abs(start.y-y)<.03 and abs(start.x-x0)<.03 for _,start,end in horiz)
for x in (x0,x25):
    assert any(abs(start.x-x)<.03 and 520<start.y<540 for _,start,end in vert)

def get_segments(solid):
    result=[]
    for drawing in paths:
        box=drawing['rect']
        if not (315.9<box.y0<box.y1<421.93 and len(drawing['items'])>3):
            continue
        if (drawing['color'][2]>.45 and drawing['color'][0]==0) != solid:
            continue
        if not solid and drawing['color'] != (1,0,0):
            continue
        for kind,start,end in drawing['items']:
            assert kind=='l'
            if end.x > start.x:
                def coord(pt):
                    return (2.5*(pt.x-x0)/(x25-x0),8*(y0-pt.y)/(y0-y8))
                result.append((*coord(start), *coord(end)))
    return result

def value(segments,e):
    values=[v0+(v1-v0)*(e-e0)/(e1-e0) for e0,v0,e1,v1 in segments if e0<=e<=e1]
    assert values and max(values)-min(values)<.001
    return values[0]

def moment(segments,lo,hi):
    # Integrate sigma_1(E) dE/E exactly on each straight figure segment.
    total=0.; covered=0.
    for x,y,v,w in segments:
        a,b=max(x,lo),min(v,hi)
        if a>=b:continue
        m=(w-y)/(v-x)
        total+=m*(b-a)+(y-m*x)*math.log(b/a)
        covered+=b-a
    assert abs(covered-(hi-lo))<1.e-8
    return total

print('phase,sigma_0.85,sigma_1.05,sigma_1.25,sigma_2.00,peak_contrast,window_moment_0.85_to_2.00')
for name,solid in [('alpha',True),('gamma',False)]:
    segments=get_segments(solid)
    a,b,c,d=(value(segments,e) for e in (.85,1.05,1.25,2.))
    print(name, *(f'{v:.5f}' for v in (a,b,c,d,2*b/(a+c)-1,moment(segments,.85,2.))),sep=',')
