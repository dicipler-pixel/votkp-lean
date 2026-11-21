# SCRIPT: VOTKP-OPENING-MAP-01
# From Jeromie's archive (data/element_thresholds_20261011.json.gz): for each noble-gas core with N
# electrons, follow the isoelectronic sequence. For element Z, the ion with N+1 electrons has charge
# q = Z-N-1; the opening ratio is IE(q+1)/IE(q) (last removal above the core, then first removal from
# the core). Report counts, first eligible element, first inside, and anything outside after that.
import gzip, json, math, sys
d=json.load(gzip.open(sys.argv[1]))
rec={r['Z']:r for r in d['records']}
w=3+2*math.sqrt(2)
out={}
for N,name in [(2,'He'),(10,'Ne'),(18,'Ar'),(36,'Kr'),(54,'Xe'),(86,'Rn')]:
    rows=[]
    for Z in range(N+1,119):
        th={t['q']:t for t in rec[Z]['thresholds']}
        q=Z-N-1
        if q in th and q+1 in th:
            a,b=th[q],th[q+1]; z=b['IE_eV']/a['IE_eV']
            rows.append((Z,rec[Z]['symbol'],a['IE_eV'],b['IE_eV'],a['unc_eV'],b['unc_eV'],a['grade'],b['grade'],z))
    outs=[r for r in rows if r[-1]>w]
    print(f'{name}-like core N={N}: {len(rows)} ratios; first {rows[0][1]} z={rows[0][-1]:.4f}; outside: '+', '.join(f'{r[1]} {r[-1]:.4f}' for r in outs))
    out[name]=rows
json.dump(out,open('opening_map_rows.json','w'))
fr=[r for r in out['Rn'] if r[1]=='Fr'][0]
lo=(fr[3]-fr[5])/(fr[2]+fr[4]); hi=(fr[3]+fr[5])/(fr[2]-fr[4])
print('Fr',fr[2],fr[3],fr[4],fr[5],fr[6],fr[7],'range',round(lo,4),round(hi,4),'wall',round(w,4))
