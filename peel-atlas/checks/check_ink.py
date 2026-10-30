import numpy as np, itertools, math
def boost(ax,d):
    B=np.eye(4); c,s=math.cosh(d),math.sinh(d)
    B[0,0]=B[ax,ax]=c; B[0,ax]=B[ax,0]=s; return B
def dist(M): return math.acosh(M[0,0])  # distance origin -> M(origin)
for L in (math.log(5),math.log(7)):
    print("L",round(L,4),"straight",round(3*L,4))
    res={}
    for seq in itertools.product([1,2,3],repeat=3):
        M=np.eye(4)
        for a in seq: M=M@boost(a,L)
        res[seq]=round(dist(M),4)
    for k,v in sorted(res.items(),key=lambda x:x[1]): print(k,v,round(3*L-v,4))
print("tanh .44",math.tanh(.44),"e^.44",math.exp(.44))
print("(5-1)/(5+1)",4/6,"tanh(ln5/2)",math.tanh(math.log(5)/2))
