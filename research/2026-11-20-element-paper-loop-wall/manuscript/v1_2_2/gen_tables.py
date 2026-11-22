# SCRIPT: GEN_TABLES_WHAT_THE_PEEL_KEEPS_V1_2
import json, math, gzip
B='/home/claude/votkp-lean/'
R=json.load(gzip.open(B+'data/element_thresholds_20261011.json.gz'))['records']
rec={r['Z']:r for r in R}
E=json.load(open(B+'research/2026-11-20-element-paper-loop-wall/ptable/ptable_data.json'))['elements']
W=3+2*math.sqrt(2); HA=27.211386245988
g=lambda z:(z-1)/(z+1)
ies=lambda Z:[t['IE_eV'] for t in rec[Z]['thresholds']]
EA={e['Z']:e['anion']['EA'] for e in E if e['anion'] and e['anion'].get('EA')}
EA[21]=0.179378
est={66:0.015,69:0.032}
po=11905.631*6.62607015e-34*299792458*100/1.602176634e-19
def cell(z):
    s=f"{z:.4f} ({g(z):.4f})"; return f"**{s}**" if z>W else s
cores=[2,10,18,36,54]
rows=["| Z | Element | First IE (eV) | anion rung | K opening (helium core) | L opening (neon core) | argon-core opening | krypton-core opening | xenon-core opening |","|---|---|---|---|---|---|---|---|---|"]
for e in E:
    Z=e['Z']; ie=ies(Z)
    if Z in EA: a=cell(ie[0]/EA[Z])
    elif Z in est: a=cell(ie[0]/est[Z])+' estimate'
    elif Z==84: a=cell(ie[0]/po)+' preliminary'
    else: a='none'
    cs=[]
    for N in cores:
        if N<Z: q=Z-N-1; cs.append(cell(ie[q+1]/ie[q]))
        else: cs.append('—')
    rows.append(f"| {Z} | {e['name']} | {ie[0]:g} | {a} | "+" | ".join(cs)+" |")
open('/home/claude/paper_v12/build/gen/table_openings.md','w').write("\n".join(rows)+"\n")
rows=["| Z | Element | $S$ | $\\sigma$ | $S-\\sigma$ |","|---|---|---|---|---|"]
for e in E:
    Z=e['Z']; ie=ies(Z)
    if Z<2 or len(ie)<Z: continue
    H=ie[-1]/HA; Bb=ie[-2]/HA; S=(H-Bb)/Z; sg=Z-math.sqrt(2*Bb)
    rows.append(f"| {Z} | {e['name']} | {S:.5f} | {sg:.5f} | {S-sg:+.5f} |")
open('/home/claude/paper_v12/build/gen/table_screening.md','w').write("\n".join(rows)+"\n")
L=[]
for e in E:
    Z=e['Z']
    if Z in EA: z=ies(Z)[0]/EA[Z]; G=g(z); L.append((e['name'],EA[Z],z,G,1/(2*G*G)))
L.sort(key=lambda x:x[2])
rows=["| Element | EA (eV) | IE/EA | $\\eta/\\chi=\\Gamma_0$ | $\\omega/\\eta$ | side |","|---|---|---|---|---|---|"]
for n,ea,z,G,oe in L: rows.append(f"| {n} | {ea:.6g} | {z:.4f} | {G:.5f} | {oe:.4f} | {'outside' if z>W else 'inside'} |")
open('/home/claude/paper_v12/build/gen/table_chemistry.md','w').write("\n".join(rows)+"\n")
print(len(L),sum(1 for x in L if x[2]>W))
