"""Independent tests of the serialized six-core map, H–Sn cutoff interval and disk-angle convention.

Example:
  python independent_wall_checks.py repo/data/element_thresholds_20261011.json.gz path/to/batch10
No tested packet code is imported. Decimal source strings and central predicates are exact.
"""
import argparse
import csv
import gzip
import hashlib
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path


def csvrows(path):
    with path.open(newline='') as inp:
        return list(csv.DictReader(inp))


def sign(x):
    return (x>0)-(x<0)


def power(z):
    return ((z-1)/(z+1))**2


def bounds(a,b,u,v):
    if None in (u,v):
        return None
    assert a-u>0 and b-v>0
    return (b-v)/(a+u),(b+v)/(a-u)


def power_extremes(interval):
    # g(z) is strictly increasing on z>0. The square has an interior zero exactly at 1.
    lo,hi=interval
    vals=[power(lo),power(hi)]
    if lo<=1<=hi:
        vals.append(F(0))
    return min(vals),max(vals)


def rendered(row,field,expected):
    # Stored maps carry nine fractional decimals. Avoid a binary-float comparison.
    assert abs(F(row[field])-expected)<=F(1,2*10**9),(field,row[field],expected)


def pairmap(archive,packet):
    # Index by *electron counts of each ion*, independently of printed q offsets.
    faces=defaultdict(dict)
    lookup={r['Z']:r for r in archive}
    for Z,e in lookup.items():
        by_count={Z-t['q']:t for t in e['thresholds']}
        for n,core in [(2,'helium'),(10,'neon'),(18,'argon'),(36,'krypton'),(54,'xenon'),(86,'radon')]:
            if n+1 in by_count and n in by_count:
                l,r=by_count[n+1],by_count[n]
                z=r['IE_eV']/l['IE_eV']
                box=bounds(l['IE_eV'],r['IE_eV'],l['unc_eV'],r['unc_eV'])
                assert box
                faces[core][Z]=z,box,l,r
    fcsv=csvrows(packet/'mixed_map/opening_faces.csv')
    assert len(fcsv)==sum(map(len,faces.values()))
    seen=set()
    for row in fcsv:
        core,Z=row['core'],int(row['Z']);key=(core,Z)
        assert key not in seen;seen.add(key)
        z,box,x,y=faces[core][Z]
        assert x['q']==int(row['q'])==y['q']-1
        for rec,field,uf,gf,rf in [(x,'start_q_IE_eV','start_unc_eV','start_grade','start_reference'),(y,'end_q_plus_1_IE_eV','end_unc_eV','end_grade','end_reference')]:
            assert F(row[field])==rec['IE_eV'] and F(row[uf])==rec['unc_eV']
            assert row[gf]==rec['grade'] and row[rf]==rec['references']
        assert F(row['exact_z'])==z
        rendered(row,'z_low',box[0]);rendered(row,'z_high',box[1])
    pcsv=csvrows(packet/'mixed_map/adjacent_pairs.csv')
    assert len(pcsv)==sum(sum(Z+1 in group for Z in group) for group in faces.values())
    scores=[]
    sides={1:'open',0:'ideal',-1:'closes'}
    events=Counter(); seen=set(); missing_pair_boxes=0
    crossing_ones=sum(box[0]<=1<=box[1] for d in faces.values() for _,box,_,_ in d.values())
    for row in pcsv:
        core,Z,W=row['core'],int(row['Z_left']),int(row['Z_right'])
        assert W==Z+1 and (core,Z) not in seen
        seen.add((core,Z))
        a,A,x0,x1=faces[core][Z]
        b,B,y0,y1=faces[core][W]
        # All four energy source charges, independently checked against row and electron count.
        assert [x0['q'],x1['q'],y0['q'],y1['q']]==[int(row['q_left']),int(row['q_left'])+1,int(row['q_right']),int(row['q_right'])+1]
        assert (x0['grade']+x1['grade'],y0['grade']+y1['grade'])==(row['left_IE_grades'],row['right_IE_grades'])
        margin=power(a)+power(b)-1
        # Strict crossing of ideal endpoints on disk boundary: projected ideal directions of first
        # geodesic have sine ±sqrt(1-g_a²). At 90° they enclose the second normal iff g_b²<1-g_a².
        # Independently clear radical/denominator using the raw squared-sinh product.
        poly=(a-1)**2*(b-1)**2-16*a*b
        assert sign(poly)==sign(margin)
        assert row['mixed']==sides[sign(margin)]
        rendered(row,'signed_margin',margin)
        pa,pb=power_extremes(A),power_extremes(B)
        low,high=pa[0]+pb[0]-1,pa[1]+pb[1]-1
        rendered(row,'margin_low',low);rendered(row,'margin_high',high)
        if low<=0<=high:missing_pair_boxes+=1
        else:assert row['mixed_endpoints']==row['mixed']
        assert (row['self_left'],row['self_right'])==(sides[sign(2*power(a)-1)],sides[sign(2*power(b)-1)])
        for key,powbox in [('self_left_endpoints',pa),('self_right_endpoints',pb)]:
            verdict='open' if powbox[0]>F(1,2) else 'closes' if powbox[1]<F(1,2) else 'straddles/touches'
            assert row[key]==verdict
        assert row['central_direction']==('falling' if a>b else 'rising' if a<b else 'unchanged')
        assert row['direction_endpoints']==('falling' if A[0]>B[1] else 'rising' if A[1]<B[0] else 'overlap')
        rendered(row,'z_left',a);rendered(row,'z_right',b)
        events['rises']+=a<b;events['falls']+=a>b;events['ties']+=a==b
        events['robust_falls']+=A[0]>B[1];events['robust_rises']+=A[1]<B[0]
        events['open' if margin>0 else 'ideal' if margin==0 else 'closed']+=1
        scores.append((abs(margin),min(abs(low),abs(high)) if low*high>0 else F(0),max(abs(low),abs(high)),core,Z,W))
    scores.sort()
    best,second=scores[:2]
    assert best[2]<min(i[1] for i in scores[1:])
    print('Map CSV face and adjacent-pair matches:',len(fcsv),len(pcsv))
    print('Ratio boxes containing 1:',crossing_ones,'unresolved mixed calls:',missing_pair_boxes,'counts:',dict(events))
    print('Closest and runner-up (core, Z, Z+1, |M|, lower/upper |M|):')
    for score,mi,ma,core,Z,W in scores[:2]:
        print(core,Z,W,f'{float(score):.12f}',f'{float(mi):.12f}',f'{float(ma):.12f}')
    # Equality and reversal hostile controls.
    assert power(F(9))+power(F(4))==1
    assert power(F(1,9))+power(F(1,4))==1
    assert power(F(9))+power(F(4)-F(1,10**12))<1<power(F(9))+power(F(4)+F(1,10**12))
    return faces


def cutoffs(archive,packet):
    rows=[]
    ea=csvrows(packet/'robust/affinities_h_sn.csv')
    assert len(ea)==50 and len({int(row['Z']) for row in ea})==50
    for e in archive:
        Z,s=e['Z'],e['symbol']
        if Z>50:continue
        line=ea[Z-1];assert int(line['Z'])==Z and s==line['symbol']
        energies={t['q']+1:(t['IE_eV'],t['unc_eV']) for t in e['thresholds']}
        if line['EA_source_units']:
            conv=F('6.62607015e-34')*299792458*100/F('1.602176634e-19') if 'cm-1' in line['source'] else 1
            energies[0]=(F(line['EA_source_units'])*conv,F(line['unc_source_units'])*conv if line['unc_source_units'] else None)
        for k in sorted(energies):
            if k==Z:continue
            a,u=energies[k];b,v=energies[k+1]
            z=b/a
            rows.append((s,k,z,bounds(a,b,u,v)))
    print('H–Sn counts:',len(rows),'ordinary:',sum(r[1]>0 for r in rows),'conditional/missing boxes:',sum(r[3] is None for r in rows))
    missing={(s,k) for s,k,z,box in rows if box is None}
    assert missing=={(r['element'],int(r['k'])) for r in csvrows(packet/'robust/cutoff_missing_boxes.csv')}
    for mode in ('ordinary','all'):
        r=[i for i in rows if mode=='all' or i[1]>0]
        inner=[p for p in r if 2*power(p[2])<=1]
        outer=[p for p in r if 2*power(p[2])>1]
        for with_box in (False,True):
            def extreme(side,left):
                a=[(s,k,box[1 if left else 0] if with_box else z) for s,k,z,box in side if box or not with_box]
                return (max if left else min)(a,key=lambda t:t[2])
            l=extreme(inner,True);u=extreme(outer,False)
            print(mode,'box' if with_box else 'central','[',l,',',u,')')
            assert l[2]<u[2]
            for s,k,z,box in r:
                if with_box and box is None:continue
                points=box if with_box else (z,)
                for point in points:
                    if with_box:assert point>F(1,2)
                    assert (point>l[2])==(2*power(z)>1)
            # At inclusive lower endpoint, the limiting inside observation must remain inside.
            # At exclusive upper endpoint, the limiting outside observation becomes equality.
            # Ensure the named limiting observations actually exist in the appropriate class.
            assert any((s,k)==l[:2] and (box[1] if with_box else z)==l[2]
                       for s,k,z,box in inner if box is not None or not with_box)
            assert any((s,k)==u[:2] and (box[0] if with_box else z)==u[2]
                       for s,k,z,box in outer if box is not None or not with_box)
            for cut,should_match in [(l[2]-F(1,10**14),False),(l[2],True),
                                     (u[2]-F(1,10**14),True),(u[2],False)]:
                matches=all((p>cut)==(2*power(z)>1) for s,k,z,box in r if box or not with_box
                            for p in (box if with_box else (z,)))
                assert matches==should_match
    high_inside=F(7576259,1304450)
    other=Counter()
    for e in archive[:50]:
        levels=e['thresholds']; z=e['Z']
        for i in range(z-1):
            if levels[i]['unc_eV'] is not None and levels[i+1]['unc_eV'] is not None:continue
            low=i;high=i+1
            while low>=0 and levels[low]['unc_eV'] is None:low-=1
            while high<z and levels[high]['unc_eV'] is None:high+=1
            assert low>=0 and high<z
            upper=(levels[high]['IE_eV']+levels[high]['unc_eV'])/(levels[low]['IE_eV']-levels[low]['unc_eV'])
            other['conditionally below silver' if upper<high_inside else 'still unknown']+=1
    print('Monotone-energy sensitivity, 17 ordinary incomplete boxes:',dict(other))
    print('Exact c=5 alternatives:',[(s,k) for s,k,z,_ in rows if (z>5)!=(2*power(z)>1)])


def tilt(faces):
    # Half widths of the arcs cut by the Poincare face circles on the unit disk boundary.
    # Their endpoints are at normal-angle ±alpha; both normals refer to oriented outward rays.
    c,n=(faces['helium'][Z][0] for Z in (6,7))
    g,h=(float((z-1)/(z+1)) for z in (c,n))
    ac,an=math.acos(g),math.acos(h)
    low,high=abs(ac-an),ac+an
    edge=math.acos(h/g)
    print('Carbon and nitrogen full-line lower & upper ideal and sector entry degrees:',*[f'{math.degrees(q):.11f}' for q in (low,high,edge)])
    for deg in (1,2,10,15,89.8,90):
        t=math.radians(deg);c0=1/g;c1=1/h;r0=math.sqrt(c0*c0-1);r1=math.sqrt(c1*c1-1)
        d=math.hypot(c1*math.cos(t)-c0,c1*math.sin(t))
        circles=abs(r0-r1)<d<r0+r1
        # Alternate endpoints along boundary for the two chords iff geodesics intersect.
        crossings=(abs(t-ac)<an)!=(abs(t+ac)<an)
        assert circles==crossings==(low<t<high)
        wedge=g*math.cos(t)<h and h*math.cos(t)<g
        print(f'{deg:g}°: supports intersect={circles}; interior-to-sector intersection={circles and wedge}')
    for t in (low,high):
        d=math.hypot(math.cos(t)/h-1/g,math.sin(t)/h)
        assert min(abs(d-(r0+r1)),abs(d-abs(r0-r1)))<2e-14
    print('At the two contact angles the complete supports have one common ideal endpoint.')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive',type=Path);parser.add_argument('packet',type=Path)
    args=parser.parse_args()
    raw=args.archive.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
    data=json.loads(gzip.decompress(raw),parse_float=F)['records']
    faces=pairmap(data,args.packet);cutoffs(data,args.packet);tilt(faces)
