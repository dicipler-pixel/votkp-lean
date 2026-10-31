# SCRIPT: MKGENS
# Writes generator files for relation_search.c.  Each letter: scale D, then 16 integers (row-major) Q, with B = Q/D.
# Letter order: for axis a in axes: (+boost, -boost); letter 2m and 2m+1 are inverses.
import sys
def boost(z, a, sgn):
    # Q = 2z*B, integer entries; B_u: cosh=(z^2+1)/(2z), sinh=sgn*(z^2-1)/(2z) on (t,axis) block, 1 on other two diagonals
    Q = [[0]*4 for _ in range(4)]
    for i in range(1,4):
        Q[i][i] = 2*z
    Q[0][0] = z*z+1
    Q[a][a] = z*z+1
    Q[0][a] = sgn*(z*z-1)
    Q[a][0] = sgn*(z*z-1)
    return Q
def write(fname, mats, D):
    with open(fname,'w') as f:
        f.write(str(len(mats))+"\n")
        for Q,d in mats:
            f.write(str(d)+" "+" ".join(str(Q[i][j]) for i in range(4) for j in range(4))+"\n")
if __name__=="__main__":
    for z in (1,2,4,8,16):
        for name,axes in (("full",(1,2,3)),("planar",(1,2))):
            mats=[]
            for a in axes:
                mats.append((boost(z,a,1),2*z)); mats.append((boost(z,a,-1),2*z))
            write("gens_z%d_%s.txt"%(z,name),mats,2*z)
    # positive control: letters B_i(2), B_i(2)^-1, B_i(4), B_i(4)^-1  (relation  b = a a ) plus B_j(2)
    mats=[(boost(2,1,1),4),(boost(2,1,-1),4),(boost(4,1,1),8),(boost(4,1,-1),8),(boost(2,2,1),4),(boost(2,2,-1),4)]
    write("gens_ctrl.txt",mats,0)
