lines=[int (line) for line in open("../input/day1.txt","r")]
for x in lines:
    for y in lines:
        if x + y == 2020: answerA = x * y
        for z in lines:
            if x + y + z == 2020: answerB = x * y * z
print (answerA, answerB)
