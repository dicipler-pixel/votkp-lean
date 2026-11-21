"""Two views of the eight straight covalent bonds of the beta-cyclooctaselenium CIF."""
from hashlib import sha256
from pathlib import Path
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

root = Path(__file__).resolve().parent
raw = (root/"COD_2204812.cif").read_bytes()
assert sha256(raw).hexdigest() == "ac27d99b1c3c9e1d9997917fa41086702ed451ea2e80392132ae3b75dd31eb89"
source = raw.decode().splitlines()
def number(value):
    return float(value.split("(")[0])
site = {}
cell = {}
edges = set()
for line in source:
    fields = line.split()
    if len(fields)==9 and fields[5]=="Uani":
        site[int(fields[0][2:])] = [number(coord) for coord in fields[1:4]]
    if fields and fields[0].startswith(("_cell_length_", "_cell_angle_")):
        cell[fields[0].removeprefix("_cell_")] = number(fields[1])
    if re.fullmatch(r"Se[1-8] Se[1-8] \d+\.\d+\(\d+\)", line):
        edges.add(tuple(sorted(int(f[2:]) for f in fields[:2])))
assert edges == {tuple(sorted((i, i%8+1))) for i in range(1,9)}
frac = np.array([site[i] for i in range(1,9)])
beta = np.deg2rad(cell["angle_beta"])
a,b,c = [cell["length_"+k] for k in "abc"]
assert cell["angle_alpha"]==cell["angle_gamma"]==90
xyz = frac @ np.array([[a,0,0], [0,b,0], [c*np.cos(beta),0,c*np.sin(beta)]])
xyz -= xyz.mean(axis=0)
plt.rcParams.update({"font.family":"DejaVu Sans","svg.fonttype":"none","svg.hashsalt":"Se8-2204812"})
fig = plt.figure(figsize=(9.2,4.8))
fig.subplots_adjust(left=.055,right=.94,top=.83,bottom=.17,wspace=.25)
left=fig.add_subplot(121,projection="3d")
right=fig.add_subplot(122)
left.set_title("Measured ring in three dimensions",fontsize=12,loc="left",y=.98)
left.set_proj_type("ortho");left.view_init(elev=9,azim=68)
left.set_box_aspect([1,1,1])
left.set_axis_off()
for i,j in edges:
    left.plot(*xyz[[i-1,j-1]].T,color="#3c5967",lw=3,zorder=1)
left.scatter(*xyz.T,c="#ba573a",edgecolors="white",s=90,depthshade=False)
lo,hi=xyz.min(),xyz.max()
for limit in (left.set_xlim,left.set_ylim,left.set_zlim):limit(lo,hi)
right.set_title("Projection along the crystal’s a axis",fontsize=12,loc="left")
points=frac[:,1:]
right.fill(*points.T,color="#b9d9d8",alpha=.6)
right.plot(*np.vstack((points,points[0])).T,color="#3a6870",lw=2)
right.scatter(*points.T,s=48,c="#ba573a",edgecolors="white",zorder=3)
centre=points.mean(axis=0)
for i,point in enumerate(points,1):
    vector=point-centre;vector/=np.linalg.norm(vector)
    right.annotate(str(i),point,xytext=vector*11,textcoords="offset points",ha="center",va="center",fontsize=9)
right.set(xlabel="Fractional b coordinate",ylabel="Fractional c coordinate")
right.set_aspect("equal");right.margins(.17)
right.spines[["right","top"]].set_visible(False)
fig.text(.055,.94,"A closed eight-atom path in elemental selenium",fontsize=17,fontweight="bold")
fig.text(.055,.055,"β-monoclinic cyclooctaselenium at 150(2) K. COD 2204812. Points mark refined atom centres; lines use the eight published bonds.",fontsize=8.5)
out=root/"selenium_ring.svg"
fig.savefig(out,metadata={"Date":None,"Title":"The closed beta-cyclooctaselenium polygon"})
out.write_text("\n".join(line.rstrip() for line in out.read_text().splitlines())+"\n")
