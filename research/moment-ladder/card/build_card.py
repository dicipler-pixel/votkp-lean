# SCRIPT: MOMENT-LADDER-CARD-BUILD-01   usage: python3 build_card.py card_body.html three.min.js out.html
import sys
body=open(sys.argv[1]).read(); three=open(sys.argv[2]).read()
assert body.count('<!--THREE-->')==1
open(sys.argv[3],'w').write(body.replace('<!--THREE-->','<script>'+three+'</script>'))
print('written',sys.argv[3],len(body)+len(three))
