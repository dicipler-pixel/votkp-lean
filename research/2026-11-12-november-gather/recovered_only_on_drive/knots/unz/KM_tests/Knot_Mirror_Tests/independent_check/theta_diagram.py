#!/usr/bin/env python3
"""Exact rational implementation of Bar-Natan/van der Veen arXiv:2509.18456v4 Eqs (1)-(6).
First benchmark against the authors' explicitly published trefoil polynomial.
No Sage, diagram isotopy, or independent knot identification is asserted.
"""
from fractions import Fraction as F
import json

def inverse(m):
 n=len(m); a=[row[:] + [F(int(i==j)) for j in range(n)] for i,row in enumerate(m)]
 for k in range(n):
  idx=next((i for i in range(k,n) if a[i][k]),None)
  if idx is None: raise ValueError('singular traffic matrix')
  a[k],a[idx]=a[idx],a[k]; q=a[k][k];a[k]=[x/q for x in a[k]]
  for i in range(n):
   if i!=k:
    q=a[i][k]
    if q:a[i]=[x-q*y for x,y in zip(a[i],a[k])]
 return [row[n:] for row in a]

def det(m):
 a=[r[:] for r in m]; n=len(a);d=F(1)
 for j in range(n):
  i=next((i for i in range(j,n) if a[i][j]),None)
  if i is None:return F(0)
  if i!=j: a[i],a[j]=a[j],a[i];d=-d
  pivot=a[j][j];d*=pivot
  for i in range(j+1,n):
   q=a[i][j]/pivot
   for k in range(j,n):a[i][k]-=q*a[j][k]
 return d

def mat(t,X,n):
 A=[[F(i==j) for j in range(n)] for i in range(n)]
 for s,i,j in X:
  ts=t**s; A[i][i+1]-=ts; A[i][j+1]-=1-ts; A[j][j+1]-=1
 return A

def calc(X,rot,t1,t2, omit=False):
 t1,t2=F(t1),F(t2); t3=t1*t2; ts=[None,t1,t2,t3];n=len(rot)
 power=-(sum(rot)+sum(s for s,i,j in X))
 if power%2:raise ValueError('nonintegral delta power')
 A=[None]+[mat(ts[k],X,n) for k in (1,2,3)]
 d=[None]+[ts[k]**(power//2)*det(A[k]) for k in (1,2,3)]
 g=[None]+[inverse(A[k]) for k in (1,2,3)]
 val=F(0)
 for s,i,j in X:
  u=t1**s;v=t2**s;w=t3**s
  F1=s*(F(1,2)-g[3][i][i]+v*g[1][i][i]*g[2][j][i]-v*g[3][j][j]*g[2][j][i]-(v-1)*g[3][i][i]*g[2][j][i]+(w-1)*g[2][j][i]*g[3][j][i]-g[1][i][i]*g[2][j][j]+2*g[3][i][i]*g[2][j][j]+g[1][i][i]*g[3][j][j]-g[2][i][i]*g[3][j][j])
  F1+=s/(v-1)*((u-1)*v*(g[3][j][j]*g[1][j][i]-g[2][j][j]*g[1][j][i]+v*g[1][j][i]*g[2][j][i])+(w-1)*g[3][j][i]*(1-v*g[1][i][i]+g[2][i][j]+(v-2)*g[2][j][j]-(u-1)*(v+1)*g[1][j][i]))
  val+=F1
 for s0,i0,j0 in X:
  for s1,i1,j1 in X:
   q=s1*(t1**s0-1)*(t3**s1-1)*g[1][j1][i0]*g[3][j0][i1]/(t2**s1-1)
   val+=q*(t2**s0*g[2][i1][i0]+g[2][j1][j0]-t2**s0*g[2][j1][i0]-g[2][i1][j0])
 for k,p in enumerate(rot):val+=(g[3][k][k]-F(1,2))*p
 return val*d[1]*d[2]*d[3],d[1]

def expected(s,t):
 return (s**4*t**4-s**4*t**3-s**3*t**4+s**4*t**2+s**2*t**4-s**3*t-s*t**3+s**2+t**2-s-t+1)/(s**2*t**2)
def conj(x):return [(-s,j,i) for s,i,j in x]
def text(x):return str(x)
X=[(1,0,3),(1,4,1),(1,2,5)];rot=[0,0,0,-1,0,0,0]
M=conj(X);C=X[:];s,i,j=C[0];C[0]=(-s,j,i)
pts=[(F(2),F(3)),(F(3),F(2)),(F(1,2),F(2))]
print('BEGIN PUBLISHED TREFOIL CONTROLS')
for t1,t2 in pts:
 k,d=calc(X,rot,t1,t2);m,dm=calc(M,rot,t1,t2);c,dc=calc(C,rot,t1,t2);want=expected(t1,t2)
 print(json.dumps({'t1':text(t1),'t2':text(t2),'theta':text(k),'target':text(want),'benchmark_pass':k==want,'mirror_theta':text(m),'mirror_negation':m==-k,'crossing_switch':text(c),'crossing_switch_zero':c==0,'alexander':text(d),'alexander_mirror':text(dm),'mutant_inverted_rejected':-k!=want}))
Y=[(1,2*k,(2*k+7)%14) for k in range(7)];rot7=[0]*15;rot7[7]=-1
print('BEGIN INFERRED 7-CROSSING PROJECTION (IDENTITY UNVERIFIED)')
for t1,t2 in pts:
 k,d=calc(Y,rot7,t1,t2); m,dm=calc(conj(Y),rot7,t1,t2)
 delta=t1**3-t1**2+t1-1+t1**-1-t1**-2+t1**-3
 print(json.dumps({'t1':text(t1),'t2':text(t2),'theta':text(k),'mirror_theta':text(m),'mirror_negation':m==-k,'alexander':text(d),'alexander_target':text(delta),'alexander_pass':d==delta,'mirror_alexander':text(dm)}))
