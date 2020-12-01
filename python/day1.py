answerA,answerB=0,0
f = open("../input/day1.txt", "r")
lines=[int(line) for line in f]
f.close()
for x in lines:
    for y in lines:
        if x + y == 2020: answerA = x * y        
        for z in lines:
            if x + y + z == 2020: answerB = x * y * z
print ("AnswerA: " , answerA)
print ("AnswerB: " , answerB)
