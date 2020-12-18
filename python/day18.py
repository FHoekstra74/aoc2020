def calculate (expression,advanced):
    while '(' in expression:
        start,end = 0,0
        for pos, c in enumerate(expression):
            if c == "(": start=pos
            elif c == ")":
                end=pos
                break
        part=expression[start+1:end]
        result = str(calculate(part,advanced))
        expression=expression.replace('(' + part+ ')', result)
    result,op,buffer=0,'',[]
    for i in [i for i in expression.split() if i != ' ']:
        if i == '+' or i == '*' : op=i
        else:
            if len(op)>0:
                if op == '+':result+=int(i)
                elif op == '*':
                     if advanced:
                        buffer.append(result)
                        result=int(i)
                     else: result*=int(i)
                op=''
            else: result=int(i)
    if advanced: 
        for i in buffer: result*=i
    return result
f,resulta,resultb=open('../input/day18.txt','r'),0,0
for line in f:
    resulta+=calculate(line.strip(),False)
    resultb+=calculate(line.strip(),True)
print(resulta)
print(resultb)
