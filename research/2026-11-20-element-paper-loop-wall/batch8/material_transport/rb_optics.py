"""Descriptive Drude fit of Smith's room-temperature Rb optical constants."""
import csv
from hashlib import sha256
from io import StringIO
from pathlib import Path
from urllib.request import urlopen

import numpy as np
from scipy.optimize import least_squares

PIN='e6d15e364f70de1cad8a96a20f75689f2fba8b21'
URL=f'https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/{PIN}/database/data/main/Rb/nk/Smith.yml'
EXPECTED='8c0909edac8f8955b53943276b3a63fe5bc72b5025253f5e27407ab427b24ede'
HC_EV_UM=1.2398419843320026

def main():
    data=urlopen(URL,timeout=30).read()
    assert sha256(data).hexdigest()==EXPECTED
    data=np.loadtxt(StringIO(data.decode().split('data: |')[1]))
    energy=HC_EV_UM/data[:,0]
    index=data[:,1]+1j*data[:,2]
    permittivity=index**2
    reflected=(1-index)/(1+index)
    power=abs(reflected)**2
    discriminant=abs(index)**2-6*index.real+1
    np.testing.assert_array_equal(power>.5,discriminant>0)
    np.testing.assert_allclose((1-1/index)/(1+1/index),-reflected)
    with Path(__file__).with_name('Rb_reflectance.csv').open('w',newline='') as output:
        writer=csv.writer(output,lineterminator='\n')
        writer.writerow(['wavelength_um','energy_eV','n','k','R_normal_incidence',
                         'complex_wall_discriminant','half_power_side'])
        for (wavelength,n,k),photon,r,w in zip(data,energy,power,discriminant,strict=True):
            writer.writerow([wavelength,round(photon,8),n,k,round(r,8),round(w,8),'above' if r>.5 else 'below'])

    with Path(__file__).with_suffix('.csv').open('w',newline='') as stream:
        writer=csv.writer(stream,lineterminator='\n')
        writer.writerow(('max_energy_eV','min_tabulated_energy_eV','points','background_epsilon','plasma_energy_eV',
                         'relaxation_energy_eV','rms_residual_per_component'))
        for top in (.85,1,1.25,1.5,2):
            select=energy<=top
            e=energy[select]
            d=permittivity[select]
            def residual(parameters):
                eps_b,wp,gamma=parameters
                diff=eps_b-wp**2/(e*(e+1j*gamma))-d
                return np.r_[diff.real,diff.imag]
            fit=least_squares(residual,[1,3.5,.03],bounds=([0,.1,0],[10,8,2]))
            assert fit.success
            rms=np.sqrt(np.mean(fit.fun**2))
            writer.writerow([top,round(e.min(),6),len(e),*np.round(fit.x,8),round(rms,8)])


if __name__=='__main__':
    main()
