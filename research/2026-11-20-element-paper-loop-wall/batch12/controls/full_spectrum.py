"""Full-frequency screening bounds, with direct real-pole and imaginary-axis controls."""
import csv
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad

HERE = Path(__file__).resolve().parent
# (name, static relative permittivity, transverse frequencies, normalized static contributions)
MODELS = [
    ("single_25", 25., [1.], [1.]),
    ("single_36", 36., [1.], [1.]),
    ("split_36", 36., [.01, 1.], [.9, .1]),
    ("split_more_36", 36., [.0001, 1.], [.99, .01]),
    ("three_lines", 1.66, [.8, 2., 5.], [.2, .5, .3]),
]


def table(name, rows):
    with (HERE / name).open("w", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=rows[0], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def finite_models():
    records = []
    for name, eps, frequencies, shares in MODELS:
        w, shares = np.array(frequencies), np.array(shares)
        np.testing.assert_allclose(sum(shares), 1.)
        v = np.sqrt((eps-1)*shares)*w
        # For epsilon = 1 + v^T (D - omega² I)^-1 v, Sherman–Morrison gives
        # 1-1/epsilon = v^T (D + vv^T - omega² I)^-1 v.
        eigenvalues, frame = np.linalg.eigh(np.diag(w*w)+np.outer(v, v))
        longs = np.sqrt(eigenvalues)
        strengths = (frame.T @ v)**2
        def susceptibility(xi):
            return np.sum(v*v/(w*w+xi*xi))
        for p in [-1., -.5, 0., .5, 1.]:
            T = math.pi/2 * np.sum(v*v*w**(p-1))
            L = math.pi/2 * np.sum(strengths*longs**(p-1))
            z = T/L
            upper = eps**((1-p)/2)
            assert 1-1e-9 <= z <= upper+1e-8
            if p in (-1., 1.) or len(w)==1:
                np.testing.assert_allclose(z, upper,rtol=1e-10)
            im_z = ""
            if p==0:
                # Split near the narrowest pole to help quadrature in separated controls.
                def integral(fun):
                    return quad(fun,0,w[0],epsabs=1e-13)[0]+quad(fun,w[0],np.inf,epsabs=1e-13)[0]
                T_imag = integral(susceptibility)
                L_imag = integral(lambda xi: susceptibility(xi)/(1+susceptibility(xi)))
                np.testing.assert_allclose([T_imag,L_imag],[T,L],rtol=1e-10)
                im_z = f"{T_imag/L_imag:.10f}"
            records.append(dict(model=name, static_eps=eps, p=p, T_p=f"{T:.10f}", L_p=f"{L:.10f}",
                                ratio=f"{z:.10f}", upper=f"{upper:.10f}", independently_imaginary_ratio=im_z,
                                upper_wall="outside" if z>3+2*math.sqrt(2) else "inside"))
    table("full_spectrum_controls.csv",records)


def fluid_kr():
    # Harvey–Lemmon, Table II and equations (1), (5), (6). Density in mol/cm³.
    with (HERE/"krypton_fit_inputs.csv").open() as src:
        states=[row for row in csv.DictReader(src) if row["phase"]=="fluid"]
        state=states[0]
    T=float(state["T_K"])
    rho=float(state["number_density_1e21_cm3"])*1e21/6.02214076e23
    inv_t=273.16/T-1
    polar=rho*(6.273+(6.485+13.48*inv_t)*rho+(-82.51-170.4*inv_t)*rho**1.7)
    eps=(1+2*polar)/(1-polar)
    upper=math.sqrt(eps)
    with (HERE/"krypton_screening_scan.csv").open() as src:
        band=next(row for row in csv.DictReader(src) if row["phase"]=="fluid")
    b=float(state["eps_background"])-1
    oscillator_increment=float(band["plasma_prefactor_eV2"])*sum(
        float(row["f"])/float(row["E_eV"])**2 for row in states)
    a=b+oscillator_increment
    s=eps-1
    assert b>=0 and a+b>=s and 0<oscillator_increment<s
    # Use the committed ten-decimal partial-integral values as the parent extraction.
    tw=float(band["int_eps_im_eV"])
    lw=float(band["int_loss_eV"])
    min_out = tw/upper - lw
    min_fraction=1-upper*lw/tw
    table("full_spectrum_krypton.csv",[dict(T_K=T,rho_mol_cm3=f"{rho:.12f}",
        eps_static_fit=f"{eps:.10f}",full_z_upper=f"{upper:.10f}",
        full_Gamma_upper=f"{(upper-1)/(upper+1):.10f}",window_T_eV=tw,window_L_eV=lw,
        window_ratio=f"{tw/lw:.10f}",min_L_outside_eV=f"{min_out:.10f}",
        min_fraction_L_outside=f"{min_fraction:.10f}",
        VUV_chi_background=b,VUV_chi_zero=f"{a:.10f}",VUV_static_increment=f"{oscillator_increment:.10f}",
        all_shape_inverse_cap_fraction=f"{oscillator_increment/s:.10f}")])

if __name__=="__main__":
    finite_models()
    fluid_kr()
