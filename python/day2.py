f = open("../input/day2.txt","r")
answerA,answerB=0,0
for line in f:
    t=line.split()
    min,max=tuple(int(e) for e in t[0].split('-'))
    c=t[1][0]
    if t[2].count(c)>=min and t[2].count(c)<=max: answerA+=1
    if (t[2][min-1] == c and t[2][max-1] != c) or (t[2][max-1] == c and t[2][min-1] != c) : answerB+=1
f.close()
print(answerA, answerB)
