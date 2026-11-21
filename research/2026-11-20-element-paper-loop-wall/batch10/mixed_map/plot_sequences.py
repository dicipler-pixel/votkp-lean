"""Plot the central archive ratios and quoted input boxes from opening_faces.csv."""
import csv
from fractions import Fraction
from itertools import groupby
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

folder = Path(__file__).resolve().parent
with (folder/"opening_faces.csv").open(newline="") as stream:
    rows = list(csv.DictReader(stream))
plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":9,
                     "svg.fonttype":"none","svg.hashsalt":"Beasley-20261121"})
wall = 3 + 2*np.sqrt(2)
colors = ["#1b617d","#893a42","#346b4c","#94531e","#674791","#3753a0"]
fig, axes = plt.subplots(3, 2, figsize=(10, 8.3), sharey=True)
fig.subplots_adjust(left=.08,right=.97,top=.86,bottom=.12,hspace=.65,wspace=.15)
for ax, (core, group), color in zip(axes.flat, groupby(rows,key=lambda r:r["core"]),colors,strict=True):
    data = list(group)
    Z = np.array([int(r["Z"]) for r in data])
    z = np.array([float(Fraction(r["exact_z"])) for r in data])
    low = np.array([float(r["z_low"]) for r in data])
    high = np.array([float(r["z_high"]) for r in data])
    ax.axhline(wall, color="#855a20", lw=1, ls=(0,(4,3)))
    ax.fill_between(Z,low,high,color=color,alpha=.22,edgecolor="none")
    ax.plot(Z,z,color=color,lw=1.1,marker=".",ms=3)
    ax.scatter(Z[z>wall],z[z>wall],facecolor="white",edgecolor=color,s=23,zorder=4)
    uncertain = (low <= wall) & (high >= wall)
    if uncertain.any():
        ax.errorbar(Z[uncertain],z[uncertain],
                    yerr=[z[uncertain]-low[uncertain],high[uncertain]-z[uncertain]],
                    fmt="D",ms=4,capsize=4,color="#942b45",lw=1.6,zorder=5)
    ax.set_ylim(.6,15.25); ax.set_yticks([1,4,6,10,14])
    ax.set_xlim(Z.min()-.9, Z.max()+.9)
    ax.spines[["top","right"]].set_visible(False)
    ax.spines[["bottom","left"]].set_color("#bac3c6")
    ax.grid(axis="y",lw=.4,color="#d8dede")
    ax.set_title(f"{core.capitalize()} core   ·   {data[0]['element']} to {data[-1]['element'].lower()}",loc="left",fontsize=10,fontweight="bold")
    ax.set_xlabel("Atomic number Z",fontsize=8)
    if ax.get_subplotspec().colspan.start==0: ax.set_ylabel("Opening ratio z")
fig.text(.08,.966,"Six noble-core opening sequences",ha="left",fontsize=20,fontweight="bold")
fig.text(.08,.923,"433 archived internal peel ratios. Dashed line: equal-face wall at 3 + 2√2.",ha="left",fontsize=11)
fig.text(.08,.059,"Open circles exceed the wall. Shading propagates the two quoted energy uncertainties. The diamond marks francium's straddling interval.",fontsize=8.5)
fig.text(.08,.031,"Lines connect adjacent available atomic numbers; each panel ends with its last available threshold pair. Jeromie Beasley’s VOTKP element atlas.",fontsize=8.5)
fig.savefig(folder/"six_core_sequences.svg",metadata={"Date":None,"Title":"Six noble-core opening sequences"})
out = folder/"six_core_sequences.svg"
out.write_text("\n".join(line.rstrip() for line in out.read_text().splitlines())+"\n")
