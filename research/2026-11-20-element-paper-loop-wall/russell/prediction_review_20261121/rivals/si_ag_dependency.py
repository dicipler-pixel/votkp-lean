#!/usr/bin/env python3
"""Correlated endpoint audit of Si-Ag. Requires mpmath 1.3+; comparison on interval boxes."""
import argparse
import csv
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

from mpmath import iv
from check_rivals import load_faces

iv.dps=35


def exact(q):
    return iv.mpf(q.numerator)/q.denominator


@dataclass(frozen=True)
class Jet:
    value: object
    da: object=0
    db: object=0

    def __add__(self,b):
        b=jet(b)
        return Jet(self.value+b.value,self.da+b.da,self.db+b.db)

    __radd__=__add__

    def __neg__(self):
        return Jet(-self.value,-self.da,-self.db)

    def __sub__(self,b):
        return self+-jet(b)

    def __rsub__(self,a):
        return jet(a)+-self

    def __mul__(self,b):
        b=jet(b)
        return Jet(self.value*b.value,self.da*b.value+self.value*b.da,self.db*b.value+self.value*b.db)

    __rmul__=__mul__

    def __truediv__(self,b):
        b=jet(b)
        return self*unary(b,1/b.value,-1/(b.value**2))

    def __rtruediv__(self,a):
        return jet(a)/self


def jet(x):
    return x if isinstance(x,Jet) else Jet(iv.mpf(x))


def unary(x,value,deriv):
    return Jet(value,deriv*x.da,deriv*x.db)


def sqrt(x):
    y=iv.sqrt(x.value)
    return unary(x,y,1/(2*y))


def exp(x):
    y=iv.exp(x.value)
    return unary(x,y,y)


def log(x):
    return unary(x,iv.ln(x.value),1/x.value)


def atan(x):
    return unary(x,iv.atan2(x.value,1),1/(1+x.value**2))


def sq(x):
    return unary(x,x.value**2,2*x.value)


def refl(x):
    return (x-1)/(x+1)


def inv_refl(x):
    return (1+x)/(1-x)


def sh(x):
    return (x-1)/(2*sqrt(x))


def theta(x):
    return 2*atan(sqrt(x))-jet(iv.pi)/2


def calc(a,b):
    ga,gb=refl(a),refl(b)
    sa,sb=sh(a),sh(b)
    u=sqrt(sa*sb)
    midpoints={
        "arithmetic_z": (a+b)/2,
        "geometric_z": sqrt(a*b),
        "harmonic_z": 2/(1/a+1/b),
        "arithmetic_gamma": inv_refl((ga+gb)/2),
        "arithmetic_gamma_squared": inv_refl(sqrt((sq(ga)+sq(gb))/2)),
        "geometric_sinh_half": sq(u+sqrt(sq(u)+1)),
    }
    logw=log(jet(3)+2*sqrt(jet(2)))
    scores={}
    for name,c in midpoints.items():
        power=logw/log(c)
        scores[name,"quadrature"]=sq(ga)+sq(gb)-2*sq(refl(c))
        scores[name,"sinh_product"]=sa*sb-sq(sh(c))
        scores[name,"log_clock_gain"]=sq(refl(exp(power*log(a))))+sq(refl(exp(power*log(b))))-1
        scores[name,"asin_angle_sum"]=theta(a)+theta(b)-2*theta(c)
    return scores


def axes(low,high,n):
    for i in range(n):
        left=low+(high-low)*F(i,n)
        right=low+(high-low)*F(i+1,n)
        yield (iv.mpf([exact(left).a,exact(right).b]),exact((left+right)/2),exact((right-left)/2))


def main(opts):
    faces=load_faces(opts.tables,opts.archive)
    inside=sorted((f for f in faces if not f.outside),key=lambda f:f.high,reverse=True)
    outside=sorted((f for f in faces if f.outside),key=lambda f:f.low)
    A,B=inside[0],outside[0]
    assert (A.symbol,A.k,B.symbol,B.k)==("Ag",0,"Si",0)
    assert inside[1].high<A.low and outside[1].low>B.high
    # All other complete input rectangles stay farther from the separating interval.
    # Records lacking an input width retain their adopted point in this sensitivity test.
    bounds={}
    ties={("arithmetic_gamma_squared","quadrature"),("geometric_sinh_half","sinh_product")}
    for ar,am,aw in axes(A.low,A.high,opts.subdivisions):
        for br,bm,bw in axes(B.low,B.high,opts.subdivisions):
            gradients=calc(Jet(ar,1,0),Jet(br,0,1))
            centers=calc(Jet(am),Jet(bm))
            for key,center in centers.items():
                if key in ties:
                    # Because this pair is used to calibrate the cutoff, these equalities
                    # hold exactly at every point; they are identities by construction.
                    assert 0 in center.value
                    low=high=0.0
                else:
                    j=gradients[key]
                    error=iv.mpf([0,1])*(abs(j.da)*aw+abs(j.db)*bw)
                    v=center.value+iv.mpf([-1,1])*error
                    low,high=float(v.a),float(v.b)
                if key in bounds:
                    old=bounds[key]
                    bounds[key]=(min(low,old[0]),max(high,old[1]))
                else:
                    bounds[key]=(low,high)
    counts={}
    with (opts.out/"si_ag_shared_boxes.csv").open("w") as f:
        w=csv.writer(f,lineterminator="\n")
        w.writerow(["midpoint","extension","score_low","score_high","shared_box_call"])
        for key,(low,hi) in bounds.items():
            assert (key in ties) or (low>0 or hi<0)
            side="open" if low>0 else "closed" if hi<0 else "ideal"
            w.writerow([*key,low,hi,side])
            counts[side]=counts.get(side,0)+1
    print("Si and Ag remain the unique calibration endpoints on the entire known-width box.")
    print(f"{opts.subdivisions} by {opts.subdivisions} interval-derivative boxes; 24 alternative rules:",counts)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("tables",type=Path)
    p.add_argument("archive",type=Path)
    p.add_argument("out",type=Path)
    p.add_argument("--subdivisions",type=int,default=8)
    main(p.parse_args())
