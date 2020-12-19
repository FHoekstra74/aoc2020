def check(message, rule):
    if len(rule)==0: return len(message)==0
    itm=rule[0]
    current = rules[itm]
    rule.remove(itm)
    if not type(current) is list:
        return len(message) > 0 and message[0] == current and check(message[1:],rule)
    else: 
        oneok=False
        for next in current:
            if check(message,next+rule): oneok=True
        return oneok

f,rules,messages = open('../input/day19.txt','r'),{},[]
for line in f:
    if ':' in line:
        name, subrules = line.split(": ")
        for sub in subrules.split(' | '):
            if any([t for t in sub if t.isnumeric()]):
                tmp=[]
                for part in sub.split():
                    tmp.append(int(part))
                if not int(name) in rules: rules[int(name)]=[]   
                rules[int(name)].append(tmp)
            else:
                rules[int(name)]=str(sub.strip()[1])
    else:
        if len(line.strip())>0: messages.append(line.strip())
answera,answerb=0,0
for m in messages:
    if check(m,[0]): answera+=1
print(answera)
rules[8]=[[42],[42,8]]
rules[11]=[[42,31],[42,11,31]]
for m in messages:
    if check(m,[0]): answerb+=1
print(answerb)

