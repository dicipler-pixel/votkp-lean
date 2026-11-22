"""Lim et al. (2005) Eq. 10 dipolar core polarization in two-component ECP ΔSCF/MP2.

Atomic CPP Hamiltonian V = -alpha/2 [sum_i g(r_i) r_i/r_i^3]^2.
It contributes both one-electron and two-electron integrals.
"""
import argparse
import json
import numpy as np
from scipy.special import roots_legendre
from pyscf import lib, scf
from pyscf.dft import gen_grid
from pyscf.data.nist import HARTREE2EV
from atomic_control import build, mp2

PARAMETERS={'Cs':(.6935,1.4702),'Fr':(1.2500,1.1636)}


def polarization(mol, points):
    alpha, delta=PARAMETERS[mol.atom_symbol(0)]
    x,w=roots_legendre(points)
    radius=(1+x)/(1-x)
    radial_weights=w * 2/(1-x)**2 * radius**2
    # Lebedev 50 integrates angular polynomials up to degree 11 (2*l+1 <= 9).
    leb=gen_grid.MakeAngularGrid(50)
    f=np.zeros((3,mol.nao,mol.nao));f2=np.zeros((mol.nao,mol.nao));s=f2.copy()
    for r, wr in zip(radius,radial_weights):
        ao=mol.eval_gto('GTOval_sph',r*leb[:,:3])
        weight=wr*4*np.pi*leb[:,3]
        damp=(-np.expm1(-delta*r*r))**2 / r**2
        product=(ao.T*weight)@ao
        s+=product
        f2+=damp*damp*product
        for k in range(3):
            f[k]+=(ao.T*(weight*damp*leb[:,k]))@ao
    if abs(s-mol.intor_symmetric('int1e_ovlp')).max()>1e-10:
        raise ValueError('AO quadrature does not reproduce overlap')
    rr,cc=np.tril_indices(mol.nao)
    packed=f[:,rr,cc]
    ericorrection= -alpha*(packed.T@packed)
    return -.5*alpha*f2,ericorrection


def attach(mol, hsingle, eri):
    h=scf.GHF(mol)
    h.with_soc=True
    h.chkfile=None
    h.conv_tol=3e-10
    h.max_cycle=100
    base=h.get_hcore()
    nao=mol.nao
    base[:nao,:nao]+=hsingle
    base[nao:,nao:]+=hsingle
    h.get_hcore=lambda *args: base
    h._eri=eri
    return h


def run(atom,basis):
    m=build(atom,1,basis)
    h1,ge=polarization(m,100)
    r1,re=polarization(m,180)
    err1=np.max(abs(h1-r1));err2=np.max(abs(ge-re))
    if max(err1,err2)>3e-9:
        raise ValueError('radial quadrature change exceeded tolerance')
    del h1,ge
    eri=m.intor('int2e',aosym='s4')
    eri+=re
    del re
    h=attach(m,r1,eri)
    h.kernel()
    g=attach(build(atom,2,basis),r1,eri)
    occupancy=h.mo_occ.copy();occupancy[np.where(occupancy>0)[0][-1]]=0
    g.kernel(dm0=h.make_rdm1(h.mo_coeff,occupancy))
    if not (h.converged and g.converged): raise RuntimeError('SCF failed')
    a,_=mp2(h,coulomb=eri);b,_=mp2(g,coulomb=eri)
    print(json.dumps(dict(atom=atom,basis=basis,radial_convergence_hartree=[float(err1),float(err2)],
       deltaHF_eV=(g.e_tot-h.e_tot)*HARTREE2EV,deltaMP2_eV=(g.e_tot+b-h.e_tot-a)*HARTREE2EV,
       e_closed=h.e_tot,e_open=g.e_tot,mp2_closed=a,mp2_open=b)))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('atom',choices=PARAMETERS);p.add_argument('basis');a=p.parse_args()
    lib.num_threads(1);run(a.atom,a.basis)
