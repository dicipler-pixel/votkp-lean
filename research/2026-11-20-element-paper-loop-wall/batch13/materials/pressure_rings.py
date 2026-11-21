"""Nearest contacts and shortest embedded six-rings in two measured oF8 structures."""
import csv
from collections import Counter, defaultdict
from decimal import Decimal as D, getcontext
from itertools import product
from pathlib import Path

getcontext().prec=40
HERE=Path(__file__).resolve().parent
# Standard Fddd origin choice 1 Wyckoff 8a (0,0,0), in integer quarter-cell units.
F_CENTERS=((0,0,0),(0,2,2),(2,0,2),(2,2,0))
SITES=F_CENTERS+tuple(tuple(i+1 for i in v) for v in F_CENTERS)
BONDS=tuple(v for v in product((-1,1),repeat=3) if v[0]*v[1]*v[2]==1)
ORIGIN=(0,0,0)


def walk(u,v,sign=1):
    return tuple(x+sign*y for x,y in zip(u,v))


def sub(u,v):
    return walk(u,v,-1)


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def shells(axes):
    result=defaultdict(list)
    for center in SITES:
        for shift in product((-1,0,1),repeat=3):
            v=tuple(c+4*s for c,s in zip(center,shift))
            if v!=ORIGIN:
                dist2=sum((a*x/4)**2 for a,x in zip(axes,v))
                result[dist2].append(v)
    return sorted(result.items())


def all_short_cycles():
    found=set()
    def extend(path):
        sign=1 if (len(path)-1)%2==0 else -1
        for bond in BONDS:
            nxt=walk(path[-1],bond,sign)
            if nxt==ORIGIN and len(path)>=3:
                cycle=tuple(path)
                found.add(min(cycle,(ORIGIN,)+tuple(reversed(cycle[1:]))))
            elif len(path)<6 and nxt not in path:
                extend(path+[nxt])
    extend([ORIGIN])
    return sorted(found)


def projection_certificate(ring):
    edges=[sub(ring[(i+1)%6],ring[i]) for i in range(6)]
    directions={edge if i%2==0 else tuple(-v for v in edge) for i,edge in enumerate(edges)}
    (normal,)=set(BONDS)-directions
    # For every oriented polygon edge, the other four projected vertices lie strictly
    # on its same side. This certifies a convex simple image without a crossing.
    turns=[]
    for i,edge in enumerate(edges):
        nonadjacent=[j for j in range(6) if j not in (i,(i+1)%6)]
        turns.extend(dot(normal,cross(edge,sub(ring[j],ring[i]))) for j in nonadjacent)
    if not (min(turns)>0 or max(turns)<0):
        raise ValueError("No strict convex projection")
    return normal,min(map(abs,turns))


def run():
    with (HERE/"pressure_structures.csv").open() as f:
        records=list(csv.DictReader(f))
    with (HERE/"pressure_contacts.csv").open("w",newline="") as f:
        out=csv.writer(f,lineterminator="\n")
        out.writerow(["element","P_GPa","shell","multiplicity","d_A","d_lo_A","d_hi_A",
                      "contact_quarter_offsets","volume_per_atom_A3","b_over_c"])
        for r in records:
            a=tuple(D(r[n+"_A"]) for n in "abc")
            u=tuple(D(r["d"+n+"_A"]) for n in "abc")
            low=tuple(x-y for x,y in zip(a,u))
            high=tuple(x+y for x,y in zip(a,u))
            center=shells(a)
            vol=a[0]*a[1]*a[2]/8
            # Any unenumerated translate has a coordinate whose magnitude is at least
            # 5/4 of a cell length. Check that this exceeds all first three shells.
            if D(5)/4*min(low)<=shells(high)[2][0].sqrt():
                raise ValueError("Translation window too small")
            for corner in product(*zip(low,high)):
                ss=shells(corner)
                if any(set(ss[i][1])!=set(center[i][1]) for i in range(3)):
                    raise ValueError("Input box changes first-three-shell ordering")
            lo,hi=shells(low),shells(high)
            if hi[0][0]>=lo[1][0] or hi[1][0]>=lo[2][0]:
                raise ValueError("Shell intervals not separated globally")
            for i,(rad,vectors) in enumerate(center[:3]):
                out.writerow([r["symbol"],r["pressure_GPa"],i+1,len(vectors),f"{rad.sqrt():.9f}",
                              f"{lo[i][0].sqrt():.9f}",f"{hi[i][0].sqrt():.9f}",
                              " ".join("/".join(map(str,v)) for v in sorted(vectors)),f"{vol:.9f}",
                              f"{a[1]/a[2]:.9f}"])
            if set(center[0][1])!=set(BONDS):
                raise ValueError("Shortest-shell graph is not the chosen four-neighbour graph")
            print(r["symbol"],"gap to next shell at worst box endpoints (Å)",
                  f"{lo[1][0].sqrt()-hi[0][0].sqrt():.9f}")
    rings=all_short_cycles()
    if Counter(map(len,rings))!={6:12}:
        raise ValueError("Unexpected short rings")
    with (HERE/"shortest_contact_rings.csv").open("w",newline="") as f:
        out=csv.writer(f,lineterminator="\n")
        out.writerow(["ring","vertices_qtr_cell","normal_integer_frame","minimum_absolute_signed_side_test"])
        for i,ring in enumerate(rings,1):
            normal,minimum=projection_certificate(ring)
            out.writerow([i," ".join("/".join(map(str,v)) for v in ring),
                          "/".join(map(str,normal)),minimum])
    print("At one site: no simple 3, 4 or 5 cycle; 12 unoriented simple six-edge cycles.")
    print("All 12 have a strictly convex projection in the integer coordinate frame.")
    print("Positive cell-axis scaling preserves their knot type.")


if __name__=="__main__":
    run()
