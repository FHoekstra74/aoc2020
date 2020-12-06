lsta,lstb,answera,answerb,lines=[],[],0,0,[l.strip() for l in open ("../input/day6.txt","r")]
for i in range(0,len(lines) + 1):
    if i == len(lines) or len(lines[i]) == 0:
        answerb += len((set.intersection(*lstb)))
        answera += len(set(lsta))
        lsta,lstb=[],[]
    else:
        lstb.append(set(lines[i]))
        for c in lines[i]: lsta.append(c)
print(f"a:{answera} b:{answerb}")
