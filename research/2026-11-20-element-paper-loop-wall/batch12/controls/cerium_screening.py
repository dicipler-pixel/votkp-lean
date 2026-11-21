"""Two readings of van der Eb et al. Fig. 1 for the screened/optical phase comparison."""
import argparse
import csv
from hashlib import sha256
from pathlib import Path

import numpy as np
import pymupdf as pdf
from scipy.constants import elementary_charge, epsilon_0, hbar

DIRECTORY=Path(__file__).resolve().parent
X0,X25=324.481,536.596


def energy(x):
    return 2.5*(x-X0)/(X25-X0)


def fetch_plot(drawings, phase):
    markers={"psi":[],"delta":[]}
    lines={"epsilon1":[],"sigma1":[]}
    for item in drawings:
        box=item['rect'];color=item['color']
        if not color:
            continue
        alpha=color[0]==0 and color[2]>.45
        gamma=color==(1,0,0)
        if not ((phase=='alpha' and alpha) or (phase=='gamma' and gamma)):
            continue
        if len(item['items'])==1 and item['items'][0][0]=='re' and 2.7<box.width<2.95:
            x,y=(box.x0+box.x1)/2,(box.y0+box.y1)/2
            if 425<y<470:
                markers['psi'].append((energy(x),.8*(517.303-y)/(517.303-432.520)))
            if 473<y<528:
                markers['delta'].append((energy(x),2*(463.048-y)/(504.333-463.048)))
        if len(item['items'])<4:
            continue
        if 216.50<box.y0<box.y1<315.70:
            group="epsilon1"
        elif 315.90<box.y0<box.y1<421.93:
            group="sigma1"
        else:
            continue
        for kind,start,end in item['items']:
            if kind!='l' or end.x<=start.x:
                continue
            for point in [start,end]:
                val= -300*(point.y-216.451)/(295.065-216.451) if group=='epsilon1' else 8*(421.923-point.y)/(421.923-327.649)
                lines[group].append((energy(point.x),val))
    out={}
    for group,values in (markers|lines).items():
        values=np.array(sorted(values))
        # Duplicate plotted x values can occur where path segments join. Median
        # values at the same x preserve central line/marker coordinates.
        x=np.unique(np.round(values[:,0],8))
        y=np.array([np.median(values[np.round(values[:,0],8)==i,1]) for i in x])
        if x[0]>.85 or x[-1]<2:
            raise AssertionError("figure coverage: "+group)
        out[group]=(x,y)
    return out


def epsilon_at(data,e,method):
    pick=lambda name:np.interp(e,*data[name])
    if method=='raw_symbols':
        theta=np.radians(80.)
        rho=pick('psi')*np.exp(1j*pick('delta'))
        return np.sin(theta)**2*(1+np.tan(theta)**2*((1-rho)/(1+rho))**2)
    return pick('epsilon1')+1j*pick('sigma1')*1e5*hbar/(epsilon_0*elementary_charge*e)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('paper',type=Path)
    args=parser.parse_args()
    digest=sha256(args.paper.read_bytes()).hexdigest()
    if digest!="c1a40bea35fc3618e85c38837c6ca85ca7d964e01b5452a9796d52e24af7f30b":
        raise ValueError("Use the pinned vector edition of the Groningen PDF")
    doc=pdf.open(args.paper)
    page,=[p for p in doc if 'FIG. 1.' in p.get_text() and len(p.get_drawings())>700]
    drawings=page.get_drawings()
    strokes=[(i[1],i[2]) for d in drawings for i in d['items'] if i[0]=='l']
    for x,y in ((X0,517.303),(X0,432.520),(545.454,463.048),(545.454,504.333),
                (X0,216.451),(X0,295.065),(X0,421.923),(X0,327.649)):
        if not any(abs(a.x-x)<.02 and abs(a.y-y)<.02 and abs(b.y-y)<.02 and abs(b.x-a.x)>2.5 for a,b in strokes):
            raise AssertionError("axis calibration")
    data={phase:fetch_plot(drawings,phase) for phase in ('alpha','gamma')}
    with (DIRECTORY/'cerium_screening.csv').open('w',newline='') as stream:
        w=csv.writer(stream,lineterminator="\n")
        w.writerow(('energy_eV','method','phase','epsilon1','epsilon2','loss_im_minus_recip_epsilon','z_screen','Gamma_screen'))
        for e in (.85,1.05,1.25,2):
            for method in ('raw_symbols','response_panels'):
                for phase in data:
                    eps=epsilon_at(data[phase],e,method)
                    op=eps.imag
                    loss=(-1/eps).imag
                    if not op>0:
                        raise AssertionError("negative measured absorption")
                    z=op/loss
                    np.testing.assert_allclose(z,abs(eps)**2,rtol=1e-13)
                    w.writerow((f"{e:.2f}",method,phase,*(f"{value:.9f}" for value in (eps.real,op,loss,z,(z-1)/(z+1)))))


if __name__=='__main__':
    main()
