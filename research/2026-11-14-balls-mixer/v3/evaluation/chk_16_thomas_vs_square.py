# SCRIPT: CHK-16-THOMAS-VS-SQUARE (Thomas angle of ONE product B_iB_j vs turn of the commutator square, several z)
import math
for z in (1.05,1.2,2,3,5,7):
    G2=((z-1)/(z+1))**2; th=2*math.atan(G2); g=(z-1)**2/(4*z); phi=(4*math.acos(g)) if g<1 else float("nan")  # turn per square (mod 360 folded below)
    print("z",z,"Thomas theta deg",round(math.degrees(th),4)," square turn phi deg",round(math.degrees(phi),4)," phi/theta",round(phi/th,4)," 1-cos(theta)=2G4/(1+G4)",round(1-math.cos(th),6),round(2*G2**2/(1+G2**2),6))
