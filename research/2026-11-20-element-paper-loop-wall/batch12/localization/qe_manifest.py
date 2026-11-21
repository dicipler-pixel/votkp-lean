"""Record the frozen-density and k-mesh evidence behind the localization readouts."""
import argparse
import csv
import hashlib
from pathlib import Path
import re
import xml.etree.ElementTree as ET


def digest(path):
    h=hashlib.sha256()
    with path.open("rb") as src:
        for chunk in iter(lambda:src.read(4<<20),b""):
            h.update(chunk)
    return h.hexdigest()


def collect(run, family, series, element, mesh):
    output=(run/"nscf.out").read_text()
    save=run/"out/system.save"
    if "JOB DONE." not in output or "Calculation stopped" in output or not (save/f"wfc{mesh**3}.dat").exists():
        return
    root=ET.parse(save/"data-file-schema.xml").getroot()
    kpoints=root.find("output/band_structure").findall("ks_energies")
    if len(kpoints)!=mesh**3:
        return
    upf=save / root.findtext("output/atomic_species/species/pseudo_file")
    density=save/"charge-density.dat"
    timing=next(line.strip() for line in output.splitlines() if re.search(r"PWSCF\s+:",line))
    return dict(family=family,series=series,element=element,mesh=mesh,kpoints=len(kpoints),
                input_sha256=digest(run/"nscf.in"),scf_density_sha256=digest(density),
                upf_sha256=digest(upf),xml_sha256=digest(save/"data-file-schema.xml"),
                wfc_files=len(list(save.glob("wfc*.dat"))),timing=timing)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("nc_work",type=Path)
    p.add_argument("paw_work",type=Path)
    p.add_argument("csv",type=Path)
    args=p.parse_args()
    rows=[]
    for family,series,path in (("NC","default",args.nc_work/"ws"),
                               ("NC","default",args.nc_work/"mpi/ws"),
                               ("NC","alternate_twist",args.nc_work/"alternate"),
                               ("NC","60_Ry",args.nc_work/"lower/ws"),
                               ("PAW-smooth","default",args.paw_work/"ws")):
        for sub in sorted(path.glob("*-*")):
            el,mesh=sub.name.split("-")
            row=collect(sub,family,series,el,int(mesh))
            if row:
                rows.append(row)
    order=lambda r:(r["series"],r["family"],r["element"],r["mesh"])
    assert len(set(map(order,rows)))==len(rows)
    with args.csv.open("w",newline="") as output:
        out=csv.DictWriter(output,rows[0].keys(),lineterminator="\n")
        out.writeheader()
        out.writerows(sorted(rows,key=order))
