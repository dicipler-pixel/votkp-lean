# SCRIPT: CHECK-GPT-ELEMENTS-BATCH1-01
# Recompute every derived number in GPT batch 1 from the IE values it quotes.
import math
IE={'He':[24.587389011,54.4177655282],'Li':[5.391714996,75.6400970,122.45435913],
    'Be':[9.322699,18.21115,153.896205,217.71858459],'B':[8.298019,25.15483,37.93059,259.374379,340.2260225]}
for el,v in IE.items():
    for k in range(len(v)-1):
        z=v[k+1]/v[k]; r=math.log(z); g=(v[k+1]-v[k])/(v[k+1]+v[k])
        print(el,k+1,round(z,8),round(r,6),round(g,8),'tanh check',abs(math.tanh(r/2)-g)<1e-12)
Eh=27.211386246
for Z,el in [(2,'He'),(3,'Li'),(4,'Be'),(5,'B')]:
    H=IE[el][-1]; He=IE[el][-2]
    print(el,'S_Z',round((H-He)/(Z*Eh),6),'sigma_Z',round(Z-math.sqrt(2*He/Eh),6),'H-like vs Z^2/2 Eh',round(H/(Z*Z*Eh/2),6))
print('z_wall',(1+1/math.sqrt(2))/(1-1/math.sqrt(2)),3+2*math.sqrt(2))
f=lambda r,V:4*math.pi*r**3/(3*V)
print('B f .85',round(f(0.85,7.67112),5),'f .84',round(f(0.84,7.67112),5),'r crit (1/3)',round((7.67112/(4*math.pi))**(1/3),4))
fl=f(1.33,21.5808); print('Li f',round(fl,5),'z',round(1/fl,5),'G',round((1/fl-1)/(1/fl+1),5))
fb=f(1.02,8.08925); print('Be f',round(fb,5),'z',round(1/fb,5),'G',round((1/fb-1)/(1/fb+1),5))
a,c=2.2859,3.5844; print('Be d_perp',round(math.sqrt(a*a/3+c*c/4),4))
print('Li bcc d',round(math.sqrt(3)*3.5093/2,4),'fcc d',round(4.404/math.sqrt(2),4))
print('B4 ratio vs Li2 and phi',1.618908-1.6180339887,'Be3 vs sqrt2',1.414711-math.sqrt(2))
# H2 ideal gas volume per H atom at 298.15K, 1 bar
kT=1.380649e-23*298.15; Vmol=kT/1e5; print('vol per H atom A^3',round(Vmol/2*1e30,1),'f',(4*math.pi/3*0.32**3)/(Vmol/2*1e30))
# shell-only ratio n=2->1 hydrogenic: Z_eff same -> (1/1)/(1/4)=4 -> Gamma 3/5
print('Gamma for z=4',(4-1)/(4+1))
