"""Memory-bounded exact contraction for large real-space orbital arrays."""
from tempfile import TemporaryDirectory
from pathlib import Path

import os

import numpy as np

from microscopic_response import load_states
from site_tensor import nc_projector, BOHR_A


def disk_weights(save, symbol, mesh, grid, family):
    states,ranks,kfrac,indices,cell,_=load_states(save,symbol,mesh,family,stream=True)
    offset=np.array([.213,.367,.479])
    real=nc_projector.ws_points(grid,cell,offset)
    wavevectors=np.repeat(indices,ranks,axis=0)
    count=int(ranks.sum())
    with TemporaryDirectory(dir=save.parent.parent,prefix="ws-tiles-") as temp:
        path=Path(temp)/"waves.bin"
        with path.open("wb") as out:
            for i,state in enumerate(states):
                if state is None:
                    continue
                G,_,coeff=state
                assert len(np.unique(G%grid,axis=0))==len(G)
                cube=np.zeros((grid,grid,grid,ranks[i]),dtype=complex)
                cube[tuple(G.T%grid)]=coeff*np.exp(2j*np.pi*(G@offset/grid))[:,None]
                periodic=np.fft.ifftn(cube,axes=(0,1,2),norm="ortho").reshape(-1,ranks[i])
                psi=periodic*np.exp(2j*np.pi*(real@kfrac[i]))[:,None]
                psi.T.tofile(out)
                if i%64==63:
                    out.flush()
                    os.fsync(out.fileno())
                    if hasattr(os,"posix_fadvise"):
                        os.posix_fadvise(out.fileno(),0,out.tell(),os.POSIX_FADV_DONTNEED)
        del states
        bytes_per_state=grid**3*np.dtype(np.complex128).itemsize
        assert path.stat().st_size==count*bytes_per_state
        shape=(mesh,)*3
        diagonal=np.zeros(mesh**3)
        cross=np.zeros(mesh**3)
        with path.open("rb") as file:
            def tile(start,end):
                file.seek(start*bytes_per_state)
                return np.fromfile(file,dtype=np.complex128,count=(end-start)*grid**3).reshape(end-start,-1)
            width=128
            for start in range(0,count,width):
                end=min(count,start+width)
                bra=tile(start,end).conj()
                for j in range(start,count,width):
                    stop=min(count,j+width)
                    ket=tile(j,stop)
                    overlap=bra@ket.T
                    delta=(wavevectors[start:end,None]-wavevectors[None,j:stop])%mesh
                    bins=np.ravel_multi_index(delta.reshape(-1,3).T,shape)
                    mass=np.bincount(bins,weights=(abs(overlap)**2).ravel(),minlength=mesh**3)
                    if j==start:
                        diagonal+=mass
                    else:
                        cross+=mass
        reverse=(-np.arange(mesh))%mesh
        histogram=diagonal+cross+cross.reshape(shape)[np.ix_(reverse,reverse,reverse)].ravel()
        X=2*np.fft.ifftn(histogram.reshape(shape))/mesh**3
        assert np.max(abs(X.imag))<1e-10
        return X.real,2*count/mesh**3,cell/BOHR_A
