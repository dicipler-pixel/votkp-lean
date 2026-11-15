# SCRIPT: CHK-08-NEVER-EXTEND (6_3, 7_5, 8_7, 8_8 and torus knots: any band hit for x in 1.0..3.0, 40 digits)
import importlib.util, sys
spec=importlib.util.spec_from_file_location('c7','/home/claude/harness2/eval/chk_07_riley_census.py'); c7=importlib.util.module_from_spec(spec); spec.loader.exec_module(c7)
xs=[round(1.0+0.02*i,2) for i in range(0,101)]
for nm in ('T(2,3)','T(2,5)','T(2,7)','6_3','7_5','8_7','8_8'):
    h=c7.scan(nm,xs); print(nm,"hits x in [1,3]:",len(h), (h[:2] if h else ''),flush=True)
