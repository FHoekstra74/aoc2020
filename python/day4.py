import re
def validheight(height):
    if height[-2:]=='cm': return height[:-2].isnumeric() and int(height[:-2]) >= 150 and int(height[:-2]) <= 193
    elif height[-2:]=='in': return height[:-2].isnumeric() and int(height[:-2]) >= 59 and int(height[:-2]) <= 76
    else: return False

answera,answerb,i,passport,lines=0,0,0,{},[line.strip() for line in open("../input/day4.txt", "r")]
while i<=len(lines):
    if i==len(lines) or len(lines[i]) == 0:
        if {'byr','iyr','eyr','hgt','hcl','ecl','pid'} <= passport.keys():
            answera+=1
            if 1920 <= int(passport.get('byr')) <= 2002 and \
               2010 <= int(passport.get('iyr')) <= 2020 and \
               2020 <= int(passport.get('eyr')) <= 2030 and \
               validheight(passport.get('hgt')) and \
               bool(re.match("^[#][a-f0-9]{6}$",passport.get('hcl'))) and \
               passport.get('ecl') in ('amb','blu','brn','gry','grn','hzl','oth') and \
               bool(re.match("^[0-9]{9}$",passport.get('pid'))):
                answerb+=1
        passport={}
    else:
        for j in lines[i].split(): passport.update({j.split(':')[0]:j.split(':')[1]})
    i+=1
print (f"{answera} {answerb}")
