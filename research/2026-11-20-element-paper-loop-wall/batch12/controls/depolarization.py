"""Three macroscopic boundary responses, with four interpolations of the Rb optical data."""
import csv
import hashlib
import math

import numpy as np
from scipy.integrate import quad, trapezoid
from scipy.interpolate import PchipInterpolator

from full_spectrum import HERE, table
from screened_optics import PIN, TABLE

GEOMETRIES = (0., 1/3, 1.)


def response(eps, n):
    chi=eps-1
    return np.imag(chi/(1+n*chi))


def metals():
    if hashlib.sha256(TABLE.read_bytes()).hexdigest()!=PIN:
        raise ValueError("The pinned Smith optical table changed")
    with TABLE.open() as source:
        rows=sorted(csv.DictReader(source),key=lambda r:float(r["energy_eV"]))
    energy=np.array([float(r["energy_eV"]) for r in rows])
    index=np.array([complex(float(r["n"]),float(r["k"])) for r in rows])
    eps=index**2
    computed={}
    for interp in ("linear_response","monotone_cubic_response","linear_index","linear_eps"):
        areas=[]
        for n in GEOMETRIES:
            y=response(eps,n)
            if interp=="linear_response":
                area=trapezoid(y,energy)
            elif interp=="monotone_cubic_response":
                area=PchipInterpolator(energy,y).integrate(energy[0],energy[-1])
            else:
                points=index if interp=="linear_index" else eps
                area=0.
                for lo,hi,z0,z1 in zip(energy,energy[1:],points,points[1:]):
                    def integrand(t):
                        z=z0+(z1-z0)*t
                        return response(z*z if interp=="linear_index" else z,n)
                    area+=(hi-lo)*quad(integrand,0,1,epsabs=1e-12)[0]
            areas.append(area)
        computed[interp]=areas
    return computed


def main():
    records=[]
    for label,(trans,sphere,longitudinal) in metals().items():
        top=math.sqrt(3.)
        outside=sphere/top-longitudinal
        share=1-top*longitudinal/sphere
        assert min(outside,share)>0
        records.append(dict(interpolation=label,T_window_eV=f"{trans:.10f}",
                            sphere_window_eV=f"{sphere:.10f}",L_window_eV=f"{longitudinal:.10f}",
                            sphere_over_L_window=f"{sphere/longitudinal:.10f}",
                            sphere_over_L_full_upper=f"{top:.10f}",
                            min_L_outside_eV=f"{outside:.10f}",min_L_fraction_outside=f"{share:.10f}"))
    table("depolarization_rb.csv",records)

if __name__=="__main__":
    main()
