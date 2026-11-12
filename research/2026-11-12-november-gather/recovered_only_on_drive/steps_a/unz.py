import json,base64,sys,zipfile,io,os
src,name=sys.argv[1],sys.argv[2]
d=json.load(open(src))
b=base64.b64decode(d['content'])
os.makedirs('/home/claude/nov/steps_a/unz',exist_ok=True)
open('/home/claude/nov/steps_a/raw/'+name,'wb').write(b)
z=zipfile.ZipFile(io.BytesIO(b))
out='/home/claude/nov/steps_a/unz/'+name[:-4]
z.extractall(out)
for i in z.infolist(): print(i.file_size,i.filename)
