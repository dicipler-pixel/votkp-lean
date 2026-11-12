import json
Y=[(1,2*k,(2*k+7)%14) for k in range(7)]; rot=[0]*15;rot[7]=-1
trace=[None]*14
for idx,(sign,i,j) in enumerate(Y):
 assert trace[i] is None and trace[j] is None
 trace[i]=(idx,'O',sign);trace[j]=(idx,'U',sign)
labels=[x[0] for x in trace];kind=''.join(x[1] for x in trace)
print(json.dumps({'labels':labels,'first_half_distinct':len(set(labels[:7]))==7,'repeat_second_half':labels[:7]==labels[7:],'over_under':kind,'alternating':all(kind[i]!=kind[i+1] for i in range(13)),'all_positive':all(x[2]==1 for x in trace),'one_negative_rotation':rot.count(-1)==1 and rot.count(0)==14}))
