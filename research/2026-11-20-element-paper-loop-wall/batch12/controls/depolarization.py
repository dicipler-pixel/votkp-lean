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
    audit=[]
    for interp in ("linear_response","monotone_cubic_response","linear_index","linear_eps"):
        areas=[]
        for n in (*GEOMETRIES,.132):
            y=response(eps,n)
            cubic=PchipInterpolator(energy,y)
            area=0.
            inverse_area=0.
            for j,(lo,hi) in enumerate(zip(energy,energy[1:])):
                def integrand(t):
                    if interp=="linear_response":
                        return y[j]+t*(y[j+1]-y[j])
                    if interp=="monotone_cubic_response":
                        return cubic(lo+t*(hi-lo))
                    if interp=="linear_index":
                        z=index[j]+t*(index[j+1]-index[j])
                        return response(z*z,n)
                    return response(eps[j]+t*(eps[j+1]-eps[j]),n)
                area+=(hi-lo)*quad(integrand,0,1,epsabs=1e-12)[0]
                inverse_area+=(hi-lo)*quad(lambda t:integrand(t)/(lo+t*(hi-lo)),0,1,epsabs=1e-12)[0]
            if n in GEOMETRIES:
                areas.append(area)
            if n>0:
                cap=math.pi/(2*n)
                audit.append(dict(interpolation=interp,depolarization=n,
                                  inverse_window=f"{inverse_area:.10f}",full_inverse_cap=f"{cap:.10f}",
                                  fraction_consumed=f"{inverse_area/cap:.10f}",
                                  passes_necessary_test=inverse_area<=cap))
            if n==.132:
                assert inverse_area>math.pi/(2*n)
        computed[interp]=areas
    table("depolarization_passivity.csv",audit)
    return computed


def main():
    records=[]
    for label,(trans,sphere,longitudinal) in metals().items():
        top=math.sqrt(3.)
        outside=sphere/top-longitudinal
        share=1-top*longitudinal/sphere
        assert min(outside,share)>0
        records.append(dict(interpolation=label,physical_audit="rejected_at_n_0.132",T_window_eV=f"{trans:.10f}",
                            sphere_window_eV=f"{sphere:.10f}",L_window_eV=f"{longitudinal:.10f}",
                            sphere_over_L_window=f"{sphere/longitudinal:.10f}",
                            sphere_over_L_full_upper=f"{top:.10f}",
                            min_L_outside_eV=f"{outside:.10f}",min_L_fraction_outside=f"{share:.10f}"))
    table("depolarization_rb.csv",records)

if __name__=="__main__":
    main()
