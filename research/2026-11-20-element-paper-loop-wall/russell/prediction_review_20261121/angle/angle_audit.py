"""Verify the oblique disk and two distinct two-coordinate transfer constructions.

Python 3, standard library. Without an argument, uses the four printed inputs.
Pass the pinned compressed thresholds to check the energy inputs and grades.
"""
import argparse
import gzip
import hashlib
import itertools
import json
import math
from fractions import Fraction as Q
from pathlib import Path

PIN = '75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
INPUT = (
    (4, 1, '18.21115', '.00004', 'E'),
    (4, 2, '153.896205', '.000004', 'T'),
    (37, 34, '4356.865', '.01', 'T'),
    (37, 35, '18305.886', '.004', 'T'),
)

def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]

def trace(a):
    return a[0][0] + a[1][1]

def determinant(a):
    return a[0][0]*a[1][1] - a[0][1]*a[1][0]

def inverse(a):
    d = determinant(a)
    return [[a[1][1]/d, -a[0][1]/d], [-a[1][0]/d, a[0][0]/d]]

def g(z):
    return (z-1)/(z+1)

def face_matrix(z, phi):
    h = math.log(z)/2
    t = math.sinh(h)
    x, y = math.cosh(h)*math.cos(phi), math.cosh(h)*math.sin(phi)
    return [[x, t+y], [-t+y, -x]]

def stretch(z, phi):
    # phi is the angle of the expanding eigenvector in the instrument plane.
    r, c, s = math.sqrt(z), math.cos(phi), math.sin(phi)
    return [[r*c*c+s*s/r, (r-1/r)*c*s],
            [(r-1/r)*c*s, r*s*s+c*c/r]]

def disk_margin(x, y, c):
    return c*c - 2*x*y*c + x*x + y*y - 1

def transfer(a, b, deg):
    theta = math.radians(deg)
    A, B = stretch(a, 0), stretch(b, theta/2)
    closed_word = multiply(multiply(A,B),multiply(inverse(A),inverse(B)))
    n, m = face_matrix(a, 0), face_matrix(b, theta)
    product = multiply(n,m)
    E = [[1,0],[0,-1]]
    left, right = multiply(n,E), multiply(E,m)
    for matrix in [closed_word,product,left,right]:
        assert math.isclose(determinant(matrix), 1, abs_tol=2e-12)
    assert math.isclose(trace(multiply(left,right)), trace(product), abs_tol=1e-12)
    x,y = g(a),g(b)
    scale = (1-x*x)*(1-y*y)
    c,s = math.cos(theta), math.sin(theta)
    F = disk_margin(x,y,c)
    norm2 = x*x+(y-x*c)**2/s**2
    assert abs((norm2-1)*s*s - F) < 2e-14
    if x>0 and y>0 and c<min(x/y,y/x):
        # Independent original Poincare-circle distance (small-angle containment
        # uses both lower and upper distance conditions).
        ca,cb = 1/x,1/y
        ra,rb = math.sqrt(ca*ca-1),math.sqrt(cb*cb-1)
        d = math.sqrt(ca*ca+cb*cb-2*ca*cb*c)
        if abs(F)>1e-12:
            assert (abs(ra-rb)<d<ra+rb) == (F<0)
    assert abs(scale*((trace(product)/2)**2-1)-F) < 2e-12
    k = math.sinh(math.log(a)/2)*math.sinh(math.log(b)/2)
    assert abs(trace(closed_word)-(2-4*k*k*s*s)) < 2e-11
    return F, trace(closed_word), trace(product)

def contacts(a,b):
    x,y = g(a),g(b)
    w = math.sqrt((1-x*x)*(1-y*y))
    lower,upper = [math.degrees(math.acos(x*y+sign*w)) for sign in (1,-1)]
    entry = math.degrees(math.acos(min(x/y,y/x)))
    k = x*y/w
    half = math.degrees(math.acos(1/k))
    return lower, entry, upper, 90-half, 90+half

def main(archive):
    if archive:
        assert hashlib.sha256(archive.read_bytes()).hexdigest()==PIN
        with gzip.open(archive,'rt') as f:
            atoms = json.load(f,parse_float=Q)['records']
        for Z,q,e,d,grade in INPUT:
            r=atoms[Z-1]['thresholds'][q]
            assert (r['q'],Q(r['IE_eV']),Q(r['unc_eV']),r['grade'])==(q,Q(e),Q(d),grade)
    energies=[Q(r[2]) for r in INPUT]
    a,b=energies[1]/energies[0],energies[3]/energies[2]
    x,y=g(a),g(b)
    # Exact counterexample at cos(theta) = 1/1000 on the original elemental inputs.
    c=Q(1,1000)
    F=disk_margin(x,y,c)
    delta=x*x*y*y*(1-c*c) - (1-x*x)*(1-y*y)
    assert F<0<delta and c<min(x/y,y/x)
    print('ratios Be and Rb:',float(a),float(b))
    print('derivative of disk margin per radian:',float(2*x*y))
    print('nearby disk/contact and commutator criticals, degrees:',contacts(float(a),float(b)))
    print('theta; disk F; commutator trace; face-product trace')
    for deg in [45,60,85,87,89,89.9,math.degrees(math.acos(c)),90,90.1,93]:
        print(f'{deg:.8f}',*[f'{f:.10f}' for f in transfer(float(a),float(b),deg)])
    # The upper disk contact increases/decreases monotonically as discussed in note.
    widths = [Q(r[3]) for r in INPUT]
    corners=[]
    for signs in itertools.product([-1,1],repeat=4):
        vals=[val+sgn*width for val,sgn,width in zip(energies,signs,widths)]
        aa,bb=vals[1]/vals[0],vals[3]/vals[2]
        xx,yy=g(aa),g(bb)
        assert disk_margin(xx,yy,c)<0
        assert xx*xx*yy*yy*(1-c*c)>(1-xx*xx)*(1-yy*yy)
        corners.append(contacts(float(aa),float(bb)))
    print('upper disk contact corner range:',min(t[2] for t in corners),max(t[2] for t in corners))
    print('lower commutator contact corner range:',min(t[3] for t in corners),max(t[3] for t in corners))
    for deg in [30,60,90,120,150]:
        forwards=transfer(float(a),float(b),deg)
        backwards=transfer(1/float(a),1/float(b),deg)
        assert all(abs(u-v)<2e-12 for u,v in zip(forwards, backwards))
    for aa,bb in [(9.,4.),(4.,4.),(7.,7.)]:
        for deg in [30,60,90,120,150]:
            transfer(aa,bb,deg)
    xx,yy=Q(4,5),Q(3,5)
    for cc,target in [(Q(-3,5),Q(-9,2)),(Q(0),Q(-2)),(Q(3,5),Q(1,2))]:
        _,wc,pc=transfer(9.,4.,math.degrees(math.acos(cc)))
        assert abs(wc-float(2-4*(1-cc*cc)))<1e-12 and abs(pc-float(target))<1e-12
        print('9,4 control cos theta:',cc,'disk F:',disk_margin(xx,yy,cc),
              'commutator normalized excess:', xx*xx*yy*yy*(1-cc*cc)-(1-xx*xx)*(1-yy*yy))
    print('PASS')
if __name__=='__main__':
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument('archive',nargs='?',type=Path)
    main(cli.parse_args().archive)
