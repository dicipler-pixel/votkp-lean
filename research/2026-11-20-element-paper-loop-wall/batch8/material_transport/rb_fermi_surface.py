"""Spin-summed cubic clean-band response reconstructed from QE symmetry-reduced grids."""
from itertools import permutations, product
from pathlib import Path
import argparse
import csv
import gzip
import json
import xml.etree.ElementTree as ET

import numpy as np
from scipy.ndimage import map_coordinates
from scipy.optimize import brentq
from scipy.signal import resample
from scipy.special import expit

EV_PER_HA=27.211386245981
ANG_PER_BOHR=0.529177210544


def extract_nodes(xml_file):
    out=ET.parse(xml_file).getroot().find('output')
    assert out.find('atomic_structure').attrib['bravais_index']=='3'
    bs=out.find('band_structure')
    n=int(bs.find('starting_k_points/monkhorst_pack').attrib['nk1'])
    extract=lambda parent:[np.fromstring(e.text,sep=' ').tolist() for e in out.find(parent)]
    nodes=[]
    for row in bs.findall('ks_energies'):
        nodes.append([np.fromstring(row.findtext('k_point'),sep=' ').tolist(),
                      float(row.find('k_point').attrib['weight']),
                      np.fromstring(row.findtext('eigenvalues'),sep=' ').tolist()])
    return dict(n=n,energy_unit='Ha',cell_unit='Bohr',k_unit='2pi/alat',
                reciprocal=extract('basis_set/reciprocal_lattice'),
                cell=extract('atomic_structure/cell'),mu=float(bs.findtext('fermi_energy')),
                nodes=nodes)


def band_grid(record):
    n=record['n']
    nb=len(record['nodes'][0][2])
    # Signed coordinate permutations are the full O_h group in Cartesian axes.
    recip=np.array(record['reciprocal'])
    inv=np.linalg.inv(recip)
    lattice=np.array(record['cell'])*ANG_PER_BOHR
    b_cart=2*np.pi*np.linalg.inv(lattice).T
    cube=np.full((n,n,n,nb),np.nan)
    for point,weight,bands in record['nodes']:
        pt=np.array(point)
        energies=np.array(bands)*EV_PER_HA
        orbit=set()
        for p in permutations((0,1,2)):
            for signs in product((1,-1),repeat=3):
                fractional=pt[list(p)]*signs @ inv * n
                nearest=np.rint(fractional).astype(int)
                assert np.max(np.abs(nearest-fractional))<1e-7
                orbit.add(tuple(nearest%n))
        assert abs(weight*n**3/2-len(orbit))<1e-6
        for idx in orbit:
            assert np.isnan(cube[idx]).all()
            cube[idx]=energies
    assert np.isfinite(cube).all()
    mu=record['mu']*EV_PER_HA
    return cube,b_cart,abs(np.linalg.det(lattice)),mu


def interpolate(cube,m,scheme):
    n=len(cube)
    if scheme=='Fourier':
        data=cube
        for axis in (0,1,2):
            data=resample(data,m,axis=axis)
        return data
    coords=np.indices((m,m,m),dtype=float)*n/m
    return map_coordinates(cube,coords,order=3,mode='grid-wrap')


def calculate(cube,b_cart,volume,ef,m,width,scheme):
    # Four deep semicore bands are full. Rb band 6 is separated from the
    # chemical potential on these grids. Explicitly check its Boltzmann tail.
    assert np.min(cube[:,:,:,5])-ef>0.5
    surface=interpolate(cube[:,:,:,4],m,scheme)
    mu=brentq(lambda v: expit((v-surface)/width).mean()-.5,
              surface.min()-1,surface.max()+1)
    f=expit((mu-surface)/width)
    shell=2*f*(1-f)/width
    frac=np.stack([(np.roll(surface,2,i)-8*np.roll(surface,1,i)+
                    8*np.roll(surface,-1,i)-np.roll(surface,-2,i))*m/12 for i in range(3)])
    # Partial derivatives in fractional coordinates = B times Cartesian gradient.
    grad=np.einsum('ij,jabc->iabc',np.linalg.inv(b_cart),frac)
    tij=np.einsum('abc,iabc,jabc->ij',shell,grad,grad,optimize=True)/m**3
    # Periodic integration by parts gives an independent curvature form.
    # Use two nested fourth-order first derivatives in the same finite-grid
    # convention to check convergence to the continuum identity.
    inverse=np.linalg.inv(b_cart)
    laplace=np.zeros_like(surface)
    for a in range(3):
        for j in range(3):
            dx=(np.roll(grad[a],2,j)-8*np.roll(grad[a],1,j)+
                8*np.roll(grad[a],-1,j)-np.roll(grad[a],-2,j))*m/12
            laplace+=inverse[a,j]*dx
    k_second=2*np.mean(f*laplace)/3
    diagonal=np.diag(tij)
    k=diagonal.mean()
    # e²/epsilon0 in eV Å; absolute unit and spin factors shown in README.
    plasma=np.sqrt(180.9512818*k/volume)
    return (len(cube),m,scheme,width,mu,shell.mean(),k,plasma,
            np.max(abs(tij-k*np.eye(3)))/k, np.min(cube[:,:,:,5])-mu,k_second,abs(k_second-k)/k)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('work',type=Path)
    p.add_argument('--read-bundle',type=Path,help='Use the archived irreducible QE bands instead of rerunning QE.')
    p.add_argument('--save-bundle',type=Path,help='Write irreducible bands read from the QE XML.')
    args=p.parse_args()
    args.work.mkdir(parents=True,exist_ok=True)
    records=json.loads(gzip.decompress(args.read_bundle.read_bytes())) if args.read_bundle else {}
    if not records:
        for n,case in [(12,'0.01'),(16,'nscf'),(20,'nscf'),(24,'nscf'),(32,'nscf'),(40,'nscf')]:
            xml=args.work/f'Rb-45-340-{n}-{case}'/'out/system.save/data-file-schema.xml'
            if xml.is_file():
                record=extract_nodes(xml)
                if record['n']==n:
                    records[str(n)]=record
    if args.save_bundle:
        args.save_bundle.write_bytes(gzip.compress(json.dumps(records,separators=(',',':')).encode(),mtime=0))
    fields=['QE_grid','quadrature_grid','interpolation','broadening_eV','mu_eV','DOS_states_eV_cell',
            'mean_K_eV_A2','intraband_plasma_energy_eV','max_relative_cubic_deviation','band6_floor_above_mu_eV','occupied_curvature_eV_A2','relative_form_difference']
    with (args.work/'Rb_fermi_surface.csv').open('w',newline='') as stream:
        writer=csv.writer(stream,lineterminator='\n')
        writer.writerow(fields)
        for record in records.values():
            cube,b,vol,ef=band_grid(record)
            for mesh in (48,72,96):
                for scheme in ('Fourier','cubic'):
                    for width in (.025,.05,.08,.12):
                        row=calculate(cube,b,vol,ef,mesh,width,scheme)
                        writer.writerow([format(x,'.10g') if isinstance(x,(float,np.floating)) else x for x in row])
                    stream.flush()


if __name__=='__main__':
    main()
