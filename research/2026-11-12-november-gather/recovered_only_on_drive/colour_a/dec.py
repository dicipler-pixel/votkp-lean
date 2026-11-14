import sys,json,base64,re
src,dst=sys.argv[1],sys.argv[2]
raw=open(src).read()
try:
    d=json.loads(raw)
    b=d['content']
except Exception:
    m=re.search(r'"content"\s*:\s*"([A-Za-z0-9+/=\s]+)"',raw)
    b=m.group(1)
open(dst,'wb').write(base64.b64decode(b))
