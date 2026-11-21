"""Exact root isolation for the 9–11 eV Laporte et al. central Lorentz fits."""
import csv
from pathlib import Path

import numpy as np
from scipy.constants import epsilon_0, hbar, m_e
from scipy.integrate import quad
import sympy as sp

DIRECTORY=Path(__file__).resolve().parent
X=sp.symbols("x")
Q=sp.Rational


def polynomial(expr):
    return sp.Poly(expr,X,domain=sp.QQ)


def exact_roots(poly):
    # x=E² and all denominators are positive for E in [9,11] eV.
    isolation=poly.intervals(eps=Q(1,10**12),inf=81,sup=121)
    pairs=[]
    for (lo,hi),multiplicity in isolation:
        if multiplicity!=1:
            raise AssertionError("non-simple crossing")
        pairs.append(float(sp.sqrt((lo+hi)/2)))
    return pairs


def analyze(rows):
    # hbar² * number_density / (epsilon_0 * electron_mass) is in eV²
    # after converting both angular frequencies and charges to eV units.
    physical=float(rows[0]['number_density_1e21_cm3'])*1e27*hbar**2/(epsilon_0*m_e)
    amplitude=Q(f"{physical:.12f}")
    rho=Q(rows[0]['eps_background'])
    osc=[(Q(r['E_eV']),Q(r['gamma_eV']),Q(r['f'])) for r in rows]
    terms=[polynomial((w*w-X)**2 + g*g*X) for w,g,_ in osc]
    denominator=polynomial(1)
    for term in terms:
        denominator*=term
    real=rho*denominator
    imag_div_E=polynomial(0)
    for (w,g,f),term in zip(osc,terms,strict=True):
        factors=denominator.exquo(term)
        real+=amplitude*f*polynomial(w*w-X)*factors
        imag_div_E+=amplitude*f*g*factors
    d2=denominator**2
    modulus=real**2+polynomial(X)*imag_div_E**2
    wall=modulus**2-6*modulus*d2+d2**2
    eq=modulus-d2
    stationary=modulus.diff()*denominator-2*modulus*denominator.diff()
    physical_osc=[tuple(map(float,x)) for x in osc]
    def response(e):
        eps=complex(float(rho))
        for w,g,f in physical_osc:
            eps+=float(amplitude)*f/(w*w-e*e-1j*g*e)
        op=eps.imag
        loss=(-1/eps).imag
        if not (op>0 and loss>0):
            raise AssertionError("lost passivity")
        return eps,op,loss
    roots=[]
    for e in exact_roots(wall):
        value=abs(response(e)[0])**2
        branch="upper_wall" if value>1 else "lower_wall"
        np.testing.assert_allclose(value,3+(2 if value>1 else -2)*np.sqrt(2),rtol=1e-9)
        roots.append((e,branch,value))
    roots.extend((e,"equal_channels",abs(response(e)[0])**2) for e in exact_roots(eq))
    extrema=[(abs(response(e)[0])**2,e) for e in [9.,11.,*exact_roots(stationary)]]
    z_min,e_min=min(extrema);z_max,e_max=max(extrema)
    lower_integral=quad(lambda e:response(e)[2],9.,11.,epsabs=1e-10,limit=250)[0]
    optical_integral=quad(lambda e:response(e)[1],9.,11.,epsabs=1e-10,limit=250)[0]
    return sorted(roots),[float(amplitude),z_min,e_min,z_max,e_max,optical_integral,lower_integral]


def main():
    with (DIRECTORY/'krypton_fit_inputs.csv').open() as f:
        data=list(csv.DictReader(f))
    with (DIRECTORY/'krypton_screening_roots.csv').open('w',newline='') as f1, (DIRECTORY/'krypton_screening_scan.csv').open('w',newline='') as f2:
        w1,w2=csv.writer(f1,lineterminator="\n"),csv.writer(f2,lineterminator="\n")
        w1.writerow(('phase','T_K','event','model_E_eV','z_screen'))
        w2.writerow(('phase','T_K','plasma_prefactor_eV2','min_z','E_min_eV','max_z','E_max_eV','int_eps_im_eV','int_loss_eV'))
        for phase in ('solid','fluid'):
            rows=[r for r in data if r['phase']==phase]
            roots,scan=analyze(rows)
            w2.writerow((phase,rows[0]['T_K'],*(f"{x:.10f}" for x in scan)))
            for e,event,value in roots:
                w1.writerow((phase,rows[0]['T_K'],event,f"{e:.10f}",f"{value:.10f}"))


if __name__=='__main__':
    main()
