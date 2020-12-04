import re
def allrequired(passport):
    return {'byr','iyr','eyr','hgt','hcl','ecl','pid'} <= passport.keys()
def validyear(year,min,max):
    return int(year)>=min and int(year)<=max
def validheight(height):
    res=False
    if height[-2:]=='cm':
        res=height[:-2].isnumeric() and int(height[:-2]) >= 150 and int(height[:-2]) <= 193
    if height[-2:]=='in':
        res=height[:-2].isnumeric() and int(height[:-2]) >= 59 and int(height[:-2]) <= 76
    return res

answera,answerb,lst,passport,f=0,0,[],{},open("../input/day4.txt", "r")
for l in f:
    if len(l.strip()) == 0:
        if len(passport)>0:
            lst.append(passport)
            passport={}
    else:
        for i in l.strip().split(): passport.update({i.split(':')[0]:i.split(':')[1]})
lst.append(passport)
for passport in lst:
    if allrequired(passport):
        answera+=1
        if validyear(passport.get('byr'),1920,2002) and \
           validyear(passport.get('iyr'),2010,2020) and \
           validyear(passport.get('eyr'),2020,2030) and \
           validheight(passport.get('hgt')) and \
           bool(re.match("^[#][a-f0-9]{6}$",passport.get('hcl'))) and \
           passport.get('ecl') in ('amb','blu','brn','gry','grn','hzl','oth') and \
           bool(re.match("^[0-9]{9}$",passport.get('pid'))):
            answerb+=1
print (f"{answera} {answerb}")
