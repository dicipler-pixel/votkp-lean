from fractions import Fraction as F
import contextlib,io,re,importlib.util,json
from pathlib import Path
p=Path(__file__).parent
spec=importlib.util.spec_from_file_location('diagram',p/'theta_diagram.py'); m=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(m)
raw=(p/'author_table_entry_7_1.txt').read_text().replace('\n',' ')
numer=raw[raw.index('(3-3 S')+1:raw.rindex(')')]
terms=re.findall(r'[+-]?[^+-]+',numer)
def tab(s,t,corrupt=False):
 total=F(0)
 for term in terms:
  term=term.strip(); sign=-1 if term.startswith('-') else 1; term=term.lstrip('+-').strip()
  c=re.match(r'\d+',term); a=re.search(r'S(?:\^(\d+))?',term); b=re.search(r'T(?:\^(\d+))?',term)
  total+=sign*(int(c.group()) if c else 1)*s**(int(a.group(1) or 1) if a else 0)*t**(int(b.group(1) or 1) if b else 0)
 if corrupt:total+=1
 return -total/(s**6*t**6)
def delta(t,X,rot):
 p=-(sum(rot)+sum(s for s,i,j in X))
 assert p%2==0
 return t**(p//2)*m.det(m.mat(t,X,len(rot)))
def join(X,R,Y,S):
 n=len(R); return X+[(s,i+n-1,j+n-1) for s,i,j in Y],R[:-1]+[R[-1]+S[0]]+S[1:]
Y=[(1,2*k,(2*k+7)%14) for k in range(7)];R=[0]*15;R[7]=-1;N=m.conj(Y)
for a,b in [(F(5,2),F(7,3)),(F(7,4),F(5,3))]:
 k,_=m.calc(Y,R,a,b); mk,_=m.calc(N,R,a,b); source=tab(a,b)
 P,Rp=join(Y,R,Y,R); Q,Rq=join(Y,R,N,R)
 kk,_=m.calc(P,Rp,a,b); km,_=m.calc(Q,Rq,a,b)
 f=delta(a,Y,R)*delta(b,Y,R)*delta(a*b,Y,R)
 print(json.dumps(dict(a=str(a),b=str(b),theta_7=str(k),theta_mirror=str(mk),author_table=str(source),candidate_is_negative_table=k==-source,mirror_is_table=mk==source,direct_sum_kk=str(kk),composed_formula_kk=str(2*k*f),kk_sum_agreement=kk==2*k*f,direct_sum_kmirror=str(km),kbar_formula_agreement=km==(k+mk)*f,kbar_zero=km==0,corrupt_table_rejected=(tab(a,b,True)!=source))))
