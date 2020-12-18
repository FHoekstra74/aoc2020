def calculate (expression,advanced):
    while '(' in expression:
        buffer,parentheses,i,j = [],[],0,0
        for i, c in enumerate(expression):
            if c == "(": buffer.append(i)
            elif c == ")":
                start = buffer.pop()
                parentheses.append((start, i))
        for item in parentheses:
            if item[1]-item[0] > j-i: i,j=item
        part=expression[i+1:j]
        result = str(calculate(part,advanced))
        expression=expression.replace('(' + part+ ')', result)
    result,op,buffer=0,'',[]
    for i in [i for i in expression.split() if not i is ' ']:
        if i is '+' or i is '*' : op=i
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
