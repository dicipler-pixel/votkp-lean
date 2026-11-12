from fractions import Fraction as Q
import json,pathlib,hashlib
p=pathlib.Path(__file__).resolve().parents[1]
r=json.load(open(p/'source/messages.json'));a=json.load(open(p/'source/stream.json'));eq=json.load(open(p/'source/math_index.json'))
assert len(r)==282
for e in eq:assert r[e['message']-1]['text'][e['start']:e['end']]==e['original']
assert [x['number'] for x in r if 'heegner' in x['text'].lower()]==[263]
assert 12-2-6+20==24
assert Q(1)-Q(1,2)**2==Q(3,4)
assert Q(3,2)*Q(1,2)==Q(3,4)
for n,m,k in [(1,2,3),(2,3,1),(0,0,0)]:assert 3**n*6**m*9**k==2**m*3**(n+m+2*k)
# Exact zero-set regularization: f=x, tangent y, Hessian diag(2/epsilon,0).
epsilon=Q(1,7);assert 0*(2/epsilon)+1*0==0
# Two energy levels: at q=exp(-t), -Theta'/Theta=(2q^2+5q^5)/(q^2+q^5).
q=Q(1,1000);ratio=(2*q**2+5*q**5)/(q**2+q**5);assert abs(ratio-2)<Q(1,10**8)
# Shift is not an additive group homomorphism.
s=3;assert 0+s!=0
print(json.dumps({'status':'PASS','entries':len(r),'formula_substrings_verified':len(eq),'heegner_messages':[263],'scope':'Source-extraction integrity and selected exact algebra; not certification of all historical theorems.'},indent=2))
