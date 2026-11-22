"""Recheck the data inside the v1 standalone page against both committed snapshots."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
checkout=Path(sys.argv[1])
base="research/2026-11-20-element-paper-loop-wall/ptable/"
pin="3fad6267f5f980f6378371d0c02b95c9a71d00e1"
original="6068b3f634817f4a9b864351466388726233a49e"
def git_file(revision, name):
    return subprocess.check_output(["git","show",f"{revision}:{base}{name}"],cwd=checkout)
html=git_file(pin,"Periodic_Table_of_Elemental_Peels_v1_20261121_standalone.html")
print("standalone sha256",hashlib.sha256(html).hexdigest())
body=html.decode().split("setTimeout(()=>{const d=",1)[1]
embedded,_=json.JSONDecoder().raw_decode(body)
for revision in (original,pin):
    assert embedded==json.loads(git_file(revision,"ptable_data.json"))
    print("Embedded JSON agrees with",revision)
steps=[s for e in embedded["elements"] for s in e["steps"]]
clamped=sum(s["g2"]<.03**2 for s in steps)
assert clamped==1562 and len(steps)==3570
print("Links receiving the display radius floor",clamped,"of",len(steps))
