from pathlib import Path
import re,json,hashlib
import sympy as s
import fitz
from lxml import html
root=Path(__file__).resolve().parent
t,p=s.symbols('theta phi',real=True);I=s.I
sig=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.Matrix([[1,0],[0,-1]])]
n=s.Matrix([s.sin(t)*s.cos(p),s.sin(t)*s.sin(p),s.cos(t)])
H=sum((n[i]*sig[i] for i in range(3)),s.zeros(2));P=(s.eye(2)-H)/2
reduce=lambda a:a.applyfunc(lambda e:s.simplify(s.trigsimp(s.expand_complex(e)))) if isinstance(a,s.MatrixBase) else s.simplify(s.trigsimp(s.expand_complex(a)))
checks={}
checks['unit_direction']=reduce(n.dot(n)-1)==0
checks['projector_idempotence_on_sphere']=reduce(P*P-P)==s.zeros(2)
curv=reduce(I*s.trace(P*(P.diff(t)*P.diff(p)-P.diff(p)*P.diff(t))))
checks['written_Berry_curvature_derivation']=reduce(curv-s.sin(t)/2)==0
uN=s.Matrix([-s.exp(-I*p)*s.sin(t/2),s.cos(t/2)])
uS=s.Matrix([-s.sin(t/2),s.exp(I*p)*s.cos(t/2)])
checks['north_lower_eigenvector']=reduce(H*uN+uN)==s.zeros(2,1)
checks['south_transition_phase']=reduce(uS-s.exp(I*p)*uN)==s.zeros(2,1)
checks['north_connection']=reduce(I*(uN.conjugate().T*uN.diff(p))[0]-(1-s.cos(t))/2)==0
checks['south_connection']=reduce(I*(uS.conjugate().T*uS.diff(p))[0]+(1+s.cos(t))/2)==0
checks['curvature_flux']=s.simplify(s.integrate(s.sin(t)/2,(t,0,s.pi))*2*s.pi)==2*s.pi
D=html.fromstring((root/'Geometric_Flux_and_Magnetic_Charge_v1.html').read_text())
ids=set(D.xpath('//@id'));bad=[a.get('href') for a in D.xpath('//a[starts-with(@href,"#")]') if a.get('href')[1:] not in ids]
checks['html_internal_links']=not bad
# Prevent silent omissions of Lean theorem names in the web rendering.
leanroot=root/'monopole_stance' if (root/'monopole_stance').is_dir() else root.parent/'monopole_stance'
report=json.loads((leanroot/'verification/verification.json').read_text())
checks['all_24_Lean_names_in_HTML']=all(name in D.text_content() for name in report['theorems'])
checks['embedded_figure']=len(D.xpath('//img[starts-with(@src,"data:image/")]'))==1
pdf=fitz.open(root/'Geometric_Flux_and_Magnetic_Charge_v1.pdf')
text='\n'.join(p.get_text() for p in pdf)
checks['pdf_references_resolved']='??' not in text
checks['pdf_11_pages']=len(pdf)==11
checks['no_overfull_boxes']='Overfull' not in (root/'Geometric_Flux_and_Magnetic_Charge_v1.log').read_text()
checks['all_24_Lean_names_in_PDF']=all(name in text for name in report['theorems'])
res={'checks':checks,'failed_internal_links':bad,'symbolic_checks_scope':'Additional exact symbolic checks of written derivations; not Lean formalization.','pdf_pages':len(pdf),'proof_theorems':report['theorem_count']}
(root/'paper_validation.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2));assert all(checks.values())
