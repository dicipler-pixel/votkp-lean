# SCRIPT: GEN_TABLES_WHAT_THE_PEEL_KEEPS_V1_2
import json, math
E=json.load(open('/home/claude/votkp-lean/research/2026-11-20-element-paper-loop-wall/ptable/ptable_data.json'))['elements']
W=3+2*math.sqrt(2); HA=27.211386245988
g=lambda z:(z-1)/(z+1)
NOB={'H':'no bound ground-state anion'}
def cell(z):
    if z is None: return '—'
    s=f"{z:.4f} ({g(z):.4f})"
    return f"**{s}**" if g(z)**2>0.5 else s
cores=['helium','neon','argon','krypton','xenon']
rows=["| Z | Element | anion rung | K opening (helium core) | L opening (neon core) | argon-core opening | krypton-core opening | xenon-core opening |","|---|---|---|---|---|---|---|---|"]
for e in E:
    an=e['anion']; a=cell(an['z0']) if an and an.get('z0') else 'none'
    cz={c['core']:c['z'] for c in e['cores']}
    rows.append(f"| {e['Z']} | {e['name']} | {a} | "+" | ".join(cell(cz.get(c)) for c in cores)+" |")
open('/home/claude/paper_v12/build/gen/table_openings.md','w').write("\n".join(rows)+"\n")
# screening table
rows=["| Z | Element | $S$ | $\\sigma$ | $S-\\sigma$ |","|---|---|---|---|---|"]
for e in E:
    Z=e['Z']
    if Z<2 or len(e['ie'])<Z: continue
    H=e['ie'][-1]/HA; B=e['ie'][-2]/HA
    S=(H-B)/Z; sg=Z-math.sqrt(2*B)
    rows.append(f"| {Z} | {e['name']} | {S:.5f} | {sg:.5f} | {S-sg:+.5f} |")
open('/home/claude/paper_v12/build/gen/table_screening.md','w').write("\n".join(rows)+"\n")
# chemistry table
L=[]
for e in E:
    an=e['anion']
    if an and an.get('z0'):
        z=an['z0']; G=g(z); L.append((e['name'],an['EA'],z,G,1/(2*G*G)))
L.sort(key=lambda x:x[2])
rows=["| Element | EA (eV) | IE/EA | $\\eta/\\chi=\\Gamma_0$ | $\\omega/\\eta$ | side |","|---|---|---|---|---|---|"]
for n,ea,z,G,oe in L:
    rows.append(f"| {n} | {ea:.6g} | {z:.4f} | {G:.5f} | {oe:.4f} | {'outside' if G*G>0.5 else 'inside'} |")
open('/home/claude/paper_v12/build/gen/table_chemistry.md','w').write("\n".join(rows)+"\n")
print(len(L), sum(1 for x in L if x[3]**2>0.5))
for e in E[:3]+[E[12],E[13]]:
    Z=e['Z']; 
    if Z>=2: H=e['ie'][-1]/HA; B=e['ie'][-2]/HA; print(e['sym'],round((H-B)/Z,5),round(Z-math.sqrt(2*B),5))
