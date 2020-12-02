items=[list(int(e) for e in line.split()[0].split('-')) + [(line.split()[1][0])] + [(line.split()[2])]for line in open("../input/day2.txt","r")]
print(f"a:{len([pwd for min,max,c,pwd in items if pwd.count(c)>=min and pwd.count(c)<=max])} b:{len([pwd for min,max,c,pwd in items if (pwd[min-1]==c) != (pwd[max-1]==c)])}")
