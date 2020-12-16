f,valid,mode,answera,answerb,nearby,fields=open('../input/day16.txt','r'),set(),0,0,1,[],{}
for line in f:
    line=line.strip()
    if 'or' in line:
        t,values=line.split(':')[1].strip(),[]
        for t1 in t.split('or'):
            i=int(t1.split('-')[0])
            while i <= int(t1.split('-')[1]):
                valid.add(i)
                values.append(i)
                i+=1
        fields[line.split(':')[0]]=values
    elif 'your' in line: mode=1
    elif 'nearby' in line: mode=2
    elif len(line)>0:
        if mode==1: myticket=line
        else:
            ok=True
            for n in line.split(','):
                if int(n) not in valid: 
                    answera+=(int(n))
                    ok=False
            if ok: nearby.append(line)
print(f"a:{answera}")
options=[set() for _ in range(len(fields))]
for ticket in nearby:
    for index,val in enumerate(ticket.split(',')):
        possible=set()
        for field,therange in fields.items():
            if int(val) in therange: possible.add(field)
        if len(options[index]) == 0: options[index]=possible
        else: options[index]=options[index].intersection(possible)
real = [None for _ in range(len(fields))]
while None in real:
    delete=set()
    for index,fields in enumerate(options):
        if len(fields) == 1:
            for field in fields: pass
            real[index]=field
            delete.add(field)
    for field in delete:
        for i in range(len(options)):
            if field in options[i]:
                options[i].remove(field)
for index,value in enumerate(real):
    if "departure" in value:
        val=int(myticket.split(',')[index])
        answerb*=val
print(f"b:{answerb}")
