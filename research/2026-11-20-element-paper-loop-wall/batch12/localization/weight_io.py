"""Lossless text interchange for finite Wigner–Seitz projector weights."""
import argparse
import csv
from pathlib import Path

import numpy as np


def write_weights(path, weights, cell, filling):
    if path.suffix == ".npz":
        np.savez_compressed(path,X=weights,cell_A=cell,nu=filling)
        return
    if path.suffix != ".csv":
        raise ValueError("Use a .csv or .npz weight file.")
    with path.open("w", newline="") as stream:
        writer=csv.writer(stream,lineterminator="\n")
        writer.writerow(["mesh",len(weights)])
        writer.writerow(["nu",float(filling)])
        for i,vec in enumerate(cell):
            writer.writerow([f"a{i+1}_A",*map(float,vec)])
        writer.writerow(["i","j","k","X"])
        for idx in np.ndindex(weights.shape):
            writer.writerow([*idx,float(weights[idx])])


def read_weights(path):
    if path.suffix == ".npz":
        with np.load(path) as file:
            return file["X"],file["cell_A"],float(file["nu"])
    with path.open(newline="") as stream:
        rows=csv.reader(stream)
        label,mesh=next(rows)
        assert label=="mesh"
        label,nu=next(rows)
        assert label=="nu"
        cell=[]
        for i in range(3):
            label,*coords=next(rows)
            assert label==f"a{i+1}_A" and len(coords)==3
            cell.append([float(x) for x in coords])
        assert next(rows)==["i","j","k","X"]
        weights=np.empty((int(mesh),)*3)
        for coord in np.ndindex(weights.shape):
            i,j,k,value=next(rows)
            assert (int(i),int(j),int(k))==coord
            weights[coord]=float(value)
        assert next(rows,None) is None
    return weights,np.array(cell),float(nu)


if __name__=="__main__":
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument("input",type=Path)
    cli.add_argument("output",type=Path)
    args=cli.parse_args()
    original=read_weights(args.input)
    write_weights(args.output,*original)
    assert all(np.array_equal(a,b) for a,b in zip(original,read_weights(args.output)))
