import re
answera,answerb,i,passport,lines=0,0,0,{},[line.strip() for line in open("../input/day4.txt", "r")]
for i in range(0,len(lines)+1):
    if i == len(lines) or len(lines[i]) == 0:
        if {'byr','iyr','eyr','hgt','hcl','ecl','pid'} <= passport.keys():
            answera += 1
            if 1920 <= int(passport.get('byr')) <= 2002 and 2010 <= int(passport.get('iyr')) <= 2020 and 2020 <= int(passport.get('eyr')) <= 2030 and ((passport.get('hgt')[-2:] == 'cm' and (150 <= int(passport.get('hgt')[:-2]) <= 193)) or (passport.get('hgt')[-2:] == 'in' and (59 <= int(passport.get('hgt')[:-2]) <= 76))) and bool(re.match("^[#][a-f0-9]{6}$",passport.get('hcl'))) and passport.get('ecl') in ('amb','blu','brn','gry','grn','hzl','oth') and bool(re.match("^[0-9]{9}$",passport.get('pid'))): answerb += 1
        passport={}
    else:
        for j in lines[i].split(): passport.update({j.split(':')[0]:j.split(':')[1]})
print (f"{answera} {answerb}")
