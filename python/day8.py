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
f,changed,val,instructions,oldp,oldval = open("../input/day8.txt","r"),0,0,{},0,''
for cnt,line in enumerate(f):
    instructions[cnt]=[line.strip().split(' ')[0],int(line.strip().split(' ')[1])]
print(f"a:{run(instructions,1)}")
while val == 0:
    onechanged=False
    while onechanged == False:    
        if instructions[changed][0] == 'jmp' or instructions[changed][0] == 'nop': 
            oldp,oldval,onechanged=changed,instructions[changed][0],True
            instructions[changed][0] = 'nop' if instructions[changed][0] == 'jmp' else 'jmp'
        changed+=1
    val=run(instructions,2)
    if val > 0 : print(f"b:{val}")
    else: instructions[oldp][0]=oldval
