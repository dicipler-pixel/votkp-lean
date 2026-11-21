"""Draw the perpendicular disk geodesics from the pinned removal energies."""
from argparse import ArgumentParser
from decimal import Decimal
import gzip
import json
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt

def reflect(r):
    return (r-1)/(r+1)

def draw_face(ax, ratio, horizontal, color):
    gamma = reflect(ratio)
    centre = 1/gamma
    radius = np.sqrt(centre**2-1)
    delta = np.arccos(radius/centre)
    angle = np.linspace(np.pi-delta, np.pi+delta, 601)
    x, y = centre+radius*np.cos(angle), radius*np.sin(angle)
    ax.plot(x if horizontal else y, y if horizontal else x, color=color, lw=2)

def main(archive, output):
    with gzip.open(archive, "rt") as stream:
        records = json.load(stream, parse_float=Decimal)["records"]
    names = {}
    for Z, core in [(6, 2), (7, 2), (37, 36), (38, 36)]:
        record = records[Z-1]
        k = Z-core
        thresholds = record["thresholds"]
        names[record["symbol"]] = float(thresholds[k]["IE_eV"]/thresholds[k-1]["IE_eV"])
    fig, axes = plt.subplots(2, 3, figsize=(10, 7))
    for ax, (a, b) in zip(axes.flat, [("C","C"),("C","N"),("N","N"),("Rb","Rb"),("Rb","Sr"),("Sr","Sr")]):
        ax.add_patch(plt.Circle((0,0),1,facecolor="#f4f7f8",edgecolor="#45616b",lw=1))
        labels = {"C":"Carbon","N":"Nitrogen","Rb":"Rubidium","Sr":"Strontium"}
        u, v = names[a], names[b]
        draw_face(ax,u,True,"#056b73")
        draw_face(ax,v,False,"#ad4c24")
        x, y = reflect(u), reflect(v)
        m = x*x+y*y-1
        if m < 0:
            scale = 1+np.sqrt(-m)
            ax.scatter(x/scale,y/scale,color="#18272c",s=22,zorder=4)
        ax.set(xlim=(-1.04,1.04),ylim=(-1.04,1.04),aspect="equal")
        ax.set_axis_off()
        ax.set_title(f"{labels[a]} × {labels[b]}    {'open' if m>0 else 'closes'}\nmargin  {m:+.6f}",fontsize=11)
    fig.suptitle("Two core-opening ratios on perpendicular disk faces",fontsize=16)
    fig.text(.5,.045,"Top: helium-core openings      Bottom: krypton-core openings\n"
             "Teal and copper arcs are geodesics. A dot marks their finite intersection. Margin = Γ₁² + Γ₂² − 1.",
             ha="center",fontsize=10)
    fig.subplots_adjust(top=.84,bottom=.14,hspace=.36)
    mpl.rcParams["svg.hashsalt"] = "Beasley-mixed-faces"
    fig.savefig(output,format="svg",metadata={"Date":None},bbox_inches="tight")
    plt.close(fig)

if __name__ == "__main__":
    cmd=ArgumentParser(description=__doc__)
    cmd.add_argument("archive",type=Path)
    cmd.add_argument("output",type=Path)
    a=cmd.parse_args()
    main(a.archive,a.output)
