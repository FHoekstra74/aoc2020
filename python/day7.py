lines,rules=[l.strip() for l in open ("../input/day7.txt","r")],{}
for line in [line.replace('bags','').replace('bag','') for line in lines]: rules.update({line.split("contain")[0].strip():[c.strip() for c in line.split('contain')[1].replace('.','').split(',')]})
bags,prev={"shiny gold"},0
while len(bags) != prev:
    prev=len(bags)
    for key,value in rules.items(): 
        if any([i for i in value if i.split(' ',1)[1] in bags]): bags.add(key)
print(f"a:{len(bags)-1}")
tocheck,answerb=['1 shiny gold'],0
while len(tocheck)>0:
    for bag in tocheck:
        for i in [i for i in rules[bag.split(' ',1)[1]] if i != 'no other']:
            count = int(i.split(' ',1)[0]) * int(bag.split(' ',1)[0])
            answerb+=count
            tocheck.append(str(count) + ' ' + i.split(' ',1)[1])
        tocheck.remove(bag)
print(f"b:{answerb}")
