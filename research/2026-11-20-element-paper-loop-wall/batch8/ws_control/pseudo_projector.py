"""Evaluate cell-block weights of selected orthonormalized smooth Bloch spans."""
import argparse
from itertools import product
from pathlib import Path
import struct
import xml.etree.ElementTree as ET

import numpy as np
from scipy.io import FortranFile

def numbers(text): return np.fromstring(text, sep=" ")

def ws_points(grid, cell, offset):
    """Uniform primitive-cell samples relocated to their nearest atomic image."""
    points = (np.indices((grid,)*3).reshape(3,-1).T + offset) / grid
    best = np.full(len(points),np.inf)
    assigned = points.copy()
    for t in product(range(-2,3),repeat=3):
        translated = points-np.array(t)
        cart = translated @ cell
        squared = np.einsum("ij,ij->i",cart,cart)
        select = squared < best
        best[select] = squared[select]
        assigned[select] = translated[select]
    return assigned

def blocks(save, symbol, mesh, grid, offset, semicore):
    root = ET.parse(save/"data-file-schema.xml").getroot().find("output")
    cell = np.array([numbers(i.text) for i in root.find("atomic_structure/cell")])
    reciprocal = np.array([numbers(i.text) for i in root.find("basis_set/reciprocal_lattice")])
    states = root.findall("band_structure/ks_energies")
    assert len(states)==mesh**3
    k = np.array([numbers(s.findtext("k_point")) for s in states]) @ np.linalg.inv(reciprocal)
    weights = np.array([float(s.find("k_point").get("weight")) for s in states])
    assert np.ptp(weights)<1.e-10
    indices = np.rint((k-k[0])*mesh).astype(int)%mesh
    assert len(set(map(tuple,indices)))==mesh**3
    evals=np.array([numbers(s.findtext("eigenvalues")) for s in states])
    mask=np.zeros_like(evals,dtype=bool)
    if symbol=='Rb':
        # Exclude occupied semicore; choose the lowest nk/2 outer levels for one electron/site.
        outer=evals[:,4:]
        order=np.argsort(outer,axis=None)
        n=len(k)//2
        assert outer.flat[order[n]]-outer.flat[order[n-1]]>1.e-10
        ii,jj=np.unravel_index(order[:n],outer.shape);mask[ii,4+jj]=True
    else:
        assert np.min(evals[:,9])-np.max(evals[:,8])>0
        mask[:,5:9]=True  # Kr 4s and 4p only; omit occupied semicore 3d.
    if semicore:
        mask[:, :4 if symbol == "Rb" else 5] = True
    real=ws_points(grid,cell,offset)
    owner=[]
    waves = np.empty((int(mask.sum()),grid**3),dtype=complex)
    cursor = 0
    min_gram=np.inf
    for index,ks in enumerate(k):
        bands=np.flatnonzero(mask[index])
        if not len(bands):continue
        with FortranFile(save/f'wfc{index+1}.dat','r') as f:
            ik, x, y, z, spin, gamma_only, scale = struct.unpack('=i3diid', f.read_record('u1'))
            alat = float(root.find('atomic_structure').get('alat'))
            expected_k = numbers(states[index].findtext('k_point')) * 2*np.pi/alat
            assert ik == index+1 and spin == 1 and gamma_only == 0
            assert np.allclose([x,y,z],expected_k,rtol=0,atol=1.e-9) and scale==1.
            ngw,npw,npol,nbnd=f.read_record('i4')
            assert npw==int(states[index].findtext('npw')) and npol==1 and nbnd==mask.shape[1]
            f.read_record('f8')
            miller=f.read_record('i4').reshape(-1,3)
            assert len(np.unique(miller%grid,axis=0))==npw, 'FFT undersampled'
            off=np.exp(2j*np.pi*(miller@offset/grid))
            cols=[]
            for j in range(bands[-1]+1):
                c=f.read_record('c16')
                if not mask[index,j]:continue
                cube=np.zeros((grid,)*3,dtype=complex)
                cube[tuple(miller.T%grid)]=c*off
                cols.append(np.fft.ifftn(cube,norm="ortho").ravel())
        u=np.stack(cols,axis=1)
        gram=u.conj().T@u
        vals,V=np.linalg.eigh(gram)
        min_gram=min(min_gram,vals[0])
        assert vals[0]>1.e-6
        u=u@((V/np.sqrt(vals))@V.conj().T)
        assert np.max(abs(u.conj().T@u-np.eye(len(bands))))<1.e-9
        psi=u*np.exp(2j*np.pi*(real@ks))[:,None]
        waves[cursor:cursor+len(bands)] = psi.T
        cursor += len(bands)
        owner.extend([index]*len(bands))
    assert cursor == len(waves)
    return waves, np.array(owner), indices, cell, min_gram

def run(save,symbol,mesh,grid,offset,semicore):
    waves,owner,k,cell,min_gram=blocks(save,symbol,mesh,grid,offset,semicore)
    # Spin is counted twice. The Frobenius square can be summed in blocks of state indices.
    bins=np.zeros(mesh**3)
    for start in range(0,len(waves),24):
        end=min(len(waves),start+24)
        W=abs(waves[start:end].conj() @ waves.T)**2
        delta=(k[owner[start:end],None,:]-k[owner[None,:]])%mesh
        ids=np.ravel_multi_index(delta.reshape(-1,3).T,(mesh,)*3)
        bins+=np.bincount(ids,weights=W.ravel(),minlength=mesh**3)
    Xcomplex=2*np.fft.ifftn(bins.reshape((mesh,)*3))/mesh**3
    assert np.max(abs(Xcomplex.imag))<1.e-9
    X=Xcomplex.real
    n=2*len(waves)/mesh**3
    assert abs(X.sum()-n)<1.e-8 and X.min()>-1.e-8
    B=n-X[0,0,0]
    trans=np.array(list(product(range(-2,3),repeat=3)))
    length=np.linalg.norm(trans@cell,axis=1)
    neighbours=trans[np.isclose(length,min(length[length>1.e-7]))]
    assert len(neighbours)=={'Rb':8,'Kr':12}[symbol]
    near=X[tuple((neighbours%mesh).T)]
    print(f'{symbol},{mesh},{grid},{n:.8f},{B:.9f},{near.mean():.9f},{near.min():.9f},{near.max():.9f},{near.sum()/B:.9f},{min_gram:.6f},{abs(X.sum()-n):.2e}',flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('save',type=Path);p.add_argument('symbol',choices=['Kr','Rb'])
    p.add_argument('mesh',type=int);p.add_argument('grid',type=int)
    p.add_argument('--offset',type=float,nargs=3,default=[.213,.367,.479])
    p.add_argument('--include-semicore', action='store_true')
    a=p.parse_args();run(a.save,a.symbol,a.mesh,a.grid,np.array(a.offset),a.include_semicore)
