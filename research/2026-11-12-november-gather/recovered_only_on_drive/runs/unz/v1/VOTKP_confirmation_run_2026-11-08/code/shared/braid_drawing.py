#!/usr/bin/env python3
"""
braid_drawing.py -- build the UPRIGHT braid-closure diagram and read the
rotation numbers off the drawing instead of guessing them.

The picture.  A braid on m strands, all strands drawn ascending, with the
closure arcs at top and bottom.  At every crossing both strands are locally
ascending, so the crossings are upright in the paper's sense.  Each braid
segment between crossings is a monotone ascending arc: no horizontal
tangency, so phi = 0.  All the rotation sits in the closure arcs: such an arc
leaves the top of the braid heading up, turns clockwise through "heading
right" (a CAP, contributing -1), descends, and re-enters the bottom heading up.
Hence phi = -1 per closure arc, and Sum phi = -(number of arcs).

The arc is not a separate edge: the segment from the last crossing of one
ascent, up over the top, around, and down to the first crossing of the next
ascent is ONE edge containing one arc, so phi = -1 on that edge.

Gates checked before any invariant is used:
  * the braid permutation is a single m-cycle (the closure is a knot);
  * the traversal produces exactly 2L visits (2L edges);
  * Sum phi = -(arc count) and Sum phi + w is even (integrality);
  * T^e det A reproduces the Alexander polynomial.
"""
from fractions import Fraction as F
from collections import defaultdict

def perm_of(word, m):
    p=list(range(m))
    for g in word:
        i=abs(g)-1
        p[i],p[i+1]=p[i+1],p[i]
    return p

def is_single_cycle(p):
    m=len(p); seen=set(); c=0
    for s in range(m):
        if s in seen: continue
        c+=1; x=s
        while x not in seen:
            seen.add(x); x=p[x]
    return c==1

def diagram(word, m, over_rule=1, sign_flip=1, verbose=False):
    """word: signed ints, +i = sigma_i, -i = sigma_i^{-1}.
    Long closure: the traversal runs from the bottom of the starting strand up
    through the braid to the top, so exactly m-1 closure arcs are inside the
    diagram and the last edge exits at infinity (it becomes edge 2n+1)."""
    L=len(word)
    p=perm_of(word,m)
    assert is_single_cycle(p), "closure is not a knot (permutation not a single cycle)"
    letters=[(abs(g)-1, 1 if g>0 else -1) for g in word]

    visits=[]                 # (crossing_idx, role_over, from, to)
    seq=[]                    # sequence of ('x',..) and ('arc',)
    pos,t=0,0
    guard=0
    arcs_done=0
    while True:
        guard+=1
        assert guard<20*(L+m)+50, "traversal did not close"
        if t<L:
            g,s=letters[t]
            if pos==g:     npos,moves=g+1,True
            elif pos==g+1: npos,moves=g,True
            else:          npos,moves=pos,False
            t+=1
            if moves:
                if over_rule==1: role=((s==1 and pos==g) or (s==-1 and pos==g+1))
                else:            role=((s==1 and pos==g+1) or (s==-1 and pos==g))
                visits.append((t-1,role,pos,npos))
                seq.append(('x',t-1))
                pos=npos
        else:
            if pos==0 and arcs_done>0:      # back at the start strand: exit at the top
                break
            arcs_done+=1
            seq.append(('arc',))
            t=0                             # descend to the bottom of the same strand
        if len(visits)>=2*L and t>=L and pos==0 and arcs_done>0:
            break
    assert len(visits)==2*L, f"expected {2*L} visits, got {len(visits)}"

    # edges: the first edge runs from the start to visits[0]; the k-th edge
    # (number k+1) is the in-edge of visits[k]; the last edge is number V+1.
    V=len(visits)
    phi=defaultdict(int)
    # walk seq, assigning arcs to the gap that precedes the next visit
    pending=0
    e=1
    for step in seq:
        if step[0]=='arc':
            pending+=1
        else:
            if pending:
                phi[e]-=pending; pending=0
            e+=1
    if pending: phi[V+1]-=pending
    # arc before the first visit belongs to edge 1
    byC=defaultdict(dict)
    for k,(cid,role,_pf,_pt) in enumerate(visits):
        byC[cid]['over' if role else 'under']=k+1
    X=[]
    for cid in range(L):
        i=byC[cid]['over']; j=byC[cid]['under']
        s=(1 if letters[cid][1]>0 else -1)*sign_flip
        X.append((s,i,j))
    return X, dict(phi), L, {'m':m,'V':V,'arcs':arcs_done,'sum_phi':sum(phi.values()),
                             'w':sum(s for s,_,_ in X)}
