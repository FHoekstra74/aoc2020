import copy
def run(instructions,mode):
    accumulator,pointer,i=0,0,set()
    while pointer not in i:
        i.add(pointer)
        instr=instructions[pointer]
        if instr[0] == 'nop': pointer += 1
        elif instr[0] == 'acc':
            accumulator += instr[1]
            pointer += 1
        elif instr[0] == 'jmp': pointer += instr[1]
        if pointer==len(instructions): return accumulator
    if mode==1: return accumulator
    else: return 0

f,changed,val,instructions = open("../input/day8.txt","r"),0,0,{}
for cnt,line in enumerate(f):
    instructions[cnt]=[line.strip().split(' ')[0],int(line.strip().split(' ')[1])]
print(f"a:{run(instructions,1)}")
while val == 0:
    instr,onechanged=copy.deepcopy(instructions),False
    while onechanged == False:    
        if instr[changed][0] == 'jmp' or instr[changed][0] == 'nop': 
            if instr[changed][0] == 'jmp': 
                instr[changed][0] = 'nop'
            else:
                instr[changed][0] = 'jmp'
            onechanged=True
        changed+=1
    val=run(instr,2)
    if val > 0 : print(f"b:{val}")
