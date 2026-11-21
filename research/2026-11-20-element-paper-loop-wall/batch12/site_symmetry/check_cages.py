"""Determine local inversion from elemental coordinates, using measured lengths for neighbour selection."""
import argparse
import csv
import hashlib
import itertools
from fractions import Fraction
from collections import Counter
from pathlib import Path
import gemmi

HERE = Path(__file__).resolve().parent
# Cell fractions are multiples of 1/12 in all selected special Wyckoff orbits.
SCALE = 12
SAMPLES = [('La','dhcp','9008525'), ('Pr','dhcp','9008527'), ('Nd','dhcp','9008526'),
           ('La','fcc','9008472'), ('La','hcp','9008503'), ('Nd','fcc','1538695'),
           ('Nd','hcp','9008508')]

def site_basis(structure):
    basis = []
    for site in structure.get_all_unit_cell_sites():
        frac = list(site.fract)
        fixed=tuple(round(x*SCALE)%SCALE for x in frac)
        if max(abs(x*SCALE-round(x*SCALE)) for x in frac)>0.002:
            raise ValueError(f'coordinate outside special-position tolerance: {frac}')
        basis.append(fixed)
    return sorted(set(basis))

def cage(structure, sites, center, shell):
    vectors=[]
    for neighbor,c in enumerate(sites):
        for cell in itertools.product(range(-shell,shell+1),repeat=3):
            v=tuple(b-a+SCALE*t for a,b,t in zip(center,c,cell))
            if any(v):
                d=structure.cell.orthogonalize(gemmi.Fractional(*(x/SCALE for x in v))).length()
                vectors.append((d,v,neighbor))
    vectors.sort()
    assert vectors[12][0]>1.3*vectors[11][0]
    return vectors[:13]

def inverted(v):
    return tuple(-x for x in v)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('cif_folder',type=Path)
    args=p.parse_args()
    with (HERE/'source_models.csv').open() as f:
        hashes={r['COD']:r['sha256'] for r in csv.DictReader(f)}
    rows=[]
    for symbol,phase,cod in SAMPLES:
        path=args.cif_folder/(cod+'.cif')
        assert hashlib.sha256(path.read_bytes()).hexdigest()==hashes[cod]
        structure=gemmi.make_small_structure_from_block(gemmi.cif.read(str(path)).sole_block())
        sites=site_basis(structure)
        expected={'fcc':4,'hcp':2,'dhcp':4}[phase]
        assert len(sites)==expected
        cages=[cage(structure,sites,s,2) for s in sites]
        assert cages==[cage(structure,sites,s,3) for s in sites]
        ids=[]
        for neighbors in cages:
            vs={v for d,v,k in neighbors[:12]}
            ids.append(sum(inverted(v) in vs for v in vs))
        assert Counter(ids)=={'fcc':{12:4},'hcp':{6:2},'dhcp':{12:2,6:2}}[phase]
        signature=lambda n: sorted(round(d,8) for d,v,k in n[:12])
        assert all(signature(n)==signature(cages[0]) for n in cages)
        for i,(point,neighbors,n_opposite) in enumerate(zip(sites,cages,ids)):
            same=sum(ids[k]==n_opposite for _,_,k in neighbors[:12])
            assert same==(6 if phase=='dhcp' else 12)
            # Fractional first and second tensors determine their Cartesian versions
            # via the same invertible linear cell map at either site.
            selected=[v for _,v,_ in neighbors[:12]]
            if phase=='dhcp':
                reference=[v for _,v,_ in cages[0][:12]]
                assert all(sum(v[j] for v in selected)==0 for j in range(3))
                for j,k in itertools.product(range(3), repeat=2):
                    assert sum(v[j]*v[k] for v in selected)==sum(v[j]*v[k] for v in reference)
            # Cartesian (x+iy)/a = u+ωv; ω²+ω+1=0 for the hexagonal setting.
            coeffs=['','']
            if phase in ('dhcp','hcp'):
                A=Fraction(sum(u**3+v**3-3*u*v*v for u,v,w in selected),12*SCALE**3)
                B=Fraction(sum(3*u*v*(u-v) for u,v,w in selected),12*SCALE**3)
                norm2=A*A-A*B+B*B
                assert norm2 == (0 if n_opposite==12 else Fraction(1,108))
                coeffs=[str(A),str(B)]
            ds=Counter(round(d,8) for d,v,k in neighbors[:12])
            rows.append([symbol,phase,cod,*point,n_opposite,n_opposite//2,same,12-same,
                         '|'.join(f'{k:.6f}x{v}' for k,v in sorted(ds.items())),f'{neighbors[12][0]:.6f}',*coeffs])
    with (HERE/'site_cages.csv').open('w',newline='') as fp:
        out=csv.writer(fp,lineterminator='\n')
        out.writerow(('element','structure','COD','12x','12y','12z','neighbors_with_antipode',
                      'opposite_pairs','same_cage_neighbors','other_cage_neighbors','first_12_A_x_count','13th_A','T3_basis_1','T3_basis_omega'))
        out.writerows(rows)
    print(f'{len(rows)} sites, {len(SAMPLES)} complete structures; all counts, shell gaps and radius signatures pass')

if __name__=='__main__':
    main()
