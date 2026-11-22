"""Derive a new offline edition from Claude's hash-verified public standalone HTML and the public H-At ledger."""
import csv,hashlib,json,sys
from html import escape
from pathlib import Path
from urllib.parse import urlparse
source,ledger=map(Path,sys.argv[1:3])
root=Path(__file__).resolve().parent
base="https://github.com/dicipler-pixel/votkp-lean/blob/"
folder="/research/2026-11-20-element-paper-loop-wall/"
v1="3fad6267f5f980f6378371d0c02b95c9a71d00e1"
review=base+"a9fe1152aaed6636c2db5a94834198c1e3904fdc"+folder+"russell/prediction_review_20261121/CODEX_RESPONSE_v1.md"
ts=base+"26b2875d04c63e26e90b08d656996bec1c4c5532"+folder+"russell/prediction_review_20261121/H_to_At_thresholds.csv"
src=base+v1+folder+"ptable/Periodic_Table_of_Elemental_Peels_v1_20261121_standalone.html"
man=base+"dfff861bfa5bd004d3d36cce01353004cc5b3eed"+folder+"manuscript/What_the_Peel_Keeps_v1.pdf"
s=source.read_text()
assert hashlib.sha256(source.read_bytes()).hexdigest()=="e954f69e30f8c545cda6ef68c55e04abd3b2746fca1cdf09ef62574ee46e976b"
assert hashlib.sha256(ledger.read_bytes()).hexdigest()=="9f7b21e9eba6f76d0cbfa4ffcae65eeac7bf43cd6289bf3205432799ba8c3803"
def replace(a,b):
 global s
 if s.count(a)!=1:raise ValueError(a[:120])
 s=s.replace(a,b)
def card(title,grade,newtitle,prose):
 global s
 lines=s.splitlines(keepends=True)
 for i,l in enumerate(lines):
  if f",'{title}'," in l:
   tail="]];\n" if l.endswith("]];\n") else "],\n"
   lines[i]="   ["+",".join(json.dumps(x,ensure_ascii=False) for x in (grade,newtitle,prose))+tail
   s=''.join(lines)
   return
 raise ValueError(title)
rows={r['symbol']:r for r in csv.DictReader(ledger.open()) if r['k']=='0'}
embedded=json.JSONDecoder().raw_decode(s.split('setTimeout(()=>{const d=',1)[1])[0]
assert sum(x['anion'] is not None for x in embedded['elements'])==65
gloss={'no bound ground-state anion in adopted ledger':'No bound ground-state anion in the adopted ledger.','theory-only':'Theory-only affinity. This edition scores no numeric rung.','measured-lower-bound':'Measured lower bound for the affinity. A central rung remains unscored.','evaluated-AMS-estimate':'Accelerator mass spectrometry (AMS) estimate.','evaluated-AMS-estimate-disputed':'Disputed accelerator mass spectrometry (AMS) estimate.','experimental-upper-limit-no-established-bound-anion':'Experimental upper limit. A bound ground-state anion has yet to be established.','evaluated-no-stable-ground-anion':'Evaluation finds no stable ground-state anion.','no established bound ground anion':'A bound ground-state anion has yet to be established.','observed-preliminary-systematics-outstanding':'Preliminary affinity observation suggests an inside rung. Its systematic uncertainty is outstanding and the rung is unscored.'}
notes={}
for e in embedded['elements']:
 if e['anion']:continue
 sym=e['sym'];r=rows[sym];note=gloss[r['grade_or_status']]
 if r['energy_eV']:
  assert sym in ('Dy','Tm')
  note+=f" Working-paper EA {float(r['energy_eV']):.3f} ± {float(r['uncertainty_eV']):.3f} eV; z₀ = {float(r['z']):.4f}, outside. Excluded from the v1 baseline."
 url=r['reference_or_source'];assert urlparse(url).scheme=='https'
 notes[sym]=escape(note)+' <a href="'+escape(url,quote=True)+'" target="_blank" rel="noopener">Source</a>.'
assert len(notes)==20
replace('Periodic Table of Elemental Peels — Jeromie Beasley','Periodic Table of Elemental Peels — Codex review v1.1 · Jeromie Beasley')
replace('Jeromie Beasley · hydrogen to astatine · every number from the pinned ionisation archive',
 'Jeromie Beasley · hydrogen to astatine · Codex review v1.1 of <a href="'+src+'">Claude’s standalone v1</a>')
replace('no anion / no core','unscored anion rung / no named core')
replace('Seven of the nine possible addresses occur.','Seven addresses occur in the plotted v1 baseline. An unscored affinity can mean an unbound state, an unresolved observation, or an estimate excluded from that baseline; each drawer gives its evidence status.')
replace('Only eight steps lie outside it.','Eight ordinary removal steps and 53 of the 65 baseline anion rungs lie outside it.')
replace('The wall is the line χ = √2·η, where ω = η and the ideal uptake ΔN = χ/η = 1/Γ₀ is exactly √2 electrons. Above the line the stone wins (53 of 65); below it the pull wins (12).','On the wall, χ/η = 1/Γ₀ = √2 and ω = η. This dimensionless descriptor uses half-hardness. The quadratic E(x) = E₀ − χx + ηx² matching the two threshold energies has its formal minimum at x = χ/(2η), or 1/√2 on the wall. Actual charge uptake requires a reservoir and a measured response. Above the plotted line are 53 of 65 baseline anion rungs; 12 lie below.')
replace('The turn inward falls between his 3− and 2− tones, one tone after his apex.','The P→S, As→Se and Sb→Te rows turn inward from 3− to 2−. Oxygen stays outside at 2− and fluorine turns inside at 1−. Bismuth (3−) is outside and astatine (1−) is inside; polonium (2−) has a preliminary inside reading and no scored v1 point.')
replace('The same wall in the visible:','The optical comparison uses the same numerical half-power threshold:')
replace("'Core opening outside, no bound anion'","'Core opening outside, unscored anion rung'")
replace("'No bound anion, core opening inside','Noble gases past helium, nitrogen, the alkaline earths past beryllium and others with no stable anion.'","'Unscored anion rung, core opening inside','This class includes several evidence statuses. Calcium, strontium and barium have numerical bound-anion rungs and belong to the outside-anion class.'")
replace("e.sym+' (no anion)'","e.sym+' (unscored)'")
replace('uptake √2 electrons','χ/η = √2')
replace('uptake 1/Γ₀ =','descriptor 1/Γ₀ =')
replace('bright core of each link = E⁻ inside the outline E⁺; gold ring on each link at Γ² = ½','true link area fraction Γ² = E⁻/E⁺; drawing radius has a visibility floor of 0.03 of the outline. Gold ring at Γ² = ½')
replace('ideal uptake 1/Γ₀','half-hardness descriptor χ/η = 1/Γ₀')
replace(' electrons (wall: √2 = 1.4142)',' (dimensionless; wall: √2)')
replace(":'no bound anion in the table'",":anionNote[e.sym]")
replace("const gam=z=>","const anionNote="+json.dumps(notes,ensure_ascii=False).replace('<','\\u003c')+";\nconst gam=z=>")
card('Connection energy on every link','EXACT · display convention','Connection energy on every link','E⁻/E⁺ = Γ² uses the exact squared difference and sum of the two energies. The drawn radius is max(|Γ|, 0.03) of the outline. This visibility floor enlarges 1,562 of 3,570 ordinary links; the ladder lists the computed Γ².')
card('Stone and wanting','EXACT · descriptor','Stone and wanting','At the anion rung Γ₀ = η/χ for the specified half-hardness. The descriptor χ/η equals √2 at the wall. The threshold-matched quadratic has formal minimizing x = 1/(2Γ₀).')
card('The data pin the wall to 1%','DERIVED · archive scan','Cutoffs giving the same labels','The forward classifications leave an interval from silver (inside, lower endpoint included) to silicon (outside, upper endpoint excluded), approximately [5.80790, 5.86654). The archive scan locates the extrema. The Lean declaration window_silver_silicon checks the encoded endpoint sides.')
card('Only the wall gives a consistent two-face rule','EXACT · specified pair of rules','Two ways to extend a single-face cutoff','The shifted sum of squared reflections and the shifted product of hyperbolic sines agree on the boundary for all input pairs only at the geometric cutoff within the interior domain. Other choices of how to mix faces remain possible. See the BoundaryAgreement.lean proof in the shared review.')
card('Francium','PREDICTION · open','Francium','For ²¹²Fr IE₁ = 4.0727411(11) eV; the geometric wall is near IE₂ = 23.738 eV. NIST lists semiempirical [22.4] ± 1.9 eV. A direct ground-channel measurement remains open. The frozen two-prior-period secant forecast gives 21.8344 eV, inside. It missed all three analogous earlier side calls. Against the raw Ag–Si midpoint an interval strictly inside 23.73769–23.77348 eV would separate the labels even with the quoted IE₁ width.')
replace("MEASURED · 8 of 3,570","DERIVED · 8 of 3,570")
replace("MEASURED: computed from the archive.","DERIVED: computed from archive inputs, which carry individual experimental or theoretical grades.")
replace('const A=[[','const A=[["Which affinity ledger is plotted?",'+json.dumps('All nine views retain Claude’s v1 baseline: 53 outside of 65 numerical affinities. The working paper also adopts Dy 0.015(3) eV and disputed Tm 0.032(7) eV as AMS estimates. Both are outside, giving 55/67. Sm has a lower bound and Po has a preliminary observation; neither adds a scored central rung. '+f'<a href="{review}">Reconciliation</a> · <a href="{ts}">Extended CSV</a> · <a href="{man}">Working paper</a>.',ensure_ascii=False)+'],[')
replace('element paper\\\'s committed table (65 bound anions)','v1 mixer ledger (65 scored numerical affinity rungs)')
replace("const LEAN_BASE='https://github.com/dicipler-pixel/votkp-lean/blob/element-paper/loop-wall/';",f"const LEAN_BASE='{base}{v1}/';")
supplement=base+"895cb6e19386c5e40d23724ee82ec5c50d0e762b"+folder+"russell/prediction_review_20261121/addendum/Where_the_Peel_Wall_Can_Be_Tested_v1.pdf"
oxygen=base+"bdd1c2fd77a3c741bb522f91cbbab85201e4b39c"+folder+"russell/prediction_review_20261121/oxygen_design/Oxygen_Identifiability.md"
replace("</header>",'<p class="by"><a href="'+man+'">39-page manuscript</a> · <a href="'+supplement+'">Six-page research addendum</a> · <a href="'+oxygen+'">State-resolved oxygen comparison</a> (separate from the ground-state counts)</p>\n</header>')
(root/'Periodic_Table_of_Elemental_Peels_Codex_review_v1_1.html').write_text(s)
