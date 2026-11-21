"""Analytic screened-metal control; infrared fit compared to higher-energy rubidium rows."""
import csv
from pathlib import Path

import numpy as np
from scipy.integrate import quad, trapezoid

DIRECTORY=Path(__file__).resolve().parent
FIT_TABLE=DIRECTORY.parents[1]/"batch8/material_transport/rb_optics.csv"


def terms(energy, background, plasma, width):
    eps=background-plasma**2/(energy*(energy+1j*width))
    return eps.imag,(-1/eps).imag


def optical_above(low, plasma, width):
    return plasma**2/(2*width)*np.log1p((width/low)**2)


def loss_above(low, background, plasma, width):
    omega=plasma/np.sqrt(background)
    if not width<2*omega:
        raise ValueError("underdamped closed form")
    center=omega**2-width**2/2
    spread=width*np.sqrt(omega**2-width**2/4)
    return plasma**2*width/(2*background**2*spread)*(np.pi/2-np.arctan((low**2-center)/spread))


def main():
    with FIT_TABLE.open() as f:
        row=next(r for r in csv.DictReader(f) if r['max_energy_eV']=='1.25')
    b,p,g=[float(row[k]) for k in ('background_epsilon','plasma_energy_eV','relaxation_energy_eV')]
    data=np.genfromtxt(DIRECTORY/'screened_optics.csv',delimiter=',',names=True)
    energy=data['energy_eV'];hold=energy>1.25
    epsilon = (data['n'] + 1j*data['kappa'])**2
    raw_optical = epsilon.imag
    raw_loss = (-1/epsilon).imag
    with (DIRECTORY/'screened_drude.csv').open('w',newline='') as stream:
        w=csv.writer(stream,lineterminator='\n')
        w.writerow(('test','lower_eV','upper_eV','optical_integral_eV','loss_integral_eV'))
        for low,hi,label in ((energy[0],energy[-1],'full_observed_window'),(energy[hold][0],energy[-1],'heldout_window')):
            ob=optical_above(low,p,g)-optical_above(hi,p,g)
            lo=loss_above(low,b,p,g)-loss_above(hi,b,p,g)
            np.testing.assert_allclose(ob,quad(lambda e:terms(e,b,p,g)[0],low,hi)[0],rtol=1e-10)
            np.testing.assert_allclose(lo,quad(lambda e:terms(e,b,p,g)[1],low,hi,points=[p/np.sqrt(b)])[0],rtol=1e-10)
            w.writerow((label+'_drude',low,hi,f"{ob:.10f}",f"{lo:.10f}"))
            mask=(energy>=low) & (energy<=hi)
            w.writerow((label+'_data_trapezoid',low,hi,f"{trapezoid(raw_optical[mask],energy[mask]):.10f}",
                        f"{trapezoid(raw_loss[mask],energy[mask]):.10f}"))
        for low in (0.1,0.01,0.001):
            w.writerow(('idealized_finite_width_control',low,'inf',f"{optical_above(low,p,g):.10f}",f"{loss_above(low,b,p,g):.10f}"))
        w.writerow(('idealized_finite_width_control',0,'inf','inf',f"{loss_above(0,b,p,g):.10f}"))
    with (DIRECTORY/'screened_drude_rows.csv').open('w',newline='') as stream:
        w=csv.writer(stream,lineterminator='\n')
        w.writerow(('energy_eV','test_group','data_eps_im','drude_eps_im','data_loss','drude_loss'))
        for i,r in enumerate(data):
            energy=r['energy_eV']
            op,screened=terms(energy,b,p,g)
            w.writerow((energy,'heldout' if energy>1.25 else 'fit_window',f"{raw_optical[i]:.10f}",
                        f"{op:.10f}",f"{raw_loss[i]:.10f}",f"{screened:.10f}"))


if __name__=='__main__':
    main()
