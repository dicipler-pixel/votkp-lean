"""Conservative figure-reading sensitivity for the four preselected cerium comparisons."""
import argparse
import csv
from pathlib import Path

import mpmath as mp
import numpy as np
import pymupdf

from cerium_screening import DIRECTORY, X0, X25, fetch_plot
from scipy.constants import elementary_charge, epsilon_0, hbar

iv=mp.iv
iv.dps=35


def band(data,label,e,err_pt,scale):
    dx=2.5*err_pt/(X25-X0)
    x,y=data[label]
    inband=y[(x>=e-dx)&(x<=e+dx)]
    vals=[*inband,*np.interp([e-dx,e+dx],x,y)]
    return iv.mpf([min(vals)-err_pt*scale,max(vals)+err_pt*scale])


def bounds(data,e,method):
    if method=='raw_symbols':
        t=band(data,'psi',e,.25,.8/(517.303-432.520))
        phi=band(data,'delta',e,.25,2/(504.333-463.048))
        den=1+t**2+2*t*iv.cos(phi)
        u=(1-t**2)/den
        v=-2*t*iv.sin(phi)/den
        theta=iv.pi*80/180
        s2=iv.sin(theta)**2
        c=s2*iv.tan(theta)**2
        a=s2+c*(u**2-v**2)
        b=2*c*u*v
    else:
        a=band(data,'epsilon1',e,.56,300/(295.065-216.451))
        s=band(data,'sigma1',e,.56,8/(421.923-327.649))
        b=s*(1e5*hbar/(epsilon_0*elementary_charge*e))
    a1,a2,b1,b2=float(a.a),float(a.b),float(b.a),float(b.b)
    assert b1>0
    # Extremise b/(r²+b²) over the enclosing rectangle analytically. It
    # decreases with r=|a| and peaks in b where b=r.
    min_abs=0 if a1<=0<=a2 else min(abs(a1),abs(a2))
    max_abs=max(abs(a1),abs(a2))
    losses_min=[v/(max_abs**2+v**2) for v in (b1,b2)]
    b_at_max=np.clip(min_abs,b1,b2)
    max_loss=b_at_max/(min_abs**2+b_at_max**2)
    return b1,b2,min(losses_min),max_loss


def order(a,b):
    return "alpha" if a[0]>b[1] else "gamma" if b[0]>a[1] else "unresolved"


def main():
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument('pdf',type=Path)
    args=cli.parse_args()
    doc=pymupdf.open(args.pdf)
    page,=[p for p in doc if 'FIG. 1.' in p.get_text() and len(p.get_drawings())>700]
    data={phase:fetch_plot(page.get_drawings(),phase) for phase in ('alpha','gamma')}
    with (DIRECTORY/'cerium_reading_bounds.csv').open('w',newline='') as f:
        w=csv.writer(f,lineterminator="\n")
        w.writerow(('energy_eV','method','alpha_eps2_lo','alpha_eps2_hi','gamma_eps2_lo','gamma_eps2_hi',
                    'alpha_loss_lo','alpha_loss_hi','gamma_loss_lo','gamma_loss_hi','larger_optical','larger_loss'))
        for e in (.85,1.05,1.25,2.):
            for method in ('raw_symbols','response_panels'):
                a,b=[bounds(data[phase],e,method) for phase in ('alpha','gamma')]
                vals=(*a[:2],*b[:2],*a[2:],*b[2:])
                w.writerow((f"{e:.2f}",method,*(f"{v:.9f}" for v in vals),order(a[:2],b[:2]),order(a[2:],b[2:])))


if __name__=='__main__':
    main()
