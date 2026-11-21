"""Validate material counts, crystal interpretation, and the metallic/atomic scale distinction."""
from collections import Counter
from fractions import Fraction as F
from math import sqrt
from pathlib import Path
import csv

DIR=Path(__file__).resolve().parent

def read(file):
    with (DIR/file).open() as f:
        return list(csv.DictReader(f))


if __name__=='__main__':
    nuc=read('isotopes.csv'); frib=read('isotope_discoveries.csv')
    ns={(r['symbol'],int(r['A'])) for r in nuc}
    fs={(r['symbol'],int(r['A'])) for r in frib}
    assert len(ns)==len(nuc)==217 and fs-ns=={('Os',160)} and not ns-fs
    for r in frib:
        z,n,a=map(int,(r['Z'],r['N'],r['A']))
        assert a==z+n and int(r['net_up'])==2*z+n and int(r['net_down'])==z+2*n
    for r in nuc:
        if r['spin_parity'] in ('0+','0-'):
            assert r['derived_spin_zero_ground_dipole_muN']=='0'
    spectrum=read('spectral_lines.csv')
    assert len(spectrum)==840 and all(F(r['wavelength_nm'])>0 for r in spectrum)
    salts=read('ionic_radii.csv')
    assert len(salts)==23
    solids={r['COD']:r for r in read('crystals.csv')}
    cuts={r['COD'] for r in read('set_aside_cells.csv')}
    assert len(solids)==31 and len(cuts)==14 and not solids.keys()&cuts
    for r in read('material_constants.csv'):
        cell=solids[r['CIF_ref']]
        a,d,phase=float(cell['a_A']),float(cell['shortest_A']),r['phase_near_295K']
        if phase=='fcc':assert abs(d-a/sqrt(2))<1e-6
        if phase=='hcp':assert abs(d-sqrt(a*a/3+float(cell['c_A'])**2/4))<1e-6
        if phase=='liquid':assert r['symbol']=='Hg' and F(r['kappa_300K_W_mK'])==100*F('0.0834')
        sigma=100/F(r['rho_Ekin_295K_microohm_cm'])
        print(r['symbol'], 'sigma, MS/m',round(float(sigma),4),'solid contact r (pm)',round(d*50,3), 'liquid at 295 K' if phase=='liquid' else phase)
    opt=read('optics.csv')
    assert len(opt)==18
    def measured(source):
        return next(r for r in opt if r['channel']==source and r['wavelength_um']=='0.65')
    assert F(measured('Os ordinary')['R_semi_infinite'])<F(1,2)<F(measured('Os extraordinary')['R_semi_infinite'])
    print('217 IAEA rows, 218 FRIB rows, 840 spectral lines, 23 ionic radii, 31 accepted and 14 set-aside cell records, 18 optical rows')
