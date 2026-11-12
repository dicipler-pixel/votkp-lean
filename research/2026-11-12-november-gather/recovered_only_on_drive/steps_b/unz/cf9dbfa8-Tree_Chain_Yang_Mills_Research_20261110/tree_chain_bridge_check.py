"""Exact finite checks for a proposed tree/channel extension, 10 November 2026.

Acceptance uses rational path sums and 192-bit outward interval LDL arithmetic
from the inspected SU(3) verifier. The infinite-tail argument is in the research
note. This script is not Lean and makes no continuum mass-gap claim.
"""
from fractions import Fraction as F
from pathlib import Path
import importlib.util
import json
import math

SOURCE = Path(__file__).resolve().parents[1] / 'yang-mills-lean/research/yang_mills_2026_09_09/scripts/su3_character_certificate.py'
if not SOURCE.exists():
    SOURCE = Path(__file__).with_name('su3_character_certificate.py')
spec = importlib.util.spec_from_file_location('original_su3_verifier', SOURCE)
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


def path_penalty(n, lam, z, depth):
    # A path of at most depth hops from the first omitted shell cannot leave
    # the shells constructed here. Missing further edges therefore do not
    # change ANY retained-to-hidden-to-retained coefficient in this polynomial.
    hidden = [v for v in c.states(n + depth + 2) if sum(v) > n]
    hi = {v:i for i,v in enumerate(hidden)}
    boundary = [(p,n-p) for p in range(n+1)]
    B = []
    for v in boundary:
        B.append({hi[w]:-lam/2 for w in c.neighbors(*v) if w in hi})
    d = [c.casimir(*v) + 3*lam-z for v in hidden]
    dmin = c.tail_floor(n)+3*lam-z
    q = 3*lam/dmin
    assert dmin > 0 and 0 <= q < 1
    adjacency = [[hi[w] for w in c.neighbors(*v) if w in hi] for v in hidden]
    Y = [{i:b/d[i] for i,b in column.items()} for column in B]
    penalty = [[F(0) for _ in boundary] for _ in boundary]
    for level in range(depth+1):
        for a, row in enumerate(B):
            for b, y in enumerate(Y):
                penalty[a][b] += sum((v*y.get(i,F(0)) for i,v in row.items()),F(0))
        if level < depth:
            nextY = []
            for y in Y:
                out = {}
                for j,v in y.items():
                    for i in adjacency[j]:out[i] = out.get(i,F(0)) + (lam/2)*v/d[i]
                nextY.append(out)
            Y = nextY
    remainder = q**(depth+1)/(dmin*(1-q))
    for a,row in enumerate(B):
        for b,col in enumerate(B):
            gram = sum((v*col.get(i,F(0)) for i,v in row.items()),F(0))
            penalty[a][b] += remainder*gram
    assert all(penalty[a][b] == penalty[b][a] for a in range(n+1) for b in range(n+1))
    return penalty, q, remainder


def interval_inertia_of_entries(size, entries):
    bw = max(j-i for i,j in entries)
    mat = [[c.ZERO for _ in range(min(bw+1,size-i))] for i in range(size)]
    for (i,j),value in entries.items():mat[i][j-i] = c.enclose(value)
    signs=[]
    for k in range(size):
        pivot=mat[k][0]
        assert not pivot[0] <= 0 <= pivot[1], ('uncertified pivot',k,pivot)
        signs.append(-1 if pivot[1] < 0 else 1)
        end=min(size,k+bw+1)
        for i in range(k+1,end):
            a=mat[k][i-k]
            if a==c.ZERO:continue
            for j in range(i,end):
                b=mat[k][j-k]
                if b!=c.ZERO:mat[i][j-i]=c.sub(mat[i][j-i],c.product_quotient(a,b,pivot))
    return signs


def check_case(n, lam, z, depth, e0_upper):
    penalty,q,remainder=path_penalty(n,lam,z,depth)
    size,entries=c.matrix_entries(n,lam,z,schur=False)
    start=n*(n+1)//2
    for i in range(n+1):
        for j in range(i,n+1):
            if penalty[i][j]:entries[start+i,start+j]=entries.get((start+i,start+j),F(0))-penalty[i][j]
    signs=interval_inertia_of_entries(size,entries)
    old_count,_=c.interval_inertia(n,lam,z,schur=True)
    assert signs.count(-1)==1
    assert old_count>1
    reference_cutoff=10 if lam==10 else 25
    ground_count,_=c.interval_inertia(reference_cutoff,lam,e0_upper,schur=False)
    assert ground_count==1 and e0_upper<z
    return dict(N=n,lambda_over_kappa=str(lam),retained_dimension=size,walk_depth=depth,
                E1_lower=str(z),E0_upper=str(e0_upper),gap_lower=str(z-e0_upper),
                q=str(q),remainder_norm_bound=str(remainder),
                exact_new_negative_pivots=signs.count(-1),old_negative_pivots_at_same_z=old_count,
                E0_upper_reference_cutoff=reference_cutoff,E0_upper_rechecked=True,
                exact_pivot_signs=signs)


def arithmetic_checks():
    # Exact reduced-coordinate tests of the three-axis auxiliary operator.
    import sympy as s
    g=s.symbols('g',real=True)
    co=(1-g*g)/(1+g*g);si=2*g/(1+g*g)
    rotations=[s.Matrix([[1,0,0],[0,co,-si],[0,si,co]]),
               s.Matrix([[co,0,si],[0,1,0],[-si,0,co]]),
               s.Matrix([[co,-si,0],[si,co,0],[0,0,1]])]
    basis=[]
    for symmetric in [False,True]:
        for i,j in [(0,1),(0,2),(1,2)]:
            b=s.zeros(3);b[i,j]=1;b[j,i]=1 if symmetric else -1;basis.append(b)
    basis += [s.diag(1,-1,0),s.diag(1,1,-2)]
    L=s.zeros(8)
    for j,e in enumerate(basis):
        le=sum((2*e-r*e*r.T-r.T*e*r for r in rotations),s.zeros(3))
        for i,f in enumerate(basis):L[i,j]=s.factor(s.trace(f.T*le)/s.trace(f.T*f))
    expected=[8*g*g/(1+g*g)]*3+[8*g*g*(g*g+3)/(1+g*g)**2]*3+[24*g*g/(1+g*g)**2]*2
    actual=[]
    for value,multiplicity in L.eigenvals().items():actual += [value]*multiplicity
    t=s.symbols('t')
    assert s.factor(s.prod(t-v for v in actual)-s.prod(t-v for v in expected))==0
    # Independent exact verification that each proposed rotation is orthogonal.
    for r in rotations:
        assert all(s.factor(x)==0 for x in r.T*r-s.eye(3))
        assert s.factor(r.det()-1)==0
    # These guards expose why the scalar mode must be removed, and why the
    # three independent axes matter.
    scalar_energy=sum((2*s.eye(3)-r*r.T-r.T*r for r in rotations),s.zeros(3))
    assert all(s.factor(x)==0 for x in scalar_energy)
    r=rotations[0];fixed=s.diag(2,-1,-1)
    assert all(s.factor(x)==0 for x in 2*fixed-r*fixed*r.T-r.T*fixed*r)
    # Prime-labelled CF words preserve determinant; primality is not used by
    # this invariant. A literal twin-coordinate lift has even determinant.
    prime=[True]*100001;prime[:2]=[False,False]
    for p in range(2,317):
        if prime[p]:prime[p*p::p]=[False]*len(prime[p*p::p])
    twins=[p for p in range(11,99999) if prime[p] and prime[p+2]]
    q0=(1,0);q1=(0,1)
    for p,r in zip(twins,twins[1:]):
        assert (r-p)%6==0
        a=(r-p)//6
        q2=(q0[0]+a*q1[0],q0[1]+a*q1[1])
        assert abs(q1[0]*q2[1]-q1[1]*q2[0])==1
        assert p*(r+2)-(p+2)*r==2*(p-r)
        q0,q1=q1,q2
    # A target above the already enclosed first excited level must fail.
    penalty,_,_=path_penalty(6,F(10),F(17),6)
    size,entries=c.matrix_entries(6,F(10),F(17),schur=False)
    start=21
    for i in range(7):
        for j in range(i,7):
            entries[start+i,start+j]=entries.get((start+i,start+j),F(0))-penalty[i][j]
    false_count=interval_inertia_of_entries(size,entries).count(-1)
    assert false_count>1
    return dict(three_axis_symbolic_spectrum='PASS',orthogonal_SU3_rotations='PASS',
                scalar_zero_mode_guard='PASS',single_axis_zero_mode_guard='PASS',
                false_E1_17_target='REJECTED',false_target_negative_pivots=false_count,
                prime_labelled_CF_steps=len(twins)-1,
                literal_twin_pairing_even='PASS',
                caveat='CF compatibility is independent of whether the labels are prime.')


if __name__=='__main__':
    results=[]
    for case in [(6,F(10),F(151,10),6,F(112158947,10000000)),
                 (15,F(100),F(433,10),6,F(192892347,5000000)),
                 (15,F(100),F(1264,25),12,F(192892347,5000000))]:
        result=check_case(*case);results.append(result);print(json.dumps(result),flush=True)
    output=dict(status='PASS',cases=results,joins=arithmetic_checks(),
                scope='Exact finite checks plus a written single-loop tail argument; no Lean compilation or volume/continuum claim.')
    Path(__file__).with_name('tree_chain_bridge_results.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output['joins']),flush=True)
