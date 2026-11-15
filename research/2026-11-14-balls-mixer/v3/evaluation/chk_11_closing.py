# SCRIPT: CHK-11-CLOSING (equal-step words to depth 5: distinct points and smallest distance; control closing step and z=3,5,6,7)
import numpy as np, math
def boost(u,r):
    u=np.array(u,float); c,s=math.cosh(r),math.sinh(r); B=np.zeros((4,4)); B[0,0]=c; B[0,1:]=s*u; B[1:,0]=s*u
    B[1:,1:]=np.eye(3)+(c-1)*np.outer(u,u); return B
def run(z,depth=5):
    r=math.log(z); gens=[]
    for a in range(3):
        u=[0,0,0]; u[a]=1; gens+= [boost(u,r), boost([-x for x in u],r)]
    o=np.array([1.,0,0,0]); pts={tuple(np.round(o[1:]/(1+o[0]),7)):o}
    front=[(np.eye(4),-1)]; words=1
    for d in range(1,depth+1):
        nf=[]
        for M,last in front:
            for k in range(6):
                if last>=0 and (k^1)==last: continue
                M2=M@gens[k]; p=M2@o; words+=1
                key=tuple(np.round(p[1:]/(1+p[0]),7)); pts.setdefault(key,p); nf.append((M2,k))
        front=nf
    P=np.array(list(pts.values())); 
    G=P[:,0][:,None]*P[:,0][None,:]-P[:,1:]@P[:,1:].T
    np.fill_diagonal(G,np.inf); m=math.acosh(max(1,G.min()))
    return len(P),words,m
for name,z in [("closing n=5",(math.sqrt(math.cos(2*math.pi/5))+math.sqrt(1+math.cos(2*math.pi/5)))**2),("closing n=6",2+math.sqrt(3)),("z=3",3),("z=5",5),("z=6",6),("line 3+2sqrt2",3+2*math.sqrt(2)),("z=7",7)]:
    n,w,m=run(z); print(name,"z",round(z,6),"distinct",n,"words",w,"min dist",round(m,6),"ln z",round(math.log(z),6),"closed" if (m>math.log(z)-1e-6 and n<w) else ("holds(no closure)" if m>math.log(z)-1e-6 else "falls"))
