def sumexists(preamble,val):
    for x in preamble:
        for y in preamble:
            if x!=y and (x+y) == val: return True
    return False

preamblecnt,answera,lines=25,0,[int(line.strip()) for line in open ('../input/day9.txt','r')]
for i in range(preamblecnt,len(lines)): 
    if not sumexists(lines[i-preamblecnt:i],lines[i] ): answera = (lines[i])
print(f"a:{answera}")
for i in range(0,len(lines)):
    setnrs,j=[],i+1
    setnrs.append(lines[i])
    while sum(setnrs) < answera:
        setnrs.append(lines[j])
        if sum(setnrs) == answera: print(f"b:{min(setnrs) + max(setnrs)}")
        j+=1
