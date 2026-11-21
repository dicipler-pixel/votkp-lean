"""Paired absorption and energy-loss readings of the same measured rubidium optical index."""
import csv
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path

import numpy as np
from scipy.constants import elementary_charge, epsilon_0
from scipy.integrate import quad, trapezoid
from scipy.interpolate import PchipInterpolator

DIRECTORY = Path(__file__).resolve().parent
TABLE = DIRECTORY.parents[1] / "batch8/material_transport/Rb_reflectance.csv"
PIN = "4fff5e6ad5d04790894d60f760ca237f131ca5a00340c62d20be65292253e674"


def branch(z):
    discriminant = z*z - 6*z + 1
    if discriminant == 0:
        return "wall"
    if discriminant < 0:
        return "inside"
    return "upper_outside" if z > 1 else "lower_outside"


def main():
    if sha256(TABLE.read_bytes()).hexdigest() != PIN:
        raise ValueError("Smith input table differs from pin")
    with TABLE.open() as f:
        rows = sorted(csv.DictReader(f),key=lambda r:F(r["energy_eV"]))
    spectra=[]
    with (DIRECTORY/"screened_optics.csv").open("w",newline="") as stream:
        w=csv.writer(stream,lineterminator="\n")
        w.writerow(("energy_eV","n","kappa","eps_re","eps_im","loss_im_minus_reciprocal",
                    "z_absorption_over_loss","Gamma_screen","wall_branch","real_index_only_branch"))
        for row in rows:
            n,k = F(row['n']),F(row['k'])
            a,b = n*n-k*k,2*n*k
            z=(n*n+k*k)**2
            loss=b/(a*a+b*b)
            gamma=(b-loss)/(b+loss)
            assert b>0 and b/loss==z and gamma==(z-1)/(z+1)
            assert (gamma*gamma>F(1,2)) == (z*z-6*z+1>0)
            assert -gamma==(1/z-1)/(1/z+1)
            values=tuple(float(x) for x in (a,b,loss,z,gamma))
            w.writerow((row['energy_eV'],row['n'],row['k'],*(f"{x:.10f}" for x in values),branch(z),branch(n**4)))
            spectra.append((float(row['energy_eV']),float(n),float(k),*values[:3]))
    energy,n,k,a,b,loss=np.array(spectra).T
    # These quantify interpolation sensitivity, without assigning statistical errors
    # to published point values for which the source table gives no pointwise sigma.
    fits=[("linear_in_eps_im_and_loss",trapezoid(b,energy),trapezoid(loss,energy)),
          ("shape_preserving_eps_im_and_loss",PchipInterpolator(energy,b).integrate(energy[0],energy[-1]),
           PchipInterpolator(energy,loss).integrate(energy[0],energy[-1]))]
    for label, real, imaginary, is_index in (("linear_complex_index",n,k,True),("linear_complex_permittivity",a,b,False)):
        bare=screened=0.
        for j,delta in enumerate(np.diff(energy)):
            e0,e1=complex(real[j],imaginary[j]),complex(real[j+1],imaginary[j+1])
            def dielectric(t):
                value=e0+(e1-e0)*t
                return value**2 if is_index else value
            bare+=delta*quad(lambda t:dielectric(t).imag,0,1,epsabs=1e-12)[0]
            screened+=delta*quad(lambda t:(-1/dielectric(t)).imag,0,1,epsabs=1e-12)[0]
        fits.append((label,bare,screened))
    # Photon energy is in eV. a³/2 is the bcc volume per atom in Å³.
    # ε0/(π n_e e²) × 1 eV converted to SI, then m² back to Å².
    standard=(epsilon_0/(np.pi*elementary_charge))*(5.700e-10)**3/2*1e20
    with (DIRECTORY/"screened_optics_window.csv").open("w",newline="") as stream:
        w=csv.writer(stream,lineterminator="\n")
        w.writerow(("interpolation","n_points","Emin_eV","Emax_eV","int_eps_im_eV","int_loss_eV",
                    "loss_over_optical_window","one_e_per_atom_optical_A2","one_e_per_atom_screened_A2",
                    "all_37_e_optical_A2","all_37_e_screened_A2"))
        for label,bare,screened in fits:
            w.writerow((label,len(energy),energy[0],energy[-1],*(f"{x:.10f}" for x in
                        (bare,screened,screened/bare,standard*bare,standard*screened,
                         standard*bare/37,standard*screened/37))))


if __name__=="__main__":
    main()
