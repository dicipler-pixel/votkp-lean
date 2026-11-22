"""Reproduce preliminary fixed-basis spin–orbit pseudopotential atomic ΔSCF checks."""
import argparse
import json
import sys
from pathlib import Path
import numpy as np
from pyscf import gto, scf, lib
from pyscf.data.nist import HARTREE2EV

ECP={'Rb':'ECPDS28MDFSO','Cs':'ECPDS46MDFSO','Fr':'ECPDS78MDFSO'}
SETS={'coarse':[(.03,3.,8),(.03,3.,8),(.1,3.,4)],
      'medium':[(.015625,2.,12),(.015625,2.,12),(.0625,2.,7)],
      'fine':[(.0078125,1.8,16),(.0078125,1.8,16),(.03125,1.8,10)]}
SETS['medium-f']=SETS['medium']+[(.10,2.5,4)]
SETS['fine-f']=SETS['fine']+[(.06,2.3,5)]
def mp2(hf, coulomb=None):
    """General spin-orbital MP2. Contract AO pair densities with exact Coulomb ERIs."""
    c=hf.mo_coeff
    n=hf.mol.nao
    occ=hf.mo_occ>0
    o=list(np.flatnonzero(occ))
    v=list(np.flatnonzero(~occ))
    rows,cols=np.tril_indices(n)
    packed=[]
    for i in o:
        d=np.zeros((len(rows),len(v)),dtype=complex)
        for spin in (0,1):
            C=c[spin*n:(spin+1)*n]
            d+=C[rows,i,None].conj()*C[cols][:,v]
            d+=(rows!=cols)[:,None]*C[cols,i,None].conj()*C[rows][:,v]
        packed.append(d.T)
    d=np.vstack(packed)
    if coulomb is None:
        coulomb=hf.mol.intor('int2e',aosym='s4')
    # The AO pair matrix is real. Avoid BLAS allocating a complex copy.
    contracted=(d.real@coulomb)+1j*(d.imag@coulomb)
    I=(contracted@d.T).reshape(len(o),len(v),len(o),len(v)).transpose(0,2,1,3)
    antisym=I-I.swapaxes(2,3)
    ei=hf.mo_energy[occ]; ea=hf.mo_energy[~occ]
    D=ei[:,None,None,None]+ei[None,:,None,None]-ea[None,None,:,None]-ea[None,None,None,:]
    # terms with repeated i=j or a=b vanish by antisymmetry even at degenerate holes
    mask=(np.arange(len(o))[:,None]!=np.arange(len(o)))[...,None,None] & (np.arange(len(v))[:,None]!=np.arange(len(v)))
    relevant=D[mask]
    if max(relevant)>=-1e-8:raise ValueError(f'Nonnegative or small MP2 denominators {max(relevant)}')
    return float(0.25*np.sum(abs(antisym[mask])**2/relevant)),float(-max(relevant))

def build(atom,charge,profile):
    basis=[[ell,[a*step**i,1.0]] for ell,(a,step,n) in enumerate(SETS[profile]) for i in range(n)]
    return gto.M(atom=atom,charge=charge,spin=(charge+1)%2,basis={atom:basis},ecp=ECP[atom],verbose=0,max_memory=450)

def optimize(atom,profile,soc,include_mp2=False):
    m1=build(atom,1,profile)
    hf=scf.GHF(m1)
    hf.with_soc=soc
    hf.chkfile=None
    hf.conv_tol=3e-10
    hf.max_cycle=100
    e1=hf.kernel()
    if not hf.converged:raise ValueError('closed-shell SCF failed')
    m2=build(atom,2,profile)
    g=scf.GHF(m2)
    g.with_soc=soc
    g.chkfile=None
    g.conv_tol=3e-10
    g.max_cycle=100
    occ=hf.mo_occ.copy()
    occ[np.where(occ>0)[0][-1]]=0
    seed=hf.make_rdm1(hf.mo_coeff,occ)
    e2=g.kernel(dm0=seed)
    if not g.converged:raise ValueError('one-hole SCF failed')
    details={}
    if include_mp2:
        corr1,den1=mp2(hf)
        corr2,den2=mp2(g)
        details=dict(mp2_corr1_Ha=corr1,mp2_corr2_Ha=corr2,mp2_IE_eV=(e2-e1+corr2-corr1)*HARTREE2EV,
                     minimum_MP2_denominators_Ha=[den1,den2])
    print(json.dumps(dict(atom=atom,basis=profile,n_ao=m1.nao,with_soc=soc,n_e=m1.nelectron,**details,
        E1_Ha=e1,E2_Ha=e2,second_IE_eV=(e2-e1)*HARTREE2EV,
        frozen_orbital_eV=-hf.mo_energy[hf.mo_occ>0][-1]*HARTREE2EV)),flush=True)

if __name__=='__main__':
    cli=argparse.ArgumentParser()
    cli.add_argument('atom',choices=ECP)
    cli.add_argument('profile',choices=SETS)
    cli.add_argument('--no-soc',action='store_true')
    cli.add_argument('--threads',type=int,default=1)
    cli.add_argument('--mp2',action='store_true')
    args=cli.parse_args()
    lib.num_threads(args.threads)
    optimize(args.atom,args.profile,not args.no_soc,args.mp2)
