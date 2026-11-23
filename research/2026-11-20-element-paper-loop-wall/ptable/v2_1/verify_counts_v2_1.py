# SCRIPT: PTABLE-V2-INDEPENDENT-COUNTS
# Recomputes every count shown on the v2 page straight from the archive and the v1 affinity/optics
# data, without using ptable_v2_data.json or the builder, then reads the same counts from the page data.
import json, gzip, math, re
B='/home/claude/votkp-lean/'; R=B+'research/2026-11-20-element-paper-loop-wall/'
W=3+2*math.sqrt(2)
rec={r['Z']:r for r in json.load(gzip.open(B+'data/element_thresholds_20261011.json.gz'))['records']}
steps=lambda Zs:[(Z,t1['IE_eV']/t0['IE_eV']) for Z in Zs for t0,t1 in zip(rec[Z]['thresholds'],rec[Z]['thresholds'][1:]) if t1['q']==t0['q']+1]
a=steps(range(1,86)); h=steps(range(86,119))
print('H-At steps',len(a),'outside',sum(z>W for _,z in a),'| expected 3570 / 8')
print('Rn-Ds steps',len(h),'outside',sum(z>W for _,z in h),'| total',len(a)+len(h),'expected 5714')
v1=json.load(open(R+'ptable/ptable_data.json'))['elements']
ea=[(e['ie'][0]/e['anion']['EA']) for e in v1 if e['anion']]
print('anion rungs',len(ea),'outside',sum(z>W for z in ea),'| expected 65 / 53')
op=[e['optic'] for e in v1 if e['optic']]
print('metals above 1/2',sum(o['metal'] and o['mean_R']>.5 for o in op),'of',sum(o['metal'] for o in op),'; non-metals above',sum((not o['metal']) and o['mean_R']>.5 for o in op),'of',sum(not o['metal'] for o in op))
ins=[z for z in ea+[z for _,z in a] if z<=W]; outs=[z for z in ea+[z for _,z in a] if z>W]
print('window [%.6f, %.6f)'%(max(ins),min(outs)))
fr=rec[87]['thresholds']; print('Fr radon-core z = %.4f'%(fr[1]['IE_eV']/fr[0]['IE_eV']), fr[1]['grade'])
# compare with page data
s=open('Periodic_Table_of_Elemental_Peels_v2_1_Jeromie_Beasley.html').read()
i=s.index('const d={"wall"'); d,_=json.JSONDecoder().raw_decode(s[i+8:])
E=d['elements']; L=[e for e in E if not e['heavy']]; Hh=[e for e in E if e['heavy']]
print('page:',sum(len(e['steps']) for e in L),sum(e['outside'] for e in L),sum(len(e['steps']) for e in Hh),sum(e['outside'] for e in Hh),sum(1 for e in L if e['anion']),sum(1 for e in L if e['anion'] and e['anion']['out']))
print('page tiles', len(E), 'Z range', E[0]['Z'], max(e['Z'] for e in E))
print('byline check:', re.findall(r'class="by">([^<]*)',s)[:1], '| other names in visible text:', [n for n in ['Codex','Claude','Elizabeth','EJ '] if n in re.sub(r'<script.*?</script>','',s,flags=re.S)])
