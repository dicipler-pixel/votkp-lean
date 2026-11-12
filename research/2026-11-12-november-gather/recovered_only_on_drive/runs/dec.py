import json,base64,sys,zipfile,io,os
src,name,out=sys.argv[1:4]
d=json.load(open(src))
b=base64.b64decode(d["content"])
os.makedirs(out,exist_ok=True)
open("/home/claude/nov/runs/raw/"+name,"wb").write(b)
z=zipfile.ZipFile(io.BytesIO(b))
z.extractall(out)
for i in z.infolist(): print(i.file_size,i.date_time,i.filename)
