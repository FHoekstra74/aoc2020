def run(instructions,mode):
    accumulator,pointer,i=0,0,set()
    while pointer not in i:
        i.add(pointer)
        instr = instructions[pointer]
        if instr[0] == 'nop' or instr[0] == 'acc' : pointer += 1
        if instr[0] == 'acc': accumulator += instr[1]
        if instr[0] == 'jmp': pointer += instr[1]
        if pointer == len(instructions): return accumulator
    return accumulator if mode == 1 else 0
f,changepointer,val,instructions,oldval,onechanged = open("../input/day8.txt","r"),0,0,{},'',False
for cnt,line in enumerate(f): instructions[cnt]=[line.strip().split(' ')[0],int(line.strip().split(' ')[1])]
print(f"a:{run(instructions,1)}")
while val == 0:
    while not onechanged:    
        if instructions[changepointer][0] == 'jmp' or instructions[changepointer][0] == 'nop': 
            oldval,onechanged=instructions[changepointer][0],True
            instructions[changepointer][0] = 'nop' if instructions[changepointer][0] == 'jmp' else 'jmp'
        changepointer += 1
    val=run(instructions,2)
    if val > 0 : print(f"b:{val}")
    else: instructions[changepointer-1][0],onechanged=oldval,False
