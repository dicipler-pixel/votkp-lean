import base64,sys
name=sys.argv[1]
s=sys.stdin.read().strip().replace('\\u003d','=')
s+= '='*(-len(s)%4)
open(name,'wb').write(base64.b64decode(s))
print(name,len(base64.b64decode(s)))
