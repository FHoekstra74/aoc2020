def traverse(coor,xstep,ystep,maxx,maxy):
    val,xpos,ypos=0,0,0
    while ypos<=maxy:
        if (xpos,ypos) in coor: val+=1
        ypos+=ystep
        xpos=xstep-(maxx-xpos+1) if xpos>(maxx-xstep) else xpos+xstep
    return val
f,coor,answerb = open("../input/day3.txt", "r"),[],1
for y,l in enumerate(f):
    for x,c in enumerate(l.strip()): 
        if c == '#': coor.append((x,y))
print(traverse(coor,3,1,x,y))
for vector in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
    answerb*=traverse(coor,vector[0],vector[1],x,y)
print(answerb)
