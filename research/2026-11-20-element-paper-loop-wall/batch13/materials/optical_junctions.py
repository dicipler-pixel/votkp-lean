"""Scalar optical boundary comparators for the batch 13 predeclared energies."""
import argparse
import cmath
import csv
import re
from fractions import Fraction as F
from itertools import combinations_with_replacement
from pathlib import Path
from urllib.request import urlopen

HERE = Path(__file__).resolve().parent
SYMS = ("Sm","Gd","Tb")
ENERGIES = (F(2),F(5,2),F(3))
DOIS = {"2025":"10.1021/acs.jpcc.5c00770","2023":"10.1038/s41598-023-30770-1"}

def extract(cache):
    with (HERE/"optical_inputs.csv").open("w",newline="") as f:
        dest=csv.writer(f,lineterminator="\n")
        dest.writerow(["symbol","year","E_eV","n","kappa","epsilon_real","epsilon_imaginary","source","doi"])
        for sym in SYMS:
            url=f"https://micro.ustc.edu.cn/database/ELF/{sym}.html"
            page=(cache/f"elf{sym}.html").read_text() if cache else urlopen(url,timeout=60).read().decode()
            for block in page.split('<div class="citation">')[1:]:
                year,doi=next((y,d) for y,d in DOIS.items() if d in block.split("</div>")[0])
                tables=re.findall(r"<table\b[^>]*>(.*?)</table>",block,re.DOTALL)
                (table,)=[t for t in tables if "Energy loss (eV)" in t]
                count=0
                for row in re.findall("<tr>(.*?)</tr>",table,re.DOTALL):
                    cols=re.findall("<td>(.*?)</td>",row,re.DOTALL)
                    if cols and F(cols[0].strip()) in (*ENERGIES,F("2.4"),F("2.6")):
                        dest.writerow([sym,year,cols[0],*cols[2:],url,doi])
                        count+=1
                assert count==5,(year,sym,count)

def reflect(x,y):
    a,b=x
    c,d=y
    denom=(a+c)**2+(b+d)**2
    # r = (x-y)/(x+y); complex field convention fixed in the report.
    return ((a-c)*(a+c)+(b-d)*(b+d))/denom, ((b-d)*(a+c)-(a-c)*(b+d))/denom

def main():
    arg=argparse.ArgumentParser()
    arg.add_argument("--fetch",action="store_true")
    arg.add_argument("--cache",type=Path)
    args=arg.parse_args()
    if args.fetch or args.cache:
        extract(args.cache)
    inputs={}
    converted={}
    raw={}
    for r in csv.DictReader((HERE/"optical_inputs.csv").open()):
        n,k,er,ei=[F(r[name]) for name in ("n","kappa","epsilon_real","epsilon_imaginary")]
        key=(r["year"],F(r["E_eV"]),r["symbol"])
        raw[key]=n,k,er,ei
        inputs[key]=n,k
        w=cmath.sqrt(complex(float(er),float(ei)))
        converted[key]=w.real,w.imag
        if key[1] in (2,3):
            assert max(abs(n*n-k*k-er),abs(2*n*k-ei))<F("0.00005")
    for sym in SYMS:
        lo,mid,hi=[raw["2025",F(k),sym] for k in ("2.4","2.5","2.6")]
        resid=max(abs(y-(x+z)/2) for x,y,z in zip(lo,mid,hi))
        assert resid<=F("0.00001")
        print(sym,"2.5 eV tabulated-column midpoint residual",float(resid))
    with (HERE/"optical_junctions.csv").open("w",newline="") as f:
        out=csv.writer(f,lineterminator="\n")
        out.writerow(["Sm_source_year","E_eV","from","to","r_real","r_imag","modulus_squared","n_only_modulus_squared"])
        for year in ("2025","2023"):
            for energy in ENERGIES:
                result=[]
                alternate=[]
                for a,b in combinations_with_replacement(SYMS,2):
                    x=inputs[year if a=="Sm" else "2025",energy,a]
                    y=inputs[year if b=="Sm" else "2025",energy,b]
                    re_part,im_part=reflect(x,y)
                    reverse=reflect(y,x)
                    assert reverse==(-re_part,-im_part)
                    exact=re_part**2+im_part**2
                    n_only=((x[0]-y[0])/(x[0]+y[0]))**2
                    if a==b:
                        assert exact==0 and n_only==0
                    else:
                        result.append((a+b,exact,n_only))
                        ru,rv=reflect(converted[year if a=="Sm" else "2025",energy,a],
                                      converted[year if b=="Sm" else "2025",energy,b])
                        alternate.append((a+b,ru*ru+rv*rv))
                    out.writerow([year,float(energy),a,b,*[f"{float(v):.10f}" for v in (re_part,im_part,exact,n_only)]])
                ranks=[tuple(v[0] for v in sorted(result,key=lambda v:v[k])) for k in [1,2]]
                assert ranks[0]==tuple(t[0] for t in sorted(alternate,key=lambda v:v[1]))
                print(year,float(energy),"complex-index vs real-index rank (weakest to strongest)",*ranks)

if __name__=="__main__":
    main()
